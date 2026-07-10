# Market Finder Harvestor: Architecture Documentation

**The traditional artifact.** This is the static, written documentation of the Market Finder data-harvesting pipeline: a C4 model (Context, Container, Component), a dynamic flow diagram, and the prose that explains them. It exists to be the *control* in an experiment. The companion video explains the same system; this document is what we measure it against.

Everything here is drawn from the implemented code in `markets_app/harvestor` and the design in `docs/plans/harvestor-phase-c.md`, not an idealized version.

---

## 1. What the system is, in one paragraph

The harvestor turns a farmers-market website into proposed database rows that a human approves before they ever touch live data. It scrapes a site to markdown (Firecrawl), extracts structured JSON with Claude tool-use, geocodes the address (US Census), and drops timestamped JSON into a git-tracked audit trail. A loader validates and de-duplicates that JSON, then stages it into an `extraction_reviews` table, **not** the live `markets`/`vendors` tables. An operator works a side-by-side diff queue, accepting or overriding each field. Only on approval does the data go live, and human-edited fields are marked "sticky" so the next crawl can't clobber them. Every approval records a per-field decision, and those decisions roll up into a quality score that shows whether extraction is getting more accurate over time.

The shape that matters: **AI proposes, a human disposes, and the disposition is measured.** It is neither a naive one-shot scrape nor a fully manual data-entry job. It is a loop with a memory.

---

## 2. C4 Level 1: System Context

Who uses the system and what it depends on.

![System Context for the Market Finder Harvestor. The public shopper sits at the top and the operator on the right; both interact with the central Market Finder system, which connects down to a row of external systems along the bottom: market websites, the Philadelphia ArcGIS feed, Firecrawl, Anthropic Claude, and the US Census Geocoder.](harvestor-context.svg)

**The two human roles are different on purpose.** The shopper consumes finished data. The operator sits *inside* the production loop: the system is designed around the operator's review action as a first-class step, not an afterthought. That single design decision is most of the story.

---

## 3. C4 Level 2: Container

The runnable pieces and where they live. Note the hard split between the **local** harvestor (never deployed) and the **deployed** app.

![Container view of the Market Finder Harvestor. The operator works the deployed Next.js app on the right. On the left, a local laptop runs the harvestor CLI, which writes a git-tracked drop-zone and stages pending reviews into Postgres, and calls the external systems collected along the bottom: Firecrawl, Anthropic Claude, US Census, and the Philadelphia ArcGIS feed.](harvestor-container.svg)

**Why the boundary is load-bearing.** The harvestor's heavy, paid, slow dependencies (Firecrawl, the Anthropic SDK) live entirely on the laptop, outside Vercel's 60-second function limit and outside the deployed dependency tree. The only thing the local tier writes to the cloud is *pending* review rows. The deployed app is the only writer to live `markets`/`vendors`, and it only writes on an explicit human approval. The drop-zone is the seam between them: a git-tracked pile of JSON that lets any stage be replayed without re-spending on the previous one.

---

## 4. C4 Level 3: Component (inside the harvestor CLI)

The internals of the local pipeline. Four stages over a shared library, plus the single bridge into the app.

![Component view of the harvestor CLI internals. cli.ts dispatches to a four-stage pipeline (scrape, extract, enrich, load). The stages call the external services at the top, read and write the git-tracked drop-zone, and rest on a shared lib. The load stage hands off through adapter/review into Postgres extraction_reviews, and a read-only metrics component scores quality.](harvestor-component.svg)

*(The `phila/*` two-pass driver is omitted from this diagram for clarity; see Section 7.)*

**The one detail people miss:** the orchestrator (`harvestor <url>`) runs scrape → extract → enrich and then *stops*. It does not auto-load. A human is meant to open the `extracted.json` and eyeball it before anything is staged for review. There are two human gates, not one: the eyeball before staging, and the approve in the queue.

**`lib/tools` is the quiet hero.** The same zod schema generates Claude's tool `input_schema` *and* validates the loader's output. One contract, two enforcement points. When the schema changes, both sides move together, and `PROMPT_VERSION` gets bumped so the quality trend doesn't silently average two different extraction approaches.

---

## 5. Dynamic view: the end-to-end flow

What actually happens to one market's data, from URL to live row, including the feedback the system keeps.

![Data flow for one market, from URL to live row. The top row runs left to right (harvestor url, scrape, extract and geocode, drop-zone), drops to the bottom row running right to left (load, extraction_reviews pending, admin diff queue, approve to live), and an amber feedback arrow closes the loop back to the start. Two human gates are marked: eyeballing the JSON before load, and approving in the queue.](harvestor-flow.svg)

---

## 6. The four mechanisms that make it a loop, not a pipe

A pipe runs left to right and forgets. This system has four features that bend it into a loop.

**6.1 The replay boundary (the drop-zone).** Every stage reads from and writes to a git-tracked folder, `drop-zone/<market-slug>/<ts>.<stage>.<ext>`. A bad load re-runs `load` against the same `extracted.json`. No re-scrape, no re-extract, no API spend. The expensive, non-deterministic steps (Firecrawl, Claude) happen once and are frozen on disk. Everything downstream is replayable and free. This is what makes iterating on the loader or the dedup thresholds cheap.

**6.2 The review gate (`extraction_reviews`).** The loader never writes live tables. It writes proposed payloads into a polymorphic staging table with the matched live row snapshotted alongside, so the operator sees a true diff. The table is idempotent on the source key: re-running `load` updates the one open pending review instead of stacking duplicates. Nothing the AI produces is "live" until a human says so.

**6.3 Sticky fields (human edits win).** When the operator overrides a field (or edits a row directly in admin CRUD), that column is marked sticky on the live row. On the next monthly crawl, the upsert-core drops every sticky column from its update clause. The precedence is strict: **sticky human edit > admin review override > extracted value.** This is the mechanism that lets you re-crawl forever without the machine quietly undoing human corrections. Without it, every re-run would be a fight between the operator and the scraper.

**6.4 The quality score (the memory).** Every approval records a per-field `field_decisions` entry: `accepted`, `overridden`, or `unchanged-from-current`. Those roll up into a clean-extraction rate (approved with zero corrections), a field-level correction rate, and a reject rate, each broken down by entity type, source domain, and field, and trended over time by `extraction_prompt_version`. When the operator changes the prompt, the dashboard shows whether clean-extraction rate actually moved. The loop has a memory, and the memory is honest because there is no bulk-approve path that could skip per-field capture and inflate the score.

---

## 7. The Philadelphia two-pass (why one size didn't fit)

Not every source yields to the same tool, and the design admits it.

The phila.gov market finder is a client-side SPA: Firecrawl sees only a heading, never the market list. So **pass 1 doesn't go through the scraper at all.** It queries the public ArcGIS FeatureServer directly for clean, structured market core data (name, hours, address, payment flags, geometry), pinned to a stable `source_external_id = phila-arcgis-<objectid>`. **Pass 2** then runs the normal `scrape → extract → enrich → load` against each market's *own* website for vendors and products, bound back to the pass-1 market so a re-run never mints a duplicate. A weekly `pnpm phila refresh` re-pulls the feed and merges a hand-editable manifest, preserving operator-owned fields (`enabled`, `pass2Url`, `cluster`, `notes`) while refreshing feed-owned ones.

The lesson embedded in the code: the "AI scrape" is one tool among several, chosen per source, not a hammer for every nail. Structured feeds get queried; rendered sites get scraped; SPAs get neither.

---

## 8. Why this is the hard thing to document statically

Read sections 2 through 7 back. The structure (containers, components) sits still and photographs well. C4 diagrams are good at *things and their arrangement*. But the part that matters most is sections 5 and 6: **a flow with state, gates, and a feedback signal that changes behavior over time.** A static diagram of a loop has to freeze it at one instant and annotate the motion in prose. The reader has to animate it in their head: hold the drop-zone's replay property, the two human gates, the sticky-precedence rule, and the prompt-version trend all in working memory at once, and run them forward.

That is exactly the gap the companion video is meant to close, and exactly the comparison the article is about. This document is complete. The question the next two steps answer is whether "complete" is the same as "understood."

---

*Source of record: `markets_app/harvestor/README.md`, `markets_app/docs/plans/harvestor-phase-c.md`, `markets_app/docs/plans/phila-harvest-two-pass.md`. This documentation is the static-baseline artifact for the "video vs diagram" comparison; see `comparison.md` (Step 3) once the video exists.*

# Content Workspace

This is Aaron Held's content production workspace. It's the structured pipeline for moving an idea into a published blog post and its companion social posts on LinkedIn, Bluesky, and Threads.

The Hugo blog itself lives at the repo root (`config.yml`, `content/post/`, `layouts/`, etc.). This workspace is **upstream of** Hugo — it's where work-in-progress lives before it lands in `content/post/[slug]/index.md`.

## Current State

New workspace. No active project. The first piece written through this pipeline will exercise it end-to-end and surface what needs tuning.

## Architecture (ICM Layers)

This workspace uses **Information Context Management (ICM)** layering. Each file is annotated with its layer so you understand the architecture, not just the files.

- **L0 — Identity**: Who Aaron is as a writer. Voice, audience. Almost never changes.
- **L1 — Domain**: Recurring themes, signature moves, references. Evolves slowly.
- **L2 — Patterns**: Format patterns, platform requirements. Updated when external surfaces change.
- **L3 — Constraints**: Hard rules — what to always do or never do.
- **L4 — Active Work**: Stage folders. Per-piece, ephemeral, archived after publish.

## Structure Map

```
content-workspace/
├── CLAUDE.md             ← you are here (workspace entry point)
├── CONTEXT.md            ← stage map and routing
│
├── _config/              ← L0–L3 reference material (read by every stage)
│   ├── voice-and-tone.md         (L0)
│   ├── audience.md               (L0)
│   ├── themes.md                 (L1, living)
│   ├── signature-moves.md        (L1)
│   ├── recurring-references.md   (L1, seeded from existing posts)
│   ├── format-patterns.md        (L2)
│   ├── platforms.md              (L2, dated, re-checked annually)
│   └── constraints.md            (L3, hard rules)
│
├── 01_research/          ← L4: gather sources, find contrarian view
├── 02_outline/           ← L4: scope the post, lock hook + close
├── 03_draft/             ← L4: collaborative human-AI writing pass
├── 04_publish_amplify/   ← L4: blog → LinkedIn → back-link → Bluesky/Threads
│
├── feature-requests/     ← PRDs for blog features content surfaces a need for
└── _archive/             ← finished pieces' working files, foldered by slug
```

## How to Use

The pipeline runs **one stage at a time** with a checkpoint between each. Each stage produces an artifact you can feel done about — that's by design, to keep motivation high on multi-day pieces.

### Starting a new piece

1. Pick a working slug (e.g., `the-quiet-cost-of-rewrites`).
2. Create a folder by that slug inside `01_research/`. All artifacts for this piece live in `01_research/[slug]/`, `02_outline/[slug]/`, etc., until publish.
3. Tell Claude what you want to write about and which stage you're in. Claude reads the relevant `CONTEXT.md` and the `_config/` files, and works only within that stage.

### Stage flow

| Stage | Trigger | Output | Checkpoint |
|---|---|---|---|
| 01_research | "Let's research [idea]" | `sources.md`, `contrarian-view.md` | Did I find material that genuinely challenges my premise, not just supports it? |
| 02_outline | "Outline this" | `outline.md` (single) or `series.md` + `part-N-outline.md` | Can I draft this in one sitting (~1 hour)? Hook strong? Close earned? |
| 03_draft | "Let's draft" | `index.md`, `summary.md`, `social-hooks.md` | Sounds like me? Alt text on every image? Any blog-feature gaps captured as PRDs? |
| 04_publish_amplify | "Publish" | live URLs, PR self-review note | All surfaces live with bi-directional links? Retrospective in PR? |

### Per-stage rule

When working in a stage, Claude reads:
- `_config/` (all of it — that's reference material)
- The current stage's `CONTEXT.md`
- The current piece's working folder for that stage
- Output from any **earlier** stages of this piece (research feeds outline, outline feeds draft, etc.)

Claude does **not** skip ahead. Drafting doesn't start until the outline is signed off. Publishing doesn't start until the draft is signed off. The checkpoints are the whole point.

### Multi-part series (the exception)

Single posts are the default. If a piece really earns multi-part treatment, the outline stage produces a `series.md` (thesis, arc, planned ending, part count) plus one outline per part — each independently scoped to ~1 hour of drafting. The "is this really multi-part?" question gets asked explicitly before this branch is taken.

### Feature requests

If during drafting a piece would clearly be better with a blog feature that doesn't exist yet (e.g., in-place mermaid diagrams, footnote popovers), drop a PRD-style writeup into `feature-requests/[short-slug].md`. Each PRD is dated and links back to the post that surfaced the need. Over time this becomes the blog's roadmap, sourced from real friction.

### Archiving

After a piece is published and amplified, move its working folders into `_archive/[slug]/` so the active stage folders stay clean. The published post itself lives in `content/post/[slug]/index.md` (Hugo's domain) — only the working artifacts get archived here.

## Relationship to the Existing Hugo Repo

- **Hugo dev workflow** (build, deploy, infrastructure): see `/CLAUDE.md` at the repo root. This workspace doesn't touch any of that.
- **Published posts**: live in `/content/post/[slug]/index.md`. The 03_draft stage produces the file that ends up there.
- **Source-as-content**: this whole repo is public. Files in `content-workspace/` should be legible to a stranger reading the repo — they're functional infrastructure *and* implicit documentation of how the blog gets made.

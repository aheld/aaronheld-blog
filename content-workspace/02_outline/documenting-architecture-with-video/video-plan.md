# Video Plan — The Harvester, Moving

**Purpose**: the variable in the experiment. Same system as `01_research/documenting-architecture-with-video/harvestor-architecture.md`, explained as a ~4–5 minute animated video. The article (`outline.md`) then compares this against the static doc on effort and effectiveness.

**Workflow inheritance** (from the Private Link video, see [/post/making-the-azure-private-link-video/](/post/making-the-azure-private-link-video/)):
- Research before script. Already done: the static doc *is* the research. Every claim in the script must trace to it.
- No characters, no theater. Diagram-explainer visual language: the four existing SVGs are the base layers; motion is payload dots, gate highlights, color shifts, lines drawing on. This is also the honest accounting move: the video's cost is incremental on top of the diagrams, and the effort log says so.
- Remotion for production. Numbered/staged animation of a chain worked last time; the flow diagram here is the same shape of problem.
- Watch for drift. The goal is "transfer the runtime model of the loop," not "make a beautiful film about a scraper." Re-read this line halfway through production.

## The one-sentence goal

A viewer who knows nothing about the harvester can, five minutes later, explain why a re-crawl can't clobber a human's edit and why a bad load costs nothing to retry.

If the video achieves that and nothing else, it wins. Those two facts are the loop.

## Script beats (draft — tighten during production)

1. **Cold open (~15s).** The container diagram, static, exactly as it appears in the doc. Narrator: one-paragraph system statement ("AI proposes, a human disposes, and the disposition is measured"). Then: "This diagram is complete. Here's what it can't show you."
2. **Act 1 — the trip out (~45s).** A payload dot enters at `harvestor <url>`, travels scrape → extract → enrich on the component diagram. Drop-zone accumulates timestamped files as the dot passes; git-tracked badge on the folder. External services light up only when called (Firecrawl, Claude, Census).
3. **Act 2 — the stop (~45s).** The orchestrator halts after enrich. Nothing moves. Human gate #1: an eyeball icon on `extracted.json`. Then `load`: dot crosses into `extraction_reviews`, marked PENDING. Gate #2: the diff queue, approve. Only now does the dot touch live `markets`/`vendors`. Beat: "Two human gates, not one."
4. **Act 3 — the replay (~40s).** A loader bug (red flash). Re-run `load` only: the dot restarts from the drop-zone, not from the website. The expensive stages (Firecrawl, Claude) stay dark. Caption: "$0.00". The frozen artifacts on disk are the point.
5. **Act 4 — sticky fields (~45s).** Next month's crawl arrives with a changed value. The operator's earlier override sits on the live row with a sticky badge. The incoming update's arrow reaches the sticky column and stops, visibly dropped from the update clause. Precedence stack appears: sticky human edit > review override > extracted value. Beat: "You can re-crawl forever and the machine never undoes a human."
6. **Act 5 — the memory (~40s).** Approvals emit per-field decisions; they roll up into a trend line (clean-extraction rate). Prompt version bumps; the line is annotated; it moves. Beat: "The loop has a memory, and the memory is honest."
7. **Recap (~30s).** All four mechanisms restated as labels appearing over the flow diagram, then the full loop animates once, end to end, silent except for the closing line: "A pipe runs left to right and forgets. This is a loop with a memory."

Total narration target: ~600–700 words. If the script passes 800, something drifted.

## Anti-transience design (answers the Tversky critique in contrarian-view.md)

- End-of-video recap frame designed as a *pausable poster*: all four mechanisms visible at once.
- YouTube chapter markers per act, so the video is partially random-access.
- Description links the static doc as the pause-and-dwell companion; the video says out loud "the diagram is the reference, this is the tour."

## Production checklist

- [ ] Script final pass (trace every claim to the static doc)
- [ ] Remotion project setup (reuse Private Link project scaffolding if salvageable)
- [ ] SVGs imported as layered components (may need to split groups for animation)
- [ ] Narration: record Aaron / TTS decision — **Aaron to decide**
- [ ] Music/none decision (default: none or minimal)
- [ ] Render, captions, upload, chapters
- [ ] Log every session in `03_draft/documenting-architecture-with-video/effort-log.md` as we go — this is data for the article, not housekeeping

## Status (2026-07-12)

Built and narrated. The Remotion project lives at `~/Projects/content-production/03_production/output/harvester-video/` (same convention as `private-link-video`). Script at `~/Projects/content-production/02_script/output/draft-explainer-video-harvester.md`; timed transcript in the project's `VOICEOVER.md`. All 7 scenes implemented; the flow diagram was ported 1:1 from `harvestor-flow.svg` into an animatable component, and the cold open shows `harvestor-container.svg` untouched.

Cuts so far:
- `output-draft1.mp4`: silent, on-screen captions (2026-07-12).
- `output-draft2.mp4`: ElevenLabs narration (Brian, same voice as the Private Link video) on all 7 scenes, 4:30, verified audio levels (2026-07-12). **Current review candidate.**

## Open questions for Aaron

1. ~~Where does the Remotion project live?~~ Answered by convention: `content-production/03_production/output/harvester-video/`.
2. ~~Narration voice?~~ ElevenLabs (Brian) generated and wired in; swap to self-recorded later if the draft doesn't land.
3. Retroactive honest estimate of hours spent on the static doc + the four SVGs (needed for The Bill section).
4. Can we get one naive reader and one naive viewer (a colleague each) for the effectiveness section?
5. Review `output-draft2.mp4`: pacing sits narration-first with a few seconds of visual breathing room per scene; tighten scene durations if it feels slow.

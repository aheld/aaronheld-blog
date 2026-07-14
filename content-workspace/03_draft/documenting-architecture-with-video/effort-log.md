# Effort Log — Documenting Architecture with Video

Data source for "The Bill" section of the article. Log every working session on either artifact, as it happens. Round to quarter hours, count honestly (including false starts and revisions), and note out-of-pocket costs.

## Artifact A: static doc + diagrams (retroactive)

| Date | Activity | Hours | $ |
|---|---|---|---|
| 2026-06/07 | C4 SVGs + harvestor-architecture.md prose, AI-drafted from existing codebase documentation | ~1 (Aaron) | 0 |
| | **Total** | **~1 hr** | 0 |

## The real cost story (Aaron, 2026-07-13) — three layers, all three go in the article

1. **Marginal cost: a tie.** ~1 hour each, *this time*. The tie is real but conditional: it only holds because the harvester was already documented in the codebase (the doc AI-drafted from that), and because the Remotion video framework and the agentic diagram framework already existed. The video was generated from the static doc and its diagrams.
2. **Cold-start cost: not a tie.** From scratch, both take more, the video much more. Aaron's first Remotion videos took *days*. Undocumented code would also push the doc past an hour.
3. **Polish tax: not a tie, and it never amortizes.** Getting the video to YouTube-creator quality is ~a day or two, *every time*: an opening voiceover intro, screenshots of the tool in use woven in (which means re-cutting the video), tighter pacing. Text docs never pay this. Aaron deliberately did **not** pay it for this draft — the published video is the "good-enough explainer," and that restraint is on-theme, not a gap.

## Artifact B: video (log as we go)

| Date | Activity | Hours | $ |
|---|---|---|---|
| 2026-07-12 | Script drafting + trace-to-doc pass (Claude session, `02_script/output/draft-explainer-video-harvester.md` + `VOICEOVER.md`) | ~0.25 (wall clock) | 0 |
| 2026-07-12 | Remotion project setup + animation build, all 7 scenes (Claude session, `03_production/output/harvester-video/`) | ~0.75 (wall clock) | 0 |
| 2026-07-12 | Stills review + layout fixes + draft render (silent, captioned) | ~0.25 (wall clock) | 0 |
| 2026-07-12 | Narration: ElevenLabs (Brian, same voice as Private Link video), 7 scenes, ~3.5 min audio + wiring into scenes + re-render | ~0.25 (wall clock) | ElevenLabs credits (~3.7 min synthesized; coldopen generated twice) |
| | Aaron: review narrated cut, revision notes | | |
| | Revisions after review | | |
| | Final render, captions, chapters, upload | | |
| | **Total** | | |

*Accounting note: the 2026-07-12 rows are AI-assisted wall-clock time, not human drafting time. The article should report both framings honestly: what it cost Aaron in attention, and what the same build would cost done by hand (the Private Link video is the reference point for that).*

## Accounting caveats (state these in the article)

- The video reuses the four SVGs as base layers, so Artifact B's total is *incremental* on top of Artifact A. This is the most favorable accounting for video; from zero, video cost = A's diagram hours + B.
- The static doc was also the video's research phase (per the workflow from the Private Link video), so some of A's prose hours are doing double duty. Note it, don't double-count it.

## Effectiveness data points (if we get them)

| Person | Artifact | Asked to explain back | Notes / verbatim |
|---|---|---|---|
| | doc only | why can't a re-crawl clobber a human edit? why is a bad load free to retry? | |
| | video only | same two questions | |

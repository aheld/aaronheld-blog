# Content Workspace — Routing

This file is the routing table for the workspace. If `CLAUDE.md` is the "what is this," `CONTEXT.md` is the "where do I go for X."

## Stage Map

| Stage | Purpose | Inputs | Output Location | Done Looks Like |
|---|---|---|---|---|
| **01_research** | Gather sources (papers, posts, SciFi, quotes) and find a genuine contrarian view that challenges the premise | the idea + `_config/` | `01_research/[slug]/sources.md`, `01_research/[slug]/contrarian-view.md` | I have material that genuinely challenges my premise, not just supports it |
| **02_outline** | Pick content type, scope to one sitting (~1 hour drafting), lock hook and close | research output + `_config/format-patterns.md` | `02_outline/[slug]/outline.md` (single) or `02_outline/[slug]/series.md` + `part-N-outline.md` (multi-part exception) | One tight outline draftable in an hour, OR a justified series plan with a real ending |
| **03_draft** | Collaborative human-AI writing pass, section by section, in voice. Summary and social-impact statement written in this same pass | outline + `_config/` (all of it) | `03_draft/[slug]/index.md` (the post), `03_draft/[slug]/summary.md`, `03_draft/[slug]/social-hooks.md`, optional PRDs in `feature-requests/` | Sounds like me, alt text on every image, opening matches close, no AI tells |
| **04_publish_amplify** | Blog live → LinkedIn post → back-link blog → Bluesky/Threads, on optimized timing | finished draft + `_config/platforms.md` | post in `content/post/[slug]/index.md`, live LinkedIn/Bluesky/Threads URLs, PR self-review note | All surfaces live with bi-directional links; PR contains the retrospective |

## How Stages Connect

```
[idea] → 01_research → [checkpoint: contrarian view found?]
                    ↓
                02_outline → [checkpoint: scoped to 1 hour? hook strong?]
                    ↓
                03_draft → [checkpoint: voice match? alt text? feature gaps captured?]
                    ↓
            04_publish_amplify → [checkpoint: bi-directional links? PR retro written?]
                    ↓
                _archive/[slug]/
```

Each `↓` is a human checkpoint. Claude does not auto-flow between stages. Aaron triggers each next stage explicitly after reviewing the prior stage's artifact.

## Reference Material (`_config/`)

Every stage reads `_config/` as background. The files there are layered by ICM:

| File | Layer | Purpose |
|---|---|---|
| `voice-and-tone.md` | L0 | How Aaron sounds. Voice, sentence rhythm, what to avoid. |
| `audience.md` | L0 | Smart colleagues + younger folks. Assume competence, no talking-down. |
| `themes.md` | L1 | Recurring topics: social contract, middle-manager survival, historical parallels. Living list. |
| `signature-moves.md` | L1 | Reusable techniques (e.g., "nothing unprecedented" historical-parallel framing). |
| `recurring-references.md` | L1 | Authors, works, thinkers Aaron returns to. Seeded from existing posts. |
| `format-patterns.md` | L2 | Named patterns: quick-tip, tutorial, deep-dive, multi-part series. Word ranges, structure. |
| `platforms.md` | L2 | LinkedIn / Bluesky / Threads / blog SEO requirements. Dated, re-checked annually. |
| `constraints.md` | L3 | Hard rules: no em dashes, no AI hedging, image rights, accessibility, etc. |

## Working Folder Convention

For a piece with slug `the-quiet-cost-of-rewrites`, files live at:

```
01_research/the-quiet-cost-of-rewrites/sources.md
01_research/the-quiet-cost-of-rewrites/contrarian-view.md
02_outline/the-quiet-cost-of-rewrites/outline.md
03_draft/the-quiet-cost-of-rewrites/index.md          ← copied to content/post/[slug]/index.md at publish
03_draft/the-quiet-cost-of-rewrites/summary.md
03_draft/the-quiet-cost-of-rewrites/social-hooks.md
04_publish_amplify/the-quiet-cost-of-rewrites/checklist.md
04_publish_amplify/the-quiet-cost-of-rewrites/pr-retro.md
```

After publish, all of these move to `_archive/the-quiet-cost-of-rewrites/`.

## Reading Order for a Fresh Session

When Claude starts a session for a piece:

1. Read this `CONTEXT.md` (routing).
2. Read `_config/voice-and-tone.md` and `_config/audience.md` (always).
3. Read the current stage's `CONTEXT.md`.
4. Read the current piece's working folder for the current stage **and all earlier stages**.
5. Read `_config/` files relevant to the current stage (e.g., `format-patterns.md` for outline stage, `platforms.md` for publish stage).

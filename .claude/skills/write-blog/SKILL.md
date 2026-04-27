---
name: write-blog
description: Routes blog-writing requests through the content-workspace pipeline (research → outline → draft → publish). Does not write directly to content/post/.
model: sonnet
color: blue
---

# write-blog — Pipeline Router

This skill routes blog work through the **content-workspace pipeline**. It does **not** draft directly into `content/post/[slug]/index.md`. That destination is owned by the publish stage, not the writing stage.

If a previous version of this skill drafted directly into `content/post/`, that was wrong. The pipeline exists for a reason: research before drafting, checkpoints between stages, an artifact you can feel done about at every step.

## STOP — Read Before Drafting

Before you write a single section of prose, do these in order:

1. Read `content-workspace/CLAUDE.md` (workspace overview, ICM layers).
2. Read `content-workspace/CONTEXT.md` (stage routing table).
3. Read `content-workspace/_config/voice-and-tone.md` and `content-workspace/_config/audience.md` (always — these are L0 reference).
4. Identify which **stage** the user is in (see "Stage Detection" below).
5. Read the stage's `CONTEXT.md` if one exists (e.g., `content-workspace/01_research/CONTEXT.md`).
6. Read the piece's working folder for the current stage **and all earlier stages**.
7. Only now begin work, and only inside the current stage's folder.

If you find yourself about to create or edit `content/post/[slug]/index.md` from this skill, stop. That file is produced by the **publish** stage from a finished draft in `03_draft/[slug]/index.md`. Use the `publish-blog` skill for that.

## Stage Detection

Match the user's request to a stage. When in doubt, ask.

| User says | Stage | First artifact |
|---|---|---|
| "let's research [topic]", "find sources for...", "what's the contrarian take on..." | **01_research** | `01_research/[slug]/sources.md` + `contrarian-view.md` |
| "outline this", "let's scope the post", "lock the hook" | **02_outline** | `02_outline/[slug]/outline.md` |
| "let's draft", "write the post", "let's write a blog post about..." | **03_draft** (only if research + outline already exist) | `03_draft/[slug]/index.md` |
| "publish this", "let's ship it", "amplify on LinkedIn" | **04_publish_amplify** — hand off to `publish-blog` skill | `content/post/[slug]/index.md` + social posts |

**Critical:** "let's write a blog post about X" is **not** a request to start at 03_draft. It's a request to start the pipeline. If `01_research/[slug]/` and `02_outline/[slug]/` don't exist for this piece, begin at **01_research**, not at drafting.

You can compress earlier stages when the material genuinely supports it (e.g., the user already has external research from another workspace), but the artifacts still get written. Research that exists only in a chat transcript doesn't count — `sources.md` and `contrarian-view.md` are real files.

## Per-Stage Behavior

### 01_research

- Pick a slug. Create `content-workspace/01_research/[slug]/`.
- Produce `sources.md`: external links, notes, quotes, prior art, related Aaron posts found via `grep` over `content/post/`.
- Produce `contrarian-view.md`: the strongest version of the *opposing* argument or the most uncomfortable critique of Aaron's premise. The checkpoint is "did I find material that genuinely challenges the premise, not just supports it?"
- **Stop and ask Aaron to review before moving on.**

### 02_outline

- Read `01_research/[slug]/` artifacts. Read `_config/format-patterns.md`.
- Produce `02_outline/[slug]/outline.md` with: format pattern chosen, locked hook, locked close, section beats. The post must be draftable in ~1 hour.
- If this genuinely warrants a series (rare), produce `series.md` + `part-N-outline.md` and ask explicitly before branching.
- **Stop and ask Aaron to review before drafting.**

### 03_draft

- Read `_config/` (all of it), `01_research/[slug]/`, `02_outline/[slug]/`.
- Draft into `03_draft/[slug]/index.md` with Hugo front matter (`draft: true`). Also produce `summary.md` and `social-hooks.md` in the same pass.
- Section by section, with feedback at natural breakpoints. Don't write the whole post then ask.
- If a missing blog feature would make the post better (mermaid in markdown, footnote popovers, etc.), drop a PRD in `content-workspace/feature-requests/[short-slug].md`.
- **Stop and ask Aaron to review before publishing.**

### 04_publish_amplify

- Don't do this here. Hand off to the `publish-blog` skill. That skill copies `03_draft/[slug]/index.md` to `content/post/[slug]/index.md`, flips `draft: false`, commits, monitors deploy, then handles LinkedIn/Bluesky/Threads cross-posting per `_config/platforms.md`.
- After publish, working folders for this slug move to `content-workspace/_archive/[slug]/`.

## Voice and Style Reference

The voice/style detail that used to live in this file now lives in:

- `content-workspace/_config/voice-and-tone.md` (L0 — Aaron's voice)
- `content-workspace/_config/audience.md` (L0 — who he's writing for)
- `content-workspace/_config/signature-moves.md` (L1 — reusable techniques)
- `content-workspace/_config/constraints.md` (L3 — hard rules)
- `.claude/context/writing-style.md` (legacy — still useful, but `_config/` is canonical)

Read those at the stage where they apply. Don't duplicate them into this skill — drift between the two will mislead future sessions.

## Retrofitting an Out-of-Pipeline Draft

If a draft already exists at `content/post/[slug]/index.md` because a prior session skipped the pipeline (it happens), don't re-draft from scratch and don't pretend it doesn't exist. Retrofit:

1. Move `content/post/[slug]/` → `content-workspace/03_draft/[slug]/`. The Hugo build no longer sees it; the pipeline now does.
2. Create `01_research/[slug]/sources.md` and capture the actual research that informed the draft (links, source documents, prior art). Add a `contrarian-view.md` even retroactively — the discipline is worth more than the timing.
3. Create `02_outline/[slug]/outline.md` reverse-engineered from the existing draft: locked hook (the opening you have), locked close (the closing you have), section beats (the H2s you have). This sounds like make-work; it isn't. The retro-outline often surfaces a structural weakness the forward draft glossed over.
4. Re-enter the pipeline at **03_draft** with the existing `index.md` as the starting point. Iterate from there.

This is slower than continuing to edit in place. It's also the only way to make the pipeline mean something the next time around.

## Anti-Patterns (things this skill used to do)

- ❌ Drafting straight into `content/post/[slug]/index.md` with `draft: true`.
- ❌ Treating "write a blog post" as a 03_draft trigger when no research/outline artifacts exist.
- ❌ Duplicating voice-and-tone guidance into this skill (it drifts from `_config/`).
- ❌ Producing the whole draft in one pass without checkpoints.

If you catch yourself doing any of those, stop and route through the pipeline.

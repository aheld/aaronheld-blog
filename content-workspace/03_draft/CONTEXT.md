# Stage 3: Draft & Review

**ICM Layer**: L4 (active work). Per-piece, ephemeral, archived after publish.

## Purpose

Turn the outline into a finished post in Aaron's voice through collaborative human-AI writing — section by section, with feedback at section boundaries. Also produce two companion artifacts in the same pass: a summary and the raw social hooks that stage 4 will turn into platform posts.

This stage is **collaborative**, not generative. Claude proposes prose; Aaron drives. Every section pauses for feedback before the next one begins. The goal is a draft that sounds like Aaron wrote it, because in every meaningful sense, he did.

## Inputs

- `02_outline/[slug]/outline.md` (or `series.md` + `part-N-outline.md`) — must be checkpoint-approved.
- `01_research/[slug]/sources.md` and `contrarian-view.md`
- `_config/voice-and-tone.md` (read every section against this)
- `_config/audience.md`
- `_config/signature-moves.md`
- `_config/format-patterns.md` (the chosen pattern's structure rules)
- `_config/constraints.md` (hard rules — no em dashes, no AI hedging, image rights, accessibility, etc.)

## Process

1. **Confirm front matter.** Hugo YAML, `draft: true` to start. Title from outline. Date today. Description (1–2 sentences). Categories and tags pulled from `_config/themes.md` if applicable. Cover image filename committed even if image not yet sourced.

2. **Section-by-section drafting.** Work the outline top to bottom:
   - Draft one section in full.
   - Read it against `_config/voice-and-tone.md` and `_config/constraints.md`. Self-flag anything that sounds AI-tinted.
   - Hand back to Aaron. Wait for feedback. Revise. Move on.
   - Don't run ahead. The pause is what keeps the voice consistent.

3. **Image sourcing as you go.** From `_config/constraints.md`: prefer credited Unsplash photos or public-domain SF book covers. AI-generated images allowed where appropriate. Every image needs alt text — accessibility is a constraint, not a nice-to-have. Image filenames go in the front matter cover block and inline references.

4. **Capture feature gaps as PRDs.** If during drafting the post would clearly be better with a blog feature that doesn't exist (in-place mermaid diagrams, footnote popovers, embedded code playgrounds, etc.), drop a PRD writeup into `feature-requests/[short-feature-slug].md`. Don't break flow to actually build the feature — capture it and keep writing.

5. **Final voice pass.** Once the full draft is complete, read top to bottom for:
   - Opening matches close (does the close land the hook?)
   - Sentence rhythm varied (no long stretches of identical length)
   - No AI tells (see `_config/constraints.md`)
   - No marketing speak, no "delve," no "in conclusion"
   - The contrarian view from research lands somewhere in the post (per outline)
   - Every image has alt text

6. **Write the summary and social hooks in this same pass.** While the post is fresh:
   - `summary.md`: a 1–2 sentence summary suitable for the Hugo `description` field and a 3–4 sentence "impact statement" for cross-posting.
   - `social-hooks.md`: 3–5 candidate openings the LinkedIn post could lead with — different angles on the same piece. Stage 4 picks one.

7. **Pause for checkpoint.** Aaron reviews end-to-end. Don't move to publish until he signs off.

## Output Format

Files in `03_draft/[slug]/`:

### `index.md`

The post itself, in Hugo format. This is the file that gets copied to `content/post/[slug]/index.md` at publish time.

```markdown
---
title: "Post Title"
date: YYYY-MM-DDTHH:MM:SSZ
draft: true                     # flipped to false at publish
description: "1-2 sentence summary for SEO and social cards"
categories: ["..."]
tags: ["...", "..."]
cover:
  image: "filename.jpg"
  alt: "Descriptive alt text — accessibility is non-negotiable"
  caption: "Optional caption with attribution"
---

[Post body in Aaron's voice.]
```

### `summary.md`

```markdown
# Summary: [Post Title]

## SEO Description (1–2 sentences)

[The Hugo `description` field content.]

## Impact Statement (3–4 sentences)

[Why this post matters. What the reader walks away with. Used as cross-post connective tissue.]
```

### `social-hooks.md`

```markdown
# Social Hooks: [Post Title]

## Candidate openings for LinkedIn

### Hook 1: [angle name, e.g., "Personal observation"]
[1–3 sentences. Doesn't auto-generate from title — fresh angle for the platform.]

### Hook 2: [angle name, e.g., "Contrarian challenge"]
[1–3 sentences from a different angle.]

### Hook 3: [angle name]
[...]

## Notes for stage 4

- [Which hook feels strongest and why]
- [Any platform-specific considerations: too long for Bluesky? Threads-friendly?]
- [Whether this piece is part of a series — if so, mention prior parts]
```

### Optional: `feature-requests/[feature-slug].md`

PRDs created during drafting. See `feature-requests/CONTEXT.md` if/when that exists. Format:

```markdown
# Feature Request: [Short Name]

**Surfaced by**: [post slug]
**Date**: YYYY-MM-DD

## Problem

[What's hard or impossible right now in the blog.]

## Proposed Solution

[What the feature would do — not how to build it.]

## Why It Matters

[What kind of content this enables, how often this gap shows up.]

## Acceptance Criteria

- [...]
- [...]
```

## Done Looks Like

> Sounds like me. Opening matches close. No AI tells. Alt text on every image. Summary and social hooks captured. Any blog-feature gaps written up as PRDs.

## Anti-Patterns to Avoid

- **Drafting ahead of feedback**: writing 3 sections then asking for review. Voice drifts and rework compounds. Pause at each section.
- **AI tells**: hedging language ("it's worth noting," "in many ways"), tricolons everywhere, em dashes (see constraints), generic transitions ("furthermore," "moreover").
- **Forgotten alt text**: every image needs it. No exceptions.
- **Generated cover images by default**: real art first. AI-generated only when nothing else fits and the choice is deliberate.
- **Skipping the summary pass**: writing summary and social hooks "later" — they're part of this stage because the post is freshest right now. Later means never, or means generic recap from the title.
- **Building features mid-draft**: capture the PRD, keep writing. Don't context-switch into feature work.

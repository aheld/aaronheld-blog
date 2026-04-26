# Format Patterns

**ICM Layer**: L2 (patterns). Updated when content patterns evolve. Stage 2 (outline) picks the pattern.

## The principle

**Utility of the content matters more than counting words.** Word ranges below are guardrails to keep scope honest, not targets to hit.

The 1-hour drafting rule is the deeper constraint — anything that won't draft in one sitting either gets cut or becomes a multi-part series.

## The patterns

### Pattern A: Quick Tip / Short Observation

- **Word range**: 300–600
- **Drafting time**: 30–45 minutes
- **Structure**:
  - Concrete observation or scene (1 paragraph)
  - The point (1–2 paragraphs)
  - Why it matters (1 paragraph)
  - Close with a question or callback (1–2 sentences)
- **Sections**: usually 0–1 H2s. Often runs as continuous prose.
- **Cover image**: optional but encouraged.
- **When to reach for it**: a small insight that stands on its own. Resist expanding it just because you "could say more." If you have more to say, write a follow-up later.
- **Examples in the blog**: many of the older 2008–2010 posts (e.g., "The real meaning of agility," "Reminiscing the cache wars" lean this direction).

### Pattern B: Tutorial / Standard Post

- **Word range**: 800–1500
- **Drafting time**: 60 minutes (the canonical "one sitting")
- **Structure**:
  - Hook: concrete scene or observation (1–2 paragraphs)
  - Setup: the question or problem (1 paragraph)
  - 3–5 H2 sections, each one focused
  - Synthesis or "the larger point" (1 section)
  - Close: callback to hook, question to reader (1–2 paragraphs)
- **Sections**: 3–6 H2s. H3s only if a section has true parallel sub-parts.
- **Cover image**: required. Inline images encouraged where they clarify.
- **When to reach for it**: the default for most posts. A real argument with real support, scoped to one sitting.
- **Examples in the blog**: "AI Won't Kill the Middle Manager," "Why Your Strategic Planning Fails," "The North Star Vision for Engineering."

### Pattern C: Deep Dive

- **Word range**: 1500–2000 per page (cap each page at 2000)
- **Drafting time**: 60 minutes per page (so a multi-page deep dive is multi-sitting)
- **Structure**: same shape as tutorial but with more sections, more grounded examples, possibly a code block or two.
- **Sections**: 5–7 H2s.
- **Cover image**: required. Inline images and code blocks where they clarify.
- **When to reach for it**: a topic that genuinely needs the room — usually when the contrarian view from research is sophisticated enough that engaging it takes real estate.
- **Examples in the blog**: "Streamlining Blog Writing with Claude Code."

### Pattern D: Multi-Part Series (the exception)

A series is **not** "a deep dive that got too long." A series has:

- A **single thesis** that runs across all parts (one sentence, written before drafting).
- A **real arc** — each part builds on the last, with foreshadowing forward.
- A **real ending** — the last part lands, doesn't trail off.
- **Independent value per part** — a reader who only sees part 2 still gets a complete piece.
- **Cadence commitment** — parts publish every 1–2 weeks. Slower than that and the series stalls.

Each part is sized as a Pattern B (tutorial, ~1500 words) so it drafts in one sitting.

**Format**:
- `series.md` lives in `02_outline/[slug]/` with thesis, arc, planned ending, cadence.
- Each `part-N-outline.md` is a full single-post outline.
- Each part publishes as its own Hugo post. Series binding via Hugo's `series` front matter (already in use — see "Why Your Strategic Planning Fails" which has `series: ["Strategists Guide to Agile"]`).
- Each part's `social-hooks.md` includes "this is part N of M, link back to part N-1, foreshadow part N+1."

**Examples in the blog**: "Strategists Guide to Agile" series; "Specialization is for Insects" + part II.

## Choosing the pattern (in stage 2)

At the start of outlining, before any section beats, decide the pattern. Default to Pattern B unless:

- The idea genuinely fits in 600 words (→ Pattern A, and don't pad it).
- The argument needs more space because the contrarian view requires real engagement (→ Pattern C).
- The piece has a real arc with a real ending and independent-value parts (→ Pattern D).

If you can't honestly fit the piece into one of A/B/C, and it doesn't meet the multi-part criteria for D, the premise is probably too vague. Go back to research.

## Front matter conventions (all patterns)

```yaml
---
title: "Post Title"
date: YYYY-MM-DDTHH:MM:SSZ
draft: true                     # flipped to false at publish
description: "1-2 sentence summary for SEO and social cards"
categories: ["..."]
tags: ["...", "..."]
cover:
  image: "filename.jpg"
  alt: "Descriptive alt text — required, accessibility is non-negotiable"
  caption: "Optional caption with attribution"
series: ["Series Name"]         # only for Pattern D parts
---
```

## Closing conventions

All patterns share these closing elements:

- A line that circles back to the opening hook (often literally references the scene).
- A question or call to engagement.
- After publish: a "Comment on LinkedIn" link added in publish stage 4 (sub-step 3, the back-link update).

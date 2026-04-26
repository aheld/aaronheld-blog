# Stage 1: Research

**ICM Layer**: L4 (active work). Per-piece, ephemeral, archived after publish.

## Purpose

Gather raw material for the piece — papers, blog posts, classic SciFi references, quotes, historical parallels — *and* deliberately surface a view that **challenges** the premise rather than supports it.

The contrarian check is the point of this stage. Without it, research drifts toward confirmation, the outline gets soft, and the post rambles. A premise that survives a real challenge produces a sharper outline, which produces a post you actually finish.

## Inputs

- The idea (a sentence, a paragraph, a question — whatever Aaron walks in with).
- `_config/voice-and-tone.md`
- `_config/audience.md`
- `_config/themes.md` (does this idea connect to a recurring thread?)
- `_config/signature-moves.md` (especially the "nothing unprecedented" historical-parallel move — this stage is where parallels get found)
- `_config/recurring-references.md` (start from the known shelf before searching cold)

## Process

1. **Restate the premise in one sentence.** Aaron approves or sharpens it. If the premise can't be stated in one sentence, the piece isn't ready for research — it needs more thinking time first.

2. **Map to recurring themes and references.** Does this connect to existing threads in `_config/themes.md`? Are there authors, works, or thinkers in `_config/recurring-references.md` that already speak to this? Start there before reaching for new sources.

3. **Look for a historical parallel.** The "nothing unprecedented" move from `_config/signature-moves.md` belongs in research, not draft. Find the earlier wave (cloud/devops, pre-cloud datacenter, dot-com, etc.) that mirrors the current pattern. If you can't find one, note that — its absence is itself interesting.

4. **Gather supporting material.** Papers, posts, quotes, SciFi stories. Capture each with a real citation (URL, author, date), not a paraphrase.

5. **Find the contrarian view.** This is non-optional. Actively search for:
   - The strongest argument *against* the premise.
   - Someone credible who thinks the opposite.
   - A case where the premise demonstrably failed.
   - A more interesting framing that complicates the binary.

   If after honest searching you can't find a contrarian view, the premise may be too obvious or too vague to be worth a post. Flag that to Aaron.

6. **Pause for checkpoint.** Hand the artifacts to Aaron. Don't move to outline until he confirms.

## Output Format

Two files in `01_research/[slug]/`:

### `sources.md`

```markdown
# Research: [Working Title]

## Premise (one sentence)

[The claim or observation the piece argues.]

## Theme Connections

- [Theme name from _config/themes.md]: [why it connects]
- [...]

## Historical Parallel

[The earlier wave or precedent. If none found: explain why the situation is genuinely novel — that's a different kind of post.]

## Sources

### [Source 1 short name]
- **Author / Source**: [...]
- **URL**: [...]
- **Date**: [...]
- **Relevance**: [why this matters to the premise — one or two sentences]
- **Quote (optional)**: [pull quote if there's a usable one]

### [Source 2 short name]
[...]
```

### `contrarian-view.md`

```markdown
# Contrarian View: [Working Title]

## Strongest argument against the premise

[State the opposing case as honestly and forcefully as you can. If a thoughtful skeptic read this, would they feel their position was steelmanned?]

## Credible voices on the other side

- [Person / publication]: [their position, with citation]

## Cases where the premise failed

[Examples where the claim didn't hold up.]

## Where this leaves the piece

[One paragraph: did the premise survive the challenge? If yes, how was it sharpened? If no, what's the new premise?]
```

## Done Looks Like

> I have material that genuinely challenges my premise, not just supports it — and the premise is sharper for it.

## Anti-Patterns to Avoid

- **Confirmation gathering**: collecting only sources that agree. The contrarian-view.md must be filled with real arguments, not strawmen.
- **Citation laundering**: paraphrasing without a URL. Every source gets a real citation.
- **Forced parallels**: stretching for a historical analogy that doesn't actually fit. If the parallel is weak, say so — don't fake it.
- **Skipping ahead**: don't start outlining inside the research file. Hold the structure for stage 2.

# Stage 2: Outline

**ICM Layer**: L4 (active work). Per-piece, ephemeral, archived after publish.

## Purpose

Turn researched material into a tight, scoped skeleton that Aaron can actually finish drafting in one sitting (~1 hour). Lock the opening hook and the closing — those are the two points the middle of the post is accountable to.

This is the make-or-break stage. The two failure modes Aaron has named both happen here:
- **Rambling post** → outline was too broad, no clear premise spine.
- **Never-finished series** → outline was too ambitious, scope wasn't honest.

A good outline is a small commitment you can keep. A bad outline is a big plan you can't.

## Inputs

- `01_research/[slug]/sources.md` and `contrarian-view.md` (must exist and be checkpoint-approved).
- `_config/voice-and-tone.md`
- `_config/audience.md`
- `_config/format-patterns.md` (this stage picks the pattern)
- `_config/signature-moves.md` (which moves does this piece use?)

## Process

1. **Pick the content type.** From `_config/format-patterns.md`: quick-tip (300–600 words), tutorial (800–1500 words), deep-dive (longer, possibly multi-part with each part ≤2000 words). Type determines structure, not just length. Default is single-post.

2. **Decide single vs. multi-part.** Multi-part is the **exception**. The default is one post. Reach for multi-part only when:
   - The piece has a real arc with a real ending (not "and we'll see where it goes").
   - Each part is independently valuable — a reader who only sees part 1 still got something complete.
   - You can scope each part to one sitting (~1 hour).
   - You're willing to publish the next part within ~2 weeks of the previous one (otherwise it's a single post pretending).

   If multi-part: produce `series.md` first (thesis, arc, planned ending, part count), then one `part-N-outline.md` per part.

3. **Lock the opening hook.** From `_config/voice-and-tone.md`: a concrete scene or observation, present tense, problem before solution. Write the first 1–3 sentences in full, not as a placeholder. The opening is non-negotiable — it earns the rest.

4. **Lock the closing.** Often circles back to the opening theme. Ends with a question or call to engagement. Write the closing in full too. If you can't write the closing, you don't know what the post is arguing yet.

5. **Outline the middle.** Section beats only — bullet form, not prose. Each section: H2 title, one-line purpose, key sources/quotes/examples it draws on. Use H3s only when a section genuinely has parallel sub-sections.

6. **The contrarian check.** From `01_research/[slug]/contrarian-view.md` — does the outline acknowledge the contrarian view, or does it pretend the opposition doesn't exist? A post that ignores the steelman it found is weaker than one that engages it. Mark where the contrarian view lands in the outline.

7. **Scope honesty test.** Read the outline and ask: *can I draft this in an hour?* If no, cut a section. Don't rationalize. The 1-hour rule is what makes finishing reliable. If after honest cutting it still won't fit, that's the signal to consider multi-part — but only if criteria in step 2 are met.

8. **Pause for checkpoint.** Hand the outline to Aaron. Don't draft until he signs off.

## Output Format

### Single post — `02_outline/[slug]/outline.md`

```markdown
# Outline: [Working Title]

**Content type**: [quick-tip | tutorial | deep-dive]
**Word target**: [range from format-patterns.md]
**Estimated drafting time**: [should be ≤ 1 hour]

## Opening Hook (final, not draft)

[The first 1–3 sentences in full. This is what the reader sees first.]

## Section Beats

### [H2 Title 1]
- Purpose: [one line]
- Draws on: [source from sources.md]
- Notes: [...]

### [H2 Title 2]
- Purpose: [one line]
- Draws on: [...]
- Notes: [...]

[...]

## Closing (final, not draft)

[The last 1–3 sentences in full. Should land the hook from the opening.]

## Contrarian View Placement

[Where in the outline does the contrarian view get acknowledged? "Section 3" or "skipped intentionally because [reason]."]

## Signature Moves Used

- [e.g., historical parallel: cache wars → modern caching debate]
- [...]
```

### Multi-part — `02_outline/[slug]/series.md` + `part-N-outline.md`

```markdown
# Series: [Series Title]

## Thesis (one sentence)

[The single argument the series makes across all parts.]

## Arc

- Part 1: [what it sets up]
- Part 2: [what it builds]
- Part 3: [what it lands]

## Real Ending

[How the series ends — the actual conclusion, not "and we'll see." If you can't write the ending, you don't have a series, you have a vague impulse.]

## Cadence Commitment

[When each part publishes. Default: every 1–2 weeks.]

## Cross-Part Hooks

[How parts call back to each other and foreshadow forward.]
```

Each `part-N-outline.md` follows the single-post outline format above.

## Done Looks Like

> Either (a) one tight outline I can draft in an hour, OR (b) a series plan with a real ending and N tightly-scoped part-outlines, where N is justified.

## Anti-Patterns to Avoid

- **Placeholder hooks/closes**: "TBD" or "something about [topic]" in the opening or closing. If you can't write them, you can't write the post.
- **Section sprawl**: more than 5–6 H2s in a single post almost always means scope creep. Cut.
- **Optimistic time estimates**: "this will only take 90 minutes" → cut a section. The 1-hour rule is real.
- **Multi-part as escape**: reaching for multi-part because you can't bear to cut. Cut first, then decide.
- **Ignoring the contrarian view**: the steelman from research must land somewhere in the outline, even if briefly.

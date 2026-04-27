# Outline (Reverse-Engineered) — Making the Azure Private Link Video

**Slug**: `making-the-azure-private-link-video`
**Stage**: 02_outline (retrofitted from existing 03_draft/index.md)
**Format pattern**: **Pattern B (Tutorial / Standard Post)** — ~1,000 words, 6 H2s, single-sitting drafting feasible. Deliberately *not* Pattern C deep-dive: the post is about the *making*, not the technical content of the video. The technical material (Private Link, DNS, CNAME chain) is the video's job. The blog's job is the meta-story.

> Note: this outline was written *after* the draft. The reverse-engineer revealed two structural weaknesses the forward draft glossed over. They're called out at the bottom under "Structural notes from the reverse-engineer."

---

## Locked hook

> "I have an Island of Misfit Toys."

A single declarative sentence, reference to the Rankin/Bass holiday special. Earns its keep three ways:

1. Universally legible — the misfit-toys metaphor is widely shared cultural shorthand.
2. Sets up the cover image (Slonik, the AKS shipping containers, the OPEN FOR BUSINESS sign) — the cover is *the island itself*, which makes the hook visually load-bearing, not just rhetorical.
3. The "I" is first-person professional, immediately matching `_config/voice-and-tone.md`.

**Cover image alt text** (already correct in the draft, kept):
> "Storyboard frames showing a friendly PostgreSQL elephant behind a desk and AKS shipping containers walking through a door beneath an OPEN FOR BUSINESS sign"

## Locked close

> "Maybe they fit into the next one, as I learn more about content creation and the available tooling continues to improve. One day, it will be as easy as making Flash animations on the timeline…"

Earns its keep:

1. Circles back to the island — the misfits aren't deleted, they're parked.
2. The "as I learn more about content creation and the available tooling continues to improve" places the constraint where it actually lives — split between Aaron's craft and the tools — instead of falsely on "I can't animate." This matches the thesis revision in the agenda below.
3. The Flash-timeline reference is voice-perfect: peers catch it (Macromedia Flash, before Adobe, before HTML5 killed it), and the 25-year-old reader gets a flavor of why "easy" once meant something specific. Lands the dual-audience test.
4. The trailing ellipsis acts as the engagement invitation — it leaves the door open for sequel posts and reader replies.

The draft also closes with a separator line and a sibling-post reference to *Streamlining Blog Writing with Claude Code*. That's a publish-stage decoration, not a structural close, but worth keeping — and per the thesis revision, the link to the sibling post should be strengthened, not just decorative.

---

## Section beats (the H2s)

The draft has 6 H2s. Each one earns a beat:

### H2 1 — "Step 1: Research before script"

- **Beat**: AI will write you a plausible script cold; the research step prevents plausibility from becoming wrong-in-ways-you-won't-notice.
- **Concrete anchor**: 5,000-word DNS deep-dive that nobody saw. CNAME chains, `168.63.129.16`, Private DNS Zone linking, hub-and-spoke gotchas.
- **Lesson surfaced**: "When you skip the research step, your script writes things that *sound* right. When you don't, your script writes things you can defend."
- **Voice match**: First-person professional. Concrete artifact (the doc) carries the abstract claim.

### H2 2 — "Step 2: The script that was too good to make"

- **Beat**: Introduce v1 in full character detail — Slonik, three Rickys, the stagehand, the circus tent, the eight-lane highway.
- **Concrete anchor**: Six-act narrative, two parallel paths, costume changes, "ALL OF AZURE: 1,000,000+ CUSTOMERS" banner.
- **Pivot line**: "It was funny. It was *correct*. And I could not make it." (Italics on *correct* per voice config — emotional truth.)
- **Honesty beat**: "That's the honest reason it went to the island. Not 'the scope was wrong' or 'we needed something cleaner.' I can write a character-driven, six-act, costume-changing, circus-tent-having animated short faster than I can animate one frame of Slonik turning his head."

### H2 3 — "Step 3: Cutting back to what I could actually finish"

- **Beat**: v2 keeps the thesis, drops the theater. Microsoft-style architecture diagrams, official Azure SVG icons, numbered DNS chain.
- **Concrete anchor**: The raccoon silhouette survived because he was the cheapest character to render. Slonik didn't, because faces and chairs require an animation pipeline Aaron doesn't have.
- **Lesson surfaced**: "The cheapest piece of the first script became the only character in the second." (This is the strongest single line in the post.)

### H2 4 — "Step 4: Make the honest version"

- **Beat**: The shipped video lands the same lesson at ~10% of the production cost the v1 would have demanded.
- **Concrete anchor**: Link to the YouTube video. "Almost everything from the first script's *thesis* and almost nothing from its *theater*."
- **Brevity**: This section is intentionally short. The work has already happened in H2-3.

### H2 5 — "What's actually on the island"

- **Beat**: Synthesis. Four bulleted maxims:
  1. AI scales your writing past your making.
  2. Research first is not optional.
  3. The cheapest piece of the first draft is often the only piece of the final.
  4. Cut to what you can finish, not what you can imagine.
- **Voice match**: Bullets are bolded (per signature-moves), each followed by a sentence that grounds the maxim in this specific project.

### H2 6 — Close (no H2 — runs as a closing paragraph after the bullets)

- **Beat**: Slonik isn't deleted. He's on the island, with the rest of the misfits.
- **Callback**: References the cover image directly ("the three Rickys, the stagehand, the circus tent, and the eight-lane highway").
- **Engagement line**: "Maybe they fit in the next one. After I learn to animate."

---

## Voice / format checks (against `_config/`)

- **Voice (L0)**: First-person professional ✓. Concrete observations from experience ✓. Italics for emotional truth ✓ ("It was *correct*"). Bold for takeaways ✓. No em dashes — **needs verification in the draft** (constraints.md is hard rule).
- **Audience (L0)**: Peer + younger reader. The contrarian view raised a real concern here — "cut to what you can finish" lands differently for the two readers. Flagged for the revision pass.
- **Format pattern (L2)**: Pattern B confirmed. Word count ~1,000, 6 H2s, draftable in one sitting.
- **Closing convention**: Circle-back to opening hook ✓. Question/invitation to engagement — *implicit* via "after I learn to animate." Could be more explicit. Flag for revision.
- **Sibling post link**: Already present, references *Streamlining Blog Writing with Claude Code*. Good.

## Structural notes from the reverse-engineer

These are weaknesses the forward draft glossed over. They become the agenda for the revision pass.

1. **The 5,000-word DNS doc is named but not cited.** The draft says "five thousand words of reference material I would never put in a video" without telling the reader what was in it or where it lives. That's a missed credibility beat — the whole "research first" lesson lands harder if the reader can see the artifact.

2. **The framing "I cut things to v2" undersells what v2 is.** v2 isn't only a stripped v1; it also adds the public-DNS-fork beat (the privatelink CNAME exists in public DNS too, falling through to the public IP without a Private DNS Zone link). That's a v2-only technical refinement — the second pass *understood the material better*, not just compressed it. The draft's "kept everything that mattered, dropped what I couldn't make" obscures this. Adding one sentence acknowledging that v2 also got more correct would make the post more honest.

3. **The "I can't animate" framing is doing more work than it earns.** It's "I chose not to invest in learning Cartoon Animator / Rive / Adobe Character Animator for this project," not "I can't." Aaron's the kind of person who learned Remotion specifically for this — the skill ceiling isn't the bottleneck, the runway is. A more precise framing makes the takeaway more transferable to readers with different budgets.

4. **The four-bullet synthesis lands well for a 20-year veteran and lands as anti-mentoring for a 25-year-old.** "Cut to what you can finish, not what you can imagine" is good late-career advice (scope discipline). It's bad early-career advice (a 25-year-old should over-scope with AI to learn what their real production budget is). One of the bullets needs to be reframed so both readers take away something useful, per the audience test.

5. **The close is implicit-engagement, not explicit-engagement.** The voice config says posts should "end with engagement or call to reflection." The current close is reflective ("After I learn to animate") but doesn't open a door for the reader. Optional revision: a one-line invitation to the reader to share their own misfit-toy island.

## Recommended revision agenda (for stage 03_draft)

**Updated 2026-04-26** based on Aaron's answer in `01_research/.../contrarian-view.md`. The contrarian view's central question — "is 'AI scales writing past your making' the right framing?" — got a clear answer: **no**. The right framing is **"AI made it easy to lose sight of the goal."** That changes the post's thesis, not just its bullets.

### Thesis change

| Old thesis | New thesis |
|---|---|
| AI scales your writing past your making. The gap between describing and making is where projects die. Cut to what you can finish. | AI made it easy to get carried away with what's *possible* and lose sight of what the work was *for*. The video's job was to explain a concept to a technical audience. v1 was a great script — and it had drifted. The pivot back to v2 was the work. |

The bones of the post survive. The cover image, the hook, the close, the v1 vs v2 walkthrough, the raccoon-silhouette-survived beat — all still earn their spots. What changes is what those beats *mean*.

### Concrete revisions in priority order

1. **Reframe H2-2's "I could not make it" line.** It's not "I could not make it." It's "I was not willing to spend the money or time on animation for this particular project, and the v1 script had drifted from the goal anyway." This is the single most important change — it's the difference between "I learned my limits" and "I caught myself drifting." The latter is the more honest and more transferable lesson.

2. **Add a new beat to H2-3 about losing sight of the goal.** Currently H2-3 is framed as "cutting back to what I could finish." It should be reframed as "re-anchoring to what the video was for." The cut wasn't a production decision — it was a re-reading of the brief. The video's job is to explain Private Link to a technical audience. v1 was an animated short *about* Private Link. v2 is an explainer of Private Link. Different things. The pivot is the post's center of gravity.

3. **Rewrite the H2-5 synthesis bullets.** The current four maxims need to be re-grounded in the new thesis:
   - "AI scales your writing past your making" → "AI makes it easier to drift from the goal. The capability ceiling isn't your animation skill — it's your discipline about what the work is *for*."
   - "Research first is not optional" → keep, this still holds.
   - "The cheapest piece of the first draft is often the only piece of the final" → keep, this is the strongest single line.
   - "Cut to what you can finish, not what you can imagine" → replace. New version: something like "The pivot — recognizing the drift and re-anchoring — is the practice. AI doesn't change that; it just makes you do it faster and more often."

4. **Add 1 sentence in H2-1 naming the DNS deep-dive's actual contents** (CNAME chain, `168.63.129.16` resolver, Private DNS Zone linking) so "research is load-bearing" has a visible anchor.

5. **Add 1–2 sentences in H2-3 acknowledging that v2 wasn't just smaller — it was more correct.** The CNAME-fork-in-the-road beat (the privatelink CNAME exists in public DNS too, falling through to the public IP without a Private DNS Zone link) is a v2-only refinement. Crediting it reinforces the new thesis: the second pass was a *different* draft anchored to the goal, not a smaller version of the first.

6. **Strengthen the sibling-post link to `streamlining-blog-writing-with-claude-code`.** Per Aaron: "this is a technique I'm continually evolving, and AI is moving so fast you have to be willing to continually refactor workflows and reset expectations. But the core concepts — breaking down large tasks into smaller deliverables with the right context at each step — is valuable." The sibling post makes the workflow claim. This post is a worked example of why the workflow itself has to keep evolving — the v1-to-v2 pivot is a workflow refactor in miniature. The current closing reference to the sibling post is decorative; this version ties the two pieces together as a small arc.

7. *Optional*: explicit engagement line before the close. Could be as light as: "What did you cut from your last project, and was it really a budget decision or a goal-discipline decision?" Defer to Aaron.

## Checkpoint question

> Can I draft this in one sitting (~1 hour)? Hook strong? Close earned?

Yes, yes, yes — but the revision pass is meaningfully larger than the original retrofit suggested. The thesis change in revisions #1–3 is structural, not a polish pass. The hook ("Island of Misfit Toys"), the cover image, and the close ("After I learn to animate" — *which now needs to change too*, since "learn to animate" reinforces the wrong framing) will need to flex with the new thesis. The locked close should probably become something like "After I get better at catching myself when I drift" — less catchy but more honest. Worth discussing before drafting.

# Contrarian View — Making the Azure Private Link Video

**Premise being challenged**: "AI scales your writing past your making. The gap between 'I can describe this' and 'I can produce this' is where projects die. The fix is to cut to what you can finish, not what you can imagine."

The premise is comfortable — it casts Aaron as the disciplined craftsman who recognized scope creep and corrected. The strongest opposing argument has to find the place where that framing is *itself* the comfortable story.

## The strongest opposing read: this isn't an AI/production gap, it's a taste-and-discipline gap dressed up as an AI/production gap

The post argues that AI gave Aaron a writing capability his production capability couldn't catch up to — as if writing capability is now infinite and production is the new bottleneck. That framing has problems:

1. **Aaron could already write character-driven six-act narratives without AI.** He's been writing this blog since 2008. The v1 script's structural ambition isn't an AI artifact — it's an Aaron artifact. AI accelerated drafting it, but the *idea* of doing it is something Aaron has done before and could do again from scratch. So the "AI lets you describe more than you can make" framing is at least partially a misattribution. The real gap is between Aaron's narrative ambition (which has always existed) and Aaron's animation skills (which never have). AI didn't widen the gap. It just made the ambition cheaper to commit to paper, which made the gap *visible* faster.

2. **The v2 script isn't just "the parts I could finish." It's also more correct.** The blog's framing — "kept everything that mattered, dropped what I couldn't make" — is gentle on itself. The v2 script *adds* technical nuance v1 didn't have: the `publicdnspath` beat where the privatelink CNAME exists in public DNS too, and without a Private DNS Zone link it resolves back to the public IP. That's not a production cut. That's a research-and-thinking improvement that happened *because* the second pass forced Aaron to engage with the material more carefully than the character-driven version did. A more honest framing: the v1 script had me hiding behind theater. The v2 script forced me to actually understand the DNS fork. The lesson there isn't "cut to what you can finish" — it's "ambitious framing can be a procrastination strategy."

3. **The "I can't animate" claim is doing a lot of work.** Off-the-shelf 2D character pipelines that don't require frame-by-frame animation exist and have for years: Cartoon Animator, Adobe Character Animator, Rive, Lottie (which the project already uses for the silhouette raccoon). A solo producer who has the patience to write 5,000 words of DNS research and learn Remotion has the patience to learn one of these. The decision not to wasn't really "I can't" — it was "I don't want to invest the runway." That's a legitimate choice, but calling it a production-capability problem is more comfortable than calling it a willingness-to-learn problem.

## A specific structural critique: the post may be teaching the wrong lesson

If the real story is "I had a character-driven script, I scoped it down to a diagram-driven script, the diagram-driven script is good," the lesson generalizes to: **trust the boring version more than the exciting version**. That's not what the post says. The post says **cut to what you can finish**. Those sound similar but they aren't:

- "Cut to what you can finish" → next time, scope smaller from the start. Don't write Slonik in v1. Save time.
- "Trust the boring version" → next time, write the ambitious version *first*, then deliberately strip it. The stripping is the work. v1 was load-bearing for v2 even though it was discarded.

The second framing is closer to what actually happened. The blog's title — "The Island of Misfit Toys" — implies the v1 characters are mourned. But they shouldn't be mourned. They were the cost of getting to v2. The post would be sharper if it argued for *deliberate* over-scoping followed by *deliberate* stripping, instead of "I learned to imagine less."

## The audience-test version of the disagreement

Apply the audience test from `_config/audience.md`: "Would a smart 25-year-old who's never managed feel respected here, AND would a 20-year veteran feel not insulted?"

A 25-year-old reading the post takes away: "Don't be too ambitious with AI. It'll write things you can't make."

That's bad advice for a 25-year-old. They *should* over-scope with AI early. That's how they learn what their actual production capability is. Discouraging them from imagining big things is exactly the wrong lesson at that career stage. A 20-year veteran reads the same paragraph and goes "yeah, scope discipline" and nods. Two readings of the same line with opposite implications — which is exactly the failure mode the audience config warns against.

## What this contrarian view would change in the draft

Not abandonment — refinement. Specifically:

1. **Lean into the v1-was-load-bearing framing.** Slonik isn't on the island because Aaron failed. He's on the island because writing him was the only way to know v2 was the right version. Make the *process* the lesson: deliberate over-scope then deliberate strip.
2. **Acknowledge that v2 also got more correct, not just leaner.** The CNAME-fork-in-the-road beat is a v2-only addition. Crediting it complicates the "I cut things" story in a useful way — it shows the second pass was a *different* draft, not a smaller version of the first.
3. **Be honest about the "can't animate" claim.** It's "didn't choose to learn animation for this project," not "couldn't." That's a different and more interesting admission. It acknowledges that the constraint is a budget choice, not a capability ceiling — which makes the lesson more transferable to readers whose budgets and ceilings are different.
4. **Reframe the takeaway for the younger audience.** "Cut to what you can finish" is good late-career advice. It's bad early-career advice. The post should either acknowledge this or refactor the takeaway to apply across both readers — something like "the gap between describing and making is a measurement, not a verdict. Use it to see your real production budget, not as a reason to imagine smaller next time."

## The version of this critique that's wrong

For honesty: the contrarian view above might be too clever. The simpler reading — "Aaron had a fun idea, couldn't ship it, shipped a smaller version, learned the smaller version was actually better, wrote about it" — is also true. The post doesn't *have* to be a meta-essay on taste vs. discipline. It can just be a workflow note. And the maxim "the cheapest piece of the first draft is often the only piece of the final" (the raccoon silhouette) is genuinely useful as-is, even if the larger frame is debatable. So the contrarian view is a refinement, not a refutation. The draft is workable. It's also missing a layer.

---

## Aaron's answer to the framing question (2026-04-26)

Asked directly whether "AI scales writing past your making" is the right framing or a self-flattering version of "I made a scope error," Aaron's answer:

> AI allowed me to get carried away with what was possible and I lost sight of what I was trying to do, which was to explain a concept to a technical audience. The animation absolutely could have been done with animators I've worked with — I was not willing to spend the money or time for this particular project, and the pivot itself is worth discussing.
>
> Note that this is a technique I'm continually evolving, and AI is moving so fast you have to be willing to continually refactor workflows and reset expectations. But the core concepts — breaking down large tasks into smaller deliverables with the right context at each step — is valuable.

This collapses several of the contrarian threads into a sharper, more honest framing. It changes the post in three concrete ways:

1. **The "I can't animate" framing is wrong and should go.** Aaron's been clear: he's worked with animators who could have shipped v1. The constraint was budget and time for *this particular project*, not capability. That's a different and more honest admission, and it generalizes better to readers whose budgets and ceilings are different.

2. **The real lesson isn't "AI scales writing past your making." It's "AI made it easy to lose sight of the goal."** The video's job was to explain a technical concept to a technical audience. The v1 script was a great script — but it had drifted from "explain Private Link" toward "make a memorable cartoon." The pivot wasn't a production cut; it was a re-anchoring to the original intent. That's a more durable lesson, and it's the one the post should land.

3. **The pivot itself is the post's center of gravity, not a side note.** The interesting thing isn't that v1 was abandoned — it's that recognizing the drift and pivoting back to the goal is a skill worth naming. AI tooling makes drift easier and faster. The discipline of catching the drift is the practice.

And the workflow framing the post should pick up from `streamlining-blog-writing-with-claude-code`:

> This is a technique I'm continually evolving, and AI is moving so fast you have to be willing to continually refactor workflows and reset expectations. But the core concepts — breaking down large tasks into smaller deliverables with the right context at each step — is valuable.

The sibling post made a workflow claim. This post is a worked example of *why that workflow has to keep evolving* — the v1-to-v2 pivot is itself a workflow refactor in miniature. The two posts now form a small arc: the workflow piece sets up the principle, the misfit-toys piece shows the principle being re-applied as the tools change underneath you.

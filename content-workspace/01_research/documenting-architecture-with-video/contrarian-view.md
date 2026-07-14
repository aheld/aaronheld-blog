# Contrarian View — Documenting Architecture with Video

**Premise being challenged**: "Static diagrams document structure well, but systems with loops, gates, and feedback need video. I made both for the harvester; the video closes the gap the diagrams leave, and the comparison tells us when each medium is worth its cost."

The premise flatters the experiment. The strongest opposition says the experiment is rigged three different ways, and that even a fair version might land against the video.

## 1. The maker is the worst possible judge, and the video goes second

The person producing both artifacts already understands the system perfectly. Every explanatory artifact you make feels clear to you, because you supply the missing understanding without noticing. Worse, the video is the *second telling*. The Private Link post already documented this effect: the second pass over the same material is more correct and better structured because the first pass was load-bearing. So if the video "explains the loop better," how much of that is motion, and how much is that it's the author's second, more practiced telling? The honest comparison would need naive readers and naive viewers, one artifact each, explaining the system back. Without that, "effectiveness" is the author grading his own homework, twice, and preferring the later draft.

## 2. The learning-science literature is genuinely split, and the skeptics ran the experiment first

Tversky, Morrison, and Bétrancourt ("Animation: Can It Facilitate?", IJHCS 2002) reviewed a decade of animation-vs-static studies and found that when the two carry equivalent information, animation frequently fails to win. Their diagnosis is the transience problem: motion plays at the animator's pace, not the reader's. A static diagram lets the reader dwell, re-inspect, compare two regions, control their own attention. A video takes that control away. The four loop mechanisms in the harvester doc (replay boundary, review gate, sticky fields, quality score) interact; a reader may need to hold 6.1 and 6.3 side by side. Paper does that. A timeline doesn't. Mayer's multimedia principles cut the other way (narration synchronized with visuals is powerful), but the contrarian point stands: the research does not simply say "moving pictures teach better." The post cannot pretend it does.

## 3. Video violates every maintainability rule we ask of documentation

Docs-as-code exists for a reason. The static doc is diffable, reviewable in a PR, greppable, and versioned next to the system it describes. When the harvester grows a fifth pipeline stage, updating the doc is an edit; updating the video is a *production*. The rendered MP4 starts rotting the day it ships, silently, with no way to flag the stale frame. It also can't be skimmed, searched, or linked into at the paragraph level (chapter markers are a weak substitute). Engineers consult architecture docs far more often than they learn a system cold; the reference use case dwarfs the onboarding use case in frequency, and video loses the reference use case completely. An accessibility corollary: the video needs a transcript anyway, and if the transcript plus a few stills carries the explanation, the motion was decoration.

## 4. The category error: this may be comparing a reference to an explainer

By the Diátaxis taxonomy, the static doc is reference + explanation; the video is explanation only. Of course each wins at its own job. If the post's conclusion is "use reference artifacts for reference and explainer artifacts for explaining," that's true and nearly empty. The post has to reach a sharper claim to earn the experiment, something like: *for systems whose essential behavior is a stateful loop, the explainer is not optional supplementary material; skipping it means most readers never actually acquire the model, no matter how complete the reference is.* That claim is falsifiable and interesting. The generic "different tools for different jobs" close is neither.

## 5. The economics probably favor the diagrams even in the best case

The diagrams already exist and the video reuses them as base layers, so the video's cost is incremental. That is the *most favorable possible accounting* for video, and it still likely runs several multiples of the diagram effort once script, animation, narration, and revision are counted. Against that cost: a shorter shelf life (point 3) and unproven effectiveness gains (points 1–2). The contrarian bet is that the honest numbers, honestly presented, argue for video only when three conditions stack: the system is stable, the audience is wide or recurring (every new hire, every quarter), and the behavior is genuinely dynamic. That's a narrow slot. The post is stronger if it says so plainly than if it advocates for video.

## What this changes in the draft

Not abandonment; discipline. Specifically:

1. **Confess the confounds up front.** Author-as-judge and video-goes-second both get named in the effectiveness section. If we get even one naive reader and one naive viewer, report what they said verbatim; if we don't, say the effectiveness half is observational and let the effort half carry the numbers.
2. **Engage Tversky, not just Mayer.** The transience problem is real for this exact content (interacting mechanisms the viewer may want side by side). The video design should answer it concretely: recap frame at the end, chapter markers, the doc linked as the pause-and-dwell companion. The post should show the design answering the critique.
3. **Concede the reference use case entirely.** The video is not documentation of record and never will be. The diagram stays canonical, versioned, and updated. The video is a mental-model bootstrap with an expiration date. Saying this early defuses the docs-as-code objection and makes the remaining claim sharper.
4. **Land the narrow claim, not the broad one.** "Video documents architecture better" is indefensible. "A five-minute animation of the loop transfers the runtime model faster than prose, and for a stable system with a recurring audience that's worth roughly Nx the diagram effort" is defensible, checkable, and useful. The conclusions section should be a short set of conditions, and it should be comfortable telling most readers *not* to make a video.

## The version of this critique that's wrong

The critique assumes documentation's only jobs are reference and teaching-for-retention, the two things labs can measure. Architecture docs have a third job the literature barely touches: getting a busy human to *engage at all*. A complete C4 doc that nobody reads past section 2 transfers nothing. If the video's real advantage is that people actually watch it to the end, then "effectiveness" includes attention, not just comprehension per minute, and the lab result about equivalent information matters less than the field result about who shows up. The post can hold both: the skeptics are right about information, and the video still wins on invitation.

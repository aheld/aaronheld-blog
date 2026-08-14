---
title: "Never Skip Leg Day: Introducing Agentic Sprint Zero"
date: "2026-08-14T09:00:00-04:00"
draft: false
description: "Most 'bad AI code' complaints are about skipped setup. Introducing Agentic Sprint Zero: a small deployed system that calibrates your agent's guidelines first."
categories: ["professional", "AI"]
tags: ["AI", "engineering management", "agile", "sprint zero", "claude code"]
cover:
  image: "cover.jpg"
  alt: "A bronze statue of a muscular figure hoisting a barbell overhead, seen from behind against a clear blue sky, legs planted and straining under the load"
  caption: "Photo by [Mário Maia](https://unsplash.com/@marium71?utm_source=aaronheld-blog&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=aaronheld-blog&utm_medium=referral)"
---
The general consensus is that AI code is bloated, repetitive, non-idiomatic. A study of more than a thousand Reddit and Hacker News threads poetically called what we are seeing ["An Endless Stream of AI Slop"](https://arxiv.org/abs/2603.27249).

So when I started [my latest project](http://dinner.isourthing.com/), I kicked it off with an admin-editable homepage. That decision forced me to build user registration, login, auth, and sessions right along with it, the necessary plumbing to wire it all up. There's nothing in our [PRD](https://github.com/aheld/consensus_app/blob/main/docs/PRD.md) about a CMS. An editable text box just happens to be a simple feature to review on its own, and building it requires all the same auth logic the real product needed anyway. I deployed it to production and reviewed every line before the fun features got a single prompt. Okay, I reviewed most of the lines. Well, I reviewed some sections. 😁

The point was to build small, production-ready features using patterns everybody already knows cold. That gave my agents and me some real "hands" on experience building good code, before we got to the more complicated parts.

I present **'Agentic Sprint Zero'**, my approach to the problem.

## The Slop Is Real

The complaints hold up under real data, not just vibes. [GitClear analyzed 211 million changed lines of code](https://www.gitclear.com/ai_assistant_code_quality_2025_research) and found that in 2024, duplicated code blocks jumped roughly **eightfold**. That was the first year on record where copy-pasted code in a single commit outpaced code that got properly refactored. Cloned code carries 15 to 50 percent more defects than code written once and reused.

The Reddit and Hacker News study puts the expected community spin on those numbers.

- "You can go very fast with AI, but you accrue technical debt at a much higher speed too."
- "I straight up asked them (the committer) if they know what their code does. They didn't."
- "if the comment has an emoji it's a guarantee" (note this doesn't apply when I put 😁 in a post like this.)
- "When the comment smells like AI but I just can't prove it"
- "I don't know how you could trust any of it [...] No real understanding of what it's doing, it's just guessing"
- "C-level executives were running parts of our codebase through AI tools and literally copy pasting the response as an answer to every technical problem [which of course were wrong]"
- "I'm almost 40 and I'm really not interested in continuing the AI slop treadmill [...] What a shitty time to be alive. I used to love technology. Now I'm coming to loathe it"

The same researchers asked what actually worked for teams that got this under control. **PR size limits.** Mandatory self-review before anyone else looks at the code. A rule that the author has to walk a reviewer through their choices out loud. Accountability for code quality showing up in performance reviews.

Turns out that we still need engineering management, not just fancy prompt invocations.

## We've Run This Experiment Before

None of this is new. In the early 2000s, companies threw specs over the wall to offshore teams with zero onboarding, no shared context, and no established patterns to follow, then acted surprised when the code came back bad. "Their code is bad" was the exact sentence people used.

The companies that got good software out of those engagements did the unglamorous thing: they invested in documentation, coding standards, and real review cycles before asking for anything complicated. In the 1990s I faxed specs over and got a .dll back that worked.  We had to write out the specs and print them, so they got more review as compared to digital tickets.  In general bad software was always 'bad engineers', as opposed to bad direction.

Management still struggles to setup the individual contributor teams to succeed, and that lack of attention has carried over to the AI world.

Software engineers already have a name for the discipline of doing that setup before real work starts. It's called Sprint Zero. To the Agile purists, that term is crimethink, but hear me out and then decide.  There is a practicality that sometimes needs to override ideological purity.

## Agentic Sprint Zero, Defined

Agentic Sprint Zero is a small, deployable, end-to-end system, built from patterns you already know cold, reviewed closely enough to trust, so the corrections land somewhere durable before the untested features show up.

I built mine for [Consensus](http://dinner.isourthing.com/), a group decision app: put the options up, everyone votes, the deadline picks a winner. (Yes, I opened this post with "the general consensus", so now I'm talking about the specific consensus.) [Phoenix](https://www.phoenixframework.org/) LiveView, Elixir and SQLite, deployed to Fly.io.

The kickoff prompt asked for registration, login, an authenticated admin area, and an admin-editable homepage. Choosing that last piece is what pulled the entire auth stack into existence on day one, because "admin-editable" means nothing without knowing who's an admin. Both shipped, deployed, and got reviewed before the actual product, the voting logic everyone was excited about, got a single prompt. The commit filenames tell the same story on their own: `seed-0-setup-repo`, `seed-1-activity-group-setup`, `seed-2-add-voting`, `seed-3-improve-ux`, `seed-4-anarchy`. Foundation first, features second, chaos last.

The [kickoff prompt](https://github.com/aheld/consensus_app/blob/main/docs/prompts/prompt-seed-0-setup-repo.md) fanned out a builder agent and a separate, fresh-context critic agent for every piece. The critic ran the app, logged in, exercised every flow, and compared the result blind against a reference generated by Phoenix's own official tooling, looping until it said ours won. Its quality bar, quoted directly: "Our app must be indistinguishable from or better than what the Phoenix core team would ship." That's many agent sessions, each graded against a bar a human could actually check.

What came out the other side were three legs I'll come back to. A deployed [walking skeleton](https://www.oreilly.com/library/view/97-things-every/9780596800611/ch60.html), the term Alistair Cockburn coined for a tiny end-to-end slice that proves the architecture, real design, not a throwaway scaffold. A working CI/CD pipeline to Fly.io, proven end to end. And a set of guidelines, CLAUDE.md, AGENTS.md, five repo-specific skills, and a running decision log, that had survived contact with real output.

That last one is where the correcting happened, and it's rarely code. One commit fixed three skill files that told future agents to check their work against a build session's scratch folder, one that gets deleted the moment the session ends. A future agent following that instruction "would be sent to diff against a folder that no longer exists, and would either skip the check or invent an answer." The fix rewrote the guidelines so the next agent wouldn't inherit the same dead end. Zero lines of application code changed. That was just one example of the refactoring of the agent harness that had to happen.  So we have production code, test code, IAC code, and now agent code.  It's all code that needs to be continually refined and improved.

In the AI world, we are a level higher in our abstraction, so I was not correcting code as much as I was correcting the Skills.md that guided the agents in how they write the code.

[DORA's 2025 research](https://dora.dev/dora-report-2025/) backs this up at scale: AI's real role is as an amplifier. It magnifies whatever foundation is already there, including the absence of one.

One more thing before the arguments against all this: the admin homepage never made it past Sprint Zero. Once the real product took over the homepage, it got deleted outright, not hidden. Training wheels come off. The three legs stayed.

## Yes, Scrum Calls This a Sin

If you know Scrum, you're already objecting. Sprint Zero has a reputation, and not a good one. Scrum.org calls it out directly, and Maarten Dalmijn goes further, calling it a ["cardinal sin"](https://medium.com/serious-scrum/why-using-sprint-0-is-a-cardinal-sin-for-all-scrum-masters-b97c4c90c0a9): a phase with no obligation to deliver value, that quietly grows until it swallows a quarter. The whole point of Scrum is a working increment at the end of every sprint, not a runway before the runway. That critique earned its teeth, and I'm not dodging it.

But look at what actually happened here. My Sprint Zero didn't produce a design doc or a backlog of good intentions, and it did produce a real feature (Login). It produced a URL. You can register on it, log into it, and edit content in it, in production. That's a shippable increment with a foundation-first backlog, closer to the letter of Scrum than most actual Sprint 1s.

The empiricism argument cuts my way too. Scrum's case against Sprint Zero is that you learn what you need by inspecting real output, not by guessing in advance. That's exactly what this was: guidelines corrected against real, reviewed output, using patterns cheap enough to verify, instead of rules written speculatively before anyone had touched the code.

## The Agent Isn't a Junior Engineer

There's a real critique of "manage AI like people," and it deserves better than a strawman. A junior engineer you mentor compounds: feedback persists, judgment grows, eventually they mentor someone else. An agent session does none of that. Correct it on Tuesday and Wednesday's session remembers nothing of it. [The LLM is not a junior engineer](https://jacobharr.is/personal/llm-not-junior-engineer), and pretending otherwise sets you up to trust something that can't earn trust the way a person does.

I think that's exactly why the foundation matters more, not less. With a person, onboarding can live in their head. With an agent, the repo is the only memory there is. When I say manage AI like you manage people, I don't mean the worker is a person. I mean the management disciplines transfer: clear expectations set early, real review of the first reps, corrections that land somewhere durable. I've made a version of this argument before about [what AI actually changes for managers](/post/ai-wont-kill-the-middle-manager/); this is the more literal version of it.

Which resolves the "hands-on experience" I mentioned earlier, scare quotes and all. The agent didn't keep it. It couldn't. What Agentic Sprint Zero produces is experience for the repo: reps that got critiqued, corrections that got written down, so the next session inherits the lesson even though this one couldn't.

None of this works if the guidelines are just prose nobody enforces. Plenty of developers have written 200 lines of rules and watched an agent ["ignore them all"](https://dev.to/minatoplanb/i-wrote-200-lines-of-rules-for-claude-code-it-ignored-them-all-4639). Fair complaint. But that's an argument against exhortation-only foundations, not against foundations. A skeleton the agent can pattern-match. Tests that fail loudly. Linters that block the merge. That's the difference between a gym membership and actually going. I wrote about this same instinct, documentation nobody wanted until AI made it mandatory, in [We Finally Care About Context](/post/we-finally-care-about-context/): we always knew how to do this. We just needed a reason.

## When It's Fine to Skip the Gym

None of this means every project needs a Sprint Zero. Andrej Karpathy coined "vibe coding" for exactly the opposite move: "fully give in to the vibes, embrace exponentials, and forget that the code even exists." For a weekend project nobody else will ever touch, that's the correct amount of process for the stakes.

Simon Willison draws the line I'd draw too: vibe coding means you don't review what the model wrote. That's fine for a throwaway prototype and [grossly irresponsible](https://simonwillison.net/2025/Mar/19/vibe-coding/) for anything other people depend on. His term for the disciplined version, agents inside real testing, real review, real planning, is "vibe engineering."

The real question is whether the code has to outlive the session that wrote it, not whether you used AI. If nobody else, including future you, ever has to read it again, skip leg day. Just don't be surprised when it can't hold any weight.

Everyone wants the bulky arms and ripped abs. That's what gets the stares in the gym and the likes on Instagram, or so I'm told. Strong legs give you balance and foundational strength: they hold up everything else, and nobody photographs them. Good design, a working CI/CD pipeline, and guidelines that survived contact with real output: that's the foundation for a good system. We never needed the CMS, and it was removed, but the whole product is better off for what we created along the way.

Developers who skip leg day probably also skip tests and IAC so they can "focus on what the business wants" and "look good."

So when you see AI slop, ask what the first two ~~weeks~~ hours of that project looked like. Run an AI project like you'd run any new team: clear expectations up front, real review of the early reps, corrections that land somewhere durable. The agent won't remember Tuesday's feedback on Wednesday, so the repo has to remember it for them.



Never skip leg day. What does your Sprint Zero look like? I'd genuinely like to know.


![GIF of Coach McMurray from Letterkenny in a hockey locker room, yelling with wide eyes: "It's because you SKIPPED... LEG... DAY!!"](leg-day.gif)

Coach knows why the team didn't get the **W**.

*"It's because you SKIPPED... LEG... DAY!!" (Coach McMurray, Letterkenny). [GIF via Tenor](https://tenor.com/view/letterkenny-coach-leg-day-gif-376703195721350186).*

[Comment on LinkedIn if this story resonated with you](https://www.linkedin.com/posts/aaronheld_ai-neverskiplegday-foundations-activity-7494095059928104960-GrZs/)

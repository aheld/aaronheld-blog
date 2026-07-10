# Outline: If Erling Haaland Were a Software Engineer, He'd Never Get Promoted

**Content type**: Pattern B (standard post)
**Word target**: 1000–1300
**Estimated drafting time**: ~1 hour

Working slug: `haaland-wouldnt-get-promoted`
Inputs: `01_research/haaland-wouldnt-get-promoted/` (sources.md, contrarian-view.md, draft-input.md), checkpoint-approved 2026-07-09.

## Opening Hook (final, not draft)

> I once had to fight to promote one of the best developers I've ever worked with. The CTO's pushback came in one sentence: "They were never in the war room."

(Bridge, still in the hook zone: the CTO wasn't wrong about the facts. They were never in the war room, because their systems never created one. Flawless execution, quiet culture builder; that detail lands here, not in the hook. Then the pivot: I finally found the right way to explain what was wrong with that sentence while watching a video about Erling Haaland. Note: the promotion ultimately went through; that resolution is held back until the close, where it pays off the prescription.)

Anonymization note (2026-07-10): no name or initial for the developer anywhere in the piece; "they/them" throughout. The internal research files use 'E' as shorthand, but that stays out of the published post.

## Section Beats

### The deadliest player on the pitch is walking

- Purpose: establish the sports mirror of E. Haaland looks disengaged by every activity metric and is the best finisher alive by the only metric that decides matches.
- Draws on: The New Media Co video (link it); StatMuse and Total Football Analysis numbers from sources.md; World Cup 2026 sources (sources.md).
- Notes:
  - **Timeliness (World Cup)**: introduce him as Norway's striker, the man dragging his country through its historic first World Cup run this summer: 7 goals in his first 4 matches (best World Cup debut since Lato in 1974), including the brace that knocked out Brazil in the round of 16. Even readers who don't follow club football have watched him this month. Phrase it to survive whatever happens after July 10 (the "first quarterfinal in Norway's history" fact is already banked; don't predicate anything on later results).
  - ~24 touches per 90, near the bottom of the Premier League for regular starters. A full 90 minutes against Arsenal with 9 touches. Once completed 3 passes in a match and still scored.
  - The Kane contrast from Aaron's draft: box-to-box, tracking back, linking play, dominating the telemetry. Haaland is invisible on those sheets.
  - Land the record: debut Premier League season, 36 goals, broke the league record, won the treble. Lowest touches-per-shot in Europe.
  - Keep Aaron's line (lightly adapted): he conserves his energy to execute flawlessly in the high-percentage zones that actually matter.
  - Constraint check: correct the draft's "30 touches" to ~24; use real numbers throughout.

### The hero anti-pattern

- Purpose: name what the war room comment actually rewards. Visibility reads as value; firefighting is the most visible work in engineering.
- Draws on: Repenning & Sterman (CMR 2001); Batman post lineage; Deming.
- Notes:
  - Keep the draft's texture: 3 AM war rooms, loud triage, high-drama deployments, Slack shout-outs.
  - Quote the paper title as the punchline: "Nobody ever gets credit for fixing problems that never happened" (credit: Repenning & Sterman, California Management Review, 2001; the line came from an auto-company engineer).
  - IMPORTANT rewrite from contrarian-view.md: do NOT moralize the heroes. Cut the draft's "firefighting the consequences of their own creations" as a blanket claim. The system manufactures firefighting by rewarding it; most heroes are good people responding to the incentives in front of them. Deming from the Batman post: "a bad system will beat a good person every time." One sentence can acknowledge that sometimes the arsonist and the firefighter are the same person, but the indictment is of the reward system.
  - Callback available: "Batman is a Terrible Executive" already argued the superhero-swooping-in pattern at the exec level; internal link.

### We've been counting the wrong things for forty years

- Purpose: the "nothing unprecedented" move. Activity metrics are a generational relapse, not a new mistake.
- Draws on: Folklore.org (-2000 lines); McKinsey 2023 + Kent Beck / Gergely Orosz response; Goodhart via Strathern; the QA lead anchor.
- Notes:
  - 1982: Apple's Lisa team starts weekly lines-of-code reports. Bill Atkinson rewrites QuickDraw's region routines 6x faster and 2,000 lines shorter, files "-2000," management stops asking. Link Folklore.org.
  - 2023: McKinsey publishes "Yes, you can measure developer productivity"; Kent Beck and Gergely Orosz dismantle it for counting effort and output instead of outcomes. Same fallacy, prettier dashboard.
  - The QA lead story lands here: embedded with engineering during development, prevented bugs instead of finding them, and the bugs-found count dropped. Leadership read better quality as less work. The metric punished exactly the improvement it existed to encourage.
  - Name Goodhart's law once, with Strathern's phrasing: "When a measure becomes a target, it ceases to be a good measure."

### But football has a scoreboard

- Purpose: the contrarian acknowledgment, engaged honestly, then answered. This is the section that turns the objection into the prescription.
- Draws on: contrarian-view.md (all of it); Roy Keane quote; Tanya Reilly "Being Glue"; Aaron's business-metrics reframe.
- Notes:
  - Steelman first: goals are unambiguous and instantly attributed. A flat dashboard is also what coasting looks like. Even football has this argument: Roy Keane on Haaland, "in front of goal he's the best in the world, but his general play... he's almost like a League Two player." Every calibration room has a Roy Keane, and he isn't a fool.
  - One honest paragraph for glue work (Tanya Reilly, "Being Glue"): the third player the noisy-hero vs. quiet-finisher binary misses. Highly active, highly visible, still unpromoted because the activity isn't "technical enough." Proof the real axis is legibility vs. value, not activity vs. outcomes. (Also: Haaland only affords to walk because ten teammates run.)
  - Then the answer (Aaron's reframe from research checkpoint): software does have a goals column. It's the business scoreboard: revenue, uptime, cost, churn, conversion. What football gets for free is attribution; a goal arrives with the scorer's name on it, while business outcomes arrive unattributed. The leadership job is mapping engineering effort to those outcomes. Activity metrics are what you get when that mapping work is skipped and the gap is filled with whatever is easiest to count.
  - The prescription is honest and harder: don't assume your quiet engineers are Haalands; do the attribution work to tell walking-with-purpose from walking away. The developer from the opening made it easy: always ready during incidents, systems that never paged. The evidence existed. It just wasn't on the dashboard.
  - Optional single sentence to preempt comments: better frameworks (DORA, SPACE) don't rescue you from this; they only work in the hands of leaders already willing to do the mapping. Do not expand further.
  - Optional credited quote if space allows, Deming quoting Lloyd Nelson: "The most important figures that one needs for management are unknown or unknowable." (Verify wording before draft.)

## Closing (final, not draft)

> That promotion went through, but only because someone in the room was willing to argue with the dashboard. Their systems never gave them a war room to be seen in. That was the whole point.
>
> Haaland's club doesn't pay him to touch the ball. They pay him to put it in the net, and the scoreboard settles the argument. Our scoreboard exists too. We just have to do the harder work of connecting the quiet effort to it. So before your next calibration cycle, look again at the flattest dashboard on your team. Are we promoting the people who make the most noise, or the people who score?

(Publish stage appends the "Comment on LinkedIn" link below this.)

## Contrarian View Placement

Section 4 ("But football has a scoreboard") engages the full steelman: the attribution asymmetry, the quiet-coaster problem, Roy Keane as the credible skeptic, and the glue-work complication. Additionally, the hero-blame correction from contrarian-view.md is applied inside section 2 (indict the system, not the heroes), keeping the piece consistent with the Batman post's Deming lineage.

## Signature Moves Used

- **Concrete-scene opener**: the promotion scene, with the CTO's sentence verbatim.
- **Personal-then-systemic-then-personal**: the promotion scene opens, the system gets indicted in the middle, the same scene closes.
- **Pop-culture lens (sports variant)**: Haaland as the vehicle; the post is about promotion systems, not football.
- **"Nothing unprecedented" historical parallel**: Atkinson's -2000 lines (1982) → McKinsey vs. Beck/Orosz (2023).
- **Credited quote**: Repenning & Sterman title quote; Strathern's Goodhart phrasing; optionally Deming/Nelson.
- **Contrarian acknowledgment**: section 4, built from contrarian-view.md.
- Not used: Rod Serling frame (considered in research, doesn't fit; the piece opens on a real scene, not a fable).

## Scope honesty check

Four H2 sections, hook and close already locked, all stats and quotes pre-gathered in sources.md with URLs. Each section is 200–350 words. This drafts in one sitting.

## Front matter notes for draft stage

- Title (locked, per Aaron 2026-07-10): "If Erling Haaland Were a Software Engineer, He'd Never Get Promoted". Full name "Erling Haaland" stays in the title for World Cup search traffic.
- Description candidate: "Norway's striker is tearing up the World Cup while failing every activity metric we use to evaluate engineers. What Haaland's walking says about war rooms, dashboards, and who actually gets promoted."
- Categories: ["professional"]. Tags: management, metrics, leadership, engineering-culture.
- Cover image: required. Retro/vintage football imagery via Unsplash (the `unsplash-retro-landscape` skill fits). Alt text non-negotiable.
- Internal links: "Batman is a Terrible Executive," "the measure of Awesome" (2011 callback is available if it fits naturally in section 3; don't force it).
- **Publish timing**: the piece capitalizes on live World Cup attention. Norway plays its first-ever quarterfinal Saturday, July 11. Draft and publish while the tournament (and ideally Norway) is still alive; every day of delay costs relevance. Facts in the post must be tournament-proof: cite only what has already happened (7 goals in first 4 matches, Brazil eliminated, first quarterfinal in history).

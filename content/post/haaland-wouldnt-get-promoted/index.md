---
title: "If Erling Haaland Were a Software Engineer, He'd Never Get Promoted"
date: 2026-07-10T09:00:00-04:00
draft: false
description: "Norway's World Cup hero fails every activity metric we track. What Haaland's walking says about war rooms, dashboards, and who gets promoted."
categories: ["professional"]
tags: ["management", "metrics", "leadership", "engineering-culture"]
cover:
  image: "cover.jpg"
  alt: "Erling Haaland in Norway's white number 9 kit, smiling and relaxed during the Morocco vs Norway match in June 2026, with a blurred crowd behind him"
  caption: "Erling Haaland, Morocco v Norway, June 2026. Photo by [Bryan Berlin](https://commons.wikimedia.org/wiki/File:Erling_Haaland_Morocco_v_Norway_7_June_2026-128.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons (cropped)"
---

Recently I caught up with a colleague who was one of the best developers I've ever worked with. They were also the hardest person to promote.

The CTO's pushback to my request came in one sentence: "They were never in the war room."

The CTO wasn't wrong about the facts. They were never in the war room, because their systems never warranted one. Everything they shipped was resilient against the failure modes we had, documented well enough that other teams and users could answer their own questions, and boring in the way that well executed systems are boring. On top of that, culturally, they made the people around them better, quietly, without ever boasting about it.

I didn't have the right words for what was wrong with that sentence until I watched a breakdown of Erling Haaland's play style.

## The deadliest player on the pitch is walking

If you've caught any of the World Cup this summer, you've watched Haaland. Norway's striker has scored seven goals in his country's first four matches, the best debut at a World Cup since 1974, and his two goals against Brazil just sent [Norway to the first quarterfinal in its history](https://www.bbc.com/sport/football/live/c3wyl9qe4xgt).

My dad would be 'loudly coaching' from the sidelines if I ever walked the field looking as disengaged as Haaland does.

There's a video called [Why Haaland Walks Almost the Entire Game](https://www.youtube.com/watch?v=_CVK1Kf_rJY) that unpacks it. (Unfortunately it's an AI generated video, but YouTube recommended it so I watched it.) At Manchester City, Haaland averages [about 24 touches per 90 minutes](https://www.statmuse.com/fc/ask/haaland-touches-per-game?l=eu5), near the bottom of the Premier League for regular starters. Last year he played a full match against Arsenal and touched the ball nine times. He once completed three passes in ninety minutes, the first player to do that under Pep Guardiola, and still scored. Nobody in Europe's top leagues needs fewer touches per shot.

Meanwhile, a "complete" striker like Harry Kane runs box-to-box, drops deep to link play, tracks back, argues with the refs, and fills every column of the telemetry sheet. By those columns, Haaland is invisible. If you evaluated him on continuous activity, you'd conclude he was slacking.

Then you check the only column that decides matches: goals. In his first Premier League season he scored 36, broke the single-season record, and City won the treble. He conserves nearly all of his energy, then spends it flawlessly in the few high-percentage moments that actually matter.

Put him on an engineering dashboard and he'd look scaled down to zero.

## The hero anti-pattern

In tech, we love a hero. The engineers who get the shout-outs in Slack and the fast-track promotions are almost always the ones leadership sees in the trenches: commandeering the 3 AM war room, loudly triaging a production outage, sweating through a high-drama deployment. Visibility reads as commitment. Noise reads as impact.

Two MIT researchers, Nelson Repenning and John Sterman, studied this pattern twenty-five years ago and gave their paper a title I think about constantly: [Nobody Ever Gets Credit for Fixing Problems that Never Happened](https://web.mit.edu/nelsonr/www/Repenning=Sterman_CMR_su01_.pdf). Organizations that depend on firefighting, they found, reward and promote the people who perform heroics when the line goes down, and quietly starve the prevention work that would keep it from going down at all. The quote in their title came from an engineer at a car company. It could have come from an engineer at any company I've worked with.

I've been in those war rooms. Most of the people in them are good engineers responding to the incentives in front of them, and while sometimes the firefighter and the arsonist are the same person, more often the fire was inherited and somebody had to put it out. The blame belongs upstream, with the reward system. W. Edwards Deming said it plainly: "A bad system will beat a good person every time." I made a version of this argument about executives in [Batman is a Terrible Executive](https://www.aaronheld.com/post/batman-is-a-terrible-executive/): an organization that keeps needing a superhero has a systems problem. When promotions pay out in glory-per-incident, everyone learns that the fastest way up is through the flames.

## We've been counting the wrong things for forty years

None of this is new. In 1982, managers on Apple's Lisa team started requiring engineers to report how many lines of code they wrote each week. Bill Atkinson had just rewritten QuickDraw's region calculation routines to be six times faster and 2,000 lines shorter, so he wrote [-2000 on the form](https://www.folklore.org/Negative_2000_Lines_Of_Code.html). Management stopped asking him. For what it's worth, that developer I mentioned once removed 20,000 lines in a PR.

Forty-one years later, McKinsey published [Yes, you can measure developer productivity](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/yes-you-can-measure-software-developer-productivity), and the industry's most experienced voices lined up to take it apart. Kent Beck called it ["a naive approach to a complicated subject"](https://tidyfirst.substack.com/p/measuring-developer-productivity-440); Gergely Orosz wrote [a rebuttal](https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity) that boiled down to the lesson Atkinson taught with a single number: the framework counted effort and output, not outcomes and impact. Same fallacy, prettier dashboard. Commits and Jira tickets are lines of code with better UX.

I watched a quieter version of this happen to a QA lead I worked with. Instead of waiting at the end of the pipeline to catch defects, they embedded with engineering during development: reviewing designs, pairing on edge cases before the code existed. Quality went up. And the number of bugs found during the formal QA cycle went down, because the bugs never made it that far. Leadership read the declining count as QA doing less work. The metric punished exactly the improvement it existed to encourage.

There's a name for this: Goodhart's law, generalized by the anthropologist Marilyn Strathern as "when a measure becomes a target, it ceases to be a good measure." I bumped into it myself fifteen years ago, when I told a developer on my team that [awesome is not a metric](https://www.aaronheld.com/post/the-measure-of-awesome/) and then spent the next week realizing that the things that matter most on a team can only be observed through their secondary effects. The count is never the thing. The count is a shadow of the thing.

## But Soccer has a scoreboard

The obvious objection: soccer makes this easy. A goal is unambiguous, instantly attributed, and updated in real time. Yet the activity bias runs so deep that Haaland catches it anyway. Roy Keane, one of the most respected voices in English football, watched him against Arsenal and said ["in front of goal he's the best in the world, but his general play... is so poor. He's almost like a League Two player."](https://www.sportbible.com/football/football-news/man-city/man-city-erling-haaland-roy-keane-league-two-228255-20240510) The best finisher on Earth, with the scoreboard fully on his side, still gets dinged for not looking busy enough. Every calibration room has a Roy Keane, and he isn't a fool. He's describing something real. He's just weighing it wrong.

There's also a third kind of player that the hero-versus-finisher binary misses. Tanya Reilly calls it [glue work](https://www.noidea.dog/glue): the unblocking, onboarding, design-reviewing, direction-keeping labor that decides whether a project ships. It's visible in every meeting and still doesn't get promoted, because it isn't "technical enough." It's disproportionately done by women, and it gets punished by both lenses: too much activity for the outcome purists, the wrong kind of outcome for the dashboard. That contradiction exposes the real axis: legibility versus value. Haaland only gets to walk because ten teammates run. Somebody plays the linking role, and a promotion system has to be able to see them too.

Engineering does have a scoreboard; yet so many keep forgetting to look at it. Revenue, uptime, cost, churn, retention: the business metrics are our goals column. What soccer gets for free is attribution. A goal arrives with the scorer's name already on it, as well as the player who initiated the pass. Business outcomes arrive unattributed, lagged by quarters, and shared across teams. Mapping quiet engineering effort onto that scoreboard is genuinely hard work, and it's precisely the leadership job. Activity metrics are what you get when that job gets skipped and the gap is filled with whatever's easiest to count. Better frameworks won't rescue you either; DORA and SPACE only work in the hands of leaders already willing to do the mapping.

So the prescription is attribution work, and it cuts both ways: trace the boring system back to the incidents that never happened, the on-call rotation nobody dreads, the teams that answer their own questions because someone chose to write the documentation. Some flat dashboards really are flat, and the same tracing will tell you that too. Learn to tell walking-with-purpose from walking away. The developer I fought for made it easy: always ready when incidents did happen, systems that never paged. The evidence existed. It just wasn't on the dashboard.

That promotion went through, but only because someone in the room was willing to argue with the dashboard. Their systems never gave them a war room to be seen in. That was the whole point.

Haaland's club doesn't pay him to touch the ball. They pay him to put it in the net, and the scoreboard settles the argument. Our scoreboard exists too. We just have to do the harder work of connecting the quiet effort to it. So before your next calibration cycle, look again at the flattest dashboard on your team. Are we promoting the people who make the most noise, or the people who ensure the team puts points on the board?

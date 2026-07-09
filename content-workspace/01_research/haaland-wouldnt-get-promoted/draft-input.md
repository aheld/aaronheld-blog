# Aaron's rough draft (input, pre-pipeline)

Captured 2026-07-09. This is the raw draft Aaron walked in with. It feeds research and outline; the 03_draft stage rewrites it in voice rather than editing it in place.

---

If Erling Haaland were a software engineer, he would be the hardest person on your team to promote.

I was watching a breakdown of his play style recently, and it perfectly highlights a trap that engineering leadership falls into every single day: mistaking visibility for velocity.

By almost every metric we track on a team dashboard, Haaland looks completely disengaged. He spends most of the match literally walking. He barely touches the ball—sometimes only 30 times a game. While "complete" players like Harry Kane run box-to-box, tracking back, linking play, and dominating the telemetry sheets, Haaland is invisible.

If you evaluated him purely on continuous activity, you'd think he was slacking. But then you look at the ultimate business outcome: Goals. He's the deadliest scorer on Earth because he conserves 100% of his energy to execute flawlessly in the high-percentage zones that actually matter.

This is exactly how we mismanage our highest-performing engineers.

## The "Hero" Anti-Pattern

In tech, we love a hero. The engineers who get the shout-outs in Slack and the fast-track promotions are almost always the ones leadership sees in the trenches:

- Commandeering the 3 AM war rooms.
- Loudly triaging production outages.
- Sweating through high-drama deployments.

But here is the uncomfortable truth we rarely talk about: The heroes are all too often firefighting the consequences of their own creations. They get the glory for fixing problems that only exist because they wrote "good enough" code that lacked resilience, robustness, or documentation in the first place. They are visible because they are noisy.

## The Quiet High-Performer

Meanwhile, your "Haaland" engineer is sitting quietly. To an outside observer, they might even look disengaged. They don't show up in triage, they aren't typing furiously in the incident channel, and they aren't pulling all-nighters.

Why? Because they designed a system that just works. They anticipated the edge cases, built the guardrails, and wrote the documentation. There is no emergency for them to fix because they eliminated the emergency before it could happen.

Like Haaland, they don't waste energy sprinting across the whole field just to look busy. They save their burst capacity for the exact 5 meters where they deliver maximum business value.

## The Leadership Challenge

This is deeply unsatisfying for managers who live in observability and proxy metrics. It is easy to count commits, Jira tickets, or war room appearances. It is much harder to quantify the absence of chaos.

When you look at a quiet engineer whose dashboard is flat, don't automatically assume they are scaled down to zero. They might just be your deadliest finisher, waiting to ship the exact architecture that wins the game.

Are we promoting the people who make the most noise, or the ones who actually score the goals?

---

## Notes from research stage (2026-07-09)

- The reference video: "Why Haaland Walks Almost the Entire Game" — The New Media Co, https://www.youtube.com/watch?v=_CVK1Kf_rJY
- The "~30 touches" figure is generous; real number is ~24 touches per 90, with a 9-touch full match vs Arsenal (Feb 2025). See sources.md.
- The "heroes firefight their own creations" claim got flagged in contrarian-view.md as the draft's most attackable line — it moralizes what Repenning & Sterman (and Deming) show is a system property.

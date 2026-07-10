# Research: If Erling Haaland Were a Software Engineer, He'd Never Get Promoted

Working slug: `haaland-wouldnt-get-promoted`
Stage: 01_research
Input: Aaron's rough draft (see `draft-input.md` in this folder) + reference video.

## Premise (one sentence)

Engineering leadership systematically rewards visible activity over quiet outcomes, and Erling Haaland proves the trap: by every activity metric he looks disengaged, yet he is the deadliest finisher on Earth.

Aaron to approve or sharpen at checkpoint.

## Theme Connections

- **Process as servant, not master** (`_config/themes.md`): activity metrics are process artifacts. When the dashboard becomes the point, the system is measuring its own noise. This is the core theme the piece engages.
- **Middle-manager survival and "do no harm"**: the practical challenge lands on managers. How do you defend a quiet high-performer in calibration when their dashboard is flat? The piece is partly a field guide for that conversation.
- **"Nothing we are seeing is unprecedented"**: activity-as-productivity has been debunked at least once per generation (see Historical Parallel below) and keeps coming back wearing new tooling.
- **The social contract between companies and employees** (secondary): promotion systems are where the social contract gets enforced or betrayed. Rewarding noise over outcomes is a quiet rewrite of the deal.

### Prior Aaron posts (direct lineage)

- **"the measure of Awesome" (2011-01-23)** — `content/post/the-measure-of-awesome/` — Aaron told a developer "awesome is not a metric," then walked it back within a week: "We simply have not developed the tools to measure and understand this thing we call 'awesome'. I can only observe the secondary effects." Fifteen years later, this Haaland piece is the mature answer to that younger post. Strong callback candidate.
- **"Batman is a Terrible Executive"** — `content/post/batman-is-a-terrible-executive/` — already argues the hero anti-pattern at the executive level: "True executive sponsorship isn't about being a superhero who swoops in to save the day." This piece extends the same argument down to the IC level. Deming's "a bad system will beat a good person every time" was the anchor quote there, and it matters here too (see contrarian-view.md).
- **"The North Star Vision for Engineering"** — `content/post/the-north-star-vision-for-engineering/` — draws the metric-vs-vision distinction ("a metric, not a vision"). Adjacent, linkable.

## Historical Parallel

**Lines of code, 1982.** When Apple's Lisa team started requiring engineers to file weekly forms reporting lines of code written, Bill Atkinson rewrote QuickDraw's region calculation routines to be six times faster and 2,000 lines shorter, and wrote **"-2000"** on the form. Management quietly stopped asking him. ([Folklore.org: -2000 Lines Of Code](https://www.folklore.org/Negative_2000_Lines_Of_Code.html))

The replay arrived on schedule: in August 2023 McKinsey published "Yes, you can measure developer productivity," and the industry's most credible practitioners (Kent Beck, Gergely Orosz, Dan North) tore it apart on exactly the grounds Atkinson demonstrated 41 years earlier — the proposed metrics count effort and output, not outcomes and impact. Forty years, same trap, new dashboard. Commits and Jira tickets are lines-of-code with better UX.

This is the "nothing unprecedented" move for the piece: the tooling to measure activity keeps improving, which makes the fallacy *more* dangerous, not less, because the dashboards are prettier and more trusted now.

## Sources

### The reference video

- **Author / Source**: The New Media Co (YouTube)
- **Title**: "Why Haaland Walks Almost the Entire Game"
- **URL**: <https://www.youtube.com/watch?v=_CVK1Kf_rJY>
- **Relevance**: the piece's seed. Breaks down Haaland's play style: walking most of the match, minimal touches, total energy conservation for the few moments in the box that decide games. The Kane contrast (box-to-box, link play, dominates every stat sheet except the one that wins matches) comes from here.

### Haaland's actual numbers

- **Source**: StatMuse + Total Football Analysis
- **URLs**: <https://www.statmuse.com/fc/ask/haaland-touches-per-game?l=eu5> , <https://www.statmuse.com/fc/ask/lowest-touches-in-a-match-with-90-minutes-played-by-haaland> , <https://totalfootballanalysis.com/thought-analysis/erling-haalands-off-ball-movement-and-finishing-efficiency>
- **Relevance**: grounds the hook in verifiable numbers instead of vibes.
  - ~24.2 touches per 90 — among the *lowest* in the Premier League for regular starters.
  - 9 touches in a full 90 minutes vs Arsenal (Feb 2, 2025).
  - Once completed just **3 passes in 90 minutes** — the first player to do so under Pep Guardiola — and still scored.
  - Lowest touches-per-shot of any player in Europe's top five leagues (~6). He is the least "active" player and the most lethal, simultaneously.
- **Note**: his debut season (2022-23) he broke the Premier League goal record (36) while ranking near the bottom of every activity stat. That season ended in the treble.

### World Cup 2026 (timeliness hook, added 2026-07-10)

- **Sources**: Al Jazeera, Yahoo Sports, FIFA.com
- **URLs**: <https://www.aljazeera.com/sports/2026/7/5/haaland-scores-twice-as-norway-stun-brazil-2-1-in-world-cup-2026-last-16> , <https://sports.yahoo.com/soccer/article/2026-world-cup-erling-haaland-takes-his-star-turn-on-soccers-global-stage-as-he-leads-norway-on-a-historic-run-040023486.html> , <https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/haaland-inspiring-norways-history-makers-after-eliminating-brazil>
- **Date**: July 2026 (tournament in progress at time of writing)
- **Relevance**: Aaron's call (2026-07-10): keep "Erling Haaland" in the title and identify him as Norway's striker to ride live World Cup attention. Facts banked as of July 10:
  - Norway's first World Cup since 1998; Haaland's World Cup debut.
  - 7 goals in his first 4 matches, a goal every 51 minutes, best debut tournament since Grzegorz Lato's 7 for Poland in 1974.
  - Brace to beat Brazil 2-1 in the round of 16 (July 5), sending Norway to its first-ever quarterfinal and Brazil to its earliest exit since 1990.
  - Quarterfinal vs England, Saturday July 11. **Post must only cite results that have already happened**; publish while the tournament is live.

### Repenning & Sterman — the academic anchor

- **Author / Source**: Nelson P. Repenning & John D. Sterman, *California Management Review* 43(4), 2001
- **URL**: <https://web.mit.edu/nelsonr/www/Repenning=Sterman_CMR_su01_.pdf> (also <https://mitmgmtfaculty.mit.edu/jsterman/nobodyevergetscredit/>)
- **Date**: 2001
- **Relevance**: the definitive study of the hero anti-pattern. Organizations dependent on firefighting "reward and promote those who, through heroic efforts, manage to save troubled projects or keep the line running," and consequently reward last-minute problem solving over the prevention work that would eliminate the crises.
- **Quote**: "Nobody ever gets credit for fixing problems that never happened." (an auto-company engineer, quoted in the paper's title)

### The -2000 lines story

- **Author / Source**: Andy Hertzfeld, Folklore.org
- **URL**: <https://www.folklore.org/Negative_2000_Lines_Of_Code.html>
- **Date**: story from early 1982
- **Relevance**: historical parallel (above). Also the purest available example of an outcome (6x faster, 2,000 lines lighter) that scores *negative* on the activity metric.

### McKinsey vs. the practitioners (2023)

- **Author / Source**: Kent Beck & Gergely Orosz rebuttal to McKinsey's "Yes, you can measure developer productivity"
- **URLs**: <https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity> , <https://tidyfirst.substack.com/p/measuring-developer-productivity-440> , <https://mozaicworks.com/blog/reactions-to-mckinseys-dev-productivity-metrics-kent-beck-gergely-orosz-and-dan-north>
- **Date**: August–September 2023
- **Relevance**: proof the debate is live, not historical. Beck called the McKinsey framework "a naive approach to a complicated subject"; the core objection is that four of its five metrics measure effort and output rather than outcomes and impact. Also useful: their recommendation to measure like sales does — outcomes (deals closed), not activity (calls made). Haaland is measured like sales. Goals are his closed deals.

### Goodhart's Law

- **Author / Source**: Charles Goodhart (1975, monetary policy); generalized by Marilyn Strathern, "'Improving Ratings': Audit in the British University System" (1997)
- **URL**: <https://en.wikipedia.org/wiki/Goodhart%27s_law>
- **Relevance**: the theoretical backbone in one line. Strathern's phrasing: "When a measure becomes a target, it ceases to be a good measure." If touches-per-game became a target, Haaland would demand the ball at midfield and score fewer goals. Engineers who know commits are counted produce more commits.

### W. Edwards Deming (recurring shelf, `_config/recurring-references.md`)

- **Source**: *Out of the Crisis* (1982); Deming quoting Lloyd S. Nelson
- **Relevance**: "The most important figures that one needs for management are unknown or unknowable." This is the precise sentence for the piece's hardest claim: the absence of chaos cannot be counted. Deming already on Aaron's shelf via the Batman post. *(Verify exact wording against the book before draft; the Nelson attribution is per Deming himself.)*

## Aaron's career anchors for this piece (captured 2026-07-09)

Two first-hand scenes, both anonymized, both stronger than any borrowed example:

### The promotion of 'E'

Aaron promoted a developer ('E') who was one of the best he'd worked with on both execution and culture-building, but he had to fight for it. The CTO's literal pushback: **"they were never in the war room."** E's systems simply didn't fail. And E was always ready to assist during incidents — the absence wasn't disengagement, it was the absence of emergencies E's own work had created. The promotion ultimately went through; the point is that it was *harder to promote a good person* because the reward system couldn't see quiet excellence. This is the opener: the moment the reward system said the quiet part out loud. It's also the piece's Repenning & Sterman quote made flesh: nobody got credit for the incidents that never happened. (Anonymization: no name or initial in the published piece; 'E' is internal shorthand only.)

### The QA lead whose numbers "got worse"

A QA lead Aaron worked with embedded directly with engineering during development — catching issues at design and build time instead of after the fact. The result: fewer bugs found during the formal QA cycle. Leadership read the declining bugs-found count as **QA doing less work**. A pure Goodhart's Law case, and proof the pattern isn't unique to engineers: the better the prevention, the worse the activity metric looks. The metric punished the improvement it should have celebrated.

**Note for outline**: the E story carries the promotion thread (matches the title); the QA story generalizes the pattern and lands the Goodhart point without needing the law named first. Together they replace the need for a purely hypothetical "quiet engineer."

## Resolved at research checkpoint (2026-07-09)

- **The "software has no goals column" objection** (contrarian-view.md #1) is answered, not conceded: the goals column is the *business metrics* (revenue, uptime, cost, churn). What football gets for free is attribution — a goal carries the scorer's name; business outcomes arrive unattributed. The leadership job is mapping engineering effort to those outcomes, and activity metrics are the lazy substitute for doing that mapping. This becomes the piece's central prescription. See contrarian-view.md "Where this leaves the piece."

## Open questions for outline stage

- Does the piece name DORA/SPACE as "better metrics done right," or stay out of the frameworks weeds entirely? (Leaning: one sentence, no more. The piece is about judgment, not a framework bake-off.)
- The Rod Serling frame probably does NOT fit here; the concrete-scene opener (watching the video, checking the stats) fits naturally. Decide in outline.

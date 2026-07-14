# Sources — Documenting Architecture with Video

**Piece premise**: Document the same system (the Market Finder harvester) twice, once as static C4 diagrams + prose, once as an animated explainer video. Measure the effort of each, assess the effectiveness of each, and draw honest conclusions about when each medium earns its cost.

## Internal artifacts (the experiment itself)

- `harvestor-architecture.md` (this folder) — the **control**: complete static documentation of the harvester. C4 Context/Container/Component + dynamic flow + prose on the four loop mechanisms. Its own Section 8 states the thesis seed: structure photographs well, but the loop (state, gates, feedback) has to be animated in the reader's head.
- `harvestor-context.svg`, `harvestor-container.svg`, `harvestor-component.svg`, `harvestor-flow.svg` (this folder) — the four diagrams. These are also the planned **base layers for the video**, which matters for the effort comparison: the video's cost is incremental on top of the diagrams, not from zero.
- Source of record for the system: `markets_app/harvestor/README.md`, `markets_app/docs/plans/harvestor-phase-c.md`, `markets_app/docs/plans/phila-harvest-two-pass.md` (separate repo).

## Prior Aaron posts (found via grep over content/post/)

- [The Island of Misfit Toys: Making the Azure Private Link Video](/post/making-the-azure-private-link-video/) — the direct predecessor. Establishes the video workflow (research first, script, Remotion, diagram-style visual language, no character animation) and the "AI makes it easy to drift from the goal" lesson. This piece inherits that workflow and should link back.
- [Streamlining Blog Writing with Claude Code](/post/streamlining-blog-writing-with-claude-code/) — the workflow-philosophy sibling: break large work into smaller deliverables with the right context at each step. The two-artifact experiment is that philosophy applied to documentation.

## External references (verify links/editions before publish)

- **Simon Brown, the C4 model** — https://c4model.com — the framework the static doc uses (Context, Containers, Components). Brown himself notes C4 diagrams are static structure and recommends supplementary dynamic diagrams for runtime behavior. Useful to cite so the post criticizes C4 fairly (using it as designed, not as a straw man).
- **Diátaxis framework** — https://diataxis.fr — documentation taxonomy (tutorials, how-to, reference, explanation). Sharpens the comparison: the static doc is *reference + explanation*; the video is *explanation* only. They are not competing for the same job, which the post must acknowledge or the comparison is rigged.
- **Barbara Tversky, Julie B. Morrison, Mireille Bétrancourt, "Animation: Can It Facilitate?"** — International Journal of Human-Computer Studies 57(4), 2002 — the classic skeptical result on animation for learning: when static and animated graphics carry equivalent information, animation frequently fails to outperform, partly because motion is transient (the viewer can't dwell or re-inspect). Core contrarian ammunition; see `contrarian-view.md`.
- **Richard E. Mayer, *Multimedia Learning*** (Cambridge University Press; 3rd ed. 2020) — the counterweight to Tversky: narration + synchronized visuals engage dual channels; the signaling and temporal-contiguity principles are exactly what an architecture video exploits (arrow lights up as the narrator says the words). Also supplies the redundancy warning: don't put the transcript on screen.
- **Remotion** — https://www.remotion.dev — the production tool (React-based programmatic video). Continuity with the Private Link video; makes "effort" measurable in developer-familiar terms.
- **Write the Docs community, docs-as-code** — https://www.writethedocs.org — the maintainability orthodoxy the video violates: documentation should be diffable, reviewable, greppable, versioned with the code. A rendered MP4 is none of these. Feeds the contrarian view and the "when to use which" conclusion.

## Facts to capture during production (needed for the article)

- [ ] Hours spent producing the static doc + 4 SVG diagrams (Aaron: retroactive estimate, honest).
- [ ] Hours spent on video: script, Remotion build, narration, revisions, render/publish (log as we go in `03_draft/documenting-architecture-with-video/effort-log.md`).
- [ ] Out-of-pocket costs for each (API spend, licenses, stock assets, if any).
- [ ] At least one naive-reader / naive-viewer data point per artifact (a colleague who reads the doc vs. one who watches the video, asked to explain the loop back). Without this the "effectiveness" half of the comparison is vibes; see contrarian view.

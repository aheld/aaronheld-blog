# Summary — Making the Azure Private Link Video

**Slug**: `making-the-azure-private-link-video`
**Live URL**: <https://www.aaronheld.com/post/making-the-azure-private-link-video/>
**Published**: 2026-04-26
**Word count**: ~1,760
**Format pattern**: Pattern B (tutorial / standard post), upper end

## One-paragraph compression

A meta-post about producing a 5-minute Azure Private Link explainer video. Aaron started with a Claude-assisted DNS deep-dive (CNAME chain, the `168.63.129.16` resolver, Private DNS Zone linking) that no viewer would ever see but every claim in the video would lean on. He then wrote a v1 script: a six-act animated short with named characters (Slonik the PostgreSQL elephant, Ricky the Raccoon in three costumes, a stagehand, a circus tent representing all of Azure). It was funny, it was technically correct, and it had quietly stopped being an explainer about Private Link. Aaron pivoted to a v2 of architecture diagrams, a numbered DNS resolution chain, and a flat raccoon silhouette who never speaks. v2 shipped at roughly a tenth of v1's production cost and lands the same lesson, plus one beat v1 didn't have (the privatelink CNAME exists in public DNS too, falling through to the public IP without a Private DNS Zone link). The post argues the cuts weren't the work; catching the drift was.

## Why this post exists (the social-impact statement)

This post tries to shift its reader's framing of AI-assisted content production from "scope discipline" to **drift discipline**. The familiar advice is "don't be too ambitious with AI." This post argues something else: the issue isn't ambition, it's quietly losing track of what the work was *for*. AI makes drafting cheap, which makes drift cheap, which means the practice that matters now is re-reading the brief halfway through and catching where you've wandered off. The post is also a worked example of `streamlining-blog-writing-with-claude-code`'s claim that workflows themselves have to keep refactoring as the tools move underneath you — making the misfit-toys post a sibling, not a one-off.

## What this post is canonically about

For future-Aaron's grep when a related topic comes up:

- **AI content production workflow** — research-first, then script, then animated production via Remotion, with ElevenLabs for narration
- **Drift discipline** — recognizing when an AI-assisted draft has stopped being the thing you meant to make
- **The pivot as the work** — why the v1-to-v2 rewrite is the post's center, not a side note
- **The cheapest-piece principle** — the throwaway in v1 (raccoon silhouette) became the only character in v2
- **Tooling refactoring** — sibling-post arc with `streamlining-blog-writing-with-claude-code`
- **Azure Private Link technical content** — DNS resolution chain, the privatelink CNAME public/private fork, the "Allow Azure services" trap

## Cross-references

- Sibling post: [Streamlining Blog Writing with Claude Code](/post/streamlining-blog-writing-with-claude-code/) — same workflow philosophy, text medium, made the original "break it down + right context per step" claim. The misfit-toys post is what that workflow looks like mid-refactor.
- Linked artifact (the video itself): <https://www.youtube.com/watch?v=EFtAm-Ao_kM>
- External tool credit: [Recraft](https://www.recraft.ai/generate/characters), called out in the close as the tool that made character animation feel reachable.

## What got captured as a feature request

Nothing this round. The post didn't surface a Hugo/PaperMod feature gap — the existing image, code-fence, and link rendering were sufficient. (If a future post about the *video itself* embeds the YouTube player inline, that may surface a shortcode preference. Defer until needed.)

## Stage notes (retrofit-specific)

This piece was retrofitted: a forward draft existed at `content/post/making-the-azure-private-link-video/` before the pipeline was applied. The retrofit produced `01_research/` (sources + contrarian view) and `02_outline/` (reverse-engineered) before re-entering at `03_draft/`. The retro-outline surfaced four structural weaknesses that drove a thesis-level revision pass — the published version is meaningfully different from the pre-retrofit draft. See `02_outline/.../outline.md` "Structural notes from the reverse-engineer" for the audit trail.

## Archive note

After publication and amplification per `_config/platforms.md`, this entire working folder (`01_research/`, `02_outline/`, `03_draft/` for this slug) moves to `_archive/making-the-azure-private-link-video/`. Per `CLAUDE.md` line 70, the published artifact lives in `content/post/`; only working files get archived here.

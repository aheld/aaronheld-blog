# Sources — Making the Azure Private Link Video

**Slug**: `making-the-azure-private-link-video`
**Stage**: 01_research (retrofitted — draft already exists in 03_draft/)
**Premise**: A meta-post about how an ambitious, character-driven video script (Slonik the elephant, Ricky the Raccoon in three costumes, a circus tent representing all of Azure) became a stripped-down architecture-diagram explainer because production capability couldn't catch up to AI-assisted writing capability.

This file captures the actual research and source materials that informed the existing draft. Most of these live in a separate workspace (`/Users/aheld/Projects/content-production/`) where the video itself was produced. The blog is downstream of that workspace.

---

## The shipped artifact (the thing the post is about)

- **Final video on YouTube**: [youtube.com/watch?v=EFtAm-Ao_kM](https://www.youtube.com/watch?v=EFtAm-Ao_kM)
- **Final Remotion source**: `/Users/aheld/Projects/content-production/03_production/output/private-link-video/`
  - `src/Root.tsx`, `src/timing.ts`, `src/layout.ts`, `src/theme.ts` — composition, timing, palette
  - `public/cute-hacker.json`, `public/ricky-hardhat.json` — Lottie assets that survived from the v1 character work and became the silhouette raccoon in the final
  - `scripts/generate-audio.mjs` — ElevenLabs TTS pipeline for narration
- **Final voiceover transcript**: `/Users/aheld/Projects/content-production/03_production/output/private-link-video/VOICEOVER.md` — timed table, 30 FPS, Brian voice. This is the script that actually got narrated. Roughly 5:15 total.

## The research that the script was built on

The blog's "Step 1: Research before script" section refers specifically to this document. Without it, the v1 and v2 scripts would have invented plausible-sounding DNS behavior that would have been wrong in subtle ways.

- **Azure Private Endpoints DNS Deep-Dive**: `/Users/aheld/Projects/content-production/01_research/output/azure-private-endpoints-dns-deep-dive.md` (515 lines)
  - The CNAME chain (`mydb.postgres.database.azure.com` → `mydb.privatelink.postgres.database.azure.com` → A record)
  - Azure DNS resolver `168.63.129.16` and how AKS CoreDNS forwards to it
  - Private DNS Zone linking, hub-and-spoke gotchas
  - Cited Microsoft Learn pages on Private Endpoint DNS, PostgreSQL networking, private AKS clusters, Azure CNI, CoreDNS customization
- **Supporting research files**:
  - `01_research/output/azure-private-link-research.md` (68 lines — short context summary)
  - `01_research/output/research-summary.md` (story-shaping notes; this one is actually about the *Universal Links* video, not Private Link — kept for reference because it shaped the meta-narrative the blog uses)
  - `01_research/output/postgres-outage-diagram.md` (84 lines — adjacent incident video that uses the same Remotion pipeline)

## The two scripts (the heart of the blog post)

These are the v1 ("too good to make") and v2 ("the honest version") drafts. The blog post is a retrospective on the gap between them.

- **v1 — character-driven, six-act, costume-changing**:
  `/Users/aheld/Projects/content-production/02_script/output/draft-explainer-video-azure-private-link.md` (328 lines)
  - Ricky in three costumes (hard hat, top hat, fedora) with full character physics
  - Slonik the PostgreSQL elephant behind a desk with a neon "OPEN FOR BUSINESS" sign
  - AKS as cute shipping containers with legs
  - The stagehand character who rolls a fake wall in front of the public door
  - The eight-lane highway terminating at a circus tent labeled "ALL OF AZURE: 1,000,000+ CUSTOMERS"
  - Two parallel paths (Internet / From Our Services) that visually evolve across the six acts
- **v1 duplicate**: `draft-explainer-video-azure-private-link copy.md` — identical content, kept because it was the file that got duplicated when v2 was forked off.
- **v2 — architecture-diagram, raccoon silhouette, numbered DNS chain**:
  `/Users/aheld/Projects/content-production/02_script/output/draft-explainer-video-azure-private-link-v2.md` (267 lines)
  - White/light-gray background, official Azure SVG icons, dashed rectangles for VNets/subnets
  - Raccoon as a flat silhouette of Azure's "Users" person icon plus ears and a mask band
  - Numbered circles ①②③④⑤ for the DNS chain — became the educational centerpiece
  - State changes via color shift (blue → red X for blocked) instead of pratfall
  - **Notable refinement, not just reduction**: v2 adds the `publicdnspath` / `publicdnspath2` beats — explaining that the `privatelink` CNAME exists in public DNS too, and without a linked Private DNS Zone it falls through to the public IP. This is *more* technical nuance than v1 had, contradicting a clean "I cut things" framing.

## The character work that didn't survive

Worth keeping because the blog leans on the visual specifics of "Slonik with a face, body, chair, desk."

- **Ricky character design brief**: `/Users/aheld/Projects/content-production/03_production/output/ricky-character-design-brief.md` — full design doc for the three costumes (hard hat, top hat & monocle, fedora), expression range, posture and movement, prop list. This is the level of fidelity the v1 script was reaching for.
- **Storyboard notes**: `/Users/aheld/Projects/content-production/03_production/output/storyboard-act1-wide-open-database.md`

## Sibling Aaron post (already linked from the draft)

- `/post/streamlining-blog-writing-with-claude-code/` — same workflow philosophy, different medium (text). The draft closes by pointing here. Worth re-reading for tone consistency since the two posts are explicitly cross-referenced.

## Adjacent posts to grep for tone / overlap

`grep -ri "AI" /Users/aheld/Projects/aheld/aaronheld-blog/content/post/` returns many — narrowed by relevance:

- `streamlining-blog-writing-with-claude-code/` — explicit sibling, workflow piece
- `2026-year-of-community/` — recent, AI-as-collaborator framing
- Older posts on craft and iteration — the "if you're proud of your last project you didn't learn anything" thread runs through several 2008–2014 posts and applies here

## What the post does NOT cite (and probably should)

These are real artifacts the post leans on implicitly. Worth surfacing because the draft says "the research wasn't waste, it was load-bearing" without naming the document that did the load-bearing.

- The DNS deep-dive document itself — never named in the draft. The draft says "five thousand words of reference material" but doesn't link or describe it. A reader who wants to verify the claim has nowhere to go.
- The v1 vs v2 comparison — the draft describes v1 in detail and v2 in summary, but a reader curious about the actual second-pass *technical* refinements (the public-DNS-fork beat, the numbered DNS chain) doesn't see them. The "cheapest piece of the first draft is the only piece of the final" maxim is true for the raccoon, but glosses over that v2 also got more correct, not just leaner.
- The Remotion code itself — the post implies but doesn't show that the final visual language exists because the React+SVG pipeline is what Aaron can actually animate. That's an honest framing the post could lean into harder.

## Open questions for the contrarian view

(See `contrarian-view.md` for the development of these.)

1. Is the "AI scales writing past your making" lesson the right framing — or is it a self-flattering version of "I made a scope error"?
2. Was Slonik actually unmakeable, or was the cost just higher than Aaron wanted to pay? (Off-the-shelf 2D character animation tools exist. Cartoon Animator, Adobe Character Animator, Rive.)
3. Would the v2 video have been *better* if the v1 character work had survived in some form — even just as a 5-second cold open?
4. Is the post's lesson generalizable, or specific to a solo producer with this particular skill stack? A two-person team with one animator would have shipped v1.

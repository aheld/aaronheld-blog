# Platforms

**ICM Layer**: L2 (patterns). Updated when external platforms change.

**Last reviewed**: 2026-04-26 (initial seed — values below should be verified before next campaign).
**Re-check cadence**: annually, or when a platform announces a relevant change.

## Why this file is dated

Platform limits, algorithm preferences, and norms drift. A 280-character limit becomes 500. An algorithm starts penalizing external links. Image dimensions shift. **Don't trust this file blindly** — when stage 4 (publish) starts, glance at the "Last reviewed" date. If it's more than a year old, spend 10 minutes confirming the values for the platforms you're about to post to.

The values below were captured at workspace setup time and are **unverified by recent research**. Treat them as starting points, not gospel.

## Blog (Hugo + aaronheld.com)

### URL pattern
`https://www.aaronheld.com/post/[slug]/`

### Front matter requirements (Hugo PaperMod)
- `title` (string)
- `date` (RFC3339, e.g., `2025-01-29T14:14:57-05:00`)
- `draft` (bool — `true` until publish)
- `description` (string, used for SEO meta and social cards — keep ~150–160 chars for ideal SEO display)
- `categories` (list)
- `tags` (list)
- `cover.image`, `cover.alt`, optional `cover.caption`
- `series` (list, optional — for multi-part)

### SEO conventions
- **Title**: aim for 50–60 characters for ideal Google display.
- **Description**: 150–160 characters.
- **Image alt text**: required for every image (constraint, not preference).
- **Internal linking**: link to prior related posts where relevant — see `recurring-references.md` for known threads.

### Cover image expectations
- Real art preferred (Unsplash credited photos, public-domain SF book covers).
- AI-generated allowed where appropriate but should be deliberate, not default.
- Reasonable resolution for retina displays (~1600px wide minimum).

## LinkedIn

### Length
- Posts: up to ~3000 characters total. Sweet spot for engagement is often 200 words (1,200 - 1,600 chars).
- "See more" cutoff: ~210 characters on desktop, ~140 on mobile. The first 1–2 lines are the entire hook for non-followers.

### URL handling
- Posts with external links can perform fine, but some authors note the algorithm prefers comments-with-link over body-with-link. Aaron's existing posts put the blog link in the body — that's fine, just be aware.
- LinkedIn auto-generates a preview card from the URL (uses the post's `description` and `cover.image`).

### Format conventions for Aaron's posts
- Lead with the hook from `social-hooks.md` (chosen in stage 4 sub-step 2, not auto-derived from title).
- Single-paragraph hook, then short paragraphs (1–3 sentences each).
- Use line breaks generously — LinkedIn collapses long blocks.
- Hashtags at the end, 3–5 max, sentence-case-or-lower (e.g., `#Leadership #Engineering #Management`).
- The blog URL goes in the post body (Aaron's current pattern).

### Bi-directional link pattern
After posting on LinkedIn, the blog post is updated with:
```markdown
[Comment on LinkedIn if this story resonated with you](https://www.linkedin.com/posts/aaronheld_...)
```
This is added in stage 4 sub-step 3.

## Bluesky

### Length
- Single post: 300 characters.
- Threads possible by chaining replies — but a focused single post often performs better than a long chain.

### URL handling
- Embeds the destination URL with a card preview (uses Open Graph metadata from the blog post).
- Counts URLs against character limit, but the displayed card doesn't take additional chars in the visible text.

### Format conventions for Aaron's posts
- Different angle from LinkedIn — Bluesky audience is technical, often skeptical of corporate tone.
- Lead with the most interesting hook (sometimes the contrarian view from research is the right opener here, where the LinkedIn post led with personal observation).
- Hashtags less culturally important on Bluesky than LinkedIn — 0–2 is fine.

## Threads

### Length
- Original limit was 500 chars; expanded over time. Verify current limit at publish time.
- Threading via reply-chain works similarly to Bluesky.

### Format conventions for Aaron's posts
- Audience overlap with Instagram + Twitter migrants. Tone slightly more conversational than LinkedIn.
- Cross-references to LinkedIn discussion can land here ("Discussion picking up on LinkedIn: [URL]") if the LinkedIn post is already getting engagement when Threads goes up.
- Hashtags: 1–3.

## Cross-platform tailoring rule

The hardest discipline is **not pasting the same text everywhere**. Each platform's audience differs. The `social-hooks.md` artifact from stage 3 should give 3–5 candidate openings — pick a *different* one for each platform if possible. The blog URL is the through-line; the framing isn't.

## When to update this file

- A platform changes a documented limit or feature.
- Aaron notices a pattern that consistently performs (or flops) on a platform — capture it in "Format conventions."
- Annually as a calendar reminder. Update the "Last reviewed" date at top.

When this file is updated, log the change at the bottom:

## Change log
- 2026-04-26: initial seed.

# Social Hooks — Making the Azure Private Link Video

**Slug**: `making-the-azure-private-link-video`
**Live URL**: <https://www.aaronheld.com/post/making-the-azure-private-link-video/>
**Sibling post**: <https://www.aaronheld.com/post/streamlining-blog-writing-with-claude-code/>

The five hooks below are different *entry angles* into the same post. Per `_config/platforms.md` line 92, the discipline is not pasting the same text everywhere — pick a different hook for each platform. Recommended pairings at the bottom.

---

## Hook A — The pivot (the post's thesis)

> AI made it cheap to write a great cartoon when what I actually needed was an explainer. The cartoon went to the Island of Misfit Toys. The pivot was the work.

**Best for**: LinkedIn lead. It's the post's central claim, lands the meta-essay framing, and the "Island of Misfit Toys" reference earns curiosity for the click.

## Hook B — Carried away (the most honest line)

> I got carried away thinking I could compete with seasoned content creators on my first go. Then I caught myself, and the pivot back to the actual job was where the real work happened.

**Best for**: Bluesky. Technical/skeptical audience reads peer-to-peer self-correction more readily than polished hooks. No theater, no setup, just the admission. Lands.

## Hook C — The cheapest piece (the strongest single maxim)

> The cheapest piece of the first draft is often the only piece of the final. The character I almost cut became the entire antagonist of the version I shipped.

**Best for**: Threads. Aphoristic, scrolls well, intriguing without context. Earns the click.

## Hook D — Tooling moves underneath you

> AI is moving fast enough that breaking work into small deliverables with the right context isn't a workflow you set once. It's a workflow you keep refactoring while you're using it. Here's a worked example, mid-refactor.

**Best for**: LinkedIn alternate, especially if the audience overlaps with readers of [Streamlining Blog Writing with Claude Code](https://www.aaronheld.com/post/streamlining-blog-writing-with-claude-code/) — this hook explicitly bridges the two posts.

## Hook E — AI wants to be used

> I think AI *wants* to be used. Without constraints, it will keep telling you how brilliant your plan is. The discipline isn't your animation skill or your tooling. It's your willingness to re-read the brief halfway through, and then re-read it again.

**Best for**: punchy alternate for any platform; especially good as a comment-thread reply once a post is live and people are agreeing too easily.

---

## Recommended pairings

| Platform | Hook | Why |
| --- | --- | --- |
| **LinkedIn** | A (pivot) | Most LinkedIn-native: meta-narrative, named characters, clear stakes. The "Island of Misfit Toys" frame is the kind of hook that makes people screenshot the first paragraph. |
| **Bluesky** | B (carried away) | Bluesky audience is technical and rewards self-correction over polish. Pair with the YouTube link, not the blog link, to put the artifact first. |
| **Threads** | C (cheapest piece) | Aphoristic, doesn't need context, scrolls well. |
| **Reply / pinned** | E (AI wants to be used) | Good comment fodder once the LinkedIn post is live and getting engagement. |

---

## LinkedIn full post (draft)

Hook A, expanded to LinkedIn length per `_config/platforms.md` (200 words target, ~1,200–1,600 chars, short paragraphs, hashtags at end, blog URL in body):

> AI made it cheap to write a great cartoon when what I actually needed was an explainer. The cartoon went to the Island of Misfit Toys. The pivot was the work.
>
> I had a six-act script with a friendly PostgreSQL elephant named Slonik, three Ricky-the-Raccoon costume changes, a stagehand character, and an actual circus tent representing "all of Azure." It was funny. It was correct. And it had quietly stopped being an explainer about Azure Private Link, which was the whole point.
>
> The version I shipped is architecture diagrams, a numbered DNS resolution chain, and a raccoon silhouette who never says a word. It lands the same lesson at maybe a tenth of the production cost. But the trade isn't really the lesson.
>
> The lesson is that I had to catch the drift before the trade was even available to me. AI doesn't change scope discipline. It just makes you exercise it faster, and more often, because the tooling keeps moving underneath you.
>
> <https://www.aaronheld.com/post/making-the-azure-private-link-video/>
>
> #AI #ContentProduction #Workflow #Engineering

**Character count check**: ~1,400 chars (within sweet spot per platforms.md).
**"See more" cutoff** (~210 chars): the first paragraph + first sentence of the second paragraph land before the cutoff. Good — the cartoon-vs-explainer tension is visible without expanding.

After this post is live, update the blog post's footer per `_config/platforms.md` line 58–62:

```markdown
[Comment on LinkedIn if this story resonated with you](https://www.linkedin.com/posts/aaronheld_...)
```

---

## Bluesky single post (draft)

Hook B, fitted to 300 chars including the URL. The Bluesky card embed will pull the cover image and description automatically, so the visible text just needs to be the hook + URL:

> I got carried away thinking I could compete with seasoned content creators on my first go. Then I caught myself. The pivot back to the actual job was the real work.
>
> <https://www.aaronheld.com/post/making-the-azure-private-link-video/>

**Character count**: ~245 (URL counts against limit but the card is the visible payload). Within 300.

No hashtags — Bluesky norms per `platforms.md`.

---

## Threads single post (draft)

Hook C. Threads' current limit needs verification at post time per `_config/platforms.md` line 82, but assuming ~500 chars is still in play:

> The cheapest piece of the first draft is often the only piece of the final.
>
> Wrote a six-act animated short about Azure Private Link. The character I almost cut, a flat raccoon silhouette, ended up the only character in the version I actually shipped. The elephant, the costumes, the circus tent? Island of Misfit Toys.
>
> <https://www.aaronheld.com/post/making-the-azure-private-link-video/>
>
> #ContentProduction #AI

**Character count**: ~430. Comfortably within most plausible limits.

If Threads is following the LinkedIn/Bluesky timing, post Threads *after* LinkedIn has some engagement, and add the LinkedIn discussion link per platforms.md line 87.

---

## Cross-platform timing (suggestion)

Per the workflow's normal cadence:

1. **Now**: blog is live.
2. **+0**: post LinkedIn (Hook A).
3. **+~2 hours**: once LinkedIn has a few comments, post Bluesky (Hook B). Pair with YouTube URL (the video itself) rather than the blog, since Bluesky users may want the artifact first.
4. **+~6 hours / next day**: post Threads (Hook C), with cross-reference to the LinkedIn discussion if it's active.
5. **After LinkedIn discussion settles**: update the blog post footer with the "Comment on LinkedIn" back-link.

This staggering matches `_config/platforms.md` line 87 ("cross-references to LinkedIn discussion can land here if the LinkedIn post is already getting engagement").

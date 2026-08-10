# Completed: High-Protein "Marry Me" Beans, Peas & Mushrooms

**Slug**: `marry-me-beans-peas-mushrooms`
**Published**: 2026-07-21
**Live URL**: <https://www.aaronheld.com/post/marry-me-beans-peas-mushrooms/>
**LinkedIn**: none (skipped at Aaron's request)
**Commits**: `0469ca0` (publish)
**Pipeline duration**: one session, same day

## What the post argues

Not an argument post, a recipe. Aaron grew up on cholent (an Eastern European bean stew cooked to a uniform mush) and his wife doesn't care for that texture or for curry, which made "eat more plant-based" hard to act on at home. Nora Cooks' "Marry Me Chickpeas" cleared both bars structurally (beans hold their shape, Italian aromatics instead of curry spice), so Aaron adapted it: seared mushrooms in place of sun-dried tomatoes, a blended cashew-white-bean cream for protein and thickening, Zoup concentrate instead of broth, one can chickpeas + one can cannellini instead of two cans chickpeas, and peas because his wife likes them. Full credit and links to Nora Taylor's original throughout.

## How it moved through the pipeline

**Input**: Aaron arrived with a fully-formed idea and a PDF export of the Gemini chat where he'd actually developed the recipe (substitution options, protein-boosting ideas, macros). That chat *was* the research.

**Research + Outline (compressed into one pass)**: With the Gemini transcript already documenting every substitution decision, there was no cold research to do. `sources.md` captured the original recipe (Nora Cooks) and the real decision points from the transcript. The contrarian view found: derivative recipe posts can siphon search traffic and ad revenue from the original creator, resolved by making the credit prominent and load-bearing (not a footnote) and framing the post honestly as a one-off riff, not a tested developer recipe.

**Outline checkpoint pivot**: Aaron rewrote the opening hook himself, from a mechanical "no sun-dried tomatoes in the pantry" detail to the real stakes: growing up on cholent, his wife's dislike of mush and curry, the actual reason this recipe mattered. Much stronger hook; the mechanical pantry detail survived as a mid-post beat instead of carrying the opening.

**Draft**: Written in one pass (a departure from the section-by-section default, justified by the short Pattern A length and the fact the recipe content already existed verbatim in sources.md). Aaron then asked to strip the "AI as amplification" framing that had been woven through the substitution story, keeping only a single AI mention at the very end, tied specifically to running the nutrition estimates through Gemini. Aaron also made his own substantial edits: added a personal, deprecating opening line ("I don't normally write about recipes..."), the cholent citation link, a Zoup Concentrate swap for the broth (with real running commentary, "Zoup is my new secret ingredient"), a joke in the method ("until your spouse can smell it upstairs"), and a personal Nuts.com referral link.

**Publish**: Copied to `content/post/`, tested locally with `hugo server -D` before going live. That local pass caught two real bugs Aaron's own edits had introduced (the method still referenced "chili flakes" and "vegetable broth" after both were removed from the ingredient list) plus two capitalization typos ("indian" / "italian"). LinkedIn/Bluesky/Threads amplification skipped entirely at Aaron's explicit request.

## Voice and process notes worth keeping

- First recipe/personal-category post through the pipeline. Confirms the workspace can flex for genuine departures from the blog's usual professional/leadership content without forcing a connection to existing themes.
- Removing the AI-collaboration framing (beyond the one factual macros mention) was the right call. Not every post needs to gesture at "AI as amplification" just because it's a recurring theme elsewhere on the blog.
- Cover image sourcing lesson: verify a public-domain image's actual resolution before proposing it, not after Aaron has committed to it emotionally. The Little Mikey (1972 Life cereal commercial) image checked out as genuinely PD-US-no_notice, but at 246x194px it's well under the blog's normal cover floor. Aaron chose to accept the blur for the nostalgia payoff; documented as a known trade-off rather than silently shipped.
- Local `hugo server -D` testing before push caught real recipe-correctness bugs (stale ingredient references after edits) that would have shipped otherwise. Worth doing even for "simple" posts.

## Amplification

None. Aaron explicitly opted out of LinkedIn, Bluesky, and Threads for this post.

## Feature requests surfaced

- `feature-requests/recipe-microformats.md` — schema.org `Recipe` structured data support, so future recipe posts get rich snippets and machine-readable ingredients/instructions instead of a plain Markdown card.

## Working artifacts

Research, outline, draft, and publish-amplify folders move to `_archive/marry-me-beans-peas-mushrooms/` at close-out.

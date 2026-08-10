## Post-publish self-review

**What worked**:
- Compressing research + outline into one pass was the right call. Aaron's own Gemini chat transcript (uploaded as a PDF) *was* the research, there was nothing left to go find. Writing it up as `sources.md` still mattered though, it's what let the outline and draft move fast without re-deriving the substitution logic from scratch.
- The cholent/curry opening hook, which Aaron wrote himself mid-checkpoint, was much stronger than the pantry-inventory hook it replaced. The original draft hook ("no sun-dried tomatoes in the pantry...") was a fine mechanical detail but not a real stake. The rewrite gave the post an actual reason to exist.
- Verifying the Little Mikey image's actual license (PD-US-no_notice, not just "it's on a wiki somewhere") before using it caught a real risk early, a lot of viral commercial screenshots on Commons are non-free/fair-use-only and would've been wrong to reuse here.
- The local `hugo server -D` test caught two real bugs before they went live: the method still called for "chili flakes" and "vegetable broth" after Aaron's edits removed both from the ingredient list. Would have been a genuinely broken recipe if published as-is.

**What was harder than expected**:
- The cover image. The only Commons copy of the Little Mikey screenshot is 246x194px, far under the blog's usual cover floor. No amount of process fixes that, it's a real trade-off between the nostalgia payoff and image quality. Flagged it, Aaron chose to accept the blur.
- Mid-draft, Aaron asked to remove the AI-collaboration framing from the narrative (keeping only the macros mention at the end). The initial draft had leaned on "AI as amplification" as a signature-move connective tissue to Aaron's usual themes, that connection didn't actually serve this post, and cutting it made the piece better, not worse. Worth remembering: not every post needs to gesture at the blog's usual themes.

**What I'd change next time**:
- Check image resolution *before* proposing an image as a candidate, not after Aaron has already picked it. Would've surfaced the 246x194px problem a step earlier.
- For personal/recipe-category posts, consider skipping the "signature moves" exercise almost entirely at outline time rather than proposing an AI-thesis connection that then has to be walked back. Not every post needs to connect to the blog's professional throughline, and a first-instinct pass toward "how does this connect to Aaron's usual themes" isn't always the right move for a genuine departure post.

**Stage timing**:
- Research + Outline (compressed): one pass
- Draft: one pass, plus a follow-up edit pass removing AI framing
- Aaron's own direct edits (cholent hook, Zoup swap, image choice, recipe tweaks): one pass
- Publish: local test → bug fixes → live, one session
- Total: same-day, single session end to end

**Feature requests surfaced**:
- `feature-requests/recipe-microformats.md` — schema.org `Recipe` structured data / recipe card shortcode, surfaced because this post shipped with a clean but unstructured recipe card.

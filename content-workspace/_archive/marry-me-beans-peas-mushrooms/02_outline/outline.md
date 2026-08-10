# Outline: High-Protein "Marry Me" Beans, Peas & Mushrooms

**Content type**: Pattern A (Quick Tip), with a recipe block attached
**Word target**: 300–500 words of prose (narrative frame) + a standard recipe card (ingredients/instructions, not counted toward prose target — utility content, not argument)
**Estimated drafting time**: 30–40 minutes

## Opening Hook (final, not draft)

> I grew up on cholent and other Eastern European gruel like stews. Mom simmers a pot of beans for over 24 hours until they're one soft, uniform mass. I loved it. My wife does not, and she's never warmed to curry either, which meant my goal of "eat more plant-based meals" was hard to enjoy. 

I think I finally found the one that gets around both, plant-based, real protein, cheap, and quick enough for a weeknight. It had enough texture for her and enough creamy consistency for my taste. 

## Section Beats

*(Pattern A default is 0-1 H2s / continuous prose — using light H2s here only because a recipe card is a genuinely distinct block from the narrative, not because the story needs sectioning.)*

### (No H2) — The story
- Purpose: open with the cholent/curry texture-and-flavor problem (the real reason this recipe mattered, not just "tried a new recipe"), then pivot to how Nora Cooks' Marry Me Chickpeas cleared that bar structurally (creamy, not mushy; garlic-oregano-basil, not curry spice) — credit the source recipe immediately and prominently — then walk through the real substitutions and why (no sun-dried tomatoes on hand → mushrooms; wanted more protein → cashew + blended white bean cream; peas because his wife likes them; one can chickpeas + one can cannellini instead of two cans chickpeas).
- Draws on: sources.md sections 1-2 (Nora Cooks original, Aaron's Gemini transcript decision points).
- Notes: keep the "peas because my wife likes them" line verbatim-ish — it's the most human beat, don't over-polish it into something generic. Mention the macro payoff (17g protein/serving vs ~10g in the original) as the "why bother" payoff, once, not belabored. The cholent/curry contrast is the actual stakes of the post — don't let it get crowded out by the substitution mechanics.
- Contrarian acknowledgment lands here, folded into the credit paragraph — not a separate section (see below).

### H2: The Recipe
- Purpose: the actual usable recipe card — ingredients (cream base + skillet) and numbered method, sized to what's in sources.md.
- Draws on: sources.md "Final recipe" section, verbatim.
- Notes: present as a real recipe someone could cook from, not prose-buried. This is the payoff of the post.

## Closing (final, not draft)

> Cholent took eighteen hours and got me a stew my wife wouldn't touch. This took fifteen minutes, tastes nothing like curry, and doesn't collapse into mush. Go make Nora's original first — it's the reason this exists at all. Then tell me what you'd swap next.

## Contrarian View Placement

Folded into the opening/credit paragraph (not its own section) — one line acknowledging this is a personal riff cooked once with AI assistance, not a tested recipe developer's release, paired with a prominent, generous link to Nora's original up top. Matches contrarian-view.md's guidance: resolve through genuine credit + honest framing, don't labor it into an essay.

## Signature Moves Used

- **Concrete-scene opener** (#3): the cholent-and-curry food history that sets up why this recipe actually mattered, not just "tried something new."
- **The personal-then-systemic move** (#6), in miniature: personal food-history scene (cholent, curry, wife's palate) → the substitution story with a light, one-sentence gesture at "AI as amplification, not replacement" (Aaron already writes about this re: engineering) → back to the personal (cholent callback, the closing question). Keep the AI-thesis connection to *one sentence, max* — this post should not become an AI-thesis piece. It's a recipe post first.
- **The contrarian acknowledgment** (#7): folded in as described above.

## Revision after draft feedback

Aaron asked to drop the "AI as amplification" gesture entirely from the narrative, this isn't a post about AI. The substitution story now reads as Aaron's own cooking decisions with no AI narration. The single remaining AI mention is at the very end, tied specifically to running the nutrition estimates through Gemini. The contrarian acknowledgment still holds (this is a one-off riff, not tested over multiple batches like Nora's original), it's just no longer framed as an AI collaboration.

## Notes for drafting stage

- **Front matter**: title "High-Protein 'Marry Me' Beans, Peas & Mushrooms" (or similar — keep distinct from Nora's title, don't compete for her search term). `categories: ["Personal"]`, tags something like `["recipe", "cooking", "vegan", "high-protein", "ai"]`. Needs a cover image — check `unsplash-retro-landscape` skill's fit or a photo Aaron actually took of the dish (real food photo is stronger than stock here if Aaron has one).
- **Attribution**: link to https://www.noracooks.com/marry-me-chickpeas/ at first mention, and again near the recipe card itself. Consider a blockquote-style callout box for the credit rather than a buried inline link — make it unmissable.
- **Feature gap**: flag `schema.org`/Hugo recipe microformats as a PRD in `feature-requests/recipe-microformats.md` during drafting — don't build it inline. Ship this post with a clean, readable recipe card using existing Hugo/Markdown conventions; structured data is a follow-up.
- **Scope check**: this fits in one sitting easily — the recipe content already exists verbatim in sources.md, drafting is mostly narrative frame + formatting.

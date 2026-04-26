# Constraints

**ICM Layer**: L3 (constraints). Hard rules. These don't bend.

These are starter rules — many from the Vault Toolkit, plus rules surfaced from Aaron's existing style guide and the workspace setup conversation. **Aaron should review this file**, remove rules he disagrees with, and add his own. Constraints are personal — what's a constraint for one writer is invisible to another.

## Punctuation and formatting

### No em dashes (—)
Use a comma, a colon, parentheses, or two sentences instead. Em dashes are a recognized AI tell and have crept into too much machine-generated prose. The voice is direct enough without them.
- ❌ "It's not weakness — it's human nature."
- ✅ "It's not weakness, it's human nature." or "It's not weakness. It's human nature."

### No double-hyphen substitutes
Don't replace `—` with `--`. The fix is rephrasing, not punctuation gymnastics.

### No "smart quotes" auto-conversion
Stick with straight quotes (`"`, `'`) — Hugo handles them fine and copy-paste is reliable.

## Language patterns to avoid

### No AI hedging language
- ❌ "It's worth noting that..."
- ❌ "In many ways..."
- ❌ "Not only... but also..."
- ❌ "It's important to remember..."
- ❌ "That said,..."

These are filler that sounds thoughtful but adds nothing. Cut them and the sentence is sharper.

### No marketing speak
- ❌ "leverage," "synergy," "robust," "seamless," "unlock," "delve into," "deep dive" (as a verb).
- ❌ Superlatives without earning them ("game-changing," "revolutionary," "unprecedented" — *unless the post is specifically arguing precedent exists*).
- ❌ "In today's fast-paced world..." or any variant.

### No "delve"
Specifically: the word "delve" is a known AI tell and is banned regardless of context. Use "look at," "examine," "get into," "explore," or just drop the framing verb entirely.

### No closing throat-clearing
- ❌ "In conclusion,..."
- ❌ "To summarize,..."
- ❌ "At the end of the day,..."

The post's closing should land — see `voice-and-tone.md`.

### No false dichotomies
"You either X or Y" framings are usually wrong. The audience (per `audience.md`) is smart enough to spot them. Acknowledge the third option, even briefly.

### No "10 simple steps" formulas
The audience constraint forbids talking-down. Numbered structure is fine; numbered formula is not.

### No fake stakes / doom framing
"This is killing your career," "Why X is destroying Y" — the existing voice guide explicitly avoids doom-and-gloom. Critique without catastrophizing.

## Image rules

### Every image has alt text
Non-negotiable. Accessibility is a constraint, not a preference.
- Alt text describes the image's content and purpose, not just literal contents.
- Decorative images: `alt=""` is acceptable, but only if the image truly carries no information.

### Image source priority
1. **Credited Unsplash photos** (free, properly licensed, attributed).
2. **Public-domain SF book covers** (especially for SciFi-referencing posts — fits the blog's aesthetic).
3. **Real photos Aaron took** (best when relevant — see "The Aging Programmer" cover with Aaron's dad).
4. **AI-generated images** — allowed where appropriate, but a deliberate choice, not the default.

### Image attribution
Always credit. Caption with photographer name + Unsplash URL when using Unsplash. Public-domain SF covers note the work and original publication.

## Sourcing rules

### Every research source has a real citation
- Author or publication name.
- URL.
- Date (when available).
- No paraphrasing without attribution.

### Quotes are credited
Always with attribution line. Anonymous quotes ("a wise person once said...") don't appear in this blog.

## Voice integrity

### The audience test (see `audience.md`)
Every paragraph must pass: would a smart 25-year-old who's never managed feel respected, AND would a 20-year veteran feel not insulted? Both must be yes.

### The contrarian view shows up
Per stage 1 (research), the post must engage the contrarian view found in research. Pretending opposition doesn't exist makes the post weaker.

### The opening earns the post
Per stage 2 (outline), the opening hook is written in full at outline time, not "TBD." If the hook isn't compelling, the post isn't ready.

### The closing lands the hook
Per `voice-and-tone.md`, closes circle back to the opening. A close that doesn't is a sign the middle drifted.

## Workflow rules

### Don't skip stage checkpoints
Each stage produces an artifact, Aaron reviews, then triggers the next. No auto-flow. The pause is the point.

### Multi-part is the exception, not the default
See `format-patterns.md` Pattern D criteria. Default is single-post.

### Capture feature gaps as PRDs, don't context-switch
If during drafting a feature would help, write the PRD in `feature-requests/`, keep drafting. Don't drop into feature work mid-draft.

### Source-as-content
This repo is public. Files in `content-workspace/` should be legible to a stranger. Write `_config/` files for *future Aaron* who's forgotten the conversation that produced them.

## Aaron's space — add your own here

skip Twitter/X entirely.
don't go deep into divisive politics, but do not hide my progressive/liberal bias
Never punch down and make harmful jokes or leverage preducicial sterotypes (except about nerdy tech people or tech bros, they are a fair targets)

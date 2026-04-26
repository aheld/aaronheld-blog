# Signature Moves

**ICM Layer**: L1 (domain). Reusable techniques Aaron reaches for across pieces. Distinct from themes (which are *what* the blog is about) — these are *how* any topic gets framed.

## What these are

Signature moves are tricks of framing, not topics. They're the writing techniques that, when present, make a piece feel like Aaron wrote it. The outline stage should consciously pick which moves a piece uses; the draft stage should execute them well.

## The Moves

### 1. "Nothing unprecedented" — the historical parallel

Take a current pattern people are panicking about, find the earlier wave that mirrored it, draw the parallel honestly. The earlier wave is usually 10–25 years back — old enough that outcomes are visible, recent enough that practitioners remember it.

**Examples from the blog**:
- AI changes programming ↔ public cloud + DevOps changes
- Modern documentation crisis ↔ accessibility/inclusion neglect we already knew about
- Modern caching debates ↔ cache wars of the 2000s

**How to use**:
- Find the parallel during research (stage 1), not draft.
- Don't force it. If the parallel is weak or strained, drop it — a fake parallel is worse than no parallel.
- The parallel earns its place by *clarifying*, not just decorating. The reader should leave with a sharper view of the present, not just a history lesson.

**Failure mode**: nostalgic history-for-history's-sake. The move is in service of the present argument.

### 2. The Rod Serling / Twilight Zone framing

Open with a stylized, italicized narrative voice — usually Rod Serling — that sets a scene, then cut to the actual point. See "The Weapon by Fredric Brown" for the canonical execution.

**Visual cue**: unicode italic formatting (𝘢𝘭𝘭 𝘵𝘩𝘦 𝘵𝘦𝘹𝘵 𝘪𝘯 𝘵𝘩𝘦 𝘩𝘰𝘰𝘬 𝘪𝘵𝘢𝘭𝘪𝘤𝘪𝘻𝘦𝘥) with a header line like:

> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗿𝗲𝗮𝗱 𝗶𝗻 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗼𝗳 𝗥𝗼𝗱 𝗦𝗲𝗿𝗹𝗶𝗻𝗴

**How to use**:
- Reserve for posts where the topic genuinely benefits from a fable/parable framing (consequences, hubris, ironic outcomes).
- The Serling voice runs for a few paragraphs, then ends with "You are now entering... the Twilight Zone." — and the post drops into Aaron's regular voice for the actual argument.

**Failure mode**: using it as gimmick rather than because the topic earns it. If the frame doesn't pay off in the post's argument, cut it.

### 3. The concrete-scene opener

Even when not using the Serling frame, the standard Aaron opener is a specific scene: a moment, a quote, a small incident. *Then* the broader point.

**Examples**:
- "Dad called me today. His team got bested by Denver at the Florida classic."
- "I was reviewing an older repository during a production incident the other day..."
- "I got into management because I saw myself as a player-coach."

**How to use**:
- Present tense or recent past. Not "Once upon a time."
- Specific over generic. "An engineer told me" is weaker than "Sarah told me."
- The scene should compress into the broader point within 2–3 paragraphs. Don't linger.

### 4. The pop-culture lens

Use a movie, TV show, or game as the vehicle for a management/engineering point. Existing posts: Batman, Iron Man, Chef Ramsay, Pelham 123, Michael Clayton.

**How to use**:
- The pop-culture reference is a vehicle, not the destination. The post is about leadership; Batman just makes the point legible.
- Don't assume universal familiarity. A line of context for the reference is fine; a paragraph of plot summary is not.
- Works especially well for "anti-hero as anti-pattern" framings.

### 5. The credited quote

Pull a quote from a serious source (Heinlein, Deming, Kate Gregory, etc.) — not a generic motivational image. Always with attribution.

**How to use**:
- The quote should land an argument the post is already making, not substitute for one.
- See `recurring-references.md` for the known shelf — start there before searching cold.
- Format: blockquote, then attribution line on its own.

### 6. The personal-then-systemic move

Start with a personal observation (a colleague, a manager, a project you were on). Pull back to the systemic pattern. Return to the personal at the close.

This is the structural backbone of most of Aaron's longer posts — even when no specific signature move is named, the personal-then-systemic-then-personal arc is operating.

### 7. The contrarian acknowledgment

Briefly engage the strongest argument against your premise, then explain why you still hold it. Not as throat-clearing — as a way of showing the reader you've already thought about what they're about to object to.

This is **why** the research stage requires a `contrarian-view.md` artifact. The move only works if real opposition was found.

## Picking moves for a piece

In stage 2 (outline), the `outline.md` includes a "Signature Moves Used" section. The choices should be deliberate:

- A piece can use multiple moves (e.g., concrete-scene opener + historical parallel + closing personal callback).
- A piece can use just one — overstuffing dilutes them.
- The moves should serve the argument, not perform Aaron-ness for its own sake. If a move doesn't earn its place, cut it.

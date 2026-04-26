# Handoff: Aaron Held — Blog Redesign

## Overview

This package contains a redesign of `aaronheld.com` — a personal essay/blog site built on Hugo + the PaperMod theme. The redesign covers two surfaces:

1. **Home** (`Home.html`) — a hero/intro block, featured essays (two-up cards), a filterable post list, dense archive, and a "Now" + tag-cloud sidecar.
2. **Single Post** (`Post.html`) — long-form reading template with breadcrumb, hero cover, body typography, in-page TOC, share/tag rail, author card, prev/next, and "More from Aaron".

The aesthetic stays close to PaperMod's reading-first DNA — narrow column, calm neutrals, a single restrained accent red sampled from Aaron's avatar — while modernizing the typography, meta surfaces, and density controls.

## About the Design Files

The HTML/CSS/JS in `design/` are **design references**, not production source. They use vanilla HTML, hand-written CSS, and a tiny inline `<script>` for theme/TOC/progress behavior. The expected outcome is to **recreate these designs in the existing aaronheld.com Hugo + PaperMod codebase**, using PaperMod partials, Hugo templates, and the site's existing build pipeline — not to drop these files in directly.

If implementing fresh in a different stack (e.g. a Next.js or Astro rebuild), choose the framework that fits the project and translate the patterns idiomatically. The CSS variable system is portable and should carry over wherever it lands.

## Fidelity

**High-fidelity (hifi).** Final colors, typography, spacing, hover/focus states, and dark-mode tokens are pinned. The cover image on the post is a placeholder (Unsplash URL) — the real article will swap in its own image.

## Screens / Views

### 1. Home (`Home.html`)

**Purpose:** entry point — establish who Aaron is, surface featured essays, let the reader scan the back catalog by category or full archive.

**Layout (top to bottom):**
- Sticky header (60px tall, full-width, `--bg-1` w/ 92% alpha + backdrop-blur, 1px bottom border in `--border-1`)
- Main column constrained to `--main-width: 720px`, centered, `padding: 40px 24px 96px`
  - **Hero**: 2-col grid `96px 1fr`, 24px gap. Avatar left (96×96 circle), text right: eyebrow ("CURRENTLY · PHILADELPHIA" w/ accent dot + 3px halo), H1 28px/1.2/700/-0.015em, sub-paragraph 17px/1.55, meta row of icon+label pairs at 13px.
  - **Featured posts**: 2-col grid, 16px gap. Each card 20px padding, `--bg-2` fill, 1px `--border-1`, `--radius-lg` (12px), 190px min-height. On hover: border darkens to `--fg-3`, a 3px `--accent` rail scales up from the top-left. Kicker (uppercase, accent), title (21px/1.25/700), summary (15px/1.55), meta row.
  - **Archive section**: chips row (rounded 999px, active = `--fg-1` bg / `--bg-1` fg), then `.post-list` rows. Row grid `92px 1fr auto`: tabular date / title+summary+meta / arrow that fades in and slides 3px right on hover.
  - **Dense mode** (`.post-list.is-dense`): summary hidden, title 16px/500, 10px vertical padding.
  - **Meta strip**: 2-col grid card with "Now" definition list (left col `74px` label / right col value) and "Tags" cloud (rounded pills tinted `--ah-tag-soft` / `--ah-tag`).
- Footer: 1024px max-width, flex justify-between, copyright + socials.

**Responsive (≤720px):** hero collapses to 1-col, nav hides, featured collapses to 1-col, post rows collapse to single column, meta-strip collapses to 1-col.

### 2. Single Post (`Post.html`)

**Purpose:** long-form reading. Optimized for ~720px column with optional desktop TOC rail.

**Layout (top to bottom):**
- 2px reading-progress bar fixed to top, `--accent`, width updated on scroll.
- Same sticky site header as Home.
- **Breadcrumb** (`.post-crumbs`): 720px column, 13px `--fg-3` text, `/` separators, hover → `--accent`.
- **Post header**:
  - Kicker — 12px uppercase 0.1em, accent color, 5px round dot prefix.
  - H1 — 40px / 1.12 / 700 / -0.02em, `text-wrap: balance`.
  - Lede — 20px / 1.5, max 60ch, `text-wrap: pretty`.
  - Meta bar — flex row, 14px gap, top + bottom hairline borders. Author chip (32px avatar + name/subtitle), spacer (`flex:1`), then pills: date / read time / comments. Pills are 4×10px padding, `--bg-2` fill, 999px radius, 12px text with 12px inline icon.
- **Cover image** — max-width 1024px, `--radius-lg` rounded, 16:9 aspect, italic centered figcaption at 13px `--fg-3`.
- **Body** (`.post-body`):
  - Container 720px, 18px / 1.7 base.
  - Paragraphs separated via `> * + *` margin-top of 1.1em.
  - H2 — 26px / 1.2 / 700, 2.2em top margin, `scroll-margin-top: 80px`. On hover, a `#` anchor link fades in 28px to the left.
  - H3 — 21px / 1.3 / 600.
  - Strong — `--fg-1` 600. Em — italic.
  - Links — color `--fg-1`, `box-shadow: inset 0 -1px 0 var(--fg-3)` underline; hover swaps both to `--accent`.
  - Lists — `padding-left: 1.4em`, marker color `--fg-3`.
  - Blockquote — serif italic, 22px / 1.45, 3px `--accent` left border, `--fg-1`.
  - Inline `<code>` — `--font-mono`, 0.92em, `--bg-3` chip, 4px radius.
  - `<pre>` — `--ah-code-block-bg` (always-dark), `#e6e6e6` text, 18×20 padding, 14px / 1.5.
  - Callout — `--bg-2` card w/ 1px `--border-1`, `--radius`. Title row with accent icon, 15px/700; body 16px.
  - `hr.section-rule` — single 1px `--border-1` line, 3em vertical margin.
- **Footer rail** (`.post-footer-rail`) — 2-col grid (tags 1fr / share auto), 24px padding, `--bg-2` card. Tag pills use `--ah-tag` palette. Share icons are 36×36 outlined squares, 8px radius; hover swaps border + icon to `--accent`.
- **Author card** — 64px avatar / 1fr text grid, `--radius-lg`, 1px `--border-1`. Name 16px, bio 14px / 1.55, links row at 13px with hairline underline.
- **Prev / Next** — 2-col grid of cards, 18×20 padding, hover swaps border to `--fg-3` and bg to `--bg-2`. Label uppercase 12px / 0.1em, title 15px/600.
- **More posts** — section header (uppercase 13px / 0.14em / `--fg-3`), then a compact `.post-list` (same row component as home).
- **TOC rail** (desktop ≥1180px only) — `position: fixed`, top 100px, left = `50% + main/2 + 32px`, width 200px. Title uppercase 11px. List has 1px left border in `--border-1`; active link gets a 2px `--accent` left border that overlaps the rail (`margin-left: -1px`).

**Responsive (≤720px):** H1 to 30px, lede to 17px, cover full-bleed (no padding/radius), body to 17px, blockquote to 19px, footer rail and prev/next collapse to 1-col, author card to 1-col with 56px avatar.

## Interactions & Behavior

- **Theme toggle** — `#theme-btn` in header swaps `data-theme` attr on `<html>` between `light` and `dark`. Persisted in `localStorage` under key `ah-theme`. Initial value resolves: stored → `prefers-color-scheme` → `light`. Inline boot script runs synchronously in `<head>` to avoid FOUC.
- **Reading progress** — listens to `scroll`/`resize`, computes `-rect.top / (rect.height - innerHeight)` against the post body and writes to `#progress` width. Transition 80ms linear.
- **Active TOC** — same scroll listener walks heading offsets, applies `.is-active` to the matching link. Threshold = `scrollY + 120`.
- **More posts list** — built from `window.AH_POSTS` at runtime, filtered to exclude the current slug, first 4. Each row is a `.post-row` matching the home component.
- **Post row arrow** — opacity 0 → 1 + `translateX(3px)` on parent hover; title shifts to `--accent`.
- **Featured card rail** — `::before` 3px `--accent` bar, `transform: scaleY(0)` resting → `scaleY(1)` on hover.
- **Wave** — hero h1 has a `<span class="wave">` animated once on load via `@keyframes wave` (0.5s delay, 2.4s ease-in-out, single iteration). Suppressed by `prefers-reduced-motion`.
- **Reduced motion** — global rule disables all animations/transitions when `prefers-reduced-motion: reduce`.

## State Management

Vanilla — no framework. The two stateful pieces are:
- **Theme** — read once at boot, written on toggle, persisted in `localStorage`.
- **Progress + TOC active section** — derived from scroll position; no stored state.

Hugo/PaperMod equivalents already exist for theme toggle and TOC; reuse those rather than porting these scripts verbatim.

## Design Tokens

All tokens live in `design/assets/colors_and_type.css` as CSS custom properties. Lift them as-is.

### Colors — light

| Token | Value | Usage |
|---|---|---|
| `--ah-paper` | `rgb(255,255,255)` | page bg |
| `--ah-paper-2` | `rgb(250,250,250)` | card / subtle surface |
| `--ah-ink` | `rgb(30,30,30)` | primary text |
| `--ah-ink-2` | `rgb(108,108,108)` | secondary / meta |
| `--ah-ink-3` | `rgb(214,214,214)` | tertiary / disabled |
| `--ah-border` | `rgb(238,238,238)` | hairlines |
| `--ah-content` | `rgb(31,31,31)` | body copy |
| `--ah-code-bg` | `rgb(245,245,245)` | inline code |
| `--ah-code-block-bg` | `rgb(28,29,33)` | pre block (always dark) |

### Colors — dark

| Token | Value |
|---|---|
| `--ah-paper-dark` | `rgb(29,30,32)` |
| `--ah-paper-2-dark` | `rgb(46,46,51)` |
| `--ah-ink-dark` | `rgb(218,218,219)` |
| `--ah-ink-2-dark` | `rgb(155,156,157)` |
| `--ah-ink-3-dark` | `rgb(65,66,68)` |
| `--ah-border-dark` | `rgb(51,51,51)` |
| `--ah-content-dark` | `rgb(196,196,197)` |
| `--ah-code-bg-dark` | `rgb(55,56,62)` |
| `--ah-code-block-bg-dark` | `rgb(46,46,51)` |

### Accent + tag

| Token | Value | Usage |
|---|---|---|
| `--ah-accent` | `#d64545` | logo mark, link hover, blockquote bar, kickers, progress bar |
| `--ah-accent-ink` | `#b13838` | pressed |
| `--ah-accent-soft` | `#fbeaea` | selection bg, dot halo |
| `--ah-tag` | `#2f6fb3` | tag text |
| `--ah-tag-soft` | `#e7eff8` | tag bg |

### Semantic aliases

`--fg-1/2/3/4`, `--bg-1/2/3`, `--border-1`, `--accent`, `--accent-ink`, `--accent-soft`. These flip automatically under `:root[data-theme="dark"]`.

### Typography

- `--font-sans`: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif` (PaperMod default system stack)
- `--font-serif`: `'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, 'Times New Roman', serif` — used for blockquotes only
- `--font-mono`: `'Monaco', 'Menlo', 'Ubuntu Mono', 'SF Mono', Consolas, monospace`

Scale: `--fs-xs 14`, `--fs-sm 16`, `--fs-base 18`, `--fs-md 20`, `--fs-lg 24`, `--fs-xl 32`, `--fs-2xl 40`, `--fs-3xl 48`.
Line heights: `--lh-tight 1.2`, `--lh-snug 1.35`, `--lh-base 1.6`.
Weights: 400 / 500 / 600 / 700.

### Layout / radius / shadow

- `--nav-width: 1024px`, `--main-width: 720px`, `--header-height: 60px`, `--gap: 24px`.
- `--radius-sm 4`, `--radius 8`, `--radius-lg 12`, `--radius-pill 999`.
- `--shadow-1: 0 1px 2px rgba(0,0,0,.04)`
- `--shadow-2: 0 2px 8px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04)`
- `--shadow-3: 0 8px 24px rgba(0,0,0,.10)`

## Assets

Real assets live in `design/assets/`:
- `aaron-profile.png` — author avatar (used in hero, post meta bar, author card)
- `apple-touch-icon.png` — used as the brand mark in the header
- `favicon-32x32.png` — favicon
- `colors_and_type.css` — design tokens (see above)

The post cover currently points at an Unsplash URL as a placeholder. Replace per article when implementing.

Inline SVGs (search, theme, calendar, clock, comment, anchor, share icons) are written directly into the markup at 12–18px, `currentColor`, `stroke-width: 2`, round caps/joins. Keep this style if extending.

## Files in this bundle

```
design_handoff_aaron_blog/
├── README.md                  ← this file
└── design/
    ├── Home.html              ← home page mock
    ├── Post.html              ← single-post mock
    ├── home.css               ← home + shared chrome styles
    ├── post.css               ← post-only additions (loaded after home.css)
    ├── posts-data.js          ← seed data for the post list
    └── assets/
        ├── aaron-profile.png
        ├── apple-touch-icon.png
        ├── colors_and_type.css ← design tokens (single source of truth)
        └── favicon-32x32.png
```

Open either HTML file directly in a browser to view the mock. They are fully static — no build step required.

Reference renders live in `screenshots/`:
- `01-home-light.png` / `02-home-dark.png` — home page, both themes
- `03-post-light-top.png` / `04-post-light-body.png` — post header + body, light
- `05-post-dark-top.png` / `06-post-dark-body.png` — post header + body, dark

## Implementation notes for Claude Code

- The site is **Hugo + PaperMod**. PaperMod already has light/dark, TOC, share, prev/next, taxonomy listing, and home-info partials. Map each section above onto the partial that already exists rather than re-implementing.
- The token sheet (`assets/colors_and_type.css`) is the cleanest port surface — drop it into `assets/css/extended/` so it overrides PaperMod's vars without forking the theme.
- Featured-cards, dense post list, "Now" strip, and TOC active-section highlighting are the additions PaperMod doesn't ship; those will need new partials or a layout override.
- Cover image, callout, and reading-progress bar are also custom; they belong in the single-post layout override.
- Keep typography on the system stack — do **not** introduce a webfont.

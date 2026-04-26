# Design Handoff: Deferred Items

This spec tracks design elements from `design_handoff_aaron_blog/` that
were implemented with hardcoded values for the initial port. Each section
below describes the current shortcut and the plan to make it data-driven.

## Status

- **Tokens, chrome, home, single-post layouts**: shipped 2026-04-25.
- **Items below**: hardcoded; no behavior gap, just no dynamic source yet.

---

## 1. "Now" strip on the home page — DONE 2026-04-25

Now items live in `data/now.yaml`. Edit that file to update — no template
changes required. The `updated:` date renders next to the section
heading in muted type so stale states are visible at a glance.

Values support markdown, so you can include inline links:
```yaml
- label: Reading
  value: "[The Making of a Manager](https://...)"
```

---

## 2. Author bio + links on single posts

**Current state**: `layouts/_default/single.html` falls back to a
hardcoded bio string and pulls links from `site.Params.socialIcons`.

**Goal**: separate "social presence" (footer) from "author card bio +
links" (single post). The author card should have its own configurable
copy block.

**Implementation plan**:
1. Add to `config.yml` under `params:`:
   ```yaml
   author: Aaron Held
   authorBio: |
       Engineering leader and software architect based in Philadelphia.
       Twenty years of building teams, shipping product, and writing about
       the parts that don't fit in a roadmap doc.
   authorLinks:
       - name: LinkedIn
         url: https://linkedin.com/in/aaronheld/
       - name: Bluesky
         url: https://bsky.app/profile/aaronheld.com
       - name: GitHub
         url: https://github.com/aheld
       - name: Email
         url: mailto:aarondheld@gmail.com
   ```
2. In the author-card section of `single.html`, swap
   `range site.Params.socialIcons` for `range site.Params.authorLinks`.

**Effort**: 5 minutes.

---

## 3. Post kicker text

**Current state**: kicker (the small accent text above the H1 — e.g.
"Management · Featured essay") is generated as
`<first-category> [· Featured essay]`. Posts can override with a
front-matter `kicker:` field.

**Goal**: this is already mostly working — front-matter override exists.
The deferred piece is just deciding the editorial convention. No code
change required.

**Action**: when writing future posts, use `kicker: "Management · Long
read"` in front matter when the auto-derived label feels wrong.

---

## 4. Comment count pill

**Current state**: The post meta-bar omits the "12 comments" pill from
the design — there's no comments backend wired up.

**Goal**: render a comments pill that links to a real conversation.

**Implementation plan**: depends on `specs/spec-bluesky-comments.md`.
Once Bluesky comment threads are integrated:
1. Each post's front matter (or a Bluesky API call) provides the
   comment-thread URI and reply count.
2. Add the pill to the meta-bar in `single.html`:
   ```go-html-template
   {{- with .Params.bskyThread }}
   <a class="pill" href="{{ . }}" target="_blank" rel="noopener">
       <svg ...></svg>
       {{ $.Params.bskyReplyCount | default 0 }} comments
   </a>
   {{- end }}
   ```

**Effort**: blocked by the Bluesky comments work.

---

## 5. Featured-post selection

**Current state**: `layouts/index.html` looks for `featured: true` in
post front matter; if fewer than 2 posts are flagged, falls back to the
two newest posts.

**Goal**: this is already working as designed. The deferred action is
editorial: tag 1–2 evergreen posts with `featured: true`. Currently the
home page falls back to "newest 2" because no current posts are flagged.

**Action**: when ready to pin specific essays, add `featured: true` to
their front matter. No template changes needed.

---

## 6. Search keyboard shortcut polish

**Current state**: ⌘K navigates to `/search/`. The design's mock
intercepts ⌘K and focuses an inline search input — we don't have an
inline input; PaperMod's search is a full page.

**Goal**: optionally upgrade to an inline command-palette style search.

**Implementation plan**: out of scope for the design port. The current
behavior (⌘K → search page) is functionally equivalent for now.
Revisit if the search UX feels heavy.

---

## 7. Reading-progress + active-TOC

**Current state**: Both work via `partials/extend_footer.html`.
TOC is opt-in per post via `showtoc: true` in front matter (PaperMod
default; site has `showtoc: false` globally).

**Goal**: working as designed.

**Action**: enable `showtoc: true` on long-form posts where the rail
adds value. The CSS hides the rail on viewports < 1180px, so it's safe
to leave on by default if desired.

# Stage 4: Publish & Amplify

**ICM Layer**: L4 (active work). Per-piece, ephemeral, archived after publish.

## Purpose

Take the finished draft live on the blog, then drive readers to it from LinkedIn, Bluesky, and Threads. Establish bi-directional links between the blog post and its LinkedIn discussion thread so engagement on either surface points to the other. Capture a post-publish retrospective in the PR description — git remembers, future-Aaron benefits.

This stage is genuinely sequential. The blog must be live before LinkedIn (you need the URL). LinkedIn must be live before the back-link update (you need the LinkedIn URL). Bluesky and Threads come last because they're shorter and benefit from cross-references to LinkedIn discussion already in motion. Don't parallelize — the order is the value.

## Inputs

- `03_draft/[slug]/index.md` (signed-off draft)
- `03_draft/[slug]/summary.md`
- `03_draft/[slug]/social-hooks.md`
- `_config/platforms.md` (LinkedIn / Bluesky / Threads requirements, dated)
- `_config/constraints.md`
- The existing `publish-blog` skill at `.claude/skills/publish-blog/SKILL.md` for the blog-publish mechanics (commit, deploy, verify)

## Process

The sequence has 5 sub-steps with a checkpoint between each. Each sub-step is a small win — that's deliberate, to keep momentum across what would otherwise feel like a long publish slog.

### Sub-step 1: Blog goes live

1. Copy `03_draft/[slug]/index.md` (and any images) to `content/post/[slug]/index.md`.
2. Flip `draft: true` → `draft: false` in front matter.
3. Verify front matter is complete: title, date, description, categories, tags, cover image with alt text.
4. Commit with the format from the repo's `CLAUDE.md`. Push. Deployment runs.
5. Use existing `publish-blog` skill mechanics: `gh run list` to monitor, WebFetch the live URL to verify content is up.
6. Confirm: live URL is accessible and renders correctly.

**Checkpoint**: live URL captured. Aaron picks the LinkedIn hook from `social-hooks.md` (or writes a fresh one).

### Sub-step 2: LinkedIn post

1. Compose the LinkedIn post using the chosen hook from `social-hooks.md`. Format per `_config/platforms.md`.
2. Include the blog URL near the end of the post (LinkedIn favors posts with later links, but they can rank fine — see platforms.md).
3. Aaron posts manually to LinkedIn. (We don't auto-post; the platform's algorithm cares about authentic posting behavior.)
4. Aaron pastes the LinkedIn post URL back into Claude.

**Checkpoint**: LinkedIn URL captured.

### Sub-step 3: Back-link the blog post

1. Edit `content/post/[slug]/index.md` to add a "Comment on LinkedIn" line near the close, linking to the LinkedIn post URL.
   - Format example from existing posts: `[Comment on LinkedIn if this story resonated with you](https://www.linkedin.com/posts/...)`
2. Commit and push the back-link update with a separate commit (`Add LinkedIn discussion link to post: [title]`). Deployment runs.
3. Verify the back-link is live.

**Checkpoint**: bi-directional links established. Blog ↔ LinkedIn. Each surface points to the other.

### Sub-step 4: Bluesky and Threads

1. Compose Bluesky post (300-char limit per `_config/platforms.md`). Different angle than LinkedIn — these audiences differ. Include blog URL.
2. Compose Threads post (longer limit, see platforms.md). Can reference the LinkedIn discussion if it's already getting engagement.
3. Aaron posts both manually.

**Checkpoint**: all four surfaces live (blog, LinkedIn, Bluesky, Threads).

### Sub-step 5: PR self-review note

The PR for this post (the commits from sub-steps 1 and 3) gets a retrospective added to its description — written **after** publishing while the work is fresh, **before** archiving.

```markdown
## Post-publish self-review

**What worked**:
- [What landed cleanly. Sections that came together fast. A line that felt right.]

**What was harder than expected**:
- [Where the draft stalled. What I underestimated.]

**What I'd change next time**:
- [Process or content lessons.]

**Stage timing**:
- Research: [how long]
- Outline: [how long]
- Draft: [how long]
- Publish/amplify: [how long]
- Total: [...]

**Feature requests surfaced**:
- [Link to any PRDs created in feature-requests/]
```

Use `gh pr edit [number] --body` to update the PR description, or include the retro in a follow-up commit's body.

**Checkpoint**: PR retrospective written. Stage 4 complete.

### Archival

Move all `[slug]/` working folders from `01_research/`, `02_outline/`, `03_draft/`, `04_publish_amplify/` into `_archive/[slug]/`. The active stage folders stay clean for the next piece.

## Output Format

Files in `04_publish_amplify/[slug]/`:

### `checklist.md`

A live status file tracking the 5 sub-steps and capturing URLs:

```markdown
# Publish Checklist: [Post Title]

- [ ] 1. Blog live
  - URL: https://www.aaronheld.com/post/[slug]/
  - Commit: [sha]
  - Deployed: [timestamp]
- [ ] 2. LinkedIn posted
  - Hook used: [from social-hooks.md, which one]
  - URL: [LinkedIn post URL]
  - Posted: [timestamp]
- [ ] 3. Blog back-linked to LinkedIn
  - Commit: [sha]
  - Deployed: [timestamp]
- [ ] 4a. Bluesky posted
  - URL: [...]
- [ ] 4b. Threads posted
  - URL: [...]
- [ ] 5. PR retrospective written
  - PR: [#number]
```

### `pr-retro.md`

The retrospective text, before it's pasted into the PR description. Kept as a file so it survives in `_archive/` after the PR is closed and (eventually) GitHub UI changes.

## Done Looks Like

> All four surfaces live with bi-directional blog ↔ LinkedIn links. PR contains the retrospective. Working folders archived.

## Anti-Patterns to Avoid

- **Parallelizing the publish sequence**: blog must be live → then LinkedIn → then back-link → then Bluesky/Threads. The order is the value.
- **Auto-generating LinkedIn from the title**: use the candidate hooks from `03_draft/[slug]/social-hooks.md`. The hook is platform-specific work, not template substitution.
- **Skipping the back-link**: bi-directional links are the whole point of having LinkedIn at all. Without the back-link, blog readers never find the discussion.
- **Pasting the same text on Bluesky and Threads**: different platforms, different audience cadences, different lengths. Tailor each.
- **Skipping the retrospective**: "I'll do it later" means it doesn't happen. Write it before archiving.
- **Archiving before retrospective is written**: archival is the last thing. Retro first.

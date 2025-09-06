# Screenshot Organization for Claude Workflow Blog Post

## Directory Structure
```
content/post/claude-workflow-blog/
├── index.md
├── screenshots/
│   ├── README.md (this file)
│   ├── 01-setup/
│   ├── 02-planning/
│   ├── 03-research/
│   ├── 04-structure/
│   ├── 05-writing/
│   ├── 06-testing/
│   ├── 07-assets/
│   ├── 08-review/
│   ├── 09-deployment/
│   └── 10-monitoring/
└── featured-image.jpg (optional)
```

## Naming Convention

### Format: `{step}-{component}-{description}.{ext}`

**Step Numbers:**
- 01-setup
- 02-planning  
- 03-research
- 04-structure
- 05-writing
- 06-testing
- 07-assets
- 08-review
- 09-deployment
- 10-monitoring

**Component Types:**
- `terminal` - Terminal/command line interfaces
- `browser` - Browser screenshots
- `claude` - Claude Code interface
- `hugo` - Hugo server output
- `github` - GitHub interface (Actions, commits, etc.)
- `editor` - File editor/IDE views
- `mobile` - Mobile responsive views

**Description:**
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise
- Include context when needed

### Examples:
- `01-terminal-dual-setup.png` - Two terminals side by side
- `01-browser-hugo-server-running.png` - Browser showing Hugo server
- `02-claude-planning-todo-list.png` - Claude's TodoWrite output
- `03-terminal-search-existing-posts.png` - Grep command results
- `05-claude-collaborative-writing.png` - Writing process in action
- `06-browser-live-reload-demo.png` - Hugo live reload
- `09-github-actions-deploying.png` - GitHub Actions workflow
- `10-browser-live-site-verification.png` - Final published post

## File Specifications

**Image Format:** PNG preferred for screenshots (better text clarity)
**Maximum Width:** 1200px (for web optimization)
**Quality:** High quality for text readability
**Compression:** Optimize for web while maintaining clarity

## Alt Text Guidelines

Each screenshot should have descriptive alt text:
- Describe what's shown in the image
- Include relevant text content when applicable  
- Make it accessible for screen readers
- Keep it concise but informative

### Alt Text Examples:
- "Terminal showing Hugo server running with live reload enabled"
- "Claude Code interface displaying TodoWrite tool with blog article planning tasks"
- "Browser showing local development server at localhost:1313 with blog post preview"
- "GitHub Actions workflow page showing successful deployment to Azure Static Web Apps"

## Usage in Markdown

```markdown
![Alt text description](screenshots/01-setup/01-terminal-dual-setup.png)
*Caption: Setting up dual terminal workflow - Hugo server in left pane, Claude work in right pane*
```

## Capture Checklist

Before taking each screenshot:
- [ ] Clean up terminal history if needed
- [ ] Ensure proper window sizing
- [ ] Check for any sensitive information
- [ ] Verify good contrast and readability
- [ ] Position windows for clear demonstration
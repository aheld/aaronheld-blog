# Hugo Site Context

Technical context for the Hugo static site that publishes to https://www.aaronheld.com. **This file is for site infrastructure, theme, build, and deployment work** — not for content production.

For content work (writing posts, planning, social cross-posting), see `content-workspace/CLAUDE.md`. The two workspaces are separate by design.

## Project Overview

Aaron Held's Blog is a Hugo-based static site using the PaperMod theme, deployed to Azure Static Web Apps. The site has 15+ years of content history and 70+ posts dating back to 2008.

## Technology Stack

- **Hugo**: Static site generator (v0.146.0 in CI/CD)
- **Theme**: PaperMod via Go modules (`github.com/adityatelange/hugo-PaperMod`)
- **Hosting**: Azure Static Web Apps
- **Infrastructure**: Terraform for Azure resource management
- **CI/CD**: GitHub Actions for automated deployment

## Directory Structure (site infrastructure)

- `content/` — Markdown content files
  - `content/post/` — Blog posts (70+, dating to 2008)
  - `content/about.md` — About page
- `static/` — Static assets (images, icons, config files)
- `layouts/` — Custom Hugo template overrides
- `assets/css/extended/` — Custom CSS extensions
- `infrastructure/` — Terraform configuration for Azure
- `public/` — Generated site output (gitignored)

## Key Configuration Files

- `config.yml` — Main Hugo configuration with PaperMod theme settings
- `.github/workflows/azure-static-web-deploy.yml` — CI/CD pipeline
- `static/staticwebapp.config.json` — Azure Static Web Apps configuration
- `go.mod` — Hugo module dependencies

## Development Commands

### Hugo
- `hugo server` — Start local development server at http://localhost:1313
- `hugo server -D` — Include draft posts in local server
- `hugo server --navigateToChanged` — Auto-navigate to changed content during development
- `hugo` — Build static site to `/public` directory
- `hugo --minify` — Build with minification (production build)
- `hugo --minify --baseURL https://HOSTNAME/` — Production build with specific base URL

### Infrastructure (Terraform)
- `cd infrastructure` — Navigate to Terraform directory
- `terraform init` — Initialize Terraform state
- `terraform plan` — Preview infrastructure changes
- `terraform apply` — Apply infrastructure changes to Azure

### Azure CLI Setup (from `infrastructure/README.md`)
```bash
az login
az account show
az account list --query "[].{name:name, subscriptionId:id}"
az account set --subscription="<subscription_id>"
```

## Theme Customization

### PaperMod Configuration
- Dark/light mode toggle enabled
- Search functionality with Fuse.js
- Social sharing buttons (Bluesky, LinkedIn, Reddit, Facebook)
- Reading time display
- Breadcrumbs navigation
- Custom callout shortcode support

### Custom Extensions
- Extended CSS in `assets/css/extended/`
- Custom head template overrides in `layouts/partials/`
- Callout shortcode in `layouts/shortcodes/`

## Deployment

### Automated Deployment
GitHub Actions automatically deploys on:
- Push to `main` branch
- Pull requests to `main`
- Ignores changes to `infrastructure/`, `archetypes/`, and `README.md`

### Build Process
1. Checkout with submodules
2. Setup Hugo v0.146.0
3. Build with `hugo --minify --baseURL https://$HOST_NAME/`
4. Deploy to Azure Static Web Apps

### Required Secrets
- `AZURE_STATIC_WEB_TOKEN` — Azure deployment token
- `HOST_NAME` — Production hostname
- `GITHUB_TOKEN` — Automatically provided

## Common Infrastructure Tasks

### Modifying infrastructure
- Always run `terraform plan` before `terraform apply`
- Changes trigger manual deployment (excluded from CI/CD)

### Debugging deployment
- Check GitHub Actions logs for build errors
- Verify Hugo version compatibility (currently 0.146.0)
- Ensure all required secrets are configured

### Working with theme files
- PaperMod is consumed via Go modules — don't edit theme files directly
- Customize via `layouts/partials/` (overrides) and `assets/css/extended/` (CSS)

## Hugo Post File Format (for reference)

The published file format that the content pipeline produces and Hugo consumes:

```yaml
---
title: "Post Title"
date: YYYY-MM-DDTHH:MM:SSZ
draft: false
description: "1-2 sentence summary for SEO and social cards"
categories: ["..."]
tags: ["..."]
cover:
  image: "filename.jpg"
  alt: "Descriptive alt text"
  caption: "Optional caption with attribution"
---

[Post body in Markdown]
```

Posts live at `content/post/[slug]/index.md` with images co-located. The `content-workspace/` pipeline produces this file and copies it into place at publish time. Do not author posts directly in `content/post/` — that bypasses the research, outline, and review stages.

## Git Commit Standards

### Commit Message Format

**Subject Line (required)**
- Sentence case, first letter capitalized
- Descriptive and specific
- Examples: `Add new post: The Weapon by Fredric Brown`, `Fix capitalization in title and add LinkedIn comment link`

**Body (for complex changes)**
- Bullet points with hyphens
- Start each bullet with an action verb (Add, Fix, Update, Remove, etc.)
- Specific about what was modified and why

Example:
```
- Enable home-info mode with professional introduction
- Add custom home_info.html template with profile photo
- Configure responsive design for mobile compatibility
```

**Footer (required when working with Claude)**
```
🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Pre-commit hygiene
- Stage specific files (`git add [files]`), not `git add .` — avoids accidentally staging working files from `content-workspace/` or stray artifacts.
- For content work, the `04_publish_amplify` stage in `content-workspace/` handles staging, commit, push, and deployment monitoring. This commit-standards section governs *infrastructure* commits.

## What is NOT in this file

- Voice, tone, audience, brand identity → `content-workspace/_config/voice-and-tone.md`, `audience.md`
- Post research, outlining, drafting workflow → `content-workspace/01_research/`, `02_outline/`, `03_draft/` CONTEXT files
- LinkedIn / Bluesky / Threads platform details → `content-workspace/_config/platforms.md`
- Publishing sequence (blog → social → back-link) → `content-workspace/04_publish_amplify/CONTEXT.md`
- Recurring themes, references, signature moves → `content-workspace/_config/themes.md`, `recurring-references.md`, `signature-moves.md`

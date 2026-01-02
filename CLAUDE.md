# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Aaron Held's Blog is a Hugo-based static site using the PaperMod theme, deployed to Azure Static Web Apps. The site serves as a personal/professional blog with 15+ years of content history.

## Development Commands

### Hugo Development  
- `hugo server` - Start local development server at http://localhost:1313
- `hugo server -D` - Include draft posts in local server
- `hugo server --navigateToChanged` - Auto-navigate to changed content during development
- `hugo` - Build static site to `/public` directory
- `hugo --minify` - Build with minification (production build)
- `hugo --minify --baseURL https://HOSTNAME/` - Production build with specific base URL

### Infrastructure Management
- `cd infrastructure` - Navigate to Terraform directory
- `terraform init` - Initialize Terraform state
- `terraform plan` - Preview infrastructure changes
- `terraform apply` - Apply infrastructure changes to Azure

### Azure CLI Setup (from infrastructure/README.md)
```bash
az login
az account show
az account list --query "[].{name:name, subscriptionId:id}"
az account set --subscription="<subscription_id>"
```

## Architecture

### Technology Stack
- **Hugo**: Static site generator (v0.146.0 in CI/CD)
- **Theme**: PaperMod via Go modules (`github.com/adityatelange/hugo-PaperMod`)
- **Hosting**: Azure Static Web Apps
- **Infrastructure**: Terraform for Azure resource management
- **CI/CD**: GitHub Actions for automated deployment

### Directory Structure
- `content/` - Markdown content files
  - `content/post/` - Blog posts (70+ posts dating to 2008)
  - `content/about.md` - About page
- `static/` - Static assets (images, icons, config files)
- `layouts/` - Custom Hugo template overrides
- `assets/css/extended/` - Custom CSS extensions
- `infrastructure/` - Terraform configuration for Azure
- `public/` - Generated site output (gitignored)

### Key Configuration Files
- `config.yml` - Main Hugo configuration with PaperMod theme settings
- `.github/workflows/azure-static-web-deploy.yml` - CI/CD pipeline
- `static/staticwebapp.config.json` - Azure Static Web Apps configuration
- `go.mod` - Hugo module dependencies

## Content Management

### Creating New Posts
Posts are organized in individual directories under `content/post/` with:
- `index.md` - Post content with YAML front matter
- Associated assets (images) co-located in the same directory

### Front Matter Structure
```yaml
---
title: "Post Title"
date: 2023-01-01T00:00:00Z
draft: false
categories: ["Category"]
tags: ["tag1", "tag2"]
---
```

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
- `AZURE_STATIC_WEB_TOKEN` - Azure deployment token
- `HOST_NAME` - Production hostname
- `GITHUB_TOKEN` - Automatically provided

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

## Common Tasks

When working with content:
- New posts go in `content/post/new-post-name/index.md`
- Images should be co-located with posts
- Use Hugo's built-in date formatting: `January 2, 2006`

When modifying infrastructure:
- Always run `terraform plan` before `terraform apply`
- Changes trigger manual deployment (excluded from CI/CD)

When debugging deployment:
- Check GitHub Actions logs for build errors  
- Verify Hugo version compatibility (currently 0.146.0)
- Ensure all required secrets are configured

## Git Commit Standards

### Commit Message Format
Follow this structure for all commits:

**Subject Line (Required)**
- Use sentence case with first letter capitalized
- Be descriptive and specific about what changed
- Examples: "Add new post: The Weapon by Fredric Brown", "Fix capitalization in title and add LinkedIn comment link"

**Body (For Complex Changes)**
- Use bullet points with hyphens for multiple changes
- Start each bullet with action verb (Add, Fix, Update, Remove, etc.)
- Be specific about what was modified and why
- Example:
  ```
  - Enable home-info mode with professional introduction
  - Add custom home_info.html template with profile photo
  - Configure responsive design for mobile compatibility
  ```

**Footer (Required for Claude Code)**
Always include this exact footer when working with Claude:
```
🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Content Publishing Workflow

**Creating New Posts**
1. Create directory: `content/post/post-slug-name/`
2. Add `index.md` with proper front matter:
   ```yaml
   ---
   title: "Post Title"
   date: 2025-01-01T00:00:00Z
   draft: false
   categories: ["Category"]
   tags: ["tag1", "tag2"]
   ---
   ```
3. Add any images to the same directory
4. Test locally with `hugo server`
5. Commit and push to publish

**Publishing Process**
1. **Stage files**: `git add [files]`
2. **Commit**: Use proper commit message format
3. **Push**: `git push` triggers automatic deployment
4. **Verify**: Check https://aaronheld.com after 2-3 minutes

**Automatic Deployment**
- Triggers on push to `main` branch
- Uses Hugo 0.146.0 to build site
- Deploys to Azure Static Web Apps
- Excludes infrastructure/, archetypes/, README.md from triggering builds
- memorize
- always remeber to write in my style
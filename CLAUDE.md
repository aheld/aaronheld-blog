# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Aaron Held's Blog is a Hugo-based static site using the PaperMod theme, deployed to Azure Static Web Apps. The site serves as a personal/professional blog with 15+ years of content history.

## Development Commands

### Hugo Development
- `hugo server` - Start local development server at http://localhost:1313
- `hugo server -D` - Include draft posts in local server
- `hugo` - Build static site to `/public` directory
- `hugo --minify` - Build with minification (production build)

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
- **Hugo**: Static site generator (v0.140.2 in CI/CD)
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
2. Setup Hugo v0.140.2
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
- Verify Hugo version compatibility (currently 0.140.2)
- Ensure all required secrets are configured
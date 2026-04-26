# CLAUDE.md — Repo Context Router

This repo holds Aaron Held's blog at https://www.aaronheld.com. It contains **two separate workspaces**, and the right one to read depends on what you're about to do. **Read this file first, then route to the appropriate context.**

## What is this repo?

A Hugo static site (PaperMod theme, Azure Static Web Apps, 70+ posts since 2008) **plus** a structured content production pipeline that feeds the site. The two are intentionally separated so content work and infrastructure work don't tangle.

## Routing Decision Tree

Pick the path that matches the user's request:

### → Content production work

Triggers: "let's write a post," "research [topic]," "outline this," "draft a post about X," "publish this," "write a LinkedIn post," "let's plan a piece on Y," anything about voice / tone / audience / themes / cross-posting.

**Read first**: [`content-workspace/CLAUDE.md`](./content-workspace/CLAUDE.md)
**Then**: `content-workspace/CONTEXT.md` for stage routing, plus the relevant stage's CONTEXT file and `_config/` files.

The content workspace is a 4-stage pipeline (research → outline → draft → publish & amplify) with checkpoints between stages and a reference layer in `_config/` (voice, audience, themes, signature moves, recurring references, format patterns, platforms, constraints).

### → Hugo / site infrastructure work

Triggers: "build the site," "deploy," "fix the theme," "update layouts," "modify CSS," "Terraform / Azure / infrastructure," "GitHub Actions," "Hugo upgrade," "config.yml changes," "PaperMod customization."

**Read first**: [`HUGO_CONTEXT.md`](./HUGO_CONTEXT.md)

Covers: technology stack, directory structure, dev commands (`hugo server`, etc.), Terraform/Azure setup, theme customization, deployment pipeline, infrastructure commit standards.

### → Mixed or unclear

If the request crosses both (e.g., "the post needs a feature the blog doesn't have yet"):
- The content side captures the gap as a PRD in `content-workspace/feature-requests/`.
- The infrastructure side picks up the PRD when ready to implement.
- This way content writing isn't blocked by feature work, and feature work has real motivating context.

## Quick Map

```
/  (repo root)
├── CLAUDE.md              ← this file (router)
├── HUGO_CONTEXT.md        ← Hugo / infrastructure / theme / deploy
│
├── content-workspace/     ← content production pipeline
│   ├── CLAUDE.md          ← workspace entry point
│   ├── CONTEXT.md         ← stage routing
│   ├── _config/           ← voice, audience, themes, references, constraints
│   ├── 01_research/       ← stage 1
│   ├── 02_outline/        ← stage 2
│   ├── 03_draft/          ← stage 3
│   ├── 04_publish_amplify/← stage 4
│   ├── feature-requests/  ← PRDs surfaced during drafting
│   └── _archive/          ← finished pieces' working files
│
├── content/post/          ← Hugo's published posts (output of stage 4)
├── layouts/, assets/, static/  ← Hugo theme + assets
├── infrastructure/        ← Terraform / Azure
└── config.yml             ← Hugo configuration
```

## Why two workspaces?

Content production and site infrastructure have different rhythms, different inputs, and different "done" definitions. Mixing them in one CLAUDE.md meant every session had to wade through irrelevant context to get to the relevant part.

Splitting them lets each workspace stay sharp:
- The content pipeline can grow stages and reference files without bloating the infra context.
- The Hugo/infra context can document deployment and theme work without burying it under voice guidelines.
- The router (this file) stays small and stable — it changes only when the workspace shape itself changes.

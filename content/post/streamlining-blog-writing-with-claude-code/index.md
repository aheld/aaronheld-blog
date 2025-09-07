---
title: "Streamlining Blog Writing with Claude Code: My Complete Workflow"
date: "2025-09-01T20:00:00-05:00"
draft: false
categories: ["Development", "AI", "Workflow"]
tags: ["claude", "ai", "hugo", "workflow", "automation", "blogging"]
cover:
  image: "featured-image.jpg"
  alt: "Modern workspace with laptop and coffee representing AI-assisted writing workflow"
  caption: "The modern writer's setup: Where human creativity meets AI assistance"
---

## Introduction

After 25+ years of blogging and countless iterations of my writing and technical process, I've found something that actually makes writing *enjoyable* again: Claude Code. This isn't another "AI will replace writers" story - it's about how AI can my creativity while handling the tedious parts of content creation. It also actually helps me get to the publish stage.

Most of my blog posts are incomplete and first drafts that never get posted, now my **Robot Buddy** guides me through the end to end execution process.

In this post, I'll walk you through my complete workflow from initial idea to published post, showing exactly how Claude Code integrates with Hugo, my static site generator of choice. You'll see real screenshots, actual commands, and the genuine collaborative process that happens when human insight meets AI assistance.

## Following a Documented Workflow

The process I'm about to demonstrate isn't ad-hoc - it follows a specific Claude workflow file I've developed and refined over time. This workflow document serves as a guide that Claude can reference to maintain consistency across different blog writing sessions.

You can view the complete workflow file here: [create-blog-post-with-image.md](https://github.com/aheld/aaronheld-blog/blob/main/.claude/workflows/create-blog-post-with-image.md)

Having a documented workflow provides several benefits:
- **Consistency** across different writing sessions
- **Reproducible process** that others can follow
- **Iterative improvement** as I refine the workflow over time
- **Context for Claude** so it understands my preferences and standards

This workflow file acts as a blueprint that transforms what could be a chaotic creative process into a structured, repeatable system.

## The Setup: Four-Window Workflow

The foundation of my Claude Code blogging workflow is an effective four-window setup that creates a comprehensive writing environment. Here's how the windows work together:

![Four-window setup](screenshots/01-setup/01-four-window-setup.png)
*Four windows working in harmony: Hugo server, Claude Code, VSCode editor, and mobile browser preview*

### Window 1: Hugo Server Terminal (botttom right)
```bash
hugo server -D --navigateToChanged
```
This stays running throughout the entire writing process, providing instant feedback as content evolves. The `--navigateToChanged` flag automatically navigates your browser to updated content, making the feedback loop nearly instantaneous.

![Hugo server running](screenshots/01-setup/01-hugo-server-output.png)
*Hugo server providing real-time feedback at localhost:1313*

### Window 2: Claude Code Terminal (top right)
This is where the collaboration happens. I use Claude Code for planning, research, writing, and even debugging the build process when needed. Claude provides the strategic thinking and content generation while I guide the direction.

### Window 3: VSCode Editor (top left)
The editor window is where I review Claude's changes, make live updates, and maintain quality control. This is crucial for the collaborative process - I can see exactly what Claude is modifying and approve or adjust changes in real-time.

### Window 4: Browser with Mobile Emulation (bottom left)
A browser window set to mobile emulation mode gives me immediate feedback on how the content looks on smaller screens. Since most readers access blogs on mobile devices, this ensures the content is optimized for the actual reading experience.

The beauty of this four-window setup is the complete feedback loop: Claude generates content, I review it in VSCode, Hugo rebuilds it instantly, and I can immediately see both desktop and mobile presentations. It's like having a complete editorial and design team working in perfect synchronization.

I enjoy using claude code in the terminal as opposed to a dedciated AI editor.  This gives me the freedom of choice.  When doing web front end work I'll often use neovim in this workflow and add an extra desktop browser preview window alongside the mobile view.  I've found that the VSCode markdown preview stays in sync much better and that is helpful in this context.

## Step 1: Content Planning with Claude's TodoWrite

One of Claude Code's most useful features for writers is the TodoWrite tool. Instead of starting with a blank page (the traditional writer's nightmare), I begin by having Claude break down the writing project into manageable tasks.

 ```
 build a plan to write a blog article about my local claude workflow
 to write blog articles.  I want to highlight the steps where I use
 the workflow.
 
 Write the article by following the workflow and capturing
 screenshots and text commands at each step.

 Add a detail that I am running "hugo serve" in another terminal window.

 When the plan is done, write it to a local file under ./specs/
```

![Claude planning with TodoWrite](screenshots/02-planning/02-claude-planning-todo-list.png)
*Claude's TodoWrite tool breaking down the blog post into specific, actionable tasks* 

Here's what happened when I asked Claude to plan this blog post:

Claude immediately created a structured task list:
- Write engaging introduction about the Claude + Hugo workflow
- Document the dual-terminal setup process  
- Explain Claude's planning and research capabilities
- Show collaborative content creation process
- Document the testing and preview workflow
- Cover deployment and monitoring steps
- Write conclusion with benefits and recommendations

This planning phase serves two purposes:
1. **Breaks down complexity** - Writing becomes a series of smaller, manageable tasks
2. **Maintains focus** - Each task has a clear objective, preventing scope creep

The TodoWrite tool also tracks progress in real-time, showing completed, in-progress, and pending tasks. It's like having a skilled project manager built into your writing process.

Once this doc is written, I review it, edit it, and then ask Claude to reload it.

## Step 2: Research and Context Gathering

Claude Code excels at gathering context from multiple sources, making research feel less like archaeology and more like collaboration. For this blog post, I demonstrated a few key research approaches:

### Mining Existing Content
First, I used Claude's Grep tool to search through my years of blog content for related topics:

![Searching existing content](screenshots/03-research/03-terminal-grep-results.png)
*Grep search results showing 67 files containing workflow, AI, automation, or tool keywords*

```bash
grep -ri "workflow|AI|automation|tool" content/post/
```

This revealed relevant posts like "We Finally Care About Context" and "Answers Chat bot for your WordPress blog" - providing valuable context about my previous thoughts on AI and automation.

### Web Research for Current Information
Since AI tooling evolves rapidly, I had Claude perform web research to get current information about Claude Code workflows in 2025:

![Claude web research](screenshots/03-research/03-claude-web-research.png)
*Claude performing WebSearch to gather current information about Claude Code best practices*

The research revealed that Claude Code has evolved significantly, with developers reporting project completion in "30–45 minutes regardless of complexity" and new features like hooks for workflow automation. 

What was interestsing about this phase is that I didn't ask Claude to do ANY external research.  I left this in because my friend Claude seemed proud of this ability and I don't want it to feel unappreciated. 

### Context Synthesis
The magic happens when Claude combines historical context (your existing content) with current research (web findings) to inform the writing process. This isn't just information gathering - it's intelligent context weaving that ensures new content fits naturally with your existing body of work while incorporating the latest developments.

## Step 3: Collaborative Writing Process

Here's where things get meta - I'm actually writing this section while demonstrating the collaborative process itself. What you're reading right now was written through the iterative dance between human direction and AI assistance.

### The Edit Tool in Action
Rather than rewriting entire sections, Claude uses targeted edits to expand and improve content. For example, the astute reader will note that Claude originally planned to write about my 'Dual Terminal' workflow.  Upon reading that I realized it didn't match my screen, where I actually have four windows running. So I commanded the following:

```
 Change the setup from a "Dual Terminal Workflow"  to a 4 window
 workflow.  Highlight the same two terminals, but add the vscode editor
 (where I make live updates and review claude's changes) as well as a
 live reload browser set to mobile emulation
```

![Claude making a controlled edit](screenshots/05-writing/05-editing-the-content.png)
*Browser automatically refreshing to show new content as it's written*

### Real-time Feedback Loop
The Hugo server running in the background means I can see changes instantly:

![Live reload demonstration](screenshots/05-writing/05-four-window-content.png)
*Browser automatically refreshing to show new content as it's written*

### The Human-AI Partnership
This isn't Claude writing *for* me - it's Claude writing *with* me. I provide:
- **Direction and voice** - "Make this more conversational" or "Add a technical example here"
- **Content expertise** - My writing experience and specific knowledge
- **Quality control** - Reviewing each change to ensure it matches my style and intent
- **Final version** - I usually write or rewrite most of the content on these pages. Hopefully you believe that I am writing this sentance write now, but a future workflow will have Claude trained on my personal style so.....

Claude provides:
- **Structure and flow** - Organizing thoughts into coherent sections
- **Research synthesis** - Weaving together information from multiple sources  
- **Draft acceleration** - Turning rough ideas into polished prose
- **Consistency** - Maintaining tone and style throughout long pieces

### The Iterative Process
Writing becomes a conversation:

1. **Human**: "Expand the section on research methods"
2. **Claude**: *Adds detailed content with examples and screenshots*
3. **Human**: "This feels too technical - make it more accessible"  
4. **Claude**: *Revises language and adds analogies*
5. **Human**: "Perfect! Now add a transition to the next section"

This back-and-forth continues until the content feels right. It's collaborative editing at its finest.

## Step 4: Publishing and Deployment

The final step in the workflow demonstrates the seamless integration between content creation and deployment. Once the blog post is complete, publishing follows the established Git workflow with Claude's assistance for monitoring.

```
let's publish this!

Commit the current changes, use the github-action agent to watch 
for the job completion, and then check that version is 
visible online at its proper url and on the homepage as the most
recent post
```

Claude handles the entire deployment process:

1. **Stages and commits all changes** with proper commit message formatting
2. **Pushes to GitHub** to trigger the automated deployment pipeline
3. **Monitors GitHub Actions** using a specialized agent to watch workflow completion
4. **Verifies deployment status** and confirms draft behavior

### Git Commit Standards

Following the CLAUDE.md standards, commits use structured messages:

```bash
git commit -m "Add comprehensive blog post about Claude Code workflow

- Document complete 4-window workflow setup for collaborative writing
- Include real screenshots and command examples from actual process
- Cover planning, research, writing, and deployment phases
- Add featured image with proper Unsplash attribution
- Create draft version for review before publication

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Automated Deployment Pipeline

The GitHub Actions workflow automatically:
- Builds the Hugo site using version 0.146.0
- Deploys to Azure Static Web Apps
- Provides immediate feedback on deployment status

### Draft Verification

Claude verifies the deployment:
- **Homepage Check**: ✅ Confirms post visible as the most recent article
- **Direct URL Check**: ✅ Confirms 200 response and checks the content  
- **Deployment Status**: ✅ Monitors GitHub Actions completion

This verification ensures that the content is what I expected.  Since I'm also using BrowserMCP, I can see my desktop browser loading the page and I can double check the layout

## The Results: Why This Workflow Works

After implementing this Claude Code + Hugo workflow, several key benefits have emerged:

### Time Savings Without Quality Loss
What used to take me days writing and procrastinating now happens in 2-3 for focus effort. The quality has actually *improved*. The research phase is more thorough, the structure is more organized, and the iterative editing process catches issues I might have missed.

### Reduced Writer's Block
The TodoWrite planning phase eliminates the blank page problem. Instead of staring at an empty document wondering where to start, I have a clear roadmap of specific tasks to complete.

### Better Research Integration
Claude's ability to quickly search through my existing content and pull in current web research means my posts are better informed and more connected to my broader body of work.
Note: For more in depth research, like my post on [Agile and Economic Downturns](https://www.aaronheld.com/post/agile-vs-economic-downturns/), I modify this workflow to create a blank post and do the research in Gemini.  Once I have my draft, I past it into vscode and continue to interate here, additionally using claude to find a non-AI generated image.

### Authentic Collaboration
This isn't AI replacing human creativity - it's AI amplifying it. My voice, expertise, and editorial judgment remain central to the process. Claude handles the mechanical aspects while I focus on the creative and strategic elements.

## Getting Started: Your Next Steps

If you want to try this workflow yourself:

1. **Start with Claude Code** - Get familiar with the TodoWrite, Edit, and research tools
2. **Set up your environment** - Hugo server (or your static generator) + Claude workspace
3. **Begin with planning** - Let Claude break down your next writing project into manageable tasks
4. **Experiment with the research phase** - Try combining existing content searches with web research
5. **Embrace the iterative process** - Don't expect perfection on the first draft; let the collaboration evolve

The future of content creation isn't about AI replacing writers - it's about AI making writing more efficient, more research-driven, and frankly, more fun. Give it a try, and you might find that writing becomes enjoyable again.

I'll get to a future post detailing my setup.  I heavily leverage a few MCPs and claude's sub-agents for efficient context use.  Much of my thinking around multi-step context files is around memory management and keeping the token use optimizes. This workflow works fine on my pro plan ($20/month at the time of this writing)

*This entire blog post was written using the exact workflow described above, with real screenshots captured during the actual writing process. The meta-experience of documenting the process while using the process has been interestsing, becuase I keep tweaking the process as I use it.  I'll need to revise this post every few weeks at the rate AI workflows are evolving*

**If you are proud of your last project, then you didn't learn anything!**

---

Photo by [Johnny Briggs](https://unsplash.com/@johnnyboylee?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/black-typewriter-on-brown-wooden-table-Q2sI-omncsk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
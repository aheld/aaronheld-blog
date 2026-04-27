---
title: "The Island of Misfit Toys: Making the Azure Private Link Video"
date: "2026-04-26"
draft: false
description: "How my initial researched deep-dive created an excellent first storyboarded script, and how my second draft became the 5-minute explainer on Azure Private Link that I wanted."
categories: ["AI", "Workflow", "Video"]
tags: ["claude", "claude-code", "video", "remotion", "azure", "content-production", "workflow"]
cover:
  image: "storyboard.jpg"
  alt: "Storyboard frames showing a friendly PostgreSQL elephant behind a desk and AKS shipping containers walking through a door beneath an OPEN FOR BUSINESS sign"
  caption: "The Island of Misfit Toys: Slonik the elephant and the AKS shipping-container pods, who didn't make it into the final cut"
---

## I'm creating Island of Forgotten Dreams.

That's Slonik up there in the cover image, a friendly PostgreSQL elephant sitting behind a desk under a neon "OPEN FOR BUSINESS" sign, watching a line of AKS (Azure Kubernetes Service) shipping containers wait their turn at the door. He was going to star in a video about Azure Private Link. He had a co-star, too: Ricky the Raccoon, our hacker, who shows up first in a hard hat with a jackhammer, then in a top hat and monocle, and finally in a fedora and trench coat where he's figured out how to spin up his own Azure VM and walk straight in through the "Allow public access from any Azure service" checkbox. There was a *circus tent*, somewhere in Act 2, representing the entirety of Azure's customer base flooding through that checkbox like a carnival.

I love every one of them. None of them are in the [video I actually shipped](https://www.youtube.com/watch?v=EFtAm-Ao_kM). That video has no elephant. No costumes. No carnival. Just clean architecture diagrams, a numbered DNS resolution chain, and a raccoon silhouette who never says a word.

Here's how the misfits got to the island, and why the trip was the work.

## Step 1: Research before script

Before I wrote a single line of narration, I had Claude produce a DNS deep-dive on AKS-to-PostgreSQL Private Endpoints. The CNAME chain (`mydb.postgres.database.azure.com` resolves to `mydb.privatelink.postgres.database.azure.com`, which resolves differently depending on whether the query comes from inside a VNet linked to the Private DNS Zone), the `168.63.129.16` Azure DNS resolver, Private DNS Zone linking, the hub-and-spoke gotchas. Five thousand words of reference material I would never put in a video.

That research wasn't waste. It was load-bearing. Every claim the video makes, every arrow on the DNS chain, every label on the Private Endpoint, every "the attacker can't even resolve the address" beat, traces back to that document. When you skip the research step, your script writes things that *sound* right. When you don't, your script writes things you can defend.  (I'll have to write another post about my contrarian researcher, who works to prove me wrong.)

This is the part of AI-assisted content production I keep coming back to. The model is happy to write you a script cold. The script will be plausible. It will also be wrong in ways you won't notice until somebody on the engineering side does.

## Step 2: The script that was too good to make

With the research in hand, I wrote the first script. This is where Slonik was born.

It was a six-act narrative. Two parallel paths leading to the same database door, one labeled "The Internet," one labeled "From Our Services." Ricky the Raccoon arrives in costume one, brute-forces the door, fails. Costume two, social-engineers the door, fails. The team adds a firewall. A stagehand character literally rolls a fake wall in front of the public door, but it's too narrow, with a comically small potted plant covering the gap. Then Azure Functions can't connect because their IPs keep shuffling. Someone checks "Allow Azure services." The wall vanishes. The side door grows into an eight-lane highway terminating at a circus tent labeled "ALL OF AZURE: 1,000,000+ CUSTOMERS." Ricky returns in fedora and trench coat, signs up for a free Azure trial at a booth, and walks in alongside the legitimate Functions.

It was funny. It was *correct*. And I wasn't going to make it.

It's not "I can't animate." I could have eventually done it, and it would probably be easy for a number of people who I've worked with. The honest reason is two things, and they belong together:

**One, I wasn't willing to spend the money or the time on character animation for this particular project.** That's a budget call, not a capability ceiling. It's a fine call to make. It's a different admission than "I can't."  My goal was to build an AI-driven content creation workflow and to learn how rapidly I could build "good enough" explainer videos.

**Two, and this is the part I almost talked myself out of, the v1 script had drifted from the goal.** The goal was to explain Private Link to a technical audience. v1 was a great six-act animated short *about* Private Link. Those are different things. AI made it cheap to write the great-cartoon version, and once it existed on paper, it took real discipline to notice that the cartoon had quietly become the thing I was making, instead of the explainer it was supposed to support. I got carried away thinking I could compete with seasoned content creators on my first go.

The pivot is the post.

## Step 3: Cutting back to the actual job

The second script kept everything that mattered to the *goal* and dropped everything that had drifted away from it.

Same six acts. Same arc: naive public IP, firewall, the checkbox trap, Private Link, lockdown, recap. Same core thesis: static IPs aren't a cloud-native security model, DNS is what makes the new model work without code changes.

What changed was the visual language. Microsoft-style architecture diagrams. Dashed rectangles for VNets. Official Azure SVG icons instead of characters. Numbered circles ①②③④⑤ for the DNS chain, which became the educational centerpiece, because I could *actually animate* a numbered chain in Remotion in an afternoon. Connection lines drawing on as the narrator describes them. State changes via color shift instead of pratfall.

The raccoon survived. He survived because he was already the cheapest character to render: a flat silhouette of the Azure "Users" person icon with two pointed ears and a mask band. No costumes. No dialogue. Just lines extending toward the database and turning red with an X when they fail. The cheapest piece of the first script became the only character in the second.

Slonik did not survive. Slonik needs a face, a body, a chair, a desk, expression changes across six acts. He needs to look *relieved* when the firewall goes up and *bewildered* when the checkbox opens the floodgates. That's a real animation pipeline. For this project, on this budget, I wasn't going to build one.

Here's the part I want to credit, because it changed how I think about pivots: the v2 script wasn't only smaller, it was also more *correct*. While I was rewriting from "cartoon explainer" toward "diagram explainer," I had to actually re-engage with the technical material instead of letting the characters carry the explanation. That second pass surfaced a beat v1 didn't have: the privatelink CNAME exists in *public* DNS too, and without a Private DNS Zone link, it falls through to the original public IP. Same connection string, same CNAME, different final answer. The Private DNS Zone is the fork in the road. v1 hand-waved this. v2 had to land it, because there was no costume gag to lean on.

The pivot didn't only save production budget. It made me understand the thing better.

## Step 4: Make the honest version

The version I made (diagrams, numbered DNS chain, silhouette raccoon) took something like a tenth of the production budget the first script would have demanded. It also lands the same lesson, which is the only test that actually matters.

If you watch the [final video](https://www.youtube.com/watch?v=EFtAm-Ao_kM), you'll see almost everything from the first script's *thesis* and almost nothing from its *theater*. That's the trade off. The trade was worth making, but the trade isn't really the lesson. The lesson is that I had to catch the drift before the trade was even available to me. And I actually shipped it, working nights and weekends over a few days.

## What's actually on the island

Here's what I keep telling myself after this one:

- **AI makes it easy to drift from the goal.** It will hand you a great cartoon when you asked for an explainer. The capability ceiling isn't your animation skill or your tooling, it's your discipline about what the work is *for*. Re-read the brief halfway through. Then re-read it again. Without constraints, AI will continually remind you how brilliant your plan is because I think it *wants* to be used.
- **Research first is not optional.** A clever script with shaky technical grounding is worse than a plain script that's correct. Spend the upfront tokens on the boring document nobody will see. (Mine had `168.63.129.16` and CNAME chains in it. The video shows none of that. The video is right because the document was.)
- **The cheapest piece of the first draft is often the only piece of the final.** The raccoon silhouette was a throwaway in v1. He's the entire antagonist in v2. Pay attention to which elements are cheap to produce, those are the survivors.
- **The pivot is the practice.** Recognizing the drift and re-anchoring to the goal is the skill worth getting better at. AI doesn't change that. It just makes you do it faster, and more often, because the tooling keeps moving underneath you. (This is the through-line from [Streamlining Blog Writing with Claude Code](/post/streamlining-blog-writing-with-claude-code/): break the work into smaller deliverables with the right context at each step, *and* be willing to refactor the workflow itself as the tools change. The misfit-toys post is what that workflow looks like when it's mid-refactor.)

Slonik isn't deleted. He's on the island, with the three Rickys, the stagehand, the circus tent, and the eight-lane highway. They're cute. They just didn't fit in this production. I highly recommend [Recraft](https://www.recraft.ai/generate/characters); that tool is the first one that made me think these characters could actually come to life.

Maybe they fit into the next one, as I learn more about content creation and the available tooling continues to improve. One day, it will be as easy as making Flash animations on the timeline...

---

*Written about [this video](https://www.youtube.com/watch?v=EFtAm-Ao_kM). Sibling post to [Streamlining Blog Writing with Claude Code](/post/streamlining-blog-writing-with-claude-code/), same workflow philosophy, different medium, harder lessons about scope and drift.*

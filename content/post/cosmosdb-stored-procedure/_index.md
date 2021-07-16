---
title: "Cosmosdb Stored Procedures" # Title of the blog post.
date: 2021-07-14T08:17:56-04:00 # Date of post creation.
description: "A short tutorial on the creation and use of stored Proceduces in Azure cosmosDB."
featured: true # Sets if post is a featured post, making appear on the home page side bar.
draft: false # Sets whether to render this page. Draft of true will not be rendered.
toc: false # Controls if a table of contents should be generated for first-level links automatically.
# menu: main
featureImage: "/images/path/file.jpg" # Sets featured image on blog post.
thumbnail: "/images/path/thumbnail.png" # Sets thumbnail image appearing inside card on homepage.
shareImage: "/images/path/share.png" # Designate a separate image for social media sharing.
codeMaxLines: 10 # Override global value for how many lines within a code block before auto-collapsing.
codeLineNumbers: false # Override global value for showing of line numbers within code block.
figurePositionShow: true # Override global value for showing the figure label.
categories:
  - Azure
tags:
  - CosmosDB
layout: section.html
# comment: false # Disable comment if false.
---

# Why stored procedures?

Stored Procedures (sprocs) are functions that run on the server side of a database. In particular we will be talking about sprocs in CosmosDB.

The main reasons to use CosmosDB Sprocs are for atomic transactions and performance. All database operations completed in a single sproc call will be atomic. Since the sproc runs on the server the network latency for loading and saving documents will be considerably less than if you ran the same operations from a remote server

This short series will show you how to programmatically update stored procedures and explore thier basic functionality.
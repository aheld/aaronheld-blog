---
title: "Overview of Azure Static Web Apps" # Title of the blog post.
date: 2021-07-13 # Date of post creation.
description: "Azure static web apps are a new (2021) service offering that make deploying static and SPA apps (such as React and Vue) easy and extensible." # Description used for search engine.
featured: true # Sets if post is a featured post, making appear on the home page side bar.
draft: false # Sets whether to render this page. Draft of true will not be rendered.
toc: false # Controls if a table of contents should be generated for first-level links automatically.
menu: main
featureImage: "../appservicestatic-feature.png" # Sets featured image on blog post.
thumbnail: "/post/using-azure-static-web-apps/appservicestatic-thumb.png" # Sets thumbnail image appearing inside card on homepage.
shareImage: "/post/using-azure-static-web-apps/appservicestatic-thumb.png" # Designate a separate image for social media sharing.
codeMaxLines: 10 # Override global value for how many lines within a code block before auto-collapsing.
codeLineNumbers: true # Override global value for showing of line numbers within code block.
figurePositionShow: true # Override global value for showing the figure label.
categories:
  - Azure
tags:
  - hosting
  - tutorial
---

# Introduction

[Azure Static Web Apps](https://azure.microsoft.com/en-us/services/app-service/static/#overview) is a newer (2021) hosting option targeted towards statically generated websites and single page javascript applications.  

Previously when deploying static or javascript single page applications (SPA) to Azure, I copied a set of static html and js files to a storage account and put a CDN in front. That set was low cost, easy to reason about and extremely fast.

The major limitation that I found with storage accounts was that I didn't get to use any of the developer - SDLC enhancements that I've grown fond of after years of deploying production workloads on Azure App Service.  The App service beings deployment slots that will allow us to easily support preview or development tiers.  Other benefits for us include enhanced logging and http security.

In this series I'm going to demonstrate how to setup and deploy a static site (this blog) and take advantage of some of these advanced features.

## Sections

1. Introduction
2. [Setting Up the Infrastructure using Terraform](../terraform)
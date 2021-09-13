---
title: "Overview of Azure Static Web Apps" # Title of the blog post.
date: 2021-07-13 # Date of post creation.
description: "Azure static web apps are a new (2021) service offering that make deploying static and SPA apps (such as React and Vue) easy and extensible." # Description used for search engine.
featured: true # Sets if post is a featured post, making appear on the home page side bar.
draft: true # Sets whether to render this page. Draft of true will not be rendered.
toc: true # Controls if a table of contents should be generated for first-level links automatically.
# menu: main
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

Previously when deploying static apps to Azure, I've deployed a set of files to a storage account and put a CDN in front.  This setup is low cost, easy to reason about and extremely fast.

The major limitation that I found with storage accounts was that I didn't get to use any of the developer / SDLC enhancements that I've grown fond of after years of deploying production workloads on Azure App Service.

In this series I'm going to demonstrate how to setup and deploy a static site (this blog) and take advantage of some of the more advanced features such as deployment slots and custom IIS configuration.  

## Sections

1. Introduction
2. [Setting Up the Infrastructure using Terraform](../terraform)
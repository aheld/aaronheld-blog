---
title: "coupling de-coupled CMS"
date: "2009-04-27"
categories: 
  - "code"
  - "professional"
tags: 
  - "cms"
---

I'm hip deep in the design of a new CMS to power some large scale sites. The big buzzword going on at this level is around how the CMS products are designed to be 'de-coupled'. Specifically we are talking about decoupling the deliver of the site from the management of the content.

This is very understandable, as your backend needs can be very different then the portal. The backend CMS has rigid security and workflow concerns and the front-end is optimized to serve pages fast.

I'm seeing very little talk about the coupling needs of the site structure in terms of the content and this surprises me. The CMS has to have some level of knowledge as to how to front-end uses the content in order to be effective. Our current CMS maintains a concept of a 'portal Model' that reflects the page structure on the site. The CMS can serve multiple sites through different portal models. To me this seems a core need and a clear gap in the industry.

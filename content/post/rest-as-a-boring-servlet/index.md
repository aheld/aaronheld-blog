---
title: "Rest as a boring servlet"
date: "2008-04-22"
categories: 
  - "professional"
  - "python"
tags: 
  - "django"
  - "python"
---

A coworker whipped up a generic REST interface for any Ruby on Rails activerecord (data model).  What he described (in 5 minutes) was a nice implementation.  I wanted see how the generic django REST interface was coded.

[http://code.google.com/p/django-rest-interface/](http://code.google.com/p/django-rest-interface/)

I was pleasantly surprised to realize that they Python developers simply used the normal form processing to handle rest and didn't invent a new paradigm.

On an early project we tried to implement RESTlet for a java based REST application.  Under load we saw some strange problems and the code was reverted to normal servlets without too much pain.

The beauty of REST is its simplicity, yet there is so much energy being expended to 'simplify' it.

The real magic is to standardize on sending XML or JSON rather then url encoded data of an http form POST.

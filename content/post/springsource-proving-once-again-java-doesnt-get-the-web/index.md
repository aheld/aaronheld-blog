---
title: "SpringSource - proving once again Java doesn't get the web"
date: "2008-05-01"
categories: 
  - "professional"
  - "python"
tags: 
  - "java"
  - "python"
---

I just read an article in a java trade mag entitled: [SpringSource CEO: "The Future of Enterprise Java is Clear and Bright"](http://java.sys-con.com/read/557307.htm "Syscon on Java")

The premise sounds positive.  Basically they took OSGI, Spring and threw it on Tomcat as a web server.  The idea of being able to deploy OSGI bundles with the bag of beans development style of Spring is really compelling.

What this negative post is about is how they still don't get the 'web'.  My biggest issue with Java web development is that not enough attention is paid to modern web basics.  The very first thing that I noticed on the SpringSource website was the 15 year old style url.

http://www.springsource.com/web/guest/home

what is with the /web/guest/home for the homepage?  That is really bad SEO mojo

The idea of bundles that you can drop in for added functionality is fantastic, but you hit an ugly query string laden url like:

http://www.springsource.com/repository/app/library/version/detail?name=org.apache.myfaces&version=1.2.2

as opposed to the far more buzzword complient library of plugins for something like django:

http://djangoplugables.com/projects/django-compress/

While the Java page shows you the really easy lines of Maven xml to paste into your pom, the python based django system talks about the usefulness of the actual bundle you are looking at.

And compare the old school search page of:

http://www.springsource.com/repository/app/search

to the happiness of a large input box with realtime results on:

http://djangoplugables.com/repositories/ At least this is better then the time I read the Jython website and was greeted by a 'blink' tag

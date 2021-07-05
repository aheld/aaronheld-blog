---
title: "grails java.sql.SQLException: Table not found in statement [insert into"
date: "2009-03-08"
categories: 
  - "code"
tags: 
  - "grails"
---

I'm spinning up a new [grails](http://www.grails.org "Goovy on Grails") experiment this weekend and ran into an error that I could not effectively google. So hopefully by adoping the very SEO style title others will benefit.

I really want to like grails, it is a full stack web development framework modeled after Ruby on Rails but written [Groovy](http://groovy.codehaus.org) with full access to the JVM.

I have an excellent project in mind for some facebook integration using a Java library I've some experience with so grails seemed to fit.

I built a simple domain class and wired it to the facebook API thinking to get a working interation done and ran into immediate problems.  The Grails convetion is that during develolment you hardcode some 'test' objects into the startup so that every time you start it creates a new set of database tables in an in-memory database.

I built a simple domain object:

> class RichMessage { String msg Integer from }

and put this into my 'startup'

> new RichMessage(msg:"test1",from:88117930).save() new RichMessage(msg:"test2",from:105019979).save()

The error that I saw was that the objects could not be inserted.  I spent a some time playing with my 'RichMessage' object on the web and in the grails shell.

Examining the stacktrace I saw this exception deeply nested down.

> Caused by: java.sql.SQLException: Table not found in statement \[insert into rich\_message (id, version, from, msg) values (null, ?, ?, ?)\]

So basically there was nothing wrong with my bootstrap file, the error was in the domain class itself.  I used 'from' - a reserved word.  That simple.  It would be nice if in the hundreds of lines of stacktrace there was some error on the hibernate table creation, but there was not.

As a contrast here is the error from Django/python for the same mistake:

> File "/Users/comcast/Documents/projects/mhi/pages/models.py", line 38 from = models.ForeignKey(User) ^ SyntaxError: invalid syntax

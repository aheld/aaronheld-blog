---
title: "Peeling back the onion of stupidity"
date: "2009-05-07"
categories: 
  - "code"
  - "professional"
tags: 
  - "agile"
  - "java"
  - "stupid"
---

I've mentioned the book [Adrenaline Junkies](http://www.amazon.com/gp/product/0932633676?ie=UTF8&tag=aarhel-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0932633676)![](http://www.assoc-amazon.com/e/ir?t=aarhel-20&l=as2&o=1&a=0932633676) in a previous post and I'm not seeing the value in a common language for discussing problems.

Today's pattern is the 'Onion of Stupidity'.  This is a common pattern where you build up hack upon workaround upon compromise, inject a little shortsightedness and wind up seeing a good chunk of your effort goes into cleaning it up.  A [colleague](http://codeartisan.blogspot.com/ "Jon Moore's blog") here promoted the term "technical debt" to describe issues were we these types of issues and help us prioritize them.  I'm thinking that my Onion is more about 'strategy debt'.  The onion is usually built with best intentions at all sides.

Peeling back the layers of stupidity is tedious and takes time, but cutting through it makes everyone in the room cry.

I'm sure we have all been here.  I had 2 instances of it today at work, and one with an old friend.  He wanted me to update some joomla modules and I said yes.  I go to ssh and wget the files and find out there is no ssh.  Without that I have to download the files, extract then and upload lots of little ones.  Then I find that some of the original files are edited so the have to be diffed.  Now I have to download the files and diff them.  Then I want to check but can't run it without the database.  I just restored my local ubuntu image and don't yet have MySQL. So I go to install MySQL and don't have connectivity yet between the VirtualBox and osx....

So the first layer of this Onion that I must peel is to fix Bridged Ethernet.  Or I cut the darn thing and move the site to a real hosting company.

So while I'm pretty much out of luck on my personal life here at my day job we all got together with a commitment to peel back our layers of issues as a team and focus on building out a solid foundation.  Hopefully the only onions we will have are the ones served on the sliders upstairs.....

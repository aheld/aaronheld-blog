---
title: "OSX vs Ubuntu, Windows wins?"
date: "2011-01-02"
categories: 
  - "code"
  - "python"
tags: 
  - "linux"
  - "python"
  - "windows7"
---

Ever since Barcamp I've been shopping for a personal laptop for general use as well as a development machine that I could use for work.  Our work issued machine is a loaded mac powerbook.  With a unix core osx has given me much of the power that I used to enjoy when I'd used linux as a primary os. However Apple is not doing wonders for free software and I felt the need to get back to my roots and move back to Linux.

I picked up a 4lb HP [DM4](http://www.shopping.hp.com/webapp/shopping/computer_can_series.do?storeName=computer_store&category=notebooks&a1=Category&v1=Ultra-Portable&series_name=dm4t_series&jumpid=in_R329_prodexp/hhoslp/psg/notebooks/Ultra-Portable/dm4t_series) and dual booted to Ubuntu with not issues.  The trackpad didn't work right, but a script off someones blog made it work reasonably ok.  A quick hop into debug mode showed that the drivers returned negative x-y coordinates when you use 2 fingers.  I downloaded the open source drivers to take a look at the code and saw that a patch was already in head.

Developing was a joy and eclipse opened nearly instantly.

Microsoft silverlight DRM is not (yet?) ported to linux so I dual boot to windows 7 to get the customer experience and use CIM products.  A funny thing happened to me while getting the 'customer' experience.   I liked it!   Windows 7 is much more usable then either osx or Linux and IE9 looks like it will be a really powerful platform for future development.

Around this time I picked up a python update on OSX and spent about 4 hours trying to get mysql and python to [talk to each other](http://www.google.com/search?q=mysql+python+osx).  I booted into windows and thought about how to use this platform as a development machine.

Enter [BitNami](http://bitnami.org/). Rather then deal with version conflicts I grabbed a virtual machine that is close to my target server and installed VMware Player.  Mapping a windows directory to the virtual machine lets me edit files in native windows while running my build chain on Linux.  The browser I use for development is finally the same browser used by the majority of my customers and my dev environment is much closer to my server environment as well.

For not I'm working through the rough edges of this setup and trying to find a decent windows SSH client but this setup seems to have legs.

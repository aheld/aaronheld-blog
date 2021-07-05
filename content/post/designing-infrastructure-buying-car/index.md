---
title: "Designing a new Infrastructure is like buying a new car"
date: "2009-06-17"
categories: 
  - "code"
  - "professional"
tags: 
  - "architecture"
---

Because I happen to be both buying a new car and deploying new infrastructure the realization dawned upon me about how similar these two activities are.

1) You start the investigation with some preconceived "gut-level" notions. code: Multiprocess distributed job engine is what I need car : I want a Mazda 3 with "Zoom Zoom"

2) Everybody has a story about why your choice is bad code: "In my last job I used a python-C++ wrapper from vcron" car : My cousin"s friends brother had a mazda and the engine fell out on 95

3) Everybody loves what they have (but its not for you) code: Our feed system rocks, oh but we don"t pull in news every minute car : I love my Civic, oh but I don"t have 3 kids where one of them is 6"2"

4) Everybody thinks what you currently have is no good code: "Your cache middleware is no good because it can"t run jobs"" car :  "Dude, you can"t drive a Camry and date girls"" (true comment post-divorce)

5) \*\* **You usually start this process due to a crash** \*\*

code: User gen data + no cache eviction = FAIL car : SUV from the side + swerve = One less Stop sign.

So my investigation has started and it is taking interesting twists.   We pull in a weather feed via a RESTish api and the vendor would like us to FTP a large data file instead.  This is clearly a good fit for a multiprocess job engine so that project has kicked off for real.  I"m looking at one of the top open source systems "Job Scheduler"" because that fit all my critericode:  It can spread jobs across multiple machines and give operations some command and control of background systems.  Our ops team is really good at the command line / Solaris thing so having our systems look more like shell scripts and less like java interface implementations will help. I did a good amount of research and made sure that this app was solaris friendly and patted myself on the back for caring about my ops team.  Just the other day I find out that the solaris binary is sparc only and we plan on running this on Solaris/x86.  First threat to my guy choice has manifested.

On the car front I went to reedman-toll and took the Mazda 3 (stick shift) around their test track with my daughter.  The car was a fun to drive but second gear took me from 5-25mph.  That will be awesome when I"m stuck in traffic (and pissed that I bought a manual rather then an automatic) but limited my sense of control over the gearing.  The point of a stick is to feel that "snick-snick" as you upshift around S curves and downshift into corners. In short there was no "Zoom-Zoom"

In my youth I would have just deployed my first choice (one day I should blog about when I thought it was a good idea to build a custom accounting program) and bought a car based on first impressions.

Now that I have less disposable income and more oversight on my engineering decisions am wiser I"ll take some time to really focus on what the needs are.

I"ll blog more on this later, but I have to work on my project plan for the Alfresco based CMS.

That was a good choice - Open source, Java, active community - "Zoom Zoom"..

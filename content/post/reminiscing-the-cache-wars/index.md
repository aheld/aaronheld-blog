---
title: "reminiscing the cache wars"
date: "2008-07-14"
categories: 
  - "professional"
  - "scalability"
---

Recently at work people are discussing the merits of different cache servers.  That brought back memories of my days as the R&D Product lead for a line of cache systems.

The high point was participating in the two week ["Cache Bake Off"](http://polygraph.ircache.net/Results/cacheoff-2/) hosted by NLANR (the team broke off and formed [The Measurement Factory](http://www.measurement-factory.com).  This was great fun where engineering teams from major companies got together to have thier systems pounded in a no holds barred performance test. I was working for a hardware company that had thier sights firmly set of being the leading tier two vendor (Tier one was considered too competative to take exponential growth risks).  I think my gear nailed it by achieving 80% of the performance of the leadning brand at 1/5 the price.  (And you could cluster 2 for less then half the cost and have over 50% better performance - if you order now you can get fee overnight shipping).

The test was run using software called web-polygraph running a 'workload'

The workload was considered to represent standard web traffic and put together by some sharp guys.

> One difficult part of this benchmark (and indeed most) was to develop the proper workload. Real-world Web traffic is incredibly complicated, both to understand and to simulate. Many workload attributes are well understood by themselves, but not when combined with each other. For example, we have a clear idea of real-world object size distributions. But how does object size combine with popularity and content-type? Are popular HTML objects larger, smaller, or the same as unpopular ones?

The per page breakdown was: `Type Percentage Reply Size Cachability Image 65.0% exp(4.5KB) 80% HTML 15.0% exp(8.5KB) 90% Download 0.5% logn(300KB,300KB) 95% Other 19.5% logn(25KB,10KB) 72%`

Surprisingly this mix is pretty close to our current page patterns.

Probably the best part about this test was the scientific way it was run.  There was no marketing aspect to in the charts and numbers that got published and once you entered you agreed to let them make your results known to the world - good or bad.

I wonder how many companies now would have enough faith in thier offering to allow objective test data to be released without markting/PR oversight?

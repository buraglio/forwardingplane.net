---
title: 'Upgrading a new SRX 3600'
date: Mon, 07 Feb 2011 22:29:00 +0000
draft: false
tags: [Security]
---

We are putting a few new SRX 3600 clusters into production soon, and we've had them for about 6 months in boxes. This presented a fairly significant issue, one that I didn't think about until it smacked me in the face.  
The code on these boxes was old. Very old. JunOS 9.2 old.  
No problem, lets just upgrade them to 10.4R something.

**Wrong**.

  

the code that shipped on these boxes was so old, and we waited so long to upgrade them that I was unable to upgrade them straight to anything modern. To compound the issue, the upgrade was only able to be performed from certain code level releases as noted [here](http://forums.juniper.net/t5/SRX-Services-Gateway/SRX-3400-upgrade-failure/m-p/55416).

  

This is a problem. I logged into the Juniper site to get the appropriate code, low and behold, it's not available. I had to contact jtac and convince them that the code wasn't there (which was a bit frustrating). Once they understood the issue (which took a bit longer than I expected; I don't have Agility services on these particular boxes or I would never have had the jtac "issue"), they provided me with a download link for junos-srx3000-9.6R4.4-domestic. Once I had that code I was able to upgrade to it and then to 10.4.

  

Not a huge issue, but something that was very annoying to have to jump through since I've never seen this issue upgrading a Juniper device.

  

  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
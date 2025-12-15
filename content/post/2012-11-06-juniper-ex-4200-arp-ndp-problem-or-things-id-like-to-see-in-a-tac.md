---
id: 10
title: 'Juniper EX 4200 ARP / NDP problem; or things I'd like to see in a TAC'
date: '2012-11-06T03:58:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/'
permalink: /2012/11/06/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/
Views:
    - '97'
categories:
    - Routing
---

    Recently we've run into an odd issue while routing on an EX4200 series.  These little JunOS boxes are a nice alternative for an entry level building router, they support L2/L3 functionality, a PVST+-ish protocol and, with advanced licensing, IPv6, ISIS and BGP. They have multi 10G interface options and come in a pluggable fiber option.  We use them all over for light layer 3.  They can also be stacked via stacking cables and fiber, which is very handy and makes them extremely versatile but not really applicable for the purpose of this entry.  Anyway, one of our buildings had some odd issues that popped up from time to time, normally over the course of several months.  How is manifests itself is an apparent corrupted ARP / NDP table.  Clearing both fixed their respective traffic....for a while.  While this problem in and of itself is moderately interesting, the real issue arose when, after an extensive JTAC experience, I couldn't find any reference to the PR that they said was causing this issue (slow memory leak). PR664807.  Even looking through the [techpub notes for the JunOS version 10.4R3](http://www.juniper.net/techpubs/en_US/junos10.4/information-products/topic-collections/release-notes/10.4/index.html?topic-51158.html), I can't find any reference to this PR.**
    What I did find was multi-facited.  Either the JTAC engineer was just incorrect and mistyped, or the site is not efficiently relaying information. 

    It's no secret that I'm hyper-critical of support engineers.  I don't call any TAC very often, if anyone in my group calls a TAC, it's an "oh sh!t" moment or we've exhausted all other resources.  We take a lot of pride, myself included, in being good at our jobs.  That being said, lets give the benefit of the doubt and make an assumption that the JTAC engineer gave us the correct PR. 

    The PR search that jtac offers is pretty awful.  It's hard to find, can't seem to find known PRs and is generally clunky and yuckie.  In their defense, most TAC KBs are not good.  However, and try doing a google search for this and you'll find links to [https://www.juniper.net/prsearch/simplesearch.jsp](https://www.juniper.net/prsearch/simplesearch.jsp), which doesn't work.  You'll also find a lot of reference to that URL when searching the JTAC KB, as noted [here](http://kb.juniper.net/InfoCenter/index?page=content&id=KB17924&actp=search&viewlocale=en_US&searchid=1352170024537) under the heading "Where can I search known Junos bugs?". 

    I'm going to make a [giant] assumption that this is *

*not **
user error on my part. ** ** This is a problem that needs fixed.  I'm into making lists lately, so here is another one:**
Things I would like to see in a TAC


- Competent first level engineers.  
- Know when to escalate, there is no shame in asking for help. 
- Engineers that have at least some *

*soft**
 skills. 
- People skills are nearly as important as tech chops, especially in a TAC
- Efficient troubleshooting process.
- This can be taught, come on guys, get to it.
- A decent knowledge base.
- Quit moving crap around or make the old links forward, this is web programming 101- Make searches work easily- Allow for multi-faceted searches
- STOP ASKING FOR INFORMATION YOU ALREADY HAVE
- We sent in the "show tech", "request support info", etc.  It's in the file.  If it's not a P1 case, read the freaking notes.  
- Make sure you follow up with the next engineer.
- We understand shifts change, please make sure hand off of cases is done correctly


These would seem like easy things to accomplish, and I have seen them in the past, but they aren't the norm.  They should be. 



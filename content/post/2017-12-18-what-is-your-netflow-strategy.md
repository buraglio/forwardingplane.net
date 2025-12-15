---
id: 1428
title: 'Strategy Series: What is your netflow strategy?'
date: '2017-12-18T05:15:30-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1428'
permalink: /2017/12/18/what-is-your-netflow-strategy/
dsq_needs_sync:
    - '1'
dsq_thread_id:
    - '6355850159'
Views:
    - '1108'
categories:
    - How-To
    - Musings
    - Security
    - 'Strategy Series'
---

You have one, right? Even if your entire strategy is “collect some flow data”, there is absolutely NO reason not to have a netflow implementation, and frankly, it will save you time and money over time if you make the effort to do it. I love network data and analytics and I have waxed poetic about how important they are at every opportunity. There are a myriad of options for analytics and flow data. If you’re not doing something, you’re doing it wrong. I can go on and on about the importance of network data for budgeting, security, capacity planing, and general knowledge of what your network is actually doing, but that’s for another day (contact me directly if you really want to chat details on that subject). Today is about network flow data - the foundational bits and pieces of what the heck your network, big or small, is actually doing. I’ve been having a breakdance fight with flow data packages for almost two decades, and I’ve jotted down a few of my more notable experiences. Regardless of your needs, budget, abilities, or time, there is a solution for you.

 *</iframe>
 
<center>
[via GIPHY](https://giphy.com/gifs/breakin-boogaloo-shrimp-11FirB7GcukiwU)</center>


## **[Arbor](https://www.arbornetworks.com/)**

Arbor is the Rolls Royce of flow analytics (and DDoS mitigation) solutions. It does almost everything, has options for managed objects, DDoS scrubbing and alerting capabilities, a magnificent interface, role based access, rainbows and gumdrop houses with lollipop trees. This system is pretty darned amazing - it truly is, and that likely comes from the fact that they were one of the first, and had/have one of the largest install bases for this kind of system. They have turnkey solutions and have the unique position of being in roughly 90% of the worlds legacy tier 1 ISPs, so their DDoS and other security options are strong, fast to update, and **<u><i>very*</u>** good. I’ve had great experience with this platform and its API. I like to think of arbor as the commercial ISP brass ring for flow data analytics. They have other solutions for enterprise and campus, but their roots are in strong ISP solutions. They’re pricey, but very, very good. Expect to need at least an FTE to really take full advantage of their very capable ecosystem, but if you dedicated the money and manpower to it, you won’t be sad.


## [Splunk](https://www.splunk.com/)

We all know spunk as a really nice log and analytic system but what many may not realize is that Splunk is really, really good at network data and analytics as well. It’s pricey, but it’s as close as you’ll get to a turkey solution for a SIEM that can actually scale. It has the notion of customizable dashboards and visualization, as a huge amount of plugins and add on’s, but they come with a legendarily steep price tag. The saying I have always heard is “if you can afford spunk, buy spunk. If you can’t use an ELK stack (noe elastic stack)”. My experience backs this up.


## [ELK /Elastic Stack](https://www.elastic.co/)

I’m a big fan of this not only because it’s essentially free, but because it’s so extremely flexible and has so many existing projects built around it. I’ve moved my go-to for net flow collection from nfdump to Elastic Stack built around the [Manito Networks flowanalyzer](https://www.manitonetworks.com/about-flow-analyzer/) install.   This platform takes a bit more command line jockeying and isn’t entirely turnkey, but it’s crazy flexible, had great eye candy and building the visualizations and dashboards is easy. Notable mention is [Elastiflow](https://github.com/robcowart/elastiflow), which is similar but has a bit more eye candy and leverages log stash. Elastiflow doesn’t have nearly as turnkey of an install (and really has almost no “newbie” install instructions at all - but it’s a strong offering if you already know how to spin up an ELK stack and tune it.


## [Nfdump](http://nfdump.sourceforge.net/)

The venerable nfdump. This is what so many large networks were using (and probably still are) for their raw flow collections. This package scales exceptionally well to huge networks and has so many tools available for the CLI that it’s the de facto standard for raw flow analytics and forensics. I love this system and ran it for many, many, MANY years. It takes a but of time to learn, and may not be the right tool for you if you want a modern GUI, lots of eye candy, or are inexperienced with the UNIX/LINIX command line, but it’s got it where it counts, supports IPFix, Netflow v5, v9 and IPFIX and you can’t dog wrong with it. I have a handy how-to getting it up and running Under CentOS [here](https://www.forwardingplane.net/2014/01/install-nfsen-and-nfdump-on-centos-6-5-for-netflow-and-or-sflow-collection/). When you couple this with something like [Justin Azoff’s flow indexer](https://github.com/JustinAzoff/flow-indexer) and [nfsen](https://sourceforge.net/projects/nfsen/) on the front end, you’ve got an enviable power user setup ripe for both forensics, tactical work as well as baseline generation.


## [SolarWinds](https://www.solarwinds.com/)

Solarwinds Orion is the go-to for windows based monitoring. It’s not cheap, but if you’re running a windows based monitoring system, you’re likely an enterprise and have budget for it. I have been impressed with the visualizations of this system and like that it does all of the monitoring in one package - once installed I never have to see windows (and since I can’t efficiently support windows, that’s probably a good thing - someone else will handle the OS work). The price tag can be a bit steep depending on number of nodes monitored, but it does what it claims and commercial support is decent. My one complaint is that I can’t seem to find a way to do raw data queries in a straightforward way. This may be possible and I have just not had the time or mental power to workout out. Overall it’s a worthy monitoring platform if you need your system to run on windows and can afford it. There are some older but still good videos from several Network Field Day events [here](http://techfieldday.com/companies/solarwinds/) and I wrote about it from a UNIX users perspective [here](https://www.forwardingplane.net/2015/07/solarwinds-orion-from-a-unix-user-point-of-view/).


## [Live Action Networks Live UX](https://www.liveaction.com/products/live-ux/)

Another commercial option that has good support and a lot of eye candy. This was born out of work with the US Government and is a really interesting system. I’ve met with these guys several times and their team is super open to taking and feature requests and they have a good product. I first heard about them at [Network Field day 7](http://techfieldday.com/appearance/liveaction-presents-at-networking-field-day-7/), their product was intriguing there and they’ve come a long way since then. Worth looking at for a turnkey solution for things like network analytics, IP-SLA,


## My take

I like the power that an indexed set of data provides and I am willing and capable of plowing through the install of a linux based system. I’m also frugal, and for a product to really warrant my money it needs to do something that nothing else does [translated: I am willing and able to support open source solutions].
![](http://www.forwardingplane.net/wp-content/uploads/2017/12/Screenshot-2017-12-15-20.32.57.png)
That said, the Manito Networks install of Elk + Kibana (no logstash in this default install) is where I typically land due to the fact that I can get indexed flow data, nice, configurable graphs and trending statistics, and can integrate things like syslog into another index on the same system giving me the tools to do forensics on a number of topics on that system. [The setup is crazy easy](https://gitlab.com/thart/flowanalyzer/blob/master/Install/README.md) and really well documented, too. Someone linux-inclined can have it up and collecting flow data (sflow, netflow v5/9 or IPFIX) in an order of about 30 minutes - probably less. The take aways really, though, is that there are options available no matter your skill level or budget, so there is really no reason not to have something.


---
id: 1707
title: 'SDN across domains in the WAN – a novice look'
date: '2012-11-27T05:04:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/'
permalink: /2012/11/27/sdn-across-domains-in-the-wan-a-novice-look/
dsq_thread_id:
    - '2154143226'
Views:
    - '86'
categories:
    - Musings
    - SDN
tags:
    - OpenFlow
    - SDN
    - WAN
---

There has been a flurry of discussion on SDN in the WAN lately, specifically, why and how.  Brent Salsbury laid out a few use cases [here](http://networkstatic.net/sdn-use-cases-for-service-providers/).  The why seems pretty straightforward.  I do believe it will happen, however, the **how **is the interesting part.  Admittedly, I'm a tad of a greenhorn in the SDN space, I've made it work in a lab, I participate as much as I can in the working groups and I attempt (poorly) to keep up.  
SDN, and likely OpenFlow, is in our roadmap at work.  Doing SDN in the data center is well documented and fairly well tested. Stanford has it all over their campus LAN and Google is pushing it around their walled garden WAN on custom built hardware.  None of this is new.  
The interesting bit is **how do you do it across multiple administrative entities**? 
As I said before, I'll never claim to be an SDN expert, so I need to break this down into simple pieces for my limited mind to comprehend.  
BGP solved this years and years ago, how is that accomplished?  Can any of these bits be re-used (why re-invent the wheel)?

My caveman mind wants to break this down into requirements:

This can likely be controlled by access between peers via an access control mechanism of some sort, i.e. place software limits on how much a given peer can provision in your network, which can be broken down into:


	- Number of circuits
	- Types of circuits (MPLS, VLAN, DWDM Waves, etc.)
	- Bandwidth per circuit
	- Duration of circuit (path TTL, permanent?)
	- Number of devices involved per circuit
	- Types of SDN (OpenFlow versions, OSCARS, etc)
	- Probably more stuff


How can this be done?  I don't currently know enough to answer that question, but I suspect it may require a little bit of work in adding a peering framework between control planes (SDN controllers) not unlike how BGP works.  To put this in familiar terminology, for example,


	- Route maps could be replaced by permissions maps or even an ACL of some sort to establish the abilities of each peer.  
	- Peers would need to agree (configuration-wise and politically) on what abilities can be exchanged before peers could operate, programmatically agree on parameters before any changes can be made.
	- Security parameters would need to be met for the peers to establish to contain the control plane traffic in a safe way, much like an MD5 across a BGP peering.


If this sounds like a tall order, I'll wager you're right and I'll also bet that before it happens we'll have a Blu Ray vs HD-DCD or VHS vs Beta throw down of SDN protocols.  
Folks have been trying to do this for years, the [DRAGON project](http://dragon.maxgigapop.net/twiki/bin/view/DRAGON/WebHome) tried this years ago and did a decent job.  Our Arlington, VA site was one of the original build outs of it. [OSCARS](https://oscars.es.net/OSCARS/docs/) is doing similar stuff and is actively working across [ESnet](http://www.es.net/). [Internet2 ION](http://www.internet2.edu/ion/) is another attempt.
These have all had their effect on the Research and Education networks, but to be adopted acrossm and more importantly between, service provider networks, there needs to be ways to do them elegantly and securely.  There is nothing that a SP hates more than risk, and without these control mechanisms, there is a pretty large amount of risk. 
It's reasonable to think that this may be there and I'm just missing it, since I am admittedly a novice in the SDN world, but if by chance I have not missed it because it's not there, it needs to be addressed.  



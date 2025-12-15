---
id: 1365
title: 'Why I care about Segment Routing'
date: '2016-10-03T18:54:27-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1365'
permalink: /2016/10/03/care-segment-routing/
dsq_thread_id:
    - '5194255270'
Views:
    - '612'
categories:
    - Routing
    - SDN
---

Edit: *Going against my normal “just get the content out there” methodology, I’ve been mulling over this blog post since July of 2016.  Segment routing is such a beautifully elegant solution I have had trouble articulating that fact. WAN technologies are squarely within my wheelhouse, and this one fits in so well I was going over and over the post never really satisfied with it, continuing to find mistakes and decided to just get it out there. *
**
As a WAN guy by chance and opportunity, and a service provider engineer and architect by choice (and also chance and opportunity), segment routing (SR) is one of those wonderful new technologies that keeps rearing its head over and over in recent days - and it's already playing in the big leagues. SR is supported by many of the large network equipment providers including Cisco, Juniper, and Nokia (Alcatel-Lucent), and as I have just learned, Arista.

Why is this a notable tech you may want to pay attention to? Wide area and service provider networks have a longer mean time before replacement. They don’t change topology or architecture nearly as often and the gear typically has higher cost due to things like deeper interface buffers, more complex feature sets, larger TCAM for things like route tables, as well as increased redundancy features. Managing a WAN has a different feel and a different set of problems. Complex overlays and traffic engineering often play a role in wide area networks. Many an attempt to reduce the the complexity of WANs has been made and SDN is creeping its way into some pretty large networks. When a network of any size is built, there comes a tipping point when managing things by hand, even with great documentation, is too daunting and cannot be done efficiently. Automation is key. Simplicity is paramount. Anyone that has ever managed a large MPLS network knows this. So, when I started looking at segment routing, I was cautiously optimistic - it had many attributes that were comfortable to a seasoned WAN engineer and yet abstracted many of the complexities of the networks that we'd been running for years. In order to really understand the benefits that SR brings to the table, it's important to understand the current landscape. When one builds a large MPLS network there are incremental elements that all build from each other in order to work. If one is broken or problematic, the problem will trickle up the stack. Fundamentally, the stack for a very vanilla MPLs WAN contains the following elements (top down):


 	- Client service interface
 	- Overlay, L3VPN, VPLS, ePIPE/PseudoWire/VLL
 	- BGP
 	- Label Distribution, LDP, etc.
 	- IGP, IS-IS or OSPFv2/3
 	- Ethernet, SONET, DS1/DS3/E1
 	- Optical transport or other last mile and long haul outside plant


Add into this list the complications of traffic engineering, and you've got a mix of things that are fairly daunting to all but the most experienced engineers. What segment routing provides is a way to remove several layers of this and simplify what is arguably the most complex and least understood element: Traffic Engineering. Segment routing allows for the selection of an entire path, from the ingress of the network to the egress port, all outside of the IGPs shortest path table. It is often labeled as "source routing" which will inevitably create feeling of disgust, dread, and distain from a network engineer and panic from the security folks. I choose not to label SR as "source routing" because of the negative connotation associated with that technological approach. Instead, I would rather use the term "deliberate path selection".
Oh, and this can be automated. That's right. It's "SDN". Utilizing a tool called a path computational engine or "PCE", these paths can be selected based on any number of criteria including latency, hop count, load, time of day, phase of the moon, mood of the boss, etc.

I was lucky enough to get to spend some quality time at a [special event](http://techfieldday.com/event/srr1/) recently. Interesting discussions were had, many a thing was learned. A few of the other attendees wrote up some great info on segment routing, including some use cases, which can be found here


Terry Slattery on No Jitter
[http://www.nojitter.com/post/240171828/segment-routing-inside-a-new-sdn-technology](http://www.nojitter.com/post/240171828/segment-routing-inside-a-new-sdn-technology)

Carl Niger on Come Route With Me
[https://comeroutewithme.com/2016/07/24/post-tfd-segment-routing-roundtable-thoughts/](https://comeroutewithme.com/2016/07/24/post-tfd-segment-routing-roundtable-thoughts/)

Russ White on Net Work
[http://ntwrk.guru/dc-fabric-segment-routing-use-case-1/](http://ntwrk.guru/dc-fabric-segment-routing-use-case-1/)

[http://ntwrk.guru/dc-fabric-segment-routing-use-case-2/](http://ntwrk.guru/dc-fabric-segment-routing-use-case-2/)

I highly recommend taking a view of the talks from some folks using SR on some pretty significant networks - it's worth your time if you're really interested in throwing down with segment routing.  But what did this tell *

**me**
*? Lets look further into SR and see why it's become so attractive to large, geographically diverse networks. First, SR builds on an existing knowledgeable. Far more people exist in the market that already know MPLS. The understand labels, they understand overlays, and they have vast experience with virtual circuits. Service providers are very likely MPLS based if they operate at any scale and offer typical ISP services. MPLS is well traveled, and even though there may be reasons that's not perfect, it's the devil we know. Other SDN technologies are either fairly green (l[et me tell you about running a production openflow experience](http://blog.ipspace.net/2015/12/running-open-daylight-in-production.html#more)) or are primarily focused on the data center, which as I will adamantly insist is a very different beast.

Large scale service providers have a very different redundancy model. Attempting to apply campus or enterprise redundancy to a service provider does not scale and it certainly isn't affordable. SR leverages the same models that MPLS does, it realies heavily on the IGP, leveraging a TLV within IS-IS. That brings me to IS-IS. Most service providers leverage IS-IS as their internal gateway protocol due to it's ability to carry multiple routed protocols at once, leverage multi-topology, and the fact that it does not rely on the protocol it is routing for connectivity like OSPF does. SR is more-or-less an extension to IS-IS. Overlapping skill set #2. The other option, and this is a big one, is that there are multiple vendors that supported, as stated above. This is a big deal as int provides that "throat to choke" that a lot of emerging technologies just do not really have yet.
Did I mention that it "fails open”? What’s not to love about falling back to an IGP rather than ceasing to process packets?  Lets do a for-instance use-case. Within your SR network you provision a path that takes a path with more hops but has less congestion. Create your label stack and away you go* Of that path fails, the traffic falls back to the standard routing table.
Much like MPLS (of which I am a fan, FWIW), this technology is better suited for a larger network with multiple paths, this could be any number of  environments such as large camps networks, large scale data centers geographically diverse environments connected by multiple WAN circuits, and of course, service and content providers. This tech is quite simply full of win. 

*greatly simplified =)



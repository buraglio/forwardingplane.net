---
title: 'Black Hole routing'
date: Tue, 04 Oct 2011 01:00:00 +0000
draft: false
tags: [Routing, Security, UNIX]
---

It's no secret or ground breaking area to do black hole routing.  

ISPs and NSPs have been doing it forever to allow for a very low cost, very scriptable and very effective way to wholesale block a layer3 address. However, it can seem like a bit of a black box to anyone who has never done it.  

I recently did some work spinning this up in a good sized network that it didn't currently exist, and remembered how monumentally useful (and simple) it actually is.

There are lots of ways to do this. There are a lot of different [articles](http://packetlife.net/blog/2009/jul/6/remotely-triggered-black-hole-rtbh-routing/) written about how to do it. Cisco includes it in their CCIE Security track.

The idea is a pretty simple one. Run [uRPF](http://en.wikipedia.org/wiki/Reverse_path_forwarding#Unicast_RPF_.28uRPF.29) on your eBGP speakers. Create a peering with a router on the inside. For my purposes I used a private ASN and peered it with eBGP to my border devices. Create a static route to null0 on the BHR (Black Hole Router), which then sends the route (possibly tagged with a community) to the eBGP speakers. They see an internal route for this external host, so any packets that come from that host on the outside get dropped on the floor by uRPF. In theory it's all handled in hardware so the overhead is minimal and the blocks are as fast as a BGP route advertisement/withdrawal.

  

There are, of course, lots of caveats to this, like, what if you are taking default on your eBGP speakers? How is that handled. One of the places I recently set this up takes default, one takes full tables. I suggest reading [this page](http://www.cisco.com/web/about/security/intelligence/unicast-rpf.html) if you aren't experienced with uRPF, it explains how cissco handles it and is a decent primer on uRPF in general.

  

I'm a simple guy and I like things to be easy to support, so my designs tend to be those that can easily be maintained by someone that !=me and not so overly complicated that they can be reverse engineered in case of emergency or replicated if need be.

That said, I've chosen to do it in a pocketbook friendly way. It probably stems from cutting my teeth at a decent sized mom and pop ISP that had a very small operating budget so we did things in creative and cost savings ways while still keeping them simple and supportable. I'm not sure why, but it makes more sense to me to run a software router like [Quagga](http://www.blogger.com/www.quagga.net) or [OpenBGPd](http://www.openbgpd.org/) that I can run as a VM and connect to my IGP and EGP, scripting the adds and removal of the routes we want to blackhole. It can also be done with an actual router, but I personally prefer to drop it in as a software router.

  

The use of a linux box allows for a bunch of neat options. You can use the iproute2 package to watch changes to the routing table, you can run it in a virtual machine, it can be done in a very economical way, etc.

Using Quagga has its pros and its cons. Quagga is a great platform, but it is an open source project. Their ISISd support is a bit lacking, so if your IGP is ISIS, it will work, but it feels half baked to me (and there is zero documentation that I could find). The ospf\[v2 and v3\] versions work fine. BGPd works well enough. It can be put into RANCID for configuration management and it is easily scriptable using vtysh and its IOS-like interface.

  

Here is a basic design for a black hole router running inside a network with an external peering with something like a bogon route server:

  

[![](http://4.bp.blogspot.com/-5lZmt2zsQ3Y/T3oMBMHyysI/AAAAAAABIS4/T5lzIgb0I2I/s320/BHR+Example.jpg)](http://4.bp.blogspot.com/-5lZmt2zsQ3Y/T3oMBMHyysI/AAAAAAABIS4/T5lzIgb0I2I/s1600/BHR+Example.jpg)

  

  

This just shows a basic setup, one site border router and a black hole box. In this example, the BHR is also peered with an external "service" like a bogon route server. This is a value-add, and not required.

Any traffic that comes in can be routed to null0 on the bhr. This, in turn, sends a routes to the SBR. The SBR then installs it as an internal route. Now, any traffic that comes in from this route outside will looked like spoofed traffic and uRPF will discard it.

Very simple, very effective.

  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
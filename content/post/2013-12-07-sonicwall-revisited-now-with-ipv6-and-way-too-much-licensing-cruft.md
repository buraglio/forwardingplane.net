---
id: 835
title: 'Sonicwall revisited – Now with IPv6 – and way too much licensing cruft.'
date: '2013-12-07T09:45:06-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=835'
permalink: /2013/12/07/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/
themeblvd_title:
    - 'Dell Sonicwall revisited 1 year later - Now with IPv6 - and way too much licensing cruft.'
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'SonicWall, SonicOS, IPv6, Netflow, Nick Buraglio, forwardingplane, firewalls, security'
themeblvd_description:
    - 'A quick revisit of the Sonicwall firewall platform and it''s IPv6 and visualization support. '
dsq_thread_id:
    - '2157152346'
Views:
    - '144'
categories:
    - IPv6
    - Security
    - 'Soap Box'
---

About a year ago <a title="Sonicwall – Old dog learns [some] new tricks" href="http://www.forwardingplane.net/2012/12/sonicwall-old-dog-learns-some-new-tricks/">I did a brief review of the "new Sonicwall"</a>, specifically a smaller branch office device that was said should have had all of the features of the larger devices.  I proposed that it had some significant limitations (much to the disagreement of a great deal of folks).  However, I stand by my statements.  If you ignore the fact that firewalls often cause more problems than they solve, that NAT is a nightmarish kludge (and not a security mechanism), and<a title="Why hardware firewalls are the walking dead" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/"> will likely be phased out for better options eventually</a>, the SonicOS I tested was pretty limited as far as what I believe should be features.
Let's be clear, I'm mostly talking about IPv6.  I've ranted and raved that anyone not doing IPv6 is already years behind.  Get on the ball, you're already late to the game.  Yesterday, a colleague said something that resonated with me regarding this and it got me thinking about how much IPv6 support SonicOS had added.  Many folks that aren't doing IPv6 think that instead of doing something that may be a little hard that they're just not going to do anything.   They're dead wrong.  They're forcing themselves to do something else like CGN or multi-layer NAT, or something else equally (or more) unpleasant.  And then they'll do IPv6 anyway after that. It **is** inevitable.
But I digress….
I pulled my old TZ-210 out and upgraded it to SonicOS Enhanced 5.9.0.2-107o.  What a pleasant surprise!  A **huge** amount of IPv6 support added!  [![](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4.png)](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4.png)
They've really done their homework here.  I was very surprised to see things like DHCPv6-PD with interface tracking.  Well done, Dell.  This will allow for small and home offices to take advantage of the Comcast and AT&T DHCPv6-PD that they've been offering for a while now, and lets be honest, once it's on, most folks will never even realize they're using IPv6.
[![](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6-257x300.png)](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6.png)
<== This is a giant step forward for reasons that are far beyond simple protocol support.
 
![](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-fw-rules.png)
 
I'm very happy to see this level of support from Dell/Sonicwall.  I expected to put this box in, turn it on, use it for a few days and turn it off.  I set it up in transparent mode, tuned the rules a bit….and I have no real plans of taking it out.  I'm actually pretty happy with it for the application I'm using it for.  It doesn't seem to really impede anything I want to do (after TCP ssh timeout rules to a reasonable time; BTW, timeouts are one of the reasons I don't like firewalls).
 
 
This brings me to my problem with Sonicwall (and many network and network security vendors).  My licenses have all expired.
I can understand having to license services that cost money because they're licensed upstream services.  I get that, I really do.  However,  Some of the things that Dell requires licenses for seem a bit extreme to me.  The fact that I get essentially zero visualization options once the licenses expire is downright shameful.  No worries, I'll just export Netflow/IPFIX data.  Nope, also a licensed feature.  You heard that right.  No flow export, no real time monitor.  Heck, I can't even look at interface graphs on-box. I have to poll with a 3rd party tool suite.  Realistically, one gets significantly better instrumentation from a default [pfSense](http://www.pfsense.org) load.  And pfSense has had IPv6 support for years.
If you take away all of the downright shameful licensing requirements to do anything useful with trending and instrumentation, this is a good platform. Their IPv6 support is solid now.   However, for anyone running  networks  that require instrumentation and visualization, you had better budget for [unnecessary] fees or have 3rd party mechanisms for collecting the data.
 
 
 
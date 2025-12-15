---
id: 1051
title: "Why you don't need a firewall [how to secure an open perimeter network"
date: '2014-09-08T01:30:07-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1051'
permalink: /2014/09/08/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/
themeblvd_title:
    - 'Your firewall is a fuse and you don''t need it. '
themeblvd_keywords:
    - 'security, openflow, science DMZ, routing, black hole routing, ipv6, buraglio, nick buraglio, infosec, open perimeter network'
themeblvd_description:
    - 'There are use cases for having a network with no security appliances in the path. Here is how to secure it in a way that is functionally equivalent. '
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '2998064043'
Views:
    - '169'
categories:
    - IPv6
    - Routing
    - SDN
    - Security
    - 'Soap Box'
---

I admit that the title was meant to be inflammatory.  However, there are use cases that aren't terribly uncommon where an in-line security appliance is just not the correct tool for the job.  Someone once told me "a firewall protects a network like a fuse protects an electrical circuit", and it's mostly a correct statement.
Firewall vendors will probably argue this and enterprise folks may discount this as heresy and call for burning me at the stake.  I can say, though, that the use of a firewall, IPS or other inline security appliance has presented many problems in many environments in my years as a network and security engineer and architect.    To that end, there are mechanisms for replacing the functions of a firewall and IPS with other options, which in many cases have a lower capital expense [although they may have a higher *initial* operational expense].  I'll outline them here, but before I do I want to re-iterate that NAT (PAT) is not a security tool, it's a translation tool.  Nothing more.  So, I will leave that out.  If you don't have appropriate IPv4 or IPv6 address space some of these things may need adjustments although they are still accomplishable by doing NAT on a border Layer 3 device.     Below is a talk that I gave at BroCon14 that is a rough outline of how to do this, if you don't want to spend 30 minutes listening to me talk about it, the clifs notes are bulleted below, but the context is all in the video so I encourage you to watch it before responding to my post.
For those that want to take a look, here is the talk.
<iframe src="//www.youtube.com/embed/IPh3aZ18IuY" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
Here are the bullets.


	- **Announce only necessary resources **


One can utilize routing to only expose the pieces of the network that need to be exposed.  If you have a /16 and on;y a /24 needs to be exposed, only announce that prefix.  This is not that different than a typical DMZ.


	- **Filter access to network, storage and management hardware**


Utilize best practice ingress filtering.  Follow [BCP38](http://tools.ietf.org/html/bcp38). You should be doing this anyway.


	- **Utilize host based firewalls**


This is a no-brainer.  Firewall as close to the resource as possible.


	- **Employ central host management**


Make your life easy.  Cloud providers do it and it's well documented nowadays.  There are [many](http://cfengine.com/) [options](http://puppetlabs.com/).


	- **Centralize logging and flow data collection**


Another no brainer, you should be doing this anyway.


	- **Create baselines for traffic and activity**


Data is good.  Knowledge is power.  Baselines are useful for both anomaly detection and forecasting and it's not that hard to do it.


	- **Deploy and tune IDS**


Passive IDS system[s] off of a TAP or SPAN are key to this kind of architecture.  See video for more details but there are a bunch of good options. I prefer [Bro IDS](http://www.bro.org) but there are many players both commercial and FOSS.


	- **Filter with black hole routing**


I've<a title="Black Hole routing" href="http://www.forwardingplane.net/2011/10/black-hole-routing/" target="_blank" rel="noopener noreferrer"> talked about this before</a>.  Automating this is key to making it function efficiently and it is a fantastic tool.  This can be done with BGP (traditionally) or with something innovative like OpenFlow.


	- **Make use of regularly scheduled external vulnerability scanning**


This is a great way to verify your exposure and works for any sized network.  Highly recommended.

 
Clearly this isn't for everyone, and that's ok.  For anyone that has struggled with issues involving security appliances either based on protocol, horsepower or interface speeds, there are options.
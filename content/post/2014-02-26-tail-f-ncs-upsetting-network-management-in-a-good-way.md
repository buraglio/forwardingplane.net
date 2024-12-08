---
id: 908
title: 'Tail-F NCS: upsetting network management&#8230;in a good way.'
date: '2014-02-26T22:36:26-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=908'
permalink: /2014/02/26/tail-f-ncs-upsetting-network-management-in-a-good-way/
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'Tail-F NCS can change the way existing and future networks are managed'
themeblvd_keywords:
    - 'tail-f, NCS, juniper, openstack neutron, cisco, ios, junos, openflow, mpls, nfd7, network field day 7, network managment, unix, snmp, yang, netconf, SDN, network rosetta stone, #NFD7'
themeblvd_description:
    - 'Utilize tail-f to manage and automate large scale networks when people needs to me removed from the management path'
dsq_thread_id:
    - '2328178640'
Views:
    - '162'
categories:
    - 'Data Center'
    - Routing
    - SDN
---

<em>“Hopefully there are some things here that will make you really upset in a very good way”</em> is how <a href="https://twitter.com/cmoberg" target="_blank" rel="noopener noreferrer">Carl Moberg</a> of Swedish based company <a href="http://www.tail-f.com/" target="_blank" rel="noopener noreferrer">tail-f</a> opened up to the crowd at <a href="http://techfieldday.com/event/nfd7/" target="_blank" rel="noopener noreferrer">Networking Field Day 7</a> on<a href="http://techfieldday.com/appearance/tail-f-systems-presents-at-networking-field-day-7/" target="_blank" rel="noopener noreferrer"> Feb 19, 2014</a>.  Tail-f is a sleeper, I had actually never heard of them before NFD7, but they've got a very unique product in <a href="http://www.tail-f.com/network-control-system/" target="_blank" rel="noopener noreferrer">NCS</a> and in my opinion it can change the way existing <strong>and</strong> future networks are managed.  Right now.  It's not a platform that is green, unpolished or unfinished.  <a href="http://www.tail-f.com/network-control-system/" target="_blank" rel="noopener noreferrer">NCS</a> is in the ring and it brought its A-game.   Their site describes it better than I ever could:
<em>"Tail-f Network Control System, or NCS, enables network operators to manage all of their services and network devices with a single tool." </em>A bold statement, and I tend to be pretty skeptical of such statements. However, I was really intrigued by the NCS platform and as I discovered, it is not hype. Watching the demo of this got my brain racing, it was exciting to think about all of the things it could simplify; I was excited about networking.  So many things In fact, I'm really just going to scratch the surface of what this software toolkit can tool.
<blockquote>
<h2><em>"Any network of of ambitious size that needs to get people out of the loop”</em></h2>
</blockquote>
The CTO says that NCS is for "<em>Any network of of ambitious size that needs to get people out of the loop</em>”, and I tend to agree, which is what makes this so powerful. In a world of openflow this and sdn that, most of which is still under heavy development, I can't help but think of NCS as a "rosetta stone" of network management tools. It’s a controller, but in a different way. Its not openflow, but it knows openflow, so it is looking forward, but it also supports everything that is already there, an absolute necessity for 95% of networks that are not greenfield. From the<a href="http://www.tail-f.com/network-control-system/#which-types-of" target="_blank" rel="noopener noreferrer"> NCS FAQ</a>:
<blockquote>
<h2><em><a href="http://www.forwardingplane.net/wp-content/uploads/2014/02/rose_lg.jpg"><img class="alignleft size-full wp-image-920" alt="rose_lg" src="http://www.forwardingplane.net/wp-content/uploads/2014/02/rose_lg.jpg" width="237" height="300" /></a>"Any device that can be remotely configured can be managed by NCS. This includes, routers, switches, load-balancers, firewalls, web servers and a whole host of other devices (both virtual and physical). Since it is not limited to one type of device or particular vendor, NCS allows for management of the entire network from a single pane of glass."</em></h2>
</blockquote>
Lets face it, network management is not exactly easy to do in a sane and robust way, there are always quirks, one-offs and proprietary goo. That's probably never going to change.  From the open source to the commercial, I've used, evaluated or extended a wide swath of them in my time in the industry, and this one really shocked me in what it was able to do in such a demonstrably elegant way, which we all know is not an easy task since we all have odd, uncommon or sometimes unreasonable requirements.
A few things are really compelling about NCS.  First, it's all <a href="http://en.wikipedia.org/wiki/YANG" target="_blank" rel="noopener noreferrer">YANG</a>, meaning it is an established standard for doing exactly this and it can be referenced by any number of protocols for obtaining or setting the desired data or parameters.  This also means that it can very quickly and easily be extended to support new products, software loads, communications mechanisms and features.
Tail-F changed the way I was thinking about network management.  They've taken the religion out of equipment vendors, because you can choose how to interact with them.  They allow for management of a myriad of platforms from an operator-chosen, familiar CLI.  Have guys that like JunOS?  Great, no problem.  Team members that prefer IOS?  No worries.  They can manage the Alcatel-Lucent, Brocade, Extreme Networks or one of the many other CLI variants from their choice of IOS or JunOS-like command sets.   No longer is it important to understand a particular CLI.  I wish I could have had access to this product 5 years ago when, at a previous job, we introduced JunOS to a team that had been working on IOS and Foundry for the majority of their careers.  It would have solved so many issues and driven the learning curve to nil.
The CLI translator is really just the icing.  The configuration validation is immensely powerful and I could easily see it preventing many typos and misconfigurations (you know you've done it, we all have).  It can also provide compliance reporting, service management and configuration reconciliation, all of which are generally in-house written tools or manually accmplished tasks in my experience.
Standardize and deploy ACLs across a range of platforms in geographically diverse areas, provision BGP policy on huge numbers of peers very quickly, reconcile MTUs on interfaces of devices that have been neglected, <a href="https://wiki.openstack.org/wiki/Neutron/ML2/Tail-f-NCS-neutron-ml2-driver" target="_blank" rel="noopener noreferrer">interface with OpenStack Neutron</a>.  The use cases are pretty open ended, really. Anything that needs to be done at scale can be, and it can be error checked in the process.
Don't take my word for it, I'm clearly excited about it and can't wait to get my hands on it.  Watch the NCS demo:
<span style="line-height: 1.5em;">Tail-f Systems NCS Demo at Networking Field Day 7</span>
<iframe src="//player.vimeo.com/video/87189864" height="281" width="500" allowfullscreen=""></iframe>
&nbsp;
All of the videos can be found <a href="http://techfieldday.com/appearance/tail-f-systems-presents-at-networking-field-day-7/" target="_blank" rel="noopener noreferrer">here</a>.
Rosetta Stone images courtesy of <a href="http://www.ancientegypt.co.uk/writing/rosetta.html" target="_blank" rel="noopener noreferrer">http://www.ancientegypt.co.uk/writing/rosetta.html</a> and <a href="http://taboodada.wordpress.com/" target="_blank" rel="noopener noreferrer">http://taboodada.wordpress.com/</a>
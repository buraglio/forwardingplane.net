---
id: 1030
title: 'Crystal Ball: Cisco buying tail-f.  What does it mean?'
date: '2014-06-23T10:24:44-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1030'
permalink: /2014/06/23/crystal-ball-cisco-buying-tail-f-what-does-it-mean/
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '2789174249'
Views:
    - '120'
categories:
    - 'Crystal Ball'
    - Musings
    - SDN
    - 'Soap Box'
---

With the recent <a href="http://www.tail-f.com/cisco-announces-intent-acquire-tail-f-acquisition-advances-ciscos-cloud-virtualization-portfolio-industry-leading-network-service-orchestration-technology/" target="_blank" rel="noopener noreferrer">announcement of Cisco Systems intent to purchase tail-f</a>, proponents of a multi-vendor environment are waiting with baited breath to see how the networking giant will deal with support of competitor hardware and CLIs.
Yang is here to stay, there is no doubt about that.  As is netconf.  Both of these are good things for the industry as a whole, having a standard way to communicate with network hardware [<a href="http://searchsdn.techtarget.com/opinion/OpenFlow-as-a-network-control-protocol-goes-deeper-than-data-center" target="_blank" rel="noopener noreferrer">that isn't openflow</a>] is necessary and immeasurably useful.
I'm not going to go into the politics, the internal technical bits or even the details of who stays and who goes.  Smarter folks than me have <a href="http://lamejournal.com/2014/06/18/thoughts-cisco-acquiring-tail-f-systems/#more-2999" target="_blank" rel="noopener noreferrer">already done that</a>. Instead, I want to think about what this means for operators, architects and engineers when looking for a management platform.  I wrote <a href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/" title="Tail-F NCS: upsetting network management…in a good way." target="_blank" rel="noopener noreferrer">before about how Tail-f was a Rosetta Stone</a> for networking equipment. With the Cisco acquisition looming, this potentially and very likely changes this and there now exists a gaping hole in this type of management system.
So, what does that mean?
If I had to guess, I'd say that even though Cisco has been a bit more friendly in the opensource world, it makes absolutely no sense for them to support a platform that allows for the use of any network platform. Perhaps I'm being cynical, but I doubt it.
What this does is leave the majority of us looking for a cross vendor management solution, where the tail--f NCS lives, out in the cold.
However, there is a silver lining. The cup is half full in the forwarding plane today. My hopes is that the lack of a real commercial product that does what NCS does, and the awareness raised that such a product existed in the first place will kick start the FOSS world into building something.  Only since RANCID have I seen a really viable option for cross platform management [and in the case of RANCID management=change and configuration tracking].
This also opens the door for an existing management protocol ::cough:: openflow ::cough:: to emerge as a really viable management and control protocol and mechanism.  
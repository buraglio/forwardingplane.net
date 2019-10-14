---
title: 'Why I care about Segment Routing'
date: Tue, 04 Oct 2016 00:54:27 +0000
draft: false
tags: [Routing, SDN]
---


#### 
[Worth Reading: Why I care about Segment Routing - &#039;net work](http://ntwrk.guru/worth-reading-care-segment-routing/ "") - <time datetime="2016-10-12 13:12:18">Oct 3, 2016</time>

\[…\] As a WAN guy by chance and opportunity, and a service provider engineer and architect by choice (and… \[…\]
<hr />
#### 
[Mike Fratto]( "mfratto@techweb.com") - <time datetime="2016-10-06 07:16:00">Oct 4, 2016</time>

Hi Nick, I'm not a WAN routing guy so this may be a ridiculous question but I'm curious how you would compare/contrast segment routing with shortest path bridging. From the little I know, the goals seem awfully similar.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2016-10-06 15:24:00">Oct 4, 2016</time>

At face value they are very close. So much so, that I was literally doing a direct comparison over the last month or so for some other projects. The biggest differences I see between them is scale out and incumbent knowledge. I struggled to find someone doing SPB in the WAN (they exist, but there don't seem to be many). SR leverages a common skill set: ISIS and Labels, both of which are very common in the SP world. It builds on that while at the same time simplifying it. Scaling out ISIDs and bridge paths is great, and I definitely see a use case, but realistically speaking, the support is lackluster across the vendor space whereas SR has pretty robust support from the likes of Cisco, Juniper, Arista, Alcatel-Lucent (Nokia), etc. SPB also really touts multicast support and segmentation as a big part of its core competency, which I don't care about so much anymore. There are also the odd governing body intricacies that have some part in this as well, but that's more political than I really want to pay attention to. At the end of the day my gut says SPB has more of a place in the campus or data center and SR has its feet firmly planted in service providers with a hand in large campuses.
<hr />

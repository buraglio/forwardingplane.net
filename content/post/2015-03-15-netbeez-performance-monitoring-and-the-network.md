---
id: 1167
title: 'NetBeez, performance monitoring and the network.'
date: '2015-03-15T23:13:46-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1167'
permalink: /2015/03/15/netbeez-performance-monitoring-and-the-network/
dsq_thread_id:
    - '3627222079'
themeblvd_title:
    - 'NetBeez, a tool for performance monitoring and baselining your network.'
themeblvd_keywords:
    - 'NetBeez, NFD9, Network Field Day 9, Nick Buraglio, Best network monitoring tools, network monitoring, iperf, perfsonar, ripe ncc, openflow, ipv6'
themeblvd_description:
    - 'NetBeez is a distributed, cloud based tool for performance monitoring and baselining your network.'
themeblvd_noindex:
    - 'true'
Views:
    - '120'
categories:
    - Musings
---

At <a href="http://techfieldday.com/event/nfd9/" target="_blank" rel="noopener noreferrer">Networking Field day 9</a> there was a great deal of discussion regarding monitoring, modeling, and maintaining networks, as would be expected at an event with such a focus. Luckily for us, an interesting product that comes from a company that I was unfamiliar with called <a href="http://netbeez.net/" target="_blank" rel="noopener noreferrer">NetBeez</a> gave an inspired presentation. Now, NetBeez got my attention for a few reasons. First off, NetBeez is doing some really great things in the field of network monitoring. What would that be, you ask? What is hard about network monitoring? Nothing, I reply. It's just hard to do it right. What they are providing is a number of things, but the most useful, at least for me, is the way their products can provide a perspective from that of a typical user. In doing that, they have brought something power to the table.
NetBeez has brought a product model that has existed for some time in a bit of a different form in scientific networking and they've made it enterprise ready. For those that are not aware of it, the <a href="http://www.perfsonar.net/" target="_blank" rel="noopener noreferrer">perfsonar</a> project has been providing latency and throughput testing and baseline creation for quite some time and <a href="https://atlas.ripe.net/" target="_blank" rel="noopener noreferrer">RIPE ATLAS</a> has been making available a small probe device that does similar network testing. The difference is that neither are really focused on enterprise. NetBeez saw a need and filled it.
With the many options that are available, NetBeez has a test for many of the critical needs of a given network, and in recent releases, they've offered up a wireless probe which only widens their portfolio. Much like its community platform analogs, the RIPE ATLAS, there are several custom tests available. Unlike the NCC, the devices are yours to configure, i.e. not open by default to test against and self contained within a given administrative environment if necessary, with an on-site dashboard service also available. Custom tests include DNS queries, http, traceroute, ping and iperf. In addition to having a powerful set of test tools in a very easy to use web interface that tracks the statistics over time, providing a nice baseline tool in addition to the obvious troubleshooting tools present.
<a href="http://www.forwardingplane.net/wp-content/uploads/2015/03/Screenshot-2015-03-15-23.32.55.png"><img class="alignright wp-image-1169" src="http://www.forwardingplane.net/wp-content/uploads/2015/03/Screenshot-2015-03-15-23.32.55.png" alt="Screenshot 2015-03-15 23.32.55" width="541" height="452" /></a>
My quick thoughts: a lack of IPv6 and detailed one and two-way latency test tools leave it outside of what I would personally need, however, NetBeez has IPv6 on their roadmap and they are very open to feature requests. A refreshing artifact that I got from them during our conversations is that they have a target and mean to meet it. They are not attempting to be everything to everyone, but instead are offering very easy to configure, long term monitoring and baseline creation of complicated and distributed enterprise networks. Something useful and necessary.
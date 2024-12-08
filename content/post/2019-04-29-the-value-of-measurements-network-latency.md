---
id: 1664
title: 'The value of measurements: Network Latency'
date: '2019-04-29T04:23:32-05:00'
author: buraglio
excerpt: 'Smokeping, or “why do I need to track latency?”'
layout: post
guid: 'https://www.forwardingplane.net/?p=1664'
permalink: /2019/04/29/the-value-of-measurements-network-latency/
Views:
    - '551'
categories:
    - How-To
    - NIX4NetEng
    - UNIX
tags:
    - nix4neteng
---

There is no shortage of network telemetry data that can be collected, recorded, graphed, and stored for cross reference and triage. Not one to be underestimated, latency at a can be incredibly powerful when leveraged for baseline and deviation notification. As I have <a href="https://www.forwardingplane.net/2018/02/strategy-series-view-outside-network/">eluded to in the past,</a> there are many tools in this space.<a href="https://netbeez.net/blog/how-to-leverage-latency-testing-and-long-term-trend-collection/"> I have written about a few of them in detail</a> and touched on others in passing. Regardless of the tool, the data is powerful and the instrumentation they provide will only serve to make your network more robust and easier to work on. One tool that is particularly easy to set up and utilize is <a href="https://oss.oetiker.ch/smokeping/">smokeping</a>. From the authors site:
<em> SmokePing keeps track of your network latency:</em>
<ul>
 	<li><em>Best of breed latency visualisation.</em></li>
 	<li><em>Interactive graph explorer.</em></li>
 	<li><em>Wide range of latency measurement plugins.</em></li>
 	<li><em>Master/Slave System for distributed measurement.</em></li>
 	<li><em>Highly configurable alerting system.</em></li>
 	<li><em>Live Latency Charts with the most 'interesting' graphs.</em></li>
 	<li><em>Free and OpenSource Software written in Perl written by Tobi Oetiker, the creator of MRTG and RRDtool </em></li>
</ul>
<img title="download_Comcast_Chicago_last_864000.png" src="https://www.forwardingplane.net/wp-content/uploads/2019/04/download_Comcast_Chicago_last_864000.png" alt="Download Comcast Chicago last 864000" width="599" height="271" border="0" />
<em>Comcast SpeedTest.net graph for home network</em>
Now, you may be asking <em>“why do I need to track latency?</em>”, well, the data is incredibly powerful and can be indicators of anything from a failing optic to a network compromise. This is especially useful in small to medium sized ISPs (and especially WISPs), where cost of software and operational overhead is at a premium, and customer satisfaction is the currency that is dealt. In fact, I was able to use smokeqping to help diagnose a functional denial of service of a commonly deployed cable CPE as detailed <a href="https://forums.businesshelp.comcast.com/t5/IPV6/Reproducible-denial-of-service-of-Netgear-CPE-running-native/m-p/31597#M787">here</a>. <strong>I can’t emphasize enough how useful long term trend data is.</strong> Smokeping can be used to monitor more than just ping RTT, it supports a myriad of plugins allowing for application latency of protocols such as DNS queries, http get, ssh daemon response, speed test results, the list of plugins - or as smokeping calls them, probes - goes on and can be found <a href="https://oss.oetiker.ch/smokeping/probe/index.en.html">here</a>.
Where this is particularly useful is in simulating customer experience.  As with most things in life, perspective is paramount. To address this, smokeping can also be deployed as a distributed model. Deploying it with installations more local to a customer or in a far flung site, say on a raspberry pi, located in remote POP sides or pedestal locations will provide a closer perspective to what the customer actually sees. In the past I have deployed remote raspberry pi devices in an actual FTTH pedestal connected to an ONT to provide the exact customer point of view and it provided a wealth of information I would not otherwise be able to see.
There are a myriad of different instal guides for Smokeping, my recommended starting point is by <a href="https://github.com/magicdude4eva">Gerd Naschenweng</a> and can be found <a href="https://github.com/magicdude4eva/docker-smokeping">here</a>. It provides a docker instance but also has a very good set of configuration files to build examples from.
Don’t discount latency data - it’s a powerful set of information for any working network. For anyone interested in seeing a working smokeping installation, mine is public and available to view. It provides a few things such as DNS latency, RTT for v4 and v6, RTT for ZeroTier hosts and RIPE ATLAS probes, etc. It’s a powerful toolkit. My public cloud instance is hosted at<a href="http://www.prgmr.com"> prgmr.com</a> and can be found <a href="https://watcher.forwardingplane.net/smokeping/smokeping.cgi">here</a>.
---
title: 'Enabling IPv6 on Juniper SRX 5800 cluster'
date: Wed, 20 Oct 2010 21:59:00 +0000
draft: false
tags: [IPv6, Security]
---

After [enabling the IPv6 Flow based processing](http://tech.buraglio.com/2010/09/srx-ipv6-flow-based-processing.html), we decided to get rolling with making our IPv6 path congruent with everything else (IPv4 unicast and multicast). With all of the other things we had going on, we thought this would be a low hanging fruit that would be easily plucked from the routing tree. Well, a minor oversight on our part caught us by surprise.

According to this [handy dandy matrix for JunOS 10.2 on the SRX](http://www.juniper.net/techpubs/software/junos-security/junos-security10.2/junos-srx-jseries-support-reference/jd0e5522.html), Active/Active is actually not supported for v6 processing. After configuring all of the rest of the path, BGP peerings, OSPFv3, an IPv6 firewall policy, we were a bit surprised to see OSPFv3 adjacencies andappropriate routes, but absolutely no state for v6 traffic that was not destined for the RE.

  

About 30 seconds of google searching came up with the matrix, which we somehow missed, that showed exactly what we feared:

  

![](http://lh3.ggpht.com/_99YK8gwWGlQ/TL8UouI51lI/AAAAAAAAACM/7humintSX-I/s1152/Screen%20shot%202010-10-20%20at%2011.09.54%20AM.png)

  

My first reaction was

![](http://www.popartuk.com/g/l/lgmp0163+homer-simpson-doh-the-simpsons-mini-poster.jpg)

  

How could we have missed that? We knew that IDP wouldn't work on v6 until a future release (probably sometime of next year, we're hoping). Oh well, we missed something. It was bound to happen sooner or later with as many moving parts as we have. Doing some more digging it looks like we're not going to get Active/Active until around the same time as IDP

  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
---
title: 'NAT IPv4 and Public IPv6'
date: Fri, 10 Sep 2010 23:51:00 +0000
draft: false
tags: [Uncategorized]
---

I've recently taken to thinking a lot more about IPv6.  I've been using an [HE tunnel](http://www.tunnelbroker.net/) for as long as I can remember at home.  This poses an interesting question about addressing.  Since I have not had a public address block at home for almost 7 years, I have been using NAT for IPv4.  However, my IPv6 netblocks are a /64 and a /48, which are both far more address space than I could ever possibly use.  
There are more IPv4/IPv6 transitional mechanisms than a person could ever need, and keeping them straight, in addition to throwing an existing NAT IPv4 network (potentially a huge one) is tough.  
How are other large IPv4 deployments with NAT handling the inclusion of public IPv6 addresses?  One would guess that many of the sites are simply ignoring IPv6 until they absolutely have to use it.  Other sites may be deploying it in small pockets and not routing it offsite.  Yet other sites may be pushing it out and just making it a default deny inbound policy behind existing firewalls.  
Of those solutions, none really seem that appealing to me.  Maybe I need to shift my thinking about the public/private aspect of v4 in comparison to v6.  
To that end, how does one create tiered firewall groups for IPv6 (a topic for yet another set of poorly written notes)?  
  
A few ideas that I've kicked around in my head were these:  
  
1\. No IPv6 (not really an option, but here for completeness)  
  
2\. IPv6 in a fully firewalled state (default deny inbound).  Not the greatest solution considering the additional headers in IPv6 and it's native support for providing message authentication and integrity (AH) and message confidentiality and the integrity (ESP).  
  
3\. Different security models for the protocols (messy and hard to manage in the long run).  
  
4.[ULA](http://en.wikipedia.org/wiki/Unique_local_address) (yuck; its not really 1918 space for IPv6 and doesn't solve the off-the-site-connectivity problem anyway unless we use an [ALG](http://en.wikipedia.org/wiki/Application-level_gateway)).  
  
  
[This](http://yorickdowne.wordpress.com/2010/01/15/ipv6-addressing-renumbering/) was an interesting read on a very similar subject.
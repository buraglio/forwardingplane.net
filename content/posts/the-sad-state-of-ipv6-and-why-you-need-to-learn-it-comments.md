---
title: 'The sad state of IPv6 and why you need to learn it.'
date: Mon, 05 Aug 2013 11:18:03 +0000
draft: false
tags: [IPv6, Musings, Soap Box]
---


#### 
[Engineer Z]( "zawada@ieee.org") - <time datetime="2013-08-12 08:13:35">Aug 1, 2013</time>

I agree fully. As you may recall Nick, for a long time I've said "NAT is a turd" and "Carrier-grade NAT is a polished turd." At least at first glance "Enhanced IP" looks like more turd polishing to me. How do we break folks' habit of working around the shortcomings of NAT and show the value of truly global address space? Why do folks keep hacking on the NAT kludge? One big problem is that too many folks now believe NAT is one of the required steps to secure their devices from the 'net. It's just one of those things you're supposed to do. If I put everything in 10.0.0.0/8 and NAT to my public address space then the bad guys can't get to my computers, right? We know the reality is that there are much better ways of controlling access without breaking the network stack in the process. (And they do a better of job of providing true security.) The cynical engineer me is starting to believe the state of networking technology has surpassed the abilities of many of the so-called network administrators and engineers out there. You're going to replace IPv4 with IPv6? (LOL- I envision a Folgers-type switch. We've secretly replaced the IPv4 protocol that John Smith's network usually serves with IPv6... Let's see if anyone can tell the difference...) You're going to freak out a lot of folks all the way up and down the IT management change because their brains can't possibly grok yet another technology to stuff into the network infrastructure. I hope I'm wrong and that things aren't so bad in the IT community. Lastly, I think part of the problem is a chicken-egg situation. While some of the big boys support IPv6 (my PFSense box stats say IPv6 has reached some significant penetration) the vast majority of sites out there still don't support IPv6. Do a "dig www.amazon.com AAAA" (or, my favorite, "dig www.slashdot.com AAAA" :-) ) and tell me what you see. However there is hope when www.fark.com has an IPv6 address. I think we need to keep up the evangelizing because there are enough useful IPv6 destinations out there. Perhaps if we get deep enough penetration with IPv6 we'll start seeing some IPv6-only destinations which can start snowballing IPv6 deployment.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-10-21 09:47:24">Oct 1, 2013</time>

Addressing in v6 is a bit different. Each interface can (and will) have many addresses, moving addressing is a bit more straightforward (yes, unless you get PI address space from ARIN you'll need to renumber if you change ISPs). I usually recommend using the M bit and DHCPv6. In my opinion static addressing for anything that isn't a server is a management challenge waiting to happen.
<hr />
#### 
[J Hull]( "jch777@gmail.com") - <time datetime="2013-09-24 14:39:49">Sep 2, 2013</time>

First off, I have to admit I know very little about IPv6. But I have a senior network admin in my team that seems pretty well versed. While he was explaining some of the differences between IPv6 & IPv4 the question came up: If we use IPv6 and all devices are addressed from a block that our ISP has assigned to us, what happens when we change ISP's? Can the address block follow the company instead of staying with the ISP? If not, then I think would make sense that when you use IPv6 it would be assumed that all systems will use DHCP? It would seem to me that static addressing may causes an incredible amount of work if you need to switch providers. Sorry if the above questions highlight my limited understanding. We're a fairly small company (<200 FTE) and our plate is always full of immediate "must have" projects for our business units. But I have told my IT team that upgrading our network to IPv6 is a priority in our 1-3yr planning process.
<hr />

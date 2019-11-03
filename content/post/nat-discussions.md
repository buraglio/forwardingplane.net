---
title: 'NAT discussions, fact checking, and debate'
date: Mon, 11 Jun 2018 09:41:15 +0000
draft: false
tags: [Security]
---

I’ve been very vocal about the misinterpretation of NAT for many, many years. Since it's inception, NAT has been slowly perverted into what many now believe to be a security mechanism. While I do see a reasonable use of IP masquerading in a larger security strategy, this is not the original intent (or implementation) of NAT. What mosts network engineers call "NAT" is actually [one to many network port address translation](https://www.tldp.org/HOWTO/IP-Masquerade-HOWTO/ipmasq-background2.1.html) - or taking one public address and "hiding" a number of private (likely [RFC1918](https://tools.ietf.org/html/rfc1918)) addresses "behind" it, using ports to translate traffic and keeping the state of those connections. Given my....vigor for debating the details of NAT, I was invited to discuss this on [an episode of The Network Collective Podcast.](https://thenetworkcollective.com/2018/05/ep28-for-the-love-of-nat/) We get to some of the grimy details with some technical heavy hitters, so if you're into the debate, it is certainly worth a watch.
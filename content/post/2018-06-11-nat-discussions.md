---
id: 1468
title: 'NAT discussions, fact checking, and debate'
date: '2018-06-11T03:41:15-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1468'
permalink: /2018/06/11/nat-discussions/
Views:
    - '172'
categories:
    - Security
---

I’ve been very vocal about the misinterpretation of NAT for many, many years. Since it's inception, NAT has been slowly perverted into what many now believe to be a security mechanism. While I do see a reasonable use of IP masquerading in a larger security strategy, this is not the original intent (or implementation) of NAT. What mosts network engineers call "NAT" is actually <a href="https://www.tldp.org/HOWTO/IP-Masquerade-HOWTO/ipmasq-background2.1.html">one to many network port address translation</a> - or taking one public address and "hiding" a number of private (likely <a href="https://tools.ietf.org/html/rfc1918">RFC1918</a>) addresses "behind" it, using ports to translate traffic and keeping the state of those connections. Given my....vigor for debating the details of NAT, I was invited to discuss this on<a href="https://thenetworkcollective.com/2018/05/ep28-for-the-love-of-nat/"> an episode of The Network Collective Podcast.</a> We get to some of the grimy details with some technical heavy hitters, so if you're into the debate, it is certainly worth a watch.
<iframe src="https://player.vimeo.com/video/272381393" width="640" height="360" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
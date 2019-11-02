---
title: 'How to be a [good] Network Engineer (and network engineer appreciation day)'
date: Sun, 10 Nov 2013 04:02:52 +0000
draft: false
tags: [Musings, Soap Box]
---


#### 
[Samuel Akoi]( "Sakoivision@yahoo.com") - <time datetime="2013-12-13 09:43:42">Dec 5, 2013</time>

I love Networking
<hr />
#### 
[Lennie](http://www.softwaredefinedeverything.com/ "forwardingplaneblog@consolejunkie.net") - <time datetime="2013-12-01 05:09:40">Dec 0, 2013</time>

On broad interests, what has me really excited right now is: Linux containers like Docker and for some strange reason WebRTC (well, only slightly strange, because I'm a webguy too). I'm thinking, maybe, just maybe, I can use more Linux routing on our network: http://containerops.org/2013/11/19/lxc-networking/ Not Docker specifically, or even containers, but network namespaces. Network namespaces in Linux supports: forwarding, bridging, static routing and dynamic routing (for example Quagga), iptables, looks like it even supports iptables conntrackd and even IPSEC. Think about it, in the data center you should be deploying small, per application VMs and networks: http://blog.ipspace.net/2013/11/typical-enterprise-application.html http://blog.ipspace.net/2013/11/make-every-application-independent.html What have we learned from the Internet and 'cloud': stateless scales. So I'm thinking about playing with: deploying network namespaces.
<hr />
#### 
[Lennie](http://www.softwaredefinedeverything.com/ "forwardingplaneblog@consolejunkie.net") - <time datetime="2013-12-01 04:38:39">Dec 0, 2013</time>

What I'm always surprised about is that sometimes you talk to people who do only routing at large providers also only know routing. Like some Microsoft Exchange admin that only knows Microsoft Exchange and nothing about Windows. Most of the other networking people I have interacted with have a lot broader interests.
<hr />
#### 
[Lennie]( "forwardingplaneblog@consolejunkie.net") - <time datetime="2013-11-10 02:15:18">Nov 0, 2013</time>

So what you might be saying is: many times network engineers are born out of necessity because nobody else wanted to do the job or enough of a generalist, curious and/or intrigued enough to take action or even understand the networking problems. I've always called myself a problem solver or even a debugger first, network engineer is just part of my job. When people can't figure out for themselves what is going I get called in to solve the problem. So this makes a lot of sense to me. On the point of too much networking would never be enough. Well, I have a feeling there is going to be a lot more networking because the hosts at the edge are going to perform more and more networking tasks. It used to be pretty much the only distributed networking protocol that the edge participated in was TCP (the distributed algorithm and protocol to fairly share the available bandwidth). But now we are seeing: more sensors, more mobile, Multi Path-TCP and overlay networking, sometimes combined with switching, firewalling, loadbalancing and routing. And even WebRTC (a peer2peer protocol for browsers and other applications that want to exchange: audio, video and data). So there will be a lot more devices in the network practicing more networking tasks and it's all based on the IP protocols. The people at the FCC are saying PSTN is going the way of the dodo. It's all IP-based. That means everything will depend on IP. For example did you know LTE is IP-based, for everything, including voice ? And did you know the encryption protocol for the signaling and data protocol is IPSEC ? Even more interesting: did you know that IPSEC for LTE is optional ?
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-11-29 14:39:13">Nov 5, 2013</time>

"Problem solver" is a very apt description of a good network engineer. Those are the ones that you want to keep around. I actually had no idea that LTE was all IP. I think that's great. I also love that most of the LTE networks are now IPv6 dual stacked.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-12-07 14:31:39">Dec 6, 2013</time>

I think this makes a lot of sense. Principals like KISS are as valid today as they were 15 years ago, see Ivan's [post](http://blog.ipspace.net/2013/12/still-waiting-for-stupid-network.html). Name spaces are a logical next step in simplifying things like simplification of service deployment. [Scott Lowe has a great write up on it](http://blog.scottlowe.org/2013/09/04/introducing-linux-network-namespaces/), and it looks like we have both commented on it. It's a logical part of a larger migration of how networking as a whole is done in my humble opinion.
<hr />
#### 
[Lennie]( "forwardingplaneblog@consolejunkie.net") - <time datetime="2013-12-07 14:55:21">Dec 6, 2013</time>

There is a reason that wasn't mentioned to keep it KISS is it makes it easier to automate, because KISS is more predicatable.
<hr />

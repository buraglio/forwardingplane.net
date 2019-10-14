---
title: 'Sonicwall - Old dog learns [some] new tricks'
date: Sat, 08 Dec 2012 00:00:26 +0000
draft: false
tags: [Firewall, Security, Security]
---


#### 
[Paul Leet]( "paul.leet@gmail.com") - <time datetime="2012-12-08 22:40:04">Dec 6, 2012</time>

Having worked on both and done POC for 5800 and Supermassive, if you enable any DPI function or SSL offload, the SRX chokes while the Supermassive hums along. There are only a couple configurations where the SRX has the SonicWALL beat. Check out Network testing and NSS labs results for independent testing. I can send them to you if you wish. /p
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2012-12-10 21:38:17">Dec 1, 2012</time>

I did not have that result at all. Quite the opposite, in fact. We were able to have full DPI on all IPv4, pumped the box full of traffic, IPv4, IPv6 and IPv4 multicast, al while inspecting all packets and spanning packet size from 9k to 64 bytes. We even pulled out SPCs while doing this and the box happily plumbed along. And actually, we’re doing DPI on IPv6 traffic as well, in production, now. That being said, I look forward to putting the supermassive through it's paces. I really welcome great competition to high level products. The more options out there, the better.
<hr />
#### 
[| The Forwarding Plane](http://www.forwardingplane.net/2013/01/294/ "") - <time datetime="2013-01-02 00:01:50">Jan 3, 2013</time>

\[...\] months. I was once again surprised to see that a firewall post was clearly the most popular.  The recent post on the Sonicwall was the clear, overwhelming winner having more than twice the views as it’s closest \[...\]
<hr />
#### 
[EH]( "ezhelm@gmail.com") - <time datetime="2012-12-15 08:52:23">Dec 6, 2012</time>

Funny story re: those older sonicwall platforms. 10 years ago or so, I was working with a client that had one of the smaller Sonicwall platforms, and there was a software bug that would hold sessions indefinitely. This would cause the box to stop forwarding traffic after a few days. You could clear the sessions through some hidden "diag.html" page, but my client didn't have anyone on staff that was savvy enough to do it. So, I ended up putting the Sonicwall on a christmas tree timer that would reboot it each night after hours. Problem solved. Haven't installed another Sonicwall since. I've worked on many and still don't care for their GUI. Maybe its time to revisit their latest platform and software versions.
<hr />
#### 
[Most popular posts of 2012 | The Forwarding Plane](http://www.forwardingplane.net/2013/01/most-popular-posts-of-2012/ "") - <time datetime="2013-01-01 23:56:57">Jan 2, 2013</time>

\[...\] months. I was once again surprised to see that a firewall post was clearly the most popular.  The recent post on the Sonicwall was the clear, overwhelming winner having more than twice the views as it’s closest \[...\]
<hr />

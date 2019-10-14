---
title: 'Building a secured network in a box'
date: Fri, 26 Jul 2013 05:28:15 +0000
draft: false
tags: [Lab Time, Security, Virtualization]
---


#### 
[Depenetration, whuaat? | JRLZN](http://jirahlization.wordpress.com/2013/09/27/depenetration-whuaat/ "") - <time datetime="2013-09-26 19:54:31">Sep 4, 2013</time>

\[…\] Photo Credit: http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/ \[…\]
<hr />
#### 
[Aaron]( "Iamenabled@hotmail.com") - <time datetime="2013-07-26 06:19:41">Jul 5, 2013</time>

Nick, can you share the server hardware you are using for your VMware host?
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-07-26 09:19:45">Jul 5, 2013</time>

For this case it's an older Dell PowerEdge 2900 with 16G RAM, 4 x 1G NIC and 8x2.3Ghz cores
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-07-28 17:03:39">Jul 0, 2013</time>

On a reliability note, uptime has been fantastic
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-07-28 17:03:04">Jul 0, 2013</time>

This is my fun time until my kids are old enough for me to get back on the mat or on the bike regularly. It's fun but it does take a lot of time, but I really do enjoy it. This is what got me into networking 15+ years ago so it's very nostalgic for sure and I enjoy writing about it. Very interested in 10.8.4 under esxi, though, for sure.
<hr />
#### 
[Ryan Harden]( "ancker@ancker.net") - <time datetime="2013-07-31 08:43:08">Jul 3, 2013</time>

Getting OSX running under ESXi on a non-Apple box is actually SUPER easy. Shoot me an email and I'll give you the instructions.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-07-31 08:44:45">Jul 3, 2013</time>

Yes, yes it is.
<hr />
#### 
[Ryan Harden]( "ancker@ancker.net") - <time datetime="2013-07-26 17:05:38">Jul 5, 2013</time>

I just got my ESXi box (Via Jim) up. Waiting on some bits and pieces for the final config, but it's mostly there. I'm not sure I want as complicated of config as you. I like my ALIX board running pfSense and don't really want to put all of my eggs in one basket. Working from home requires 100% uptime. :) I also have a slight advantage/benefit of having a Cisco 3650G-PS as my home switch. So I can SPAN right from there. It'll only see traffic behind the pfSense box, but that's good enough for me. I'm planning on putting that directly into Security Onion as well. As a side note: I have 10.8.4 running in ESXi as my new Plex server. Holy Crap it's awesome. I haven't decided whether I'm just retiring the old Mac Mini or going to turn it into a Plex Client. I'm envious that you're doing stuff like this but I've got enough going on in my work life that I'm very happy to forget about networking when I'm done for the day. If things ever settle down I might reopen the 'networking as a hobby' can of worms again.
<hr />

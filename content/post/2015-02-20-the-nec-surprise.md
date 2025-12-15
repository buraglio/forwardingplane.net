---
id: 1161
title: 'The NEC surprise'
date: '2015-02-20T00:52:33-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1161'
permalink: /2015/02/20/the-nec-surprise/
themeblvd_title:
    - 'NEC brings a strong offering to the SDN table'
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'NEC, Data Center, OpenFlow, NFV, Network Field day 9, NFD9, #NFD9, nick buraglio, tech field day, carrier, service provider'
themeblvd_description:
    - 'NEC shored up and brings a strong player to the table in the SDN and OpenFlow world at Network Field day 9. '
dsq_thread_id:
    - '3626689584'
Views:
    - '170'
categories:
    - Cloud
    - 'Data Center'
    - OpenFlow
    - SDN
---

When <a href="http://necam.com/">NEC</a> began talking about SDN at <a href="http://techfieldday.com/event/nfd9/">Network Field Day 9</a>, I was not sure what to expect. I knew they had been heavily involved with openflow since the early days, and many years ago I was able to get my hands on their early OpenFlow controller and was immediately frustrated by its cryptic nature and frankly, poor documentation. Their switches were fine and were heavily utilized in early OpenFlow deployments. I knew they had decent support and were squarely on board the SDN train. Their controller, in 2010, was not terribly fun to work with. It was (if memory serves) prohibitively expensive and the support manual was nearly as cryptic as the controller. Because it's my personality type, I went in with a very open mind, hoping to be surprised. After all, it'd been 4+ years since I'd seen that controller.
Well, I am here to report that I will happily eat some crow.
<a href="http://www.forwardingplane.net/wp-content/uploads/2015/02/Eat-Crow.jpg"><img class=" size-full wp-image-1162 aligncenter" src="http://www.forwardingplane.net/wp-content/uploads/2015/02/Eat-Crow.jpg" alt="Eat Crow" width="293" height="200" /></a>
 
A few things became very apparent to me as I sat and watched the presentation from NEC, which you can view in its entirety below:
<ul>
	<li>NEC is not messing around with their SDN offering. They've been in the openflow game since the beginning and the polish on their controller shows it. The topology is quite nice and they've got a finished looking product that would find itself at home in a decent sized NOC.</li>
	<li>NEC is playing well with others. Their demo consisted of both NEC and DELL whitebox switches. To me this is an indication of both great forward thinking and a clear message that the controller is a product that can stand on its own.</li>
	<li>NEC is setting the barrier of entry low. Very low. They've got an entry level "SDN in a box" that consists of their controller and a few switches for like 3k. They're also offering a 90 day free trial on their controller that is bundled with <a href="http://mininet.org/">mininet</a>.</li>
	<li>Like most other controllers, the NEC controller is topology aware and using openflow 1.3 for it's communication. Unlike any other demo I've seen, NEC used CLI to make changes and displayed the updates in near realtime on the controller.</li>
</ul>
They've got a tap product aimed at security tap aggregators a la <a href="http://www.gigamon.com/">gigamon</a>, so they're seeing the value of SDN and openflow from a security lens as well as a network operations perspective, a good play in my opinion. SDN and openflow in particular have a great deal to offer the security community (think of all of the wacky stuff your security team has asked for and then map that into an openflow network. You'll probably hit 80% match). NEC has done some tight integration with <a href="https://technet.microsoft.com/en-us/windowsserver/dd448604.aspx" target="_blank" rel="noopener noreferrer">microsoft hyper-v</a> too, so environments leveraging hyper-v as a virtualization technology can drop this in to take advantage of the network programmability on top of their virtualization environment. This is something that I'd not seen before [although it may exist and I just don't know it].
In addition, NEC has spun up an "app store" for SDN apps and allowed for some cross pollination, with a handful of caveats, with <a href="http://www.opendaylight.org/">opendaylight</a> for testing.
&lt;speculation&gt;
There are a few things I find interesting about the NEC offering and about NEC in general. Being in a service provider environment off and on for most of my career, the fact that NEC is getting involved so heavily is intriguing. Unlike most of the other DC focused companies, NEC plays in the carrier market. While this particular briefing did not include any carrier updates, it would surprise me if this wasn't being investigated behind some big doors. It makes sense to me and it would be a surprise if it did not occur to someone else. The SP market is fickle and slow to change, but ripe for fresh ideas. I see a lot of potential both there and in the DC / campus / enterprise.
&lt;/speculation&gt;
 
<iframe src="//player.vimeo.com/video/119508255?title=0&byline=0&portrait=0" width="500" height="281" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<a href="https://vimeo.com/119508255">Introduction to NEC Networking</a> from <a href="https://vimeo.com/sfoskett">Stephen Foskett</a> on <a href="https://vimeo.com">Vimeo</a>.
<iframe src="//player.vimeo.com/video/119508725?title=0&byline=0&portrait=0" width="500" height="281" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<a href="https://vimeo.com/119508725">NEC ProgrammableFlow vCOps Solution</a> from <a href="https://vimeo.com/sfoskett">Stephen Foskett</a> on <a href="https://vimeo.com">Vimeo</a>.
<iframe src="//player.vimeo.com/video/119510207?title=0&byline=0&portrait=0" width="500" height="281" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<a href="https://vimeo.com/119510207">ProgrammableFlow SCVMM Demo</a> from <a href="https://vimeo.com/sfoskett">Stephen Foskett</a> on <a href="https://vimeo.com">Vimeo</a>.
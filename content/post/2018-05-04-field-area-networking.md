---
id: 1463
title: 'Field Area Networking'
date: '2018-05-04T07:38:15-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1463'
permalink: /2018/05/04/field-area-networking/
Views:
    - '295'
categories:
    - IPv6
    - Musings
---

It's no secret that RF technologies and what like to call "specialty networking" are two of my favorite things in the networking space. <strong>Put them together and it is like chocolate and peanut butter!</strong> Now, some may not consider Field Area Networking (FAN) to be "unconventional", but it certainly falls well outside of the space of what is typically traditional enterprise networking. That said, Cisco's FAN briefing at <a href="http://techfieldday.com/event/nfd17/">Network Field Day 17</a> really got me excited and thinking about the alternatives for the IoT space. Other than cellular LTE or <a href="https://www.link-labs.com/blog/what-is-lte-m">LTE-M</a>, there are few options for remote IoT devices with limited power draw and bandwidth requirements. So I went down the twisted path of investigating that space, and recently, I recorded a <a href="https://thenetworkcollective.com/">Network Collective</a> short take on the subject, available below.
<iframe src="https://player.vimeo.com/video/267986827" width="640" height="360" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
The NFD 17 Cisco FAN briefing that this is based around is also worth a watch - this is really innovative stuff that many of us probably don't think about.
<iframe src="https://player.vimeo.com/video/253197120?title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<a href="https://vimeo.com/253197120">Cisco Innovations for the Field Area Network with Rupak Chandra</a> from <a href="https://vimeo.com/sfoskett">Stephen Foskett</a> on <a href="https://vimeo.com">Vimeo</a>.
 
<h3>Nick's take:</h3>
As we talk about things like cloud migration, automation, orchestration, and security architectures, lets consider the sheer scale of not just IoT networking but the sensor and other industrial networking <em><strong>outside</strong> </em>of the enterprise space. The sheer number of devices to be managed in these spaces is stupefying, and the transport of the data created by these networks as well as the management of the devices and network elements is a non-trivial detail. Building out networks such as a sensor network has a completely different scope and scale than a stereotypical enterprise or even a carrier service provider network. Keeping in mind just the number of hosts things like addressing schema become a critical part of the architecture (spoiler: you're probably not going to be able to scale IPv4). Power and environmental considerations are also not nearly as squishy as they can be in a nice, controlled data center. Considering those data points, it's pretty clear that there is plenty of interesting stuff happening in both the engineering and security areas.
 
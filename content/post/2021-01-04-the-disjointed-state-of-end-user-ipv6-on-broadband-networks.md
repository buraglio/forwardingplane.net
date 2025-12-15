---
id: 2414
title: 'The Disjointed state of end user IPv6 on broadband networks'
date: '2021-01-04T04:36:00-06:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2414'
permalink: /2021/01/04/the-disjointed-state-of-end-user-ipv6-on-broadband-networks/
Views:
    - '1097'
image: /wp-content/uploads/2021/01/Beginner-s-Guide-to-IPv6-min.png
categories:
    - IPv6
    - Musings
    - Rant
---

<!-- wp:list -->

- *I have been sitting on this post for quite some time. This is a long, and personal story with some technical bits for those looking to solve the same problem I was. *

<!-- /wp:list -->

<!-- wp:paragraph -->

It was a long, complicated, frustrating journey of sad realization about the state of IPv6 for everyday users and those with business class connections over consumer focused network last mile networks. It is well documented and annoyingly understood that[ I am a vocal proponent](https://forwardingplane.net/2018/09/01/as-a-small-to-medium-isp-why-you-should-deploy-ipv6/) of IPv6. My hands have been on it both professionally and as a enthusiastic learner since roughly 2002, and I have had it at my home network since very early [HE tunnelbroker services ](https://www.tunnelbroker.net)were available, and natively as soon as it was live on my provider(s). I consistently ran IPv6 only using NAT64/DNS64 for quite a long time, even [pointing out to my provider back in 2017 ](https://forums.businesshelp.comcast.com/t5/IPV6/Reproducible-denial-of-service-of-Netgear-CPE-running-native/td-p/31579)that I could successfully, and repeatedly DoS the modem they forced me to pay them to rent on my business service. Having both built run broadband internet providers in my career, I understand the economies of scale of consistently running a service. However, I have found this to break down quite quickly with certain things - IPv6 being the one here. See, when someone has a business class service with certain providers, and they want a static ip or a block of addresses, they are required to rent a CPE from said provider. This makes sense, I did it even back in the early DSL days, and the advantages are clear: consistent service, configuration, support. Easy inventory for replacement, and over time the kit pays for itself. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Lets jump back to that modem I could DoS. After a bit of time and a lot of level2 tech calls, I was given a new modem. This modem had more channels (meaning it could support faster speeds over the DOCSIS network) and supposedly had better, longer support life in front if it. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I was happy with this device. I had it for 3 years without issue, able to use my static IPv4 and /59 pieces of my /56 of static IPv6 space. What I did not know, though, was that this was a one-off. I had the ONE device that worked on their service and correctly supported [DHCPv6-PD](https://en.wikipedia.org/wiki/Prefix_delegation). See, DHCP in IPv6 is quite different. On a normal connection with static addressing, the addresses are routed with RIPv2 from the modem device. Easy, simple, low overhead. With IPv6, we think about network prefixes as the building blocks, not individual addresses, and the DHCP mechanisms are quite different as well. On a typical DOCSIS connection you one may have a modem with a /128 address on the "outside" interface of the modem, and then a prefix that is delegated to the inside of the modem. If you have a standard bridge and no static IPs, you can stop here - you're done. Your CPE gets a block of addresses and assigns them to your internal networks and you have end to end connectivity again, just as the internet was intended to have before we polluted it with layers of address translation, [RFC 6598](https://tools.ietf.org/html/rfc6598), [RFC1918 space](https://tools.ietf.org/html/rfc1918) and [CGNAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT). If you're not sing a bridge, though, from there, a modem that is acting as a router (as the business class connections are required to do to support static addressing), it must then sub-delegate a chunk of the original delegation. In most cases it's a /56 then sub-delegated into a /59. Plenty of space. That is how my Cisco modem worked until the day it died in June of 2020. 

<!-- /wp:paragraph -->

<!-- wp:image {"id":2415,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large">![](https://forwardingplane.net/wp-content/uploads/2021/01/Screen-Shot-2020-08-29-at-2.45.41-PM-976x1024.png)</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

Easy, right? Wrong. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

As you may have ascertained, this provider is Comcast, and as I alluded to earlier, I was quite happy with the service for many, many years, had very little as far as interruptions and happily paid a premium for business service. I still have their business service and (somewhat less) happily pay for it. For those that are looking at "solving" this problem for themselves, the take aways for the issue at hand are this:

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The only devices at the time of this writing that work with static IPv4 and IPv6 on this provider are the Older Netgear and just one of the [Puma based](https://www.classactionlawyers.com/puma6/) Cisco modems, the DPC3939B *(related: the link on the puma chip issues is a great read and emphasizes the unparalleled importance of actually understanding the hardware that comprises given network gear and the problems it can create)* . I am under the impression that neither model is deployed any longer. Once I realized that the "Technicolor" model I was issues was not going to work, I went through all of the available options including the CBR-T CGA4131COM for their gig service. They all have the same behavior: sub-delegation of a /56 and continual neighbor discovery for the sub-delegated prefix, i.e. totally broken and unusable behavior. Let's be clear: **The only IPv6 that Comcast officially supports is a single /64 connected directly to their device, period. Full Stop. **For those looking to solve this problem, it isn't happening any time soon, there is no profit to appease a handful of squeaky wheels and I have been told by more than one higher up that the problem reports to fix these modem firmware issues are not even in the pipeline yet, largely because there are so few complaints. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

What does this mean? It means that there is a lot of work to still do to make v6 work as well on terrestrial broadband as it does on mobile networks. It has come quite a long way, but - probably not unexpectedly - the edges are still a tad rough. Perplexingly, consumer grade services seem to have significantly better IPv6 support. For those of us that live in a world where we understand the technologies used to deliver our service, have built or supported them in the past, and have a high expectation of support, we will probably be left wanting. It's not all for not, though. Every complaint, every question, every canceled service grows an increasing mound of data that this service is expected. Why did I write this? Because the data didn't exist anywhere and the forums were not terribly useful. In short, to save someone else headaches that I already had. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

As for me? I gave up my statics, sent back the modem and bought my own DOCSIS 3.1 bridge. I can reliably get a /60 with this setup and work around the rest, as well as save myself $50 a month in fees. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

 For anyone still interested, this whole trash fire was documented in this long, rambling [thread](https://forums.businesshelp.comcast.com/t5/IPV6/Another-broken-dhcpv6-pd-complaint-on-brand-new-DPC3939B/td-p/41952).

<!-- /wp:paragraph -->
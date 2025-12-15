---
id: 2455
title: 'IPv6-only and why it is past time to embrace IPv6'
date: '2021-02-10T04:04:00-06:00'
author: buraglio
excerpt: 'IPv6-only is coming'
layout: post
guid: 'https://forwardingplane.net/?p=2455'
permalink: /2021/02/10/ipv6-only-and-why-it-is-past-time-to-embrace-ipv6/
Views:
    - '1198'
image: /wp-content/uploads/2021/02/IPv6-Only.png
categories:
    - IPv6
    - Podcast
---

<!-- wp:paragraph -->
<p>IPv6 has been a hotly contested technology for as long as I can remember. It has always been "a few years out", or something "no one is asking for", depending on who is asked. In reality, and like most things, the truth lies somewhere in the middle. IPv6 has been slow to appear for certain demographics of networking, but a long standing pillar in others. It just so happens that IPv6 is not being asked for because when deployed correctly most users just don't notice that it is there - and that's by design. To really understand how IPv6 deployments work, one needs to know a bit of history and have a dash of understanding of deployment models. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>In the "old days", running multiple protocols on the same routed medium was common.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In the "old days", running multiple protocols on the same routed medium was common. It was not a surprise to see AppleTalk, IPX/SPX, and IP all on the same LAN. Sometime around 2002 the multiple protocols stopped being as common, and IP just took over. It was, after all, the protocol that ran the internet which was quickly becoming more like a utility and less like a novelty. Around this time, IPv6 started to bubble up here and there and the <a href="https://en.wikipedia.org/wiki/6bone">6bone</a> deployment was peaking. IPv6 became "important" to a whole new cohort, but alas, the stack was not really ready for prime time support and vendor support - and by extension hardware capabilities - were novelty at best and non-existent at worst. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":2456,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://forwardingplane.net/wp-content/uploads/2021/02/IPv6-is-coming.png" alt="" class="wp-image-2456"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Fast forward a decade. IPv6 support is reasonable and it has started to bubble up in backbones and even on dual stacked networks. Remember the multiple protocols running on the same network? This the time where that becomes relevant again, and probably the time that most engineers should have started paying attention to IPv6 and getting familiar. It started showing up in mobile networks, sensor networks, compute clusters, and more importantly it was getting mainstream OS support. This becomes important because there is also an initiative by vendors to support and in some cases even enable tunnels such as <a href="https://en.wikipedia.org/wiki/Teredo_tunneling">teredo</a> by default. What did this mean? It means that even those engineers staunchly against IPv6 were almost certainly running it without even knowing. What was the right answer to the concern? There were two:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Disable IPv6 by policy on every device in a given administrative domain</li><li>Enable native IPv6 everywhere </li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Both were daunting tasks, so most just happily ignored v6 as a novelty problem for "<em>future me</em>". Well, the future has steamrolled over many folks. There are now initiatives to implement IPv6-only. That's not dual stack. That means no IPv4 for large parts of a given networks. Fret not, friends! This isn't as extreme as it sounds. There are <a href="https://www.tunnelbroker.net">significant</a> <a href="https://forwardingplane.net/ipv6-qa-for-isps/">resources</a> for learning and <a href="https://packetpushers.net/series/ipv6-buzz/">mastering</a> IPv6, and the truth is that for most organizations, IPv4 behind some middle box doing <a href="https://en.wikipedia.org/wiki/Network_address_translation#One-to-many_NAT">masquerading</a> isn't going anywhere, but there will almost certainly be a need for some IPv6 transit. And while there is still <a href="https://forwardingplane.net/2021/01/04/the-disjointed-state-of-end-user-ipv6-on-broadband-networks/">a lot of work to be done</a>, we are closer than we have ever been. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Fret not, friends! This isn't as extreme as it sounds.</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For those interested in learning a bit more about IPv6-only, there are some resources I have been involved with that are a reasonable start. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I was asked to talk about some of the more recent efforts in deploying IPv6-only on a recent IPv6 Buzz podcast, take a listen. </p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<iframe width="320" height="30" src="https://packetpushers.net/?powerpress_embed=50294-podcast&powerpress_player=mediaelement-audio" frameborder="0" scrolling="no"></iframe>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
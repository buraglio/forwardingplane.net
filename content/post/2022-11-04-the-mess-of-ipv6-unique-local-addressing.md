---
id: 2552
title: 'The mess of IPv6 Unique Local Addressing'
date: '2022-11-04T02:52:00-05:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2552'
permalink: /2022/11/04/the-mess-of-ipv6-unique-local-addressing/
Views:
    - '1839'
    - '1839'
image: /wp-content/uploads/2021/01/Beginner-s-Guide-to-IPv6-min.png
categories:
    - IPv6
    - 'Lab Time'
    - Podcast
tags:
    - IPv6
---

<!-- wp:paragraph -->
<p>IPv6 unique local addressing has been a popular topic over the years. From its humble beginnings, replacing site-local, to the surge of interest within service providers, enterprise, and casual users due to the wealth of content now available on IPv6 and the prevalence of availability within major consumer ISPs, it has become quite a polarizing topic in the technical communities that are diving head first into the modern, current networking protocol - IPv6. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As defined by RFC4193:&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>“This IETF standards document defines an IPv6 unicast address format that is globally unique and is intended for local communications.&nbsp; These addresses are called Unique Local IPv6 Unicast Addresses and are abbreviated in this document as Local IPv6 addresses.&nbsp; They are not expected to be routable on the global Internet.&nbsp; They are routable inside of a more limited area such as a site.&nbsp; They may also be routed between a limited set of sites.”</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>One mistake that is repeated over, and over, and over, and over is the desire to replicate RFC1918 space - and one can understand why: Networks have been built with private IPv4 addressing for over two decades now, and in that span of time vendors, FOSS projects, and pundits have championed NAP-T (Or NAT masquerading) as a part of the requisite security suite. Right or wrong, that is the common belief, so, when folks start thinking about their dual-stack IPv6 deployments, often one of the first thoughts is "how can I make this like what I already have?". This line of thinking inevitably leads to thoughts of Unique Local Addressing. Now, many folks have <a href="https://blogs.infoblox.com/ipv6-coe/ula-is-broken-in-dual-stack-networks/" target="_blank" rel="noreferrer noopener">written</a> and <a href="https://packetpushers.net/podcast/ipv6-buzz-107-ipv6-unique-local-addresses-at-ietf-114/" target="_blank" rel="noreferrer noopener">talked</a> <a href="https://www.modem.show/post/s02e03/">about</a> this. There is no end of content detailing out ULA, its flaws, it's uses, and a wealth of folks that have not really tested it but continue to discuss it. A few of us have even written a now WG accepted <a href="https://datatracker.ietf.org/doc/draft-ietf-v6ops-ula/" target="_blank" rel="noreferrer noopener">IETF draft</a> to address some of the misconceptions, considerations, and consequences of using ULA. Rather than details them out here, I submit a talk I gave on the use of ULAs, and what should be considered before deciding on a strategy.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>TL;DR:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>Operating systems treat IPv4 space equally</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Operating systems <strong><em>do not</em></strong> treat all IPv6 equally (by design)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Care must be taken when ULA is used because:<!-- wp:list -->
<ul><!-- wp:list-item -->
<li><strong>Operating systems will ignore its existence in the presence of IPv4 without intentional customization, requiring notable operational overhead</strong></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>While unique based on a 40bit randomization, there is the chance it can overlap.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Without quirky hacks, it is limited to a /48 in size&nbsp;</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Sounds crazy, right? This video of the entire talk explains it better than I can likely type out.  The real point is that there isn't really an analog for private IPv4 space, so moving to IPv6 will take a little bit of care, a lot of learning, and a fair amount of perspective.</p>
<!-- /wp:paragraph -->

<!-- wp:embed {"url":"https://www.youtube.com/embed/H98OL06ZAwM","type":"rich","providerNameSlug":"embed-handler","responsive":true,"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} -->
<figure class="wp-block-embed is-type-rich is-provider-embed-handler wp-block-embed-embed-handler wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://www.youtube.com/embed/H98OL06ZAwM
</div></figure>
<!-- /wp:embed -->

<!-- wp:paragraph -->
<p>Slides for the talk. </p>
<!-- /wp:paragraph -->

<!-- wp:file {"id":2556,"href":"https://forwardingplane.net/wp-content/uploads/2022/11/Using-Unique-Local-Addressing-ULA-in-IPv6-Enterprise-Networks.pdf","displayPreview":true} -->
<div class="wp-block-file"><object class="wp-block-file__embed" data="https://forwardingplane.net/wp-content/uploads/2022/11/Using-Unique-Local-Addressing-ULA-in-IPv6-Enterprise-Networks.pdf" type="application/pdf" style="width:100%;height:600px" aria-label="Using-Unique-Local-Addressing-ULA-in-IPv6-Enterprise-Networks"></object><a id="wp-block-file--media-b231a82c-4264-4859-8512-f06b3821ec68" href="https://forwardingplane.net/wp-content/uploads/2022/11/Using-Unique-Local-Addressing-ULA-in-IPv6-Enterprise-Networks.pdf">Using-Unique-Local-Addressing-ULA-in-IPv6-Enterprise-Networks</a><a href="https://forwardingplane.net/wp-content/uploads/2022/11/Using-Unique-Local-Addressing-ULA-in-IPv6-Enterprise-Networks.pdf" class="wp-block-file__button wp-element-button" download aria-describedby="wp-block-file--media-b231a82c-4264-4859-8512-f06b3821ec68">Download</a></div>
<!-- /wp:file -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
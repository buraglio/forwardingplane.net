---
id: 2595
title: 'PODCAST: MODEM.show; The road not-so-less traveled'
date: '2024-12-18T'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2594'
permalink: /2024/12/18/dns-dot-doh/
categories:
    - DNS
    - UNIX
    - Internet
tags:
    - DNS

DNS over TLS and DNS over HTTPS have become nearly ubiquitous in the home networking and enthusiast circles. But what do we really know about them and how they work? Most of the searches will yield results centering around using a pihole to front end upstream DoH services from huge providers. But what if you want to built services outside of your home network? What if you need to build DoH and DoT services for a larger audience? How much o we really know about what it takes to operate such a service?

It turns out that there is a fair bit more to understand, and most of it centers around DNS. DNS, that absolutely critical service that is understood, but not necessarily *deeply* understood. 

Kevin Myers once said “It’s always MTU, unless it’s DNS”, and my experience as a network engineer has proven that correct more times than can be attributed to coincidence.
DNS is such an important component of the internet that the IETF typically has TWO DNS working group meetings per IETF event to accommodate the large numbers of drafts and changes.

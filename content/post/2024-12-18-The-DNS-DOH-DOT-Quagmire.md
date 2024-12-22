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

In 25+ years of doing IT, DNS has frequently been a part of the responsibilities. Things have....changed. DNS is the BGP of the application services - we have put a great many things into it. Things that may be unexpected. Diving into DoH and DoT have opened that can of records back up to me. Let's start with DoT since I have a personal affinity for it (although given the fact that browsers have pushed DoH I suspect it will become more common). 
Building a DoT and DoH server is more than simply creating a configuration that references some certificates. There are new records that tell things like browsers that there are in fact services available. 



Testing DoT - 
`kdig -d @dot.chi.mpls.rsvp +tls-ca +tls-host=dot.chi.mpls.rsvp buraglio.com -t aaaa`
Testing DoH - 
https://doh.chi.mpls.rsvp/dns-query

```bash
# json
curl -vH 'accept: application/dns-json' 'https://doh.chi.mpls.rsvp/dns-query?name=www.forwardingplane.net&type=AAAA' | jq .
# dns wireformat
curl -vH 'accept: application/dns-message' 'https://doh.chi.mpls.rsvp/dns-query?name=www.forwardingplane.net&type=AAAA'  | hexdump -c
```
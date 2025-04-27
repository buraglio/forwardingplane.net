
---
title: 'Developing and publishing a new IPv6 documentation prefix'
date: '2024-12-21'
author: buraglio
layout: post

categories:
    - IPv6
    - IETF
tags:
    - IETF
    - IPv6
---


One of the reasons for lack of blog post publishing is that my attention has been focused fairly heavily on working within the IETF. Toward the beginning of the COVID pandemic, the US Government published a new initiative - [M-21-07](https://www.whitehouse.gov/wp-content/uploads/2020/11/M-21-07.pdf), which requires the migration of all federally owned systems to IPv6-only. What does "IPv6-only" mean, you may ask. Well, that's kinda nebulous. People define it in varying levels of extremism, I've chosen to define it as "a device that can operate without the use of IPv4 configured".
Now, as those of us working on this got deeper and deeper into turning off legacy IP, we started uncovering details ranging from little annoyances to major issues, most of which were hidden by the presence of legacy IP in a dual-stacked environment. However, one thing that was pretty obvious pretty quickly was the lack of a documentation prefix that was large enough to accommodate the current state of address and network planning.

And so the effort to define a new documentation space began.

Now, working ion the IETF is a developed skill that takes a lot of diplomacy, a good amount of knowledge of the system, an understanding of the technology, and patience. I once presented on IPv6 migration and referenced a very specific quite from the fantastic movie ["The Shawshank Redemption"](https://www.imdb.com/title/tt0111161/):

Patience and time.  

This kind of progress is no different. After a couple of years of work, we emerged with [RFC9637](https://datatracker.ietf.org/doc/rfc9637/), which allocates `3fff::/20` in addition to the existing `2001:db8:/32` allocated in [RFC3849](https://datatracker.ietf.org/doc/rfc3849/). So go forth, design large networks, and use `3fff::/20` in your documentation - stop using GUA space!
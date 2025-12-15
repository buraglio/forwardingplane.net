---
id: 330
title: 'Alternate model for Service Provider networks; or how to keep net neutrality intact'
date: '2013-01-22T23:34:38-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=330'
permalink: /2013/01/22/alternate-model-for-sp-networks/
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'Net Neutrality, ISP, Service Provider, Open Access Network, FTTP, FTTH, UC2B, BGP'
themeblvd_title:
    - 'Limitless bandwidth in a metered world.'
themeblvd_description:
    - 'Local peering points are a good way to stave off the transit providers from metering all of the content that consumers want to see. Let''s re-think how we do internet service delivery. '
Views:
    - '60'
categories:
    - Musings
    - NSP
tags:
    - NSP
    - 'Service Provider'
---

There has been a lot of buzz about the service provider model, [net neutrality](http://en.wikipedia.org/wiki/Net_neutrality) and tiered access for consumers in the past few years.  Just this week [Google has been accused of paying Orange](http://www.theverge.com/2013/1/19/3894182/french-isp-orange-says-google-pays-to-send-traffic) (more likely Orange is forcing google) for handling its traffic.  This is a VERY slippery slope that teeters on the edge of what we all want to avoid as consumers or content creators.
This recent story has sparked something I've been thinking about for a very long time.
Rewind to 1999.
I worked for a small, regional broadband provider what seems like a lifetime ago, back when broadband was new and shiny and not terribly common.  We provided ATM based DSL, T1, ISDN and on some occasions dry copper gorilla net access to southern Chicago communities, Champaign-Urbana, IL, Danville, IL, Kankakee, IL,  a bit of west Indiana and a handful of small communities in between.  It was a proving ground for a young, motivated networking guy.  I was the senior network engineer, technical lead and for a while had a handful of direct report employees and students. This was where I really cut my teeth with routing, switching, content delivery and service levels.
I ended up leaving there and moving on to work on a lot of HPC work and bleeding edge WAN stuff (think n x 10Gbps across the country in 2003).  However, one thing I took away from that ISP job was something that wasn't really a new idea as much as just a uniquely positioned service and a good idea.  There was this local POP connection run by the university that allowed for exchange of  routes between any network that could pay the local loop charge.  It was a way to get cheap, fast access to anything local.  Unmetered, unfiltered.  Exchange any routes you want (that you own), take whatever routes you need.
This was a clever model because down where we are located, 2.5 hours south of Chicago, transit bandwidth wasn't (and isn't) cheap.  Every local provider connected as did the community hospital, the university and a handful of others.  We took FULL advantage of fast connectivity between each other and all saved on transit bandwidth.  [This kind of thing has been in place in the R&E](http://en.wikipedia.org/wiki/National_research_and_education_network) community for far longer than I've been around.
Fast forward 11 years.
I'm still a huge fan of bi-lateral BGP peerings.  I want as many as I can get.  As a service provider I want a default free network with a lot of peers in many geographically diverse locations.
I propose a [not-so]new model for service providers.  Create peering points, meet me routers.  Allow any network to connect for a port fee and exchange local routes.  Make these local routes free, unlimited and unfiltered (do your proper capacity planning, of course).  Opening up exchanges promotes better, diverse paths to resources and allows for a better overall user experience.
Data is where the telecom companies make their money nowadays.  Net Neutrality is constantly in the news and in danger of being compromised.  Tiered services are everywhere.  I understand the need to meter service.  I did the ISP thing, I know that 5% of the users use 80% of the bandwidth.  That's not new either.  I challenge larger service providers to think about it in a new way, though.  We're making it work.  It's a smaller scale, but it works.  I think it can scale if architected correctly.  It may have more operational overhead, but I suspect it can also command a bit more in price.  It could also allow for the non-asterisked use of the word "unlimited", so marketing guys will love it.
Is it more engineering? Sure.  Is it harder to manage? Maybe, but likely not harder than architecting around content providers that don't want to pay.  It is a better idea and promoting better service for both content providers and consumers of their service than making content providers pay for transit?  Absolutely.
We're doing this on [UC2B](http://uc2b.net). It played a part in winning us the [Community Broadband Project of the Year award from the NATOA](http://www.natoa.org/2012/09/natoa-announces-recipients-of-4.html).  It's a good idea.
 
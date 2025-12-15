---
id: 1506
title: 'DNS – the treasure trove of information your ISP can see'
date: '2018-12-10T04:23:42-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1506'
permalink: /2018/12/10/dns-the-treasure-trove-of-information-your-isp-can-see/
Views:
    - '582'
categories:
    - How-To
    - Musings
    - Security
    - UNIX
tags:
    - DNS
    - Privacy
    - ZeroTier
---


In recent years, the nature of [privacy on the internet](http://fortune.com/2017/11/23/net-neutrality-explained-what-it-means-and-why-it-matters/) has become a very important topic amongst those concerned with the now lack of [net neutrality](https://www.theverge.com/2017/12/14/16776154/fcc-net-neutrality-vote-results-rules-repealed). The de-facto mechanism for dealing with privacy has been to "[SSL all the things](https://letsencrypt.org/)", which I am very much in favor of. What many do not realize, though, is that simply using SSL for the traffic that transits a given ISP still leaves a wealth of thick, rich, delicious personal data still easily available to your ISP to harvest, sell, and do with as they please. This data comes in the form of DNS queries. DNS is the nearly-always-forgotten, crucial aspect of how the internet functions. Without DNS, nothing works. Everything appears broken and manifest as what appears to be a networking problem. ISPs typically provide what is called a [recursive resolver](https://umbrella.cisco.com/blog/2014/07/16/difference-authoritative-recursive-dns-nameservers/), which for most people is handed down by a local provider to the customer premise equipment (CPE; usually a modem or optical terminal of some kind) that they install at a residence. This CPE then hands that resolver to your clients that use it to - you guessed it - recursively resolve DNS queries. These queries can be logged and then mined for browsing habits, etc. Anyone that has ever done any network forensics will know straight away that the value of the information contained in DNS query logs is very, very high. 


What this means is that even though a privacy conscious individual is hiding the bulk of their content in SSL, meaning the bulk of what they’re reading, searching for, and doing, is encrypted, the requests for that content or activity is not. For example, an ISP can potentially see that a client is making many, many queries for $onlineshopping.com and begin selling that data to advertisers. If you think they’re not doing this now, [think again](https://www.wired.com/story/can-verizon-build-a-strong-brand-from-the-bones-of-yahoo-and-aol/). 


Great, so $bigbadprovider can see your queries. There are a number of pretty good ways to work around this, and [one of my favorite projects](https://pi-hole.net/) handily deals with one of them with great simplicity. What I am referring to is the newly popular [DNS over HTTPS](https://scotthelme.co.uk/securing-dns-across-all-of-my-devices-with-pihole-dns-over-https-1-1-1-1/), which is supported by the [cloudflare 1.1.1.1 service](https://one.one.one.one/). 


So, as a thought experiment I decided to play Reeses Peanut butter and chocolate with two of my favorite technological creations: the aforementioned PiHole, and [ZeroTier](https://zerotier.com/). Now anyone that isn’t familiar with ZeroTier, you should acquaint yourself - Packet Pushers did a good[ podcast on it back in November of 2017](https://packetpushers.net/podcast/pq-134-meet-zerotier-open-source-networking/). It’s functionally an encrypted overlay supporting dual stack networking with auto configuration and gateway capabilities, and it runs on almost everything. I love this overlay technology and have been using it for a while - highly recommended.


Back to my peanut butter and chocolate experiment. So, given that I had an existing ZeroTier network and an existing PiHole setup at home, I went over to [Vultr.com](https://www.vultr.com/?ref=7692870) and spun up a small VM for $3.50/mo, integrated it into my fleet with my Ansible and Salt tools, and installed ZeroTier and Pihole. From there I set up this DNS hierarchy. 


![](https://docs.google.com/drawings/d/e/2PACX-1vS-DsmzNWvE335KZtNo6AHX3SySG-VQWhK7i9sNgT6mFMHC5VzRWtMuJg5JraU2dJTFQT4QIGnfaMFP/pub?w=960&h=720)


What this buys me is a fully encrypted DNS path up through the Vultr.com VM host without modifying the underlying DNS transport. And it works surprisingly well. I ran SmokePing from two hosts - both leveraging ZeroTier to do their testing, one on my local network and one in the cloud - to measure latency for a few days before I did this and kept that running after the deployment. Now, it’s not perfect but my family and I have been using this for about a month with minimal issues. Once in a great while we’ll see some slow DNS resolution time, but overall it works fairly well. 


 


![Resolver Queries](https://www.forwardingplane.net/wp-content/uploads/2018/12/Resolver-Queries.png)


**My take **


The idea of using a public resolver kinda bothers me, I realize it’s probably unfounded, but I know how to and have run resolvers for ISPs and organizations for like 20 years, so I have the burden of knowledge about what is in the logs and how to run my own. Using a secured recursive resolver is simply trading transit privacy for lack of query privacy somewhere else. Then there is the issue of content networks that use DNS queries to take you to the best / topologically closest cache of their content [NOTE: this, along with the forensics data for debugging potential security issues is a **top** reason that all ISPs should run their own resolvers]. I fully realize that a normal end user running their own resolver is unlikely and that this deployment is a bit overkill. However, as I can demonstrably prove, it works. And it works pretty well. It also has the added bonus of allowing me to have internal DNS resolution of my own hosts and any mobile ZeroTier client. Is it for everyone? No way. Does it prove viability for low/medium traffic use? Sure. The point is really just to get folks thinking about information leaking that they may not have considered. The nature of the internet makes true privacy pretty much impossible, but there are a few ways to make your data a little harder to for companies to compile and capitalize on if you truly don’t want them to. 

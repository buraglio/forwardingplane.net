---
id: 2363
title: 'It’s always MTU, unless it’s DNS'
date: '2020-05-04T03:48:00-05:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2363'
permalink: /2020/05/04/its-always-mtu-unless-its-dns/
Views:
    - '2800'
image: /wp-content/uploads/2020/05/DNS_Quad8_IPv4_mini.png
categories:
    - How-To
    - UNIX
tags:
    - DNS
    - ISP
    - Linux
---

One of the most common questions I hear from small and even medium sized ISPs is “why should I run my own DNS resolver(s)?” The perception that DNS is hard, complicated, or even unnecessary is often cited as a reason to just farm it out to one of the “free” anycast resolver services available across the internet. Now, there are many reasons to be wary of DNS, both from the professional and the consumer side - it is a huge treasure trove of personal  information about behavior, and is easily monitized by entities large enough to consume and process it. I’ve even[ written about sidestepping your providers DNS](https://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/) all together (although my experiment, which lasted a bit over a year, was a tad more controlled than simply hacking DoH into my system and moving to an anycast resolver service.

As an ISP, there are So. Many. Reasons. To run your own DNS systems (both recursive resolvers and authoritative systems). Just to rattle off a few:


    - Control your PTR (reverse lookups) locally - you need these wether you know it or not
    - Ability to log queries - very helpful for determining bad actor behavior on your network
    - Availability to use [DNS RPZ](https://dnsrpz.info/) - Response policy zones allow you to do a handful of things, not the least of which is filtering known bad actor domains.
    - Keeping your data as local as you can - this is where I am really going to focus here.


Now, these definitely aren’t the only reasons, but they’re pretty important. I will focus on the last one here because it pertains to my crude little project I call the [DNS latency monitor](https://dns.qosbox.com). Authoritative and recursive is a topic for another post in and of itself. To understand where I am going, it is probably best to understand my perspective.

There is an old networking adage -* “It’s always MTU, unless it’s DNS*”. DNS is the single most non-networking protocol that causes the most networking pain. It will ***always*** be up to networking prove that a DNS issue is not a networking problem, and this is true ten fold when it comes to ISPs. The customer - or Carol in payroll - does not care what is broken, they just know something does not work.

They can’t get to google. They cannot get email. Netflix won’t stream. **The internet is broken**. ***Broken DNS makes the network functionally broken for an average user.*** DNS is like BGP. You have to have it for the internet as we know it work. Why anyone would want to outsource something that high visibility is beyond me, but I do understand that resources are hard to come by in small ISP shops, and that many blogs have encouraged the use of DoH for the end user to side step provider based resolvers (and for those that don’t know, even [Comcast provides a DoH option](https://dnsprivacy.org/wiki/display/DP/DNS+Privacy+Public+Resolvers#DNSPrivacyPublicResolvers-DNS-over-HTTPS(DoH))). In my opinion (and experience) this is a mixed bag of cats and razor blades. Small providers aren’t likely to sell off your browsing data. The big providers that are using it are the ones you can not change - cellular devices. While on cellular most of not all devices / providers do not allow you to change from their on-net resolvers. This is of particular interest for two reasons:


    - At least one of the large US providers owns a company that literally analyzes this data for use
    - Cellular devices comprise a *<em>huge*</em> amount of the active devices on the internet (we’ll save the smug IPv6 network deployment talk about this fact for another day).


So really, an average user changing this data on their home network but still carrying around a smartphone is really closing a door but leaving the windows wide open. Yes, I do realize there are apps that account for this, but none are seamless and your mom is almost certainly not going to use it.

The ironic thing here is that DNS is actually quite easy to run. It is true that in the early days bind was a bit of a bear (most of that has changed, and it’s still the most feature rich). That has largely changed with the introduction of so many solid DNS resolvers. [Unbound](https://nlnetlabs.nl/documentation/unbound/), for example, is lightweight, very feature complete, super well documented, and incredibly easy to install. It will also happily run on very low powered machines.

Where is this meandering nonsense all going, you might ask? It’s going to the anycast DNS latency logging “service” that came to life at the beginning of the US COVID-19 shelter in place. I wanted to see what changed, if anything, from a customer quality of experience perspective. What was learned was that a single DNS query to an outside system can add a noticeable amount of latency RTT to *every. single. request.* that a customer makes. As a service provider not running your own recursive resolvers, imagine a 120ms pad on every web page requested. Now imagine that across every subscriber. Then imagine the anycast system closest to you goes down, and you’re hitting the next one over. Every single DNS request and response is now at the mercy of the internet at large. Totally out of your control, because you neither control the entire path, and have zero input as to how that service is being run.

Running your own resolver is straightforward, fairly easy and lets you take back some of that control.

![Screen Shot 2020 05 03 at 10 23 38 PM](https://forwardingplane.net/wp-content/uploads/2020/05/Screen-Shot-2020-05-03-at-10.23.38-PM.png)

As a customer not wanting to use an ISPs resolver, you can also consider that you’re freely handing over all of the DNS queries you make to a company that can and does (in some cases) monetize it.

So what does this thing really do? It’s quite simple, actually. It’s a run of the mill [smokeping](https://oss.oetiker.ch/smokeping/) master-slave install. Why smokeping? Check out the[ project front page](https://dns.qosbox.com) and it’ll explain. In order to most closely mimic a user experience, it currently runs 16 DNS query tests for the same DNS name and reports the RTT back from the anycast resolver closest to it, then smokeping does what smokeping does - it records it. So far it has been a good litmus test for how the largest of the anycast recursive resolvers behave from any given point of view. Sometimes it’s great, sometimes it’s not. This is useful data not just for the smaller ISPs that may be using them, but also for anyone trying to pick out and troubleshoot different performance or DNS issues. There are certainly commercial tools that do this, but none the that I have seen are freely available to both use and participate in, while also providing a consistent, long term interface into the data. I am, as always, happy to be corrected in that regard.

I plan to keep this running as long as folks keep providing test points. It’s a very lightweight install and is totally controlled by the master system, so once you get it installed, it’ll just run. Many of these probes run on linux containers, raspberry pi systems, or other lightweight unix environments. If you’re interested in providing a probe on the DNS latency monitor project, please reach out and[ contact me. ](mailto:buraglio+dns@forwardingplane.net)I am currently looking for probes in:


    - Hawai'i
    - Guam
    - Australia (both coasts and Taz)
    - Singapore
    - India
    - Canada (anywhere)
    - Iceland
    - Greenland
    - Mexico
    - Any and all countries in Central and South America
    - Japan
    - Eastern Europe
    - Ireland
    - UK
    - Any Caribbean islands
    - Anywhere in Africa


If you’re ready to dive into running a set of DNS recursive resolvers for your environment, here are some simple instructions, you can check out everything you should need to get a basic install up and running [here](https://github.com/buraglio/unbound-setup).
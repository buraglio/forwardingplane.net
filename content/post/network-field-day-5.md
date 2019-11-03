---
title: 'Network Field Day 5 - Participate Remotely'
date: Wed, 06 Mar 2013 14:59:05 +0000
draft: false
tags: [Crystal Ball, Musings, OpenFlow, Routing, SDN]
---

Last year, [Networking Field Day](http://techfieldday.com/event/nfd5/) was something that I'd heard of but wasn't really aware of what is really was.  I occasionally looked at Twitter and saw the hash tags but did not know much about how it was set up or what it was about.  In fact, I actually thought it was supposed to be like the HAM radio field day stuff where you go out and build out an emergency network on the fly.  OK, I should have done more homework, admittedly. Fast forward 6 months. I'm working more and more with [Brent Salisbury](http://www.networkstatic.com) on day job stuff and he's encouraging me to brush the dust off of my [old blog](http://www.forwardingplane.net) (which became this site). I'm working more on [OpenFlow](http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/ "Building a Floodlight OpenFlow controller on CentOS 6"),  virtualization stuff like [KVM](http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/ "CentOS KVM Install – Quick Start to a VM"), [VirtualBox](http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/ "Headless VirtualBox host on CentOS") and [VMware](http://www.vmware.com) and bringing up 100G WAN links.  I even had the extremely cool opportunity to do a [Packet Pushers Podcast](http://packetpushers.net/show-131-golf-cart-in-my-fibre-tunnel/). Many of these things are a direct result of becoming more engaged in the larger community, a networking community I had pretty much carved myself out of back in 2002 when I left the service provider world for R&E.  This self isolation was a bit of an oversight on my part. What I did not realize was that, as someone in R&E, I had a unique perspective on some of the industry products and direction and was often seeing things a lot sooner than the general enterprise world. As I got more and more engaged I realized that there were a **lot** of great folks out there that like to collaborate, share and write about their professional experiences in our field of choice.  These same people were doing innovative and interesting things that I didn't know about.  [NFD](http://techfieldday.com/event/nfd5/) was one of those things.  So, I started to write down more of the things I was thinking and doing.  I figured that at least someone would find them useful or interesting or at least fodder for solving insomnia.  When I was asked to participate and come out to NFD5, I was both ecstatic and humbled at the same time.  This was the place where the networking industry thought leaders go to convene and discuss directionality as well as current networking technologies. Just to relay the scale and scope of the folks involved, here is the list of delegates for NFD5:  

[![http://techfieldday.com/wp-content/uploads/2012/08/Carroll-wpcf_60x60.jpeg](http://techfieldday.com/wp-content/uploads/2012/08/Carroll-wpcf_60x60.jpeg "http://techfieldday.com/wp-content/uploads/2012/08/Carroll-wpcf_60x60.jpeg")](http://techfieldday.com/delegate/brandon-carroll/)

[Brandon Carroll](http://techfieldday.com/delegate/brandon-carroll/)

[@BrandonCarroll](http://twitter.com/BrandonCarroll)

CCIE Instructor, Blogger, and Technology Enthusiast

[![http://techfieldday.com/wp-content/uploads/2012/08/brent-salisbury1-wpcf_60x60.jpeg](http://techfieldday.com/wp-content/uploads/2012/08/brent-salisbury1-wpcf_60x60.jpeg "http://techfieldday.com/wp-content/uploads/2012/08/brent-salisbury1-wpcf_60x60.jpeg")](http://techfieldday.com/delegate/brent-salisbury/)

[Brent Salisbury](http://techfieldday.com/delegate/brent-salisbury/)

[@NetworkStatic](http://twitter.com/NetworkStatic)

Brent Salisbury works as a Network Architect, CCIE #11972.

[![http://techfieldday.com/wp-content/uploads/2012/08/cmcnamara-headshot-2011-color-scaled-wpcf_42x60.jpg](http://techfieldday.com/wp-content/uploads/2012/08/cmcnamara-headshot-2011-color-scaled-wpcf_42x60.jpg "http://techfieldday.com/wp-content/uploads/2012/08/cmcnamara-headshot-2011-color-scaled-wpcf_42x60.jpg")](http://techfieldday.com/delegate/colin-mcnamara/)

[Colin McNamara](http://techfieldday.com/delegate/colin-mcnamara/)

[@ColinMcNamara](http://twitter.com/ColinMcNamara)

Colin McNamara is a seasoned professional with over 15 years experience with network and systems technologies.

[![http://techfieldday.com/wp-content/uploads/2012/08/ethan-banks-headshot-500x667-wpcf_44x60.jpg](http://techfieldday.com/wp-content/uploads/2012/08/ethan-banks-headshot-500x667-wpcf_44x60.jpg "http://techfieldday.com/wp-content/uploads/2012/08/ethan-banks-headshot-500x667-wpcf_44x60.jpg")](http://techfieldday.com/delegate/ethan-banks/)

[Ethan Banks](http://techfieldday.com/delegate/ethan-banks/)

[@ECBanks](http://twitter.com/ECBanks)

Ethan Banks, CCIE #20655, is a hands-on networking practitioner who has designed, built and maintained networks for higher education, state government, financial institutions, and technology corporations.

[![http://techfieldday.com/wp-content/uploads/2012/08/Ferro-wpcf_60x39.jpg](http://techfieldday.com/wp-content/uploads/2012/08/Ferro-wpcf_60x39.jpg "http://techfieldday.com/wp-content/uploads/2012/08/Ferro-wpcf_60x39.jpg")](http://techfieldday.com/delegate/greg-ferro/)

[Greg Ferro](http://techfieldday.com/delegate/greg-ferro/)

[@EtherealMind](http://twitter.com/EtherealMind)

Over the last twenty odd years, Greg has worked Sales, Technical and IT Management but mostly he delivers Network Architecture and Design. Today he works as a Freelance Consultant for F100 companies in the UK & Europe focussing on Data Centres, Security and Operational Automation.

[![http://techfieldday.com/wp-content/uploads/2012/09/johnherbert-wpcf_60x60.jpeg](http://techfieldday.com/wp-content/uploads/2012/09/johnherbert-wpcf_60x60.jpeg "http://techfieldday.com/wp-content/uploads/2012/09/johnherbert-wpcf_60x60.jpeg")](http://techfieldday.com/delegate/john-herbert/)

[John Herbert](http://techfieldday.com/delegate/john-herbert/)

[@MrTugs](http://twitter.com/MrTugs)

John has worked in the networking industry for 14 years, and obtained his CCIE Routing & Switching in early 2001.

[![http://techfieldday.com/wp-content/uploads/2013/02/profile_picture-wpcf_52x60.jpg](http://techfieldday.com/wp-content/uploads/2013/02/profile_picture-wpcf_52x60.jpg "http://techfieldday.com/wp-content/uploads/2013/02/profile_picture-wpcf_52x60.jpg")](http://techfieldday.com/delegate/jon-langemak/)

[Jon Langemak](http://techfieldday.com/delegate/jon-langemak/)

[@blinken\_lichten](http://twitter.com/blinken_lichten)

Jon Langemak is a Network Engineer, tech blogger, and dedicated tech enthusiast.

[![http://techfieldday.com/wp-content/uploads/2012/08/OBrien-wpcf_60x60.jpeg](http://techfieldday.com/wp-content/uploads/2012/08/OBrien-wpcf_60x60.jpeg "http://techfieldday.com/wp-content/uploads/2012/08/OBrien-wpcf_60x60.jpeg")](http://techfieldday.com/delegate/josh-obrien/)

[Josh O’Brien](http://techfieldday.com/delegate/josh-obrien/)

[@JoshOBrien77](http://twitter.com/JoshOBrien77)

Josh has worked in the industry for 14 years and is now serving as CTO in the Telemedicine sector.

[![http://techfieldday.com/wp-content/uploads/2012/08/IMG_0264-002-wpcf_60x60.jpg](http://techfieldday.com/wp-content/uploads/2012/08/IMG_0264-002-wpcf_60x60.jpg "http://techfieldday.com/wp-content/uploads/2012/08/IMG_0264-002-wpcf_60x60.jpg")](http://techfieldday.com/delegate/paul-stewart/)

[Paul Stewart](http://techfieldday.com/delegate/paul-stewart/)

[@PacketU](http://twitter.com/PacketU)

Paul Stewart is a Network and Security Engineer, Trainer and Blogger who enjoys understanding how things really work.

[![http://techfieldday.com/wp-content/uploads/2013/02/DSC6539smaller2-wpcf_60x47.jpg](http://techfieldday.com/wp-content/uploads/2013/02/DSC6539smaller2-wpcf_60x47.jpg "http://techfieldday.com/wp-content/uploads/2013/02/DSC6539smaller2-wpcf_60x47.jpg")](http://techfieldday.com/delegate/pete-welcher/)

[Pete Welcher](http://techfieldday.com/delegate/pete-welcher/)

[@pjwelcher](http://twitter.com/pjwelcher)

Pete is a 15+ year CCIE who loves network design, and is currently avidly learning various datacenter technologies.

[![http://techfieldday.com/wp-content/uploads/2012/08/Slattery-wpcf_60x50.jpg](http://techfieldday.com/wp-content/uploads/2012/08/Slattery-wpcf_60x50.jpg "http://techfieldday.com/wp-content/uploads/2012/08/Slattery-wpcf_60x50.jpg")](http://techfieldday.com/delegate/terry-slattery/)

[Terry Slattery](http://techfieldday.com/delegate/terry-slattery/)

Terry Slattery, CCIE #1026, is a senior network engineer with decades of experience in the internetworking industry.

[![http://techfieldday.com/wp-content/uploads/2012/08/bwry5mviq6ss0pe6m517-wpcf_46x60.png](http://techfieldday.com/wp-content/uploads/2012/08/bwry5mviq6ss0pe6m517-wpcf_46x60.png "http://techfieldday.com/wp-content/uploads/2012/08/bwry5mviq6ss0pe6m517-wpcf_46x60.png")](http://techfieldday.com/delegate/tom-hollingsworth/)

[Tom Hollingsworth](http://techfieldday.com/delegate/tom-hollingsworth/)

[@NetworkingNerd](http://twitter.com/NetworkingNerd)

Tom Hollingsworth, CCIE #29213, is a Senior Solutions Architect for a small VAR focusing primarily on K-12 education.

In addition to the above folks, [Steven Foskett](http://blog.fosketts.net), who is as prolific of a tech writer as he is experienced in the industry holds it all together and brings it to the public. The list of vendor participants is also deep.  [Cisco](http://www.cisco.com), [Juniper](http://www.juniper.net), [Ruckus Wireless](http://www.ruckuswireless.com), [Plexxi](www.plexxi.com/), [Brocade](www.brocade.com/) and [SolarWinds](http://www.solarwinds.com) are all on the docket. Unfortunately for me, I was not able to attend due to work scheduling and coordination of family stuff, something I truly lament.  To think that I was even considered to be on that list is truly humbling and something I'm very proud of. Not being able to attend, I wanted to participate as much as I could, so I started looking around and talking to folks and found the link to the live feed as well as the Twitter hashtag. It seems like a good idea to put this out there to as many folks as possible to not only bring attention to the fact that this is happening, but that you can participate from wherever you are.  I would encourage anyone who reads this and is interested in Networking as a profession, or is already in our industry, to pay attention to the Tech Field Day events.  Watch the live stream.  Ask questions and make comments on Twitter via the hashtag [#NFD5](https://twitter.com/search?q=%23NFD5).  Get involved. During the event you should be able to do a live stream from right inside this post or from the [NFD5 page](http://techfieldday.com/event/nfd5/).
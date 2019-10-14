---
title: 'SDN across domains in the WAN - a novice look'
date: Tue, 27 Nov 2012 05:04:00 +0000
draft: false
tags: [Musings, OpenFlow, SDN, SDN, WAN]
---


#### 
[Brent Salisbury](http://www.blogger.com/profile/16141388907060749402 "noreply@blogger.com") - <time datetime="2012-11-28 04:59:44">Nov 3, 2012</time>

Nice thoughts Nick. The SP is moving quickly on this. You keyed in on the part that is such a question mark. How do inter-domain exchange information safely and usefully. Good thing is the content providers have been doing similar things for a long time. When I click post your site will do an OAUTH to Google. APIs and open source might be the ticket. Awesome post.
<hr />
#### 
[billowens]( "owens.bill@gmail.com") - <time datetime="2012-12-10 10:10:54">Dec 1, 2012</time>

This is a good description of the breadth of the problem, but there are places where it is very, very deep. Your description is focusing on one possible outcome, just talking about building Layer 2 circuits between two (or more) networks. Do you think that's a worthwhile end, or are you thinking about true 'SDN peering' that would include some degree of delegated control of network elements as well? As a network engineer I might be satisfied with a simple Ethernet VLAN, but a researcher's application could require the installation of specific flow rules on every port along my path. And I would make the claim that past history has demonstrated the difficulty of even the simple VLAN model. To date, the serious efforts to implement some kind of multi-domain dynamic circuit networking in the R&E world have fallen into two categories: a dynamic core surrounded by static, manually-configured access networks, or a federation of networks managed by a single control plane, with all the participants subject to the central authority. Both of those models have been proven to work and to have a level of complexity that, while perhaps not optimal, is within our grasp. I'm not at all sure that the fully-generic model of interoperating autonomous circuit networks is really practical; perhaps if the set of services is made so simple and straightforward that it reduces to a lowest common denominator. The holy grail of peering between multiple autonomous networks that allows full programmability of the resultant path is something that I think will remain a distant dream.
<hr />
#### 
[Most popular posts of 2012 | The Forwarding Plane](http://www.forwardingplane.net/2013/01/294/ "") - <time datetime="2013-01-02 00:05:30">Jan 3, 2013</time>

\[...\] post on Plexxi and the post on SDN across the WAN are also pretty popular and both are subjects I will likely revisit as time \[...\]
<hr />
#### 
[Bill Z Walton](http://BillZWalton "rfreyqjdslw@gmail.com") - <time datetime="2013-02-12 16:04:28">Feb 2, 2013</time>

Today, I went to the beach with my kids. I found a sea shell and gave it to my 4 year old daughter and said "You can hear the ocean if you put this to your ear." She placed the shell to her ear and screamed. There was a hermit crab inside and it pinched her ear. She never wants to go back! LoL I know this is totally off topic but I had to tell someone!|
<hr />
#### 
[Software defined Networking for the service provider WAN](http://www.forwardingplane.net/2013/01/sdn-across-the-wan-part-deux-primitives/ "") - <time datetime="2013-01-10 21:20:40">Jan 4, 2013</time>

\[...\] been lamenting about the SDN WAN options for a while now.  Having SDN/OpenFlow in a data center or campus is relatively well \[...\]
<hr />

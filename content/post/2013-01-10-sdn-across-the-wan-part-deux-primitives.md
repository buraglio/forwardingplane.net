---
id: 350
title: 'SDN Across the WAN, part deux.  Primitives.'
date: '2013-01-10T21:18:47-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=350'
permalink: /2013/01/10/sdn-across-the-wan-part-deux-primitives/
themeblvd_title:
    - 'Software defined Networking for the service provider WAN'
themeblvd_noindex:
    - 'true'
themeblvd_description:
    - 'How can enterprises, campus and end users utilize software defined networking across the service provider wide area?  This article aims to start the process of vocalizing the potential pieces needed to plumb SDN across multiple administrative domains. '
themeblvd_keywords:
    - 'SDN, OpenFlow, Service Provider, WAN, Wide Area, MPLS, GMPLS, BGP, Nick Buraglio, Brent Salisbury'
Views:
    - '90'
categories:
    - Musings
    - SDN
---

I've been <a title="SDN across domains in the WAN – a novice look" href="http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/" target="_blank" rel="noopener noreferrer">lamenting about the SDN WAN</a> options for a while now.  Having SDN/OpenFlow in a data center or campus is relatively well documented and already widely deployed.  Google has been doing SDN across their private WAN in production.  These pieces are easy.  What isn't easy is the ability to plumb SDN across many domains that are under disparate control.   This part is hard. What is lacking is a fundamental framework, or set of primitives to build from.  As an example, how does one build a SDN path across this:
&nbsp;
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/01/SDN-Reference-Architecture-Sanitized.png"><img class="aligncenter size-full wp-image-351" title="SDN Reference Architecture -Sanitized" src="http://www.forwardingplane.net/wp-content/uploads/2013/01/SDN-Reference-Architecture-Sanitized.png" alt="" width="470" height="704" /></a>
First I think we need to define what we want out of the SDN path.  A reserved bandwidth allocation?  A Layer2 path?  Flow instantiation across the entire path?  The first two have a least common denominator.  The third is hard, especially if the path transits a segment with no SDN capability.
This piece is making my brain hurt.  There seems to be a lot of early work on this, <a href="http://events.internet2.edu/speakers/speakers.php?go=people&amp;id=2865">Inder Monga</a> from <a href="http://www.es.net">ESnet</a> has been working at making this happen, and I think he's the closest from what I've seen in my searching and researching.   I want to know how to do this across <strong>all</strong> networks.   I want to see the future of carrier WAN connectivity, to taste the unicorn milk.
The methodology so far has been to break this down into small black boxes.  After doing that, I realized that there is going to have to be a common protocol.  The least common denominator to all of this is the SDN.  It doesn't much matter what that SDN is as long as there is a central controller.  It can be OpenFlow, <a href="http://www.es.net/services/virtual-circuits-oscars/" target="_blank" rel="noopener noreferrer">OSCARS</a>, <a href="http://en.wikipedia.org/wiki/Generalized_Multi-Protocol_Label_Switching" target="_blank" rel="noopener noreferrer">GMPLS</a>, <a href="http://ext.delaat.net/olex/index.html" target="_blank" rel="noopener noreferrer">Open LightPath Exchange</a>, whatever.  It doesn't matter.  They all need a controller.  Within those controllers there needs to be "an energy field created by all SDN. It surrounds us and penetrates us; it binds the galaxy together".  Yes, I like Star Wars.
So, how would one do this?  It would be ideal, to me at least, if there was a standard set of protocols that all of these controllers could speak.  This standard communication could be as simple as how a BGP peering functions.  Site A has a controller, it "peers" with it's upstream and announces its capabilities.
For example,
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/01/SDN-peering.png"><img class="aligncenter size-full wp-image-352" title="SDN peering" src="http://www.forwardingplane.net/wp-content/uploads/2013/01/SDN-peering.png" alt="" width="591" height="740" /></a>
All of these peers exchange capability information and pass it on with a standardized set of language and a location identifier (think ASN and route announcements).  To me this appears to be the lowest hanging fruit. I'm not a developer but there doesn't seem to be to be any reason that this couldn't be built into any controller, commercial or opensource. That way, regardless of vendor, SDN implementation or capabilities everyone can create a SDN path based on the available implementations upstream. Of course, there would need to be a "multihop" option for those that have to upstream SDN paths. In this case something like a GRE tunnel could be the lowest common denominator. This would have to transcend OpenFlow and be a true "SDN" at the fundamental level to actually work, but it needs to take into account managing the flow table of networks outside of a given administrative domain. As a starting point, here is the framework I came up with:
<ul>
	<li>Reliable transport: TCP</li>
	<li>Authentication method: MD5 Capabilities exchanged:</li>
	<li>Number of circuits</li>
	<li>Types of SDN (MPLS, VLAN, DWDM Waves, OpenFlow Version, Flow manipulation)</li>
	<li>Bandwidth per circuit (if applicable)</li>
	<li>Duration of circuit or flow (path TTL, permanent?)</li>
	<li>Path validation (to ensure end to end connectivity over negotiated methodology)</li>
</ul>
I've been talking a lot with <a href="http://www.networkstatic.net/" target="_blank" rel="noopener noreferrer">Brent Salisbury</a> about this.  I know folks are thinking about it.  Bill Owens<a href="http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/#comment-47"> had some great comments</a> to my last post regarding this and I think he's totally spot on.  However, I want to hit 88mph in my Delorean and see the future.  I think it's a ways way off but someone needs to come up with this framework.  SDN is so disjointed that it needs a one ring.  Controlling the forwarding plane of someone else network is scary and needs to have a leash on it.  Building this standard protocol could be it.  Unfortunately, I am no developer but I do know a little bit about running a decent sized network.  There will need to be safeguards, policy and knobs to tweak.  I keep coming back to BGP.  It's not as much of a routing protocol as it is a policy framework disguised as a routing protocol.  There needs to be something similar with SDN.
I'm going to continue to think through this publicly and I welcome constructive input.
&nbsp;
&nbsp;
<strong>EDIT</strong>:  <a href="https://datatracker.ietf.org/doc/draft-ietf-alto-protocol/" target="_blank" rel="noopener noreferrer">ALTO</a> is pretty close.  There has been a lot of work going on but I don't think it's all the way to where we need it to be.  Some interesting proof of concept and detail stuff can be read <a href="http://www.ewsdn.eu/presentations/ALTOwrtSDN.pdf" target="_blank" rel="noopener noreferrer">here</a> and <a href="http://opennetsummit.org/talks/ward-wed.pdf" target="_blank" rel="noopener noreferrer">here</a>.
<pre></pre>
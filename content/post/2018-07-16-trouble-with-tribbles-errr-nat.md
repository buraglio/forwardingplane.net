---
id: 1471
title: 'Trouble with Tribbles &#8230;..errr NAT'
date: '2018-07-16T04:24:00-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1471'
permalink: /2018/07/16/trouble-with-tribbles-errr-nat/
Views:
    - '242'
categories:
    - IPv6
    - Musings
    - Security
---

<div>As a follow up to my <a href="https://www.forwardingplane.net/2018/06/nat-discussions/">last post</a>, I wanted to dive a little deeper into the world of address translation and to suss out some of the more compelling details.</div>
<div>As I've said on many occasions, it pains me to see NAT referenced as a security mechanism. That said, where PNAT can be beneficial is in an overall privacy strategy, however, even that is comparatively low value and given the current state of global IPv4 allocations, arguably a detriment to usability - we’ll get to that - before we do, it is important to understand what ’NAT” as we call it today actually is, and to do that we need to explain all of the types of address translation (yes, there are several). When what was designed</div>
<div></div>
<div><b><u>Static, or one-to-one NAT</u></b> This is the original and most simple. It is comprised of an internal and corresponding external IP address. Every machine on the network still needs a public IP address for external mapping with this model. It was originally designed to solve the problem NAT was built to address: address translation between two networks.</div>
<div></div>
<div><b><u>Dynamic NAT</u></b> This is a bit of a hybrid of static and the next type, NAPT. In this model, a NAT router maintains a set of external IPv4 address and cynically allocates one to internal addressed for outbound communication.</div>
<div></div>
<div><b><u>Network Address port translation (NAPT)</u></b> This is what most folks will mean when they say “NAT”. Really, this is address masquerading with port translation. This is what is often confused with a security tool, given that it provides a low level of obfuscation from external scanning and “hides” the hosts behind an externally facing address. This mechanism is typically conflated with stateful firewall implementation, which is not inclusive of this implementation.</div>
<div></div>
<div>Because of the enterprise expectation of a modern UTM, NAPT is unfortunately used interchangeably by many security professionals. What NAPT actually buys is a mechanism for obfuscating many hosts to a smaller number of addresses, typically on the same device. By removing a single data reconnaissance vector (scanning of ipv4) you’re actually providing a new one that’s much easier to exploit (state table exhaustion). While it does work to prevent inbound scanning, that’s really all it does other than allow for network and port translation, it should not be expected to provide anything more than simple obscuring of the internal data. NAPT as security is primarily predicated on the notion that your source address is critically important and should be obscured. While this is true to a certain extent, this believe is somewhat antiquated and should be treated as such. Tracking via source address is still completely doable with simple tools, and geolocation is completely available (assuming it is correctly registered) based on the NAPT address. This is true of IPv4 and IPv6. What NAT does accomplish is prevention of scanning and external recon of potentially sensitive systems. That’s it. I would also assert that this over-stated sense of usefulness users a false sense of protection and encourages a relaxed diligence on hardening end hosts. The same level of protection can very easily be accomplished on a public IPv4 or IPv6 prefix with a simple stateful firewall or host based firewall. What NAPT buys is two fold:</div>
<ul>
 	<li>
<div>Extension of IPv4 resources</div></li>
 	<li>
<div>A poor shortcut to resource protection</div></li>
</ul>
<div>If sized appropriately, the expense of this is a very under-stated price tag</div>
<ul>
 	<li>
<div>A sizable cost for right-sized UTM</div></li>
 	<li>
<div>Acceptance of the risk of a state table exhaustion DoS event</div></li>
 	<li>
<div>Insecure internal resources, IoT devices, or BYOD nodes that are compromised or vulnerable.</div></li>
</ul>
<div>Without proper east-west filtering and a tight egress policy, this sheen of protection becomes significantly less useful. Add in the likelihood of <a href="https://en.wikipedia.org/wiki/Carrier-grade_NAT">carrier grade NAT (CGNAT)</a> due to extreme <a href="https://en.wikipedia.org/wiki/IPv4_address_exhaustion">exhaustion of IPv4 resource</a>, and you compound the limits with additional operational and troubleshooting overhead. IPv6, while the correct next step, does solve a large part of the issues, but not without it’s own [mostly one-time] costs, and given the large uptake in IPv6 from both the client and content perspectives, it would behoove every organization to get their IPv6 strategy sorted and underway.</div>
<div>
<div></div>
</div>
<h3><u><b>My take</b></u></h3>
<div></div>
<div>In the olden times of winnuke, providing a layer of confusion between the delicious caramel center of your network resource and the dragons of the internet was pretty important. The tracking mechanisms and scanning was mostly thwarted by the thin candy shell of the NAPT device. While this is still a very important aspect in your network architecture and defense in depth strategy, understanding the real risks and true value is important. The belief that NAPT provides your security (or that it is even a security tool at all) is somewhat misguided. With regard to privacy, the real threats lie in the metadata collection, and unless you are high profile or have a highly targeted business or personal footprint, the security incidents are far more nuanced and often happen at higher layers. In addition, lets not forget that a very, very real threat is not from random poking at our externally facing network resources, but in the social engineering attacks that are readily let right in the door. In addition, there are a number of significant risks that NAPT beings to bear based on it’s use of a state table to track IP to port mappings. All of these details need to be considered and continually revisited for relevance.</div>
<div></div>
<h3><b><u>Further study</u></b></h3>
Understanding that this is a very high profile, sensitive, and polarizing subject, additional reading and research is important. A few good white papers detailing shortcomings and misconceptions surrounding NAPT can be found <a href="https://www.google.com/amp/s/www.calyptix.com/top-threats/ddos-attacks-101-types-targets-motivations/amp/">here</a> and <a href="https://f5.com/resources/white-papers/the-myth-of-network-address-translation-as-security">here</a>. In addition, <a href="https://thenetworkcollective.com/">The Network Collective</a> invited me back to discuss privacy in networking. What resulted was a very spicy podcasts that really highlights the complexity of privacy as a concept in today's internet.
<div></div>
<div></div>
<iframe src="https://player.vimeo.com/video/272381393" width="640" height="360" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
<a href="https://vimeo.com/272381393">Ep28 - For The Love Of NAT</a> from <a href="https://vimeo.com/networkcollective">Network Collective</a> on <a href="https://vimeo.com">Vimeo</a>.
---
id: 547
title: 'My SDN soapbox (now with IPv6!)'
date: '2013-03-23T15:45:17-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=547'
permalink: /2013/03/23/my-sdn-soapbox-now-with-ipv6/
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3651234561'
Views:
    - '165'
categories:
    - IPv6
    - Musings
    - OpenFlow
    - SDN
---

This week there was a lot of buzz about SDN (as usual). There was a<a href="http://www.lightreading.com/blog/software-defined-networking/sdns-killer-app-more-network-control/240151376" target="_blank" rel="noopener noreferrer"> lightreading thread that I commented on</a> and a fantastic read by <a href="http://www.twitter.com/networkstatic" target="_blank" rel="noopener noreferrer">Brent Salisbury</a> about <a href="http://networkstatic.net/be-the-steamroller-not-the-road/" target="_blank" rel="noopener noreferrer">being the steamroller and not the road</a> that got me thinking about OpenFlow and SDN in a way I had not before.
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/03/fearofchange.jpg"><img class="alignright size-full wp-image-550" alt="fearofchange" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/fearofchange.jpg" width="339" height="500" /></a>
&lt;soapbox&gt;
All that is old is new again. I remember when internal networks were small and routing protocols were taboo in many internal environments. RIP (AKA routing by rumor) was about as innovative as we got, OSPF was "too complex" and was "software changing the network topology", according to some folks I worked with in what seems like a lifetime ago. Clearly they didn't have the entire picture and were clouded by FUD. Now using a link state protocol is a standard and one would probably not consider building a complex, production layer 3 network without an IGP like ISIS or OSPFv[2/3] (or even EIGRP...I guess).
This is simple evolution and progression. The more folks try to resist, the further behind they'll be left.
SDN and OpenFlow are not unlike IPv6 in many ways when viewed from a technology implementation perspective, and in fact, we can probably learn from the resistance to IPv6 to help us with the acceptance of SDN and OpenFlow. V6 has been coming for years. It's <em>mostly</em> here. Backbones have been running it for a very long time and we actually <strong>need</strong> it on the client side to account for the huge number of hosts now connecting to the public Internet.
Many entities, especially very risk averse enterprises, are struggling to resist it (IPv6) and hold onto NAT and IPv4 as long as possible.  While this will almost certainly buy them a handful of years, it's futile.  Translation and transition tech geared toward the folks that refuse to adapt will allow them to grasp onto legacy methodologies for a bit longer, but as the Borg say, "resistance is futile".
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg.jpg"><img class="alignleft size-medium wp-image-557" alt="Borg" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg-300x274.jpg" width="300" height="274" /></a>
These same things are all going to happen with SDN.
What we say is "OpenFlow is simply an open protocol for creating flow based forwarding.  It allows for the inclusion of other factors such as Layer4 to make those decisions more tunable and granular."
What skeptics hear is "There is a hole in the boat, we're all going to die" or "Network Engineers are all going to be out of a job!" or "your job is going to be replaced by software" or even "software and applications will make the way we think about and do everything obsolete", all of which translate to "dramatic and drastic change".
Most of this is just sensationalism and FUD. In my opinion, though, it is all based in truth .  It may be "drastic" but it's not dramatic.  It's natural evolution.  It will happen slowly.  We will have to change they way we do things. The proven fact we as networking and security professionals need to remember is that change going to happen with or without SDN, it's the nature of an innovative field like technology to change.  None of us would be doing what we do without being inquisitive enough to figure out problems, challenge norms and shift thinking.
SDN, just like IPv6, is happening.  Personally I'd rather be knowledgeable about as opposed to in the dark and scrambling to learn about them at the 11th hour.<em id="__mceDel"> </em>
&lt;/soapbox&gt;
&nbsp;
&nbsp;
&nbsp;
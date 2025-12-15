---
id: 1647
title: 'Soap Box: Mikrotik; "IPv6 Apocalypse", or maybe not.'
date: '2019-03-31T11:35:10-05:00'
author: buraglio
excerpt: 'Neighbor table and route-cache have been problems in IPv6 implementations since the beginning. No one is immune to the basics. '
layout: post
guid: 'https://www.forwardingplane.net/?p=1647'
permalink: /2019/03/31/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/
Views:
    - '611'
categories:
    - IPv6
    - 'Soap Box'
tags:
    - IPv6
---

Over the last few days there has been a <em><strong>huge</strong></em> amount of FUD and panic surrounding two as-yet-to-be-published CVEs (found <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-19298">here</a> and <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-19299">here</a>) related to Mikrotik's IPv6 implementation.It is my opinion that this entire process has been poorly handled, and that the community involved tends to be fairly sensitive to issues such as, and the cloak and dagger nature of the two issues has only exacerbated it. Mikrotik, as a company, is well known for being terse in their responses and tight lipped with their internal workings and dealings with these kinds of issues. I take that as a given, that’s their business and realistically we’re entitled to know exactly none of that information, even if it would be nice to have it. The history behind this is discouraging, the original discovery was quite some time ago with reports dating back to 2013, and the person who originally uncovered the issues did so upwards of a year ago, bringing them to Mikrotik at that time, as can be seen in this <a href="https://forum.mikrotik.com/viewtopic.php?f=2&t=125841&p=654116&hilit=ndpexhaust26#p654116">thread</a>. Now, anyone with a passing knowledge of pen testing or IPv6 device load testing can trivially put together the information needed to decipher the problem and replicate it, neither are exactly complicated or <a href="https://insinuator.net/2013/03/ipv6-neighbor-cache-exhaustion-attacks-risk-assessment-mitigation-strategies-part-1/">new</a>. Both can be done in literally one line of<a href="https://tools.kali.org/information-gathering/thc-ipv6"> common, open source toolkits. </a> The issues are not magical and are not even esoteric or cryptic. They are very straightforward, and by reading the threads and understanding how things like route caches and <a href="https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol">neighbor discovery</a> work, they become very clear.
Since this is IPv6 related I am very interested in it because I feel that WISPs and emerging markets are an excellent environment for moving IPv6 forward, and the equipment and mindset involved makes that fairly straightforward. Reverse engineering these given the information available is pretty straightforward, and <a href="https://www.iparchitechs.com/">folks other than me have done it</a> too.
I personally do not consider either of these a security vulnerability or a bug, per se. They’re both the result of a short sighted protocol implementation resulting in a very acute, unfortunate event. With the benefit of hindsight, and as an outsider, I can only wonder if this had been handled differently (i.e. not framed as a critical security vulnerability but rather a broken protocol), if the hysteria that resulted could have been quelled. On a <a href="https://forum.mikrotik.com/viewtopic.php?f=2&t=147048&start=50">particular forum thread,</a> this was likened to the discovery of the “ping of death”, and that feels like a good analogy to me. It probably should have been handled that way.
So, I will post my .02 as to how this kind of even can be handled in the future, in case there is no better process to work with:
1. Involve the vendor early.
2. Involve a trusted third party to validate the result. It’s very easy to miss trees when you’re stuck in a forest. 3rd party validation is pretty important either way as it proves a problem can be repeated independently.
3. Disclose the environment hardware, in detail, that was used to test and confirm the the issue in.
4. Have both validated it with said trusted, embargoed outside source(s). Again, ideally one is the vendor.
5. If unable to define and at least indicate that there is a remediation, leverage outside trusted source to <strong>make sure that’s not possible</strong>. In this case, that seems to be kept between the person who discovered it and the vendor, which as discussed above has a track record of being pretty closed off.
For this particular issue and platform, one can monitor the IPv6 route-cacheing near real-time, here is the command to do it at 1 second intervals
<pre>[buraglio@gw] &gt; /ipv6 route cache print interval=1
cache-size: 190max-cache-size: 1024000</pre>
The ND issue can be mitigated with the following command (obviously adjusted for your own environment).
<pre>/ipv6 firewall filter
add action=drop chain=forward connection-mark=drop connection-state=new
/ipv6 firewall mangle
add action=accept chain=prerouting connection-state=new dst-address=\
2001:db8:3::/64 limit=2,5:packet
add action=mark-connection chain=prerouting connection-state=new dst-address=\
2001:db8:3::/64 new-connection-mark=drop passthrough=yes</pre>
And for those more interested in the actual process, here is a video demonstrating the basic route-cache issue (commands, although very easy to figure out are obfuscated)
<p style="text-align: center;"><iframe src="https://www.youtube.com/embed/YEdMTa6XKWk" width="640" height="480" frameborder="0" allowfullscreen="allowfullscreen"></iframe></p>
Mikrotik has released a fix as of this morning (4/1/2019), although it is currently beta. ROS 6.45 addresses both the route cache and the neighbor table issue. More details on the discovery will be <a href="https://indico.uknof.org.uk/event/46/contributions/speakers">disclosed at the UKNOF conference</a>.
<h4>My take:</h4>
A problem like this that is as egregious as described needs to be independently validated and ideally a remediation found before disclosure. If a mitigation strategy does not exist, the $vendor takes responsibility by default and realistically, nothing can be done until they fix it. It may also be disclosed as a zero-day-style, weaponized tactic. Obviously that is the worst case. The real point is that we’re a community, and we need to build the trust frameworks to work together on issues such as this without pointing fingers or running around with our hands waving.
This behavior is, sadly, pretty easy to re-create. There is an old thread that implies some of this was triggered by "real traffic", and I have definitely seen an uptick in ipv6 scanning that impacts major vendor router platforms to the point that they get salty about traffic flows and spike CPUs. This feels pretty darned similar, but not the catastrophic event horizon it's being played out to be. It's still bad, it stinks, and it's definitely been handled in a way that is less than optimal. I would also like to point out a few things since there has been a fair amount of hair on fire panic. I realize I am being a tad pedantic, but it's important to identify things correctly in order to handle them in the correct manner. This is not a security vulnerability as I would describe it. There is no remote or local execution of code, no raised privileges, no mechanism of compromise. I don't think this is a software bug, either. It's close, but in reality what this is is a poorly implemented protocol that had what I can only believe was a poverty of testing before release and as such allows for a remotely triggered denial of service.
Denial of service isn't necessarily malicious, it just means exactly what it says: service is denied. As mentioned earlier in the thread, this is like the old ping of death issue: a poorly executed stack.
I'd like to know who has executed this in the wild and how far back this goes in their code train, references go back as far as 2013, but I suspect they go back to the original support.
<h4>---- UPDATE</h4>
Mikrotik has addressed this issue with the release of ROS 6.44.2. The prior methodologies no longer exhaust resources and reload devices, as can be seen here
<iframe width="640" height="480" src="https://www.youtube.com/embed/XWPMzPW4jPA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>
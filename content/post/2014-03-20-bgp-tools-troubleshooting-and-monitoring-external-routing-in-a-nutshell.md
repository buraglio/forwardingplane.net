---
id: 955
title: 'BGP tools; troubleshooting and monitoring external routing in a nutshell'
date: '2014-03-20T22:51:06-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=955'
permalink: /2014/03/20/bgp-tools-troubleshooting-and-monitoring-external-routing-in-a-nutshell/
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'Maintaining and troubleshooting BGP in a nutshell'
themeblvd_keywords:
    - 'BGP, David Meyer, routeviews, Nick Buraglio, buraglio, OpenDayLight, eBGP, iBGP, Cisco, Juniper, IOS, JunOS, bgpmon, peermon, ARIN, IPV6, networking, network engineering, routing BGP, routing, show advertised routes, show bgp advertised routes, show received routes, show bgp received routes, TiMOS, show ipv6 received routes, show ipv6 bgp received routes, show ipv6 advertised routes, show ipv6 bgp received routes, Alcatel-Lucent, ALU 7750'
themeblvd_description:
    - 'How I monitor BGP peerings in the real world. Running BGP in the wild in a nutshell.'
dsq_thread_id:
    - '2474358218'
Views:
    - '834'
categories:
    - How-To
    - Routing
---

Time to rewind from the new and shiny and get back to roots of networking. <a href="http://en.wikipedia.org/wiki/Border_Gateway_Protocol" target="_blank" rel="noopener noreferrer">BGP</a> is one of those odd protocols that is foundational to the functioning of the internet but yet somewhat hard to get experience with.  Say what you will about this venerable protocol, it's been here a while and it is not going anywhere any time soon. I've been doing BGP since around late 1999, and I completely fell into it by accident, having only the Cisco <a href="http://www.amazon.com/Internet-Routing-Architectures-2nd-Edition/dp/157870233X" target="_blank" rel="noopener noreferrer">Internet Routing Architectures</a> book (which I literally read cover to cover) and the<a href="http://www.amazon.com/IP-Routing-Protocols-OSPF-Cisco/dp/0130142484/ref=la_B001HCXUMA_1_1?s=books&ie=UTF8&qid=1395373752&sr=1-1" target="_blank" rel="noopener noreferrer"> Ulysses Black Routing Protocols Book</a>  and whatever I could find on a random search engine to guide me, and that was only after having to learn on the CLI for the first 6-7 months. In actuality, that is how many of the folks of my vintage came into doing BGP. Someone needed to announce some routes that were allocated to them by an <a href="https://www.arin.net/knowledge/rirs.html" target="_blank" rel="noopener noreferrer">RIR</a>, or bring up some multi-homing or whatever.  Whoever knew how to work on the border device (or was willing to touch arguably the most important device on the network) got to learn how to do it. In 15 years of configuring, monitoring, tweaking, tuning and generally just maintaining BGP across service provider, research, enterprise networks and in labs and test environments, here are the tools I had to find to either put out fires, prevent blazing flames or prove that there is/was no fire.
Lets assume that you already have all of the appropriate prefix lists, policy options and route maps in place to filter correctly. You're doing that, right? If not, go do that and then come back to this. It will make your life easier in the long run. All eBGP peerings should have inbound and outbound filters on them. No exceptions. Yes, it can be a pain to maintain but when someone leaks you a full table when you're expecting directly connected, you'll be glad that they're there. See below about automating the filters programatically.
Now on to the fun stuff.
Look at what the router is sending and receiving.  You know what you're announcing, right?
Under Cisco IOS the appropriate commands to display this information will look like this:
<pre>show ip bgp neighbor received-routes</pre>
<pre>show ip bgp neighbor advertised-routes</pre>
In JunOS it will look like this:
<pre>show route rec protocol bgp &lt;neighbor&gt;</pre>
<pre>show route adv protocol bgp &lt;neighbor&gt;</pre>
On an Alcatel-Lucent the command will look like this:
<pre>show router bgp neighbor &lt;neighbor&gt; advertised-routes</pre>
Brocade has their methods too, it is <em>relatively</em> similar to IOS. One important thing to note, JunOS requires no difference in the show command for IPv6. IOS and ALU has an additional command to display IPv6 information. IOS-XR may be different still, but I cannot confirm or recall since I have not used it since late 2012 (additions welcome in the comments).  For IPv6 on Cisco IOS and ALU respectively:
<pre>show ipv6 bgp neighbors &lt;neighbor&gt; received-routes | advertised-routes
show router bgp neighbor &lt;neighbor&gt; advertised-routes ipv6</pre>
This will provide a view from the street, it will display exactly what your router knows.
<a href="http://www.traceroute.org/#Route%20Servers" target="_blank" rel="noopener noreferrer">Route servers </a>/ <a href="http://www.bgp4.as/looking-glasses" target="_blank" rel="noopener noreferrer">Looking Glass</a> --This is your basic  external view. Log in and see what other ASNs know about your routes.  Critically important during those "something is on fire" times mentioned above.  They are maintained by a myriad of entities and positioned all over the globe.
<a href="http://www.bgpmon.org" target="_blank" rel="noopener noreferrer">BGPmon</a> --A project by <a href="https://twitter.com/atoonk" target="_blank" rel="noopener noreferrer">Andree Toonk</a>. Allows for the automatic discovery and monitoring of prefixes, alerting on many, many  attributes such as prefix hijacks.  Free and commercial plans available, but the commercial plans are far more feature rich and well worth it if you monitor large amounts og BGP.
<a href="https://www.bgpmon.net/new-version-of-bgpmon-net/" target="_blank" rel="noopener noreferrer">Peermon</a> --Part of the new and improved BGPmon.  Allows for the on-demand monitoring of prefixes within your network. Very useful for viewing as-path changes of destination networks for long term troubleshooting.
<a href="http://www.routeviews.org" target="_blank" rel="noopener noreferrer">RouteViews</a> -- Great project out of U of Oregon that was (is?) run by the groundbreaking <a href="https://twitter.com/dmm613" target="_blank" rel="noopener noreferrer">David Meyer</a> of <a href="http://www.opendaylight.org/" target="_blank" rel="noopener noreferrer">OpenDaylight</a> (and many other things) fame.  Peers with networks and records routing changes, allows for public query and has vast historical data.
<a href="http://bgplay.routeviews.org/" target="_blank" rel="noopener noreferrer">bgplay</a> - Great visualization tool for tracking routing, as-path and prefix announcement changes. This is part of the routeviews project and utilizes their vast historical data.  L=It currently acks IPv6 support and I;m unsure if it is maintained anymore.
<a href="http://routerproxy.grnoc.iu.edu/internet2/" target="_blank" rel="noopener noreferrer">Router Proxies</a> -- This has been a big thing int he R&E world for quite some time.  Other entities may offer it, it's similar to a looking glass but more easily configured to allow or disallow different show commands.  The <a href="http://routerproxy.sourceforge.net/" target="_blank" rel="noopener noreferrer">code is open source</a> and pretty easy to hack new commands into or adapt to new platforms (if I can do it anyone can).
Lookup tools such as whois.  I find that looking uo ASNs and networks against the ARIN, RIPE and other RIRs is very handy as a starting point.  using CLI commands such as "whois -h whois.arin.net 1224" would display the following information:
<pre>#
# The following results may also be obtained via:
# http://whois.arin.net/rest/asns;q=1224?showDetails=true&ext=netref2
#</pre>
<pre>ASNumber: 1224
ASName: NCSA-AS
ASHandle: AS1224
RegDate: 1991-02-25
Updated: 1997-10-27
Ref: http://whois.arin.net/rest/asn/AS1224</pre>
<pre>OrgName: National Center for Supercomputing Applications
OrgId: NCSA-3
Address: NCSA
Address: 1205 W. Clark St
City: Urbana
StateProv: IL
PostalCode: 61801
Country: US
RegDate: 1990-03-26
Updated: 2011-04-06
Ref: http://whois.arin.net/rest/org/NCSA-3</pre>
<pre>OrgAbuseHandle: ND63-ORG-ARIN
OrgAbuseName: Network Development
OrgAbusePhone: +1-217-244-0714
OrgAbuseEmail: neteng @ ncsa.illinois.edu
OrgAbuseRef: http://whois.arin.net/rest/poc/ND63-ORG-ARIN</pre>
<pre>OrgTechHandle: ND63-ORG-ARIN
OrgTechName: Network Development
OrgTechPhone: +1-217-244-0714
OrgTechEmail: neteng @ ncsa.illinois.edu
OrgTechRef: http://whois.arin.net/rest/poc/ND63-ORG-ARIN</pre>
<pre>RTechHandle: ND63-ORG-ARIN
RTechName: Network Development
RTechPhone: +1-217-244-0714
RTechEmail: neteng @ ncsa.illinois.edu
RTechRef: http://whois.arin.net/rest/poc/ND63-ORG-ARIN</pre>
<pre>#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/whois_tou.html
#</pre>
Very handy for prefixes and ASNs.  There are also service like the <a href="https://www.team-cymru.org/Services/ip-to-asn.html" target="_blank" rel="noopener noreferrer">Team Cymru whois server</a> that can display date/time based information for forensics and to provide IP to ASN mappings. Also very handy.  I believe this code is also open source.
<a href="http://irrtoolset.isc.org/" target="_blank" rel="noopener noreferrer">IRR Toolset</a>.  Extremely handy for automation of routing policy configuration.  I found it a tad painful to set up but it is a useful toolkit.
Notable Mention: <a href="https://ring.nlnog.net/" target="_blank" rel="noopener noreferrer">NLNog RING</a>.  -- This is a trust based unix host that provides a <a href="https://ring.nlnog.net/toolbox/" target="_blank" rel="noopener noreferrer">large variety of services </a>to those that qualify for participation.  Very handy when looking for an on-net perspective.
Notable Mention / Shameless Plug:<a href="http://psps.perfsonar.net/toolkit/" target="_blank" rel="noopener noreferrer"> perfSonar toolkit</a>.  In addition to thewell known performance testing tools, PS provides things like reverse traceroute and other handy networking widgets.  It also has a far lower barrier of entry than the NLNog RING.
 
There are obviously more ways to do this and there are possibly better ones, too.  This is how I've done it for a long time and it has mostly worked for me.  I had to learn most of this by trial and error so I thought it maybe useful to throw it all together into one place for future reference.
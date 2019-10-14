---
title: 'BGP tools; troubleshooting and monitoring external routing in a nutshell'
date: Fri, 21 Mar 2014 04:51:06 +0000
draft: false
tags: [How-To, Routing]
---

Time to rewind from the new and shiny and get back to roots of networking. [BGP](http://en.wikipedia.org/wiki/Border_Gateway_Protocol) is one of those odd protocols that is foundational to the functioning of the internet but yet somewhat hard to get experience with.  Say what you will about this venerable protocol, it's been here a while and it is not going anywhere any time soon. I've been doing BGP since around late 1999, and I completely fell into it by accident, having only the Cisco [Internet Routing Architectures](http://www.amazon.com/Internet-Routing-Architectures-2nd-Edition/dp/157870233X) book (which I literally read cover to cover) and the [Ulysses Black Routing Protocols Book](http://www.amazon.com/IP-Routing-Protocols-OSPF-Cisco/dp/0130142484/ref=la_B001HCXUMA_1_1?s=books&ie=UTF8&qid=1395373752&sr=1-1)  and whatever I could find on a random search engine to guide me, and that was only after having to learn on the CLI for the first 6-7 months. In actuality, that is how many of the folks of my vintage came into doing BGP. Someone needed to announce some routes that were allocated to them by an [RIR](https://www.arin.net/knowledge/rirs.html), or bring up some multi-homing or whatever.  Whoever knew how to work on the border device (or was willing to touch arguably the most important device on the network) got to learn how to do it. In 15 years of configuring, monitoring, tweaking, tuning and generally just maintaining BGP across service provider, research, enterprise networks and in labs and test environments, here are the tools I had to find to either put out fires, prevent blazing flames or prove that there is/was no fire. Lets assume that you already have all of the appropriate prefix lists, policy options and route maps in place to filter correctly. You're doing that, right? If not, go do that and then come back to this. It will make your life easier in the long run. All eBGP peerings should have inbound and outbound filters on them. No exceptions. Yes, it can be a pain to maintain but when someone leaks you a full table when you're expecting directly connected, you'll be glad that they're there. See below about automating the filters programatically. Now on to the fun stuff. Look at what the router is sending and receiving.  You know what you're announcing, right? Under Cisco IOS the appropriate commands to display this information will look like this:```
show ip bgp neighbor  received-routes
``````
show ip bgp neighbor  advertised-routes
```In JunOS it will look like this:```
show route rec protocol bgp <neighbor>
``````
show route adv protocol bgp <neighbor>
```On an Alcatel-Lucent the command will look like this:```
show router bgp neighbor <neighbor> advertised-routes
```Brocade has their methods too, it is _relatively_ similar to IOS. One important thing to note, JunOS requires no difference in the show command for IPv6. IOS and ALU has an additional command to display IPv6 information. IOS-XR may be different still, but I cannot confirm or recall since I have not used it since late 2012 (additions welcome in the comments).  For IPv6 on Cisco IOS and ALU respectively:```
show ipv6 bgp neighbors <neighbor> received-routes | advertised-routes

show router bgp neighbor <neighbor> advertised-routes ipv6
```This will provide a view from the street, it will display exactly what your router knows. [Route servers ](http://www.traceroute.org/#Route%20Servers)/ [Looking Glass](http://www.bgp4.as/looking-glasses) --This is your basic  external view. Log in and see what other ASNs know about your routes.  Critically important during those "something is on fire" times mentioned above.  They are maintained by a myriad of entities and positioned all over the globe. [BGPmon](http://www.bgpmon.org) --A project by [Andree Toonk](https://twitter.com/atoonk). Allows for the automatic discovery and monitoring of prefixes, alerting on many, many  attributes such as prefix hijacks.  Free and commercial plans available, but the commercial plans are far more feature rich and well worth it if you monitor large amounts og BGP. [Peermon](https://www.bgpmon.net/new-version-of-bgpmon-net/) --Part of the new and improved BGPmon.  Allows for the on-demand monitoring of prefixes within your network. Very useful for viewing as-path changes of destination networks for long term troubleshooting. [RouteViews](http://www.routeviews.org) -- Great project out of U of Oregon that was (is?) run by the groundbreaking [David Meyer](https://twitter.com/dmm613) of [OpenDaylight](http://www.opendaylight.org/) (and many other things) fame.  Peers with networks and records routing changes, allows for public query and has vast historical data. [bgplay](http://bgplay.routeviews.org/) - Great visualization tool for tracking routing, as-path and prefix announcement changes. This is part of the routeviews project and utilizes their vast historical data.  L=It currently acks IPv6 support and I;m unsure if it is maintained anymore. [Router Proxies](http://routerproxy.grnoc.iu.edu/internet2/) -- This has been a big thing int he R&E world for quite some time.  Other entities may offer it, it's similar to a looking glass but more easily configured to allow or disallow different show commands.  The [code is open source](http://routerproxy.sourceforge.net/) and pretty easy to hack new commands into or adapt to new platforms (if I can do it anyone can). Lookup tools such as whois.  I find that looking uo ASNs and networks against the ARIN, RIPE and other RIRs is very handy as a starting point.  using CLI commands such as "whois -h whois.arin.net 1224" would display the following information:```
#
# The following results may also be obtained via:
# http://whois.arin.net/rest/asns;q=1224?showDetails=true&ext=netref2
#
``````
ASNumber: 1224
ASName: NCSA-AS
ASHandle: AS1224
RegDate: 1991-02-25
Updated: 1997-10-27
Ref: http://whois.arin.net/rest/asn/AS1224
``````
OrgName: National Center for Supercomputing Applications
OrgId: NCSA-3
Address: NCSA
Address: 1205 W. Clark St
City: Urbana
StateProv: IL
PostalCode: 61801
Country: US
RegDate: 1990-03-26
Updated: 2011-04-06
Ref: http://whois.arin.net/rest/org/NCSA-3
``````
OrgAbuseHandle: ND63-ORG-ARIN
OrgAbuseName: Network Development
OrgAbusePhone: +1-217-244-0714
OrgAbuseEmail: neteng @ ncsa.illinois.edu
OrgAbuseRef: http://whois.arin.net/rest/poc/ND63-ORG-ARIN
``````
OrgTechHandle: ND63-ORG-ARIN
OrgTechName: Network Development
OrgTechPhone: +1-217-244-0714
OrgTechEmail: neteng @ ncsa.illinois.edu
OrgTechRef: http://whois.arin.net/rest/poc/ND63-ORG-ARIN
``````
RTechHandle: ND63-ORG-ARIN
RTechName: Network Development
RTechPhone: +1-217-244-0714
RTechEmail: neteng @ ncsa.illinois.edu
RTechRef: http://whois.arin.net/rest/poc/ND63-ORG-ARIN
``````
#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/whois\_tou.html
#
```Very handy for prefixes and ASNs.  There are also service like the [Team Cymru whois server](https://www.team-cymru.org/Services/ip-to-asn.html) that can display date/time based information for forensics and to provide IP to ASN mappings. Also very handy.  I believe this code is also open source. [IRR Toolset](http://irrtoolset.isc.org/).  Extremely handy for automation of routing policy configuration.  I found it a tad painful to set up but it is a useful toolkit. Notable Mention: [NLNog RING](https://ring.nlnog.net/).  -- This is a trust based unix host that provides a [large variety of services](https://ring.nlnog.net/toolbox/) to those that qualify for participation.  Very handy when looking for an on-net perspective. Notable Mention / Shameless Plug: [perfSonar toolkit](http://psps.perfsonar.net/toolkit/).  In addition to thewell known performance testing tools, PS provides things like reverse traceroute and other handy networking widgets.  It also has a far lower barrier of entry than the NLNog RING.   There are obviously more ways to do this and there are possibly better ones, too.  This is how I've done it for a long time and it has mostly worked for me.  I had to learn most of this by trial and error so I thought it maybe useful to throw it all together into one place for future reference.
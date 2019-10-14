---
title: 'OpenDNS acquires BGPMon and the future of route monitoring'
date: Fri, 20 Mar 2015 05:18:30 +0000
draft: false
tags: [Routing, Security, Soap Box]
---

For those that run BGP networks, [BGPmon](http://www.bgpmon.net) is often a tool they turn to for some really unique and hard to find information. Remember back in February 2008 when Pakistan Telecom "blocked" [Youtube](http://www.youtube.com/buraglio)? That one was a really, really public example of something that BGPMon caught. BGPmon has been around for a long, long time. Quietly watching prefixes. Silently noting changes and reporting them to the ones lucky enough to know of its existence. For those that don't [know how BGP works](http://searchtelecom.techtarget.com/feature/BGP-essentials-The-protocol-that-makes-the-Internet-work), I am not going to go into it too much other than to say that it is both the foundation that the internet is built upon, and one of the most antiquated trust models that exists in a world where most of the pundits are going on and on about SDN and network engineers being out of a job in 10 years. See, the problem with BGP is not that it is a terrible protocol. Quite the opposite, it is elegant in its simplicity and ability to be extended.It is lightweight and arguably the easiest of the routing protocols with the exception of RIPv2.

_Many have argued that it is not a routing protocol, per se, but a policy enforcement framework for paths, but that is a completely different discussion. I happen to agree_

The issue with BGP is that its install base is so vast that changing it is not unlike parting the red sea or holding the earth on ones shoulders, because that is what BGP does. It holds the internet on its shoulders every bit as much as things like fiber in the ground does. Lets get back to BGPmon. BGPmon does something that nothing else really does. It watches the global routing table from points all over the globe and keeps track of prefixes. For a network operation that provides transit, financial services or any sensitive data, notification of a ROA violation, prefix hijack or more specific route announcement is a critical service. BGPmon provides that among other equally distinct services. In fact, [I have it listed as one of my critical tools for maintaining, monitoring and troubleshooting external routing](https://www.forwardingplane.net/2014/03/bgp-tools-troubleshooting-and-monitoring-external-routing-in-a-nutshell/).

What does the acquisition of BGPmon by OpenDNS mean? I honestly can not say, but I am fairly confident that it means good things and [OpenDNS has a very, very encouraging position](https://blog.opendns.com/2015/03/12/opendns-acquires-bgpmon/):

_Moving forward, our integration plan for BGPmon is straightforward. We’ll invest in building out the service and making it more complete—but we also are committed to keeping the free features free. We’ll continue to use BGPmon data and innovate to augment our predictive intelligence and provide better threat protection to OpenDNS customers. So basically status quo for current customers._

Strong backing from a forward thinking company with a solid track record of good products likely means a bright future for an invaluable service. I am optimistic and encouraged, this was the next logical step and they have taken it with elegance and thought.
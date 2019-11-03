---
title: 'And a purple pony.'
date: Mon, 05 Nov 2012 10:58:00 +0000
draft: false
tags: [Musings]
---

If I had my perfect world where I lived in a gumdrop house with lollypop trees and everything smelled like butterfly kisses, here is what I would like to see in WAN networking gear.   I can build a list for LAN and edge gear as well.  It's not a golden rocket ship I'm looking for.  OK, maybe it is.

*   Full MPLS support 
*   Full IPv6 support, all the features, not just pieces.    
*   Full VRF support 
*   LACP support
*   Layer2 + Layer3, MPLS OpenFlow/SDN simultaneously on all hardware interfaces
*   9000+ byte frame support
*   Full instrumentation of software and hardware interfaces.
*   OSPFv2/3
*   ISIS
*   mBGP4
*   Multicast (MSDP, PIM-SM)
*   Flow export (IPFIX/V9 or sFlow)
*   Full ACL support on software and hardware interfaces, inbound and outbound, IPv4 and IPv6.
*   v4 and v6 uRPF in all VRFs
*   ACL support for control plane services (ssh, snmp, telnet, etc.)
*   Non Stop Routing in all VRFs, ideally in logical systems as well  
*   Logical systems / Multi-Tenant routers
*   In-Service Software Upgrade (Hitless upgrades)
*   Support for 4x the current global table
*   Support for 4x global IPv6 table
*   32+ nonblocking 10G interfaces
*   4+ nonblocking 100G interfaces
*   18000 byte frame support on 100G interfaces
*   Separate control and forwarding plane and/or control plane policing
*   All supported routing protocols in non-default VRF and/or logical router
*   OpenFlow/SDN support in non-default VRFs
*   Flow based policing on all software and hardware based interfaces
*   **I want to be able to turn all of this on at the same time **

Why would anyone want all of these things, you may ask?  Not everyone is an enterprise customer.  Not everyone is an ISP.  Some of us are all of those things, plus more.  Not everyone has a brinks truck full of money to pour into layers of network gear.  Some people try to innovate and step outside of comfort zones to create new ways of doing things.  

In the research and education realm, we actually \*need\* some, if not all, of these things.  Is there any chance we can get this?  Maybe, The MX series juniper makes comes pretty close.  The Brocade MLXe claims to do a good portion of this stuff on paper.  ...I don't actually know what is in the Cisco portfolio that can come close.  ASR 9K?  You tell me.  Can the Arista do it?  It's a linux box at it's core so maybe, but are the buffers deep enough?  If you take out the OpenFlow bits the Alcatel-Lucent can probably do it.  H3C?  Maybe I live in a fantasy world.  Come on, folks, point me at something.  

Push limits or be limited.
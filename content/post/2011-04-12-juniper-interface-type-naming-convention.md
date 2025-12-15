---
id: 37
title: 'Juniper interface type naming convention'
date: '2011-04-12T19:04:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/'
permalink: /2011/04/12/juniper-interface-type-naming-convention/
Views:
    - '1478'
categories:
    - Routing
---

I found most of this on a web page somewhere tha tI can't seem to find again. Below are some common useful junos tidbits regarding routing tables and interface types/names:**
JunOS CLI supports the basic grep command (like | include) so any show commands can be grepped. I believe the grep command implies the -i flag for case insensitivity.

The routing table is presented in such a way to group types of routes.

<b>inet.0 is the ipv4 unicast routing table

****inet.1 is the ipv4 multicast routing table

****inet.3 is the MPLS routing table

****inet6.0 is the ipv6 routing table****

Juniper interface types


Most common ones you'll probably see:

<b>fe: Fast Ethernet 100Base-TX (Fast Ethernet, 100 Mbps).

fxp0: Management and internal Ethernet The management Ethernet interface is an out-of-band management interface within the routing platform.

fxp1: Interface that connects the routing engine and packet forwarding engine.

xe: 1GE optical interface on ex switches

ge: Gigabit and 10gigabit Ethernet. Includes Gigabit Ethernet IQ interfaces.

me0: - out of band management interface on ex switches

lo: Loopback This interface is internally generated. The logical interface lo0.16383 is a non-configurable interface for routing platform control traffic.

vcp: - virtual chassis interface (EX4200 only)

Other ones you may run into:

ae: Aggregated Ethernet A virtual aggregated link.

****as: Aggregated SONET/SDH A virtual aggregated link.

****at: ATM1 or ATM2 IQ Asynchronous Transfer Mode

****cau4: Channelized AU-4 IQ Configured on the Channelized STM-1 IQ PIC.

****coc1: Channelized OC-1 IQ Configured on the Channelized OC-12 IQ PIC.

****coc12: Channelized OC-12 IQ Configured on the Channelized OC-12 IQ PIC.

****cstm1: Channelized STM-1 IQ Configured on the Channelized STM-1 IQ PIC.

****ce1: Channelized E1 IQ Configured on the Channelized E1 IQ PIC or Channelized STM-1 IQ PIC.

****ct1: Channelized T1 IQ Configured on the Channelized DS-3 IQ PIC or Channelized OC-12 IQ PIC.

****ct3: Channelized T3 IQ Configured on the Channelized DS-3 IQ PIC or Channelized OC-12 IQ PIC.

****cp: Collector Configured on the Monitoring Services II PIC.

****ds: DS-0 Configured on the Channelized DS-3 to DS-0 PIC, Channelized E1 PIC, Channelized OC-12 IQ PIC,

****dsc: Discard Allows you to identify the ingress point of a denial-of-service (DoS) attack.

****e1: E1 Includes the channelized STM-1 to E1 interfaces.

****e3: E3 Includes the E3 IQ interfaces.

****es: Encryption, Allows you to configure a security association (SA) name with a logical interface.

****gr: Generic Route Encapsulation tunnel Allows you to configure a unicast tunnel using GRE encapsulation.

****gre: Internally generated This interface is internally generated and is not configurable.

****ip: IP-over-IP encapsulation tunnel Allows you to configure a unicast tunnel using IP-IP encapsulation.

****ipip: Internally generated This interface is internally generated and is not configurable.

****ls: Link services Supports bundles that contain links.

****lsi: Internally generated This interface is internally generated and is not configurable.

****ml: Multilink Includes Multilink Frame Relay and Multilink PPP.

****mo: Monitoring services Includes the monitoring services and monitoring services
II interfaces: The logical interface mo-fpc/pic/port.16383 is an internally generated, non-configurable interface for routing platform control traffic.

****mt: Multicast tunnel Internal routing platform interface for VPNs.

****mtun: Internally generated This interface is internally generated and is not configurable.

****oc3: OC-3 IQ Configured on the Channelized OC-12 IQ PIC.

****pe: This interface is present on the first-hop routing platform. Encapsulates packets destined for the rendezvous point (RP) routing platform.

****pd: This interface is present on the RP De-encapsulates packets at the RP.

****pimd: Internally generated This interface is internally generated and is not configurable.

****pime: Internally generated This interface is internally generated and is not configurable.

****rlsq: - a redundant bundle interface, made of two or more lsq interface. If you have redundant AS Pics.

****se: Serial Includes the EIA-530, V.35, and X.21 interfaces.

****so: SONET/SDH Both are widely used methods for very high speed transmission of voice and data signals across the numerous world-wide fiber-optic networks.

****sp: Adaptive services The logical interface sp-fpc/pic/port.16383 is an internally generated, non-configurable interface for routing platform control traffic.

****t1: T1 Includes the channelized DS-3 to DS-1 interfaces.

****t3: T3 Includes the channelized OC-12 to DS-3 interfaces.

****tap: Internally generated This interface is internally generated and is not configurable.

****vsp: Voice services, The Adaptive Services (AS) Physical Interface Card (PIC) supports the compressed real-time transport protocol (RTP) on this interface.

****vt: Virtual loopback tunnel On routing platforms equipped with a Tunnel PIC, enables egress filtering.
****Other interesting terminology regarding the juniper architecture is the module layout:

<b>RE: Routing Engine, Like a cisco supervisor module. Central brains of the system

****PFE: Packet forwarding Engine. Controls the data packet forwarding of the system.

****SCB: Switch control board. Contains ASICs that handle route lookups and memory management.

****PIC: Physical interface card. Sort of like a port, but can contain multiple interfaces.

****FPC: Flexible PIC concentrator. Like a linecard that has module slots. Can handle different types of PICs**
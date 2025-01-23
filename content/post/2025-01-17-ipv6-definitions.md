---
title: Defining IPv6 operating modes
date: 2025-01-17
author: Nick Buraglio
layout: post
categories:
    - configuration
    - ipv6-only
    - ipv6
    - ietf
tags:
    - ipv6
    - ietf
---

Since IPv6 is gaining momentum, and is generally operating alongside other protocols, it has become important to define the operating modes that may exist in any IPv6 environment. This allows for consistent communication and understanding of a fundamental part of operating a production network. Most of this hard work has been done by the IETF, and 99% of those definitions as can be referenced by engineers and architects when creating designs, proposals, and documentation, can be found in one really well crafted RFC. Within the [RFC8925](https://www.rfc-editor.org/rfc/rfc8925.html) terminology section there are easy to understand definitions for most operating modes that an engineer will see in the wild. As this is an RFC that defines an operational option for running a network, it is very complete in its description of operational models.

* Dual-stack network or device:
A network or device that has both versions of the Internet Protocol (IPv4 and IPv6) enabled and operational.

* IPv6-only-capable host:

`A host that does not require an IPv4 address and can operate on IPv6-only networks. More precisely, IPv6-only capability is specific to a given interface of the host: if some applications on a host require IPv4 and the 464XLAT CLAT (customer-side translator) [RFC6877] is only enabled on one interface, the host is IPv6-only capable if connected to a NAT64 network via that interface. This document implies that IPv6-only-capable hosts reach IPv4-only destinations via a NAT64 service provided by the network. Section 4 discusses hypothetical scenarios for other transition technologies being used.`

* IPv4-requiring host:

`A host that is not IPv6-only capable and cannot operate in an IPv6-only network providing NAT64 service.`

* IPv4 on demand:

`A deployment scenario where end hosts are expected to operate in IPv6-only mode by default and IPv4 addresses can be assigned to some hosts if those hosts explicitly opt in to receive IPv4 addresses.`

* IPv6-mostly network:

`A network that provides NAT64 (possibly with DNS64) service as well as IPv4 connectivity and allows the coexistence of IPv6-only, dual-stack, and IPv4-only hosts on the same segment. Such a deployment scenario allows operators to incrementally turn off IPv4 on end hosts, while still providing IPv4 to devices that require IPv4 to operate. But IPv6-only-capable devices need not be assigned IPv4 addresses.`

* IPv6-only mode:

`A mode of operation where a host acts as an IPv6-only-capable host and does not have IPv4 addresses assigned (except that IPv4 link-local addresses [RFC3927] may have been configured).`

* IPv6-only network:

`A network that does not provide routing functionality for IPv4 packets. Such networks may or may not allow intra-LAN IPv4 connectivity. An IPv6-only network usually provides access to IPv4-only resources via NAT64 [RFC6146].`

In addition to these definitions, and given my experience with migrating off of legacy IP, I propose two additional definitions. Please note that these are as I have defined them personally, based on my experience disabling IPv4 and running as what I can describe as "Practical IPv6-only":

* Practical IPv6-only

`This is very close to the above definition of an IPv6-only node, combining the node definition with the notion of the IPv6-only network. Further, a practical IPv6-only deployment does not preclude the use of concepts such as IPv4 loopback addressing, NAT64 access to legacy IP resources, or intra-system communications. Internal system communications may be IPv4-only, dual stacked, or IPv6-only. Examples of internal system communications may be, but are not limited to intra-shelf communications such as backplane communications internal to an optical platform, within a closed (i.e. air-gapped) system such as an optical service channel (OSC), within a containerization cluster, or between stacked network devices using dedicated stacking cabling enabling the functional extension of a network device backplane. Legacy IP may exist, but is limited to communication within a constrained, and contained element or set of elements, or in a central location used for communication to legacy resources.`

* Ideal IPv6-only

`Similar to IPv6-only mode, a mode of operation where a host acts as an IPv6-only-capable host and does not have IPv4 addresses assigned, can only operate on IPv6, both internally and externally. All internal host communications are devoid of IPv4 (i.e. no loopback 127.0.0.1). This is an idealistic approach that is likely not operationally feasible outside experimental or isolated environments with complete control of all aspects of the host operating systems, network element, and capabilities.`
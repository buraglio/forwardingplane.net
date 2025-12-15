---
id: 527
title: 'Building a Bridge Domain on MX series JunOS'
date: '2013-03-09T10:48:48-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=527'
permalink: /2013/03/09/building-a-bridge-domain-on-mx-series-junos/
themeblvd_keywords:
    - 'Juniper, routing, switching, junos, layer 3, layer 2'
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'Configure transit vlans on MX series JunOS'
themeblvd_description:
    - 'How to confiure a transit vlan on an MX series JunOS device in conjunction with a layer3 unit. '
dsq_thread_id:
    - '3626763679'
Views:
    - '2964'
categories:
    - How-To
    - 'Lab Time'
    - Routing
---

I started working on Juniper equipment around 2002. At my employer, we had an M40 with the serial number 256.  We did Layer3 only.  I had no idea if the Juniper even did layer2.  It certainly wasn't a layer3 switch like a 6500 like I was used to.  It was like a deliciously robust version of any Layer 3 router I'd worked on previously.  Over the years [Juniper](http://www.juniper.net/us/en/) has added a [switching line](http://www.juniper.net/us/en/products-services/switching/ex-series/) utilizing their FreeBSD based OS, [JunOS](http://www.juniper.net/us/en/products-services/nos/junos/).
All that being said, I'd never really messed with doing a layer2 transit VLAN on a JunOS routing platform.  Lets say we want to make 2 VLANs and transit them up through the WAN.  Here is how to make it work on an MX:
Create the bridge domains:

```
set bridge-domains vlan-123 domain-type bridge
set bridge-domains vlan-123 vlan-id 123
set bridge-domains vlan-124 domain-type bridge
set bridge-domains vlan-123 vlan-id 124

```

Configure the interfaces facing south (LAN) to nbe members of the VLAN:

```

set interfaces xe-1/0/0 description "SW1 xe-1/1/0"
set interfaces xe-1/0/0 mtu 9192
set interfaces xe-1/0/0 unit 0 description "Untagged VLAN 123"
set interfaces xe-1/0/0 unit 0 family bridge interface-mode access
set interfaces xe-1/0/0 unit 0 family bridge vlan-id 123
set interfaces xe-1/0/1 description "SW1 xe-1/1/1"
set interfaces xe-1/0/1 mtu 9192
set interfaces xe-1/0/1 unit 0 description "Untagged VLAN 123"
set interfaces xe-1/0/1 unit 0 family bridge interface-mode access
set interfaces xe-1/0/1 unit 0 family bridge vlan-id 123
set interfaces xe-1/0/2 description "SW2 xe-1/1/2"
set interfaces xe-1/0/2 mtu 9192
set interfaces xe-1/0/2 unit 0 description "Untagged VLAN 124"
set interfaces xe-1/0/2 unit 0 family bridge interface-mode access
set interfaces xe-1/0/2 unit 0 family bridge vlan-id 124
set interfaces xe-1/0/3 description "SW2 xe-1/1/3"
set interfaces xe-1/0/3 mtu 9192
set interfaces xe-1/0/3 unit 0 description "Untagged VLAN 124"
set interfaces xe-1/0/3 unit 0 family bridge interface-mode access
set interfaces xe-1/0/3 unit 0 family bridge vlan-id 124

```

Now add it to the uplink (that in this case has a layer3 instance on it as well):

```

set interfaces et-5/0/0 description "100G North"
set interfaces et-5/0/0 vlan-tagging
set interfaces et-5/0/0 mtu 9192
set interfaces et-5/0/0 unit 123 description "L3 testing vlan 123"
set interfaces et-5/0/0 unit 123 family bridge interface-mode trunk
set interfaces et-5/0/0 unit 123 family bridge vlan-id-list 123
set interfaces et-5/0/0 unit 124 description "L3 testing vlan 124"
set interfaces et-5/0/0 unit 124 family bridge interface-mode trunk
set interfaces et-5/0/0 unit 124 family bridge vlan-id-list 124
set interfaces et-5/0/0 unit 100 description "VLAN100 Layer3 Peering"
set interfaces et-5/0/0 unit 100 vlan-id 100
set interfaces et-5/0/0 unit 100 family inet mtu 9000
set interfaces et-5/0/0 unit 100 family inet address 10.100.100.1/30
set interfaces et-5/0/0 unit 100 family inet6 mtu 9000
set interfaces et-5/0/0 unit 10 family inet6 address 2001:fd8:a100:100::1/64

```

Now check your bridge table:

```

buraglio@mx480> show bridge domain
Routing instance Bridge domain VLAN ID Interfaces
default-switch vlan-123 123
                                                             et-5/0/0.123
                                                             xe-1/0/0.0
                                                             xe-1/0/1.0
default-switch vlan-124 124
                                                             et-5/0/0.124
                                                             xe-1/0/2.0
                                                             xe-1/0/3.0

```

That's it. Pretty straightforward. 
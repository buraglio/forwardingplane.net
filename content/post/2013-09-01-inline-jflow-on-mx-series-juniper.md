---
id: 770
title: 'Inline-jflow on MX series Juniper'
date: '2013-09-01T09:40:29-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=770'
permalink: /2013/09/01/inline-jflow-on-mx-series-juniper/
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'Enable inline-jflow for netflow functinality on Juniper MX platform'
themeblvd_keywords:
    - 'Juniper, ipfix, junos, inline-jflow, arbor, solarwinds, netflow, ipv6'
themeblvd_description:
    - 'Enable inline-jflow for one to one IPFIX / netflow functinality on Juniper MX platform.'
dsq_thread_id:
    - '3626762109'
Views:
    - '3573'
categories:
    - How-To
    - Routing
    - Security
---

One of the things that I've always lamented about using non-Cisco hardware is the lack of true 1:1 [netflow](http://en.wikipedia.org/wiki/Netflow) support.  Say what you will about jflow, cflow, sflow....there is no substitute for netflow, with sflow being the exception to that since it is a protocol that inherently supports ipv6 and <a title="Host based sflow, or, sflow for more than just network traffic" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/" target="_blank" rel="noopener noreferrer">can transport far more than simple network information</a> if configured in certain ways on certain devices.
On newer MX series Juniper routers the game has changed.  One to one flow data export (in IPFIX format) is now available, in hardware, for IPv4 and IPv6.  Queue the service providers rejoice.  Configuring this on the MX is a tad more involved than a Cisco, but it's still pretty straightforward.
In set commands:

```
 buraglio@mx480> show configuration forwarding-options | display set
 set forwarding-options sampling traceoptions file ipfix.log
 set forwarding-options sampling traceoptions file size 10k
 set forwarding-options sampling instance 1to1 input rate 1
 set forwarding-options sampling instance 1to1 family inet output flow-server \
 10.16.120.204 port 9995
 set forwarding-options sampling instance 1to1 family inet output flow-server \
 10.16.120.204 version-ipfix template ipv4
 set forwarding-options sampling instance 1to1 family inet output \
 inline-jflow source-address 10.16.120.1
 set forwarding-options sampling instance 1to1 family inet6 output flow-server \
 10.16.120.204 port 9995
 set forwarding-options sampling instance 1to1 family inet6 output flow-server \
 10.16.120.204 version-ipfix template ipv6
 set forwarding-options sampling instance 1to1 family inet6 output inline-jflow \
 source-address 10.16.120.1
```

Once the forwarding-options are set the chassis hardware has to be told what it can do.  Lets say you want to configure the inline-jflow on interfaces that exist on fpc0 (MPC0):

```
buraglio@ur1rtr> show configuration chassis fpc 0 | display set
set chassis fpc 0 pic 0 tunnel-services bandwidth 1g
set chassis fpc 0 pic 1 tunnel-services bandwidth 1g
set chassis fpc 0 sampling-instance 1to1
set chassis fpc 0 inline-services flow-table-size ipv4-flow-table-size 5
set chassis fpc 0 inline-services flow-table-size ipv6-flow-table-size 5
```

Notice we're referencing the sampling instance we created in the forwarding-options.  This tells the MPC (FPC) and MIC (PIC) that you want a traceoptions file (deactivate this after the setup is all working; I generaly keep a traceoptions section configured but deactivated in nearly every protocol for quick debugging.)  Enables the sampling instance we jut added to the forwarding options and sets the flow collector address and port.  It also sets the protocol as [IPFIX](http://en.wikipedia.org/wiki/IP_Flow_Information_Export) (Essentially netflow v9).  Now that we have the framework set up, we need to add the bits to the interface that tell it to sample the traffic

```
buraglio@ur1rtr> show configuration interfaces xe-0/0/1 | display set
set interfaces xe-0/0/1 description "trib port 1"
set interfaces xe-0/0/1 flexible-vlan-tagging
set interfaces xe-0/0/1 encapsulation flexible-ethernet-services
set interfaces xe-0/0/1 unit 105 description "Trib peering #1"
set interfaces xe-0/0/1 unit 105 vlan-id 1005
set interfaces xe-0/0/1 unit 105 family inet mtu 9000
set interfaces xe-0/0/1 unit 105 family inet sampling input
set interfaces xe-0/0/1 unit 105 family inet address 10.17.120.1/30
set interfaces xe-0/0/1 unit 105 family inet6 mtu 9000
set interfaces xe-0/0/1 unit 105 family inet6 sampling input
set interfaces xe-0/0/1 unit 105 family inet6 address 2001:DB8:1:dead:beef::1/64
```


```

```

Point this at your favorite flow collector and reap the benefits of having flow data. As far as collectors there are a lot of options, I prefer [nfdump](http://nfdump.sourceforge.net/)/[nfsen](http://nfsen.sourceforge.net/) because it's FOSS, very flexible, has [plugins](http://sourceforge.net/apps/trac/nfsen-plugins/) and is well supported, but there are fantastic commercial options for every flavor.  I've used the Arbor Peakflow and like it but it has a very expensive licensing model so it is generally deployed in larger environments.   I've also heard good things about the [SolarWinds Netflow Analyzer ](http://www.solarwinds.com/netflow-traffic-analyzer.aspx)but I've never used it.
Caveats:
On the older ichip platform with the MS-DPC you can view the actual flows on the box itself using the command <command>  much like show cef on a cisco.  I cannot find a way to do that on in the inline-jflow configuration on the trio hardware.
This was configured on JunOS 12.3R3.4 on MX480 hardware with MPC3/Trio hardware.
I can't seem to get the IPv6 flow data from the flow records.  I suspect it's either not in there yet or I've configured that part wrong.
-----EDIT-----
IPv6 flow data is working fine, flows are just being obfuscated by IPv4.  Using nfdump and singling out the IPv6 traffic shows what we expect:

```
nfdump -M /home/netflow/profiles-data/testlab/rtr1  -T  -r \
2013/09/03/nfcapd.201309030945 -n 20 -s ip/flows -6
nfdump filter:
inet6
Top 20 IP Addr ordered by flows:
---SNIP---
Summary: total flows: 19222, total bytes: 28.7 M, total packets: \
45173, avg bps: 732, avg pps: 0, avg bpp: 636
Time window: 2013-07-15 16:42:57 - 2013-09-03 09:50:20
Total flows processed: 4134975, Blocks skipped: 0, Bytes read: 281643580
Sys: 1.235s flows/second: 3345958.0  Wall: 1.770s flows/second: 2335921.0
```


```

```

---
title: 'Multicast through Juniper SRX 5800'
date: Sun, 17 Oct 2010 23:56:00 +0000
draft: false
tags: [Routing, Security]
---

We've been working toward a more simplified model for our network path, and in doing so, we desired a congruent path for IPv6, IPv4 Multicast and IPv4 Unicast.  
However, this is actually pretty hard when dealing with the link speeds, amounts of traffic and flows that we do, in conjunction with Firewall.....and IDP/IPS...  
Lots of research, reading and testing was done.  
Juniper SRX series has full support for 90% of this, with IPv6 IDP coming in Q2 of 2011.  
  
IPv4 Multicast is that unpleasant, poorly understood beast that most folks try to ignore. Nevertheless, we need it. So, we had to make this work through our SRX (in the past IPv4 multicast took a different path in/out of our network.

I'm going to glaze over the multicast bits on our Juniper MX routers, if you're doing multicast already, this should already be working and Juniper has well documented and well implemented multicast capabilities.

On the SRX, luckily, it's pretty similar.

  

buraglio@srx5800> show configuration protocols pim

rib-group inet multicast-rpf-rib;

rp {

static {

address 10.16.0.145;

}

}

interface xe-1/1/0.0;

interface xe-2/1/0.0;

interface xe-10/1/0.0;

interface xe-13/1/0.0;

  

{primary:node0}

  

Make sure you are importing the routes into the tables by configuring your RIB groups

  

buraglio@srx5800> show configuration routing-options rib-groups

igp-rib {

import-rib \[ inet.0 inet.2 \];

}

multicast-rpf-rib {

export-rib inet.2;

import-rib inet.2;

}

  

You'll need to make sure that there is a firewall policy to permit your multicast to actually flow. For arguments sake, I'm assuming you have an outbound policy that is less than or equal to this in terms of policy allowed.

  

{primary:node0}

buraglio@srx5800> show configuration security policies from-zone Untrust to-zone Trust policy Multicast-permit

match {

source-address any;

destination-address multicast\_224\_0\_0\_0\_4;

application junos-udp-any;

}

then {

permit;

log {

session-init;

}

}

  

Thats pretty much it as far as the SRX goes (assuming I'm remembering correctly, it's been a while since we did it and I don't know multicast as well as I'd like). Using the [cookbook from Internet2](http://globalnoc.iu.edu/i2network/multicast-cookbook.html) one should be enough to get Multicast working with your SRX as long as you have your policy set to allow it.

  

  

buraglio@srx5800> show multicast statistics

...snip...

Interface: xe-10/1/0.0

Routing protocol: PIM Mismatch error: 0

Mismatch: 8 Mismatch no route: 0

Kernel resolve: 287 Routing notify: 0

Resolve no route: 0 Resolve error: 0

Resolve filtered: 0 Notify filtered: 0

In kbytes: 4273 In packets: 45042

Out kbytes: 18014398509409554 Out packets: 18446744073709258616

Interface: xe-1/1/0.0

Routing protocol: PIM Mismatch error: 0

Mismatch: 11786 Mismatch no route: 3

Kernel resolve: 323210 Routing notify: 0

Resolve no route: 0 Resolve error: 0

Resolve filtered: 0 Notify filtered: 0

In kbytes: 100127811 In packets: 1164651571

Out kbytes: 10827919 Out packets: 80039321

...snip...

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
---
title: 'MPLS PseudoWire (VLL) between JunOS and Brocade MLX/XMR'
date: Sun, 19 May 2013 16:24:03 +0000
draft: false
tags: [Lab Time, Routing]
---

I love to be the "uncola" of networking sites.  I like interop and I don't do a lot with Cisco because I don't have access to much of their gear anymore.  So, that being the case, I had a need to bring up a l2circuit (in JunOS speak), or VLL (in Brocade speak) between an MX480 and an MLX.  Since they are very different platforms, I had to do some digging and playing around to get it to work. You should have a rudimentary understanding of MPLS (which is about what I have) to do this. l2circuit / pseudowire / vll are all synonymous for the scope of this post. JunOS:```
set protocols l2circuit neighbor interface virtual-circuit-id
set protocols l2circuit neighbor interface encapsulation-type ethernet

set interfaces xe-3/3/0 description
set interfaces xe-3/3/0 vlan-tagging
set interfaces xe-3/3/0 encapsulation flexible-ethernet-services
set interfaces xe-3/3/0 unit encapsulation vlan-ccc
set interfaces xe-3/3/0 unit vlan-id
```Brocade:```
MLX1#show mpls config
router mpls
policy
no propagate-ttl

mpls-interface e1/1
ldp-enable

mpls-interface e1/4
ldp-enable

vll TEST-ICCN-VLL-1 raw-mode
vll-peer
vlan
tagged e 5/2
```Some commands I found helpful for debugging while testing this out: JunOS: Useful for debugging connections that won't come up:```
set protocols l2circuit traceoptions file l2-VLL
set protocols l2circuit traceoptions file size 20240
set protocols l2circuit traceoptions flag all
show log l2-VLL
```Brocade:```
logging console
terminal monitor
debug mpls all
debug mpls ldp
```Show commands that are very useful: JunOS: check end to end l2circuit / VLL connectivity```
ping mpls l2circuit interface  detail
```Show detail of l2circuit / pseudowire / vll show interfaces extensive # or detail Brocade:```
show VLL detail 
```
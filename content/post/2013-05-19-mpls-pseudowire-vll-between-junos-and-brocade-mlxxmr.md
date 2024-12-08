---
id: 644
title: 'MPLS PseudoWire (VLL) between JunOS and Brocade MLX/XMR'
date: '2013-05-19T10:24:03-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=644'
permalink: /2013/05/19/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/
themeblvd_title:
    - 'MPLS Pseudowire between Juniper and Brocade'
themeblvd_keywords:
    - 'MPLS Pseudowire  Juniper Brocade VLL VPLS l2circuit junos'
themeblvd_description:
    - 'MPLS Pseudowire between Juniper and Brocade'
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3628689716'
Views:
    - '1715'
categories:
    - 'Lab Time'
    - Routing
---

I love to be the "uncola" of networking sites.  I like interop and I don't do a lot with Cisco because I don't have access to much of their gear anymore.  So, that being the case, I had a need to bring up a l2circuit (in JunOS speak), or VLL (in Brocade speak) between an MX480 and an MLX.  Since they are very different platforms, I had to do some digging and playing around to get it to work.
You should have a rudimentary understanding of MPLS (which is about what I have) to do this.  l2circuit / pseudowire / vll are all synonymous for the scope of this post.
JunOS:
<pre>set protocols l2circuit neighbor interface virtual-circuit-id
set protocols l2circuit neighbor interface encapsulation-type ethernet
set interfaces xe-3/3/0 description
set interfaces xe-3/3/0 vlan-tagging
set interfaces xe-3/3/0 encapsulation flexible-ethernet-services
set interfaces xe-3/3/0 unit encapsulation vlan-ccc
set interfaces xe-3/3/0 unit vlan-id</pre>
Brocade:
<pre>MLX1#show mpls config
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
tagged e 5/2</pre>
Some commands I found helpful for debugging while testing this out:
JunOS:
Useful for debugging connections that won't come up:
<pre>set protocols l2circuit traceoptions file l2-VLL
set protocols l2circuit traceoptions file size 20240
set protocols l2circuit traceoptions flag all
show log l2-VLL</pre>
Brocade:
<pre>logging console
terminal monitor
debug mpls all
debug mpls ldp</pre>
Show commands that are very useful:
JunOS:
check end to end l2circuit / VLL connectivity
<pre>ping mpls l2circuit interface <interface.unit> detail</pre>
Show detail of l2circuit / pseudowire / vll
show interfaces <interface.unit> extensive # or detail
Brocade:
<pre>show VLL detail <vll id></pre>

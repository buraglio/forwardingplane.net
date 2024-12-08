---
id: 2574
title: 'Mikrotik CG-NAT using NETMAP and hardware offload NAT'
date: '2023-05-09T14:07:16-05:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2574'
permalink: /2023/05/09/mikrotik-cg-nat-using-netmap-and-hardware-offload-nat/
Views:
    - '2739'
image: /wp-content/uploads/2023/05/5009Tik.png
categories:
    - How-To
    - NSP
tags:
    - NSP
---

<!-- wp:paragraph -->
<p>I will preface this with that I always say: <strong>do not implement this without IPv6 unless you literally have no other choice</strong>. IPv6 will allow for a significant resource offload because most eyeball services (Netflix, Youtube, Google, Facebook, etc.) will prefer IPv6, thus removing your requirement for more IPv4 NAT state and overload / port utilization. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Because I found no simple how-to for using NETMAP for CGN on a Mikrotik, here is one. This simple configuration will map all TCP ports 1024-9087 to 198.51.100.0/24 and all UDP ports from 1024-9087 to 192.0.2.0/24. This is a very simple configuration that can be adjusted and further refined with address-lists for the to-addresses, etc. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This was tested on an RB2004 running ROS 7.8</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>/ip firewall address-list add address=100.64.0.0/21 comment="CGN Client block 1" list=cgn1</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>/ip firewall nat add action=netmap chain=srcnat comment="TCP: NetMap TCP CGNAT Rule" out-interface=WAN protocol=tcp src-address-list=cgn1 to-addresses=198.51.100.0/24 to-ports=1024-9087</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>/ip firewall nat add action=netmap chain=srcnat comment="UDP: NetMap UDP CGNAT Rule" out-interface=WAN protocol=udp src-address-list=cgn1 to-addresses=192.0.2.0/24 to-ports=1024-9087</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This will essentially create a 4:1 ratio of client to NAT considering UDP and TCP as equal, which they will not be. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>/ip firewall nat add action=masquerade chain=srcnat comment="Masquerade to WAN Rule" out-interface=WAN src-address-list=masquerade-list</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It is also possible to offload NAT translations into hardware if your platform supports it, and requires some changes to the internal switch chip. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Assuming switch 0: </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><code>/interface/ethernet/switch&nbsp;set&nbsp;0&nbsp;l3-hw-offloading=yes</code><br><code>/interface/ethernet/switch/port&nbsp;set&nbsp;[find]&nbsp;l3-hw-offloading=yes</code><br><code>/interface/ethernet/switch/port&nbsp;set&nbsp;sfp-sfpplus2&nbsp;l3-hw-offloading=no</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And add the firewall filter rule:<br><code>/ip firewall filter add action=fasttrack-connection chain=forward comment="Hardware Offload for IPv4 Fasttrack" connection-state=established,related hw-offload=yes</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>There may be better ways to do this, but this worked in the case I needed it for. </p>
<!-- /wp:paragraph -->
---
id: 1626
title: 'FreeRouter as a test environment'
date: '2019-03-02T11:03:18-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1626'
permalink: /2019/03/02/freertr-as-a-lab-environment/
Views:
    - '957'
categories:
    - 'Lab Time'
    - Routing
    - Virtualization
---

<!-- wp:paragraph -->
<p>A few months ago <a href="https://www.stubarea51.net/about-me/">Kevin Myers</a> of <a href="https://www.iparchitechs.com/">IP Architechs</a> introduced me to a really interesting project called <a href="http://freerouter.nop.hu/">FreeRouter</a>. Being that I absolutely love alternative routing platforms and feature complete simulation environments, this really got me going. I tend to define "feature complete" in a routing platform as something that can do both IS-IS and MPLS. Given that there aren't many platforms that do both correctly or within a reasonable budget, and offer simulation options, I was pretty excited. I spent a fair amount of time pounding through it. I recommend spending some time with this if you have even remote interest in any of the above technologies. It costs nothing but your time. The project was written and is maintained by a Cisco CCIE and was built (according to his site) as a mechanism to learn. However, the feature list is incredibly complete, and extremely impressive, as seen below:</p>
<!-- /wp:paragraph -->
<!-- wp:preformatted -->
<pre class="wp-block-preformatted">forwarding: ipv4, ipv6, ipx, mpls, nsh, layer2, irb, atom, eompls, vpls, evpn<br />routing protocols: ospf, isis, bgp, rip, eigrp, babel, olsr, pim, msdp<br />lsp support: p2p, p2mp, mp2mp built by ldp, rsvp-te, sr, sr-te, bier<br />crypto: macsec, ipsec, ikev1, ikev2, tls, dtls, ssh, openvpn<br />tunnel: gre, ipip, l2tp, pptp, lisp, geneve, nvgre, vxlan, etherip<br />encapsulation: ethernet, vlan, nsh, ppp, framerelay, pwether, virtppp, hairpin<br />misc: acl, hqos, nat, pbr, srv6, vrrp, hsrp, transproxy, 6to4, rpl, tunnel, vpdn </pre>
<!-- /wp:preformatted -->
<!-- wp:paragraph -->
<p><a href="https://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/">My configurations</a> can be found in the <a href="https://www.forwardingplane.net/configuration-archive/">Configuration Archive</a> section of this site. It is definitely worth your time to check out. </p>
<!-- /wp:paragraph -->
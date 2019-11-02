---
title: 'FreeRouter as a test environment'
date: Sat, 02 Mar 2019 17:03:18 +0000
draft: false
tags: [Lab Time, Routing, Virtualization]
---

A few months ago [Kevin Myers](https://www.stubarea51.net/about-me/) of [IP Architechs](https://www.iparchitechs.com/) introduced me to a really interesting project called [FreeRouter](http://freerouter.nop.hu/). Being that I absolutely love alternative routing platforms and feature complete simulation environments, this really got me going. I tend to define "feature complete" in a routing platform as something that can do both IS-IS and MPLS. Given that there aren't many platforms that do both correctly or within a reasonable budget, and offer simulation options, I was pretty excited. I spent a fair amount of time pounding through it. I recommend spending some time with this if you have even remote interest in any of the above technologies. It costs nothing but your time. The project was written and is maintained by a Cisco CCIE and was built (according to his site) as a mechanism to learn. However, the feature list is incredibly complete, and extremely impressive, as seen below:

```
forwarding: ipv4, ipv6, ipx, mpls, nsh, layer2, irb, atom, eompls, vpls, evpn  
routing protocols: ospf, isis, bgp, rip, eigrp, babel, olsr, pim, msdp  
lsp support: p2p, p2mp, mp2mp built by ldp, rsvp-te, sr, sr-te, bier  
crypto: macsec, ipsec, ikev1, ikev2, tls, dtls, ssh, openvpn  
tunnel: gre, ipip, l2tp, pptp, lisp, geneve, nvgre, vxlan, etherip  
encapsulation: ethernet, vlan, nsh, ppp, framerelay, pwether, virtppp, hairpin  
misc: acl, hqos, nat, pbr, srv6, vrrp, hsrp, transproxy, 6to4, rpl, tunnel, vpdn 
```

[My configurations](https://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/) can be found in the [Configuration Archive](https://www.forwardingplane.net/configuration-archive/) section of this site. It is definitely worth your time to check out.
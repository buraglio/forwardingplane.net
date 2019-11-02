---
title: 'Setting IPv6 precedence under FreeBSD'
date: Thu, 02 Sep 2010 18:44:00 +0000
draft: false
tags: [Uncategorized]
---

I had been discussing [IPv6](http://en.wikipedia.org/wiki/IPv6) address precedence recently and realized that I'd never really messed with it.  I have a FreeBSD host that has multiple IPv6 addresses, an [EUI-64](http://standards.ieee.org/regauth/oui/tutorials/EUI64.html) address as well as a statically assigned address.  If you don't know what IPv6 or [EUI-64](http://standards.ieee.org/regauth/oui/tutorials/EUI64.html) is, I suggest you brush up because [IPv6](http://en.wikipedia.org/wiki/IPv6) is coming and it's coming sooner than you thing.  
  
Using the [ip6addrctl](http://man.freetechsecrets.com/ip6addrctl.8.html) command I can manipulate which  address is preferred for outbound connections.  
  
  
\[buraglio@synack:~ \] ip6addrctl show                                                                                          
Prefix                          Prec Label      Use  
::1/128                           50     0        0  
::/0                              40     1  1165005  
2002::/16                         30     2        0  
::/96                             20     3        0  
::ffff:0.0.0.0/96                 10     4        0  
2620:0:e00:4000::/64               1     0       63  

  

This is the default configuration on my FreeBSD 7.1 machine.  Here we can see that I have several IPv6 addresses:

  

\[buraglio@synack:~ \] ifconfig                                                                                               <1215>

le0: flags=8843 metric 0 mtu 1500

options=8

ether 00:0c:29:b6:96:ba

inet6 fe80::20c:29ff:feb6:96ba%le0 prefixlen 64 scopeid 0x1 

inet6 2620:0:e00:4000::146 prefixlen 64 

inet6 2620:0:e00:4000:20c:29ff:feb6:96ba prefixlen 64 

inet 128.174.43.146 netmask 0xffffff80 broadcast 128.174.43.255

media: Ethernet autoselect

status: active

  

Obviously the fe80 address is my link local.  The 2620:0:e00:4000::146 is a manually assigned address and 2620:0:e00:4000:20c:29ff:feb6:96ba is my [EUI-64](http://standards.ieee.org/regauth/oui/tutorials/EUI64.html) address.I believe the default behavior on FreeBSD is to prefer the manually configured address, which is the behavior that is exhibited when I test it.  

  

buraglio@synack:~ \] ping6 remote.buraglio.com                                                                              <1218>

PING6(56=40+8+8 bytes) 2620:0:e00:4000::146 --> 2607:f2f8:4980::2

16 bytes from 2607:f2f8:4980::2, icmp\_seq=0 hlim=47 time=44.454 ms

16 bytes from 2607:f2f8:4980::2, icmp\_seq=1 hlim=47 time=64.172 ms

  

results in

  

\[buraglio@collector:~ \] sudo tcpdump ip6 proto 58

  

08:30:17.381695 IP6 2620:0:e00:4000::146 > 2607:f2f8:4980::2: ICMP6, echo request, seq 0, length 16

08:30:17.381781 IP6 2607:f2f8:4980::2 > 2620:0:e00:4000::146: ICMP6, echo reply, seq 0, length 16

08:30:18.951558 IP6 2620:0:e00:4000::146 > 2607:f2f8:4980::2: ICMP6, echo request, seq 1, length 16

08:30:18.951641 IP6 2607:f2f8:4980::2 > 2620:0:e00:4000::146: ICMP6, echo reply, seq 1, length 16

  

If I change the precedence to prefer the EUI-64 address, it will source that traffic from there, as such:  

sudo ip6addrctl add 2620:0:e00:4000:20c:29ff:feb6:96ba/64 1 primary                              

  
and do the experiment again, I see different results.
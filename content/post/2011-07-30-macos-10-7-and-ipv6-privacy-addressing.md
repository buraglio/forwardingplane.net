---
id: 32
title: 'MacOS 10.7 and IPv6 privacy addressing'
date: '2011-07-30T20:40:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/'
permalink: /2011/07/30/macos-10-7-and-ipv6-privacy-addressing/
dsq_thread_id:
    - '4185424321'
Views:
    - '105'
categories:
    - IPv6
    - UNIX
---

I'm not a fan of IPv6 privacy addressing. I understand the logic behind it, I really doo, obfuscate the LLADDR (MAC address) of the host in question, but I really dont't see the realistic purpose. If someone wanted to use my mac address, what good would that really get them, unless they're on the same layer 2 segment? More importantly, if they;re on the same layer 2 segment, they have my MAC address anyway.**Privacy addresses cause more heartburn than they cure. How do I track someone who has a rotating address? Am I scraping the neighbor table of my network equipment often enough to have reasonable accountability? Probably, but what if I'm not? I could go on and on about how I think [RFC4941](http://www.ietf.org/rfc/rfc4941.txt) addresses aren't that useful, but instead I'll just write down how to disable them (I've always been known as more of a machete than a scalpel anyway =).

With MacOS 10.7 (Lion) it's now on by default. To disable it, you need to open a terminal and type:

*sudo sysctl -w net.inet6.ip6.use_tempaddr=0
*
Poof! There you go.[ You should be using DHCPv6 anyway](http://tech.buraglio.com/2011/07/osx-107-lion-dhcpv6-client-working-with.html) =)[ ](http://events.internet2.edu/2011/jt-uaf/agenda.cfm?go=session&id=10001852&event=1151)[*

**cue vendors getting off their rear ends and implementing dhcpv6 relay**
*](http://events.internet2.edu/2011/jt-uaf/agenda.cfm?go=session&id=10001852&event=1151)

*---edit---**
**A good point made by Charley Kline, to make this persist across reboots a line needs to be added to your /etc/sysctl.conf. 
****To accomplish this, edit /etc/sysctl.conf
*****sudo vi /etc/sysctl.conf
****Add the following line:
*****net.inet6.ip6.use_tempaddr=0
```

```
****--edit--**
For all you windows users:

XP:
*netsh interface ipv6 set privacy state=disabled store=persistent
netsh interface ipv6 set privacy state=disabled*

Vista:

*netsh interface ipv6 set global randomizeidentifiers=disabled
netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent
netsh interface ipv6 set privacy disabled*

I assume Windows 7 is similar to Vista, but I have not tested.
---
id: 32
title: 'MacOS 10.7 and IPv6 privacy addressing'
date: '2011-07-30T20:40:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/'
permalink: /2011/07/30/macos-10-7-and-ipv6-privacy-addressing/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2011/07/macos-107-and-ipv6-privacy-addressing.html
dsq_thread_id:
    - '4185424321'
Views:
    - '105'
categories:
    - IPv6
    - UNIX
---

I'm not a fan of IPv6 privacy addressing.  I understand the logic behind it, I really doo, obfuscate the LLADDR (MAC address) of the host in question, but I really dont't see the realistic purpose.  If someone wanted to use my mac address, what good would that really get them, unless they're on the same layer 2 segment?  More importantly, if they;re on the same layer 2 segment, they have my MAC address anyway.<br />Privacy addresses cause more heartburn than they cure.  How do I track someone who has a rotating address?  Am I scraping the neighbor table of my network equipment often enough to have reasonable accountability?  Probably, but what if I'm not?   I could go on and on about how I think <a href="http://www.ietf.org/rfc/rfc4941.txt">RFC4941</a> addresses aren't that useful, but instead I'll just write down how to disable them (I've always been known as more of a machete than a scalpel anyway =).<br /><br />With MacOS 10.7 (Lion) it's now on by default.  To disable it, you need to open a terminal and type:<br /><br /><span><i>sudo sysctl -w net.inet6.ip6.use_tempaddr=0<br /></i></span><br />Poof!  There you go.<a href="http://tech.buraglio.com/2011/07/osx-107-lion-dhcpv6-client-working-with.html">  You should be using DHCPv6 anyway</a> =)<a href="http://events.internet2.edu/2011/jt-uaf/agenda.cfm?go=session&id=10001852&event=1151">  </a><a href="http://events.internet2.edu/2011/jt-uaf/agenda.cfm?go=session&id=10001852&event=1151"><b>*cue vendors getting off their rear ends and implementing dhcpv6 relay*</b></a><div><br /></div><div><b>---edit---</b></div><div><b>A good point made by Charley Kline, to make this persist across reboots a line needs to be added to your /etc/sysctl.conf.  </b></div><div><b><br /></b></div><div><b>To accomplish this, edit /etc/sysctl.conf</b></div><div><b><br /></b></div><div><i><b>sudo vi /etc/sysctl.conf</b></i></div><div><b><br /></b></div><div><b>Add the following line:</b></div><div><b><br /></b></div><div><i><b>net.inet6.ip6.use_tempaddr=0</b></i></div><div><span style="font-family: Helvetica, Arial, sans-serif; font-size: 13px; line-height: 17px; "><b><pre style="padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; text-align: left; overflow-x: auto; overflow-y: auto; font-family: 'Courier New', Courier, monospace; line-height: 1.3; "></pre></b></span></div><div><b>--edit--</b></div><div><br /></div><div>For all you windows users:<br /><br />XP:<div><br /><span><i>netsh interface ipv6 set privacy state=disabled store=persistent<br />netsh interface ipv6 set privacy state=disabled</i></span><br /><br />Vista:<br /><br /><span><i>netsh interface ipv6 set global randomizeidentifiers=disabled<br />netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent<br />netsh interface ipv6 set privacy disabled</i></span><br /><br />I assume Windows 7 is similar to Vista, but I have not tested.</div></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
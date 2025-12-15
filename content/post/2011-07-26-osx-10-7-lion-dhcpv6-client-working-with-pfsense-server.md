---
id: 33
title: 'OSX (10.7; Lion) DHCPv6 client working with pfsense server.'
date: '2011-07-26T12:20:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/07/osx-10-7-lion-dhcpv6-client-working-with-pfsense-server/'
permalink: /2011/07/26/osx-10-7-lion-dhcpv6-client-working-with-pfsense-server/
dsq_thread_id:
    - '3640194170'
Views:
    - '75'
categories:
    - IPv6
    - Musings
    - UNIX
---

It looks like MacOS 10.7 (Lion) has fully functioning DHCPv6. It's about time.

Before:

[![](http://1.bp.blogspot.com/-6FQwzCiawpg/TjDWmwrbONI/AAAAAAAAAEI/9mOtP9fMbqE/s400/Screen%2BShot%2B2011-07-25%2Bat%2B8.45.24%2BPM.png)](http://1.bp.blogspot.com/-6FQwzCiawpg/TjDWmwrbONI/AAAAAAAAAEI/9mOtP9fMbqE/s1600/Screen%2BShot%2B2011-07-25%2Bat%2B8.45.24%2BPM.png)

After:

[![](http://4.bp.blogspot.com/-stFnUb3g1zI/TjDW1MDpOyI/AAAAAAAAAEY/YgG7fXCfujY/s400/Screen%2BShot%2B2011-07-26%2Bat%2B7.18.45%2BAM.png)](http://4.bp.blogspot.com/-stFnUb3g1zI/TjDW1MDpOyI/AAAAAAAAAEY/YgG7fXCfujY/s1600/Screen%2BShot%2B2011-07-26%2Bat%2B7.18.45%2BAM.png)

pfSense setup:

[![](http://2.bp.blogspot.com/-gSN5Rx7vIUU/TjDW0t1BcEI/AAAAAAAAAEQ/1hQNIlCJl30/s400/Screen%2BShot%2B2011-07-26%2Bat%2B7.16.50%2BAM.png)](http://2.bp.blogspot.com/-gSN5Rx7vIUU/TjDW0t1BcEI/AAAAAAAAAEQ/1hQNIlCJl30/s1600/Screen%2BShot%2B2011-07-26%2Bat%2B7.16.50%2BAM.png)


Using Internet Systems Consortium DHCP Server 4.2.1-P1 as the server (on my pfSense box) I am able to get not only a privacy address (via stateless autoconfigure) but also a normal EUI-64 address as well as an IPv6 address via dhcpv6. 
I didn't do anything except use the "Automatic" setting in the network control panel, so out of the box OSX 10.7 "Lion" looks like it does the right thing with DHCPv6, at least at face value.



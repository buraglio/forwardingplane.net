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

It looks like MacOS 10.7 (Lion) has fully functioning DHCPv6. It's about time.<br /><br />Before:<br /><br /><a href="http://1.bp.blogspot.com/-6FQwzCiawpg/TjDWmwrbONI/AAAAAAAAAEI/9mOtP9fMbqE/s1600/Screen%2BShot%2B2011-07-25%2Bat%2B8.45.24%2BPM.png"><img style="cursor:pointer; cursor:hand;width: 400px; height: 343px;" src="http://1.bp.blogspot.com/-6FQwzCiawpg/TjDWmwrbONI/AAAAAAAAAEI/9mOtP9fMbqE/s400/Screen%2BShot%2B2011-07-25%2Bat%2B8.45.24%2BPM.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5634239095230904530" /></a><br /><br />After:<br /><br /><a href="http://4.bp.blogspot.com/-stFnUb3g1zI/TjDW1MDpOyI/AAAAAAAAAEY/YgG7fXCfujY/s1600/Screen%2BShot%2B2011-07-26%2Bat%2B7.18.45%2BAM.png"><img style="cursor:pointer; cursor:hand;width: 400px; height: 366px;" src="http://4.bp.blogspot.com/-stFnUb3g1zI/TjDW1MDpOyI/AAAAAAAAAEY/YgG7fXCfujY/s400/Screen%2BShot%2B2011-07-26%2Bat%2B7.18.45%2BAM.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5634239343098411810" /></a><br /><br />pfSense setup:<br /><br /><a href="http://2.bp.blogspot.com/-gSN5Rx7vIUU/TjDW0t1BcEI/AAAAAAAAAEQ/1hQNIlCJl30/s1600/Screen%2BShot%2B2011-07-26%2Bat%2B7.16.50%2BAM.png"><img style="cursor:pointer; cursor:hand;width: 400px; height: 341px;" src="http://2.bp.blogspot.com/-gSN5Rx7vIUU/TjDW0t1BcEI/AAAAAAAAAEQ/1hQNIlCJl30/s400/Screen%2BShot%2B2011-07-26%2Bat%2B7.16.50%2BAM.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5634239334984020034" /></a><br /><br /><br /><br />Using Internet Systems Consortium DHCP Server 4.2.1-P1 as the server (on my pfSense box) I am able to get not only a privacy address (via stateless autoconfigure) but also a normal EUI-64 address as well as an IPv6 address via dhcpv6. <div><br /></div><div>I didn't do anything except use the "Automatic" setting in the network control panel, so out of the box OSX 10.7 "Lion" looks like it does the right thing with DHCPv6, at least at face value.<br /><br /><div><div><span><span style="white-space: pre;"><br /></span></span></div><div><br /></div><br /></div></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
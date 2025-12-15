---
id: 724
title: 'The sad state of IPv6 and why you need to learn it.'
date: '2013-08-05T05:18:03-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=724'
permalink: /2013/08/05/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'IPv6, NAT, Security, Soapbox, Nick Buraglio, buraglio, forwarding plane, juniper, junos, Cisco, IOS, IPv4, Security, tunnelbroker, OpenFlow, SDN'
themeblvd_title:
    - 'NAT is out. IPv6 is in. '
themeblvd_description:
    - 'NAT is only a stopgap. Enterprise and IT networking at large needs to embrace IPv6, it''s not going away. '
dsq_thread_id:
    - '3646771858'
Views:
    - '307'
categories:
    - IPv6
    - Musings
    - 'Soap Box'
---

I have been learning and using IPv6 for a quite a while, even before I worked in research and education, back in the ISP days.  I thought I should learn it because, frankly, I figured we'd all be converted to it by now, already whole hog using it like it was the layer 3 addressing mechanism that it is.  Flashback: My first IPv6 access was via a tunnel to HE a long, long time ago and before that I was reading what I could about it.  I've been evangelizing IPv6 for about that long, too.  I've taught IPv6 networking workshops on many occasions showing eager network engineers, security engineers, sysadmins, incident responders and even the occasional CIO how to understand, interpret and plumb v6.
Now, I love OpenFlow and SDN as much as the next network geek, and I think it's about as disruptive and game changing as the next guy.  However, IPv6 is next.  There.  I said it.  We need it.  Hey, OpenFlow 1.3 supports it so there is your tie in.  We're out of v4 for the most part and, lets be honest, NAT is a freaking abomination. It's not a solution to anything other than over complicating a transit path with translational mappings.
I recently received an email from a buddy from my first days in tech about [a project that some colleagues of his had been working on](http://www.enhancedip.org/home) and while at a base technical level it's an interesting concept, this project infuriated me.  This is the problem with the industry, especially in North America.
The right thing, in my opinion, is to put effort like this aside and concentrate on IPv6 development and deployment. Projects like this, while good intentioned and technically innovative, delay he inevitable and give lazy, "luddist" engineers and developers a way to keep ipv4 even longer. [![](http://www.forwardingplane.net/wp-content/uploads/2013/08/alarm_clock.jpg)](http://www.forwardingplane.net/wp-content/uploads/2013/08/alarm_clock.jpg)
I have mostly just kept this to myself publicly.  Sure, I blather on about it the office and preach about IPv6 over beers with networking professionals, but mostly I just suffer and bite my tongue when I hear some enterprise architect talk about firewalls, NAT, IPv4 only security appliances and how "they don't need IPv6" or how "the enterprise isn't ready" [for IPv6].
Wake up call, you're late. <script type="text/javascript" src="http://ipv6.he.net/v4ex/sidebar.js"></script>**IPv6 is here**.  It's **been** here.  It's all over in Asia and other parts of the world.  It's supported by default by your consumer service provider.  Guess what?  It's too bad that your lazy developers didn't code your apps for it. It's too bad that your specialized app only supports IPv4 and probably doesn't even understand DNS.  You'll eventually have to deal with IPv6.  In actuality, you're likely already using it and have no idea it is happening.  If someone finally tore that legacy XP machine from your change-despising hands you're probably tunneling your traffic.  Unless you explicitly disable IPv6 on a modern operating system, you're using it.  It may be just locally on your segment, but it's on.  [![](http://www.forwardingplane.net/wp-content/uploads/2013/08/borg.jpg)](http://www.forwardingplane.net/wp-content/uploads/2013/08/borg.jpg) Get on board.  Resistance is futile.  There are great resources for learning IPv6.  Your desktop and server OS have probably supported it for years.  Your routers likely support routing it.  The last parts are going to be the security devices, policy and the legacy apps.  If you're a networking guy, go do the [HE tunnelbroker certification process. ](http://ipv6.he.net/certification/) They have a very good fundamentals tutorial and it covers everything you need to know to get started.  You can also get a cool shirt and some code to shove into your website.  Mine looks like this:<script type="text/javascript" src="http://ipv6.he.net/certification/badge.js" language="javascript"></script><script type="text/javascript">// <![CDATA[
var user = "buraglio"; display_swf(user);
// ]]></script>
 
Take the plunge, get some IPv6 going in your enterprise, home network, lab, whatever.  Learn and educate.  It will only improve your value and you're going to have to learn it later anyway.
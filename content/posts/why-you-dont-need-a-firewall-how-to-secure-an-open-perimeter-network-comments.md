---
title: 'Why you don''t need a firewall [how to secure an open perimeter network]'
date: Mon, 08 Sep 2014 07:30:07 +0000
draft: false
tags: [IPv6, Routing, SDN, Security, Soap Box]
---


#### 
[cryptochrome]( "sascha@picchiantano.de") - <time datetime="2014-09-08 02:11:00">Sep 1, 2014</time>

Wow. I completely disagree. Just because a firewall can give you some headaches in your network environment it shouldn't be a reason to just dump it. A very dangerous proposition, and your "alternatives" will not be enough. Fix your firewall if it causes issues.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2014-09-08 08:53:00">Sep 1, 2014</time>

Like I said, it's not for everyone, but there are very real use cases where there is no hardware firewall that does what is necessary. For example, how do you firewall 100G WAN connectivity and still retain the ability to do >10Gbps flows? What firewall can handle 40Gbps flows end to end for things like gridftp? How would a typical firewall handle experimental protocols like named data networking? For 95% of the normal users, a generic security appliance is probably fine. There are, however, things that they just don't work for. I'm in no way proposing that some random bank go and remove its border firewall, but running without a perimeter device can be done and it is useful to think about because it's really not that hard. I have done it in one way or another for more than a decade. That is not to say that there are not firewalls or appliances in the network somewhere, but they're not at the perimeter and they are provisioned for extremely specific purposes. I could probably successfully argue that they are more efficient because of that alone.
<hr />

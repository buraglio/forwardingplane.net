---
id: 50
title: 'SRX IPv6 flow based processing'
date: '2010-09-16T11:18:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/'
permalink: /2010/09/16/srx-ipv6-flow-based-processing/
dsq_thread_id:
    - '3634721127'
Views:
    - '121'
categories:
    - IPv6
    - Security
---

One of our plans is to consolidate as many of the egress trafic paths as possible.  To facilitate this, we had to do some things like buy carrier grade equipment.  Enter the [SRX 5800](http://bit.ly/9jrUiG).  No one really does IPS/IDP+Firewall quite like the SRX.  After extensive research and exhaustive hands on testing with quite a bit of equipment, that is what we settled on.  Even the IBM "technical evangelist" guy that came to talk to us said "No one really does it like they do" when referring to Juniper and 10G firewall/IPS. 

[![](http://www.juniper.net/shared/img/products/srx-series/srx5800/lbox-srx5800-left.jpg)](http://www.juniper.net/shared/img/products/srx-series/srx5800/lbox-srx5800-left.jpg)

Lets make one thing clear, IPv6 isn't going away.  We'll all be using in in the next few years, and so, to that end, it needs to work through our network as closely to the way folks are using the current resources as we can make it....within the confines of our resources and the limitations of IPv4 and IPv6 respectively.

To make IPv6 process similarly to IPv4 on the SRX 5800 cluster, we have to enable flow based security processing for it.  To make that happen, you have to do the following things, as documented [here](http://bit.ly/9jrUiG):

set security forwarding-options family inet6 mode flow-based


Enabling this actually requires a reboot of the boxes, and on a chassis cluster, I've been told by our Agility JTAC guy (and learned the herd way because I'm stubborn like that) that you need to reboot both cluster nodes at the same time (which I find dumb since the purpose of a firewall cluster is almost always redundancy).

Regardless, I used the recommended method and kicked the boxes after a commit check. 

commit check


The router then spits out the following information after the commit check:


node0:
warning: You have enabled/disabled inet6 flow.
You must reboot the system for your change to take effect.
If you have deployed a cluster, be sure to reboot all nodes.
configuration check succeeds

 

 
node1:
warning: You have enabled/disabled inet6 flow.
You must reboot the system for your change to take effect.
If you have deployed a cluster, be sure to reboot all nodes.
configuration check succeeds


From here I like to comment all of my commits, as it's just good practice and it will be logged on your handy [syslog server](http://campin.net/syslog-ng/faq.html) for later use or reference.


commit comment "Enabling Flow-Based Processing for IPv6 Traffic"


And from there, a reboot of both nodes (at the same time) is necessary..

request system reboot


And then, we wait...... 

.....and wait some more...

....and then.....the prompt on the console is back.

...........and after about 6-7 minutes, we have OSPF adjacencies and packets are flowing.  The SPCs take a bit to self test, fully boot and start processing traffic, as I would expect from something processing so many pieces of so much traffic.  

Now we need to verify that what we did actually worked.  From the SRX, check the security flow status:


show security flow status


node0:
--------------------------------------------------------------------------
  Flow forwarding mode:
    Inet forwarding mode: flow based
    Inet6 forwarding mode: flow based
    MPLS forwarding mode: drop
    ISO forwarding mode: drop
    Flow trace status
    Flow tracing status: off


node1:
--------------------------------------------------------------------------
  Flow forwarding mode:
    Inet forwarding mode: flow based
    Inet6 forwarding mode: flow based
    MPLS forwarding mode: drop
    ISO forwarding mode: drop
    Flow trace status
    Flow tracing status: off


We're looking for:


    Inet6 forwarding mode: flow based
This would have said "drop" before the change. 

We hope to actually swing over our IPv6 traffic soon and start processing it on the SRXs.  I'll post notes as soon as we go forward with that.  



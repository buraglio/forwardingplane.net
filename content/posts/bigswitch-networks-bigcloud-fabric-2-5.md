---
title: 'BigSwitch Networks BigCloud Fabric 2.5'
date: Thu, 29 Jan 2015 01:04:46 +0000
draft: false
tags: [Lab Time, SDN]
---

[BigSwitch](http://www.bigswitch.com) is [making waves again](http://www.bigswitch.com/press-releases/2015/01/28/big-switch-networks-unveils-big-cloud-fabric-2_5?mkt_tok=3RkMMJWWfF9wsRonvqTIZKXonjHpfsX56eQrUKS2lMI%2F0ER3fOvrPUfGjI4ASMtrI%2BSLDwEYGJlv6SgFQ7fBMbd4yLgIXRA%3D), this time with its Big Cloud Fabric product update. I was lucky enough to get a bit of a preview of what was coming and was pleasantly surprised by the new features, finding them functionally useful for both operators, security folks and management alike.

Not only is the fabric fit to operate at hyper scale proportions, they've paid  close attention to making such operations even easier. With release 2.5 they're focusing more on white box switches and abstracting the control plane further, which is important to note because decoupling those things can prove to be confusing and complicated and doing so can make operation and service clunky if not done well. From what [I've seen and experienced in their fabric cloud training](http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/ "BigSwitch Labs for SDN learning: a sneak peek!") and in this update, it appears smooth and easy to use.

Something mentioned during this briefing that I found particularly cool was the notion of a starter kits. BigSwitch is making available a "kickstarter" of their big cloud fabric with available software, hardware, cables and optics; a turnkey SDN platform in a box. Where I could see this being convenient is for those looking to build out a lab, dip their toe into the SDN / data center fabric world or to build out a dedicated project. A nice option for sure.

BigSwitch is also adding support for VMWare VCenter and they're also adding support for the [dell open network switch](http://www.dell.com/us/business/p/open-networking-switches/pd) series to boot.

What really caught my eye, though, was the existence of a very robust looking set of analytics. An eye catching assortment of graphs, logs and functional data that is, get this, driven by an [elasticsearch](http://www.elasticsearch.com) back end.   What is included is useful not only for Network and SDN engineers, but also for security [![bsw-eyecandy](http://www.forwardingplane.net/wp-content/uploads/2015/01/bsw-eyecandy.png)](http://www.forwardingplane.net/wp-content/uploads/2015/01/bsw-eyecandy.png)professionals. Including things like event logs, fine grained search, canned reports for the execs and presenting everything via a REST API and a subset available via syslog for good measure I could see this being a very handy set of data for tracking down any number of things from incident response to problem resolution.

I look forward to seeing more from [BigSwitch](http://www.bigswitch.com).
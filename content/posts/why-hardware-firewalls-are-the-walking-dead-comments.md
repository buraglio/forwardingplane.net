---
title: 'Why hardware firewalls are the walking dead'
date: Mon, 18 Mar 2013 11:02:42 +0000
draft: false
tags: [Crystal Ball, OpenFlow, Security, Virtualization]
---


#### 
[cryptochrome (@cryptochrome)]( "sascha@picchiantano.de") - <time datetime="2013-03-21 16:06:30">Mar 4, 2013</time>

What everybody seems to forget is that actually simple stateful inspection firewalls are the walking dead. Modern firewalls do a lot of inspection at layer 7 (think Palo Alto Networks). I want to see one of those white box Intel boxes push 20 gigabit of application level firewalled traffic. I highly doubt it. And I am also curious how you want to put OpenFlow to use here, when basically every flow would need to be forwarded to the Controller and passed on to the "OpenFlow Firewall" for inspection. In other words: I don't believe you can get rid of ASICs just yet and you will need hardware firewalls for the forseeable future.
<hr />
#### 
[cryptochrome (@cryptochrome)]( "sascha@picchiantano.de") - <time datetime="2013-03-22 01:37:18">Mar 5, 2013</time>

The controller in an OpenFlow architecture also makes decisions for unknown/undefined flows. Flows that a switch doesn have in it's forwarding table are being sent to the controller. Now if you think of a firewall, it will naturally have truck loads full of unknown flows, especially if the firewall is placed at the edge/perimeter of a network. Don't get me wrong, I would personally welcome our new OpenFlow Firewall overlords :) But I just don't think that OpenFlow firewall setups would scale and perform anywhere near as good as dedicated, ASIC-based firewalls for a long time to come. I am talking real firewalls here, not simple enhanced ACLs (read: stateful packet inspection). If you reduce the OpenFlow controller to simply being the management system (policy definition etc.), then why use OpenFlow in the first place? We already have firewalls with separate management software. Nothing new.
<hr />
#### 
[Nuno]( "ndelgado29@gmail.com") - <time datetime="2013-03-21 19:44:00">Mar 4, 2013</time>

The controller in an OpenFlow architecture is only used for managing the firewalls, defining the policy, pushing the policy, and other overhead operations. The firewalls are left to do their core functions, so the traffic wouldn't need to be backhauled to the controller.
<hr />
#### 
[EtherealMind](http://etherealmind.com "greg.ferro@packetpushers.net") - <time datetime="2013-03-18 08:59:36">Mar 1, 2013</time>

I'm now working on the theory that I can flow balance white box Intel servers with a hypervisor. The hypervisor would host a VM that runs a firewall. Current Intel servers can handle up 40 Gbps of raw throughput so I'm expecting 50% in real use. Ten white box servers with rapid upgrades for both hardware and software sounds like a solution to me .....
<hr />
#### 
[EtherealMind](http://etherealmind.com "greg.ferro@packetpushers.net") - <time datetime="2013-03-22 01:48:54">Mar 5, 2013</time>

Not quite. There are controller architectures that put some controller functions, like packet inspection, into the device. Consider a master controller with the full database of thousands of rules could distribute OpenFlow entries that are relevant to exact device. Instead of one big firewall process running thousands of rules, I have hundreds of smaller devices running tens of rules. CPU is less important and security is improved since firewall are located where the data is.
<hr />
#### 
[cryptochrome (@cryptochrome)]( "sascha@picchiantano.de") - <time datetime="2013-03-22 02:22:32">Mar 5, 2013</time>

Interesting concept, Greg. Although that's already reality today without OpenFlow. Check Point Provider-1 management platform does exactly that. Junos Space does exactly that. Of course the nodes are not tiny cheap white boxes but expensive firewall appliances. Still, to me the question remains whether plain x86 hardware is able to scale when we are talking complex layer7 inspection, IPS, DDoS prevention etc. We've already seen Check Point fail miserably with their software-only firewalls when it comes to performance/throughput. There is a reason for Fortinet/Juniper(SRX) being selected over Check Point in large datacenter designs.
<hr />

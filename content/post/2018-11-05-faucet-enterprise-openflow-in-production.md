---
id: 1499
title: 'Faucet: Enterprise OpenFlow in production'
date: '2018-11-05T04:56:21-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1499'
permalink: /2018/11/05/faucet-enterprise-openflow-in-production/
Views:
    - '629'
categories:
    - How-To
    - SDN
    - Security
    - 'Soap Box'
tags:
    - OpenFlow
    - SDN
---

    Remember OpenFlow? It was the media and marketing darling for the better part of 5 years as “the machine” conflated OpenFlow with SDN and SDN with - almost literally - everything. "Still Does Nothing" was a common phrase uttered around those of us that had run large scale, complex networks for a long time. Quietly, [and mostly](https://faucet-sdn.blogspot.com/), out of the fickle media and blogosphere eye, a scrappy little SDN project called [faucet](https://github.com/faucetsdn/faucet) has been [diligently plugging away](https://github.com/faucetsdn/faucet) -- making easy to use, production quality, well documented, and very stable code that runs OpenFlow networks quite happily in production and at scale. Oh, did I mention that it's also got a very small footprint? Did I also mention that we've built a multi-terabit network that scales, transiting IPv4, IPv6, L2/L3 switching as well as routing? Or that faucet can control switches from multiple vendors, including P4 vendors who provide a P4-to-OF bridge, and interoperates with non-SDN networks? Or (and possibly most importantly) that faucet provides automated integration tests, allowing many bugs to be caught early (sometimes even by the switch vendor) before shipping new releases? 
    Well, I should probably mention those things. I've been lucky enough to have been involved in SDN off and on since around 2009, and I can emphatically say that of the production SDN and OpenFlow networks that I have been intimately involved in, this combination of hardware, software and people has been, hands down, the most rewarding and most supportable. In fact, this has been so supportable and great to work with, we migrated our production branch office over to a set of faucet controlled SDN switches, and will soon migrate first hop routing over to our robust faucet system. "However did you do this?!?!" you might be inclined to say. Well, I'm glad you asked, because I am going to tell you. 
    First, though, there should be some design goals. As many of the naysayers of SDN will happy point out, "what problem are you trying to solve?" to that end, here is what our design goals were:


 	- Run all layer 2 in via faucet
 	- Remove need to log into any network elements after deployment (other than firmware updates)
 	- Centralize management
 	- Stretch goal to NFV BGP, do first hop L3


    Easy enough, right? It really is. For our deployment we leveraged Aruba 2930F switches giving us a wealth of 1G copper ports and a handful of 10G SFP+ ports. Luckily, we already had this gear because as so many that have tried to deploy openflow in the past have seen, all hardware is not created equally. Luckily, the [faucet foundation](https://www.faucet.org.nz/) has published a list of requirements for support, and there are a reasonable number of vendors that actually conform. The real key that I learned in this process is that without proper vendor support (which had been several lacking in the past), and without multi-table, OpenFlow is not positioned for success. It comes down to using the right tools for the job, and OpenFlow (as well as SDN) is no different. 
    Originally this post was to detail the process of building this network, much like posts in the past where there has been a “do this, then do that” how-to, it’s more or less unnecessary here. Why? The faucet project is serious, well documented and generally here to work. The expectation is that this is not an enclave, or a science experiment, or a lab. It’s a production network with real people and real traffic. Read that again. The expectation is that this is stable, supportable, and can do in ready to use day-to-day. And it doesn’t disappoint. Installing is a snap, the[ documentation](https://docs.faucet.nz/en/latest/tutorials/first_time.html) for faucet is fantastic and complete. If there is something missing or a question, the developers are incredibly responsive and very quick to answer and address any issues that may arise. It’s extremely low footprint - it runs very well on a raspberry pi and does not tax a raspberry pi series 2, even with the gauge telemetry interface (there is a[ pre-built pi OS](https://docs.faucet.nz/en/latest/installation.html#installing-on-raspberry-pi) for anyone that would prefer a more turnkey option). You may be thinking “*But Nick, I need my CLI!!!*” You’re covered - and here is why: the developers use this system. They run real networks with it. Every day. They know what is necessary to manage and maintain a real production network and sometimes that means troubleshooting. Like many engineers that learned on traditional network equipment, most of us prefer a CLI to troubleshoot, so the inclusion of this feature from the controller is not really a surprise. The fctl command provides a reasonable visibility into the operations of the controller and can be augmented and scripted. 

```
buraglio@faucet:~ $ /usr/bin/fctl --help
usage:
    MACs learned on a DP.
    /usr/bin/fctl -n --endpoints=[http://172.17.0.1:9302](http://172.17.0.1:9302) --metrics=learned_macs --labels=dp_id:0xb827eb608918
    Status of all DPs
    /usr/bin/fctl -n --endpoints=[http://172.17.0.1:9302](http://172.17.0.1:9302) --metrics=dp_status
Retrieve FAUCET/Gauge state using Prometheus variables.
optional arguments:
  -h, --help            show this help message and exit
  -n, --nonzero         nonzero results only
  -e ENDPOINTS, --endpoints ENDPOINTS
                        list of endpoint URLs to query
  -m METRICS, --metrics METRICS
                        list of metrics to query
  -l LABELS, --labels LABELS
                        list of labels that must be present
  --display-labels DISPLAY_LABELS
                        list of labels to filter display by (default all)
```

Monitoring is also taken into account in the form of the gauge interface, which provides a nearly-real-time telemetry stream of important and useful information. Leveraging both the wealth of topological information that the controller has at its disposal and a familiar [prometheus](https://github.com/prometheus) / [grafana](https://grafana.com/) back / front end interface, the oft-touted notion of streaming telemetry is fully - and quite capably - realized. From the perspective of a networking monitoring and statistics geek, this is the cat’s meow. Very, very data rich.
[![](http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap-1024x275.png)](http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap.png)
A simple diagram of our office network pretty well explains the decoupled control plane architecture. Keep it simple, architect for success. Fundamentally SDN networks should be designed like other networks, redundant systems, good monitoring, out of band access. A good design principle is that if you wouldn’t do it on a traditional network, you probably shouldn’t do it for an SDN based network.   [![](http://www.forwardingplane.net/wp-content/uploads/2018/11/faunet-office.png)](http://www.forwardingplane.net/wp-content/uploads/2018/11/faunet-office.png)
 
Don’t trust me? Fair enough, check out the [University of Waikato](https://www.waikato.ac.nz/research/units/wand.shtml) interface [here](https://grafana.redcables.wand.nz/d/000000003/redcables-bgp?orgId=1). For more interface on the deployment at [WAND](https://wand.net.nz/), check[ this link](https://redcables.wand.nz/). You won’t be disappointed.  
 

## My take


### Building and running it

    The [documentation for faucet](https://docs.faucet.nz/en/latest/) is indescribably better than any other SDN project I have worked with over the span of nearly 10 years.** It’s also supportable.** My office has been running the enterprise network off of faucet for a while now, without issue, and it meets our design goals [stretch goal of BGP NFV is still in process - testing is successful]). It is easy to manage and very information rich. I can see security minded folks being very interested in the ACLs and other such options available. 

### Telemetry and analytics    

    Where so many others in this space are talking about their Telemetry solution, this one is already here, complete, and usable. Frankly, I am fully comfortable running a production network on this technology, operationally it is truly easier. From a security perspective, the options added scale well and deliver on their promise. Where OpenFlow was once touted as the networking silver bullet (without a lot of real stick time to prove or disprove it), it has now fallen comfortable into a nice, supportable model. 

### Up next….    

    If you think this is cool, wait until [SuperComputing 18](https://sc18.supercomputing.org/), where we’re deploying a[ first-of-it’s kind network](https://www.linkedin.com/feed/update/urn:li:activity:6461072411969363968/), all controlled by FAUCET. 
 
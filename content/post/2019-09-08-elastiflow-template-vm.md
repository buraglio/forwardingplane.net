---
id: 1712
title: 'ElastiFlow Template VM'
date: '2019-09-08T12:11:58-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1709'
permalink: /2019/09/08/elastiflow-template-vm/
Views:
    - '3253'
categories:
    - How-To
    - 'Lab Time'
    - Musings
---

<!-- wp:paragraph -->

Flow data is a critical piece of understanding how your network works what what it is actively doing. It also provides a great baseline and capacity planning tool. However, some of the more feature rich NetFlow and/or sFlow collectors can be quite daunting in their cost and/or complexity to install. [ElastiFlow](https://github.com/robcowart/elastiflow) is a great alternative for flow analytics and is built on the well traveled and robust [ElasticStack](https://www.elastic.co/start?ultron=[EL]-[B]-[AMER]-US+CA-Exact&blade=adwords-s&Device=c&thor=elastic%20stack&gclid=EAIaIQobChMIuKC5xefB5AIVCYnICh0wEg5lEAAYASAAEgIp_fD_BwE), meaning, its back end is well documented, well supported, and scales exceptionally well. For those that would like to play around with this but don't want to take the time to install it (see below for the instruction set I used), I have provided a simple VM to toy around with. 

<!-- /wp:paragraph -->
<!-- wp:image {"id":1710} -->
<figure class="wp-block-image">![](http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM-1024x704.png)</figure>
<!-- /wp:image -->
<!-- wp:paragraph -->

Included here is a vanilla Ubuntu 18 LTS VM with a basic [Elastiflow](https://github.com/robcowart/elastiflow) install. This includes all of the components of an ElasticStack plus the front end pieces of the ElastiFlow project. Most of the install is based on [this](https://www.catapultsystems.com/blogs/install-elastiflow-on-ubuntu-18-04-part-1/) how-to. 

<!-- /wp:paragraph -->
<!-- wp:paragraph -->

Included in the image is also a base install of NGINX and certbot so that you can reverse proxy the access and have a valid SSL certificate. There are a plethora of guides on how to accomplish that task on the internet. 

<!-- /wp:paragraph -->
<!-- wp:paragraph -->

This was build and validated on Proxmox 6.0.6 but should be able to run on VMWare as well with a bit of qemu-img conversion. As expected, ElastiFlow (and ElasticStack) are fairly resource hungry. 16G of Memory and a handful of CPU cores is the bare minimum to run this with any real efficiency. Additionally, Ubuntu 18 has changed how the networking is setup - it is all located in /etc/netplan/ now.   


<!-- /wp:paragraph -->
<!-- wp:paragraph -->

Login Information:

<!-- /wp:paragraph -->
<!-- wp:preformatted -->

```
User Name: root
Password: elastiflow
Privileged user: elastiflow
Password: elastiflow

```

<!-- /wp:preformatted -->
<!-- wp:paragraph -->

Default IP addresses:

<!-- /wp:paragraph -->
<!-- wp:preformatted -->

```
10.255.255.5/27
2001:db8:ffff:2::5/64
```

<!-- /wp:preformatted -->
<!-- wp:paragraph -->

Download the image [here](https://drive.google.com/open?id=1ga_Pj2j6h1ce9rcT7jQjncpVjLIC4X4t). 

<!-- /wp:paragraph -->
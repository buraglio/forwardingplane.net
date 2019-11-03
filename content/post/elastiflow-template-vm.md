---
title: 'ElastiFlow Template VM'
date: Sun, 08 Sep 2019 18:11:58 +0000
draft: false
tags: [How-To, Lab Time, Musings]
---

Flow data is a critical piece of understanding how your network works what what it is actively doing. It also provides a great baseline and capacity planning tool. However, some of the more feature rich NetFlow and/or sFlow collectors can be quite daunting in their cost and/or complexity to install. [ElastiFlow](https://github.com/robcowart/elastiflow) is a great alternative for flow analytics and is built on the well traveled and robust [ElasticStack](https://www.elastic.co/start?ultron=[EL]-[B]-[AMER]-US+CA-Exact&blade=adwords-s&Device=c&thor=elastic%20stack&gclid=EAIaIQobChMIuKC5xefB5AIVCYnICh0wEg5lEAAYASAAEgIp_fD_BwE), meaning, its back end is well documented, well supported, and scales exceptionally well. For those that would like to play around with this but don't want to take the time to install it (see below for the instruction set I used), I have provided a simple VM to toy around with.

![](http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM-1024x704.png)

Included here is a vanilla Ubuntu 18 LTS VM with a basic [Elastiflow](https://github.com/robcowart/elastiflow) install. This includes all of the components of an ElasticStack plus the front end pieces of the ElastiFlow project. Most of the install is based on [this](https://www.catapultsystems.com/blogs/install-elastiflow-on-ubuntu-18-04-part-1/) how-to. 

Included in the image is also a base install of NGINX and certbot so that you can reverse proxy the access and have a valid SSL certificate. There are a plethora of guides on how to accomplish that task on the internet.

This was build and validated on Proxmox 6.0.6 but should be able to run on VMWare as well with a bit of qemu-img conversion. As expected, ElastiFlow (and ElasticStack) are fairly resource hungry. 16G of Memory and a handful of CPU cores is the bare minimum to run this with any real efficiency. Additionally, Ubuntu 18 has changed how the networking is setup - it is all located in /etc/netplan/ now.     

Login Information:

```
User Name: root
Password: elastiflow
Privileged user: elastiflow
Password: elastiflow  

```

Default IP addresses:

```
10.255.255.5/27
2001:db8:ffff:2::5/64
```

Download the image [here](https://drive.google.com/open?id=1ga_Pj2j6h1ce9rcT7jQjncpVjLIC4X4t).
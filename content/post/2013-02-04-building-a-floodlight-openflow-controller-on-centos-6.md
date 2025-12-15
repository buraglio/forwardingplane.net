---
id: 429
title: 'Building a Floodlight OpenFlow controller on CentOS 6'
date: '2013-02-04T07:10:24-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=429'
permalink: /2013/02/04/building-a-floodlight-openflow-controller-on-centos-6/
geo_latitude:
    - '40.072829'
geo_longitude:
    - '-88.245813'
themeblvd_noindex:
    - 'true'
geo_public:
    - '1'
themeblvd_title:
    - 'Floodlight OpenFlow controller on CentOS 6'
themeblvd_keywords:
    - 'openflow, sdn, centos, floodlight, bigswitch'
themeblvd_description:
    - 'How to build a Floodlight OpenFlow controller on CentOS 6'
dsq_thread_id:
    - '3626869649'
Views:
    - '373'
categories:
    - 'Lab Time'
    - SDN
    - UNIX
---

A bit of back history: I came from BSD land. I was a FreeBSD user from way back in the 1990s. BSD land is a land of secure boxes and very high uptimes. It's also a land of arguably clunky package support, a lot of compiling by hand and these days, not nearly as encompassing package and network tuning support. <a title="Better support for Linux (and annoyed about it)" href="http://www.forwardingplane.net/2011/06/better-support-for-linux-and-annoyed-about-it/">I decided to move to Linux</a> a while ago, reluctantly, and chose Debian as my flavor of choice. I do love debian, however, I very quiuckly realized that even debian is a bit of a fringe OS build of Linux. Commercial support is nearly all based on RHEL. Folks that run RHEL also run CentOS. We run both in my day job. About a year ago to I, once again, decided I needed to learn CentOS.
There are a lot of posts about building floodlight as an openflow controller. I used this tutorial [Brent Salisbury did](http://networkstatic.net/floodlight-openflow-controller-gui-applet/) to build mine. There is a good one on the [openflow hub](http://floodlight.openflowhub.org/getting-started/) site as well. I've found that many are based on Debian or Ubuntu, which can be subtly different than a CentOS / RHEL experience.
 
In CentOS, log in and sudo -s or su to root. Install the prereqs:
*yum -y install build-essential default-jdk ant python-dev eclipse git*
*mkdir /services/floodlight*
*cd /services/floodlight/*
*git clone git://github.com/floodlight/floodlight.git
ant*
Start floodlight in the background.
*./floodlight.sh &*
Because I'm terrible at looking at directions, I went to the base URL. This will yield an error that looks something like this:
*{"name":"Not Found","error":true,"throwable":null,"description":"The server has not found anything matching the request URI","success":false,"informational":false,"code":404,"reasonPhrase":"Not Found","uri":"http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5","serverError":false,"connectorError":false,"clientError":true,"globalError":false,"redirection":false,"recoverableError":false}*
The right way to access floodlight is to use the entire URL:
http://<address>:8080/ui/index.html
Learn from my stupidity.
 
Here is a script to build it for you:

```
#!/bin/bash
echo "Installing prerequisits:"
yum -y install build-essential default-jdk ant python-dev eclipse git
echo "Installing floodlight to /services/floodight/"
mkdir /services/floodlight
cd /services/floodlight/
git clone git://github.com/floodlight/floodlight.git
ant
echo "Starting floodlight:"
./floodlight.sh&
echo "Floodlight started, point your beowser at http://<address>:8080/ui/index.html"
```

 
 
 
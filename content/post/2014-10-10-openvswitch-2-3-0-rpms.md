---
id: 1098
title: 'OpenVswitch 2.3.0 RPMs'
date: '2014-10-10T15:06:50-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1098'
permalink: /2014/10/10/openvswitch-2-3-0-rpms/
themeblvd_title:
    - 'OpenvSwitch 2.3.0 RPMs'
themeblvd_keywords:
    - 'OpenvSwitch, devops, buraglio, forwardingplane, sdn, RPMs, centos, Linux, openflow, opendaylight'
themeblvd_description:
    - 'Download OpenvSwitch RPMs for centos 6.5 and 7'
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3104509898'
Views:
    - '58'
categories:
    - SDN
---

I was wanting to do a few quick mock-ups with [OpenvSwitch](http://openvswitch.org/) and [OpenDayLight](http://www.opendaylight.org/) and wanted to use CentOS since I have templates for it that I replicate.  Just like with the<a title="OpenvSwitch 2.0 Debian packages" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/" target="_blank" rel="noopener noreferrer"> debian stuff I had been doing</a>, I wasn't able to find any in some quick searches.   I stumbled upon [This site](http://n40lab.wordpress.com/2014/09/04/openvswitch-2-3-0-lts-and-centos-7/), which had a great how to for building them, so I just used that.  Seeing as that the debian packages actually got downloaded a lot, I figured I'd post these RPMs as well.  They're available [here](http://www.forwardingplane.net/wp-content/uploads/OVS2.0/OpenvSwitch-2.3.0-RPM.tgz) and should work on CentOS 6.5 and probably 7.
Just do a quick local install and start the service and you should be up and running.
 

```
yum localinstall /home/ovswitch/rpmbuild/RPMS/x86_64/openvswitch-2.3.0-1.x86_64.rpm 
sudo service openvswitch start
```


```

```

---
title: 'OpenVswitch 2.3.0 RPMs'
date: Fri, 10 Oct 2014 21:06:50 +0000
draft: false
tags: [SDN]
---

I was wanting to do a few quick mock-ups with [OpenvSwitch](http://openvswitch.org/) and [OpenDayLight](http://www.opendaylight.org/) and wanted to use CentOS since I have templates for it that I replicate.  Just like with the [debian stuff I had been doing](http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/ "OpenvSwitch 2.0 Debian packages"), I wasn't able to find any in some quick searches.   I stumbled upon [This site](http://n40lab.wordpress.com/2014/09/04/openvswitch-2-3-0-lts-and-centos-7/), which had a great how to for building them, so I just used that.  Seeing as that the debian packages actually got downloaded a lot, I figured I'd post these RPMs as well.  They're available [here](http://www.forwardingplane.net/wp-content/uploads/OVS2.0/OpenvSwitch-2.3.0-RPM.tgz) and should work on CentOS 6.5 and probably 7. Just do a quick local install and start the service and you should be up and running.  ```
yum localinstall /home/ovswitch/rpmbuild/RPMS/x86\_64/openvswitch-2.3.0-1.x86\_64.rpm 
sudo service openvswitch start
```
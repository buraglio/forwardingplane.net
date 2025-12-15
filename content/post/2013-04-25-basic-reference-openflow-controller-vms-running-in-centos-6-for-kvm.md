---
id: 602
title: 'Basic reference openflow controller VMs running in CentOS 6 for KVM.'
date: '2013-04-25T22:56:07-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=602'
permalink: /2013/04/25/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3635309244'
Views:
    - '152'
categories:
    - 'Lab Time'
    - OpenFlow
    - SDN
    - UNIX
---

I had been working, off and on, on a how-to for building the [daylight openflow controller](http://www.opendaylight.org/) under CentOS.  Most openflow docs and dev are done under ubuntu or debian, and while those are both fantastic alternatives, there are a huge number of folks that will want or need to use RHEL or CentOS. So, seeing as that is the case, having someone be mindful of that is important.  When I saw the [write up](http://www.dasblinkenlichten.com/installing-opendaylight-on-centos/) by [Jon Langemak](https://twitter.com/blinken_lichten), I scrapped my attempt at a how-to since his was so much better.
If you're not following Jon and reading his blog, you should be.  He's a sharp guy with interesting things to say.
[![](http://www.forwardingplane.net/wp-content/uploads/2013/04/projectfloodlight-logo-header.png)](http://www.forwardingplane.net/wp-content/uploads/2013/04/projectfloodlight-logo-header.png)
That got me thinking about references and resources, and I decided that I would take a few of the things I had been working on on my home lab and make them available to the masses.  I'm a fan of importable base VMs.  So, seeing that I am working on testing openflow controllers, it made sense in my [constantly racing] mind to make the reference, base level VMs available.  If anyone is interested in the [floodlight controller](http://www.projectfloodlight.org/floodlight/) running under CentOS 6.3 built using the method documented <a title="Building a Floodlight OpenFlow controller on CentOS 6" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/" target="_blank" rel="noopener noreferrer">here</a>, a KVM image is now available to download from [here](http://www.forwardingplane.net/wp-content/uploads/vm-images/centos-floodlight-template.tbz).  It is, as stated, a KVM image, created by using the method I documented in <a title="CentOS KVM Install – Quick Start to a VM" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/" target="_blank" rel="noopener noreferrer">this post</a> a few months ago.    There is a readme file in the archive wth basic instructions.  You'll need a basic understanding of [KVM](http://www.linux-kvm.org/page/Main_Page) to make it work, or you can try to convert it to something else like vmware, XEN or virtualbox.
I'll be adding one of these soon for [daylight](http://www.opendaylight.org/) as well.
 
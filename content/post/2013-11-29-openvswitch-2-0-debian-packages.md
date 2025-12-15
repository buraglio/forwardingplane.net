---
id: 824
title: 'OpenvSwitch 2.0 Debian packages'
date: '2013-11-29T14:15:17-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=824'
permalink: /2013/11/29/openvswitch-2-0-debian-packages/
themeblvd_title:
    - 'Roll your own OpenvSwitch 2.0 Debian packages for fun and [probably no] profit.'
themeblvd_keywords:
    - 'OpenFlow, Debian, OpenvSwitch, OVS, OpenDaylight, buraglio, nick buraglio, ipv6, alix'
themeblvd_description:
    - 'Build OpenvSwitch 2.0 debian packages for fun!'
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '2154737404'
Views:
    - '153'
categories:
    - How-To
    - OpenFlow
    - SDN
---

As part of a larger fun project I'm working on (OVS for the ALIX platform; more to come on that once I have it 100% working), I have been playing a lot with <a href="http://openvswitch.org/" target="_blank" rel="noopener noreferrer">OVS</a>.  It's a great platform, and<a href="http://networkstatic.net/install-open-vswitch-v2-redhat-fedora-19/" target="_blank" rel="noopener noreferrer"> as others have mentioned</a>, it's as close to an SDN reference data plane implementation as we have.  I'd be surprised if many if not all commercial implementations of OpenFlow aren't based on OVS.  Anyway, I wanted to build debian packages since I'd never done it before and thought it'd be fun.  I wanted to use OVS2 so that I can play with some of the newer features and specifically to see how well the IPv6 support is in 2.0 when paired with <a href="http://www.opendaylight.org/" target="_blank" rel="noopener noreferrer">OpenDaylight</a>(more to come on this, too. I promise =).
This proved to be more simple than I anticipated mostly due to lots of good documentation.  To accomplish it, I decided to start with a VM since I lie to work in virtualized environments for experimentation and lambing. I spun up a Debian 7 VM from scratch and began configuring it as I usually do with the inclusion of the tools necessary to build packages.
<em>** I originally tried this from the git repo via </em>git clone git://openvswitch.org/openvswitch<em> but kept seeing weird errors so I moved to the 2.0.0 tarball.  </em>
<pre>apt-get -y install screen sudo vim etckeeper mlocate autoconf2.13 \
libssl-dev graphviz python-all python-qt4 python-zopeinterface \
python-twisted-conch tcpdump build-essential fakeroot debhelper \
gdebi-core pkg-config</pre>
Grab the OVS tarball
<pre>wget <a href="http://openvswitch.org/releases/openvswitch-2.0.0.tar.gz">http://openvswitch.org/releases/openvswitch-2.0.0.tar.gz</a></pre>
<pre>mv openvswitch-2.0.0.tar.gz openvswitch-2.0.0.orig.tar.gz</pre>
<pre>cd openvswitch-2.0.0</pre>
<pre>dpkg-buildpackage -b</pre>
<pre>cd ../</pre>
Install all of the packages
( # Answer Y to all prompts )
<pre>gdebi openvswitch-datapath-source_2.0.0-1_all.deb</pre>
module-assistant auto-install openvswitch-datapath
gdebi openvswitch-common_2.0.0-1_amd64.deb
gdebi openvswitch-switch_2.0.0-1_amd64.deb</pre>
<div></div>
You should now be able to check the version:
 
<pre>
buraglio@deb7ovs-vm:/home/buraglio# ovs-vsctl -V
ovs-vsctl (Open vSwitch) 2.0.0
Compiled Nov 29 2013 13:18:32
</pre>
Check the OpenFlow versions supported:
<pre>
buraglio@deb7ovs-vm:/home/buraglio# ovs-ofctl -V
ovs-ofctl (Open vSwitch) 2.0.0
Compiled Nov 29 2013 13:18:32
OpenFlow versions 0x1:0x4
</pre>
More to come on this.  For anyone that doesn't want to build the .debs themselves, they're available to download from <a href="http://www.forwardingplane.net/wp-content/uploads/OVS2.0/" target="_blank" rel="noopener noreferrer">here</a>, no warranty implied or expressed =)
 
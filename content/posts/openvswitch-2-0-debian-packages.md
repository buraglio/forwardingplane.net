---
title: 'OpenvSwitch 2.0 Debian packages'
date: Fri, 29 Nov 2013 20:15:17 +0000
draft: false
tags: [How-To, OpenFlow, SDN]
---

As part of a larger fun project I'm working on (OVS for the ALIX platform; more to come on that once I have it 100% working), I have been playing a lot with [OVS](http://openvswitch.org/ ).  It's a great platform, and [as others have mentioned](http://networkstatic.net/install-open-vswitch-v2-redhat-fedora-19/), it's as close to an SDN reference data plane implementation as we have.  I'd be surprised if many if not all commercial implementations of OpenFlow aren't based on OVS.  Anyway, I wanted to build debian packages since I'd never done it before and thought it'd be fun.  I wanted to use OVS2 so that I can play with some of the newer features and specifically to see how well the IPv6 support is in 2.0 when paired with [OpenDaylight](http://www.opendaylight.org/)(more to come on this, too. I promise =). This proved to be more simple than I anticipated mostly due to lots of good documentation.  To accomplish it, I decided to start with a VM since I lie to work in virtualized environments for experimentation and lambing. I spun up a Debian 7 VM from scratch and began configuring it as I usually do with the inclusion of the tools necessary to build packages. _\*\* I originally tried this from the git repo via _git clone git://openvswitch.org/openvswitch_ but kept seeing weird errors so I moved to the 2.0.0 tarball.  _```
apt-get -y install screen sudo vim etckeeper mlocate autoconf2.13 \\
libssl-dev graphviz python-all python-qt4 python-zopeinterface \\
python-twisted-conch tcpdump build-essential fakeroot debhelper \\
gdebi-core pkg-config
```Grab the OVS tarball```
wget [http://openvswitch.org/releases/openvswitch-2.0.0.tar.gz](http://openvswitch.org/releases/openvswitch-2.0.0.tar.gz)
``````
mv openvswitch-2.0.0.tar.gz openvswitch-2.0.0.orig.tar.gz
``````
cd openvswitch-2.0.0
``````
dpkg-buildpackage -b
``````
cd ../
```Install all of the packages ( # Answer Y to all prompts )```
gdebi openvswitch-datapath-source\_2.0.0-1\_all.deb
```module-assistant auto-install openvswitch-datapath gdebi openvswitch-common\_2.0.0-1\_amd64.deb gdebi openvswitch-switch\_2.0.0-1\_amd64.deb

You should now be able to check the version:  ```
buraglio@deb7ovs-vm:/home/buraglio# ovs-vsctl -V
ovs-vsctl (Open vSwitch) 2.0.0
Compiled Nov 29 2013 13:18:32

```Check the OpenFlow versions supported:```
buraglio@deb7ovs-vm:/home/buraglio# ovs-ofctl -V
ovs-ofctl (Open vSwitch) 2.0.0
Compiled Nov 29 2013 13:18:32
OpenFlow versions 0x1:0x4

```More to come on this.  For anyone that doesn't want to build the .debs themselves, they're available to download from [here](http://www.forwardingplane.net/wp-content/uploads/OVS2.0/), no warranty implied or expressed =)
---
title: 'CentOS KVM Install - Quick Start to a VM'
date: Sat, 02 Mar 2013 01:12:02 +0000
draft: false
tags: [Data Center, How-To, Lab Time, UNIX, Virtualization]
---


#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-03-21 13:35:05">Mar 4, 2013</time>

Fixed a typo in the ifcfg-br0 section.
<hr />
#### 
[Networking Field Day 5, participation.](http://www.forwardingplane.net/2013/03/network-field-day-5/ "") - <time datetime="2013-03-06 10:41:09">Mar 3, 2013</time>

\[...\] old blog (which became this site). I’m working more on OpenFlow,  virtualization stuff like KVM, VirtualBox and VMware and bringing up 100G WAN links.  I even had the extremely cool opportunity \[...\]
<hr />
#### 
[vps](http://blogmareczka.blog.com/ "xlpggh@gmail.com") - <time datetime="2013-03-14 09:03:01">Mar 4, 2013</time>

I really like your blog. You write about very interesting things. Thanks for all your tips and information
<hr />
#### 
[vps](http://fajnyblogoadministracji "xjijdaeyl@gmail.com") - <time datetime="2013-03-14 10:33:15">Mar 4, 2013</time>

Hello! I really like this blog. Tell me please - from where do you have information for ths blog?
<hr />
#### 
[cryptochrome (@cryptochrome)]( "sascha@picchiantano.de") - <time datetime="2013-03-22 01:53:36">Mar 5, 2013</time>

I am in the exact same boat right now, having a network security background and a fair amount of experience with "desktop" hypervisors like Fusion/Parallels but also some ESXi. I discovered KVM through my interest in SDN/OpenFlow and have been hooked ever since. In your opening statement you mentioned you were looking for a headless, remotely managable solution without a GUI. If you ever want to dive into a web GUI for the management, you should check out archipelproject.org (awesome system, really clever, controlling hypervisors through XMPP/Jabba!) and also oVirt.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-03-22 10:25:14">Mar 5, 2013</time>

Great find! Thanks for the link. A web client would also work well as it implies that it can run on a headless box for remote management. I'm going to look into this for sure for the OpenFlow lab I'm working on.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-05-02 18:46:32">May 4, 2013</time>

Agreed. Openstack is good stuff. Check out Brent's blog over at networkstatic.net for some good info in it. Ill be adding some openstack stuff hopefully soon as well. It's been on my list for a while.
<hr />
#### 
[cryptochrome]( "sascha@picchiantano.de") - <time datetime="2013-04-26 05:54:08">Apr 5, 2013</time>

oh.. and http://spice-space.org/ of course.
<hr />
#### 
[saniel]( "realsuso@gmail.com") - <time datetime="2013-04-26 05:28:31">Apr 5, 2013</time>

hmmm...but how to give a VM an IP when there is no guest OS yet :) I need a way how to connect to a VM-guest console to do the install of an OS. My scenario is...an centOS6.4 KVM server-no GUI and a win7 workstation.
<hr />
#### 
[cryptochrome]( "sascha@picchiantano.de") - <time datetime="2013-04-26 05:50:00">Apr 5, 2013</time>

you want to look into SPICE (it's basically something like RDP). Libvirt has support for it. I am not sure though you would be able to connect to a new machine over the network without the help of some additional libvirt management tools. Take a look at http://www.ovirt.org/
<hr />
#### 
[cryptochrome]( "sascha@picchiantano.de") - <time datetime="2013-04-26 02:21:04">Apr 5, 2013</time>

Saniel, you need to give your VM an IP address that is routable through the host system. Then you can connect to that IP.
<hr />
#### 
[saniel]( "realsuso@gmail.com") - <time datetime="2013-04-26 01:43:35">Apr 5, 2013</time>

hi there, I really like this howto. I was folloving it on a cenOS6.4 up to the "connect to the console" part. At that point I haven't find a way how to VNC connect to the KVM-guest fom a windows machine. Is there some easy way to do that???
<hr />
#### 
[Jeff Loughridge]( "jeffl@alumni.duke.edu") - <time datetime="2013-04-28 12:44:05">Apr 0, 2013</time>

cryptochrome, Thanks for the tip. It would work as far as basic network connectivity. I am not sure if the topology would affect the results of my TCP throughput testing and tuning. Maybe software is software with two private network segments or a single bridged one.
<hr />
#### 
[cryptochrome (@cryptochrome)]( "sascha@picchiantano.de") - <time datetime="2013-04-28 12:55:47">Apr 0, 2013</time>

Possibilities are endless. In fact, you can do way more than you can do with ESXi when it comes to networking (out of the box). And if the Linux bridge is too basic for your needs, you can always use Open vSwitch. Just remember you have Linux' powerful networking stack on the host machine. Just point your VMs to the host as default gateway and take it from there. One bridge, 1000 bridges, however you like it. Pull in some IPTables for security and other packet mangling. Happy days. Doing the same with ESXi is either impossible or $$$.
<hr />
#### 
[cryptochrome (@cryptochrome)]( "sascha@picchiantano.de") - <time datetime="2013-04-28 12:26:25">Apr 0, 2013</time>

Jeff, you can do the same kind of network setup with KVM. Just hook up all the virtual machines to the same bridge and make either your host or another virtual machine the router.
<hr />
#### 
[Jeff Loughridge]( "jeffl@alumni.duke.edu") - <time datetime="2013-04-28 12:22:48">Apr 0, 2013</time>

Nick, Great post. I'll have to give KVM on Centos a shot. KVM is definitely rough around the edges. Simple bridge/NAT networking is easy, although installing on headless server complicates matters. I didn't want to go the VNC route as you did. I couldn't get the console output to a terminal the way you can using '-display curses' in qemu. Another frustrating aspect for me was trying to set up a network topology such a two VMs talking to one another through a virtual router. This is easy with ESXi, Workstation, and virtualbox. Not so much with KVM.
<hr />
#### 
[Lennie]( "forwardingplaneblog@consolejunkie.net") - <time datetime="2013-04-29 02:18:09">Apr 1, 2013</time>

Stop and delete would have been a far better names than destroy and undefine. Currently looking at setting up OpenStack/KVM/libvirt.
<hr />

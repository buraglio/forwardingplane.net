---
id: 731
title: 'Building a secured network in a box'
date: '2013-07-25T23:28:15-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=731'
permalink: /2013/07/25/building-a-secured-network-in-a-box/
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'security onion, vmware, virtualization, uinx, firewall, IDS, kvm , openvswitch, ovs'
themeblvd_title:
    - 'Security Onion Network in a box'
themeblvd_description:
    - 'Build a secure network in a box using Security Onion.  Span a port on VMware vswitch.  Virtualization is here to stay.  '
dsq_thread_id:
    - '3629172097'
Views:
    - '915'
categories:
    - 'Lab Time'
    - Security
    - Virtualization
---

In many environments, the move to virtualization is a path well traveled.  My home and lab networks are no exception to this and I'm sure nearly everyone who reads these pages has at least been exposed to it in one way or another.  I have played with nearly all of the virtualization platforms and am firmly in the camp that there will be a large segment of networking that will move to a virtualized platform especially in the data center and campus segments.  Virtualization of routing tables has existed for a long time, see <a href="http://en.wikipedia.org/wiki/Virtual_Routing_and_Forwarding" target="_blank" rel="noopener noreferrer">VRF-Lite  and MPLS VRF </a>as well as multi-tenancy technologies like Junipers logical systems so the concept, at some level, has existed in networking for quite some time.
"How is a small to medium sized environment going to take advantage of this and more interestingly, how can it be secured?"
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions.jpg"><img class="alignleft  wp-image-732" alt="Red_onions" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions-1024x763.jpg" width="368" height="275" /></a>This is a question I inadvertently found at least one answer to when building out my own network and testing a great little project called <a href="http://securityonion.blogspot.com/" target="_blank" rel="noopener noreferrer">security onion</a>.  I'd seen and used this platform a bit in the past, but it had been at least a version ago and my exposure was pretty short.
The problem now, though, was that everything I have in use other than a gigabit switch and a NAS is virtualized.  My firewall, my router, all of my dev and test boxes and all but one of my non-portable machines.  All VMs.  I'd gone back and forth between VMware and KVM, and while I like KVM better, management of edge case or non-standard networking stuff wasn't as well documented and <a href="http://openvswitch.org/" target="_blank" rel="noopener noreferrer">OVS</a> either wasn't in the build of CentOS I was using or I didn't know about its inclusion yet, so I settled on VMware ESXi 5 for this particular box.  I needed to be able to span a port on a vswitch.  My hopes were not high, but I figured there may be an unsupported way.
Interestingly enough, the VMWare operating system has a mechanism for makeshift "spanning" a port.  More correctly, it has a way to see "all vlans" on a given vswitch, and it's quite simple.  Essentially, you have to create a port group on vlan 4095 on the vswitch then set that port group to promiscuous mode. Add the vm NIC that you are going to use to monitor traffic to that port group.  <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1004099" target="_blank" rel="noopener noreferrer">From VMware site</a>:
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site.png"><img class=" wp-image-734 aligncenter" alt="VMWare-site" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site.png" width="582" height="211" /></a>
I was pleasanty surprised at how easy it was and was at the point of telling security onion to have interfaces on both of the vswitches in less than 15 minutes. Configuration, Networking, Properties, Security. VLAN 4095. Done.Here are a few screenshots of my VMware config following the steps laid out above. It's far more simple than I could have imagined.
&nbsp;
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking.png"><img class="wp-image-735 alignright" alt="VMWAre-config-networking" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking.png" width="564" height="350" /></a>
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1.png"><img class="alignleft  wp-image-736" alt="VMWare-SPAN-WAN1" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1.png" width="452" height="332" /></a>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWARE-Span-WAN2.png"><img class=" wp-image-737 alignright" alt="VMWARE-Span-WAN2" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWARE-Span-WAN2.png" width="300" height="373" /></a>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
At this point Security onion was able to see what was going on.  In my case I allowed for visibility on both sides of my routing firewall, so there was a decent amount of data.
&nbsp;
&nbsp;
This is the interesting part, I think.  My initial thoughts are that this could be a "network in a box" for small offices.  No router, no servers (other than the VMware host), essentially a fully functional "enterprise" network of hosts, including a very high quality IDS device in a single device.  Put whatever firewall / vrouter in there that is supported or familiar, <a href="http://www.pfsense.org" target="_blank" rel="noopener noreferrer">pfsense</a>, <a href="http://www.juniper.net" target="_blank" rel="noopener noreferrer">Juniper vSRX</a>, <a href="http://www.fortinet.com" target="_blank" rel="noopener noreferrer">fortinet</a>,<a href="http://www.paloaltonetworks.com" target="_blank" rel="noopener noreferrer"> Palo Alto</a>, they all have virtual devices and they all do a fine job [with the exception of IPv6; the only one I could get DHCPv6-PD to work with was pfsense.  Still need to test the fortinet].
Here is a high level diagram of how mine is put together. <a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN.jpg"><img class="alignright size-full wp-image-742" alt="VMWare SPAN" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN.jpg" width="488" height="425" /></a>
Is this a viable option?  I have no idea, but it does work pretty darned well.  In fact, ironically enough, the day I got this working (July 13, 2013), a post went up over at <a href="http://www.geekempire.com/2013/07/virtual-security-onion-via-ubuntu-kvm.html" target="_blank" rel="noopener noreferrer">GeekEmpire</a> doing almost exactly the same thing with KVM and OVS.  The setup is shockingly similar, right down to using pfSense. I was actually a bit envious, not only because his post went up first, but because he did what I had actually wanted to do by using KVM and OVS.  It's well done, I recommend reading it.
I think this is a sign of what will come.  "network in a box" is an intriguing concept, and I'm absolutely <a href="https://www.google.com/search?q=network+in+a+box&amp;ie=utf-8&amp;oe=utf-8&amp;aq=t&amp;rls=org.mozilla:en-US:official&amp;client=firefox-a&amp;channel=fflb" target="_blank" rel="noopener noreferrer">positive I am not the only one thinking about it</a>.  I think, however, that the important part is to see the options available and make sure the masses know that there are many ways to do it.  It is not VMware or nothing, and it's certainly not cisco or the highway.  OpenSource tools like OVS and KVM under a free operating system like Linux can compete at the highest levels and there are documents and how-tos out there.  More importantly, it's not hard.  The same goes for security appliances and even vrouters.  Security Onion and pfSense are both viable platforms and they're just the tip of the iceberg.  At the end of the day it all comes down to options. Opensource, commercial, they all have virtualization strategies and the more you know the better off you'll be in the long run because virt is here to stay.
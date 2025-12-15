---
id: 1380
title: 'Creating an internal span port inside proxmox OVS'
date: '2017-03-20T21:49:58-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1380'
permalink: /2017/03/20/creating-internal-span-port-inside-proxmox-ovs/
dsq_thread_id:
    - '5650874337'
Views:
    - '3709'
categories:
    - How-To
    - NIX4NetEng
    - SDN
    - Security
    - UNIX
---

In the last few years I have moved all of my virtualization to <a href="https://www.proxmox.com/en/">proxmox</a> and docker. Seeing as I like to look at packets because I am a closet security guy, and being as I have been working off-and-on on a security project in recent times, I wanted to be able to span a port not only from a hardware switch, but also within my software switches. I had been using linux bridge, which I am not a fan of, so when I started down this path I did not look hard to find a way to do so under that platform. Instead I used it as an opportunity to move some of the internal bridges to <a href="http://openvswitch.org/">OpenVSwitch</a>. I wanted to create an OVS span port internally.
I had experience with OVS in the past for SDN work that I was doing, but I had never created a mirror port. I briefly thought about using OpenFlow to do it, but the unnecessary complexity was off putting. Instead I chose to create a simple mirror of a span port from my switch. So, traffic flow goes as such:
<a href="http://www.forwardingplane.net/wp-content/uploads/2017/03/OVS-SPAN-1.png"><img class="wp-image-1383 size-full alignleft" src="http://www.forwardingplane.net/wp-content/uploads/2017/03/OVS-SPAN-1.png" alt="" width="573" height="148" /></a>
 
 
This was fairly trivial, and I was seeing packets in no time. I'm not going to go through creating an OVS bridge in proxmox, there are lots of <a href="https://pve.proxmox.com/wiki/Open_vSwitch">documents</a> on how to do that. Once you have your switch port SPAN up and running, and the physical interface in the OVS bridge, you essentially just need to add the following:
Create the mirror
<pre>ovs-vsctl -- --id=@m create mirror name=span -- add bridge vmbr1 mirrors @m</pre>
Find your ports that you want to mirror - you'll need the physical port if consuming from a real switch like I am, and the software port of the virtualized analyzer.  Remember, in OVS anything you want to mess with is going to have a UUID. You need to match the interfaces with the UUID to verify.
ovs-vsctl list port
_uuid :<span style="color: #ff0000;"> 42dbd5a9-27c6-4f1b-958b-943f67b6801b</span>
bond_downdelay : 0
bond_fake_iface : false
bond_mode : []
bond_updelay : 0
external_ids : {}
fake_bridge : false
interfaces : [<span style="color: #000000;">b155454d-db6e-4bb8-af88-7cd6b544c303</span>]
lacp : []
mac : []
name : "<span style="color: #ff0000;">eth1</span>"
other_config : {}
qos : []
statistics : {}
status : {}
tag : []
trunks : []
vlan_mode : []
_uuid : 85c932b2-4f98-4650-8298-ae9e9ca72796
bond_downdelay : 0
bond_fake_iface : false
bond_mode : []
bond_updelay : 0
external_ids : {}
fake_bridge : false
interfaces : [5219306f-96ec-440a-ac8b-d949ea18d752]
lacp : []
mac : []
name : "vmbr1"
other_config : {}
qos : []
statistics : {}
status : {}
tag : []
trunks : []
vlan_mode : []
_uuid : <span style="color: #ff0000;">d53c7323-517f-48a2-9235-4505e654d4b1</span>
bond_downdelay : 0
bond_fake_iface : false
bond_mode : []
bond_updelay : 0
external_ids : {}
fake_bridge : false
interfaces : [91d52d05-d881-4693-ab5c-fc64b5d87518]
lacp : []
mac : []
name : "<span style="color: #ff0000;">veth100i9</span>"
other_config : {}
qos : []
statistics : {}
status : {}
tag : []
trunks : []
vlan_mode : []
In red we have the interfaces I want to to use. the veth interface is the software port on the VM. Eth1 is the hardware interfce that my switch is spanning traffic to. Pro tip: In OVS, the commands are a little unintuitive to me when talking about mirrors.  "select_src_port" and "select_dst_port=" is the destination of the traffic flow from an interface and not source and destination of the traffic you are mirroring from the point of view of the in and out ports. Confusing, right? For instance I can monitor the input from one interface and the output of another in the mirror. What we want is the input and output of the same interface to get both directions of traffic. This is not unlike how span ports are configured on your hardware switch, the nomenclature just threw me off.
<pre>ovs-vsctl set mirror span select_src_port=@eth1 select_dst_port=@eth1</pre>
You can also do this with the UUID
<pre>ovs-vsctl set mirror span select_src_port=42dbd5a9-27c6-4f1b-958b-943f67b6801b select_dst_port=42dbd5a9-27c6-4f1b-958b-943f67b6801b</pre>
Now that we have the source of our mirror we just need to send it somewhere. I wanted mine to go to an internal host running some analytics software (on interface veth100i9)
<pre>ovs-vsctl -- --id=@veth100i9 get port veth100i9 -- set mirror span output-port=@veth100i9</pre>
And that's it. Log into your host and do a tcpdump on whatever interface is mapped to veth100i9 and you should see packets flowing. A few tips:
<ul>
 	<li>Verify your span from the hardware switch is working before diving into the software stack.</li>
 	<li>If you're doing this is proxmox, be aware that proxmox networking stack can be unforgiving when you much around outside of their environment.</li>
 	<li>This will not persist across reboots. Add it to /etc/network/interfaces manually to keep it after a restart.</li>
</ul>
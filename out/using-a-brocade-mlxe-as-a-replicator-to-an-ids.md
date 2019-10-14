---
title: 'Using a Brocade MLXe as a replicator to an IDS'
date: Sun, 25 Nov 2012 17:26:00 +0000
draft: false
tags: [Routing, Security]
---

Have you ever needed to replicate a lot of data transparently to an IDS without the use of a rack of optical taps?  Not enough budget for a Gigamon or cPacket?  Have a spare MLXe laying around?  you're in luck, we were in that boat too. Let me first preface this by saying that this would be fairly trivial using OpenFlow / SDN.  That being said, we didn't have the time to set that up, so this is what we came with.

[![](http://3.bp.blogspot.com/-dkBh5cQqBtc/UKPe167KFsI/AAAAAAABbFY/5DP_E2YVWgg/s640/TransHWFlood.jpg)](http://3.bp.blogspot.com/-dkBh5cQqBtc/UKPe167KFsI/AAAAAAABbFY/5DP_E2YVWgg/s1600/TransHWFlood.jpg)

This would also work using an input interface of 100G, but of course the flows would be limited to 10G. How this works is pretty simple, it just uses a policy based route to direct the flow of traffic out of the desired aggregate interface.  In this real world use case that this was built for, the destination was a Bro cluster, consuming as much of the data as possible.  The config on a brocade is pretty similar to Cisco IOS if you're not familiar, but the VLAN bits are a tad different (actually more intuitive in my opinion).  Here are the bits to make all of this work: Create the vlans and tag them appropriately

mlxe8# conf t mlxe8(config)# vlan 100 mlxe8(config-vlan-100)# untag ethernet 1/1 mlxe8(config-vlan-100)# transparent-hw-flooding mlxe8(config-vlan-100)# router-interface ve 100 mlxe8(config)\# vlan 101 mlxe8(config-vlan-101)# untag ethernet 4/1 ... mlxe8(config-vlan-101)# untag ethernet 4/10 mlxe8(config-vlan-101)# router-interface ve 101 mlxe8(config-vlan-101)#exit mlxe8(config)#interface ve 100 mlxe8(config-vlan-100)#ip policy route-map PBR-TRAFFIC mlxe8(config-vlan-100)#ip access-group pbr\-traffic-acl

mlxe8(config-vlan-101)#exit

mlxe8(config)#interface ve 101

mlxe8(config)#ip address 10.101.101.1/24

Enable all of the interfaces.

mlxe8(config)#interface ethernet 4/1

mlxe8(config)#enable

...

mlxe8(config)#interface ethernet 4/10

mlxe8(config)#enable

Create the LAG.

mlxe8(config)# lag “IDS” static

   mlxe8(config)#ports ethernet 4/1 to 4/10

   mlxe8(config)#primary-port 4/1

   mlxe8(config)#deploy

s

     Create the PBR ACL bits. This can also be done to filter types of traffic using more complex ACLs  if so desired

   mlxe8(config)#access-list pbr\-traffic-acl permit ip any any

mlxe8(config)#exit

mlxe8(config)#route-map PBR-TRAFFIC permit 1

mlxe8(config)#matchipaddress pbr\-traffic-acl

mlxe8(config)#set ip next-hop 10.101.101.1

Create a static ARP entry to tie it all together. 

arp 10.101.101.1 c0ff.eec0.ffee ethernet 1/1

That's it, let the security folks drink from the firehose.  =)

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
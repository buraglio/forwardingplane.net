---
title: 'Brocade VDX First Impressions....'
date: Sat, 08 Dec 2012 17:53:00 +0000
draft: false
tags: [Brocade, Data Center, Data Center, Lab Time]
---

I recently had the opportinity to work with the much-anticipated [Brocade VDX "Ethernet Fabric"](http://www.brocade.com/launch/cloud-clarity/solutions-technology-innovation.html) platform.  I do admit tha tI'm intrigued by this product.  I'd seen it work multiple times in demos and it worked so well and looked to easy that we actively tried to throw curve balls at the demo organizer to prove it wasn't canned. ![](http://www.brocade.com/images/products/vdx-6720-dc-switches/VDX6720-24_front_large.jpg) It succeeded. The hardware hashing across the VLAGs is very slick.  The VMware VSwitch integration worked well and was handy.  With the movement to virtualization, this is an important piece for most data center folks. That being said, some people have very specific data center requirements that aren't really the same as an enterprise.  For example:

*   Don't firewall everything at the DC. That's right. I said it.  Firewalls don't solve all security problems.  Take that "defense in depth"!
*   A potential need to do non-standard or experimental protocols.
*   A lot of line rate 10G internally and to the rest of network.
*   Integration with legacy, existing and or in-house written tools
*   Need for GSLB/SLB
*   Self Healing
*   Ease of fabric upgrade (software upgrade doesn't cause fabric isolation)
*   Ease of fabric upgrade (increase LAG numbers and capacity easily)
*   Multi-Homed hosts
*   IPv4
*   IPv6
*   IPv4 Multicast
*   Future SDN support
*   NAT
*   Public Address space
*   All at the same time

But I digress.  We can get into the Data Center design details later.  Below would be a theoretical data center reference design for a fabric deployment.  Please bear in mind that I mostly like to focus on the WAN and SP bits, so take my data center speculations and musings with a grain of salt.

[![](http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC.jpg "Flexible DC")](http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC.jpg)   The Brocade VDX does most of what can be expected of a layer 2 fabric.  It really is the "easy" part of a DC design.  If you can avoid STP, I would heavily recommend it.  I have an unnatural dislike for spanning tree. The unexpected things I ran into with my very brief hands-on with the VDX were just that, unexpected.  I could reliably crash ssh on the boxes by sending a public key at login, which is default behavior for a normal ssh client.  This was very annoying and implied that they don't yet support ssh keys for authentication.  One can work around it by doing _ssh -o PubkeyAuthentication=no -l <name>_ and worked with the newest version of putty, which I don't use.  The version of OpenSSH on my Mac running 10.8.2 had an issue with it, as did the linux jumphost I used. There is no way, in current software to manage this centrally like you can with qfabric.  Each device is an individual switch.  I suspect this will change since it's pretty inconvenient and I know many folks have asked for it.  This was my biggest issue with it. It doesn't run spanning tree.  It has a loop detection mechanism, but it isn't spanning tree.  It's not meant to have anything but end hosts or other VDX plugged into it from what I gather, other than uplinks. Unknown SDN roadmap.  Currently it's unsupported but with the level of commitment that Brocade has given to SDN so far, I'm cautiously optimistic. Untested Layer 3 capabilities.  It's a new platform and they've just added layer3 into it.  I have no intention of testing the layer3 capabilities since I doubt that I'd want to route on them. Unknown IPv6 RA guard status.  Tis is important and I'm fairly certain they'll add it, but it wasn't in the code load that we had at SC12, at least that I could find. It is easily integrated into RANCID. [I hacked together a script to do this](http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/) in about 10 minutes and I'm an awful programmer. It looks EXACTLY like IOS so folks familiar with Ciscos venerable IOS command line will have absolutely no issue picking this right up. Some of the things I didn't get to do during this first run were to put a packet cannon like an IXIA on it and jam traffic up to, and ideally beyond the limits and see how it reacts and to point existing SNMP based tools at it (other than basic up/down status).  I'd also like to push the limits of the interconnect between geographic locations and see the latency and efficiency of the VLAG ports when moving traffic and virtual machines.  With luck these will happen at some point soon. Bear in mind that this is a relatively new product.  I would probably place the best competitor for this as the Juniper Qfabric or Microfabric, bith of which are a larger scale product and suffer from some of the same issues.  I'm excited to see more about it, it did its job pretty well.  Juniper and cisco take notice, these bits are important and [more than just brocade are working on it](http://www.plexxi.com).
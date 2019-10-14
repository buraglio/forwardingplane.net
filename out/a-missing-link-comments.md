---
title: 'A missing link in small MPLS, 10G devices.'
date: Fri, 29 Mar 2013 04:43:17 +0000
draft: false
tags: [IPv6, Musings, Routing]
---


#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-03-30 13:24:31">Mar 6, 2013</time>

The qfabric stuff seems even more green than the EX series. Perhaps i should give it another look, but I didn't have the best experience with it in testing. My guess is the mpls support will be about the same as the EX series, but it's certainly one I did not consider. Thanks, I will give it another once over.
<hr />
#### 
[EtherealMind](http://etherealmind.com "greg.ferro@packetpushers.net") - <time datetime="2013-04-01 02:40:28">Apr 1, 2013</time>

The product you want for campus backbones is also what most Enterprises would like to have for Top of Rack switching to extend MPLS to the server access layer. However the SDN market is moving to implement tunnels ( VXLAN) so there won't be any support for MPLS in the data centre (except from MPLS blowhards). There are several problems with MPLS in this platform. Because every MPLS entry and route requires a TCAM entry it's supposed to be expensive because you need a TCAM big enough to hold all the routes in your campus. Five years ago, switches could hold only 8000 MAC addresses, which is a problem today. So MPLS isn't a viable technology. Some of the MPLS tosspots are attempting to develop segmentation protocols to reduce TCAM cnsumption that might give you a long term solution but I'm doubtful. There are so many knobs, buttons and levers on MPLS that who knows what is supported and not supported anymore ? (no one seems to know why TCAM is expensive but the vendors would like us to believe it).
<hr />
#### 
[Duane]( "Duaneogrant@gmail.com") - <time datetime="2013-03-30 12:42:42">Mar 6, 2013</time>

Hi Nick, Have a look at a QFX 3500. It meets most of your requirements but MPLS is a bit of a question. If you look around, there appears to be lots of feature support in there, mostly from the qfabric stuff i'm guessing. i don't know how official it is and i haven't had a chance to play with it but it might fit your needs. Have a chat with your SE. I did with mine and he's going to pose the question to the BU for me. We might be able to use them too. good luck! -Duane dg@qfxa# set ? Possible completions: + apply-groups Groups from which to inherit configuration data + apply-groups-except Don't inherit configuration data from these groups > bfd Bidirectional Forwarding Detection (BFD) options > bgp BGP options > connections Circuit cross-connect configuration > dcbx DCBX Protocol > iccp ICCP options > igmp IGMP options > igmp-snooping IGMP Snooping Configuration > isis IS-IS options > lacp Link Aggregation Control Protocol configuration > ldp LDP options > link-management LMP options > lldp Link Layer Detection Protocol > lldp-med LLDP Media Endpoint Discovery > mld MLD options > mld-snooping MLD Snooping configuration > mpls Multiprotocol Label Switching options > msdp MSDP configuration > mstp Multiple Spanning Tree Protocol options > neighbor-discovery IPv6 neighbor discovery > oam Operation, Administration, and Management configuration > ospf OSPF configuration > ospf3 OSPFv3 configuration > pim PIM configuration > rip RIP options > router-advertisement IPv6 router advertisement options > router-discovery ICMP router discovery options > rstp Rapid Spanning Tree Protocol options > rsvp RSVP options > sflow SFLOW protocol > stp Spanning Tree Protocol options > uplink-failure-detection Uplink-failure-detection configuration > vrrp VRRP options > vstp VLAN Spanning Tree Protocol options dg@qfxa# set mpls ? Possible completions: admin-down Set GMPLS LSP to administrative down state > admin-group Administrative group policy > admin-group-extended Extended administrative group policy > admin-groups Administrative groups advertisement-hold-time Time that an 'LSP down' advertisement will be delayed + apply-groups Groups from which to inherit configuration data + apply-groups-except Don't inherit configuration data from these groups > auto-policing Automatic policing of LSPs > bandwidth Bandwidth to reserve (bps) class-of-service Class-of-service value (0..7) > diffserv-te Global diffserv-traffic-engineering options disable Disable MPLS > egress-protection Egress router protection exclude-srlg Exclude SRLG links for secondary path expand-loose-hop Perform CSPF path computation to expand loose hops explicit-null Advertise the EXPLICIT\_NULL label when the router is the egress hop-limit Maximum allowed router hops (2..255) icmp-tunneling Allow MPLS LSPs to be used for tunneling ICMP error packets > interface MPLS interface options ipv6-tunneling Allow MPLS LSPs to be used for tunneling IPv6 traffic > label-switched-path Label-switched path > log-updown Logging actions for LSP up/down events > lsp-external-controller External path computing entity mib-mpls-show-p2mp Show p2mp tunnels entries in mpls mib walk no-cspf Disable automatic path computation no-decrement-ttl Do not decrement the TTL within an LSP no-propagate-ttl Disable TTL propagation from IP to MPLS (on push) and MPLS to IP (on pop) no-record Don't record transit routers > oam Periodic OAM optimize-aggressive Run aggressive optimization algorithm based on IGP metric only optimize-hold-dead-delay Delay before tearing down the old optimized path (seconds) optimize-switchover-delay Delay before switching LSP to newly optimized path optimize-timer Periodical path reoptimizations (0..65535 seconds) > path Route of a label-switched path > path-mtu Path MTU configuration preference Preference value priority Preemption priorities record Record transit routers revert-timer Hold-down window before reverting back to primary path, 0 means disable rsvp-error-hold-time Time that RSVP PathErr events will be remembered (seconds) smart-optimize-timer Path optimization interval after a link traversed by the path goes down standby Keep backup paths in continuous standby > static-label-switched-path Static label-switched path > statistics Collect statistics for signaled label-switched paths > traceoptions Trace options for MPLS traffic-engineering Protocols to perform traffic engineering > transit-lsp-association Transit label switch path assoication ultimate-hop-popping Request ultimate hop popping from egress \[edit protocols\]
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-03-30 20:51:27">Mar 6, 2013</time>

That is great info. I'd love to hear more about your deployment because honestly the qfx didn't even come onto my radar since my experience was strictly within qfabric. I agree, "buy a router" is a ridiculous statement to hear when you talk about a 380 building campus. 300+ MX80s? Riiiiight. Let me put those in the back of my company provided Maserati and drive them out to install.
<hr />
#### 
[Duane]( "Duaneogrant@gmail.com") - <time datetime="2013-03-30 20:22:19">Mar 6, 2013</time>

Hi Nick, I didn't mean to suggest that you use the box in a fabric but rather standalone. Qfabric uses MPLS and ISIS under the hood to accomplish the qfabric magic, so I'm hoping that fact coupled with the trident chips ability to deal with multiple tags might result in pretty complete MPLS support. The asic in the EX has a single tag limitation. i've asked my SE about formal MPLS support and he's going to be talking to the BU next week. Have a look at the control plane on these things: 3Gb of RAM and a 12 core 1.2Ghz processor. That's quite a bit of control plane for a TOR... I'm using the qfx in a relatively complicated ip edge roll. It's still cabled up to the Ixia, but so far, so good. When i ask some other vendors about specific features, they tell me to buy a router to do that job. Given the port counts and speeds that i'm talking about, that pushes me into a pretty big box at 10X the cost. if i get around to looking at the qfx with MPLS enabled, i'll be sure to let you know. --Duane
<hr />
#### 
[Duane]( "Duaneogrant@gmail.com") - <time datetime="2013-06-23 18:54:20">Jun 0, 2013</time>

Hi Nick, We've got ex4550s running as well and they are nice boxes too (if you don't need mpls). I had to upgrade to the latest release to get DOM working and stop some spurious PSU messages from being sent, other than that, pretty smooth sailing. RE: Ex9200, there are 3 sizes, and they equate to mx240, mx480 and mx960. That said, the prices tag (and features) do not match the MX. These boxes are tailor made for a use case I have that doesn't require fancy hqos but does require some deep buffers. The REs in the box are 16G of memory and a quad core Intel chip for SDN uses. I don't need that today, but for the price, it makes the box even more useful for me as i look around the network.
<hr />
#### 
[Pete Welcher](http://www.netcraftsmen.net/about-us/bios/staff-articles-and-blogs/pete-welcher.html "pjw@netcraftsmen.net") - <time datetime="2013-04-18 18:27:36">Apr 4, 2013</time>

I've thought along similar lines for quite a while, mostly re Cisco. It might be cost, it might be turf defense by the 6500 team (lots of internal clout until recently). But it might just be positioning -- not anticipating a use case like this, and/or not having models with sufficient CPU / RAM / forwarding chips / whatever. Its a small enough market (?) that engineering something specifically for it is probably not cost effective? The use case I've seen is small rural provider networks, where a Cisco 6500 costs too much. And where folks want MPLS to eventually scale up better than L2 techniques do. The ME series was perennially overly costly and an order of magnitude slow. 3560-G partially worked in the 1 G edge / 10 G core space for a while. Using VRF Lite, not MPLS.
<hr />
#### 
[Duaneo]( "Duaneogrant@gmail.com") - <time datetime="2013-06-23 10:24:53">Jun 0, 2013</time>

Hi Nick, After asking my SE a couple of times, the answer I received was, "it works, but its not officially supported and I'm not sure it's gonna be." That said, have you had a look at the ex9200? It seems to have the mpls support you need and a 32 port 10ge card as well. The box come with a huge RE, mostly to support SDN I suspect and a pretty modest price tag and support costs. Compared to our 7600s and asr9k, the 9200 is a compelling buy if you can make do with the feature set. For fancy hqos, we're stuck with the 9k or mx as the advanced features just aren't there and we're not buying new 7600s. I'm hearing some interesting things about the next gen qfx box as well, which is due out later this year.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-06-23 12:02:45">Jun 0, 2013</time>

Check out the ex4550 running 12.3. It has a larger route / TCAM table. The ex9200 is essentially an mx960, and while it does have the ports it is far too expensive and huge or what we need.
<hr />
#### 
[John Harrington (@networksherpa)](http://thenetworksherpa.com "johnharr.ie@gmail.com") - <time datetime="2013-04-11 23:27:49">Apr 4, 2013</time>

I agree with Duane. The QFX is a rocking standalone box, and I believe MPLS is a committed feature.
<hr />
#### 
[Jawaid Bazyar]( "jawaid.bazyar@forethought.net") - <time datetime="2015-05-24 20:38:00">May 0, 2015</time>

Check out Telco Systems, www.telco.com. We've been using their inexpensive MPLS for a couple years.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2015-06-20 08:15:00">Jun 6, 2015</time>

I've actually seen these in production but never actually used one myself. I'll give them another look, thanks!
<hr />

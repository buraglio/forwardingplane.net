---
id: 147
title: 'Plexxi could be WDM for the rest of us.'
date: '2012-12-10T23:15:42-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=147'
permalink: /2012/12/10/plexxi-could-be-wdm-for-the-rest-of-us/
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3682720334'
Views:
    - '146'
categories:
    - 'Data Center'
    - SDN
---

<a href="http://www.plexxi.com">Plexxi</a> is an interesting product that has recently emerged in the data center space.  While data center, fabric and cloud are all the rage in the buzzword world of data networking, this one caught my attention because it was something unique that I'd not seen before.  Their TOR boxes have a few interesting additions to them, the first of which is a WDM port on the back. Now, I'm not really a stranger to the WDM world.  I've been helping maintain a DWDM network in one capacity or another for a little over a decade, but seeing this, by default, in a data center positioned switch?  Now that got my attention.
For those that don't know what that is, <a href="http://en.wikipedia.org/wiki/Wavelength-division_multiplexing">Wave Division Multiplexing</a> the ability to slice up light into what telco (and other networking folks) call waves. Each wave is a different "color" or wavelength.  Plexxi calls their flavor "Affinity Networking" and it allows for the ability to provision more bandwidth over a single pair of fiber, just like typical WDM.
For example, say you have a pair of fiber from one data center to another, either in the same facility or across your city (distances up to 10K now, 70K on the roadmap).  You'd normally plug in a 1G or 10G (or 100G if you're really, really well funded) and provision service over that pair of fiber, assuming it is in within distance and optical power spec of the other side.  You're stuck with that interface speed, right?  Wrong. Enter WDM.   On WDM systems you have the ability to provision channels, sometimes in huge amounts, over the same pair.  I've seen multiple 100G waves, OC192 Waves, a plethora of 10G waves and a few 1G waves all working fine over the same pair of fiber, and where fiber is sparse or prohibitively expensive, this is a big deal.
<a href="http://www.forwardingplane.net/wp-content/uploads/2012/12/prism4c.gif"><img class="aligncenter size-full wp-image-163" title="prism4c" src="http://www.forwardingplane.net/wp-content/uploads/2012/12/prism4c.gif" alt="" width="400" height="300" /></a>
Plexxi "Affinity Networking" boasts the ability to do WDM right in the back of their 32 port 10G switches.
Very slick.  But that's not all.  Enter part 2.  They also boast software defined (but not OpenFlow) control over the product, enabling dynamic provisioning of  bandwidth, on demand.. They've purpose built their own proprietary and described as "extended" version of SDN, geared toward a bigger picture of their network equipment and what it can do.  Their  SDN is called called "Plexxi Control" and it ties all of their switches together, allowing for a flattening of the network.  I find this approach intriguing, I'm a fan of the fabric approach to layer 2 a la <a href="http://www.juniper.net/us/en/products-services/switching/qfx-series/">Juniper Qfabric</a> or <a href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/">Brocade VDX</a>, but the WDM port and the decoupled control together is unique ....and enthralling.
Now, I have not yet had my hands on these boxes, but I think that they will be a piece in what has become a rapidly changing landscape of data centers.  WDM has been around forever in the service provider wide area, but the ability to change bandwidth allocations using WDM on the fly in a commercially supportable commoditized box is game changing.  There have been several research projects in the past that have attempted to do this, the <a href="http://dragon.maxgigapop.net/twiki/bin/view/DRAGON/WebHome">DRAGON project</a>, of which one of the sites I helped maintain was a member, attempted to do something like this using <a href="http://en.wikipedia.org/wiki/Generalized_Multi-Protocol_Label_Switching">GMPLS</a>  on the WAN gear.
Doing it in the data center?  That's new.
I look forward to seeing some of these boxes function up close and personal.  I'm especially interested in the longer distance pieces of these for remote data centers and DR locations.
For a comprehensive write up, see <a href="http://searchnetworking.techtarget.com/news/2240173858/Plexxi-SDN-includes-tiered-controller-data-center-based-WDM">this article</a> by <a href="http://searchnetworking.techtarget.com/contributor/Shamus-McGillicuddy">Shamus McGillicuddy</a>.  <a href="http://searchnetworking.techtarget.com/news/2240173858/Plexxi-SDN-includes-tiered-controller-data-center-based-WDM"> </a>
<h3></h3>
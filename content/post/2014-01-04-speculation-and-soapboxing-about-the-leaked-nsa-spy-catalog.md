---
id: 858
title: 'Speculation and soapboxing about the leaked NSA spy catalog.'
date: '2014-01-04T11:15:40-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=858'
permalink: /2014/01/04/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/
themeblvd_title:
    - 'Speculation and soapboxing about the leaked NSA spy catalog.'
themeblvd_keywords:
    - 'NSA, Security, Networking, SDN, OpenFlow, IDS, Bro, Snort'
themeblvd_description:
    - 'NSA spy catalog and what''s not being said. Speculation about the NSA security backdoor catalog and toolbox. '
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '2154133710'
Views:
    - '80'
categories:
    - Security
    - 'Soap Box'
---

The buzz as of late around the security and networking communities has been about the [NSA and their catalog or spy toolkit](http://www.spiegel.de/international/world/nsa-secret-toolbox-ant-unit-offers-spy-gadgets-for-every-need-a-941006.html).  I've spent time in my career thinking about and doing infosec and I did a brief stint working for the FBI in a project called [NCDIR](http://gcn.com/articles/2007/08/20/fbi-launches-cybersecurity-project.aspx).  I like to think that I can provide at least a peripherally competent commentary about it [take it with a grain of salt].  Instead of thinking about the morality of it or the violation of privacy that everyone else seems to be focused on, I want to think about the mechanics.
If one takes the emotion and outrage out of the equation, there are some [really interesting tools here](http://permalink.gmane.org/gmane.comp.encryption.general/17244).  My initial thoughts, though, are "how is the backdoor installed?" and "how is the data harvested?" There are cases where I'm sure the backdoors are installed via local access and the data is harvested in uninteresting ways like optical taps, wireless bridges, etc., however, what how about in cases where this isn't possible?  What about when the equipment is in a bunker with no viable wireless in or out, it's have to be done either in-band or via a tap, which would require physical access.   It'd be interesting to see a [BroIDS](http://www.bro.org/) or [Snort](http://www.snort.org/) policy for the "DNT Implant Communications Protocol" once that is deconstructed.
As far as installation of the backdoor, how about the case about when interception of hardware in transit isn't an option and physical access is also not viable?  The implications of remotly exploitable network equipment for things such as this are very-wide scoped and ***extremely*** unpleasant.  One can assume that if our government can exploit something like this, so can another nation-state.  Not good.  Not good at all.  How much of our gear is manufactured abroad?  They have physical access because they ***build*** it, one could assert that it is plausible that "they" could insert whatever they wanted in the hardware.  Again, I'm not a hardware engineer, but I can speculate.
[![](http://www.forwardingplane.net/wp-content/uploads/2014/01/40g-tap-500x500-300x126.jpg)](http://www.forwardingplane.net/wp-content/uploads/2014/01/40g-tap-500x500.jpg)
I'd be really interested in seeing if data is being harvested inline, without a tap and how that is being done.  It's implied in some of the descriptions of the *THROUGH listings that there is inline control available.  What I'd really be interested in seeing is someone that can capture that traffic flow data in an upstream device.  Flow data doesn't lie, and it is highly likely that there is a router in the path somewhere exporting flow data that isn't obfuscating traffic by being compromised.  Where is the traffic going?  How is it transported (encrypted, for sure, but how?)
How does this change how we, as network engineers, feel about RMA'd hardware?  If the manufacturers don't know about modded boot ROMS, it's likely that RMA'd hardware is being shipped all over with backdoors that were intended for someone else in it.  Oh, and another thing, this is an *old* document.  2008 is a lifetime ago in terms of networking and computing technology.  I saw no mention of the [Juniper SRX](http://www.juniper.net/us/en/products-services/security/srx-series/), [Juniper MX](http://www.juniper.net/us/en/products-services/routing/mx-series/), [Cisco ASR](http://www.cisco.com/en/US/products/ps9343/prod_models_comparison.html), [Brocade MLX/CES](http://www.brocade.com/products/all/routers/index.page) or[ Alcatel-Lucent](http://www.alcatel-lucent.com/) devices.  I'd bet real money all of that exists now.
Additionally, what about [FIPS 140](http://en.wikipedia.org/wiki/FIPS_140)?  I want to believe this can come into play, but admittedly I don't know a lot about FIPS, just what I've read on the [NIST site](http://csrc.nist.gov/groups/STM/cmvp/standards.html#02).  How does FIPS assist in preventing the software hacks? Or does it? As far as most of the the network equipment backdoors, they imply that boot time code modifies the OS, can cryptographic checks aide in rooting some of these out?  I have not done much in this aspect of security, but I have to believe there is a way to detect this kind of boot time modification of the OS.
This opens up an entirely new aspect of SDN, too. When your control plane is decoupled and likely running on a linux box of some sort, the targeting of "the network" becomes far more simple of a compromise.  Ever done linux forensics?  Most of the hacks are fairly low-brow.  Root one box and you have access to the control plane of a data center, internet backbone or campus network.  What about all of the white box network devices that are just linux like [Arista](http://www.aristanetworks.com/) and [Cumulus Networks](http://cumulusnetworks.com/)? Now we're managing linux boxes like we are with Juniper and FreeBSD, except they are less customized and more vanilla (read: potentially more likely to be exploitable).  This is a problem.  Think because you have a firewall and a NAT device you're safe?  You're wrong [clearly].  Hardening controllers will be increasingly important, perhaps even running them on trusted unix platforms.  It's a problem that is now much easier than intercepting hardware in transit and installing backdoors into it, but an in-depth SDN security talk is an *entirely* different can of worms.
This just solidifies my thought that if something is ***so*** critically important that it must remain secret and secure, don't put it on a computer.  Especially one with a network connection.
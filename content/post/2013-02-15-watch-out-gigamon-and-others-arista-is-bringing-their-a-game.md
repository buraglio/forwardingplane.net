---
id: 439
title: 'Watch out, Gigamon (and others), Arista is bringing their A game'
date: '2013-02-15T21:11:20-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=439'
permalink: /2013/02/15/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'Arista, Bro-IDS, Snort, Tap, Symmetric Hash, IPS, Security, python, sysdb'
themeblvd_title:
    - 'Arista as an intrusion detection tap solution'
themeblvd_description:
    - 'Arista Networks switches as an intrusion detection tap solution using their new symmetric hashing feature. Replace expensive tap solutions using off the shelf ethernet switches managed like any other network hardware for better, performance, ROI and OpEx. '
dsq_thread_id:
    - '3629199579'
Views:
    - '1130'
categories:
    - 'Data Center'
    - 'Lab Time'
    - Security
    - UNIX
---

It's no secret that I'm a fan of the model <a href="http://www.aristanetworks.com" target="_blank" rel="noopener noreferrer">Arista Networks</a> is using to make gear and provide innovative services and products. In my opinion, they're changing the landscape of campus and data center networking gear. I'm always a fan of the little guy trying to change the world and this falls under that category. For those that don't know, Arista Networks is a "hardware" networking company that is using merchant silicon wrapped in their custom linux based operating system (which is very much like IOS).
<p style="text-align: center;"><a href="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.jpg"><img class="aligncenter wp-image-445" alt="ARISTA-TAP" src="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-1024x768.jpg" width="430" height="323" /></a></p>
This model does a few things. It takes the time it would normally take a vendor to engineer and spin an ASIC, typically 1-3 years) and completely removes it. Instead, they rely on silicon manufacturers like Intel and <a href="http://www.fulcrummicro.com" target="_blank" rel="noopener noreferrer">Fulcrum</a> for their already engineered and tested chips. Arista is generally touted as an extremely low latency box and has been widely deployed in the financial industry because of this. However, they're not a one trick pony, not by any means. Their open architecture and OS allows for <span style="text-decoration: underline;"><strong>heavy</strong></span> customization. In fact, unlike most others, it's encouraged. Arista has put together an <a href="https://eos.aristanetworks.com/home.php" target="_blank" rel="noopener noreferrer">ecosystem for extending and expanding</a> their <a href="https://eos.aristanetworks.com/2011/03/eos-so-what-is-it/" target="_blank" rel="noopener noreferrer">EOS</a> networking operating system. Want something added to the CLI? Easy, it's all python and can be changed on-box and submitted back to the community. They also have a very, very slick internal mechanism called the sysdb, but that's another blog post altogether.
 
None of this is really new. Folks have been using merchant silicon forever. What is new and refreshing is the open nature of it. Additionally, the exclusive use of merchant silicon is something [I believe] is now in this class of hardware. With the open nature of this platform, it also lends itself well to the OpenFlow movement in that it's essentially a linux box on well documented hardware of which the vendor is encouraging modification. In addition, it is a well tested data center product. I'm calling it now, this platform is going to go places in it's market.
For the newest addition to the capabilities portfolio, this is where it really gets interesting. As of 2/13/2013 Arista has added some very <a href="http://www.aristanetworks.com/en/news/pressrelease/532-pr-20130212-01" target="_blank" rel="noopener noreferrer">compelling tap aggregation options</a>. What this means, is that you can now aggregate Nx1 or 10G at 40G, then symmetrically hash that across another 10G array to an IDS cluster. Why is this important? Monitoring fat links. Have some 100G? Good luck finding a security mechanism to watch that.
<p style="text-align: center;"><a href="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png"><img class="aligncenter wp-image-440" alt="ARISTA TAP" src="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png" width="467" height="354" /></a></p>
Until now the only options for this are players like <a href="http://www.gigamon.com" target="_blank" rel="noopener noreferrer">Gigamon</a>, <a href="http://www.cpacket.com" target="_blank" rel="noopener noreferrer">cPacket</a> and maybe <a href="http://www.mrv.com" target="_blank" rel="noopener noreferrer">MRV</a>. All are very expensive and one-off solutions. Arista offers a standard ethernet switch that can be managed by an existing networking team, integrated into existing network tools and maintained like any other router or switch. OpEx is a wash. Capital expenditure is standard [probably cheaper] than a normal Layer2 switch. It looks JUST like IOS, so the old networking guy that hates change will only complain a little that it's not a blue box with a bridge on it.
This may seem like a small deal, but the implications for passive security monitoring are huge. This feature alone will have a trickle down effect over the next few years since it's something that is only recently being exercised in enterprise worlds. I suspect this will also have a very large impact to gigamon, who is really the current industry leader in this corner of the market, but is priced well beyond what many can afford.
Arista can now do the symmetric hashing on layer2, layer3 or layer4 parameters. ACL support is also coming, although I've not seen it work like I have the hashing.
 
Oh, you want to know how to do it? =) It currently doesn't exist in the CLI, but here is basically how it's done. Thanks to an awesome Arista rep, the heavy lifting of parsing through the Acons interface is all condensed to a simple script.
from the CLI:
Log in and enable.
<pre>7150-Source#bash
Arista Networks EOS shell
[arista@7150-Source ~]$ cd /mnt/flash
[arista@7150-Source ~]$vi set_hash.sh
#!/bin/ti
rm /mnt/flash/set_hash_log.txt
cat &lt;&lt; EOF | Acons FocalPointV2 &gt;&gt; /mnt/flash/set_hash_log.txt 2&gt;&1
from FmApi import *
fmDbgWriteRegisterField(0,0,0,0,"FM6000_HASH_LAYER3_PROFILE","SymmetrizeL3",1)
fmDbgWriteRegisterField(0,0,0,0,"FM6000_HASH_LAYER3_PROFILE","SymmetrizeL4",1)
fmDbgWriteRegisterField(0,0,0,0,"FM6000_HASH_LAYER2_KEY_PROFILE","SymmetrizeMAC",1)
EOF
exit 0</pre>
Done. This, of course, doesn't include any of the port channel and monitor interface configuration, but if you're this deep, you probably know how to do that already.
If you'd like to dump this to a log, add the following lines to the end of the script before the "EOF"
<pre>fmDbgDumpRegisterV2(0,0,0,"FM6000_HASH_LAYER2_KEY_PROFILE")
fmDbgDumpRegisterV2(0,0,0,"FM6000_HASH_LAYER3_PROFILE")</pre>
*As the CLI bits become available in EOS 4.12, this post will be amended to the more supportable way of managing this awesome new feature.
 
 
 
 
 
 
 
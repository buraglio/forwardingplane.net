---
title: 'Watch out, Gigamon (and others), Arista is bringing their A game'
date: Sat, 16 Feb 2013 03:11:20 +0000
draft: false
tags: [Data Center, Lab Time, Security, UNIX]
---

It's no secret that I'm a fan of the model [Arista Networks](http://www.aristanetworks.com) is using to make gear and provide innovative services and products. In my opinion, they're changing the landscape of campus and data center networking gear. I'm always a fan of the little guy trying to change the world and this falls under that category. For those that don't know, Arista Networks is a "hardware" networking company that is using merchant silicon wrapped in their custom linux based operating system (which is very much like IOS).

[![ARISTA-TAP](http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-1024x768.jpg)](http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.jpg)

This model does a few things. It takes the time it would normally take a vendor to engineer and spin an ASIC, typically 1-3 years) and completely removes it. Instead, they rely on silicon manufacturers like Intel and [Fulcrum](http://www.fulcrummicro.com) for their already engineered and tested chips. Arista is generally touted as an extremely low latency box and has been widely deployed in the financial industry because of this. However, they're not a one trick pony, not by any means. Their open architecture and OS allows for **heavy** customization. In fact, unlike most others, it's encouraged. Arista has put together an [ecosystem for extending and expanding](https://eos.aristanetworks.com/home.php) their [EOS](https://eos.aristanetworks.com/2011/03/eos-so-what-is-it/) networking operating system. Want something added to the CLI? Easy, it's all python and can be changed on-box and submitted back to the community. They also have a very, very slick internal mechanism called the sysdb, but that's another blog post altogether.   None of this is really new. Folks have been using merchant silicon forever. What is new and refreshing is the open nature of it. Additionally, the exclusive use of merchant silicon is something \[I believe\] is now in this class of hardware. With the open nature of this platform, it also lends itself well to the OpenFlow movement in that it's essentially a linux box on well documented hardware of which the vendor is encouraging modification. In addition, it is a well tested data center product. I'm calling it now, this platform is going to go places in it's market. For the newest addition to the capabilities portfolio, this is where it really gets interesting. As of 2/13/2013 Arista has added some very [compelling tap aggregation options](http://www.aristanetworks.com/en/news/pressrelease/532-pr-20130212-01). What this means, is that you can now aggregate Nx1 or 10G at 40G, then symmetrically hash that across another 10G array to an IDS cluster. Why is this important? Monitoring fat links. Have some 100G? Good luck finding a security mechanism to watch that.

[![ARISTA TAP](http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png)](http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png)

Until now the only options for this are players like [Gigamon](http://www.gigamon.com), [cPacket](http://www.cpacket.com) and maybe [MRV](http://www.mrv.com). All are very expensive and one-off solutions. Arista offers a standard ethernet switch that can be managed by an existing networking team, integrated into existing network tools and maintained like any other router or switch. OpEx is a wash. Capital expenditure is standard \[probably cheaper\] than a normal Layer2 switch. It looks JUST like IOS, so the old networking guy that hates change will only complain a little that it's not a blue box with a bridge on it. This may seem like a small deal, but the implications for passive security monitoring are huge. This feature alone will have a trickle down effect over the next few years since it's something that is only recently being exercised in enterprise worlds. I suspect this will also have a very large impact to gigamon, who is really the current industry leader in this corner of the market, but is priced well beyond what many can afford. Arista can now do the symmetric hashing on layer2, layer3 or layer4 parameters. ACL support is also coming, although I've not seen it work like I have the hashing.   Oh, you want to know how to do it? =) It currently doesn't exist in the CLI, but here is basically how it's done. Thanks to an awesome Arista rep, the heavy lifting of parsing through the Acons interface is all condensed to a simple script. from the CLI: Log in and enable.```
7150-Source#bash
Arista Networks EOS shell
\[arista@7150-Source ~\]$ cd /mnt/flash

\[arista@7150-Source ~\]$vi set\_hash.sh
#!/bin/ti
rm /mnt/flash/set\_hash\_log.txt
cat << EOF | Acons FocalPointV2 >> /mnt/flash/set\_hash\_log.txt 2>&1
from FmApi import \*
fmDbgWriteRegisterField(0,0,0,0,"FM6000\_HASH\_LAYER3\_PROFILE","SymmetrizeL3",1)
fmDbgWriteRegisterField(0,0,0,0,"FM6000\_HASH\_LAYER3\_PROFILE","SymmetrizeL4",1)
fmDbgWriteRegisterField(0,0,0,0,"FM6000\_HASH\_LAYER2\_KEY\_PROFILE","SymmetrizeMAC",1)
EOF
exit 0
```Done. This, of course, doesn't include any of the port channel and monitor interface configuration, but if you're this deep, you probably know how to do that already. If you'd like to dump this to a log, add the following lines to the end of the script before the "EOF"```
fmDbgDumpRegisterV2(0,0,0,"FM6000\_HASH\_LAYER2\_KEY\_PROFILE")
fmDbgDumpRegisterV2(0,0,0,"FM6000\_HASH\_LAYER3\_PROFILE")
```\*As the CLI bits become available in EOS 4.12, this post will be amended to the more supportable way of managing this awesome new feature.
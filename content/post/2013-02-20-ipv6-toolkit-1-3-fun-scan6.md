---
id: 457
title: 'IPv6 Toolkit 1.3 fun – scan6'
date: '2013-02-20T04:53:38-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=457'
permalink: /2013/02/20/ipv6-toolkit-1-3-fun-scan6/
themeblvd_noindex:
    - 'true'
Views:
    - '342'
categories:
    - IPv6
    - 'Lab Time'
    - Security
---

Recently <a href="http://www.si6networks.com/tools/ipv6toolkit/" target="_blank" rel="noopener noreferrer">SI6 released the IPv6 Toolkit 1.3 </a>  This release is on the heels of this <a href="http://tools.ietf.org/html/draft-ietf-opsec-ipv6-host-scanning-00" target="_blank" rel="noopener noreferrer">IETF draft </a> on IPv6 host scanning.  It was long thought that scanning an IPv6 network was impossible.  The address space was too large and reliably ascertaining the hosts from it would be too time consuming to even attempt.  However, as <a href="http://en.wikipedia.org/wiki/Hans_Zarkov" target="_blank" rel="noopener noreferrer">Dr. Hans Zarkov </a>says in the 1980 classic cult film of my youth, <a href="http://en.wikipedia.org/wiki/Flash_Gordon_(film)" target="_blank" rel="noopener noreferrer">Flash Gordon</a>, "You can't beat the human spirit!"  That fine community out there has thought outside the box and found a way.
<p style="text-align: center;"><img class="aligncenter" alt="" src="http://www.thiel-a-vision.com/wp-content/uploads/2010/07/flash68sm.jpg" width="468" height="202" /></p>
I'm a network engineer by profession, but I've been a security guy more than once during my ~15 years doing IT work; I think there is definite value in studying "the dark side" and learning it's power.  Couple that with my zealotry of IPv6....and I've found a time vortex.
Scanning IPv6 is not like scanning IPv4.   It can't be.  A /64 network has 18,446,744,073,709,551,616 (18 quintillion) unique addresses and a /64 is the default allocation for an end user subnet.  Have fun scanning that one by one.  The methodology used by scan6 is pretty innovative, but first you have to build it.
The <a href="http://www.si6networks.com/tools/ipv6toolkit/" target="_blank" rel="noopener noreferrer">IPv6 toolkit</a> is available via download <a href="http://www.si6networks.com/tools/ipv6toolkit/ipv6-toolkit-v1.3.1.tar.gz" target="_blank" rel="noopener noreferrer">here</a>.  It is current;y supported under FreeBSD, NetBSD, OpenBSD, Linux, and Mac OS X.  I've chosen to build mine on my laptop, a macbook pro running OS 10.8.
It's pretty straightforward to build assuming you have the Developers Tools and CLI support added.
<em>(~/Downloads/ipv6-toolkit-v1.3) Tardis $ make</em>
<em>gcc -Wall -o flow6 tools/flow6.c -lpcap -lm </em>
<em>gcc -Wall -o frag6 tools/frag6.c -lpcap -lm </em>
<em>gcc -Wall -o icmp6 tools/icmp6.c -lpcap -lm</em>
<em>gcc -Wall -o jumbo6 tools/jumbo6.c -lpcap -lm</em>
<em>gcc -Wall -o na6 tools/na6.c -lpcap -lm</em>
<em>gcc -Wall -o ni6 tools/ni6.c -lpcap -lm</em>
<em>gcc -Wall -o ns6 tools/ns6.c -lpcap -lm</em>
<em>gcc -Wall -o ra6 tools/ra6.c -lpcap -lm</em>
<em>gcc -Wall -o rd6 tools/rd6.c -lpcap -lm</em>
<em>gcc -Wall -o rs6 tools/rs6.c -lpcap -lm</em>
<em>gcc -Wall -o scan6 tools/scan6.c -lpcap -lm</em>
<em>gcc -Wall -o tcp6 tools/tcp6.c -lpcap -lm</em>
 
That's it.  If you want to install it in the global environment, to a "<em>make install</em>"
Now for the good stuff.  The docs are well written for this tool. Here is an example of scanning a local segment in verbose mode and the output:
<em>(~/Downloads/ipv6-toolkit-v6.8) tardis $ sudo ./scan6 -i en6 -l -e -v</em>
<em>Link-local addresses:</em>
<em>fe80::20d:b9ff:fe68:8ca6 @ 00:0d:b9:68:8c:a6</em>
<em>fe80::264:d6ff:fe25:9704 @ 00:64:d6:25:97:04</em>
<em>fe80::26f:f8ff:fe06:dcb4 @ 00:6f:f8:06:dc:b4</em>
<em>fe80::22cf:80ff:fea8:ec26 @ 20:cf:80:a8:ec:26</em>
<em>fe80::224:86ff:fe9f:c628 @ 00:24:86:9f:c6:28</em>
<em>fe80::267:f2ff:fe52:8574 @ 00:67:f2:52:85:74</em>
<em>fe80::8ed0:f8ff:fe8a:4d29 @ 8c:d0:f8:8a:4d:29</em>
<em>fe80::62fa:cdff:fe86:62bd @ 60:fa:cd:86:62:bd</em>
<em>fe80::629a:ddff:fe45:6c08 @ 60:9a:dd:45:6c:08</em>
<em>Global addresses:</em>
<em></em><em>2001:db8:86c0:24::6 @ 00:0d:b9:68:8c:a6</em>
<em>2001:db8:86c0:24:224:86ff:fe9f:c628 @ 00:24:86:9f:c6:28</em>
<em>2001:db8:86c0:24:22cf:80ff:fea8:ec26 @ 20:cf:80:a8:ec:26</em>
<em>2001:db8:86c0:24:26f:f8ff:fe06:dcb4 @ 00:6f:f8:06:dc:b4</em>
<em>2001:db8:86c0:24:267:f2ff:fe52:8574 @ 00:67:f2:52:85:74</em>
<em>2001:db8:86c0:24:62fa:cdff:fe86:62bd @ 60:fa:cd:86:62:bd</em>
<em>2001:db8:86c0:24:8ed0:f8ff:fe8a:4d29 @ 8c:d0:f8:8a:4d:29</em>
<em>2001:db8:86c0:24:629a:ddff:fe45:6c08 @ 60:9a:dd:45:6c:08</em>
This example,  taken straight from the documentation and run on my local network (with MAC and v6 addresses changed to protect the innocent), will "Perform host scanning on the local network (“-l” option) using interface “eth0” (“-i” option). Use both ICMPv6 echo requests and unrecognized IPv6 options of type 10xxxxxx (default). Print link- link layer addresses along with IPv6 addresses (“-e” option). Be verbose (“-v” option)."
One of the interesting things I saw available in this scan6 tool was the ability to narrow down a search based on a known OUI.  If someone wanted to search for virtual machines hosted by VMWare host and the IPv4 address of the VMWare host is known, this command would be useful for scanning from a host off net, scanning a network in the lab area:
<div title="Page 6">
<em>sudo ./scan6 -i en0 -d 2001:db8:e00:4000::/64 –tgt-virtual-machines vmware –tgt-ipv4-embedded 10.17.4.195/32</em>
</div>
<div title="Page 6">
 What this does is target the /64 but narrow down the search to vmwre specific virtual machines hosted on the vmware host at IPv4 address 10.17.4.195/32. It is able to accomplish this because it can make assumptions about vmware (or virtual box) based on their OUI and how they build their
The OUI will always be set to  00:05:59 for VMWare.  Additionally, The next 16-bits of the MAC address are set to the same value as the last 16 bits of the console operating system's primary IPv4 address. If that were not enough, the final eight bits of the MAC address are set to a hash value based on the name of the virtual machine's configuration file. That, according to the IETF draft and math, means that if you know the VMWare host IPv4 address you can reduce a scan of 64 bits down to just 8 bits.  This is a powerful set of tools that this post does not even scratch the surface of.
Be careful using this scan tool, there are a number of devices that will have their neighbor table exhausted and potentially cause a DoS by running the networking gear out of resources, which in and of itself is another potential use of this tool.  There is a HUGE amount of work to be done and learned about IPv6, it's not going away and, in fact, I've been using it in one form or another for 10 years or so.  If you're a network engineer or a security professional you're doing yourself a disservice by not learning it.
In addition to the scan6 binary, the toolkit includes:
flow6
frag6
icmp6
jumbo6
na6
ni6
ns6
ra6
rd6
rs6
scan6
tcp6
With the content providers and consumer ISPs providing native IPv6 more and more every day (my comcast service has a DHCPv6-PD /64 and a DHCPv6 /128 provisioned by default) the world at large is doing more v6.  If you've got MS windows on your network and it's even relatively new, you've got v6 unless you policy it as disabled.  It's tunneling it.
Make these part of your arsenal for testing gear, pen testing, whatever. I promise it's worth your time.
</div>
 
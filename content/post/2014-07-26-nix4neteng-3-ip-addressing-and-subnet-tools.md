---
id: 1039
title: 'NIX4NetEng #3: IP Addressing and Subnet Tools'
date: '2014-07-26T10:46:07-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1039'
permalink: /2014/07/26/nix4neteng-3-ip-addressing-and-subnet-tools/
themeblvd_title:
    - 'ip addressing and subnet tools for the devops engineer'
themeblvd_keywords:
    - 'ipv6 subnet calculator, ipv4 ubnet calculator, subnet calculator, unix, SDN, openflow, ipv6, nick buraglio, buraglio, sipcalc, ipcalc, hex convertor, decimal to hexidecimal converter, nix4neteng, devops'
themeblvd_description:
    - 'Utilize command line tools for checking ipv4 and ipv6 addressing.  '
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '2875360568'
Views:
    - '159'
categories:
    - How-To
    - IPv6
    - NIX4NetEng
    - UNIX
---

IP addressing and subnetting is a common interview subject. I assert that memorizing these things is useful for learning the concepts but ultimately futile in that it is time consuming and inefficient use of engineering time when tools can be utilized to accomplish the same goals in less time with fewer errors. Honestly, I gave up doing this kind of work manually around 10 years ago and have never regretted it, and in actuality, I'd probably struggle to do it at this point because it's a repetitive process better suited by code.
In the old days, subnetting IPv4 manually was a badge of honor (and one that I always hated), but I learned it because I needed to know it for cert tests and daily work. However, once I started doing IPv6 around 2001, it became clear that doing this kind of thing by hand was consuming more time than it needed to.
Enter UNIX tools.
HEX
Hex isn't really a tool as much as it's a hack for your shell.  Remember the <a title="NIX4NetEng #1 Managing dotfiles; pwn the unspoken pain of UNIX administration" href="http://www.forwardingplane.net/2014/04/nix4neteng-1-managing-dotfiles-pwn-the-unspoken-pain-of-unix-administration/">post on dotfiles</a>? This is something that can go right into your .bashrc and allows for the quick and easy translation of decimal to hexidecimal, which is very useful for IPv6 dual stacking because [in my opinion] the appropriate addressing scheme is to match the last octet based on hex and not numerically. So, to do that one needs to be able to easily convert the last octet quickly and easily.  Adding this to your .bashrc will accomplish this:
<pre>alias hex='printf "%x\n"'</pre>
Now, if you have an address of 10.143.27.199, you take the .199 you can utilize the shell alias to convert it to the hex equivalent.  For example:
If you're using static addresses or dhcpv6 with static addressing, you can match the last octet properly.
<pre>(~) desktop $ hex 199
c7</pre>
If you're using static addresses or dhcpv6 with static addressing, you can match the last octet properly.
<pre>10.143.27.199/27
2001:DB8:1b::c7/120
</pre>
There are more than this, but these are the tools I use almost daily.
I generally use <a href="http://www.routemeister.net/projects/sipcalc/" target="_blank" rel="noopener noreferrer">sipcalc</a> at this point since it does what I used to use <a href="http://jodies.de/ipcalc" target="_blank" rel="noopener noreferrer">ipcalc</a> for and more.  For gathering and verifying information, this is a fantastic tool.
<pre>(~) desktop $ sipcalc 2001:DB8:1b::c7/120
-[ipv6 : 2001:DB8:1b::c7/120] - 0</pre>
<pre>[IPV6 INFO]
Expanded Address - 2001:0db8:001b:0000:0000:0000:0000:00c7
Compressed address - 2001:db8:1b::c7
Subnet prefix (masked) - 2001:db8:1b:0:0:0:0:0/120
Address ID (masked) - 0:0:0:0:0:0:0:c7/120
Prefix address - ffff:ffff:ffff:ffff:ffff:ffff:ffff:ff00
Prefix length - 120
Address type - Aggregatable Global Unicast Addresses
Network range - 2001:0db8:001b:0000:0000:0000:0000:0000 -
 2001:0db8:001b:0000:0000:0000:0000:00ff -</pre>
And for IPv4:
<pre>(~) desktop $ sipcalc 10.143.27.199/27
-[ipv4 : 10.143.27.199/27] - 0</pre>
<pre>[CIDR]
Host address - 10.143.27.199
Host address (decimal) - 177150919
Host address (hex) - A8F1BC7
Network address - 10.143.27.192
Network mask - 255.255.255.224
Network mask (bits) - 27
Network mask (hex) - FFFFFFE0
Broadcast address - 10.143.27.223
Cisco wildcard - 0.0.0.31
Addresses in network - 32
Network range - 10.143.27.192 - 10.143.27.223
Usable range - 10.143.27.193 - 10.143.27.222</pre>
&nbsp;
Notable mention:
Web tools are also useful and are becoming more prolific than the UNIX tools, but I will assume that you're probably already loged into a UNIX system like a jump box or bastion host anyway and the tools are faster and thinner in that environment. That said, here are some useful web tools:
<a href="http://jodies.de/ipcalc" target="_blank" rel="noopener noreferrer">ipcalc</a> has the web interface to their tool.
<a href="http://www.gestioip.net/cgi-bin/subnet_calculator.cgi" target="_blank" rel="noopener noreferrer">This site </a>has a v4 and v6 calculator that works well and looks a lot like the output of sipcalc.
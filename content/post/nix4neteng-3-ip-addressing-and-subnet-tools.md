---
title: 'NIX4NetEng 3: IP Addressing and Subnet Tools'
date: Sat, 26 Jul 2014 16:46:07 +0000
draft: false
tags: [How-To, IPv6, NIX4NetEng, UNIX]
---

IP addressing and subnetting is a common interview subject. I assert that memorizing these things is useful for learning the concepts but ultimately futile in that it is time consuming and inefficient use of engineering time when tools can be utilized to accomplish the same goals in less time with fewer errors. Honestly, I gave up doing this kind of work manually around 10 years ago and have never regretted it, and in actuality, I'd probably struggle to do it at this point because it's a repetitive process better suited by code. In the old days, subnetting IPv4 manually was a badge of honor (and one that I always hated), but I learned it because I needed to know it for cert tests and daily work. However, once I started doing IPv6 around 2001, it became clear that doing this kind of thing by hand was consuming more time than it needed to. Enter UNIX tools. HEX Hex isn't really a tool as much as it's a hack for your shell.  Remember the [post on dotfiles](http://www.forwardingplane.net/2014/04/nix4neteng-1-managing-dotfiles-pwn-the-unspoken-pain-of-unix-administration/ "NIX4NetEng #1 Managing dotfiles; pwn the unspoken pain of UNIX administration")? This is something that can go right into your .bashrc and allows for the quick and easy translation of decimal to hexidecimal, which is very useful for IPv6 dual stacking because \[in my opinion\] the appropriate addressing scheme is to match the last octet based on hex and not numerically. So, to do that one needs to be able to easily convert the last octet quickly and easily.  Adding this to your .bashrc will accomplish this:```
alias hex='printf "%x\\n"'
```Now, if you have an address of 10.143.27.199, you take the .199 you can utilize the shell alias to convert it to the hex equivalent.  For example: If you're using static addresses or dhcpv6 with static addressing, you can match the last octet properly.```
(~) desktop $ hex 199
c7
```If you're using static addresses or dhcpv6 with static addressing, you can match the last octet properly.```
10.143.27.199/27
2001:DB8:1b::c7/120

```There are more than this, but these are the tools I use almost daily. I generally use [sipcalc](http://www.routemeister.net/projects/sipcalc/) at this point since it does what I used to use [ipcalc](http://jodies.de/ipcalc) for and more.  For gathering and verifying information, this is a fantastic tool.```
(~) desktop $ sipcalc 2001:DB8:1b::c7/120
-\[ipv6 : 2001:DB8:1b::c7/120\] - 0
``````
\[IPV6 INFO\]
Expanded Address - 2001:0db8:001b:0000:0000:0000:0000:00c7
Compressed address - 2001:db8:1b::c7
Subnet prefix (masked) - 2001:db8:1b:0:0:0:0:0/120
Address ID (masked) - 0:0:0:0:0:0:0:c7/120
Prefix address - ffff:ffff:ffff:ffff:ffff:ffff:ffff:ff00
Prefix length - 120
Address type - Aggregatable Global Unicast Addresses
Network range - 2001:0db8:001b:0000:0000:0000:0000:0000 -
 2001:0db8:001b:0000:0000:0000:0000:00ff -
```And for IPv4:```
(~) desktop $ sipcalc 10.143.27.199/27
-\[ipv4 : 10.143.27.199/27\] - 0
``````
\[CIDR\]
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
Usable range - 10.143.27.193 - 10.143.27.222
```  Notable mention: Web tools are also useful and are becoming more prolific than the UNIX tools, but I will assume that you're probably already loged into a UNIX system like a jump box or bastion host anyway and the tools are faster and thinner in that environment. That said, here are some useful web tools: [ipcalc](http://jodies.de/ipcalc) has the web interface to their tool. [This site](http://www.gestioip.net/cgi-bin/subnet_calculator.cgi) has a v4 and v6 calculator that works well and looks a lot like the output of sipcalc.

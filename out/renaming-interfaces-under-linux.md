---
title: 'Renaming interfaces under linux'
date: Tue, 28 May 2019 13:23:50 +0000
draft: false
---

There are many of us that learned Linux in the very early days, and with that history comes habits. One habit I have is to look for spec interface names. In particular, I prefer to have my interfaces named eth\* (with some notables exceptions here). Modern linux systems seem to have adopted the BSD methodology of naming the interfaces based on what it is - and while I did do a fair amount of work in BSD, I still prefer the eth naming scheme. [ZeroTier](https://www.zerotier.com/) has the inconsistency of using zt\* on some platforms and ztublkahlah on others. I am sure there is a reason, but I prefer consistency. Here are two ways to rename the interfaces. This is on a Debuntu system. Temporarily rename an interface:```
ifconfig ztukuxzo4f down
ip link set ztukuxzo4f name zt0
ifconfig zt0 up
```Rename an interface persistently:```
vi /etc/udev/rules.d/70-persistent-net.rules
```Append:```
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="96:3c:ee:c0:ff:ee", NAME="zt0"
```Reboot.
---
title: 'Basic IOS-XR command cheat sheet'
date: Wed, 20 Feb 2019 20:05:58 +0000
draft: false
---

Some basic commands that I have found useful in managing an ASR9K / IOS-XR device. This page is likely to grow and change over time.

Clear ARP

```
clear arp-cache <interface> <IPv4 addr> location all 
```

BGP

```
show bgp all unicast summary 
```

BGP Routes

```
  
show bgp ipv\[4/6\] unicast neighbors <neighbor> received route  
show bgp ipv\[4/6\] unicast advertised neighbor <neighbor>   
show bgp ipv\[4/6\] unicast summary  
show bgp ipv\[4/6\] unicast summary  
clear bgp ipv\[4/6\] unicast <neighbor> soft in  
show bgp all unicast summary  
show bgp ipv\[4/6\] unicast bestpath-compare
```

NetFlow

```
show flow exporter _<exporter>_ location 0/RSP0/CPU0 
```

Show all hardware linecards

```
show hw-module fpd location all
```
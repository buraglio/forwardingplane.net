---
title: 'Mikrotik Routed VLANs (non-CRS)'
date: Mon, 18 Feb 2019 17:57:21 +0000
draft: false
---

Add a simple set of VLANs to a CCR or other non-CRS RouterBoard.

```
/interface vlan   
add interface=sfpplus1 name=sfpplus1.4 vlan-id=4 comment="VLAN ID 4"  
add interface=sfpplus1 name=sfpplus1.5 vlan-id=5 comment="VLAN ID 5"  
add interface=sfpplus1 name=sfpplus1.6 vlan-id=6 comment="VLAN ID 6"  
add interface=sfpplus1 name=sfpplus1.7 vlan-id=7 comment="VLAN ID 7"  
add interface=sfpplus1 name=sfpplus1.8 vlan-id=8 comment="VLAN ID 8"  
add interface=sfpplus1 name=sfpplus1.9 vlan-id=9 comment="VLAN ID 9"
```

Add IP addressing to each VLAN

```
/ipv6 address   
add address=2001:db8:c33e:f0::1/64 advertise=no  
add address=2001:db8:c:f4::1/64 advertise=yes interface=sfpplus1.4   
add address=2001:db8:c:f5::1/64 advertise=yes interface=sfpplus1.5 add address=2001:db8:c:f6::1/64 advertise=yes interface=sfpplus1.6   
add address=2001:db8:c:f7::1/64 advertise=yes interface=sfpplus1.7   
add address=2001:db8:c:f8::1/64 advertise=yes interface=sfpplus1.8   
add address=2001:db8:c:f9::1/64 advertise=yes interface=sfpplus1.9 
```

Add legacy IPv4 addressing for each VLAN

```
/ip address  
add address=10.2.200.1/26 interface=sfpplus1 comment="Native VLAN"  
add address=10.2.4.1/25 interface=sfpplus1.4   
add address=10.2.5.1/25 interface=sfpplus1.5    
add address=10.2.6.1/25 interface=sfpplus1.6    
add address=10.2.7.1/25 interface=sfpplus1.7   
add address=10.2.8.1/25 interface=sfpplus1.8   
add address=10.2.9.1/25 interface=sfpplus1.9 
```
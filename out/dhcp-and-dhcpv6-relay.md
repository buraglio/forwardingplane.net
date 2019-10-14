---
title: 'ISC dhcp and dhcpv6 relay'
date: Sat, 16 Mar 2019 16:00:52 +0000
draft: false
---

When deploying dual stack, dhcpv6 is a crucial piece of the puzzle.  I personally prefer to run the dhcp process on a linux system and relay it for both v4 and v6. 

Assuming you are installing isc-dhcpd, the following configurations can be used to delegate host addresses for both IPv4 and IPv6

```
#  
\# Sample configuration file for ISC dhcpd for Debian / Ubuntu  
\# Examples provided without support by buraglio@forwardingplane.net  
\# Use at your own risk  
\# https://www.forwardingplane.net  
#  
\# Attention: If /etc/ltsp/dhcpd.conf exists, that will be used as  
\# configuration file instead of this file.  
#  
#  
  
\# The ddns-updates-style parameter controls whether or not the server will  
\# attempt to do a DNS update when a lease is confirmed. We default to the  
\# behavior of the version 2 packages ('none', since DHCP v2 didn't  
\# have support for DDNS.)  
ddns-update-style none;  
  
  
default-lease-time 259200;  
max-lease-time 345600;  
  
\# If this DHCP server is the official DHCP server for the local  
\# network, the authoritative directive should be uncommented.  
authoritative;  
  
\# Use this to send dhcp log messages to a different log file (you also  
\# have to hack syslog.conf to complete the redirection).  
log-facility local7;  
  
\# No service will be given on this subnet, but declaring it helps the   
\# DHCP server to understand the network topology. Errors will occur if not set,   
\# but functionality will remain intact  
  
#subnet 10.152.187.0 netmask 255.255.255.0 {  
#}  
  
\# Primary LAN Scope  
  
subnet 10.254.209.0 netmask 255.255.255.192 {  
range 10.254.209.30 10.254.209.57;  
option routers 10.254.209.1;  
#option domain-name-servers resolver.anycast.my-isp.net, resolver2.dc1.my-isp.net;  
option domain-name-servers resolver.anycast.my-isp.net;  
#option domain-name-servers 10.254.209.14;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# LAN scope 1  
subnet 10.254.3.0 netmask 255.255.255.224 {  
range 10.254.3.10 10.254.3.25;  
option routers 10.254.3.1;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# POP scope 1  
subnet 10.254.5.0 netmask 255.255.255.224 {  
range 10.254.5.10 10.254.5.25;  
option routers 10.254.5.1;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# POP Scope 2  
subnet 10.254.6.0 netmask 255.255.255.224 {  
range 10.254.6.5 10.254.6.27;  
option routers 10.254.6.1;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# POP Scope 3  
subnet 10.254.7.0 netmask 255.255.255.224 {  
range 10.254.7.10 10.254.7.25;  
option routers 10.254.7.1;  
#option domain-name-servers resolver1.opendns.com, resolver1.ipv6-sandbox.opendns.com;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# POP Scope 4  
subnet 10.254.4.0 netmask 255.255.255.224 {  
range 10.254.4.10 10.254.4.25;  
option routers 10.254.4.1;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# POP Scope 5  
subnet 10.254.8.0 netmask 255.255.255.224 {  
range 10.254.8.3 10.254.8.30;  
option routers 10.254.8.1;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# POP Scope 6  
subnet 10.254.9.0 netmask 255.255.255.224 {  
range 10.254.9.10 10.254.9.25;  
option routers 10.254.9.1;  
option domain-name-servers resolver.anycast.my-isp.net;  
option domain-name "dhcp.my-isp.net";  
}  
  
\# Static IPv4 addresses  
  
host business-customer1 {  
hardware ethernet ff:ff:ff:f3:3d:9f;  
fixed-address 10.254.4.9;  
}  
  
host business-customer2 {  
hardware ethernet ff:ff:ff:f3:3d:90;  
fixed-address 10.254.4.11;  
}  
  
host business-customer3 {  
hardware ethernet ff:ff:ff:f3:3d:9a;  
fixed-address 10.254.209.5;  
}  
  
host wap1 {  
hardware ethernet ff:ff:ff:40:d6:b0;  
fixed-address 10.254.209.4;  
}  
  
host wap2 {  
hardware ethernet ff:ff:ff:46:76:DC;  
fixed-address 10.254.209.7;  
}  
  
host wap3 {  
hardware ethernet ff:ff:ff:1d:d1:6a;  
fixed-address 10.254.209.3;  
}  
  
  

```

For IPv6, this configuration will provide host addresses to any devices requesting them

```
  
#  
\# Sample configuration file for ISC dhcpd for Debian / Ubuntu  
\# Examples provided without support by buraglio@forwardingplane.net  
\# Use at your own risk  
\# https://www.forwardingplane.net  
#  
  
default-lease-time 600;  
max-lease-time 7200;   
log-facility local7;   
authoritative;  
  
  
\# Primary LAN IPv6 Scope  
  
option dhcp6.name-servers 2001:db8:f00d::e9::a;  
option dhcp6.domain-search "dhcp.my-isp.net";  
  
option dhcp6.info-refresh-time 21600;  
  
\# The subnet where the server is attached  
subnet6 2001:db8:f00d::e9::/64 {  
range6 2001:db8:f00d::e9:d::2 2001:db8:f00d::e9:d::ffff;  
}  
  
\# Other Nets  
  
\# Primary LAN Scope  
option dhcp6.name-servers 2001:db8:f00d::e9::a;  
option dhcp6.domain-search "dhcp.my-isp.net";  
option dhcp6.info-refresh-time 21600;  
  
subnet6 2001:db8:f00d::e0::/64 {  
range6 2001:db8:f00d::e0:d::2 2001:db8:f00d::e0:d::ffff;  
}  
  
\# Pop scope 4  
option dhcp6.name-servers 2001:db8:f00d::e9::a;  
option dhcp6.domain-search "dhcp.my-isp.net";  
option dhcp6.info-refresh-time 21600;  
  
subnet6 2001:db8:f00d::e4::/64 {  
range6 2001:db8:f00d::e4:d::2 2001:db8:f00d::e4:d::ffff;  
}  
  
\# Pop Scope 5  
  
option dhcp6.name-servers 2001:db8:f00d::e9::a;  
option dhcp6.domain-search "dhcp.my-isp.net";  
option dhcp6.info-refresh-time 21600;  
subnet6 2001:db8:f00d::e8::/64 {  
range6 2001:db8:f00d::e8:d::2 2001:db8:f00d::e8:d::ffff;  
}  
  
\# Pop Scope 2  
option dhcp6.name-servers 2001:db8:f00d::e9::a;  
option dhcp6.domain-search "dhcp.my-isp.net";  
option dhcp6.info-refresh-time 21600;  
subnet6 2001:db8:f00d::e6::/64 {  
range6 2001:db8:f00d::e6:d::2 2001:db8:f00d::e6:d::ffff;  
}  
  
\# Pop scope 3  
option dhcp6.name-servers 2001:db8:f00d::e9::a;  
option dhcp6.domain-search "dhcp.my-isp.net";  
option dhcp6.info-refresh-time 21600;  
subnet6 2001:db8:f00d::e7::/64 {  
range6 2001:db8:f00d::e7:d::2 2001:db8:f00d::e7:d::ffff;  
}  
  
\# Fixed host section  
  
\# this needs fixed  
#host host1 {  
\# #host-identifier option dhcp6.client-id "\\000\\000\\000\\000\\000\\001\\000\\001 ;\\232\\351h\[5\\204\\270\\024";  
\# host-identifier option dhcp6.client-id "00010001 203b9ae9 685b3584 b814";  
\# fixed-address6 2001:db8:f00d::e0:0:d::9;  
\# }  
  
#}
```

\# For most ISPs, you'll want to delegate prefixes. ARIN recommends a /48 but in most cases the de facto standard is a /59 or /56. These are significantly more sane # # prefixes. A single /64 is not sufficient, and basic IPv6 connectivity should \*never\* be a revenue generating option.

```
\# dhcpv6-pd - this needs to match the ipv6 scope of the interface, given here as a poor example that needs adjusted  
\# delegate /56's from this /40 block (65K /56's, a /56 is 256 /64's)  
prefix6 2001:db8:f00d::  2001:db8:ff00:: /56;  
}
```

This linux configuration can be leveraged by any modern router, below is the Mikrotik configuration.

For IPv6, please note that the managed flag must be set for relay, and that you may not want to set that flag for all interfaces depending on your environment

```
/ipv6 dhcp-relay  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.4 name=vlan4-dhcpv6  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1 name=vlan0-dhcpv6  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.6 name=vlan6-dhcpv6  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.5 name=vlan5-dhcpv6  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.7 name=vlan7-dhcpv6  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.9 name=vlan9-dhcpv6  
add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.8 name=vlan8-dhcpv6  
  
/ipv6 nd  
set \[ find default=yes \] managed-address-configuration=yes
```

For IPv4:

```
/ip dhcp-relay  
add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.9 local-address=10.254.9.1 name=dhcp-vlan9  
add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.8 local-address=10.254.8.1 name=dhcp-vlan8  
add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.6 local-address=10.254.6.1 name=dhcp-vlan6  
add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.4 local-address=10.254.4.1 name=dhcp-vlan4  
add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.7 local-address=10.254.7.1 name=dhcp-vlan7  
add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1 local-address=10.254.209.1 name=dhcp-vlan209
```
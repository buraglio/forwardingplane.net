---
title: 'Enabling LLDP'
date: Thu, 07 Mar 2019 02:00:11 +0000
draft: false
---

Enabling LLDP can aid in understanding network and system topologies, I am very much in favor of running it and largely dismiss the perceived security issues surrounding it, when done correctly and with full knowledge of what it is being enabled.

Enable LLDP on a SROS based Nokia (formerly Alcatel-Lucent). It is per physical port, so replace 1/1/1 with your physical port and replicate on every port you want it to run on

```
/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system   
/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-cap sys-desc   
/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge admin-status tx-rx 
```

Enable LLDP on a Juniper is by interface or global

```
set protocols lldp advertisement-interval 30   
set protocols lldp interface all   

```

Mikrotik switch to LLDP as the discovery protocol in 6.something. MNDP/LLDP is on by default but can be changed by configuring the discover-interface-list

```
/ip neighbor discover-interface-list
```

Brocade VDX. This is a little dated but I suspect it's still correct.

```
conf t   
protocol lldp   
 hello 180   
 advertise dcbx-tlv   
 advertise optional-tlv management-address   
 advertise optional-tlv port-description   
 advertise optional-tlv system-capabilities   
 advertise optional-tlv system-description   
 advertise optional-tlv system-name   
 system-name dnoc960-sw1-mgmt   
 system-description Brocade VDX switch   
exit  
copy running-config startup-config 
```

Ubuntu / Debian Linux

```
apt install lldpd  
service lldpd start
```
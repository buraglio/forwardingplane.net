---
title: 'Comcast Business IPv6 Prefix Delegation'
date: Mon, 18 Feb 2019 18:58:29 +0000
draft: false
---

Comcast Business class service has some quirks when using the Cisco branded business gateway. Essentially, the prefix delegation will not work without very specific configuration options on the client. In order to run your own network border (i.e. not using their device as the first hop router for your LAN(s)), the following is required. In addition, with static IP addresses also comes with a static IPv6 prefix delegation.

For Ubiquity EdgeOS (or a derivative like a Unifi USG) the following needs to be set (eth2 is the port facing the comcast router)

```
set interfaces ethernet eth2 dhcpv6-pd prefix-only   
set interfaces ethernet eth2 dhcpv6-pd rapid-commit disable 
```

Mikrotik RouterOS

```
/ipv6 dhcp-client  
add add-default-route=yes comment="Native Comcast IPv6 External" interface=ether2 pool-name=comcast-ipv6 pool-prefix-length=59 request=prefix use-peer-dns=no
```

Essentially, the trick is make sure you do the following:

disable rapid-commit

request a prefix-length of exactly 59

It won't work any other way. Requesting an address (as opposed to an address+prefix or a different prefix hint essentially breaks the request.
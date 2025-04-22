
---
title: Mikrotik route leaking between VRFs
date: 2025-04-21
author: Nick Buraglio
layout: page
categories:
    - configuration
tags:
    - routeros
    - mikrotik
---


Have you ever wanted to leak routes between two VRFs on a mikrotik? I did. And I wanted to do it with IPv4 and IPv6. Now, this mostly works, and there are a few ways to do it. the easiest is using interfaces and their corresponding IP assignments and VRFs, but I wanted to leak entire tables. This is doable as well, but it comes with some limits. This is broken for the main VRF as of 21-April-2025, which means that to do it, you'll need to move anything from @main into it;s own VRF. A bit of a pain, however, there is a valid use case here - moving things from @main and making @main your management plane isolates the management. Anyway, it is not for everyone, but here is how you do it for those brave enough to take it on.


```
/routing bgp vpn 

add export.redistribute=connected .route-targets=1:1 import.route-targets=1:2 label-allocation-policy=per-vrf name=bgp-mpls-vpn-1 \ route-distinguisher=1.2.3.4:1 vrf=vrf1 

add export.redistribute=connected .route-targets=1:2 import.route-targets=1:1 label-allocation-policy=per-vrf name=bgp-mpls-vpn-2 \ route-distinguisher=1.2.3.4:1 vrf=vrf2
```

Pretty simple, yeah? Now we just wait until they fix leaking with @main.
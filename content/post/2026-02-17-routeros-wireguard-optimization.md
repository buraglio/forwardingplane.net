---
title: Mikrotik wireguard optimization
date: 2026-02-17
author: Nick Buraglio
layout: post
categories:
    - wireguard
    - routeros
    - mikrotik
    - vpn
tags:
    - mikrotik
    - wireguard
    - vpn
---

Most modern mikrotik can handle reasonable wireguard performance, but it is a CPU based encryption model, so there are some tweaks that can be made to improve performance. The following can be used to optimize for better wireguard behavior. However, it should be noted that unlike the IPSec capabilities that are measured and reported on the Mikrotik product pages for each platform, wireguard limits are not published for any mikrotik platform. This can be translated into "you get what you get", essentially, and as stated, wireguard is all CPU based, so perfornmance and scale will be limited by CPU.

### Set the queuing for the WAN interface to `fq-codel` or `cake`

**FQ-CoDel** and **CAKE** are both modern queue management systems designed to reduce bufferbloat and ensure fair bandwidth distribution, but CAKE offers several enhancements:

 1. **Flow Hashing**

- **FQ-CoDel**: Uses a basic hash to assign packets to flows, which can lead to collisions under high flow counts. 

- **CAKE**: Uses an **8-way set-associative hash**, drastically reducing collisions and improving flow isolation. 

2. **Fairness**

- **FQ-CoDel**: Fairness is per-flow—clients with more connections get more bandwidth. 

- **CAKE**: Adds **per-host fairness** (via Cobalt), so a client with 10 connections doesn’t dominate one with 1. 

3. **Shaping & Overhead Handling**

- **FQ-CoDel**: Often paired with a separate shaper (e.g., HTB), increasing CPU use. 
   
- **CAKE**: Includes an **integrated shaper**, is more CPU-efficient, and supports **framing compensation** (e.g., for PPPoE, ATM). 

4. **MSS & MTU Awareness**

- **CAKE**: Tracks packet sizes in **bytes**, not packets, avoiding issues with large GSO/GRO packets. 
   
- **FQ-CoDel**: Uses packet count, which can misrepresent memory usage.

5. **Diffserv Support**

- **CAKE**: Built-in **DiffServ mode** for traffic class prioritization. 
   
- **FQ-CoDel**: No native Diffserv support.
- 
Using `cake`

```
/queue type
add kind=cake name=cake
/queue interface
set sfp-sfpplus1 queue=cake
```

Or, with `fq_codel`

```
/queue type
add kind=fq-codel name=fq-codel
/queue interface
set sfp-sfpplus1 queue=fq-codel
```

### Disable fasttrack for the wireguard interface

```
/ip firewall raw add action=notrack chain=prerouting in-interface=wg1   
```

Set the correct MTU and MSS in order to to account for encapsulation overhead. 
Clamp MSS on TCP traffic to prevent fragmentation.

```
/ip firewall mangle add protocol=tcp tcp-flags=syn action=change-mss new-mss=1400 chain=forward out-interface=wg1   
```

The **MTU** and **MSS** are related but distinct values:

- **MTU (Maximum Transmission Unit)** = 1420 bytes: This is the largest IP packet size the WireGuard interface can transmit, including all headers. 
- **MSS (Maximum Segment Size)** = 1400 bytes: This is the largest payload size for **TCP data** within that packet, excluding the TCP and IP headers. 

The difference accounts for the **40-byte overhead** of the TCP and IPv4 headers (20 bytes each). Explicitly: 

```
MSS = MTU - 40
1400 = 1420 - 40
```

Setting MSS to 1400 ensures that when TCP adds its 40-byte header, the total packet size (1440 bytes) stays safely below the effective path MTU, preventing fragmentation. However, since WireGuard itself adds ~80 bytes of encapsulation overhead, the outer packet must be smaller — therefor setting the WireGuard interface MTU to **1420**. 

This combination avoids fragmentation and packet drops, especially on paths with lower MTU or blocked ICMP (which breaks Path MTU Discovery).

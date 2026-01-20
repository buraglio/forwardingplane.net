---
title: Packet Buffer Sizing Resources
date: 2026-01-16T12:00:00-06:00
author: Nick Buraglio
excerpt: A curated collection of resources on router and switch packet buffer sizing, bufferbloat, and related research - largely derived from Jim Warner's UCSC buffer page.
description: "Comprehensive reference for router and switch packet buffer specifications by ASIC family. Buffer sizes for Memory sizes for Broadcom Memory sizes for Trident, Memory sizes for Memory sizes for Tomahawk, Memory sizes for Memory sizes for Memory sizes for Jericho, Memory sizes for Memory sizes for Memory sizes for Memory sizes for Memory sizes for Memory sizes for Memory sizes for Mellanox Spectrum, Memory sizes for Tofino, and more from Cisco, Arista, Juniper, Dell, and other vendors."
keywords:
  - packet buffer sizing
  - switch buffer specifications
  - network buffer memory
  - Broadcom Trident buffer
  - Broadcom Tomahawk buffer
  - Memory sizes for Memory sizes for Broadcom Memory sizes for Jericho buffer
  - Mellanox Spectrum buffer
  - bufferbloat
  - microburst handling
  - switch ASIC memory
  - datacenter switch buffers
  - deep buffer switch
  - shallow buffer switch
  - VoQ virtual output queuing
tags:
  - networking
  - switching
  - buffers
  - datacenter
  - ASIC
categories:
  - configuration-archive
  - reference
layout: page
---

This page is a curated archive of resources related to packet buffer sizing in network equipment. Much of this information is derived from [Jim Warner's packet buffer page](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/buffer.html) at UCSC, which notes that "information here is by rumor, innuendo and extrapolation." Manufacturers historically left buffer information out of their data sheets, though this situation has improved significantly.

## Background

Information here is by **rumor, innuendo and extrapolation**. Manufacturers used to leave info on packet buffers out of their data sheets. This situation is now much improved. Readers -- be sure to let your suppliers know that you want this info. There are some [summary thoughts](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/summary).

The _buffer size_ question discussed in 2012 on the [NANOG list](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/nanog-thread) is reproduced. [Buffer requirements](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/buffer-requirements) for long RTT networks is less well understood than you might hope. IETF tests for burst management are not as well developed as bandwidth tests. Packet pacing can improve buffer effectiveness by making TCP less bursty. [Cisco wrote a review](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/Buffering-WP_August_2017.pdf) of the buffer question in 2017. Geoff Huston wrote _Sizing the Buffer_, a review published as a blog entry in 2019.

Packet buffers and switch performance have shown steady improvement. The table below attempts to show this for ASICs with integrated packet buffers and why using crufty old stuff is at your peril.

**[Incast](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/incast.html)** is a buffer exhaustion phenomena that is one consequence of running out of packet memory.

**Shared memory** means that the hardware permits buffers to be used by any port that needs them. In a shared memory design it is not possible to let ALL the memory go to queued packets. There would be no room for new arrivals which would lead to head of line blocking. The other major option for a switch fabric is a **crossbar matrix**.

**Buffer queue depth monitoring** cannot be done directly with SNMP MIB-II polling of the current occupancy of the buffer. Even if a buffer depth SNMP poll object existed it would not possible to interrogate it on a time scale short enough to catch microbursts. A burst that would fill a 4 MByte buffer would completely drain in 3.2 mS at 10 Gb/s. You could hope for indirect evidence of buffer exhaustion by monitoring packet drops. Bursts too short to cause drops can nonetheless be long enough to affect performance. Direct queue monitoring can thus add valuable information.

Some switches have multiple switch ICs that each manage their own memory pool. Memory from one IC can be shared among the ports in that IC's group but cannot be loaned out to ports controlled by other switch chips. Here we are interested in queue resources that can be claimed by a single flow for burst absorption -- not the total RAM in the system.

[Tolly](https://tolly.com) occasionally reports on the ability of switches to sustain **microbursts** in his reports on data center switches. These measurements relate directly to output port buffering.

Max buffer queue depth requires that all packet memory can be put into a single queue. QoS schemes divide buffer resources among defined queues.

---

## Switch Buffer Specifications by ASIC Family

### Trident+ Shared Memory

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Accton 5652 | 48 SFP+ and 4 QSFP+ | 8Q | 9 MB | 5? MB |
| Juniper QFX3500 | 48 SFP+ and 4 QSFP+ | 8Q | 9 MB | 5 MB |
| Arista 7050S-64 | 48 SFP+ and 4 QSFP | 8Q | 9 MB/switch | 5 MB |
| Dell 8132F & 4032F | 24 SFP+ and 2 x QSFP+ | 8Q | 9 MB | |
| Dell 8164F & 4064F | 48 SFP+ and 4 x QSFP+ | 8Q | 9 MB | |
| Pica8 P-3922 | 48 SFP+ and 4 x QSFP+ | | 9 MB | |
| Pica8 P-3930 | 48 10GbaseT and 4 x QSFP+ | | 9 MB | |
| Penguin 4804x | 48 SFP+ and 4 x QSFP+ | | 9 MB | |
| Cisco Nexus 3064X | 48 SFP+ and 4 QSFP+ | 12Q | 9 MB | 5 MB |
| Supermicro SSE-X3348T | 48 10GTw-Pr and 4 QSFP+ | 8Q | 9 MB | |
| Supermicro SSE-X3348S | 48 SFP+ and 4 QSFP+ | 8Q | 9 MB | |
| IBM G8264 | 48 SFP+ and 4 QSFP+ | 8Q | 9 MB/switch | |
| Force10 S4810 | 48 SFP+ and 4 QSFP+ | 4Q | 9 MB | |
| Allied Telesis DC2552 | 48 SFP+ and 4 QSFP+ | 8Q | 9 MB | 5 MB |
| HP 5900AF-48XG-4QSFP+ | 48 SFP+ and 4 QSFP+ | | 9 MB | |
| Edgecore AS5600-52X | 48 SFP+ and 4 QSFP+ | | 9 MB | |
| Cisco Nexus 3048 | 48 1000-base-T and 4 SFP+ | 8Q | 9 MB | 5? MB |
| Brocade VDX 6740 | 48 SFP+ and 4 QSFP+ | | 24 MB | Dynamic up to 8 MB |
| Brocade VDX 6940 | 96 SFP+ and 12 QSFP+ | | 24 MB | Dynamic up to 8 MB |

### Trident II and II+

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Champion Trident2 | varies by model | | 12.2 MB | |
| Lenovo G8272 | 48 SFP+ and 6 QSFP+ | | 12.2 MB | |
| Arista 7050X | 32 QSFP+ | 8Q | 12 MB | Dynamic up to 8 MB |
| Arista 7250X | 64 QSFP+ | 8Q | 12 MB/ASIC, 48 MB total | Dynamic up to 8 MB |
| netberg Aurora 420 | 48 SFP+ and 6 QSFP+ | 8Q | 12 MB | Dynamic up to 8 MB |
| Arista 7300X 4/8/16 slot chassis | 16 slot: 512 QSFP | 8Q | 12 MB/ASIC | Dynamic up to 8 MB |
| Brocade 7750-26Q | 26 QSFP+ and slot | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Brocade 7750-48F | 48 SFP+ and 6 QSFP+ and expansion | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Brocade 7750-48C | 48 10GbaseT and 6 QSFP+ and expansion | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Quanta BMS T3048-LY8 | 48 SFP+ and 4 QSFP+ | 8Q | 12 MB | 8 MB |
| Pluribus E68 | 44 SFP+ and 6 QSFP+ | 8Q | 12 MB | |
| Cisco Nexus 3132Q | 32 QSFP+ or 31 QSFP+ and 4 SFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Cisco Nexus 3172PQ | 48 SFP+ and 6 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Dell-S4048-ON | 48 SFP+ and 6 QSFP+ | 8Q | 12 MB | Dynamic up to 8 MB |
| Dell S6000 | 32 QSFP+ | 8Q | 12 MB | Dynamic up to 8 MB |
| Juniper QFX5100-24Q | 24 QSFP+ + expansion slots | 8Q | 12 MB | Dynamic up to 8 MB |
| Juniper EX4600 | 24 SFP+ + 4 QSFP + expansion slots | 8Q | 12 MB | Dynamic up to 8 MB |
| HP 5930 | 32 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| HP Altoline 5712 | 48 SFP+ and 6 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| HP Altoline 6712 | 32 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Accton edgecore AS5712-54X | 48 SFP+ and 6 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Accton edgecore AS6712-32X | 32 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Supermicro SSE-X3648S | 48 SFP+ and 6 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Inventec D6232Q | 48 SFP+ and 6 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |
| Wedge - Facebook OCP | 16 QSFP+ | 8Q | 12.2 MB | Dynamic up to 8 MB |

### Trident II+

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Alpha Networks SNX-60x0-486x | 48 SFP+ and 4 QSFP28 100G and 2 QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |
| Artica 4806xp | 48 SFP+ and 6 QSFP 40G | 8Q | 16 MB | Dynamic up to 12 MB |
| Champion Trident2+ | Three switch configurations | 8Q | 16 MB | |
| Arista 7050X2 family | see table | 8Q | 16 MB | Dynamic up to 12 MB |
| Dell S4048T-ON | 48 10G-BASE-T and 6 x QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |
| Dell S6010-ON | 32 40-Gbps QSFP | 8Q | 16 MB | Dynamic up to 12 MB |
| Cisco Nexus 3132Q-V | 32 QSFP+ or 26 QSFP+ and 6 QSFP28 | 8Q | 16 MB | Dynamic up to 12 MB |
| Cisco Nexus 31108PC-V | 48 SFP+ and 6 QSFP28 | 8Q | 16 MB | Dynamic up to 12 MB |
| Cisco NCS5001 | 40 1/10-Gbps SFP+ and 4 QSFP28 100G | 8Q | 16 MB | Dynamic up to 12 MB |
| Cisco NCS5002 | 80 1/10-Gbps SFP+ and 4 QSFP28 100G | 8Q | 16 MB | Dynamic up to 12 MB |
| EdgeCore AS6812-32X | 32 40-Gbps QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |
| Accton edgecore AS5812-54X | 48 SFP+ and 6 QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |
| Huawei CE6855-48S6Q-HI | 48 SFP+ and 6 QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |
| Huawei CE6855-48T6Q-HI | 48 10G base-T and 6 QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |
| HPE Altoline 6921-54X | 48 SFP+ and 6 QSFP+ | 8Q | 16 MB?? | Dynamic up to 12 MB |
| Juniper QFX5110-48S | 48 SFP+ and 4 QSFP28 100G | 8Q | 16 MB | Dynamic up to 12 MB |
| Juniper QFX5110-32Q | 20 QSFP+ and 4 QSFP28 100G or 32 QSFP+ | 8Q | 16 MB | Dynamic up to 12 MB |

### Trident 3

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Arista 7050CX3-32S | 32 port 100G QSFP28 and 2 port 10 Gb/s | 8Q | 32 MB | 27 MB shared pool |
| Arista 7050SX3-48YC8 | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | 27 MB shared pool |
| Ragile RA-BS6510-48V8C | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | 27 MB shared pool |
| Celestica Seastone2 Trident3 X7 | 32 port 100G QSFP28 and 2 port 10 Gb/s | 8Q | 32 MB | 27 MB shared pool |
| Celestica Questone2 Trident3 X5 | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | 27 MB shared pool |
| Edgecore AS7326-56X BCM56873 | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| Edgecore AS7726-32X BCM56870 | 32 port 100 Gb/s | 8Q | 32 MB | |
| Edgecore AS5835-54X BCM56771 | 48 port 10G SFP+ and 6 port 100 Gb/s | 8Q | 32 MB | |
| Edgecore AS5835-54T BCM56771 | 48 port 10 GBase-T and 6 port 100 Gb/s | 8Q | 32 MB | |
| Edgecore AS4630-54PE BCM56371 | 48 X 1000BaseT and 4 X 25 Gb/s SFP28 and 2 x 100Gb/s QSFP28 | 8Q | 8 MB | |
| Arista 720XP family Trident X3 | 48 and 24 port, models with uplinks and PoE (varies) | | 8 MB | 6 MB |
| Delta/Agema AGV424 BCM56771 | 24 port 25 Gb/s SFP28 and 4 port 100 Gb/s | 8Q | 32 MB | |
| Extreme SLX9150 | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| Extreme SLX9250 | 32 port 100 Gb/s | 8Q | 32 MB | |
| Inventec D6356 | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| Inventec D6332 | 32 port 100G QSFP28 | 8Q | 32 MB | |
| FS.COM N5860-48SC | 48 port 10G SFP+ and 8 port 100 Gb/s | 8Q | 32 MB | |
| FS.COM N8560-48BC | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| Juniper QFX5120-48T | 48 port 10G Tw-Pr and 6 port 100 Gb/s | 8Q | 32 MB | 24 MB |
| QuantaMesh BMS T4048-IX8 | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| QuantaMesh BMS T7032-IX7 | 32 port 100G QSFP28 | 8Q | 32 MB | |
| Alpha SNC-60x0-488F | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| Lenovo ThinkSystem NE2580o | 48 port 25G SFP28 and 8 port 100 Gb/s | 8Q | 32 MB | |
| Huawei CE6857-48S6CQ-EI Trident3 X4 | 48 port 10 Gb/s SFP+ and 6 100 Gb/s QSFP28 | 8Q | 32 MB | |
| Huawei CE6865-48S8CQ-EI Trident3 X5 | 48 port 25 Gb/s SFP28 and 8 100 Gb/s QSFP28 | 8Q | 32 MB | |
| Dell S5212-ON | 12 port 25 Gb/s SFP28 and 3 100 Gb/s QSFP28 | 8Q | 32 MB | |
| Dell S5224-ON | 24 port 25 Gb/s SFP28 and 4 port 100G QSFP28 | 8Q | 32 MB | |
| Dell S5232-ON | 32 port 100 Gb/s QSFP28 | 8Q | 32 MB | |
| Dell S5248-ON | 48 port 25 Gb/s SFP28 and 4 100 G QSFP28 and 2 200 G QSFP | 8Q | 32 MB | |
| Dell S5296-ON | 96 x 25 Gb/s SFP28 and 8 x 100 G QSFP28 | 8Q | 32 MB | |
| Delta 9032v2 | 32 port 100 Gb/s QSFP28 | 8Q | 32 MB | |
| Cisco C3132C-Z | 32 port 100 Gb/s QSFP28 | 8Q | 32 MB | |
| Ruckus ICX 7850-32Q | 32 x QSFP28 100 Gb/s ports | | 32 MB | |
| Ruckus ICX7850-48FS | 48 x SFP+ 1/10 Gb/s and 8 x QSFP28 100 G ports | | 32 MB | |
| Ruckus ICX 7850-48F | 48 x SFP28 1/10/25 Gb/s and 8 x QSFP28 100 G | | 32 MB | |

### Trident 4

| Model | Port Type | Total Buffer |
| --- | --- | --- |
| Arista 7050PX4-32S | 32 x OSPF | 132 MB |
| Arista 7050DX4-32S | 32 x QSFP56-DD | 132 MB |
| Arista 7358X4 | 8 slot 16- and 4- port cards | 132 MB |
| Juniper QFX5130 | 32 x QSFP56-DD | 132 MB |
| Dell Z9432F-ON | 32 x QSFP56-DD | 132 MB |
| Aurora 830 BCM56880 | 32 x QSFP56-DD | 132 MB |
| ufiSpace S9300-32D BCM56880 | 32 x QSFP56-DD | 132 MB |
| Ragile RA-B6520-24DC8QC BCM56780 | 8 x QSFP56-DD 400G and 24 × QSFP56 200G | 82 MB |
| Ragile RA-B6520-48C8QC BCM56780 | 8 x QSFP56-DD 400G and 48 × DSFP56 100G | 82 MB |

### Nephos 8360 Taurus Family

| Model | Port Type | RX Queue | Total Buffer |
| --- | --- | --- | --- |
| Netberg Aurora 705 NP8367 | 32 port 100 Gb/s QSFP28 | 8Q | 28 MB |
| Netberg Aurora 740 NP8369 | 64 port 100 Gb/s QSFP28 | 8Q | 40 MB |
| CIG CS-6436-56P NP8366 | 48 port 25 Gb/s and 8 ports 100G QSFP28 | 8Q | 24 MB |
| Liteon-LS3048-SN1 NP8363 | 48 port 10G SFP+ and 6 port 100 Gb/s | 8Q | 20 MB |
| Liteon-LS4048-SN3 NP8365 | 48 port 25G SFP28 and 6 port 100 Gb/s | 8Q | 20 MB |
| Nephos-AS7116-54X NP8365 | 48 port 25G SFP28 and 6 port 100 Gb/s | 8Q | options: 20-50 MB |
| Ingrasys S9130-32X | 32 port 100G QSFP28 | 8Q | options: 20-50 MB |
| Ingrasys S9230-32X | 64 port 100G QSFP28 | 8Q | options: 20-50 MB |

### Broadcom Maverick

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Alpha Networks SNX-61A0-486T | 48 10G-base-T and 4 QSFP28 and 2 QSFP | 8Q | ?? MB | |
| Alpha Networks SNX-61A0-486F | 48 SFP+ and 4 QSFP28 and 2 QSFP | 8Q | ?? MB | |
| Dell S4148F-ON | 48 port SFP+ and 2 QSFP+ and 2 QSFP28 | 8Q | 12 MB | 8 MB |
| Dell S4148T-ON | 48 port 10BaseT and 2 QSFP+ and 2 QSFP28 | 8Q | 12 MB | 8 MB |
| Dell S4112F-ON and S4112T-ON | 12 port SFP28 and 3 QSFP28 | 8Q | 12 MB | 8 MB |
| QCT QuantaMesh T3048 LY7 | 48 port SFP+ and 4 QSFP28 | 8Q | 12 MB | 8 MB |

### Broadcom Tomahawk

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Penguin 3200C | 32 port QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Dell Z9100 | 32 port QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Dell S6100-ON | Depends on modules selected | 8Q | 16 MB | Est 3 MB per core |
| Dell S5148 | 48 port SFP28 25 Gb/s + 6 x 100G | 8Q | 16 MB | Est 3 MB per core |
| Cisco Nexus 3232C | 32 port QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Cisco NCS5011 | 32 QSFP28 100G | 8Q | 16 MB | Est 3 MB per core |
| Arista 7060CX-32 | 32 port QSFP28 100 Gb/s and 2 SFP+ | 8Q | 16 MB | Est 3 MB per core |
| Arista 7260CX-64 | 64 port QSFP28 100 Gb/s and 2 SFP+ | 8Q | 64 MB | Est 3 MB per core |
| Arista 7320X | 256 port QSFP28 100 Gb/s | 8Q | 64 MB | Est 3 MB per core |
| Juniper QFX5200-32C | 32 port QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Juniper QFX5200-64Q | 32 port QSFP28 OR 64 QSFP | 8Q | 16 MB | Est 3 MB per core |
| Aurora 620 with ONIE | 48 SFP28 25 Gb/s and 6 QSFP28 100 G | 8Q | 16 MB | Est 3 MB per core |
| Aurora 630 with ONIE | 48 SFP28 25 Gb/s and 16 QSFP28 100 G | 8Q | 16 MB | Est 3 MB per core |
| Aurora 720 with ONIE | 32 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Inventec D7032Q28B | 32 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Edgecore AS7710 and AS7712 | 32 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Edgecore OMP800 | 256 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Ragile RA-B6500-32H | 48 X 50 Gb/s and 8 x QSFP28 100 Gb/s | | 16 MB | Est 3 MB per core |
| HP 6960 | 32 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Quanta T7032-IX1 | 32 x QSFP28 100Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Quanta T4048-IX2 | 48 x SFP28 + 8 x QSFP28 | 8Q | 16 MB | Est 3 MB per core |
| Agema AG5648 | 6 QSFP28 100 Gb/s and 48 SFP28 25 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Supermicro SSE-C3632S | 32 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Agema AG9032 | 32 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Facebook OCP Backpack | 128 QSFP28 100 Gb/s | 8Q | 256 MB | Est 3 MB per core |

### Broadcom Tomahawk+

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| fs.com N8500-48B6C | 48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s | 8Q | 16 MB | |
| Juniper QFX5200-48Y | 48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s | 8Q | 22 MB | |
| Agema AG5648V1 | 48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s | 8Q | 16 MB | |
| Edgecore AS7312-54XS | 48 SFP28 and 6 QSFP28 | 8Q | 22 MB | Est 4.5 MB per core |
| Alpha Networks SNC-60x0-486F | 48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s | 8Q | 22 MB | |
| Arista 7060CX2-32S | 32 QSFP28 100 Gb/s AND 2 SFP+ | 8Q | 22 MB | Est 4.5 MB per core |
| Lenovo NE2572 & NE2572O | 48 SFP28 25 Gb/s AND 6 QSFP28 | 8Q | 22 MB | Est 4.5 MB per core |

### Broadcom Tomahawk-II

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Arista 7260QX-64 | 64 QSFP 40 Gb/s AND 2 SFP+ | 8Q | 16 MB | Est 3 MB per core |
| Arista 7260CX3-64 | 64 QSFP28 100Gb/s AND 2 SFP+ | 8Q | 42 MB | 10.5 MB per slice |
| Agema AG9064 | 64 QSFP28 100 Gb/s | 8Q | 16 MB | Est 3 MB per core |
| Edgecore AS7816-64X | 64 QSFP28 100 Gb/s | 8Q | 42 MB | Est 10.5 MB per slice |
| Cisco Nexus C3264C-E | 64 QSFP28 100 Gb/s AND 2 SFP+ | 8Q | 42 MB | Est 10.5 MB per slice |
| Juniper QFX5210-64C | 64 QSFP28 100 Gb/s AND 2 SFP+ | 8Q | 42 MB | Est 10.5 MB per slice |
| Dell Z9264f-ON | 64 QSFP28 100 Gb/s AND 2 SFP+ | 8Q | 42 MB | Est 10.5 MB per slice |
| FS.COM N8560-64 | 64 QSFP28 100 Gb/s AND 2 SFP+ | 8Q | 42 MB | Est 10.5 MB per slice |
| Ragile RA-B6910-64C | 64 QSFP28 100 Gb/s | 8Q | 42 MB | Est 10.5 MB per slice |

### Broadcom Tomahawk 3

| Model | Port Type | Total Buffer |
| --- | --- | --- |
| Edgecore AS7900-32X & AS9716-32D | 32 x QSFP-DD 400 Gb/s ports | 64 MB |
| Arista 7060PX4-32 | 32 x OSFP 400 Gb/s ports and 2 x SFP+ | 64 MB |
| Arista 7060DX4-32 | 32 x QSFP-DD 400 Gb/s ports and 2 x SFP+ | 64 MB |
| Facebook Minipack | 8-slot chassis: 4x400 Gbps and 16x100 Gbps cards | 64 MB |
| Arista 7368X4 | 8-slot chassis: 4x400 Gbps and 16x100 Gbps cards | 64 MB |
| QuantaMesh BMS 9032-IX9 | 32 x QSFP-DD 400 Gb/s ports | 64 MB |
| Delta AGC032 | 32 x QSFP-DD 400 Gb/s ports and 2 x SFP+ | 64 MB |
| Dell Z9332F-ON | 32 x QSFP-DD 400 Gb/s ports and 2 x SFP+ | 64 MB |
| Aurora 820 | 32 x QSFP-DD 400 Gb/s ports | 64 MB |
| Ragile RA-B6920-32QC2X | 32 x QSFP-DD 400 Gb/s ports and 2 x SFP+ | 64 MB |
| Ragile RA-B6920-4S | 4 slots, 32 x QSFP 100 Gb/s cards | 64 MB |

### Tomahawk-4

| Model | Port Type | Total Buffer | TX Buffer |
| --- | --- | --- | --- |
| Arista 7060X5 | 64 x QSFP-DD 400 Gb/s ports and 2 SFP+ | 113 MB | 113 MB |
| Arista 7388X5 | 8-slot chassis: 8- and 16-port cards | 113 MB | 113 MB |
| Ragile RA-B6930-64QC | 64 x QSFP-DD 400 Gb/s ports | 113 MB | |
| Ragile RA-B6930-128DC | 128 x QSFP 200 Gb/s ports | 113 MB | |

### Innovium Teralynx

| Model | Port Type | Total Buffer |
| --- | --- | --- |
| Aurora Netberg 615 | 48 x SFP28 25 Gb/s ports + 8 x QSFP28 100 Gb/s | 45 MB |
| Aurora Netberg 715 | 32 x QSFP28 100 Gb/s ports | 45 MB |
| Cisco Nexus 3408-S | 8-slot chassis w 4-port 400G and 16-port 100G cards | 70 MB |
| Cisco Nexus 3432D-S | 32 port QSFP-DD 400 Gb/s + 2 x SFP | 70 MB |

### Broadcom Jericho (StrataDNX DUNE family)

| Model | Port Type | Total Buffer | Notes |
| --- | --- | --- | --- |
| Cisco NCS 5508 | 288 QSFP28 100 Gb/s ports | 4 GB per ASIC | VoQ 10 mS per queue |
| Cisco Nexus N9K-X9636C-R | 36 x 100 Gb/s QSFP28 linecard | 4 GB per ASIC | VoQ |
| Cisco Nexus N9K-X9636Q-R | 36 x 40 Gb/s QSFP linecard | 4 GB per ASIC | VoQ |
| Arista 7500R Linecard 36CQ | 36 x QSFP28 100G | 24 GB | VoQ |
| Arista 7500R Linecard 36Q | 30 x 40G QSFP and 6 x 100G | 8 GB | VoQ |
| Arista 7500R Linecard 48S2CQ | 48 port sfp+ and 2 x 100G | 4 GB | VoQ |
| Arista 7280QR-C36 | 24 QSFP+ and 12 QSFP28 | 8 GB in 2 groups | VoQ |
| Arista 7280QR-C48 | 48 QSFP+ and 24 QSFP28 | 32 GB in 8 groups | VoQ |
| Brocade SLX-9850 | 36 QSFP28 per linecard | 4 or 6 GB per 6-port group | VoQ |

### Broadcom Qumran (StrataDNX DUNE family)

| Model | Port Type | RX Buffer | Notes |
| --- | --- | --- | --- |
| Arista 7020SR-24C2 | 24 x 10G SFP+ and 2 x QSFP28 | 3 GB | VoQ |
| Arista 7020SR-32C2 | 32 x 10G SFP+ and 2 x QSFP28 | 3 GB | VoQ |
| Arista 7020TR-48 | 48 x 1GBASE-T and 6 x SFP+ | 3 GB | VoQ |
| Arista 7280SR-48C6 | 48 x 10 G SFP+ and 6 x QSFP28 | 4 GB | VoQ |
| Arista 7280TR-48C6 | 48 x 10GBASE-T and 6 x QSFP28 | 4 GB | VoQ |
| Cisco NCS 5501 | six QSFP28 100 Gb/s ports and 48 x 10 Gb/s | 4 GB per ASIC | VoQ 10 mS per queue |
| Brocade SLX-9540 / Extreme SLX-9540 | 6 QSFP28 100/40 Gb/s and 48 10/1 Gb/s | 6 GB | VoQ |
| Extreme SLX-9640 | 12 QSFP28 100/40 Gb/s and 24 10/1 Gb/s | 6 GB | VoQ |
| Edge-Core AS5912-54X | 48 SFP+ and 6 QSFP28 Qumran-MX BCM88370 | 6 GB | VoQ |
| Edge-Core AS5916-54XKS | 48 SFP+ and 6 QSFP28 Qumran-MX BCM88375 | 8 GB | VoQ |
| Edge-Core AS5916-54XL | 48 SFP+ and 6 QSFP28 Qumran-MX BCM88370 | 8 GB | VoQ |
| HPE FlexFabric 5980 | 48 SFP+ and 6 QSFP28 | 4 GB | VoQ |
| Champion Qumran | 48 SFP+ and 6 QSFP28 | 4 GB | VoQ |
| Alpha STX-60x0-486F Qumran | 48 SFP+ and 6 QSFP28 | 4 GB | VoQ |
| Dell S4248-ON | 48 SFP+ and 6 QSFP28 | 4 GB | VoQ |
| Agema AGC7648A BCM88375 | 48 SFP+ and 6 QSFP28 | 4 GB | VoQ |

### Disaggregated Cell Site Gateways

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| ufiSpace S9500-22XST | 4 x 1G RJ-45, 8 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 | 2 GB QumranAX BCM88470 | VoQ |
| ufiSpace S9500-30XS | 20 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 | 3 GB QumranAX BCM88470 | VoQ |
| Delta AGCV208S | 4 x 1G RJ45/ 4 x 10G SFP+/ 8 x 25G SFP28/ 2 x 100G QSFP28 | 1 GB QumranAX BCM88470 | VoQ |
| Edgecore AS7316-26XB aka CSR320 | 16 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 | 3 GB QumranAX BCM88470 | VoQ |
| Edgecore AS7315-27X aka CSR310 | 20 x 10G SFP+, 4 x 25G SFP28, 3 x 100G QSFP28 | 3 GB QumranAX BCM88470 | VoQ |
| Edgecore AS7315-30X aka CSR300 | 4 x 1G RJ45, 16 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 | 3 GB QumranAX BCM88470 | VoQ |
| Edgecore AS5915-18X aka CSR200 | 4 x 1G RJ45, 8 x 1G SFP, 6 x 10G SFP+ | 2 GB QumranUX BCM88272 | VoQ |
| ufiSpace S9501-18SMT | 4 x 1G RJ45, 8 x 1G SFP, 6 x 10G SFP+ | 1 GB QumranUX BCM88272 | VoQ |
| ufiSpace S9501-28SMT | 4 x 1G RJ45, 16 x 2.5G SFP, 6 x 10G SFP+, 2 x 10G SFP+ MACsec | 1 GB QumranUX BCM88272 | VoQ |

### Broadcom Qumran-2C (StrataDNX DUNE family)

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| Agema AGCX422S | 22 x QSFP28 100G + 4 x QSFP-DD 400G + 4 x SFP28 10G/25G | | VoQ |
| Agema AGCVA48S | 48 x SFP28 + 4 x SFP+ 10G + 10 x QSFP28 100G | 4 GB | VoQ |
| UfiSpace S9600-32X | 32 x QSFP28 100G | 4 GB | VoQ |
| Edge-core AS7946-30XB | 22 x QSFP28 100G + 4 x QSFP-DD 400G + 4 x SFP28 10G/25G | 4 GB | VoQ |

### Broadcom Jericho+ (StrataDNX DUNE family)

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| Agema AGC5648 Jericho+ | 48 SFP28 and 6 QSFP28 | 8 GB per ASIC | VoQ |
| Cisco 3636C-R | 36 ea QSFP28 100 Gb/s | 4 GB per ASIC | VoQ |
| Cisco NCS-55A1-36H-S/SE | 36 ea QSFP28 100 Gb/s | 4 GB per ASIC | VoQ |
| Cisco NCS-55A1-24H-S/SE | 24 ea QSFP28 100 Gb/s | 4 GB per ASIC | VoQ |
| Arista 7280SR2A-48YC6 | 48 x 25 G SFP28 and 6 x QSFP28 | 8 GB | VoQ |
| Arista 7500R2-36CQ | 36 x QSFP28 100 Gb/s | 4 GB per ASIC | VoQ |

### Broadcom Jericho2 (16 nm StrataDNX DUNE family)

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| Edgecore AS7926-80X | 80 x QSFP28 100 Gb/s | 8 GB | VoQ |
| Edgecore AS9926 Sw Fabric | 24 x 400Gb/s QSFP-DD | ? | VoQ |
| Edgecore AS7926-40XKFB | 40 x QSFP28 100 Gb/s + 13 x QSFP-DD 400 Gb/s | 8 GB | VoQ |
| ufiSpace S9700-53DX | 40 x QSFP28 100 Gb/s ports + 13 x QSFP-DD 400 Gb/s fabric | 8 GB | VoQ |
| ufiSpace S9600-48X | 48 x QSFP28 100 Gb/s | 8 GB | VoQ |
| ufiSpace S9700-23D | 10 x 400 Gb/s QSFP-DD ports and 13 x 400 G QSFP-DD fabric | 8 GB | VoQ |

### Arista 7280xR3 (Jericho2 switches)

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| 7280CR3-32P4 | 32 ports QSFP28 100G + 4 ports OSFP 400G | 8 GB - 1 Jericho2 ASIC | VoQ |
| 7280CR3-32D4 | 32 ports QSFP28 100G + 4 ports QSFP-DD 400G | 8 GB - 1 Jericho2 ASIC | VoQ |
| 7280PR3-24 | 24 ports 400 Gb/s, OSFP 400 G | 16 GB - 2 Jericho2 ASICs | VoQ |
| 7280DR3-24 | 24 ports 400 Gb/s QSFP-DD 400 Gb/s | 16 GB - 2 Jericho2 ASICs | VoQ |
| 7280CR3-96 | 96 ports QSFP28 100 Gb/s | 16 GB - 2 Jericho2 ASICs | VoQ |
| Cisco NC57-24X400G-BA linecard | 24 ports 400 Gb/s QSFP-DD | 16 GB - 2 Jericho2 ASICs | VoQ |
| Cisco NC57-18D12TH-SB linecard | 18 x 400 Gb/s or 30 x 100/200 Gb/s QSFP-DD | 16 GB - 2 Jericho2 ASICs | VoQ |

### Broadcom Jericho2C+ (7 nm StrataDNX DUNE family)

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| ufiSpace S9710-76D | 36 x 400 Gb/s QSFP-DD ports and 40 x 400 G QSFP-DD fabric | 16 GB | VoQ |

### Cisco 8000 Silicon One

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| Cisco 8201 (Q100 ASIC) | 24 QSFP56-DD 400 Gb/s and 12 QSFP28 100 Gb/s | 8 GB | VoQ |
| Cisco 8202 (Q100 ASIC) | 12 QSFP56-DD 400 GbE and 60 QSFP28 100 Gb/s | 8 GB | VoQ |
| Cisco 8201-32FH (Q200 ASIC) | 32 QSFP56-DD 400 GbE | 8 GB | VoQ |

### Broadcom ARAD (StrataDNX DUNE family)

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| Arista 7280E-64 | 48 port SFP+ and 4 x QSFP | 9 GB | VoQ 125 MB per 10 gig port |
| Arista 7280E-68 | 48 port SFP+ and 2 x QSFP28 100 Gb/s | 9 GB | VoQ 125 MB per 10 gig port |
| Arista 7280E-72 | 48 port SFP+ and 2 x MXP | 9 GB | VoQ 125 MB per 10 gig port |
| Arista 7504E/7508E | 48 port sfp+ line card | 3 GB per each of 3 processors | VoQ |
| Arista 7504E Linecard 12CQ | 12 QSFP28 100G | 3 GB per each of 6 processors | VoQ |

### EZChip NP-5

| Model | Port Type | Buffer | Notes |
| --- | --- | --- | --- |
| PARPRO N5R-100 | 24 SFP+ and 4 QSFP+ | 12 GB | VoQ very large |
| NoviSwitch 2122 | 20 SFP+ and 2 QSFP28 | 1 GB | VoQ very large |
| NoviSwitch 2128 | 20 SFP+ and 4 SFP+ and 4 QSFP+ | 1 GB | VoQ very large |
| NoviSwitch 2150 | 48 SFP and 2 QSFP+ | 1 GB | VoQ very large |
| NoviSwitch 21100 | 96 10/100/1000Base-T and 4 QSFP+ | 1 GB | VoQ very large |

### Cavium

| Model | Port Type | TX Buffer |
| --- | --- | --- |
| edgecore AS7500-32X | 32 QSFP28 100 Gb/s | 24 MB |
| edgecore AS7512-54X | 6 QSFP28 100 Gb/s and 48 SFP28 | 24 MB |
| Wedge_100C | 32 QSFP28 100 Gb/s | 24 MB |
| Arista 7160 family | 32 QSFP28 100 Gb/s | 24 MB |
| Brocade SLX-9240 | 32 QSFP28 100 Gb/s | 24 MB |
| Brocade SLX-9140 | 6 QSFP28 100 Gb/s and 48 QSFP28 | 24 MB |
| Pegatron w/out model num | 6 QSFP28 100 Gb/s and 48 QSFP28 | 24 MB |

### Barefoot Tofino

| Model | Port Type | Total Buffer | TX Buffer |
| --- | --- | --- | --- |
| Wedge 100BF-32X | 32 x QSFP28 100G | 16 MB | 16 MB |
| Wedge 100BF-65X | 65 x QSFP28 100G | 16 MB | 16 MB |
| OSW 1800 | 48 x SFP28 25G and 6 x QSFP28 100G | 16 MB | 16 MB |
| InterfaceMasters Tahoe 2624 | 20 x SFP28 25G and 26 x QSFP28 100G | 22 MB | 20 MB |
| Netberg Aurora 610 Tofino BFN-T10-032D | 48 SFP28 25 Gb/s and 8 x QSFP28 100 Gb/s | 22 MB | 20 MB |
| Netberg Aurora 710 Tofino BFN-T10-032D | 32 x QSFP28 and 2x SFP+ | 22 MB | 20 MB |
| Netberg Aurora 750 Tofino BFN-T10-064Q | 64 x QSFP28 and 2x SFP+ | 22 MB | 22 MB |
| Arista 7170-64C | 64 x QSFP28 | 22 MB | 20 MB |
| Stordis BF2556XT-1T | 48 x SFP28 and 8 x QSFP28 | 22 MB | 20 MB |
| Stordis BF6064X-T | 65 QSFP28 100 Gb/s | 22 MB | 20 MB |
| APS Networks APS2172Q | 64 SFP28 1/10/25G and 8 QSFP28 100 Gb/s | 22 MB | 20 MB |
| APS Networks APS2140D | 32 SFP28 1/10/25G and 8 QSFP28 100 Gb/s | 22 MB | 20 MB |
| APS Networks APS6120Q | 16 QSFP28 100 Gb/s | 22 MB | 20 MB |
| Cisco Nexus C34180 | 48 x SFP28 and 6 x QSFP28 | 20 MB | 20 MB |
| Arista 7170-32C | 32 x QSFP28 | 22 MB | 20 MB |
| ufiSpace S9180-32X | 32 x QSFP28 + 2 x SFP+ | 22 MB | 20 MB |

### Intel Tofino2

| Model | Port Type | Total Buffer |
| --- | --- | --- |
| Edgecore 9516-32D aka DCS810 | 32 x QSFP56-DD | 64 MB |

### Mellanox Spectrum

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Mellanox SX1024 | 48 SFP+ and 12 QSFP+ | | 4.6 MB | 64 KB to 1 port |
| Mellanox SX1036 | 36 QSFP+ | | 4.6 MB | 128 KB to 1 port |
| Mellanox SN2700 SN2410 SN2100 | 32 QSFP28 100Gb/s | 8 | 16 MB | 12 MB to 1 port? |
| Mellanox MSN2010-CB2RC | 18 SFP28 25G and 4 QSFP28 100Gb/s | 8 | 16 MB | 12 MB to 1 port? |
| HPE SN2700M SN2410M SN2100iM | 32 QSFP28 100Gb/s | 8 | 16 MB | 12 MB to 1 port? |

### Mellanox Spectrum-2

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Mellanox SN3800 | 64 QSFP28 100Gb/s | 16 | 42 MB | 32 MB to 1 port? |
| Mellanox SN3700 and SN3700C | 32 QSFP56 200Gb/s or QSFP28 100Gb/s | 16 | 42 MB | 32 MB to 1 port? |
| Mellanox SN3510 | 8 QSFP-DD 400 Gb/s + 48 QSFP56 50Gb/s | 16 | 42 MB | 32 MB to 1 port? |
| Mellanox SN3420 | 12 QSFP28 100Gb/s + 48 SFP28 | 16 | 42 MB | 32 MB to 1 port? |

### Mellanox Spectrum-3

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Mellanox SN4700 | 32 port QSFP-DD 400Gb/s | 16 | 64 MB | 50 MB to 1 port? |
| Mellanox SN4600 | 64 port QSFP56 200Gb/s | 16 | 64 MB | 50 MB to 1 port? |
| Mellanox SN4600C | 64 port QSFP28 100Gb/s | 16 | 64 MB | 50 MB to 1 port? |
| Mellanox SN4800 | 8 slots: 4x400Gb/s, 8x200Gbs, 16x100Gb/s | 16 | 64 MB | 50 MB to 1 port? |

### Broadcom Helix

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Arista 7010T | 48 1000-base-T + 4 SFP+ | 8Q | 4 MB/switch | 4 MB |
| Brocade ICX 7150-24 | (24+2) 1000-base-T and 4 SFP+ | 8Q | 2 MB | 2 MB to 1 port |
| Brocade ICX 7250-24 | (24+2) 1000-base-T and 4 SFP+ | 8Q | 2 MB | 2 MB to 1 port |
| Brocade ICX 7650-48P | 48 x 1000bsseT and (2 x 40G or 4 x 10G front module) | 8Q | 5 MB | |
| Brocade ICX 7650-48ZP | 24 x 1000BaseT and 24 multiGig ports and (1 x 100G or 2 x 40G) | 8Q | 12 MB | |
| HPE Altoline 6900 | 48 1000-base-T and 4 SFP+ and 2 QSFP stacking ports | 8Q | 4 MB | |
| Dell S3048-ON | 48 1000-base-T and 4 SFP+ | 8Q | 4 MB | |
| Agema AG6248C | 48 1000-base-T PoE+ w 2 SFP+ | 8Q | 4 MB | |
| Edgecore 4610-30T Helix4 | 24 1000-base-T w 4 SFP+ and 2 QSFP stacking ports | 8Q | 4 MB | |
| Edgecore 4610-54T Helix4 | 48 1000-base-T w 4 SFP+ and 2 QSFP stacking ports | 8Q | 4 MB | |

### Centec

| Model | Port Type | Total Buffer |
| --- | --- | --- |
| Centec V580-20Q4Z and E580-20Q4Z | 20 x QSFP 40G and 4 x SFP+ and 4 x QSFP28 100G | 9 MB |
| Centec V580-48X2Q4Z and E580-48X2Q4Z | 48 x SFP+ 10G and 2 x QSFP+ 40G and 4 x QSFP28 100G | 9 MB |
| Centec V350-48T4X and E350-48T4X | 48 x 1000baeT and 4 x QSFP+ 40G and 4 x QSFP28 100G | 3 MB |
| Centec E330-52SX | 48 x SFP 1G and 4 x SFP+ 10G | 6 MB |

### Cisco UADP Catalyst

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Catalyst 3850, 3650 | ASIC support 24 GE ports AND 2 x 10GE | 8Q | 6 MB per ASIC | 4 MB per ASIC |
| Catalyst C3850-12XS | 12 SFP+ (6 ports per ASIC) | 8Q | 6 MB per ASIC | 4 MB per ASIC |
| Catalyst C9200-family | 24- and 48-port 1-Gb/s access switches + uplinks | 8Q | 6 MB | 4 MB |
| Catalyst C9300-24T | ASIC support 24 GE ports AND uplink module | 8Q | | ~5 MB |
| Catalyst C9300-48T | 48 GE ports AND uplink module | 8Q | | ~5 MB |
| Catalyst C9300-24UX | 24 100/1G/2.5G/5G/10G Tw-Pr ports AND uplink module | 8Q | | ~5 MB |
| Catalyst C9500-24Q | 24 QSFP 40 Gb/s | 8Q | | ~10 MB |
| Catalyst C9500-40X | 24 SFP+ ports AND uplink module | 8Q | | ~10 MB |
| Catalyst C9500-24Y4C [UADP 3.0] | 24 SFP28 ports AND 4 QSFP28 100G | 8Q | 36 MB per ASIC | est 23 MB |
| Catalyst C9500-32QC [UADP 3.0] | 16 x QSFP28 100G OR 32 QSFP 40G | 8Q | 36 MB per ASIC | est 23 MB |
| Catalyst C9500-32C [UADP 3.0] | 32 QSFP28 100G ports | 8Q | 36 MB per ASIC | est 23 MB |
| Catalyst C9500-48Y4C [UADP 3.0] | 48 SFP28 ports AND 4 QSFP28 100G | 8Q | 36 MB per ASIC | est 23 MB |
| Catalyst C9600R | 6-slot chassis w 3 ea UADP3.0 ASICs | 8Q | 36 MB per ASIC | est 23 MB |

### Cisco Nexus switches w ACI silicon

| Model | Port Type | Total Buffer | TX Buffer |
| --- | --- | --- | --- |
| Cisco Nexus 92160YC-X | 48 SFP28 and 6 QSFP28 | Single ASE3 20 MB | 10.2 MB |
| Cisco Nexus 9272Q | 2RU 72 x 40Gb/s QSFP+ | Single ASE2 30 MB | 5.1 MB |
| Cisco Nexus 92304QC | 2RU 56 x 40Gb/s QSFP+ and 8 QSFP28 | Single ASE2 30 MB | 5.1 MB |
| Cisco Nexus 9372TX | 48 10-Gbps Base-T and 6 QSFP+ | 12 MB NFE + 25 MB ALE | 21 MB max burst |
| Cisco Nexus 9396PX | 48 SFP+ and {12 QSFP+ or 4 CPAK 100G} | 12 MB NFE + 40 MB ALE | 21 MB max burst |
| Cisco Nexus 93180YC-EX | 48 SFP28 25 Gb/s and 6 QSFP28 | 2 slices x 20 MB | 17.6 MB |
| Cisco Nexus 93108TC-EX | 48 tw-pr 10 Gb/s and 6 QSFP28 | 2 slices x 20 MB | 17.6 MB |
| Cisco Nexus 93180YC-FX | 48 SFP28 25 Gb/s and 6 QSFP28 | 40 MB | ~35 MB |
| Cisco Nexus 93108TC-FX | 48 tw-pr 10 Gb/s and 6 QSFP28 | 40 MB | ~35 MB |
| Cisco Nexus 9364C | 64 ports QSFP28 100 Gb/s | 40 MB | 10 MB |
| Cisco Nexus 9332C | 32 ports QSFP28 100 Gb/s | 40 MB | 10 MB |
| Cisco N9K-9336C-FX2 | 36 ports QSFP28 100 Gb/s | 40 MB | 20 MB |
| Cisco N9K-93360YC-FX2 | 96 x 10/25 Gb/s SFP28 + 12 x 40/100 Gb/s QSFP28 | 40 MB | 20 MB |
| Cisco Nexus N9K-C9316D-GX | 16 QSFP-DD 400/100 Gb/s | 80 MB | 20 MB |
| Cisco Nexus N9K-C93600CD-GX | 28 SFP28 and 8 QSFP28-DD | 80 MB | 20 MB |
| Cisco Nexus 9364-GX2A | 64 QSFP-DD + 2 SFP+ | 120 MB | 30 MB per slice |
| Cisco Nexus 9332-GX2B | 32 QSFP-DD + 2 SFP+ | 120 MB | 60 MB per slice |

### Large Queue 1RU Switches

| Model | Port Type | RX Queue | Total Buffer | Notes |
| --- | --- | --- | --- | --- |
| Force10 S60 | 48 Gig-E + 4 SFP+ | 4Q | 1250 MB | enough |
| Arista 7048 | 48 Gig-E + 4 SFP+ | 8Q | 768 MB | GOBBS |
| Corsa DP2100 | 32 1/10 G SFP+ | 8Q | 6 GB | |
| Corsa DP2200 | 32 1/10 G SFP+ and 2 QSFP28 100G | 8Q | 6 GB | |
| Corsa DP2400 | 32 1/10 G SFP+ and 2 QSFP28 100G + stack | 8Q | 6 GB | |
| Corsa DP6430 | 24 SFP+ and 2 CFP/2 100G | 8Q | 20 GB | |
| Corsa DP6440 | 48 SFP+ and 4 CFP/2 100G | 8Q | 20 GB | |

### Virtual Output Port Queuing

| Model | Port Type | RX Queue | Buffer | Notes |
| --- | --- | --- | --- | --- |
| Brocade MLX | 2-port 100 Gb/s line card | 8Q | 3 GB | 256 MB/port-queue VoQ |
| Brocade MLX | 8-port 10 Gb/s line card | 8Q | 3 GB | 256 MB/port-queue VoQ |
| Brocade MLX | 24-port 1 Gb/s line card | 8Q | 1 GB | 64 MB/port-queue VoQ |
| Cisco Nexus 5010 | 26 SFP+ | 8 | 480 KB per port | VoQ |
| Cisco Nexus 5548P | 32 fixed SFP+ and 16-port expansion module | 8 | 640 KB per port | VoQ |
| Cisco Nexus 5672UP | 48 fixed SFP+ and 6 QSFP+ | 8 | 25 MB per 12-port 10G ASIC | VoQ |
| Cisco Nexus 6001 | 48 fixed SFP+ and 4 QSFP+ | 8 | 25 MB per 12-port 10G ASIC | VoQ |
| Cisco ASR-9000 | Chassis solution. 1-6 ports per ASIC | | ASICs have 0.5 to 3.3 GB/port | VoQ |
| Juniper QFX10002-36 | QSFP: 12 x 100 Gb/s OR 36 x 40 Gb/s | 8Q | 4 GB per ASIC | VoQ 100 mS per port |

### Nexus 7000/7700

| Model | Port Type | RX Queue | TX Queue | Buffer |
| --- | --- | --- | --- | --- |
| Cisco Nexus 7000 (M1 series) | 48-port Tw-Pr GE | 2q4t | 1p3q4t | 7.56 MB per port RX, 6.15 MB per port TX |
| Cisco Nexus 7000 (F3 Series) | 6-port 100GE CPAK | 4q | 4q | 72 MB shared, VoQ |
| Cisco Nexus 7000 (F2 series) | 48 SFP+ across 12 ASICs | 4q1t | 1p3q1t | 72 MB shared, VoQ |
| Cisco Nexus 7000 (F3 series) | 12 QSFP+ across 6 ASICs | 4q1t | 1p3q1t | 72 MB shared, VoQ |
| Cisco Nexus 7000 (M1 series) | 32-port 10GE shared 4-port groups SFP+ | 8q2t | 1p7q4t | 65 MB per group RX, 80 MB per group TX |
| Cisco Nexus 7000 (M1 series) | 8-port 10GE X2 | 8q2t | 1p7q4t | 92 MB RX, 80 MB TX |
| Cisco Nexus 7000 (M2 series) | 2-port 100GE CFP2 | 8q2t | 1p7q4t | 62.46 MB RX, 31.23 MB TX |
| Cisco Nexus 7000 (M2 series) | 24-port 10GE SFP+ | 8q2t | 1p7q4t | 5.21 MB RX, 5.21 MB TX |
| Cisco Nexus 7700 (F3 Series) | 12-port 100GE CPAK across 12 ASICs | 4q | 4q | 144 MB shared, VoQ |
| Cisco Nexus 7700 (F3 Series) | 24-port 40GE QSFP+ across 12 ASICs | 4q | 4q | 144 MB shared, VoQ |
| Cisco Nexus 7700 (F3 Series) | 48-port 10GE SFP+ across 6 ASICs | 4q | 4q | 144 MB shared, VoQ |

### Other Shared Memory Switches

| Model | Port Type | RX Queue | Total Buffer | TX Buffer |
| --- | --- | --- | --- | --- |
| Catalyst 3550-24 | 24 10/100-base-T + 2 x 1G GBIC | 8Q | 2 MB | 2 MB |
| Extreme X450-G2-48T-10G | 48 1000-base-T + 4 x 10G SFP+ | 8Q | 4 MB | |
| Extreme 620X-16 | 16 10-Gbps SFP+ | 8Q | 2 MB | 2 MB |
| Extreme 620X-10 | 10 10-Gbps SFP+ | 8Q | 2 MB | 2 MB |
| Brocade FCX624S | 24Gig-E and 4 SFP+ | 8Q | 2 MB | 1.04 MB to 1 port |
| Juniper Ex4300 | 48 or 24 Tw-pair, 20 SFP+ | 8Q | | undisclosed |
| Juniper Ex4500 / Ex4550 | 40 SFP+ plus 8 SFP+ | 8Q | 4 MB per ASIC | 230 KB |
| Brocade ICX6610-24 | 24Gig-E w 8 SFP+ | 8Q | 4 MB | 1 MB to 1 port |
| HP 3800 | 24Gig-E and 4 10Gb/s | 8Q | | 0.23 MB |
| HP 2920-24 | 24 tw-pr Gig-E and 4 optional 10Gb/s | 8Q | 11.25 MB | 6.75 MB shared TX |
| HP 2824 | 20 tw-pr Gig-E and 4 SFP | 4Q | 0.512 MB shared | 0.512 MB shared |
| HP A5800-24G | 24Gig-E and 4 10Gb/s | 8Q | 4 MB | 4 MB |
| HP E6600-24G-4XG | 24Gig-E w 2 10Gb/s | 8Q | 18 MB for GE | 18 MB |
| Arista 7124SX | 24 x SFP+ | 8Q | 2 MB/sw-chip | 1.238 + 0.02 MB |
| Arista 7148SX | 48 SFP+ | 8Q | 2 MB/sw-chip, 8 MB total | 1.238 + 0.02 MB |
| Arista DCS-7150S-24 | 24 SFP+ | 8Q | 7.5 MB | |
| Arista DSC-7150S-52 | 52 SFP+ | 8Q | 7.5 MB | |
| Arista DCS-7150S-64 | 48 SFP+ and 4 QSFP+ | 8Q | 7.5 MB | |
| Dell 8024 | 24 SFP+ | 2Q | 2 MB | |
| Dell 6248 | 48 Gig-E, 4 x SFP+ | 8Q | 0.75 MB | 98 KB per port |
| Dell 7024 | 24 Gig-E, 4 x SFP+ | 8Q | 4 MB | 4 MB |
| IBM BNT G8052 | 48 GE + 4 SFP+ | 8Q | 4 MB/switch | 4 MB |
| Nortel 5520-48T ver 1-3 | 48 GE + 4 SFP shared | 8Q | 786 KB per 12-port | 131 KB w 8 Queues |
| Nortel 5520-48T ver 4-5 | 48 GE + 4 SFP shared | 1-8Q | 786 KB per 12-port | 786 KB w 1 Queue |
| Catalyst 3750G-48TS, 2960G | 12 ASICs w/ 4 GE ports ea | 8Q | 576KB per ASIC | 384 KB per ASIC |
| Catalyst 2960S | Single ASIC: 48 +2 10Gb/s | 8Q | 2 MB | 2 MB |
| Catalyst 3750E, 3560E, 3750X & 3560X | ASIC support 24 GE ports or 2 x 10G | 2Q | 2750KB per ASIC | 2 MB per ASIC |
| Catalyst 2960-X | ASIC support 48 GE ports AND uplink and stack | 4Q | | 4 MB per ASIC |
| Catalyst 4948E | 48 GigE + 4 SFP+ | 4 | 17.5 MB | Max 16 MB to 1 port |
| Cisco Catalyst 4510R+E | Chassis w 8 interface slots -- 12 port SFP+ line card | 8 | 32 MB on Supervisor | Max 14 MB to 1 port |
| Cisco Catalyst WS-C4500X-32SFP+ | 1 RU w 32 SFP+ ports and module for 8 more | 8 | 32 MB | |
| Cisco Nexus 3548 and 3548X | 48 SFP+ | 4 | 18 MB | 5.8 MB |

### Huawei

| Model | Port Type | TX Buffer |
| --- | --- | --- |
| Huawei S6720-54C-EI-48S | 48 SFP+ and 2 QSFP and 4 QSFP expansion | 8 MB to 1 port |
| Huawei S6720-30C-EI-24S | 24 SFP+ and 2 QSFP and 4 QSFP expansion | 8 MB to 1 port |

---

## Relevant / Important Papers and Documents

### Vendor White Papers

- [Extreme Networks: Congestion Management and Buffering in Data Center Networks](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/Extreme-Buffer-WP.pdf)
- [Cisco Buffer Sizing White Paper (August 2017)](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/Buffering-WP_August_2017.pdf)
- [Juniper QFX Buffer Documentation](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/juniper-qfx-buf.pdf)
- [Cisco NCS 5500 Buffering Architecture](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/xrdocs_io_ncs5500_blogs_2018_05_07_ncs_5500_buffering_architecture.pdf)
- [Cisco Nexus 9300 Buffer Information](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/Nexus-9300-buffer.pdf)
- [Arista Microbursts, Jitter and Buffers](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/AristaMicrobursts.pdf)

### Research and Analysis

- [Ancient History of Buffer Sizing](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/buffer-requirements)
- [Buffer Summary Thoughts](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/summary)
- [Incast Problem](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/incast.html)
- [NANOG Thread on Buffer Sizing](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/Bufs/nanog-thread)

## External Resources

- [ESnet: Router/Switch Buffer Size Issues](https://fasterdata.es.net/network-tuning/router-switch-buffer-size-issues/)
- [Bufferbloat Wikipedia](https://en.wikipedia.org/wiki/Bufferbloat)
- [OPNsense: Fighting Bufferbloat with FQ_CoDel](https://docs.opnsense.org/manual/how-tos/shaper_bufferbloat.html)
- [Switch Comparison Table (isp-tech.ru)](https://isp-tech.ru/en/switch-asic/)

## Original Source

This page is based on content from [Jim Warner's packet buffer page](https://web.archive.org/web/20260106162119/https://people.ucsc.edu/~warner/buffer.html) at UCSC.

---
title: MikroTik RouterOS 7 Basics
date: 2026-05-06
author: Nick Buraglio
layout: page
---

# MikroTik RouterOS 7 Basics

A practical curriculum for network engineers learning MikroTik RouterOS 7, with emphasis on operational commands, platform differences between routing-focused CCR hardware and switch-chip CRS hardware, and cross-platform translation from JunOS, Nokia SR OS, and Arista EOS. Covers the critical role of switch ASICs in CRS platforms and when hardware offload applies.

---

## Table of Contents

1. [RouterOS 7 Fundamentals](#1-routeros-7-fundamentals)
2. [CLI Navigation & Usability](#2-cli-navigation--usability)
3. [Output Filtering & Export](#3-output-filtering--export)
4. [Interface Commands](#4-interface-commands)
5. [Switching — CCR vs CRS](#5-switching--ccr-vs-crs)
   - [CCR: Software Bridge](#51-ccr-software-bridge)
   - [CRS: Switch Chip and Hardware Offload](#52-crs-switch-chip-and-hardware-offload)
   - [VLAN Configuration by Platform](#53-vlan-configuration-by-platform)
6. [OSPF Commands](#6-ospf-commands)
7. [IS-IS — Not Supported](#7-is-is--not-supported)
8. [BGP Commands](#8-bgp-commands)
9. [MPLS Commands](#9-mpls-commands)
10. [IPv6 Commands](#10-ipv6-commands)
11. [Configuration Management](#11-configuration-management)
12. [Platform Details — CCR, CRS, and Switch Chips](#12-platform-details--ccr-crs-and-switch-chips)
13. [Cross-Platform Command Reference](#13-cross-platform-command-reference)
14. [Quick Reference Card](#14-quick-reference-card)

---

## 1. RouterOS 7 Fundamentals

### Architecture Overview

RouterOS is MikroTik's proprietary operating system, based on a customized Linux kernel. It runs on MikroTik's own RouterBOARD hardware and on x86 platforms (CHR — Cloud Hosted Router). All configuration is persistent by default: changes take effect immediately without a commit step, analogous to Cisco IOS rather than JunOS or Nokia SR OS.

The forwarding plane varies dramatically by hardware:

- **CCR (Cloud Core Router)**: CPU-based forwarding using the main processor or an onboard NPU. No dedicated switch chip. All L2 bridging and L3 forwarding runs in software. High throughput is achieved through multi-core CPU design and FastPath/hardware acceleration.
- **CRS (Cloud Router Switch)**: Contains a dedicated **switch ASIC** (typically Marvell Prestera) alongside a general-purpose CPU. The switch chip handles L2 forwarding at wire speed. The CPU handles routing, management, and features the chip cannot accelerate. Correct configuration is required to engage the switch chip — if the bridge configuration is incompatible with chip capabilities, RouterOS silently falls back to CPU forwarding.

```
CCR architecture:
┌──────────────────────────────────────────┐
│     Multi-core CPU (ARM / MIPS)          │
│  RouterOS kernel ── FastPath engine      │
│  All L2 + L3 forwarding in software      │
└──────────────────────────────────────────┘

CRS architecture:
┌──────────────────┐     ┌───────────────────────────┐
│  CPU (ARM)        │     │  Switch ASIC              │
│  RouterOS kernel  │◄───►│  Marvell Prestera         │
│  Routing, mgmt    │     │  L2 wire-speed forwarding │
│  Non-offloadable  │     │  VLAN, STP, ACL in HW     │
│  features         │     │  (when offload = active)  │
└──────────────────┘     └───────────────────────────┘
```

RouterOS 7 is a major version with significant changes from v6, including a rewritten BGP implementation, improved OSPF, new bridge VLAN filtering model, RPKI, WireGuard, container support, and a restructured routing subsystem. CLI paths changed between v6 and v7 — this guide covers **RouterOS 7 exclusively**.

### Management Interfaces

RouterOS is accessible through multiple interfaces:

| Interface | Notes |
|-----------|-------|
| SSH CLI | Primary; covered in this guide |
| Telnet | Legacy; disabled by default in v7 |
| Serial console | Out-of-band access |
| WinBox | Proprietary GUI client (Windows/Wine/WebAssembly) |
| WebFig | Web-based GUI |
| REST API | JSON-based HTTP/HTTPS API (v7+) |
| Netinstall | Recovery/reimaging tool |

### Prompt Structure

```
[admin@router] >           # root operational prompt
[admin@router] /ip> >      # navigated into /ip menu
[admin@router] /ip/address> # navigated into /ip/address
```

There is no separate operational vs. configuration mode. All menus contain both show (`print`) and configuration (`add`, `set`, `remove`) commands.

### Safe Mode — Closest to `commit confirmed`

RouterOS has no candidate configuration, but **safe mode** provides a timed auto-revert:

```
# Press Ctrl+X to enter safe mode (prompt shows <SAFE>)
[admin@router] <SAFE>>

# Any changes made while in safe mode are auto-reverted if:
# - The session drops (SSH disconnect, timeout)
# - You press Ctrl+X again without first confirming

# To confirm changes (make them permanent):
exit                         # normal exit confirms safe mode changes

# To explicitly revert without disconnecting:
/system/safe-mode/revert
```

Safe mode is the only built-in protection against locking yourself out of a remote session. Use it whenever making changes that could affect connectivity.

---

## 2. CLI Navigation & Usability

### Menu System

RouterOS uses a hierarchical menu system. Commands are typed as a path followed by a verb:

```
/ip address print            # absolute path from root
/routing bgp session print   # absolute path

# Navigate into a menu (like JunOS 'edit'):
/ip
/ip> address
/ip/address> print           # relative command within menu

# Go up one level:
/ip/address> ..
/ip>

# Go to root:
/ip/address> /
[admin@router] >
```

### Tab Completion & Help

```
/ip <Tab>                    # list all sub-menus under /ip
/routing bgp <Tab>           # list sub-menus under bgp
/interface print <Tab>       # show command options
?                            # context help (some versions/contexts)
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Complete command or list options |
| `Ctrl+A` | Move cursor to beginning of line |
| `Ctrl+E` | Move cursor to end of line |
| `Ctrl+U` | Clear entire line |
| `Ctrl+K` | Delete from cursor to end |
| `Ctrl+W` | Delete previous word |
| `Ctrl+R` | Reverse search history |
| `Ctrl+C` | Abort current command |
| `Ctrl+D` | Exit session (if line empty) |
| `Ctrl+X` | Toggle safe mode |
| `Ctrl+Z` | Return to root menu |
| Up/Down | Navigate command history |

### Abbreviations

RouterOS supports unambiguous prefix abbreviations:

```
/ip a pr                    # /ip address print
/ro b se pr                 # /routing bgp session print
/in pr                      # /interface print
/sy id pr                   # /system identity print
```

### Console Settings

```
/console print               # show terminal settings
/console set term-width=250  # wider output
/ip ssh set always-allow-password-login=yes
```

---

## 3. Output Filtering & Export

RouterOS does not use Unix-style pipes. Filtering is done with `where` clauses and `print` options. The `export` command generates reproducible configuration scripts.

### Print Variants

| Command | Description |
|---------|-------------|
| `print` | Standard list/table output |
| `print detail` | All fields, one item per block |
| `print terse` | Compact single-line per item |
| `print count-only` | Count matching items |
| `print from=<n>` | Show from item number N |
| `print follow` | Live-updating output (like `tail -f`) |
| `print follow-only` | Live-updating, new entries only |
| `print interval=<sec>` | Refresh output every N seconds |
| `print file=<name>` | Save output to file |

### Filtering with `where`

`where` is the equivalent of `| match` / `| include`. It supports the `~` regex operator.

```
/ip address print where interface=ether1
/ip route print where active=yes
/ip route print where dst-address~"10\."
/routing bgp session print where state=established
/interface print where running=yes
/log print where message~"BGP"
/interface bridge host print where on-interface=ether2
```

### Chaining Conditions

```
/ip route print where active=yes && dst-address~"192.168"
/interface print where running=yes && type=ether
/log print where message~"bgp" && time>"12:00:00"
```

### Value Operators

| Operator | Meaning |
|----------|---------|
| `=` | Equals |
| `!=` | Not equals |
| `~` | Regex match |
| `!~` | Regex does not match |
| `>` `<` | Greater/less than (numeric or time) |
| `&&` | Logical AND |
| `\|\|` | Logical OR |

### Export — The Most Important Output Tool

`export` generates a complete, re-importable script of the current configuration. It is the primary tool for config documentation, backup, and diff.

```
/export                              # export entire config
/export compact                      # minimal (no defaults) — most common
/export verbose                      # include all defaults
/export file=backup                  # save to router filesystem as backup.rsc
/ip address export                   # export only /ip/address section
/routing bgp export                  # export only BGP config
/export compact file=pre-maintenance # save named checkpoint before changes
```

Export output is valid RouterOS script — you can import it directly:

```
/import file=backup.rsc              # apply exported config
/import file=backup.rsc verbose=yes  # show what's being applied
```

### Log Viewing

```
/log print                           # all log entries
/log print where message~"BGP"       # filtered log
/log print follow                    # live log tail (Ctrl+C to stop)
/log print follow-only               # live log, new entries only
/log print where topics~"ospf"       # by log topic
```

---

## 4. Interface Commands

### Show Commands

```
/interface print                     # all interfaces, type, state
/interface print detail              # full per-interface detail
/interface print terse               # compact one-line output
/interface print where running=yes   # only up interfaces
/interface print where running=no    # only down interfaces
/interface ethernet print            # Ethernet-specific detail
/interface ethernet print detail     # MAC, speed, duplex, statistics
/interface monitor-traffic [numbers] # live traffic rate (like 'watch bps/pps')

# Specific interface types
/interface sfp-sfpplus print         # SFP+ interfaces
/interface bridge print              # bridges
/interface vlan print                # VLAN sub-interfaces
/interface bonding print             # 802.3ad LAG (bonding)

# Optical / SFP DOM
/interface ethernet print detail where name=sfp-sfpplus1
# (DOM info appears in detail output under sfp-rx-power, sfp-tx-power, sfp-temperature)

# Counters
/interface print stats               # packet/byte/error counters
/interface print stats-detail        # extended counters
```

### Monitor Traffic (Live)

```
/interface monitor-traffic ether1                # live bps and pps for one interface
/interface monitor-traffic ether1,ether2,ether3  # multiple interfaces
# Press Ctrl+C to stop
```

### Interface Status Fields

```
/interface print
Flags: D - dynamic, X - disabled, R - running, S - slave
 #    NAME                 TYPE   ACTUAL-MTU L2MTU  MAX-L2MTU MAC-ADDRESS
 0  R ether1               ether        1500  1598       ...  AA:BB:CC:DD:EE:01
 1  R sfp-sfpplus1         ether        1500  ...            AA:BB:CC:DD:EE:02
 2    ether2               ether        1500  ...            AA:BB:CC:DD:EE:03  # no R = down
```

### Interface Configuration Examples

```
# Set description and enable/disable
/interface set ether1 comment="To-Peer-Router"
/interface set ether1 disabled=no
/interface set ether1 disabled=yes

# Set MTU (for jumbo frames)
/interface set sfp-sfpplus1 mtu=9000

# Create a bonding (LAG)
/interface bonding add name=bond1 slaves=ether1,ether2 mode=802.3ad
/interface bonding set bond1 lacp-rate=1sec

# Create a loopback (RouterOS uses dummy or bridge for loopback)
/interface bridge add name=loopback
/ip address add address=10.0.0.1/32 interface=loopback
```

---

## 5. Switching — CCR vs CRS

This is the most platform-critical section of this guide. The switching behavior of RouterOS differs fundamentally between CCR and CRS hardware. Getting this wrong — particularly on CRS — means running wire-rate traffic through a CPU instead of through the dedicated switch ASIC, which can be the difference between a platform handling 200 Mbps or 20 Gbps.

### The Core Distinction

| Platform | L2 Switching | Switch Chip | Hardware Offload |
|---|---|---|---|
| **CCR** | Software (CPU) | None | N/A |
| **CRS** | Hardware (switch ASIC) + CPU fallback | Marvell Prestera | Must be explicitly enabled and verified |
| **RB (RouterBOARD)** | Software (CPU) | None on most models | N/A |

---

### 5.1 CCR: Software Bridge

CCR platforms have no dedicated switch chip. All bridging runs in the RouterOS kernel (Linux bridge or FastPath). For CCR deployments:

- **Do not expect wire-speed L2** — throughput is CPU-limited
- Use CCR for **routing**, not high-density L2 switching
- Bridge is useful for transit L2 segments or limited port aggregation
- FastPath/FastTrack acceleration applies to routed (not bridged) traffic in most cases

#### CCR Bridge Configuration

```
# Create a bridge
/interface bridge add name=bridge1 protocol-mode=rstp

# Add ports to bridge
/interface bridge port add bridge=bridge1 interface=ether2
/interface bridge port add bridge=bridge1 interface=ether3

# Set bridge IP (management or L3 gateway)
/ip address add address=10.1.0.1/24 interface=bridge1
```

#### CCR VLAN on Bridge (Software)

```
# Bridge with VLAN filtering enabled (software VLAN in CPU)
/interface bridge add name=bridge1 vlan-filtering=yes protocol-mode=rstp

/interface bridge port add bridge=bridge1 interface=ether2 pvid=10
/interface bridge port add bridge=bridge1 interface=ether3 pvid=20
/interface bridge port add bridge=bridge1 interface=sfp-sfpplus1 pvid=1

# Define VLAN membership
/interface bridge vlan add bridge=bridge1 vlan-ids=10 untagged=ether2 tagged=sfp-sfpplus1
/interface bridge vlan add bridge=bridge1 vlan-ids=20 untagged=ether3 tagged=sfp-sfpplus1

# L3 SVI on bridge VLAN
/interface vlan add name=vlan10 interface=bridge1 vlan-id=10
/ip address add address=10.10.0.1/24 interface=vlan10
```

---

### 5.2 CRS: Switch Chip and Hardware Offload

CRS platforms contain a Marvell Prestera switch ASIC alongside the RouterOS CPU. When properly configured, L2 forwarding (bridging, VLAN switching, STP, MAC learning) runs entirely in the switch chip at line rate. Routing and anything outside the chip's capabilities runs on the CPU.

#### Why Hardware Offload Matters

On a CRS3xx with 24×1G or 8×10G ports, the switch chip can forward at full line rate for all ports simultaneously. If hardware offload is not active, all that traffic routes through the CPU — which is typically an ARM core at ~1GHz capable of a few hundred Mbps total. The performance difference is an order of magnitude or more.

**Hardware offload is NOT automatic.** RouterOS enables it when the bridge configuration is compatible with what the switch chip supports. Incompatible configuration silently disables chip offload and falls back to CPU switching with no warning beyond the `hw=no` status flag.

#### Verifying Hardware Offload Status

```
# Check per-port offload status — this is the most important command on CRS
/interface bridge port print detail
# Look for "hw=yes" — this means the port IS offloaded to switch chip
# "hw=no" means CPU bridging — investigate why

# Check switch chip state directly
/interface ethernet switch print
/interface ethernet switch port print

# Show MAC table from switch chip (hardware MAC table)
/interface ethernet switch host print

# Show switch chip ACL rules (hardware TCAM)
/interface ethernet switch rule print
```

#### What Disables Hardware Offload

The following features are NOT supported by the Marvell Prestera switch chip and force CPU-based forwarding when enabled on a bridge:

- **Bridge firewall** (`/interface bridge filter`) — forces CPU
- **IGMP snooping** on some CRS models — may force CPU
- **DHCP snooping** — forces CPU
- **ARP proxy on bridge** — forces CPU
- **Bonding members** as bridge ports — forces CPU on some chip revisions
- **STP with some configurations** — depends on chip revision
- **Certain VLAN configurations** not natively supported by the chip

When in doubt: add ports one at a time, check `hw=yes` after each, and verify with traffic tests.

#### CRS Switch Chip-Native Configuration

For maximum hardware offload, configure VLANs directly at the switch chip level using `/interface ethernet switch`:

```
# Switch chip VLAN configuration (most hardware-native approach)
# Applicable to CRS3xx with Marvell Prestera 98DX3236 / 98DX3255

# Set port VLAN mode
/interface ethernet switch port
set ether1 vlan-mode=secure vlan-header=add-if-missing default-vlan-id=10
set ether2 vlan-mode=secure vlan-header=add-if-missing default-vlan-id=20
set sfp-sfpplus1 vlan-mode=secure vlan-header=leave-as-is default-vlan-id=1

# Define VLANs in switch chip VLAN table
/interface ethernet switch vlan
add switch=switch1 vlan-id=10 ports=ether1,sfp-sfpplus1
add switch=switch1 vlan-id=20 ports=ether2,sfp-sfpplus1
add switch=switch1 vlan-id=1 ports=sfp-sfpplus1,ether3,ether4
```

Note: For RouterOS 7, the **bridge + VLAN filtering approach** is preferred over direct switch chip configuration because it is more consistent across platforms and supports dual operation as both a bridge and a router. The switch chip approach is more direct but less portable.

#### CRS Bridge + Hardware Offload (Preferred for RouterOS 7)

```
# Create bridge with VLAN filtering
/interface bridge add \
    name=bridge1 \
    vlan-filtering=yes \
    protocol-mode=rstp

# Add ports to bridge with hw-offload=yes
/interface bridge port add bridge=bridge1 interface=ether1  pvid=10  hw-offload=yes
/interface bridge port add bridge=bridge1 interface=ether2  pvid=20  hw-offload=yes
/interface bridge port add bridge=bridge1 interface=ether3  pvid=30  hw-offload=yes
/interface bridge port add bridge=bridge1 interface=sfp-sfpplus1 pvid=1 hw-offload=yes

# Define VLAN membership
/interface bridge vlan add bridge=bridge1 vlan-ids=10 untagged=ether1  tagged=sfp-sfpplus1
/interface bridge vlan add bridge=bridge1 vlan-ids=20 untagged=ether2  tagged=sfp-sfpplus1
/interface bridge vlan add bridge=bridge1 vlan-ids=30 untagged=ether3  tagged=sfp-sfpplus1

# Verify offload (run after committing config)
/interface bridge port print detail where bridge=bridge1
# All ports should show hw=yes
```

#### CRS Switch Chip ACLs (Hardware TCAM)

CRS platforms expose the switch chip's ACL/TCAM via `/interface ethernet switch rule`. These rules are programmed directly into the switch ASIC and apply at full line rate. They are separate from and faster than RouterOS `/ip firewall filter` rules (which always run on CPU).

```
# Show current switch chip rules
/interface ethernet switch rule print

# Drop traffic from specific MAC
/interface ethernet switch rule add \
    switch=switch1 \
    src-mac-address=AA:BB:CC:DD:EE:FF/FF:FF:FF:FF:FF:FF \
    action=drop

# Allow only tagged VLAN 100 on port ether5
/interface ethernet switch rule add \
    switch=switch1 \
    ports=ether5 \
    vlan-id=100 \
    action=allow

# Mirror traffic from ether3 to ether8 (SPAN)
/interface ethernet switch rule add \
    switch=switch1 \
    ports=ether3 \
    action=mirror \
    mirror-ports=ether8

# View switch chip MAC table (hardware forwarding database)
/interface ethernet switch host print
```

> **TCAM scale**: The Marvell Prestera chips in CRS3xx have limited TCAM entries (typically 128–512 rules). Exceeding this causes additional rules to fall back to CPU evaluation. See [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/) for per-chip TCAM and buffer details.

---

### 5.3 VLAN Configuration by Platform

#### CCR — VLAN Sub-interfaces (Routed L3 Use Case)

On CCR, the most common VLAN use case is routing between VLANs. Use VLAN sub-interfaces directly on the physical port:

```
# Create VLAN sub-interfaces on a trunk port
/interface vlan add name=vlan100 interface=sfp-sfpplus1 vlan-id=100
/interface vlan add name=vlan200 interface=sfp-sfpplus1 vlan-id=200
/interface vlan add name=vlan300 interface=sfp-sfpplus1 vlan-id=300

# Assign IP addresses (router-on-a-stick or inter-VLAN routing)
/ip address add address=10.100.0.1/24 interface=vlan100
/ip address add address=10.200.0.1/24 interface=vlan200
/ip address add address=10.300.0.1/24 interface=vlan300
```

#### CCR — Bridge VLAN Filtering (L2 + L3 Combined)

```
/interface bridge add name=core-bridge vlan-filtering=yes protocol-mode=rstp

# Trunk ports
/interface bridge port add bridge=core-bridge interface=sfp-sfpplus1 pvid=1
/interface bridge port add bridge=core-bridge interface=sfp-sfpplus2 pvid=1

# Access ports
/interface bridge port add bridge=core-bridge interface=ether1 pvid=100
/interface bridge port add bridge=core-bridge interface=ether2 pvid=200

/interface bridge vlan add bridge=core-bridge vlan-ids=100 \
    untagged=ether1 tagged=sfp-sfpplus1,sfp-sfpplus2
/interface bridge vlan add bridge=core-bridge vlan-ids=200 \
    untagged=ether2 tagged=sfp-sfpplus1,sfp-sfpplus2

# L3 gateway on VLAN
/interface vlan add name=vlan100 interface=core-bridge vlan-id=100
/ip address add address=10.100.0.1/24 interface=vlan100
```

#### CRS — Full L2 Switch with L3 Management (Hardware-Offloaded)

```
# 1. Create bridge with VLAN filtering
/interface bridge add name=sw-bridge vlan-filtering=yes protocol-mode=none

# 2. Add all switch ports with hw-offload=yes
/interface bridge port
add bridge=sw-bridge interface=ether1  pvid=10  hw-offload=yes
add bridge=sw-bridge interface=ether2  pvid=10  hw-offload=yes
add bridge=sw-bridge interface=ether3  pvid=20  hw-offload=yes
add bridge=sw-bridge interface=ether4  pvid=20  hw-offload=yes
add bridge=sw-bridge interface=ether5  pvid=30  hw-offload=yes
add bridge=sw-bridge interface=ether6  pvid=30  hw-offload=yes
add bridge=sw-bridge interface=sfp-sfpplus1 pvid=1 hw-offload=yes   # uplink/trunk

# 3. Define VLANs
/interface bridge vlan
add bridge=sw-bridge vlan-ids=10 untagged=ether1,ether2 tagged=sfp-sfpplus1
add bridge=sw-bridge vlan-ids=20 untagged=ether3,ether4 tagged=sfp-sfpplus1
add bridge=sw-bridge vlan-ids=30 untagged=ether5,ether6 tagged=sfp-sfpplus1
add bridge=sw-bridge vlan-ids=1  tagged=sfp-sfpplus1               # management trunk

# 4. Management IP (VLAN 1 / untagged on trunk)
/interface vlan add name=mgmt-vlan interface=sw-bridge vlan-id=1
/ip address add address=192.0.2.1/24 interface=mgmt-vlan

# 5. Verify hardware offload is active
/interface bridge port print detail
# Confirm hw=yes on all ports — if any show hw=no, review bridge configuration
```

#### Spanning Tree on CRS

```
# RSTP is the recommended STP mode for CRS
/interface bridge set sw-bridge protocol-mode=rstp

# STP show commands
/interface bridge print detail                   # STP mode and state per bridge
/interface bridge port print                     # per-port STP state and role
/interface bridge port print detail where bridge=sw-bridge

# Port roles and states
/interface bridge monitor sw-bridge              # live STP state
```

#### MAC Address Table

```
# Show MAC table (bridge/software level)
/interface bridge host print
/interface bridge host print where bridge=sw-bridge
/interface bridge host print where on-interface=ether1

# Show MAC table from switch chip (hardware level — CRS only)
/interface ethernet switch host print            # hardware MAC table in chip
```

---

## 6. OSPF Commands

### Show Commands

```
# OSPF process and overview
/routing ospf instance print                     # OSPF instances
/routing ospf instance print detail

# Neighbors
/routing ospf neighbor print                     # all OSPF neighbors
/routing ospf neighbor print detail              # with state, timers, DR/BDR
/routing ospf neighbor print where state=full   # only full adjacencies
/routing ospf neighbor print where state!=full  # non-full (troubleshoot)

# Interfaces
/routing ospf interface-template print           # configured interface templates
/routing ospf interface print                    # active OSPF interfaces (operational)
/routing ospf interface print detail

# LSDB
/routing ospf lsa print                          # link-state database
/routing ospf lsa print detail                   # full LSA content
/routing ospf lsa print where type=router        # Router LSAs
/routing ospf lsa print where type=network       # Network LSAs
/routing ospf lsa print where type=as-external   # External (Type-5) LSAs
/routing ospf lsa print where area=0.0.0.0       # LSDB for specific area

# Routes
/ip route print where routing-mark="main" && active=yes
/ip route print where gateway-status~"ospf"
/ip route print detail where dst-address~"10\."
```

### Route Table Integration

```
/ip route print where active=yes                 # all active routes
/ip route print where routing-mark="main"        # default routing table
/ip route print detail                           # full route detail with metrics
```

### Configuration Examples

```
# Create OSPF instance
/routing ospf instance
add name=ospf-main version=2 router-id=10.0.0.1

# Create area
/routing ospf area
add name=backbone area-id=0.0.0.0 instance=ospf-main
add name=area1 area-id=0.0.0.1 instance=ospf-main type=stub

# Configure interfaces via templates
/routing ospf interface-template
add area=backbone interfaces=sfp-sfpplus1 type=ptp cost=10 \
    auth=md5 auth-key="secretkey" hello-interval=10s dead-interval=40s
add area=backbone interfaces=loopback passive

# Redistribute connected routes into OSPF
/routing ospf instance
set ospf-main redistribute=connected

# Reference bandwidth (for cost calculation at 100G)
/routing ospf instance set ospf-main reference-bandwidth=100000000000
```

### OSPFv3 (IPv6)

```
# Show OSPFv3
/routing ospf neighbor print where instance~"v3"
/routing ospf lsa print where instance~"v3"
/ipv6 route print where active=yes

# Configure OSPFv3
/routing ospf instance
add name=ospf3-main version=3 router-id=10.0.0.1

/routing ospf area
add name=backbone-v3 area-id=0.0.0.0 instance=ospf3-main

/routing ospf interface-template
add area=backbone-v3 interfaces=sfp-sfpplus1 type=ptp
```

---

## 7. IS-IS — Not Supported

**RouterOS does not implement IS-IS as a routing protocol.** This is a significant limitation compared to JunOS, Nokia SR OS, and Arista EOS, and means RouterOS is generally not deployed as a provider-edge or core router in IS-IS-based networks.

For network engineers coming from SP environments where IS-IS is standard, the functional replacement in RouterOS is:

| IS-IS Use Case | RouterOS Alternative |
|---|---|
| IGP for core/backbone | OSPF (v2 for IPv4, v3 for IPv6, or dual-stack) |
| SR-MPLS transport | Not supported in RouterOS |
| Multi-level hierarchy | OSPF areas |
| Traffic engineering | Not supported (no RSVP-TE) |
| Large-scale routing | BGP with OSPF as IGP underlay |

If IS-IS is a hard requirement, MikroTik hardware is not the appropriate platform. The CCR and CRS series are positioned for enterprise edge, ISP access aggregation, and SMB networking where OSPF is the dominant IGP.

---

## 8. BGP Commands

RouterOS 7 significantly rewrote the BGP subsystem. The old `/routing bgp peer` model from v6 is replaced with a connection/template model.

### Show Commands

```
# BGP session state (primary operational view)
/routing bgp session print                       # all sessions and state
/routing bgp session print detail                # full per-session detail
/routing bgp session print where established=yes # only up sessions
/routing bgp session print where established=no  # sessions that are down

# BGP connections (configuration view)
/routing bgp connection print
/routing bgp connection print detail

# Routing table — BGP routes
/ip route print where bgp=yes                    # all BGP routes in RIB
/ip route print where bgp=yes && active=yes      # active BGP routes only
/ip route print detail where dst-address~"10\."  # specific prefix range

# BGP advertisements (what we are sending)
/routing bgp advertisements print
/routing bgp advertisements print where peer~"10.0.0"

# BGP received routes (what peers sent us)
/ip route print where received-from~"10.0.0.2"

# BGP statistics
/routing bgp session print detail where name~"peer-name"
# (stats are embedded in detail output: prefixes-received, prefixes-sent, etc.)
```

### Configuration Examples

```
# Define BGP instance (AS and router-id)
/routing bgp template
add name=default as=65000 router-id=10.0.0.1

# iBGP peer
/routing bgp connection
add name=IBGP-R2 \
    remote.address=10.0.0.2 \
    remote.as=65000 \
    local.role=ibgp \
    local.address=10.0.0.1 \
    nexthop-choice=force-self \
    output.network=yes \
    input.filter=IBGP-IMPORT \
    output.filter=IBGP-EXPORT

# eBGP peer
/routing bgp connection
add name=EBGP-ISP \
    remote.address=192.0.2.2 \
    remote.as=65001 \
    local.role=ebgp \
    local.address=192.0.2.1 \
    input.filter=EBGP-IMPORT \
    output.filter=EBGP-EXPORT \
    authentication-key=secret

# Route reflector
/routing bgp connection
add name=RR-CLIENT \
    remote.address=10.0.0.5 \
    remote.as=65000 \
    local.role=ibgp \
    local.address=10.0.0.1 \
    cluster-id=10.0.0.1

# Announce specific networks
/routing bgp network
add network=10.0.0.0/24
add network=192.0.2.0/24
```

### Routing Filters (Policy)

RouterOS 7 uses a scripting-based routing filter system under `/routing filter rule`:

```
# Create a filter chain
/routing filter rule
add chain=EBGP-IMPORT \
    rule="if (dst-len > 24) { reject } accept"

# Match and set local preference
/routing filter rule
add chain=IBGP-IMPORT \
    rule="if (bgp-communities includes 65000:100) { set bgp-local-pref 200 } accept"

# Prefix list match
/routing filter rule
add chain=EBGP-EXPORT \
    rule="if (dst in 10.0.0.0/8 && dst-len <= 24) { accept } reject"

# AS path prepend on export
/routing filter rule
add chain=EBGP-EXPORT \
    rule="if (dst in 192.0.2.0/24) { set bgp-prepend 2 } accept"

# Strip all communities on import
/routing filter rule
add chain=EBGP-IMPORT \
    rule="set bgp-communities \"\" accept"
```

### RPKI (Route Origin Validation)

RouterOS 7 supports RPKI for BGP route origin validation:

```
# Configure RPKI validator
/routing bgp rpki session
add address=192.0.2.100 port=8282 refresh-interval=600

# Check RPKI session state
/routing bgp rpki session print

# RPKI-based filtering in routing filter
/routing filter rule
add chain=EBGP-IMPORT \
    rule="if (rpki invalid) { reject } accept"
```

---

## 9. MPLS Commands

RouterOS supports MPLS with LDP for label distribution. **RSVP-TE, SR-MPLS, and L3VPN (BGP/MPLS VPN) are not supported.** VPLS (Virtual Private LAN Service) is supported over MPLS. MPLS performance on CCR is CPU-bound; CRS switch chips do not support MPLS forwarding.

### Show Commands

```
# MPLS forwarding table
/mpls forwarding-table print                     # label forwarding entries
/mpls forwarding-table print detail

# LDP
/mpls ldp neighbor print                         # LDP neighbors
/mpls ldp neighbor print detail
/mpls ldp interface print                        # LDP-enabled interfaces
/mpls ldp local-info print                       # local LDP router-id and settings

# MPLS interfaces
/mpls interface print

# VPLS
/interface vpls print                            # VPLS instances
/interface vpls print detail                     # full VPLS detail
/interface vpls monitor 0                        # live VPLS stats

# Traffic Engineering Database (not RSVP — static TE only)
/mpls traffic-eng print
```

### Configuration Examples

```
# Enable MPLS globally and on interfaces
/mpls interface
add interface=sfp-sfpplus1
add interface=sfp-sfpplus2

# Enable LDP
/mpls ldp
set enabled=yes transport-address=10.0.0.1 lsr-id=10.0.0.1

/mpls ldp interface
add interface=sfp-sfpplus1
add interface=sfp-sfpplus2

# Static LSP (no RSVP-TE support)
/mpls static-mapping
add out-label=301 dst-address=10.0.0.2/32 nexthop=192.0.2.2

# VPLS pseudowire
/interface vpls
add name=vpls100 remote-peer=10.0.0.2 vpls-id=65000:100 pw-type=ethernet

# Disable MPLS on an interface
/mpls interface remove [find interface=ether1]
```

> **MPLS limitations**: RouterOS does not support RSVP-TE, SR-MPLS/SR-MPLS TE, or BGP L3VPN (VRF with MPLS forwarding). For these features, Juniper, Nokia, or Arista platforms are required. RouterOS MPLS is best suited for simple VPLS deployments over LDP.

---

## 10. IPv6 Commands

### IPv6 Interface Show Commands

```
/ipv6 address print                              # all IPv6 addresses
/ipv6 address print detail
/ipv6 address print where interface=sfp-sfpplus1

/interface print                                 # interfaces (IPv6 shown in address table)
/ipv6 neighbor print                             # NDP neighbor cache (like show arp)
/ipv6 neighbor print detail
/ipv6 neighbor print where interface=sfp-sfpplus1
```

### IPv6 Routing Table

```
/ipv6 route print                                # full IPv6 routing table
/ipv6 route print where active=yes              # active routes only
/ipv6 route print where bgp=yes                 # BGP IPv6 routes
/ipv6 route print where ospf=yes                # OSPFv3 routes
/ipv6 route print where dst-address~"2001:db8"  # match prefix range
```

### IPv6 Ping and Traceroute

```
/tool ping 2001:db8::1
/tool ping 2001:db8::1 count=5
/tool ping 2001:db8::1 src-address=2001:db8:1::1
/tool traceroute 2001:db8::1
/tool traceroute 2001:db8::1 src-address=2001:db8:1::1
```

### OSPFv3 (OSPF for IPv6)

```
/routing ospf neighbor print where instance~"v3"
/routing ospf lsa print where instance~"v3"
/ipv6 route print where active=yes
```

**OSPFv3 Configuration:**

```
/routing ospf instance
add name=ospf3 version=3 router-id=10.0.0.1

/routing ospf area
add name=backbone area-id=0.0.0.0 instance=ospf3

/routing ospf interface-template
add area=backbone interfaces=sfp-sfpplus1 type=ptp

# IPv6 address on interface
/ipv6 address add address=2001:db8:1::1/64 interface=sfp-sfpplus1
```

### BGP for IPv6

```
# BGP IPv6 session
/routing bgp connection
add name=IBGP-V6 \
    remote.address=2001:db8:0:2::1 \
    remote.as=65000 \
    local.role=ibgp \
    local.address=2001:db8:0:1::1 \
    address-families=ipv6 \
    nexthop-choice=force-self

# Announce IPv6 network
/routing bgp network
add network=2001:db8:100::/48

# View IPv6 BGP routes
/ipv6 route print where bgp=yes
```

### IPv6 Configuration Reference

```
# Dual-stack interface
/ipv6 address add address=2001:db8:1::1/64 interface=sfp-sfpplus1
/ip address add address=192.0.2.1/30 interface=sfp-sfpplus1

# IPv6 loopback
/ipv6 address add address=2001:db8:0:1::1/128 interface=loopback

# Static IPv6 route
/ipv6 route add dst-address=::/0 gateway=2001:db8:1::2
/ipv6 route add dst-address=2001:db8:100::/48 gateway=2001:db8:1::2

# Router Advertisement (SLAAC)
/ipv6 nd
add interface=ether1 advertise-dns=yes ra-lifetime=200s

# ND prefix for SLAAC
/ipv6 nd prefix
add interface=ether1 prefix=2001:db8:100::/64

# Suppress RA (uplink / point-to-point interfaces)
/ipv6 nd set [find interface=sfp-sfpplus1] disabled=yes

# DHCPv6 server
/ipv6 dhcp-server
add interface=ether1 name=dhcpv6-ether1 address-pool=v6-pool

/ipv6 pool
add name=v6-pool prefix=2001:db8:100::/48 prefix-length=64
```

### IPv6 Firewall

```
# Show IPv6 firewall rules and hit counts
/ipv6 firewall filter print

# Allow ICMPv6 (required for NDP and path MTU discovery)
/ipv6 firewall filter
add chain=input protocol=icmpv6 action=accept comment="Allow ICMPv6"
add chain=forward protocol=icmpv6 action=accept

# Block specific prefix
/ipv6 firewall filter
add chain=input src-address=2001:db8::/32 action=drop comment="Block documentation prefix"
```

---

## 11. Configuration Management

### Viewing Configuration

```
/export                                  # entire running configuration
/export compact                          # minimal (no defaults) — most common
/export verbose                          # include all default values
/ip address export                       # section-level export
/routing bgp export                      # BGP-only export

# Show current system identity and uptime
/system identity print
/system clock print
/system resource print                   # CPU, memory, uptime, version

# Show version
/system package print                    # all packages and versions
```

### Saving and Restoring Configuration

```
# Save config to router filesystem
/export file=pre-maintenance-backup

# Files stored in router's flash:
/file print                              # list files on router
/file print where name~"backup"

# Download via SCP/FTP/SMB from the router
# Config files are at / on the RouterOS filesystem

# Restore from file
/import file-name=pre-maintenance-backup.rsc

# Factory reset (WARNING: removes all config)
/system reset-configuration no-defaults=yes
```

### Backup vs Export

RouterOS has two distinct backup mechanisms:

| Method | Command | Format | Portable |
|---|---|---|---|
| Binary backup | `/system backup save` | Binary `.backup` | Same RouterOS version only |
| Script export | `/export file=name` | Plain text `.rsc` | Portable, human-readable |

```
# Binary backup (preserves everything including passwords, certificates)
/system backup save name=full-backup

# Restore binary backup
/system backup load name=full-backup.backup

# Script export (human-readable, for documentation and migration)
/export compact file=config-export
```

### Safe Mode (Config Rollback Protection)

```
# Enter safe mode before risky changes
# Press Ctrl+X — prompt changes to show <SAFE>

# Changes are auto-reverted if session drops
# To confirm changes: type 'exit' normally
# To manually revert without disconnecting:
/system safe-mode revert

# View what's changed while in safe mode
/system safe-mode print
```

### Netinstall (Factory Recovery)

Netinstall is an out-of-band recovery tool for when RouterOS is inaccessible. It reinstalls RouterOS from a network boot:

1. Hold the reset button while powering on to enter Netinstall mode
2. A Windows-based Netinstall tool provides the install image
3. After reinstall, the device is at factory defaults

---

## 12. Platform Details — CCR, CRS, and Switch Chips

### Platform Families

| Family | Role | Forwarding | Key Differentiator |
|---|---|---|---|
| **CCR** (Cloud Core Router) | Core/edge routing | CPU / NPU | High CPU throughput, no switch chip |
| **CRS** (Cloud Router Switch) | L2/L3 switching | Switch chip + CPU | Hardware-offloaded L2 at wire speed |
| **RB** (RouterBOARD) | SMB / prosumer | CPU | Compact, cost-effective |
| **CHR** | Virtual / cloud | Software | x86 VM, licensed by throughput |
| **hEX / hAP / cAP** | Home/SOHO | CPU | Consumer products, not covered here |

---

### CCR Series — Routing Platforms

CCR platforms are designed for high-throughput routing. They do not contain switch chips. All forwarding is CPU or NPU based, with MikroTik's FastPath and hardware queuing features providing acceleration for routed (L3) traffic.

| Model | CPU | RAM | Key Interfaces | Notes |
|---|---|---|---|---|
| CCR1009-8G-1S | Tilera (9-core) | 2G | 8×1G + 1×SFP | Older, MIPS |
| CCR1036-12G-4S | Tilera (36-core) | 4G | 12×1G + 4×SFP | Older, MIPS |
| CCR1072-1G-8S+ | Tilera (72-core) | 16G | 8×SFP+ | High core count MIPS |
| CCR2004-1G-12S+2XS | ARM Cortex-A72 (4-core) | 4G | 12×SFP+ + 2×SFP28 25G | Modern ARM, popular ISP router |
| CCR2116-12G-4S+ | ARM (16-core) | 16G | 12×1G + 4×SFP+ | High-memory variant |
| CCR2216-1G-12XS+2XQ | ARM (16-core) | 16G | 12×25G SFP28 + 2×100G QSFP28 | Current flagship, 100G capable |

**CCR use cases:**
- ISP edge routing, border BGP
- Inter-VLAN routing for large VLAN deployments
- VPN concentrator (IPSec, WireGuard)
- Traffic shaping and QoS at scale
- Firewall/NAT for enterprise internet edges

**Not suitable for:** High-density L2 switching, large MAC table deployments, or any application requiring wire-speed L2 forwarding across many ports.

---

### CRS Series — Switch Platforms with Switch ASICs

CRS platforms pair a RouterOS CPU with a dedicated **Marvell Prestera** switch ASIC. The switch chip provides wire-speed L2 forwarding, hardware VLANs, hardware STP, and hardware ACLs (limited TCAM). The CPU handles routing, management, and features the chip cannot execute.

> For detailed buffer specifications, TCAM sizing, and VOQ behavior by Marvell Prestera variant: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

#### CRS3xx — Mainstream Layer 2/3 Switches

Built around **Marvell Prestera 98DX3xxx** ASICs.

| Model | Ports | Switch Chip | Notes |
|---|---|---|---|
| CRS326-24G-2S+RM | 24×1G + 2×SFP+ | 98DX3236 | Most common 1G switch — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| CRS328-24P-4S+RM | 24×1G PoE + 4×SFP+ | 98DX3236 | PoE variant |
| CRS354-48P-4S+2Q+RM | 48×1G PoE + 4×SFP+ + 2×QSFP+ | 98DX3255 | 48-port PoE — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| CRS317-1G-16S+RM | 16×SFP+ | 98DX3236 | 10G aggregation |
| CRS309-1G-8S+IN | 8×SFP+ | 98DX3236 | Compact 10G switch |

**98DX3236 characteristics:**
- 24 ports at 1G or mixed 1G/10G
- Shared buffer architecture (not VOQ)
- Moderate TCAM: ~512 ACL rules in hardware
- Full VLAN support (4096 VLANs)
- Hardware STP/RSTP/MSTP
- No MPLS in switch chip

#### CRS5xx — High-Performance 25G/100G Switches

Built around **Marvell Prestera 98DX8xxx** ASICs. These chips support 25G and 100G ports, deeper buffers, and more capable TCAM.

| Model | Ports | Switch Chip | Notes |
|---|---|---|---|
| CRS504-4XQ-IN | 4×100G QSFP28 | 98DX8xxx | Compact 100G aggregation — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| CRS510-8XS-2XQ-IN | 8×25G + 2×100G | 98DX8xxx | 25G access + 100G uplinks — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| CRS518-16XS-2XQ-IN | 16×25G + 2×100G | 98DX8xxx | High-density 25G — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |

**98DX8xxx characteristics:**
- 25G/100G native port speeds
- Larger external packet buffer (vs. 98DX3xxx)
- More TCAM entries
- Still no MPLS in switch chip
- No VOQ — shared buffer with per-port and per-queue allocation

#### CRS Switch Chip Feature Matrix

| Feature | 98DX3236 (CRS3xx) | 98DX8xxx (CRS5xx) |
|---|---|---|
| L2 wire-speed forwarding | Yes | Yes |
| VLAN (802.1Q) in hardware | Yes | Yes |
| STP/RSTP/MSTP in hardware | Yes | Yes |
| ACL / TCAM rules | ~512 entries | More entries |
| MPLS forwarding | No | No |
| L3 routing in chip | Limited (basic) | Limited |
| Port speeds | 1G / 10G | 25G / 100G |
| Buffer type | Shared | Shared (larger) |
| Hardware offload in RouterOS | Yes | Yes |

#### Hardware Offload Show Commands (CRS)

```
# Most important: verify each port is actually in hardware
/interface bridge port print detail
# Key fields:
#   hw=yes     — port is hardware-offloaded (switch chip)
#   hw=no      — port is CPU-forwarded (investigate)
#   hw-offload-group=<n> — switch chip instance handling this port

# Direct switch chip view
/interface ethernet switch print
/interface ethernet switch port print
/interface ethernet switch port print detail

# Hardware MAC table (entries learned in chip)
/interface ethernet switch host print
/interface ethernet switch host print count-only

# Hardware ACL rules (programmed into switch TCAM)
/interface ethernet switch rule print

# Switch chip statistics (packet counters per port in chip)
/interface ethernet switch port print stats
```

#### SwOS — Alternative to RouterOS on CRS

CRS platforms can also run **SwOS**, MikroTik's dedicated switch-only OS. SwOS exposes the switch chip capabilities through a simplified web interface with no routing features. Use SwOS when:

- The device is purely a L2 switch with no routing requirement
- Simplicity and maximum switch chip utilization are the priority
- RouterOS complexity is not needed

Switch between OS modes:
```
# From RouterOS, switch to SwOS
/system routerboard settings set boot-os=swos
/system reboot

# From SwOS (web UI): System → RouterOS
```

### RB Series — RouterBOARD General Purpose

| Model | CPU | RAM | Key Interfaces | Notes |
|---|---|---|---|---|
| RB4011iGS+RM | ARM Cortex-A15 (4-core) | 1G | 10×1G + 1×SFP+ | Popular prosumer router |
| RB5009UG+S+IN | ARM Cortex-A72 (4-core) | 1G | 7×1G + 1×2.5G + 1×SFP+ 10G | Compact, high-port-count |
| RB3011UiAS-RM | ARM Cortex-A9 (dual) | 1G | 10×1G + 1×SFP | Two 5-port groups |

RB platforms have no switch chip (or limited switch chip on some older models). All switching and routing is CPU-based. Suitable for SMB routing, VPN, and moderate traffic volumes.

---

### QoS and Traffic Shaping

RouterOS QoS is CPU-based on all platforms. Switch chip-based QoS (shaping at wire speed within the chip) is not exposed in RouterOS in the same way as enterprise switch OS. Per-queue behavior in the Marvell Prestera chip is configurable via `/interface ethernet switch` but the full QoS model is accessed through RouterOS queues.

```
# Show queues
/queue simple print
/queue tree print

# Interface queue stats
/queue simple print stats

# HTB (Hierarchical Token Bucket) — full scheduler
/queue tree
add name=root-upload parent=sfp-sfpplus1 packet-mark=no-mark max-limit=1G
add name=voice parent=root-upload packet-mark=voice-mark priority=1 max-limit=100M
add name=best-effort parent=root-upload packet-mark=no-mark priority=8 max-limit=1G

# Firewall mangle to mark packets for QoS
/ip firewall mangle
add chain=prerouting src-address=10.0.0.0/24 \
    protocol=udp dst-port=5060,10000-20000 \
    action=mark-packet new-packet-mark=voice-mark passthrough=no
```

---

### Chassis and Hardware Commands

```
/system resource print                   # CPU load, memory, uptime, version
/system resource monitor                 # live resource stats (refresh every second)
/system health print                     # temperature, voltage, fan speed
/system routerboard print                # hardware model, serial, firmware
/system routerboard settings print       # boot settings, CPU frequency
/system package print                    # installed packages and versions
/system license print                    # license level and limits (CHR)
/interface ethernet print detail         # per-port detail including SFP DOM
```

---

## 13. Cross-Platform Command Reference

### General & Interface Commands

| Function | RouterOS 7 | JunOS | Nokia SR OS MD-CLI | EOS |
|---|---|---|---|---|
| Show interfaces | `/interface print` | `show interfaces terse` | `show router interface` | `show interfaces status` |
| Interface detail | `/interface print detail where name=ether1` | `show interfaces ge-0/0/0` | `show router interface "to-peer" detail` | `show interfaces Ethernet1` |
| Interface counters | `/interface print stats` | `show interfaces statistics` | `show port 1/1/1 statistics` | `show interfaces Ethernet1 counters` |
| Show MAC table | `/interface bridge host print` | `show ethernet-switching table` | `show service id 100 fdb` | `show mac address-table` |
| Disable interface | `/interface set ether1 disabled=yes` | `set interfaces ge-0/0/0 disable` | `/configure port 1/1/1 admin-state disable` | `shutdown` (interface mode) |
| Show running config | `/export compact` | `show configuration` | `info flat` | `show running-config` |
| Enter config mode | N/A (always in config) | `configure` | `edit-config exclusive` | `configure terminal` |
| Save config | Auto-saved (immediate) | `commit` | `commit` + `admin save` | `write memory` |
| Config rollback | `/import file=backup.rsc` | `rollback 1` | `tools rollback revert 1` | `configure replace checkpoint:X` |
| Config diff | Manual compare of exports | `show config \| compare` | `compare` | `show running-config diff` |

### Routing Protocol — OSPF

| Function | RouterOS 7 | JunOS | Nokia SR OS MD-CLI | EOS |
|---|---|---|---|---|
| OSPF neighbors | `/routing ospf neighbor print` | `show ospf neighbor` | `show router ospf neighbor` | `show ip ospf neighbor` |
| OSPF neighbor detail | `/routing ospf neighbor print detail` | `show ospf neighbor detail` | `show router ospf neighbor detail` | `show ip ospf neighbor detail` |
| OSPF interfaces | `/routing ospf interface print` | `show ospf interface` | `show router ospf interface` | `show ip ospf interface` |
| OSPF LSDB | `/routing ospf lsa print` | `show ospf database` | `show router ospf database` | `show ip ospf database` |
| OSPF routes | `/ip route print where ospf=yes` | `show route protocol ospf` | `show router route-table protocol ospf` | `show ip route ospf` |
| OSPFv3 neighbors | `/routing ospf neighbor print` (v3 instance) | `show ospf3 neighbor` | `show router ospf3 neighbor` | `show ipv6 ospf neighbor` |

### Routing Protocol — BGP

| Function | RouterOS 7 | JunOS | Nokia SR OS MD-CLI | EOS |
|---|---|---|---|---|
| BGP session summary | `/routing bgp session print` | `show bgp summary` | `show router bgp summary` | `show bgp summary` |
| BGP session detail | `/routing bgp session print detail` | `show bgp neighbor 10.0.0.2` | `show router bgp neighbor 10.0.0.2` | `show bgp neighbors 10.0.0.2` |
| BGP routes in RIB | `/ip route print where bgp=yes` | `show route protocol bgp` | `show router bgp routes ipv4` | `show bgp ipv4 unicast` |
| BGP prefix detail | `/ip route print detail where dst-address=10.0.0.0/8` | `show route 10/8 detail` | `show router bgp routes 10.0.0.0/8 detail` | `show bgp ipv4 unicast 10.0.0.0/8` |
| Routes advertised | `/routing bgp advertisements print where peer~"10.0.0.2"` | `show bgp neighbor X advertised-routes` | `show router bgp neighbor X advertised-routes ipv4` | `show bgp neighbors X advertised-routes` |
| BGP peers (config) | `/routing bgp connection print` | `show bgp group` | `show router bgp group "IBGP"` | `show bgp peer-group` |
| VRF routes | `/ip route print where routing-table=CUST-A` | `show route table CUST-A.inet.0` | `show router 100 route-table` | `show ip route vrf CUST-A` |

### MPLS

| Function | RouterOS 7 | JunOS | Nokia SR OS MD-CLI | EOS |
|---|---|---|---|---|
| LDP neighbors | `/mpls ldp neighbor print` | `show ldp neighbor` | `show router ldp neighbor` | `show mpls ldp neighbor` |
| LDP label bindings | `/mpls forwarding-table print` | `show ldp database` | `show router ldp bindings` | `show mpls ldp bindings` |
| MPLS label table | `/mpls forwarding-table print` | `show route table mpls.0` | `show router tunnel-table` | `show mpls lfib route` |
| RSVP-TE | **Not supported** | `show rsvp session` | `show router rsvp session` | `show mpls rsvp session` |
| SR-MPLS | **Not supported** | `show spring-traffic-engineering lsp` | `show router sr-te lsp` | `show traffic-engineering segment-routing` |

### L2 / VLANs

| Function | RouterOS 7 | JunOS | Nokia SR OS MD-CLI | EOS |
|---|---|---|---|---|
| Show VLANs | `/interface bridge vlan print` | `show vlans` | N/A (service-based) | `show vlan brief` |
| MAC table (software) | `/interface bridge host print` | `show ethernet-switching table` | `show service id 100 fdb` | `show mac address-table` |
| MAC table (hardware) | `/interface ethernet switch host print` | N/A | N/A | N/A |
| HW offload status | `/interface bridge port print detail` | N/A | N/A | N/A |
| LACP status | `/interface bonding print detail` | `show lacp interfaces ae0` | `show lag 1 detail` | `show lacp interface Port-Channel1` |
| STP state | `/interface bridge port print` | `show spanning-tree bridge` | `show service id 100 stp` | `show spanning-tree` |
| Pseudowire / VPLS | `/interface vpls print` | `show l2circuit connections` | `show service epipe` | N/A |

### System & Diagnostics

| Function | RouterOS 7 | JunOS | Nokia SR OS MD-CLI | EOS |
|---|---|---|---|---|
| Ping | `/tool ping 8.8.8.8 count=5` | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 repeat 5` |
| Traceroute | `/tool traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` |
| Bandwidth test | `/tool bandwidth-test 10.0.0.2` | N/A | N/A | N/A |
| Show ARP | `/ip arp print` | `show arp` | `show router arp` | `show arp` |
| Show routes | `/ip route print` | `show route` | `show router route-table` | `show ip route` |
| Disable paging | N/A (no pager by default) | `set cli screen-length 0` | `environment more false` | `terminal length 0` |
| Show version | `/system resource print` + `/system routerboard print` | `show version` | `show version` | `show version` |
| Show hardware | `/system routerboard print` | `show chassis hardware` | `show chassis detail` | `show inventory` |
| Logs | `/log print` | `show log messages` | `show log 99` | `show logging` |
| Live log tail | `/log print follow` | `monitor start messages` | `show log 99 \| tail` | `bash tail -f /var/log/messages` |
| CPU/memory | `/system resource print` | `show chassis routing-engine` | `show system cpu` | `show processes top` |
| Reboot | `/system reboot` | `request system reboot` | `admin reboot` | `reload` |
| Save config | `/export file=backup` (manual) | `commit` | `admin save` | `write memory` |
| Match/grep | `/x print where field~"pattern"` | `show ... \| match <regex>` | `show ... \| match <regex>` | `show ... \| include <regex>` |

---

## 14. Quick Reference Card

### Top 20 Daily-Driver Commands

```bash
# System health
/system resource print                   # CPU, memory, uptime, version
/system health print                     # temperature, voltage, fan speed
/log print where message~"error" follow-only  # live error log

# Interfaces
/interface print                         # all interfaces and link state
/interface print stats                   # packet/byte counters
/interface monitor-traffic ether1        # live bps/pps

# CRS-specific — always check this first on switch platforms
/interface bridge port print detail      # verify hw=yes on all bridge ports
/interface ethernet switch host print    # hardware MAC table

# Routing
/ip route print where active=yes         # active routing table
/ip route print count-only               # total route count
/ip route print where bgp=yes && active=yes  # active BGP routes
/ip arp print                            # ARP table

# BGP / OSPF
/routing bgp session print               # BGP session state at a glance
/routing ospf neighbor print             # OSPF adjacencies
/routing ospf neighbor print where state!=full  # non-full (problems)

# MPLS
/mpls ldp neighbor print                 # LDP session state
/mpls forwarding-table print             # MPLS label forwarding table

# Config workflow
/export compact                          # running config as import-ready script
/export compact file=pre-change          # save named backup before changes
# Ctrl+X                                 # enter safe mode before risky changes
/import file=pre-change.rsc              # restore from backup
```

### Useful One-Liners

```bash
# Show only up interfaces
/interface print where running=yes

# Show only down interfaces (not admin-disabled)
/interface print where running=no && disabled=no

# Count active BGP sessions
/routing bgp session print count-only where established=yes

# BGP sessions that are NOT established
/routing bgp session print where established=no

# OSPF neighbors not in Full state
/routing ospf neighbor print where state!=full

# Find interfaces without hardware offload (CRS — critical check)
/interface bridge port print where hw=no

# Find a specific IP in the config
/ip address print where address~"192.0.2"

# Show all routes for a specific next-hop
/ip route print where gateway~"10.0.0.2"

# Show recent log entries matching a term
/log print where message~"bgp" && time>([/system clock get time]-00:10:00)

# Bandwidth test to a remote RouterOS host
/tool bandwidth-test 10.0.0.2 protocol=tcp direction=both duration=10

# Check switch chip MAC count vs hardware capacity
/interface ethernet switch host print count-only

# Show all VLANs and their port membership
/interface bridge vlan print detail

# Export only BGP config for documentation
/routing bgp export compact
```

### RouterOS 7 Mental Models

| Concept | RouterOS Way | Notes |
|---|---|---|
| No candidate config | Changes apply immediately | Use safe mode (Ctrl+X) to protect against lockout |
| `export` is your backup | `/export compact file=name` | Script format — both backup and documentation |
| `where` is your filter | `/ip route print where active=yes` | Replaces Unix pipes for filtering |
| Print is universal show | `print`, `print detail`, `print terse`, `print stats` | Every menu uses `print` variants |
| Paths are hierarchical | `/ip/address` or `/ip address` both work | Navigate with `..` and `/` |
| CCR = routing, not switching | No switch chip | CPU-limited for L2; excellent for routed traffic |
| CRS = switch chip + CPU | Must verify `hw=yes` | Wire-speed L2 only when hardware offload active |
| hw=no is a silent failure | RouterOS will not warn you | Always verify with `/interface bridge port print detail` |
| Switch chip ACLs | `/interface ethernet switch rule` | TCAM-limited; faster than `/ip firewall filter` |
| IS-IS not supported | Use OSPF | Hard limitation — not a configurable feature |
| MPLS = LDP only | No RSVP-TE, no SR-MPLS | VPLS over LDP is the main MPLS use case |
| `follow` for live output | `/log print follow-only` | Like `tail -f` — Ctrl+C to stop |
| Safe mode | Ctrl+X to enable | Auto-reverts if session drops |
| SwOS alternative | CRS can run SwOS instead | Web-only, switch-only mode for pure L2 deployments |

---

*Curriculum version: 1.0 | Target: MikroTik RouterOS 7 — CCR2xxx / CRS3xx / CRS5xx / RBxxxx platforms*
*Reference platforms for comparison: Juniper JunOS MX/ACX, Nokia SR OS MD-CLI, Arista EOS*
*Switch chip buffer and TCAM details: [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)*

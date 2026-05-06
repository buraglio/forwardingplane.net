---
title: Nokia SR Linux Basics
date: 2026-05-06
author: Nick Buraglio
layout: page
---

# Nokia SR Linux Basics

A practical curriculum for network engineers learning Nokia SR Linux, with emphasis on its model-driven CLI, YANG-based configuration paradigm, cloud-native architecture, and platform-specific capabilities across 7220 IXR (merchant silicon) and 7250/7730 IXR (FP-based) hardware. Includes cross-platform translation from JunOS, Nokia SR OS, Arista EOS, and RouterOS.

> **SR Linux vs SR OS**: These are distinct operating systems that share the Nokia brand. SR OS targets service provider core/edge routing on proprietary FP silicon with a full carrier Ethernet and MPLS service stack. SR Linux targets cloud and data center networking on merchant silicon, emphasizing programmability, EVPN/VXLAN, and API-first operation. They run different YANG models, different CLIs, and are generally deployed in different network layers.

---

## Table of Contents

1. [SR Linux Fundamentals](#1-sr-linux-fundamentals)
2. [CLI Navigation & Usability](#2-cli-navigation--usability)
3. [Pipe Commands & Output Filtering](#3-pipe-commands--output-filtering)
4. [Interface Commands](#4-interface-commands)
5. [Network Instances, VLANs & EVPN/VXLAN](#5-network-instances-vlans--evpnvxlan)
6. [OSPF Commands](#6-ospf-commands)
7. [IS-IS Commands](#7-is-is-commands)
8. [BGP Commands](#8-bgp-commands)
9. [MPLS Commands](#9-mpls-commands)
10. [IPv6 Commands](#10-ipv6-commands)
11. [Configuration Management](#11-configuration-management)
12. [Platform & Silicon Details](#12-platform--silicon-details)
13. [Cross-Platform Command Reference](#13-cross-platform-command-reference)
14. [Quick Reference Card](#14-quick-reference-card)

---

## 1. SR Linux Fundamentals

### Architecture Overview

Nokia SR Linux is a cloud-native, fully containerized network operating system built on an unmodified Debian Linux kernel. Unlike JunOS or Nokia SR OS, SR Linux does not use a proprietary or customized kernel — the entire OS layer is standard Linux, and the network control plane runs as a set of isolated microservice-style applications (called **agents**) that communicate through a shared in-memory state database called **IDB** (Interaction Database), conceptually similar to Arista's Sysdb but fully documented via YANG models.

```
┌──────────────────────────────────────────────────────────────────┐
│                         SR Linux                                 │
│                                                                  │
│  mgr  bgp  ospf  isis  evpn  mpls  acl  qos  ...                │
│   │    │    │     │     │     │     │    │                       │
│   └────┴────┴─────┴─────┴─────┴─────┴────┴── IDB ──► CLI/gNMI  │
│                                                                  │
│  Standard Debian Linux kernel                                    │
│  Hardware abstraction layer (platform manager)                   │
│  Forwarding ASIC driver (Broadcom SDK / FP SDK)                  │
└──────────────────────────────────────────────────────────────────┘
```

SR Linux is **API-first**: the CLI, gNMI server, JSON-RPC server, and all management interfaces share the same underlying YANG data models. Every CLI command corresponds to a gNMI path. A configuration applied via `commit now` in the CLI is identical to one pushed via `gnmi_set`. This makes SR Linux uniquely suited to intent-based and programmable networking.

The **NDK (Nokia Development Kit)** allows custom applications (written in Go, Python, or Rust) to run directly on SR Linux as first-class agents, subscribing to state events and modifying configuration through the same IDB bus used by native daemons.

SR Linux runs on merchant silicon (Broadcom Trident4, Tomahawk4, Jericho2c+) and Nokia FP4/FP5 (on 7250 IXR-e and 7730 SXR). The feature set is partly determined by the underlying ASIC. For chipset-specific buffer and TCAM details, see [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/).

### Configuration Datastores

SR Linux uses a three-datastore model derived from NETCONF/YANG principles:

| Datastore | Description | CLI Access |
|---|---|---|
| **Running** | The committed, active configuration | `enter running` |
| **Candidate** | Editable staging area for uncommitted changes | `enter candidate` |
| **State** | Operational (live) data — not editable | `enter state` or `info from state` |

This is more granular than JunOS (which conflates running and candidate into one active/candidate pair) and more explicit than Arista EOS (where config is active immediately unless using sessions). The `state` datastore is a first-class concept in SR Linux and exposes operational counters, adjacency state, routes, and hardware tables all through the same YANG tree as configuration.

### CLI Prompt Structure

The prompt encodes the current datastore and YANG path context:

```
--{ running }--[ ]--
A:leaf1#                          # running datastore, at YANG root

--{ candidate shared default }--[ ]--
A:leaf1#                          # candidate datastore, at YANG root

--{ running }--[ network-instance default ]--
A:leaf1#                          # running mode, inside network-instance context

--{ candidate private }--[ interface ethernet-1/1 ]--
A:leaf1#                          # private candidate, inside interface context
```

### Candidate Modes

| Mode | Command | Behavior |
|---|---|---|
| Shared | `enter candidate` | Multiple users can edit; last commit wins for each path |
| Exclusive | `enter candidate exclusive` | Locks candidate; others cannot edit until you exit |
| Private | `enter candidate private` | Isolated copy; changes invisible to other users until committed |

---

## 2. CLI Navigation & Usability

### Entering Datastores

```
enter running                    # view active configuration
enter candidate                  # open shared candidate for editing
enter candidate exclusive        # exclusive lock on candidate
enter candidate private          # private isolated candidate
enter state                      # view operational/state data
exit                             # exit current mode, return to running
```

### Path Navigation

SR Linux CLI navigation directly mirrors the YANG model hierarchy. You navigate by typing path segments, which sets your current context:

```
# From root, navigate into a context:
/ network-instance default

--{ running }--[ network-instance default ]--
A:leaf1#

# Navigate deeper:
/ network-instance default protocols bgp

# Return to root:
/

# Go up one level:
..

# Show current path:
pwd
```

### Tab Completion & Help

```
show <Tab>                        # list all show sub-commands
/ interface <Tab>                 # list available interfaces
set admin-state <Tab>             # show valid values (enable / disable)
/ interface ethernet-1/1 ?        # context-sensitive help
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Complete command or show options |
| `?` | Context-sensitive help |
| `Ctrl+A` | Move cursor to beginning of line |
| `Ctrl+E` | Move cursor to end of line |
| `Ctrl+U` | Delete to beginning of line |
| `Ctrl+K` | Delete to end of line |
| `Ctrl+W` | Delete previous word |
| `Ctrl+R` | Reverse search history |
| `Ctrl+C` | Abort current command |
| `Ctrl+D` | Exit session (if line empty) |
| `Ctrl+Z` | Return to YANG root context |
| Up/Down | Navigate command history |

### Abbreviations

SR Linux supports unambiguous prefix abbreviations:

```
sh int                           # show interface
sh net def rou                   # show network-instance default route-table
en cand                          # enter candidate
```

### Terminal Settings

```
environment cli prompt-format ""             # simplify prompt
environment cli default-format flat          # default to flat format for info
environment more false                       # disable pagination globally
environment cli output-format table          # prefer table output for show commands
```

### Bash Shell Access

Because SR Linux runs on standard Debian Linux, engineers with root access can drop to bash for diagnostics:

```
bash                             # open a bash shell
# Linux tools available: ip, ss, ping, tcpdump, curl, python3, etc.
exit                             # return to SR Linux CLI
```

```bash
# Examples from bash:
ip route show                    # Linux kernel route table
ip link show                     # Linux interface state
ss -s                            # socket statistics
cat /proc/net/dev                # raw interface counters
```

---

## 3. Pipe Commands & Output Filtering

SR Linux pipe commands apply to both `show` output and `info` output. They follow Unix grep conventions.

### Core Pipe Commands

| Pipe Command | Description | Example |
|---|---|---|
| `\| grep <pattern>` | Show lines matching pattern | `show interface \| grep ethernet` |
| `\| grep -v <pattern>` | Exclude matching lines | `show network-instance default route-table \| grep -v 0.0.0.0` |
| `\| grep -i <pattern>` | Case-insensitive match | `show interface \| grep -i "up"` |
| `\| grep -A <n>` | Match + N lines after | `show interface \| grep -A 3 "ethernet-1/1"` |
| `\| head <n>` | First N lines | `show network-instance default route-table \| head 20` |
| `\| tail <n>` | Last N lines | `show log \| tail 50` |
| `\| more` | Paginate output | `show network-instance default route-table \| more` |
| `\| count` | Count lines | `show network-instance default route-table \| count` |
| `\| as-json` | Output in JSON format | `show interface \| as-json` |
| `\| as-table` | Force table layout | `show network-instance default route-table \| as-table` |

### Chaining Pipes

```
show network-instance default route-table | grep bgp | count
show interface | grep -v "down" | grep ethernet
show network-instance default protocols bgp neighbor | grep "Established"
info flat | grep "192.0.2"
```

### `info` — The Configuration Display Command

`info` is the primary tool for viewing configuration. It reads from the current datastore (running or candidate) at the current YANG path context.

```
info                             # show config at current path (hierarchical)
info flat                        # show as flat absolute YANG path statements
info detail                      # include all attributes, even defaults
info from state                  # show operational state at current YANG path
info from state flat             # operational state in flat format
```

Example flat config output (analogous to JunOS `display set`, Nokia SR OS `info flat`):
```
--{ running }--[ ]--
A:leaf1# info flat | grep ethernet-1/1
    interface ethernet-1/1 admin-state enable
    interface ethernet-1/1 description "To-Spine-1"
    interface ethernet-1/1 ethernet port-speed 100G
    interface ethernet-1/1 subinterface 1 ipv4 address 192.0.2.1/30
    interface ethernet-1/1 subinterface 1 ipv4 admin-state enable
    network-instance default interface ethernet-1/1.1
```

### JSON Output for Automation

```
show interface | as-json
show network-instance default route-table | as-json
info | as-json                   # entire config as JSON
info from state | as-json        # entire state as JSON
```

JSON output matches the gNMI response format, making it directly usable in scripts and automation pipelines.

---

## 4. Interface Commands

### Interface Model

SR Linux uses the same port/subinterface separation as Nokia SR OS, extended with an explicit **network-instance binding** step:

1. **Interface** (`/interface ethernet-1/1`) — physical layer config: speed, description, admin-state
2. **Subinterface** (`/interface ethernet-1/1 subinterface 1`) — logical L3 layer: IP addresses, VLAN encapsulation, ACLs
3. **Network-instance binding** — `interface ethernet-1/1.1` must be explicitly added to a network-instance before the subinterface participates in routing

The subinterface index (`.1`, `.2`) is arbitrary — it does NOT need to match the VLAN ID. VLAN IDs are configured within the subinterface's `vlan encap` block.

### Interface Naming

```
ethernet-1/1         # Ethernet, slot 1, port 1 (fixed platform)
ethernet-1/1/1       # Ethernet, slot 1, card 1, port 1 (modular)
ethernet-1/1.1       # subinterface 1 on ethernet-1/1 (notation: interface.subif-index)
mgmt0                # out-of-band management interface
mgmt0.0              # management subinterface
system0              # system loopback (like "system" in SR OS, lo0 in JunOS)
system0.0            # system loopback subinterface
loopback-1           # numbered loopback (additional loopbacks beyond system0)
lag-1                # link aggregation group
lag-1.1              # LAG subinterface
irb0                 # integrated routing and bridging (L3 gateway for mac-vrf)
irb0.1               # IRB subinterface
```

### Show Commands

```
show interface                               # all interfaces, summary
show interface ethernet-1/1                  # specific interface detail
show interface ethernet-1/1 detail           # full detail including counters
show interface brief                         # one-line per interface
show interface | grep -v "down"              # only interfaces not down

# Subinterface and binding
info interface ethernet-1/1                  # config view of interface
info from state interface ethernet-1/1       # operational state of interface

# Optical / transceiver
info from state interface ethernet-1/1 transceiver
# (shows rx-power, tx-power, temperature, voltage)

# LAG
show lag
show lag lag-1 detail                        # member links, LACP state

# LLDP neighbors
show system lldp neighbor
show system lldp neighbor ethernet-1/1 detail
```

### Interface Status Output

```
show interface
```
```
+---------------------+-------+--------+--------+-------+------------------+
| Interface           | Admin | Oper   | Speed  | MTU   | Type             |
+=====================+=======+========+========+=======+==================+
| ethernet-1/1        | enable| up     | 100G   | 9232  | 100GBASE-SR4     |
| ethernet-1/2        | enable| down   | 25G    | 9232  | Not Present      |
| ethernet-1/3        | enable| up     | 25G    | 9232  | 25GBASE-SR       |
| mgmt0               | enable| up     | 1G     | 1514  | copper           |
| system0             | enable| up     |        | 65535 | none             |
+---------------------+-------+--------+--------+-------+------------------+
```

### Configuration Examples

```
# Enable physical interface and set speed
set / interface ethernet-1/1 admin-state enable
set / interface ethernet-1/1 description "To-Spine-1"
set / interface ethernet-1/1 ethernet port-speed 100G

# Create L3 subinterface (routed, untagged)
set / interface ethernet-1/1 subinterface 1 admin-state enable
set / interface ethernet-1/1 subinterface 1 ipv4 address 192.0.2.1/30
set / interface ethernet-1/1 subinterface 1 ipv6 address 2001:db8:1::1/64

# Create L3 subinterface (single-tagged VLAN)
set / interface ethernet-1/1 subinterface 100 admin-state enable
set / interface ethernet-1/1 subinterface 100 vlan encap single-tagged vlan-id 100
set / interface ethernet-1/1 subinterface 100 ipv4 address 10.100.0.1/24

# System (loopback) interface
set / interface system0 subinterface 0 admin-state enable
set / interface system0 subinterface 0 ipv4 address 10.0.0.1/32
set / interface system0 subinterface 0 ipv6 address 2001:db8:0:1::1/128

# Bind subinterface to default network instance
set / network-instance default interface ethernet-1/1.1
set / network-instance default interface system0.0

# LAG
set / interface lag-1 admin-state enable
set / interface lag-1 lag lag-type lacp
set / interface lag-1 lag lacp interval fast
set / interface ethernet-1/3 ethernet aggregate-id lag-1
set / interface ethernet-1/4 ethernet aggregate-id lag-1
set / interface lag-1 subinterface 1 ipv4 address 192.0.2.5/30
set / network-instance default interface lag-1.1

# MTU (jumbo frames)
set / interface ethernet-1/1 mtu 9232
```

---

## 5. Network Instances, VLANs & EVPN/VXLAN

The **network instance** is SR Linux's unified model for routing domains — it replaces JunOS routing-instances, Nokia SR OS VPRNs/VPLS/EPIPE services, and Arista EOS VRFs within a single consistent concept.

### Network Instance Types

| Type | Purpose | Analogous |
|---|---|---|
| `default` | The default IP routing domain | JunOS `inet.0`, SR OS Base router, EOS default VRF |
| `ip-vrf` | Named L3 VPN / VRF | JunOS routing-instance type vrf, SR OS VPRN |
| `mac-vrf` | L2 broadcast domain (EVPN) | JunOS routing-instance type evpn, SR OS VPLS |
| `host` | Used for management plane isolation | Internal |

```
# Show all network instances
show network-instance
show network-instance default

# Route tables
show network-instance default route-table
show network-instance default route-table ipv4-unicast
show network-instance default route-table ipv6-unicast
show network-instance default route-table all

# ARP / NDP tables
show network-instance default arp-table
show network-instance default ipv6 nd-table
show arpnd

# Next-hop table
show network-instance default route-table nexthop-group
```

### IP-VRF (L3 VRF)

```
# Create an L3 VRF
set / network-instance CUST-A type ip-vrf
set / network-instance CUST-A interface ethernet-1/5.1
set / network-instance CUST-A protocols bgp autonomous-system 65100
set / network-instance CUST-A protocols bgp router-id 172.16.0.1

# Static routes in a VRF
set / network-instance CUST-A next-hop-groups nhg-1 nexthop 1 ip-address 172.16.0.2
set / network-instance CUST-A static-routes route 0.0.0.0/0 next-hop-group nhg-1

# View VRF route table
show network-instance CUST-A route-table
```

### MAC-VRF (L2 Network Instance — EVPN/VXLAN)

A `mac-vrf` defines a single L2 broadcast domain. VXLAN VNI, EVPN EVI, and bridge-table management all live here.

```
show network-instance mac-vrf-100 bridge-table mac-table all
show network-instance mac-vrf-100 bridge-table mac-table all | grep evpn
show tunnel-interface vxlan1 vxlan-interface 1
show tunnel-interface vxlan1 vxlan-interface 1 bridge-table
```

### VXLAN Tunnel Interface

```
# Create VXLAN tunnel interface (source = system loopback)
set / tunnel-interface vxlan1 vxlan-interface 1 type bridged
set / tunnel-interface vxlan1 vxlan-interface 1 ingress vni 10100

# Routed VXLAN (for symmetric IRB / L3 EVPN)
set / tunnel-interface vxlan1 vxlan-interface 2 type routed
set / tunnel-interface vxlan1 vxlan-interface 2 ingress vni 10200
```

### EVPN/VXLAN Configuration

This is the primary L2VPN model in SR Linux. Symmetric IRB (with ip-vrf + mac-vrf pairing) is the standard pattern for distributed L3 gateways in DC fabrics.

```
# 1. Create MAC-VRF (L2 network instance)
set / network-instance mac-vrf-100 type mac-vrf
set / network-instance mac-vrf-100 interface ethernet-1/1.100
set / network-instance mac-vrf-100 vxlan-interface vxlan1.1

# 2. Attach IRB subinterface for L3 gateway (symmetric IRB)
set / interface irb0 subinterface 100 admin-state enable
set / interface irb0 subinterface 100 ipv4 address 10.100.0.1/24
set / interface irb0 subinterface 100 anycast-gw true
set / network-instance mac-vrf-100 interface irb0.100

# 3. Configure BGP EVPN control plane within mac-vrf
set / network-instance mac-vrf-100 protocols bgp-evpn bgp-instance 1 admin-state enable
set / network-instance mac-vrf-100 protocols bgp-evpn bgp-instance 1 vxlan-interface vxlan1.1
set / network-instance mac-vrf-100 protocols bgp-evpn bgp-instance 1 evi 100
set / network-instance mac-vrf-100 protocols bgp-evpn bgp-instance 1 ecmp 4

set / network-instance mac-vrf-100 protocols bgp-vpn bgp-instance 1 route-distinguisher rd 65000:100
set / network-instance mac-vrf-100 protocols bgp-vpn bgp-instance 1 route-target export-rt target:65000:100
set / network-instance mac-vrf-100 protocols bgp-vpn bgp-instance 1 route-target import-rt target:65000:100

# 4. Bind IRB to IP-VRF for symmetric IRB routing
set / network-instance ip-vrf-1 type ip-vrf
set / network-instance ip-vrf-1 interface irb0.100

# 5. BGP EVPN type-5 (IP prefix) for the IP-VRF
set / network-instance ip-vrf-1 protocols bgp-evpn bgp-instance 1 admin-state enable
set / network-instance ip-vrf-1 protocols bgp-evpn bgp-instance 1 vxlan-interface vxlan1.2
set / network-instance ip-vrf-1 protocols bgp-evpn bgp-instance 1 evi 200
set / network-instance ip-vrf-1 protocols bgp-vpn bgp-instance 1 route-distinguisher rd 65000:200
set / network-instance ip-vrf-1 protocols bgp-vpn bgp-instance 1 route-target export-rt target:65000:200
set / network-instance ip-vrf-1 protocols bgp-vpn bgp-instance 1 route-target import-rt target:65000:200
```

### EVPN Show Commands

```
show network-instance mac-vrf-100 bridge-table mac-table all      # MAC/IP table
show network-instance mac-vrf-100 bridge-table mac-table evpn     # EVPN-learned MACs
show network-instance mac-vrf-100 bridge-table statistics         # per-EVI stats
show tunnel-interface vxlan1 vxlan-interface 1 bridge-table       # per-VTEP MAC entries
show network-instance default protocols bgp routes evpn summary   # EVPN BGP route types
show network-instance default protocols bgp routes evpn route-type 2  # Type-2 MAC/IP
show network-instance default protocols bgp routes evpn route-type 3  # Type-3 IMET
show network-instance default protocols bgp routes evpn route-type 5  # Type-5 IP prefix
show network-instance default tunnel-table all                     # resolved VTEP tunnel table
```

---

## 6. OSPF Commands

### Show Commands

```
show network-instance default protocols ospf
show network-instance default protocols ospf neighbor             # adjacencies
show network-instance default protocols ospf neighbor detail      # full neighbor state
show network-instance default protocols ospf interface            # per-interface OSPF state
show network-instance default protocols ospf interface detail     # DR/BDR, timers, costs
show network-instance default protocols ospf database             # LSDB summary
show network-instance default protocols ospf database detail      # full LSDB
show network-instance default protocols ospf database lsa router  # Router LSAs
show network-instance default protocols ospf database lsa network # Network LSAs
show network-instance default protocols ospf database lsa external# External (Type-5) LSAs
show network-instance default protocols ospf route-table          # OSPF-computed routes
show network-instance default protocols ospf statistics           # PDU + SPF counters
```

### Route Table Integration

```
show network-instance default route-table ipv4-unicast | grep ospf
show network-instance default route-table ipv4-unicast prefix 10.0.0.0/8 detail
```

### OSPFv3 (IPv6)

```
show network-instance default protocols ospf3 neighbor
show network-instance default protocols ospf3 interface
show network-instance default protocols ospf3 database
show network-instance default route-table ipv6-unicast | grep ospf
```

### Configuration Examples

```
# OSPF instance in the default network instance
set / network-instance default protocols ospf instance ospf-main
set / network-instance default protocols ospf instance ospf-main admin-state enable
set / network-instance default protocols ospf instance ospf-main version ospf-v2
set / network-instance default protocols ospf instance ospf-main router-id 10.0.0.1

# Area 0 — add interfaces
set / network-instance default protocols ospf instance ospf-main area 0.0.0.0 \
    interface ethernet-1/1.1 admin-state enable
set / network-instance default protocols ospf instance ospf-main area 0.0.0.0 \
    interface ethernet-1/1.1 interface-type point-to-point
set / network-instance default protocols ospf instance ospf-main area 0.0.0.0 \
    interface ethernet-1/1.1 metric 10

# Passive loopback
set / network-instance default protocols ospf instance ospf-main area 0.0.0.0 \
    interface system0.0 admin-state enable
set / network-instance default protocols ospf instance ospf-main area 0.0.0.0 \
    interface system0.0 passive true

# Stub area
set / network-instance default protocols ospf instance ospf-main area 0.0.0.1 \
    stub admin-state enable

# Authentication
set / network-instance default protocols ospf instance ospf-main area 0.0.0.0 \
    interface ethernet-1/1.1 authentication keychain OSPF-KEYS

# Reference bandwidth
set / network-instance default protocols ospf instance ospf-main \
    reference-bandwidth 100000000000

# Redistribute connected
set / network-instance default protocols ospf instance ospf-main \
    export-policy EXPORT-CONNECTED

# OSPFv3 for IPv6
set / network-instance default protocols ospf3 instance ospf3-main
set / network-instance default protocols ospf3 instance ospf3-main admin-state enable
set / network-instance default protocols ospf3 instance ospf3-main router-id 10.0.0.1
set / network-instance default protocols ospf3 instance ospf3-main area 0.0.0.0 \
    interface ethernet-1/1.1 admin-state enable
```

---

## 7. IS-IS Commands

IS-IS is natively supported in SR Linux and is commonly used as the underlay IGP in EVPN/VXLAN data center fabrics (either IS-IS-only or combined with eBGP underlay). It supports both IPv4 and IPv6 topologies, multi-topology IS-IS, and segment routing with the `ipv4-node-sid` extensions.

### Show Commands

```
show network-instance default protocols isis
show network-instance default protocols isis adjacency            # IS-IS adjacencies
show network-instance default protocols isis adjacency detail     # hold time, circuit type
show network-instance default protocols isis interface            # per-interface IS-IS state
show network-instance default protocols isis interface detail     # metrics, timers
show network-instance default protocols isis database             # LSDB summary
show network-instance default protocols isis database detail      # full TLV content
show network-instance default protocols isis database level 2     # L2 only
show network-instance default protocols isis hostname             # dynamic hostname map
show network-instance default protocols isis route-table          # IS-IS computed routes
show network-instance default protocols isis statistics           # PDU counters, SPF runs
show network-instance default protocols isis segment-routing prefix-segments
```

### Route Table Integration

```
show network-instance default route-table ipv4-unicast | grep isis
show network-instance default route-table ipv6-unicast | grep isis
show network-instance default route-table ipv4-unicast prefix 10.0.0.0/8 detail
```

### Configuration Examples

```
# IS-IS instance
set / network-instance default protocols isis instance CORE
set / network-instance default protocols isis instance CORE admin-state enable
set / network-instance default protocols isis instance CORE level-capability L2
set / network-instance default protocols isis instance CORE net ["49.0001.0100.0000.0001.00"]

# Wide metrics (required for SR and IPv6 MT)
set / network-instance default protocols isis instance CORE level 2 metric-style wide

# Multi-topology IS-IS for IPv6
set / network-instance default protocols isis instance CORE ipv6-unicast-routing multi-topology

# Interface configuration
set / network-instance default protocols isis instance CORE \
    interface ethernet-1/1.1 admin-state enable
set / network-instance default protocols isis instance CORE \
    interface ethernet-1/1.1 circuit-type point-to-point
set / network-instance default protocols isis instance CORE \
    interface ethernet-1/1.1 level 2 metric 10

# Passive loopback
set / network-instance default protocols isis instance CORE \
    interface system0.0 admin-state enable
set / network-instance default protocols isis instance CORE \
    interface system0.0 passive true

# Authentication
set / network-instance default protocols isis instance CORE \
    interface ethernet-1/1.1 level 2 authentication keychain ISIS-KEYS
set / network-instance default protocols isis instance CORE \
    interface ethernet-1/1.1 level 2 authentication hello-authentication true

# L2-only router
set / network-instance default protocols isis instance CORE level 1 admin-state disable

# Segment Routing (SR-MPLS) — requires FP-based platform
set / network-instance default protocols isis instance CORE \
    segment-routing mpls admin-state enable
set / network-instance default protocols isis instance CORE \
    segment-routing mpls srgb start-label 16000 end-label 24000

# Node SID assignment
set / interface system0 subinterface 0 isis ipv4-node-sid index 1

# Redistribute into IS-IS
set / network-instance default protocols isis instance CORE \
    export-policy EXPORT-CONNECTED
```

---

## 8. BGP Commands

### Show Commands

```
# Summary
show network-instance default protocols bgp summary
show network-instance default protocols bgp neighbor             # all neighbors
show network-instance default protocols bgp neighbor 192.0.2.2   # specific neighbor
show network-instance default protocols bgp neighbor 192.0.2.2 detail

# Route views
show network-instance default protocols bgp routes ipv4-unicast summary
show network-instance default protocols bgp routes ipv4-unicast prefix 10.0.0.0/8 detail
show network-instance default protocols bgp routes ipv6-unicast summary
show network-instance default protocols bgp routes evpn summary        # all EVPN NLRIs
show network-instance default protocols bgp routes evpn route-type 2  # MAC/IP
show network-instance default protocols bgp routes evpn route-type 5  # IP prefix

# Per-neighbor advertised/received
show network-instance default protocols bgp neighbor 192.0.2.2 received-routes ipv4
show network-instance default protocols bgp neighbor 192.0.2.2 advertised-routes ipv4

# BGP community filtering
show network-instance default protocols bgp routes ipv4-unicast community 65000:100

# L3VPN / VRF
show network-instance CUST-A protocols bgp summary
show network-instance CUST-A route-table ipv4-unicast
```

### Debugging BGP

```
show network-instance default protocols bgp neighbor 192.0.2.2 | grep -i "state\|hold\|prefix"
info from state network-instance default protocols bgp neighbor 192.0.2.2
show log | grep -i bgp | tail 50
```

### Configuration Examples

```
# BGP in default network instance
set / network-instance default protocols bgp autonomous-system 65000
set / network-instance default protocols bgp router-id 10.0.0.1
set / network-instance default protocols bgp dynamic-neighbors accept-all-peers true

# iBGP group (route reflector clients)
set / network-instance default protocols bgp group IBGP
set / network-instance default protocols bgp group IBGP admin-state enable
set / network-instance default protocols bgp group IBGP peer-as 65000
set / network-instance default protocols bgp group IBGP local-as as-number 65000
set / network-instance default protocols bgp group IBGP family evpn admin-state enable
set / network-instance default protocols bgp group IBGP family ipv4-unicast admin-state enable
set / network-instance default protocols bgp group IBGP next-hop-self true
set / network-instance default protocols bgp group IBGP route-reflector client true
set / network-instance default protocols bgp group IBGP route-reflector cluster-id 10.0.0.1

# Add iBGP neighbors
set / network-instance default protocols bgp neighbor 10.0.0.2 peer-group IBGP
set / network-instance default protocols bgp neighbor 10.0.0.3 peer-group IBGP

# eBGP group (fabric underlay or peering)
set / network-instance default protocols bgp group EBGP
set / network-instance default protocols bgp group EBGP admin-state enable
set / network-instance default protocols bgp group EBGP family ipv4-unicast admin-state enable
set / network-instance default protocols bgp group EBGP export-policy EXPORT-LOOPBACKS
set / network-instance default protocols bgp group EBGP import-policy IMPORT-ALL

# eBGP neighbor with explicit ASN
set / network-instance default protocols bgp neighbor 192.0.2.2
set / network-instance default protocols bgp neighbor 192.0.2.2 peer-as 65001
set / network-instance default protocols bgp neighbor 192.0.2.2 peer-group EBGP

# BFD for BGP
set / network-instance default protocols bgp neighbor 192.0.2.2 \
    failure-detection enable-bfd true
set / network-instance default protocols bgp neighbor 192.0.2.2 \
    failure-detection fast-failover true

# MD5 authentication
set / network-instance default protocols bgp neighbor 192.0.2.2 \
    authentication keychain BGP-AUTH

# ADDPATH
set / network-instance default protocols bgp group IBGP \
    add-paths ipv4-unicast send true
set / network-instance default protocols bgp group IBGP \
    add-paths ipv4-unicast receive true

# EVPN overlay BGP (typically iBGP between spines and leaves)
set / network-instance default protocols bgp group EVPN-OVERLAY
set / network-instance default protocols bgp group EVPN-OVERLAY peer-as 65000
set / network-instance default protocols bgp group EVPN-OVERLAY family evpn admin-state enable
set / network-instance default protocols bgp group EVPN-OVERLAY \
    transport local-address 10.0.0.1
```

### Routing Policy

SR Linux routing policy uses a match/action framework under `/routing-policy`:

```
# Prefix set
set / routing-policy prefix-set PS-LOOPBACKS prefix 10.0.0.0/24 mask-length-range exact

# Policy to accept loopbacks
set / routing-policy policy EXPORT-LOOPBACKS
set / routing-policy policy EXPORT-LOOPBACKS statement 10 match prefix-set PS-LOOPBACKS
set / routing-policy policy EXPORT-LOOPBACKS statement 10 action accept

# Reject all (default deny)
set / routing-policy policy REJECT-ALL default-action reject

# Set communities
set / routing-policy policy EXPORT-WITH-COMM statement 10 action bgp-communities add "65000:100"
set / routing-policy policy EXPORT-WITH-COMM statement 10 action accept

# Set local preference on import
set / routing-policy policy SET-LOCALPREF statement 10 match bgp-community "65000:200"
set / routing-policy policy SET-LOCALPREF statement 10 action bgp local-pref 200
set / routing-policy policy SET-LOCALPREF statement 10 action accept

# Apply to BGP
set / network-instance default protocols bgp neighbor 192.0.2.2 export-policy EXPORT-LOOPBACKS
set / network-instance default protocols bgp neighbor 192.0.2.2 import-policy REJECT-ALL
```

---

## 9. MPLS Commands

MPLS support in SR Linux is **platform-dependent**. On 7220 IXR platforms (Trident4, Tomahawk4 merchant silicon), MPLS forwarding is not supported — these chips are designed for DC switching and VXLAN, not label switching. Full MPLS is available on the 7250 IXR-e and 7730 SXR platforms, which use Nokia FP4/FP5 forwarding processors on WAN/routing line cards.

> See [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/) for per-platform MPLS capability and buffer details.

### Show Commands (FP-based Platforms)

```
# LDP
show network-instance default protocols ldp neighbor
show network-instance default protocols ldp session
show network-instance default protocols ldp interface
show network-instance default protocols ldp bindings

# MPLS forwarding table
show network-instance default tunnel-table mpls
show network-instance default tunnel-table mpls detail

# Segment Routing
show network-instance default protocols isis segment-routing prefix-segments
show network-instance default protocols ospf segment-routing prefix-segments
show network-instance default protocols sr-policy
show network-instance default tunnel-table sr detail
```

### Configuration Examples (FP-based Platforms)

```
# Enable MPLS on interface
set / interface ethernet-1/1 subinterface 1 mpls admin-state enable

# LDP
set / network-instance default protocols ldp admin-state enable
set / network-instance default protocols ldp transport-preference ipv4
set / network-instance default protocols ldp interface ethernet-1/1.1 admin-state enable

# SR-MPLS with IS-IS (requires FP4/FP5)
set / network-instance default protocols isis instance CORE \
    segment-routing mpls admin-state enable
set / network-instance default protocols isis instance CORE \
    segment-routing mpls srgb start-label 16000 end-label 24000
set / interface system0 subinterface 0 isis ipv4-node-sid index 1

# SR policy (traffic steering)
set / network-instance default protocols sr-policy admin-state enable
set / network-instance default protocols sr-policy policy SR-POLICY-1
set / network-instance default protocols sr-policy policy SR-POLICY-1 \
    color 100 endpoint 10.0.0.2
set / network-instance default protocols sr-policy policy SR-POLICY-1 \
    candidate-path preference 100 explicit segment-list 1
```

---

## 10. IPv6 Commands

### IPv6 Interface Show Commands

```
show interface | grep -A5 "ethernet-1/1"      # includes IPv6 if configured
info from state interface ethernet-1/1 subinterface 1 ipv6

# NDP neighbor table
show network-instance default ipv6 nd-table
show network-instance default ipv6 nd-table interface ethernet-1/1.1
```

### IPv6 Routing Table

```
show network-instance default route-table ipv6-unicast
show network-instance default route-table ipv6-unicast summary
show network-instance default route-table ipv6-unicast | grep bgp
show network-instance default route-table ipv6-unicast | grep isis
show network-instance default route-table ipv6-unicast prefix 2001:db8::/32 detail
show network-instance default route-table ipv6-unicast prefix ::/0 detail
```

### IPv6 Ping and Traceroute

```
ping network-instance default 2001:db8::1
ping network-instance default 2001:db8::1 count 5
ping network-instance default 2001:db8::1 source 2001:db8:1::1
ping network-instance CUST-A 2001:db8::1

traceroute network-instance default 2001:db8::1
traceroute network-instance default 2001:db8::1 source 2001:db8:1::1
```

### OSPFv3 (IPv6)

```
show network-instance default protocols ospf3 neighbor
show network-instance default protocols ospf3 interface
show network-instance default protocols ospf3 database
show network-instance default route-table ipv6-unicast | grep ospf
```

### IS-IS with IPv6

IS-IS natively supports both IPv4 and IPv6 topology in SR Linux. Enable multi-topology for independent metric control:

```
# Multi-topology IPv6 in IS-IS
set / network-instance default protocols isis instance CORE \
    ipv6-unicast-routing multi-topology

# Per-interface IPv6 metric
set / network-instance default protocols isis instance CORE \
    interface ethernet-1/1.1 level 2 ipv6-unicast-metric 10
```

### BGP for IPv6

```
show network-instance default protocols bgp routes ipv6-unicast summary
show network-instance default protocols bgp routes ipv6-unicast prefix 2001:db8:100::/48
show network-instance default protocols bgp neighbor 2001:db8::2 received-routes ipv6
show network-instance default protocols bgp neighbor 2001:db8::2 advertised-routes ipv6
```

**BGP IPv6 Configuration:**

```
# Enable IPv6 address family in BGP group
set / network-instance default protocols bgp group EBGP-V6
set / network-instance default protocols bgp group EBGP-V6 admin-state enable
set / network-instance default protocols bgp group EBGP-V6 family ipv6-unicast admin-state enable

# IPv6 neighbor
set / network-instance default protocols bgp neighbor 2001:db8::2
set / network-instance default protocols bgp neighbor 2001:db8::2 peer-as 65001
set / network-instance default protocols bgp neighbor 2001:db8::2 peer-group EBGP-V6

# Dual-stack (same group, both families)
set / network-instance default protocols bgp group DUAL-STACK
set / network-instance default protocols bgp group DUAL-STACK family ipv4-unicast admin-state enable
set / network-instance default protocols bgp group DUAL-STACK family ipv6-unicast admin-state enable
```

### IPv6 Configuration Reference

```
# Dual-stack subinterface
set / interface ethernet-1/1 subinterface 1 ipv4 address 192.0.2.1/30
set / interface ethernet-1/1 subinterface 1 ipv6 address 2001:db8:1::1/64

# System loopback IPv6
set / interface system0 subinterface 0 ipv6 address 2001:db8:0:1::1/128

# Static IPv6 routes
set / network-instance default next-hop-groups nhg-v6 nexthop 1 ip-address 2001:db8:1::2
set / network-instance default static-routes route ::/0 next-hop-group nhg-v6
set / network-instance default static-routes route 2001:db8:100::/48 next-hop-group nhg-v6

# IPv6 multipath
set / network-instance default protocols bgp group IBGP add-paths ipv6-unicast send true
```

### IPv6 ACL

```
# IPv6 ACL filter
set / acl ipv6-filter IPV6-FILTER entry 10 match next-header icmpv6
set / acl ipv6-filter IPV6-FILTER entry 10 action accept
set / acl ipv6-filter IPV6-FILTER entry 20 match source-ip prefix 2001:db8::/32
set / acl ipv6-filter IPV6-FILTER entry 20 action drop
set / acl ipv6-filter IPV6-FILTER entry 9999 action accept

# Apply to interface subinterface
set / interface ethernet-1/1 subinterface 1 acl input ipv6-filter IPV6-FILTER
```

---

## 11. Configuration Management

### Viewing Configuration

```
# From running mode
info                                      # config at current path (hierarchical)
info flat                                 # flat absolute paths
info detail                               # include all fields and defaults
info | grep <pattern>                     # filtered view

# From state mode — operational data
info from state                           # state at current path
info from state flat                      # state as flat paths
info from state | grep "oper-state"       # filter state output

# Diff candidate vs running (from candidate mode)
diff                                      # show pending changes
diff flat                                 # pending changes as flat paths
```

### Commit Operations

```
# Enter candidate mode
enter candidate

# Make changes...
set / interface ethernet-1/1 description "Updated"

# Inspect pending changes
diff

# Apply changes
commit now                                # immediate commit
commit confirm 300                        # commit; auto-revert in 300 seconds
commit confirm 300 persist                # commit confirmed that survives reboot
commit confirmed-accept                   # confirm a 'commit confirm' before timer expires
commit stay                               # commit and remain in candidate mode

# Validate without committing
validate

# Discard changes
discard now                               # discard all changes immediately
discard stay                              # discard but remain in candidate mode
```

### Rollback and History

SR Linux maintains a history of committed configurations (rollback checkpoints):

```
show system configuration checkpoint      # list available checkpoints
show system configuration checkpoint 1 diff  # diff checkpoint 1 vs current running

# Rollback to a checkpoint
tools system configuration checkpoint 1 restore

# Create a named checkpoint
tools system configuration checkpoint save name pre-maintenance
```

### Saving Configuration

SR Linux automatically persists committed configuration to the startup datastore. No explicit `write memory` or `admin save` is needed. You can also explicitly manage startup:

```
tools system configuration save           # explicitly save to startup
tools system configuration load           # load from startup (emergency restore)

# Export config to file
info flat | as-json > /tmp/config-backup.json
info flat > /tmp/config-backup.txt

# Push config from file (via gNMI or CLI paste)
# Import via paste in candidate mode or via gNMI set
```

### Checkpoints and Rollback

```
# Create checkpoint before risky change
tools system configuration checkpoint save name pre-bgp-change

# List checkpoints
show system configuration checkpoint

# Compare current running with a checkpoint
show system configuration checkpoint pre-bgp-change diff

# Restore from checkpoint
tools system configuration checkpoint pre-bgp-change restore
commit now
```

### gNMI — Programmatic Configuration

SR Linux's gNMI server is a first-class management interface. Every CLI path corresponds to a gNMI path:

```bash
# Using gnmic (open-source gNMI client) from bash
gnmic -a 192.0.2.1:57400 -u admin -p admin \
    get --path /interface[name=ethernet-1/1]

gnmic -a 192.0.2.1:57400 -u admin -p admin \
    set --update /interface[name=ethernet-1/1]/description:::string:"New description"

# Subscribe to interface counters via streaming telemetry
gnmic -a 192.0.2.1:57400 -u admin -p admin \
    subscribe --path /interface[name=ethernet-1/1]/statistics --mode stream
```

The JSON-RPC API is also available on port 80/443:

```bash
curl -X POST https://192.0.2.1/jsonrpc -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","id":1,"method":"get","params":{"commands":[{"action":"get","path":"/interface[name=ethernet-1/1]"}]}}'
```

---

## 12. Platform & Silicon Details

SR Linux is Nokia's cloud-native NOS and is designed around merchant silicon for the 7220 IXR family, with Nokia FP4/FP5 available on the 7250 IXR-e and 7730 SXR for WAN/routing use cases. This is the inverse emphasis of SR OS, which is FP-first with merchant silicon as an option on IXR variants.

For detailed per-chipset buffer sizing, TCAM allocation, and VOQ behavior: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

### Silicon Overview

| ASIC | Vendor | Type | Buffer | MPLS | Primary Use in SR Linux |
|---|---|---|---|---|---|
| Trident4 | Broadcom | Merchant | Shallow on-chip | No | 7220 IXR-D leaf switching |
| Tomahawk4 | Broadcom | Merchant | Shallow on-chip | No | 7220 IXR-H spine fabric |
| Jericho2c+ | Broadcom | Merchant | Deep HBM | Full | 7250 IXR-e WAN/routing |
| FP4 | Nokia | Proprietary | Deep VOQ | Full | 7250 IXR-e / 7730 SXR |
| FP5 | Nokia | Proprietary | Deep VOQ | Full | 7730 SXR (newer variants) |

### Platform Hardware Overview

| Platform | Role | ASIC | Key Interfaces | SR Linux Feature Notes |
|---|---|---|---|---|
| 7220 IXR-D2 | DC leaf | Trident4 | 32×100G QSFP28 | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-D2L | DC leaf (large) | Trident4 | 48×25G + 8×100G | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-D3 | DC leaf | Trident4 | 48×25G SFP28 + 8×100G | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-D3L | DC leaf (large) | Trident4 | 60×25G + 4×100G | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-D4 | DC leaf | Trident4 | 32×400G | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-H2 | DC spine | Tomahawk4 | 32×400G QSFP-DD | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-H3 | DC spine (dense) | Tomahawk4 | 64×200G | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7250 IXR-6e | IP/MPLS routing | FP4 + Jericho2c+ | 6-slot modular, 400G | Full MPLS, SR-MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7250 IXR-10e | IP/MPLS routing | FP4 + Jericho2c+ | 10-slot modular, 400G | Full MPLS, SR-MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7730 SXR-1d-32D | Core routing | FP5 | 32×400G ZR/ZR+ | Coherent optics, full MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| cSRL | Container | Software | Virtual (x86) | All software features, no hardware offload |

### Feature Matrix by Platform

| Feature | 7220 IXR-D (Trident4) | 7220 IXR-H (Tomahawk4) | 7250 IXR-e (FP4) | 7730 SXR (FP5) |
|---|---|---|---|---|
| L3 routing (OSPF/IS-IS/BGP) | Yes | Yes | Yes | Yes |
| EVPN / VXLAN | Yes | Yes | Yes | Yes |
| MPLS / LDP | No | No | Full | Full |
| SR-MPLS | No | No | Full | Full |
| SRv6 | No | No | Yes | Yes |
| L3VPN (ip-vrf over MPLS) | IP-only | IP-only | Full MPLS | Full MPLS |
| gNMI / gRIBI / gNOI | Yes | Yes | Yes | Yes |
| NDK (custom agents) | Yes | Yes | Yes | Yes |
| PTP / IEEE 1588v2 | Limited | No | BC support | BC + GM |
| SyncE | Limited | No | Yes | Yes |
| Buffer depth | Shallow | Shallow | Deep (HBM/VOQ) | Deep (VOQ) |
| Coherent optics (ZR/ZR+) | No | No | No | Yes (7730 SXR) |
| External TCAM (eTCAM) | No | No | Yes | Yes |
| ACL scale | Moderate | Moderate | Large | Large |

### Merchant Silicon Deep Dive — 7220 IXR

The 7220 IXR-D series uses **Broadcom Trident4**, and the 7220 IXR-H series uses **Broadcom Tomahawk4**. These are the same ASICs used in Arista 7050X4/7060X5 platforms and many other DC switches. Key implications for SR Linux deployments:

- **No MPLS forwarding**: Trident4 and Tomahawk4 do not support label switching. Any MPLS requirement (including VXLAN over SR-MPLS) must be addressed with a different platform.
- **Shallow buffers**: On-chip buffers are limited to tens of MB total across all ports. This is sufficient for DC spine/leaf with consistent traffic patterns but problematic for bursty WAN traffic or high-RTT workloads. See [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/) for exact sizing.
- **TCAM scale**: On-chip TCAM limits ACL and routing table size. Route scale is typically handled through hardware ECMP and careful summarization.
- **VXLAN VTEP**: Both Trident4 and Tomahawk4 support hardware VXLAN encapsulation/decapsulation. EVPN/VXLAN is the primary L2VPN technology on these platforms.

### Nokia FP4/FP5 — 7250 IXR-e and 7730 SXR

When SR Linux runs on FP-based hardware (7250 IXR-e, 7730 SXR), the full MPLS and routing feature set becomes available:

- **Deep distributed buffers** with VOQ architecture (same as SR OS platforms)
- **Full MPLS**: LDP, SR-MPLS, SRv6, RSVP-TE (on SR OS; SR Linux has subset)
- **External TCAM (eTCAM)**: Large routing table scale (millions of entries)
- **Coherent optics**: The 7730 SXR-1d-32D supports 400ZR/OpenROADM coherent optics directly in QSFP-DD ports
- **Timing**: PTP Boundary Clock, SyncE on applicable platforms

For per-platform VOQ queue count, buffer sizing, and scheduling details: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

### cSRL — Containerized SR Linux

Nokia distributes SR Linux as a container image (`ghcr.io/nokia/srlinux`) that runs on standard x86 Linux. cSRL is functionally equivalent to hardware SR Linux for all control-plane and management features, with no hardware dataplane.

```bash
# Pull and run cSRL (requires Docker/containerlab)
docker pull ghcr.io/nokia/srlinux:latest

# Typical deployment via containerlab
# (see containerlab.dev for topology files and lab examples)
```

cSRL is widely used for:
- CI/CD pipeline testing of network configurations
- Protocol compatibility testing (BGP, OSPF, IS-IS, EVPN)
- NDK application development
- Learning and certification preparation

### Chassis and Hardware Commands

```
show platform                              # overall platform status
show platform chassis                      # chassis model, serial, temperature
show platform linecard                     # line card inventory (modular systems)
show platform environment                  # temperature, fans, power supplies
show platform environment temperature
show platform environment power
show interface ethernet-1/1 transceiver   # DOM: Rx/Tx power, temperature, voltage
show system information                    # hostname, version, uptime
show version                              # SR Linux version, build info
show system resource-monitor              # CPU, memory utilization
info from state platform                  # full platform state via YANG
```

### QoS and Buffer Management

SR Linux exposes QoS configuration through the `/qos` YANG model. As with all merchant silicon platforms, the actual buffer and scheduling capabilities are ASIC-determined:

```
# Show QoS state
show qos
show qos interface ethernet-1/1
info from state qos interface ethernet-1/1

# Interface queue statistics
info from state interface ethernet-1/1 subinterface 1 statistics
```

**QoS Configuration (Trident4/Tomahawk4):**

```
# DSCP-to-forwarding-class mapping
set / qos dscp-policy default entry 46 forwarding-class ef drop-probability low
set / qos dscp-policy default entry 34 forwarding-class af4 drop-probability low
set / qos dscp-policy default entry 0 forwarding-class be drop-probability low

# Forwarding class to queue mapping
set / qos forwarding-class ef output queue 7
set / qos forwarding-class af4 output queue 4
set / qos forwarding-class be output queue 0

# Scheduler profile
set / qos scheduler-policy CORE-SCHED tier 1 node ef weight 30
set / qos scheduler-policy CORE-SCHED tier 1 node be weight 70

# Apply to interface
set / interface ethernet-1/1 qos input dscp-policy default
set / interface ethernet-1/1 qos output scheduler-policy CORE-SCHED
```

For queue depth and buffer allocation per forwarding class by ASIC: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

### SR Linux Logging and Telemetry

```
# CLI log viewer
show log
show log | tail 50
show log | grep -i bgp
show log | grep -i error

# Streaming telemetry (gNMI subscribe) — from bash
gnmic -a 127.0.0.1:57400 -u admin -p admin \
    subscribe --path /interface[name=ethernet-1/1]/statistics \
    --mode stream --stream-mode sample --sample-interval 10s

# gNOI — operational actions over gRPC
gnoi system Ping --destination 10.0.0.2 --count 5
gnoi system Traceroute --destination 10.0.0.2
```

---

## 13. Cross-Platform Command Reference

### General & Interface Commands

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|---|
| Show interfaces | `show interface` | `show router interface` | `show interfaces terse` | `show interfaces status` |
| Interface detail | `show interface ethernet-1/1 detail` | `show router interface "to-peer" detail` | `show interfaces ge-0/0/0` | `show interfaces Ethernet1` |
| Interface counters | `info from state interface ethernet-1/1 statistics` | `show port 1/1/1 statistics` | `show interfaces statistics` | `show interfaces Ethernet1 counters` |
| Show MAC table | `show network-instance mac-vrf-100 bridge-table mac-table all` | `show service id 100 fdb` | `show ethernet-switching table` | `show mac address-table` |
| Disable interface | `set / interface ethernet-1/1 admin-state disable` + `commit now` | `/configure port 1/1/1 admin-state disable` | `set interfaces ge-0/0/0 disable` | `shutdown` |
| Show running config | `info flat` | `info flat` | `show configuration` | `show running-config` |
| Config context | path navigation (e.g. `/ network-instance default`) | path navigation | `edit protocols ospf` | `configure terminal` |
| Enter config mode | `enter candidate` | `edit-config exclusive` | `configure exclusive` | `configure terminal` |
| Apply config | `commit now` | `commit` + `admin save` | `commit` | `write memory` |
| Config diff | `diff` (in candidate mode) | `compare` | `show config \| compare` | `show running-config diff` |
| Config rollback | `tools system configuration checkpoint X restore` | `tools rollback revert 1` | `rollback 1` + `commit` | `configure replace checkpoint:X` |
| Validate config | `validate` | `validate` | `commit check` | `configure session` + diffs |
| JSON output | `show interface \| as-json` | `show router interface \| as-json` | `show interfaces \| display json` | `show interfaces \| json` |
| Flat config format | `info flat` | `info flat` | `show config \| display set` | `show running-config \| section X` |

### Routing Protocol — OSPF

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|---|
| OSPF neighbors | `show network-instance default protocols ospf neighbor` | `show router ospf neighbor` | `show ospf neighbor` | `show ip ospf neighbor` |
| OSPF neighbor detail | `show ... ospf neighbor detail` | `show router ospf neighbor detail` | `show ospf neighbor detail` | `show ip ospf neighbor detail` |
| OSPF interfaces | `show ... ospf interface` | `show router ospf interface` | `show ospf interface` | `show ip ospf interface` |
| OSPF LSDB | `show ... ospf database` | `show router ospf database` | `show ospf database` | `show ip ospf database` |
| OSPF routes | `show network-instance default route-table \| grep ospf` | `show router route-table protocol ospf` | `show route protocol ospf` | `show ip route ospf` |
| OSPFv3 neighbors | `show ... ospf3 neighbor` | `show router ospf3 neighbor` | `show ospf3 neighbor` | `show ipv6 ospf neighbor` |

### Routing Protocol — IS-IS

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | RouterOS 7 |
|---|---|---|---|---|
| IS-IS adjacencies | `show network-instance default protocols isis adjacency` | `show router isis adjacency` | `show isis adjacency` | Not supported |
| IS-IS adjacency detail | `show ... isis adjacency detail` | `show router isis adjacency detail` | `show isis adjacency detail` | Not supported |
| IS-IS database | `show ... isis database` | `show router isis database` | `show isis database` | Not supported |
| IS-IS database detail | `show ... isis database detail` | `show router isis database detail` | `show isis database detail` | Not supported |
| IS-IS routes | `show network-instance default route-table \| grep isis` | `show router route-table protocol isis` | `show route protocol isis` | Not supported |
| IS-IS overview | `show network-instance default protocols isis` | `show router isis overview` | `show isis overview` | Not supported |

### Routing Protocol — BGP

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|---|
| BGP summary | `show network-instance default protocols bgp summary` | `show router bgp summary` | `show bgp summary` | `show bgp summary` |
| BGP neighbors | `show ... bgp neighbor` | `show router bgp neighbor` | `show bgp neighbor` | `show bgp neighbors` |
| BGP neighbor detail | `show ... bgp neighbor 10.0.0.2 detail` | `show router bgp neighbor 10.0.0.2` | `show bgp neighbor 10.0.0.2` | `show bgp neighbors 10.0.0.2` |
| BGP routes | `show ... bgp routes ipv4-unicast summary` | `show router bgp routes ipv4` | `show route protocol bgp` | `show bgp ipv4 unicast` |
| BGP route detail | `show ... bgp routes ipv4-unicast prefix 10.0.0.0/8` | `show router bgp routes 10.0.0.0/8 detail` | `show route 10/8 detail` | `show bgp ipv4 unicast 10.0.0.0/8` |
| EVPN routes | `show ... bgp routes evpn summary` | `show router bgp routes evpn` | `show route table bgp.evpn.0` | `show bgp evpn` |
| VRF routes | `show network-instance CUST-A route-table` | `show router 100 route-table` | `show route table CUST-A.inet.0` | `show ip route vrf CUST-A` |

### MPLS

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|---|
| LDP neighbors | `show network-instance default protocols ldp neighbor` | `show router ldp neighbor` | `show ldp neighbor` | `show mpls ldp neighbor` |
| MPLS label table | `show network-instance default tunnel-table mpls` | `show router tunnel-table` | `show route table mpls.0` | `show mpls lfib route` |
| SR prefix SIDs | `show ... protocols isis segment-routing prefix-segments` | `show router isis segment-routing prefix-sids` | `show isis source-packet-routing node-segment` | `show isis segment-routing prefix-segments` |
| Note | 7220 IXR: No MPLS | 7750 SR: Full MPLS | MX/ACX: Full MPLS | 7280R: Full MPLS |

### L2 / VLANs / EVPN

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|---|
| L2 network instances | `show network-instance` (type mac-vrf) | `show service vpls` | `show route instance` | `show vxlan vtep` |
| MAC table | `show network-instance mac-vrf-100 bridge-table mac-table all` | `show service id 100 fdb` | `show ethernet-switching table` | `show mac address-table` |
| VTEP table | `show network-instance default tunnel-table all` | `show service id 100 vxlan` | `show evpn instance` | `show vxlan vtep` |
| EVPN BGP type-2 | `show ... bgp routes evpn route-type 2` | `show service id 100 evpn routes` | `show route table bgp.evpn.0 \| match "Type 2"` | `show bgp evpn route-type mac-ip` |
| EVPN BGP type-5 | `show ... bgp routes evpn route-type 5` | `show bgp routes evpn \| grep type-5` | `show route table bgp.evpn.0 \| match "Type 5"` | `show bgp evpn route-type ip-prefix` |

### System & Diagnostics

| Function | SR Linux | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|---|
| Ping | `ping network-instance default 8.8.8.8 count 5` | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 repeat 5` |
| Traceroute | `traceroute network-instance default 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` |
| Show ARP | `show network-instance default arp-table` | `show router arp` | `show arp` | `show arp` |
| Show routes | `show network-instance default route-table` | `show router route-table` | `show route` | `show ip route` |
| Disable paging | `environment more false` | `environment more false` | `set cli screen-length 0` | `terminal length 0` |
| Show version | `show version` | `show version` | `show version` | `show version` |
| Show hardware | `show platform chassis` | `show chassis detail` | `show chassis hardware` | `show inventory` |
| Logs | `show log` | `show log 99` | `show log messages` | `show logging` |
| Live log | `show log \| tail 50` + gNMI subscribe | `show log 99 \| tail` | `monitor start messages` | `bash tail -f /var/log/messages` |
| CPU/memory | `show system resource-monitor` | `show system cpu` | `show chassis routing-engine` | `show processes top` |
| Reboot | `tools system reboot` | `admin reboot` | `request system reboot` | `reload` |
| Save config | Auto-persisted on commit | `commit` + `admin save` | `commit` | `write memory` |
| Match/grep | `show ... \| grep <pattern>` | `show ... \| match <pattern>` | `show ... \| match <regex>` | `show ... \| include <regex>` |
| JSON output | `show ... \| as-json` | `show ... \| as-json` | `show ... \| display json` | `show ... \| json` |
| gNMI native | Yes (port 57400) | Via SR OS gNMI | Via Junos Telemetry Interface | Via gNMI extension |

---

## 14. Quick Reference Card

### Top 20 Daily-Driver Commands

```bash
# System health
show version                              # SR Linux version, build, platform
show platform chassis                     # hardware, temperature, fans
show system resource-monitor             # CPU, memory
show log | tail 50                        # recent syslog

# Interfaces
show interface                            # all interfaces, one line each
show interface ethernet-1/1 detail        # full interface detail with counters
show system lldp neighbor                 # discovered neighbors (like CDP)

# Routing
show network-instance default route-table ipv4-unicast          # IPv4 RIB
show network-instance default route-table ipv4-unicast summary  # count by protocol
show network-instance default route-table ipv4-unicast | grep bgp  # BGP routes
show network-instance default arp-table                          # ARP table

# BGP / OSPF / IS-IS
show network-instance default protocols bgp summary             # BGP peer state
show network-instance default protocols bgp neighbor            # neighbor detail
show network-instance default protocols ospf neighbor           # OSPF adjacencies
show network-instance default protocols isis adjacency          # IS-IS adjacencies

# EVPN/VXLAN
show network-instance default protocols bgp routes evpn summary # EVPN route types
show network-instance mac-vrf-100 bridge-table mac-table all    # MAC/IP table

# Config workflow
info flat                                 # running config as flat paths
enter candidate                           # open candidate for editing
diff                                      # show pending changes before commit
commit now                                # apply changes
```

### Useful One-Liners

```bash
# Count routes by protocol
show network-instance default route-table ipv4-unicast summary | grep -v "^$"

# Show only established BGP sessions
show network-instance default protocols bgp neighbor | grep -i "established"

# Find BGP sessions NOT established
show network-instance default protocols bgp neighbor | grep -v "established"

# Show OSPF neighbors not in Full state
show network-instance default protocols ospf neighbor | grep -v "Full"

# Find a specific IP anywhere in the flat config
info flat | grep "192.0.2.1"

# Show all interfaces that are admin-up but operationally down
show interface | grep "enable" | grep -v "up.*up" | grep -v mgmt

# Check all EVPN MAC-VRF bridge-table statistics
show network-instance | grep mac-vrf | grep -o "name [^ ]*" | while read n; do
    show network-instance $n bridge-table statistics
done

# Operational state for all BGP neighbors as JSON (for automation)
info from state network-instance default protocols bgp neighbor | as-json

# Watch interface counters refresh every 10 seconds via gNMI
gnmic -a 127.0.0.1:57400 subscribe \
    --path '/interface[name=ethernet-1/1]/statistics' \
    --mode stream --sample-interval 10s

# Diff current candidate vs running before committing
diff flat

# Show IS-IS SR prefix SIDs for node SID verification
show network-instance default protocols isis segment-routing prefix-segments | grep "node"

# Verify VXLAN tunnels are resolved
show network-instance default tunnel-table all | grep -v "unresolved"
```

### SR Linux Mental Models

| Concept | SR Linux Way | Notes |
|---|---|---|
| Three datastores | `running` / `candidate` / `state` | `state` is operational, not config — unique to SR Linux |
| `info flat` = `display set` | Flat absolute YANG paths | Primary tool for config documentation and diffs |
| `info from state` | Operational data via YANG tree | Same tree as config — powerful for comparison |
| Network instance | `network-instance default`, `ip-vrf`, `mac-vrf` | Unified model: replaces VRF + VPLS + routing-instance |
| MAC-VRF | L2 broadcast domain for EVPN | Each VXLAN VNI / EVPN EVI maps to one mac-vrf |
| Interface + subinterface + binding | Three-step model | Subinterface must be bound to a network-instance |
| `commit now` vs `commit confirm` | Immediate vs auto-revert | Use `commit confirm 300` for risky remote changes |
| YANG is canonical | CLI = gNMI = JSON-RPC = same model | Every CLI path is a gNMI path |
| NDK | Custom agents as first-class citizens | Custom apps subscribe to IDB, not an afterthought |
| MPLS requires FP silicon | 7220 IXR: no MPLS | Trident4/Tomahawk4 do not label-switch |
| Merchant silicon implies shallow buffers | 7220 IXR: on-chip shared buffer | See [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| cSRL for development | Full control-plane, no hardware | Use containerlab for multi-node topologies |
| `bash` always available | Standard Debian under the hood | `ip`, `ss`, `tcpdump`, `python3` all work |
| Auto-persistent commits | No `write memory` needed | Committed config is automatically the startup config |
| gNMI streaming telemetry | Native, same YANG tree | No separate telemetry daemon — gNMI server is core SR Linux |

---

*Curriculum version: 1.0 | Target: Nokia SR Linux — 7220 IXR-D/H / 7250 IXR-e / 7730 SXR / cSRL platforms*
*Reference platforms for comparison: Nokia SR OS MD-CLI, Juniper JunOS MX/ACX, Arista EOS, MikroTik RouterOS 7*
*Platform buffer and silicon details: [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)*

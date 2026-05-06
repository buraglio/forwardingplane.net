---
title: Arista EOS Basics
date: 2026-05-05
author: Nick Buraglio
layout: page
---

# Arista EOS Basics

A practical curriculum for network engineers learning Arista EOS, with emphasis on operational commands, usability features, and cross-platform translation from JunOS, IOS-XR, and IOS-XE. Covers the implications of merchant silicon and provides chipset-specific buffer references.

---

## Table of Contents

1. [EOS Fundamentals](#1-eos-fundamentals)
2. [CLI Navigation & Usability](#2-cli-navigation--usability)
3. [Pipe Commands & Output Filtering](#3-pipe-commands--output-filtering)
4. [Interface Commands](#4-interface-commands)
5. [VLAN Commands](#5-vlan-commands)
6. [OSPF Commands](#6-ospf-commands)
7. [ISIS Commands](#7-isis-commands)
8. [BGP Commands](#8-bgp-commands)
9. [MPLS Commands](#9-mpls-commands)
10. [IPv6 Commands](#10-ipv6-commands)
11. [Configuration Management](#11-configuration-management)
12. [Platform & Merchant Silicon Details](#12-platform--merchant-silicon-details)
13. [Cross-Platform Command Reference](#13-cross-platform-command-reference)
14. [Quick Reference Card](#14-quick-reference-card)

---

## 1. EOS Fundamentals

### Architecture Overview

Arista EOS (Extensible Operating System) runs on a standard Linux kernel (originally based on Fedora, now internally maintained). Unlike vertically integrated NOS platforms, EOS decouples the system into independent agent processes that communicate through a central in-memory database called **Sysdb** (System Database). This is a fundamental architectural difference from JunOS's RE/PFE separation model.

```
┌─────────────────────────────────────────────────┐
│                    Sysdb                        │  ← Central state store
│         (in-memory, replicated to flash)        │
└───────────────┬─────────────────────────────────┘
                │  All agents read/write Sysdb
    ┌───────────┼────────────────────────────────┐
    │           │                                │
  CLI        Routing agents              Hardware drivers
  (FastCLI)  (Bgpd, Ospfd, Isisd…)     (FwdAgent, AclAgent…)
```

The forwarding plane uses **merchant silicon** ASICs (Broadcom Trident, Tomahawk, Jericho families; Intel/Barefoot Tofino on the 7170 series). Because Arista does not design its own forwarding chips, the feature set and buffer characteristics are directly determined by the ASIC. This has important implications for buffer sizing, TCAM scale, and supported features — see [Section 12](#12-platform--merchant-silicon-details) and [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/) for chipset-specific details.

EOS shares the same "hypervisor + containerized OS" model described in comparable JunOS documentation. vEOS (virtual EOS), cEOS (containerized EOS), and cEOS-XR are all rooted in the same Linux base. This model is common across modern platforms including Cisco IOS-XR/XE on x86, Nokia SR OS, and whitebox NOSes like SONiC and Cumulus Linux.

### CLI Modes

```
localhost>          # User EXEC mode — limited show commands
localhost#          # Privileged EXEC mode — full show, copy, debug
localhost(config)#  # Global configuration mode
localhost(config-if-Et1)#  # Interface sub-mode
localhost(config-router-bgp)#  # Protocol sub-mode
```

| Action | Command |
|--------|---------|
| Enter privileged mode | `enable` |
| Enter configuration mode | `configure` or `configure terminal` |
| Enter configuration session | `configure session <name>` |
| Return to privileged mode from anywhere | `end` or `Ctrl+Z` |
| Go up one sub-mode level | `exit` |
| Run privileged command from config mode | `do show ...` |

### Configuration Modes

EOS supports two configuration paradigms:

- **Direct configuration** (default, IOS-style) — changes take effect immediately when entered in config mode
- **Configuration sessions** (optional, JunOS-like candidate config) — `configure session <name>` opens an isolated workspace; changes are only applied on `commit`

```
configure session PLANNED-CHANGE     # open isolated session
! make changes here — not yet active
show session-config diffs            # diff session vs running-config
commit                               # apply changes atomically
abort                                # discard session
```

---

## 2. CLI Navigation & Usability

### Tab Completion & Help

```
show route ?              # list all options at this level
show ip route <Tab>       # complete or list options
show ip b<Tab>            # completes to 'show ip bgp' if unambiguous
show interfaces Eth<Tab>  # completes to Ethernet interface names
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Complete command |
| `?` | Context-sensitive help |
| `Ctrl+A` | Move cursor to beginning of line |
| `Ctrl+E` | Move cursor to end of line |
| `Ctrl+U` | Delete from cursor to beginning of line |
| `Ctrl+K` | Delete from cursor to end of line |
| `Ctrl+W` | Delete previous word |
| `Ctrl+R` | Reverse search command history |
| `Ctrl+C` | Abort current command |
| `Ctrl+D` | Exit CLI (if line is empty) |
| `Ctrl+Z` | Return to privileged EXEC mode |
| `Ctrl+L` | Redraw screen |
| Up/Down arrows | Navigate command history |

### Navigation Within Config Mode

```
interface Ethernet1              # descend into interface sub-mode
exit                             # go up one level
end                              # return to privileged EXEC mode
show running-config              # show full active config
show running-config interfaces   # show interface section only
show running-config | section bgp
```

### Abbreviations

EOS supports unambiguous abbreviations:

```
sh ip ro                  # show ip route
sh int st                 # show interfaces status
sh bgp sum                # show bgp summary
conf t                    # configure terminal
wr                        # write memory (save config)
```

### Operational History & Display Settings

```
show history              # recent command history
terminal length 0         # disable pagination (like 'set cli screen-length 0')
terminal length 24        # restore default pagination
terminal width 250        # wider output
```

---

## 3. Pipe Commands & Output Filtering

EOS pipe filtering uses a Unix-style syntax. Pipe commands can be chained.

### Core Pipe Commands

| Pipe Command | Description | Example |
|---|---|---|
| `include <regex>` | Show lines matching pattern (grep) | `show ip route \| include 10.0` |
| `exclude <regex>` | Exclude lines matching pattern | `show bgp summary \| exclude Idle` |
| `grep <regex>` | Same as include | `show ip route \| grep 10.0` |
| `grep -v <regex>` | Same as exclude | `show bgp summary \| grep -v Idle` |
| `begin <regex>` | Start output at first matching line | `show running-config \| begin router bgp` |
| `section <regex>` | Show config sections matching regex | `show running-config \| section ospf` |
| `head <n>` | Show first N lines | `show ip route \| head 20` |
| `tail <n>` | Show last N lines | `show logging \| tail 50` |
| `count` | Count lines | `show ip route \| count` |
| `no-more` | Disable pagination for this command | `show ip route \| no-more` |
| `json` | Show output as JSON | `show ip route \| json` |
| `json native` | Show output as native JSON (more detail) | `show bgp summary \| json` |
| `awk '<program>'` | AWK processing | `show ip route \| awk '{print $1}'` |

### Chaining Pipes

```
show ip route | include 192.168 | count
show bgp summary | exclude "^$" | include "Estab|Peer"
show running-config | section bgp | include neighbor
show interfaces | include "Ethernet|connected" | exclude "Admin"
```

### The `section` Pipe — Most Useful for Config

`section` is the EOS equivalent of navigating a JunOS hierarchy — it extracts a full config block:

```
show running-config | section router ospf
show running-config | section interface Ethernet1$
show running-config | section router bgp
show running-config | section "ip prefix-list"
```

### JSON Output

EOS natively outputs most `show` commands as JSON for scripting and automation:

```
show ip route | json
show bgp summary | json
show interfaces Ethernet1 | json
show version | json
```

This integrates directly with eAPI (JSON-RPC over HTTP/HTTPS) and the EOS SDK.

### Watching Output Repeatedly

```
watch 2 show interfaces Ethernet1 counters    # refresh every 2 seconds
watch 1 show bgp summary                      # refresh every second (Ctrl+C to stop)
```

---

## 4. Interface Commands

### Show Commands

```
show interfaces                          # full detail, all interfaces
show interfaces status                   # one-line summary per interface (like 'terse')
show interfaces Ethernet1                # detail for specific interface
show interfaces Ethernet1 counters       # packet/byte/error counters
show interfaces Ethernet1 counters rates # rate-based counters (pps/bps)
show interfaces Ethernet1 transceiver   # optic/SFP detail
show ip interface brief                  # L3 interfaces with addresses
show interfaces description              # interface descriptions

# Port-Channel (LAG)
show interfaces Port-Channel1
show port-channel summary                # all LAGs, member state, LACP mode
show lacp interface Port-Channel1        # LACP PDU stats and state

# Optical / Transceiver
show interfaces Ethernet1 transceiver    # DOM: Rx/Tx power, temperature, voltage
show inventory                           # all hardware including transceivers
```

### Interface Status Output

```
show interfaces status
```
```
Port       Name         Status       Vlan    Duplex Speed   Type
Et1        To-Peer-Rtr  connected    routed  full   100G    100GBASE-SR4
Et2        Uplink       connected    1       full   10G     10GBASE-SR
Et3                     notconnect   1       auto   auto    Not Present
Ma1        Mgmt         connected    routed  full   1000    10/100/1000
```

### Configuration Examples

```
! Basic L3 interface
interface Ethernet1
   description To-Peer-Router
   no switchport
   ip address 192.0.2.1/30
   ipv6 address 2001:db8:1::1/64
   no shutdown

! Loopback
interface Loopback0
   ip address 10.0.0.1/32
   ipv6 address 2001:db8:0:1::1/128

! Shutdown interface
interface Ethernet1
   shutdown

! Interface naming conventions
! Ethernet1             — physical port 1 (fixed chassis)
! Ethernet1/1           — modular chassis: module 1, port 1
! Management1           — out-of-band management
! Loopback0             — loopback (no hardware)
! Port-Channel1         — link aggregation group (LAG)
! Vlan100               — SVI (switched virtual interface, L3 VLAN)
```

---

## 5. VLAN Commands

### Show Commands

```
show vlan                               # all VLANs, member ports
show vlan 100                           # specific VLAN detail
show vlan brief                         # condensed VLAN summary
show mac address-table                  # global MAC table
show mac address-table vlan 100         # MAC table for specific VLAN
show mac address-table interface Ethernet1
show mac address-table count            # total MAC entry count
show mac address-table aging-time       # aging timer

# Spanning Tree
show spanning-tree                      # STP instance summary
show spanning-tree vlan 100             # STP state for specific VLAN
show spanning-tree interface Ethernet1  # per-interface STP state
show spanning-tree detail               # full STP detail

# Interface VLAN membership
show interfaces Ethernet1 switchport    # access/trunk mode, VLANs
show interfaces trunk                   # all trunk ports and allowed VLANs
```

### VXLAN

```
show vxlan vtep                         # all known VTEPs
show vxlan vni                          # VNI to VLAN mapping
show vxlan address-table                # MAC/IP learned via VXLAN
show vxlan flood vtep                   # BUM flood list per VNI
show vxlan counters                     # per-VTEP/VNI packet counters
show interfaces Vxlan1                  # VXLAN interface state
```

### VLAN Configuration Examples

```
! Define VLANs
vlan 100
   name Production
vlan 200
   name Management

! Access port
interface Ethernet2
   switchport mode access
   switchport access vlan 100

! Trunk port
interface Ethernet3
   switchport mode trunk
   switchport trunk allowed vlan 100,200,300
   switchport trunk native vlan 1

! SVI (L3 gateway for VLAN — equivalent to JunOS IRB)
interface Vlan100
   ip address 10.100.0.1/24
   ipv6 address 2001:db8:100::1/64
   no shutdown

! VXLAN VTEP configuration
interface Vxlan1
   vxlan source-interface Loopback0
   vxlan udp-port 4789
   vxlan vlan 100 vni 10100
   vxlan vlan 200 vni 10200

! Q-in-Q (dot1q tunneling)
interface Ethernet4
   switchport mode dot1q-tunnel
```

---

## 6. OSPF Commands

### Show Commands

```
show ip ospf                             # OSPF process summary, router-id, areas
show ip ospf neighbor                    # neighbor adjacencies
show ip ospf neighbor detail             # detailed neighbor state
show ip ospf interface                   # per-interface OSPF state
show ip ospf interface brief             # condensed interface state
show ip ospf database                    # LSDB summary
show ip ospf database detail             # full LSDB
show ip ospf database router             # Router LSAs only
show ip ospf database network            # Network LSAs only
show ip ospf database summary            # Summary (Type-3) LSAs
show ip ospf database external           # External (Type-5) LSAs
show ip ospf database router detail      # Router LSAs with full TLVs
show ip ospf route                       # OSPF computed routes
show ip ospf traffic                     # packet and SPF counters
```

### Route Table Integration

```
show ip route ospf                       # OSPF routes in the RIB
show ip route 10.0.0.0/8 detail         # how a prefix was learned
show ip route ospf summary
```

### OSPFv3 (IPv6)

```
show ipv6 ospf neighbor
show ipv6 ospf interface
show ipv6 ospf database
show ipv6 ospf route
show ipv6 route ospf
```

### Configuration Examples

```
! Basic OSPF
router ospf 1
   router-id 10.0.0.1
   network 10.0.0.0/8 area 0.0.0.0
   passive-interface Loopback0
   auto-cost reference-bandwidth 100000    ! 100G reference

! Per-interface OSPF (preferred, more explicit)
interface Ethernet1
   ip ospf 1 area 0.0.0.0
   ip ospf cost 10
   ip ospf authentication message-digest
   ip ospf message-digest-key 1 md5 secretkey

interface Loopback0
   ip ospf 1 area 0.0.0.0
   ip ospf passive

! Area types
router ospf 1
   area 0.0.0.1 stub
   area 0.0.0.2 nssa

! Redistribute connected
router ospf 1
   redistribute connected route-map CONNECTED-TO-OSPF

ip prefix-list CONNECTED seq 10 permit 10.0.0.0/8 le 32
route-map CONNECTED-TO-OSPF permit 10
   match ip address prefix-list CONNECTED
```

---

## 7. ISIS Commands

### Show Commands

```
show isis summary                        # IS-IS process, NET, levels
show isis neighbors                      # IS-IS neighbor adjacencies
show isis neighbors detail               # state, hold time, circuit type
show isis interface                      # per-interface IS-IS config and state
show isis interface detail               # metrics, timers, circuit type
show isis database                       # LSDB summary (all LSPs)
show isis database detail                # full TLV details
show isis database level-2               # Level-2 LSDB only
show isis database <system-id> detail    # specific LSP
show isis route                          # IS-IS computed routes
show isis route detail
show isis traffic                        # SPF runs, PDU counters
show isis hostname                       # dynamic hostname mappings
show isis segment-routing prefix-segments  # SR-MPLS prefix SIDs
```

### Route Table Integration

```
show ip route isis
show ip route isis detail
show ip route 10.0.0.0/8                 # check IS-IS learned routes
```

### Configuration Examples

```
! IS-IS process
router isis CORE
   net 49.0001.0100.0000.0001.00        ! NET: area 49.0001, sysid from 10.0.0.1
   is-type level-2-only
   log-adjacency-changes
   !
   address-family ipv4 unicast
      redistribute connected route-map CONNECTED-TO-ISIS
   !
   address-family ipv6 unicast
      multi-topology

! Enable IS-IS on interfaces
interface Ethernet1
   isis enable CORE
   isis circuit-type level-2-only
   isis metric 10
   isis authentication mode md5
   isis authentication key secretkey

interface Loopback0
   isis enable CORE
   isis passive

! Segment Routing (SR-MPLS) — requires Jericho-based platform
router isis CORE
   segment-routing mpls
   !
   address-family ipv4 unicast
      segment-routing mpls

interface Loopback0
   node-segment ipv4 index 1           ! node SID
```

---

## 8. BGP Commands

### Show Commands

```
show bgp summary                         # all peers, state, prefix counts
show bgp neighbors                       # all neighbor details
show bgp neighbors 192.0.2.2            # specific neighbor
show bgp neighbors 192.0.2.2 detail     # full neighbor detail + timers
show bgp peer-group                      # peer groups
show bgp peer-group IBGP detail

! Route table views
show ip route bgp                        # BGP routes in the RIB
show bgp ipv4 unicast                    # BGP IPv4 unicast RIB (full table)
show bgp ipv4 unicast summary            # abbreviated
show bgp ipv4 unicast 10.0.0.0/8        # specific prefix detail
show bgp ipv4 unicast 10.0.0.0/8 detail # with path attributes

! Per-neighbor route views
show bgp neighbors 192.0.2.2 received-routes    # routes received from peer
show bgp neighbors 192.0.2.2 advertised-routes  # routes sent to peer

! L3VPN
show bgp vpnv4 unicast                   # all VPNv4 routes
show bgp vpnv4 unicast vrf CUST-A        # VPN routes for specific VRF
show ip route vrf CUST-A                 # VRF routing table

! EVPN
show bgp evpn summary
show bgp evpn route-type mac-ip         # Type-2 routes
show bgp evpn route-type imet            # Type-3 routes
show bgp evpn route-type ip-prefix       # Type-5 routes
```

### Debugging BGP

```
show bgp neighbors 192.0.2.2 | include "State|Hold|Prefix"
show logging | include BGP
debug ip bgp 192.0.2.2 updates          ! verbose — use with caution
no debug all                             ! disable all debug
```

### Configuration Examples

```
! Basic iBGP
router bgp 65000
   router-id 10.0.0.1
   !
   neighbor IBGP peer group
   neighbor IBGP remote-as 65000
   neighbor IBGP update-source Loopback0
   neighbor IBGP send-community
   neighbor 10.0.0.2 peer group IBGP
   !
   address-family ipv4
      neighbor IBGP activate

! eBGP
router bgp 65000
   neighbor 192.0.2.2 remote-as 65001
   neighbor 192.0.2.2 description Upstream-Peer
   !
   address-family ipv4
      neighbor 192.0.2.2 activate

! Route reflector
router bgp 65000
   neighbor IBGP route-reflector-client

! Apply policy
router bgp 65000
   neighbor 192.0.2.2 route-map IMPORT-POLICY in
   neighbor 192.0.2.2 route-map EXPORT-POLICY out

! BFD for BGP
router bgp 65000
   neighbor 192.0.2.2 bfd

! Next-hop-self
router bgp 65000
   neighbor IBGP next-hop-self

! MD5 authentication
router bgp 65000
   neighbor 192.0.2.2 password secret

! Additional paths (ADDPATH)
router bgp 65000
   address-family ipv4
      bgp additional-paths send ecmp
      bgp additional-paths receive
```

### Policy and Communities

```
! Define community list
ip community-list standard MY-COMM permit 65000:100

! Route map matching community
route-map IMPORT permit 10
   match community MY-COMM
   set local-preference 200

! AS path prepend
route-map EXPORT permit 10
   set as-path prepend 65000 65000

! Prefix list
ip prefix-list MY-PREFIXES seq 10 permit 10.0.0.0/8 le 24
route-map EXPORT permit 10
   match ip address prefix-list MY-PREFIXES
```

---

## 9. MPLS Commands

> **Note:** MPLS forwarding requires a platform with an ASIC that supports it. Trident and Tomahawk chipsets have limited or no MPLS forwarding capability. Full MPLS (LDP, RSVP-TE, SR-MPLS) is supported on **Jericho/Jericho2-based platforms** (7280R, 7500R, 7800R series). See [Section 12](#12-platform--merchant-silicon-details) and [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/).

### Show Commands

```
! LDP
show mpls ldp neighbor                   # LDP session state
show mpls ldp neighbor detail
show mpls ldp interface                  # LDP-enabled interfaces
show mpls ldp bindings                   # LDP label bindings (local + remote)
show mpls ldp bindings detail
show mpls ldp traffic                    # LDP PDU counters

! RSVP / Traffic Engineering
show mpls traffic-eng tunnels            # all TE tunnels
show mpls traffic-eng tunnels detail     # ERO, path, bandwidth
show mpls traffic-eng tunnels bandwidth  # bandwidth utilization
show mpls rsvp neighbor                  # RSVP neighbors
show mpls rsvp session                   # RSVP session state
show mpls traffic-eng topology           # TE database

! MPLS forwarding table
show mpls lfib route                     # label forwarding table (like mpls.0)
show mpls lfib route detail
show mpls lfib route <label>             # specific label

! Segment Routing
show isis segment-routing prefix-segments   # IS-IS SR SIDs
show ip route segment-routing               # SR routes in RIB
show mpls route segment-routing             # SR label table
show traffic-engineering segment-routing    # SR-TE LSPs
```

### L3VPN

```
show ip route vrf CUST-A                 # VRF routing table
show bgp vpnv4 unicast vrf CUST-A       # BGP VPNv4 routes for VRF
show vrf                                 # all VRFs and their state
show vrf CUST-A detail                   # VRF route distinguisher, targets
```

### Configuration Examples

```
! Enable MPLS globally
mpls ip

! LDP
mpls ldp
   router-id interface Loopback0
   transport-address interface Loopback0
   interface Ethernet1

! Enable MPLS on interface
interface Ethernet1
   mpls ip

! RSVP-TE
mpls traffic-engineering
   interface Ethernet1
   router-id Loopback0
   lsp TO-R2
      to 10.0.0.2
      primary PATH-TO-R2
   path PATH-TO-R2
      explicit 10.0.1.1 strict
      explicit 10.0.0.2 strict

! SR-MPLS with IS-IS (Jericho platform)
router isis CORE
   segment-routing mpls
   address-family ipv4 unicast
      segment-routing mpls

! L3VPN
vrf instance CUST-A
   rd 65000:100
   route-target import 65000:100
   route-target export 65000:100
!
interface Ethernet2
   vrf CUST-A
   ip address 172.16.0.1/30
!
router bgp 65000
   vrf CUST-A
      neighbor 172.16.0.2 remote-as 65100
      address-family ipv4
         neighbor 172.16.0.2 activate
   address-family vpn-ipv4
      neighbor IBGP activate
```

---

## 10. IPv6 Commands

### Key IPv6 Concepts in EOS

EOS handles IPv4 and IPv6 as separate address families on the same interface. IPv6 routes live in the main RIB alongside IPv4. Protocol daemons run separate IPv6 instances (OSPFv3, BGP `address-family ipv6 unicast`, IS-IS `address-family ipv6 unicast`).

### IPv6 Interface Show Commands

```
show ipv6 interface brief                # all interfaces with IPv6 addresses
show ipv6 interface Ethernet1            # detail including ND state
show interfaces Ethernet1               # includes IPv6 when configured
show ipv6 route                          # IPv6 routing table
```

### IPv6 NDP (Neighbor Discovery)

```
show ipv6 neighbors                      # NDP neighbor cache (like show arp)
show ipv6 neighbors detail
show ipv6 neighbors Ethernet1            # NDP table for specific interface
show ipv6 neighbors 2001:db8::1          # lookup specific neighbor
```

### IPv6 Routing Table

```
show ipv6 route                          # full IPv6 RIB
show ipv6 route summary                  # prefix count by protocol
show ipv6 route bgp                      # IPv6 BGP routes
show ipv6 route ospf                     # OSPFv3 routes
show ipv6 route isis                     # IS-IS IPv6 routes
show ipv6 route 2001:db8::/32            # specific prefix lookup
show ipv6 route ::/0                     # IPv6 default route
```

### IPv6 Ping and Traceroute

```
ping ipv6 2001:db8::1
ping ipv6 2001:db8::1 repeat 5
ping ipv6 2001:db8::1 source 2001:db8:1::1
ping vrf CUST-A ipv6 2001:db8::1

traceroute ipv6 2001:db8::1
traceroute ipv6 2001:db8::1 source 2001:db8:1::1
```

### OSPFv3 (OSPF for IPv6)

```
show ipv6 ospf
show ipv6 ospf neighbor
show ipv6 ospf neighbor detail
show ipv6 ospf interface
show ipv6 ospf database
show ipv6 ospf route
show ipv6 route ospf
```

**OSPFv3 Configuration:**

```
! OSPFv3 process
router ospf6 1
   router-id 10.0.0.1
   passive-interface Loopback0

! Enable on interface
interface Ethernet1
   ipv6 ospf 1 area 0.0.0.0
   ipv6 ospf cost 10

! Interface IPv6 address required
interface Ethernet1
   ipv6 address 2001:db8:1::1/64
   ipv6 enable                         ! generates link-local if no global address
```

### IS-IS with IPv6

```
! Same adjacency serves both IPv4 and IPv6
show isis neighbors                     # shared adjacency
show ipv6 route isis                    # IPv6 routes via IS-IS

! Multi-topology IS-IS for IPv6
router isis CORE
   address-family ipv6 unicast
      multi-topology

interface Ethernet1
   isis enable CORE
   ipv6 address 2001:db8:1::1/64
```

### BGP for IPv6

```
! IPv6 BGP summary
show bgp ipv6 unicast summary
show bgp ipv6 unicast                   # full IPv6 BGP table
show bgp ipv6 unicast 2001:db8:100::/48

! Per-neighbor IPv6 views
show bgp neighbors 2001:db8::2 received-routes
show bgp neighbors 2001:db8::2 advertised-routes
```

**BGP IPv6 Configuration:**

```
! iBGP with IPv6
router bgp 65000
   neighbor IBGP-V6 peer group
   neighbor IBGP-V6 remote-as 65000
   neighbor IBGP-V6 update-source Loopback0
   neighbor IBGP-V6 send-community
   neighbor 2001:db8:0:2::1 peer group IBGP-V6
   !
   address-family ipv6
      neighbor IBGP-V6 activate
      neighbor IBGP-V6 next-hop-self

! eBGP IPv6
router bgp 65000
   neighbor 2001:db8:peer::2 remote-as 65001
   address-family ipv6
      neighbor 2001:db8:peer::2 activate

! Dual-stack (carry both families over a single session)
router bgp 65000
   neighbor 192.0.2.2 remote-as 65001
   address-family ipv4
      neighbor 192.0.2.2 activate
   address-family ipv6
      neighbor 192.0.2.2 activate
```

### IPv6 Configuration Reference

```
! Dual-stack interface
interface Ethernet1
   ip address 192.0.2.1/30
   ipv6 address 2001:db8:1::1/64
   no shutdown

! IPv6 loopback
interface Loopback0
   ip address 10.0.0.1/32
   ipv6 address 2001:db8:0:1::1/128

! Static IPv6 routes
ipv6 route ::/0 2001:db8:1::2           ! default
ipv6 route 2001:db8:100::/48 2001:db8:1::2

! IPv6 NDP (Router Advertisement) — for SLAAC
interface Ethernet1
   ipv6 nd ra-interval 30
   ipv6 nd ra-lifetime 200
   ipv6 nd prefix 2001:db8:100::/64

! Suppress RA (uplink to router — don't advertise)
interface Ethernet1
   ipv6 nd ra suppress
```

### IPv6 ACLs

```
! Show IPv6 ACL counters
show ip access-lists V6-FILTER          ! EOS uses unified ACL syntax

! IPv6 ACL configuration
ipv6 access-list V6-FILTER
   10 permit icmpv6 any any             ! allow ICMPv6
   20 deny   ipv6 2001:db8::/32 any    ! block documentation prefix
   30 permit ipv6 any any

! Apply to interface
interface Ethernet1
   ipv6 access-group V6-FILTER in
```

---

## 11. Configuration Management

### Viewing Configuration

```
show running-config                      # full active config
show running-config | section bgp        # specific section
show running-config interfaces           # all interface config
show startup-config                      # saved config (on flash)
show running-config diff                 # diff running vs startup
show configuration sessions              # active configuration sessions
```

### Saving Configuration

```
write memory                             # save running to startup (like 'commit' in JunOS)
copy running-config startup-config       # equivalent to write memory
copy running-config flash:backup.cfg     # save to flash file
copy running-config tftp://10.0.0.1/router.cfg
```

### Configuration Sessions (Candidate Config)

```
configure session PLANNED-CHANGE         # open an isolated session
! make all changes here
show session-config diffs                # diff: session vs running-config
commit                                   # apply atomically
abort                                    # discard all session changes

! Timer-based safety (auto-abort if not committed)
configure session RISKY-CHANGE timer 300
! make changes
commit                                   ! must commit within 300 seconds
```

### Checkpoints (Rollback Points)

```
! Save a named checkpoint
copy running-config checkpoint:pre-maintenance

! List available checkpoints
show checkpoint summary

! Restore from checkpoint
configure replace checkpoint:pre-maintenance

! Diff running vs checkpoint
show running-config diff checkpoint:pre-maintenance
```

### Loading and Replacing Configuration

```
copy tftp://10.0.0.1/new-config.cfg running-config   ! merge (IOS-style)
configure replace flash:full-config.cfg               ! full replace (atomic)
configure replace checkpoint:pre-maintenance          ! restore checkpoint
```

### Editing Configuration

```
! Standard mode — changes apply immediately
configure terminal
   interface Ethernet1
      no shutdown
   exit
end

! Delete configuration blocks
no router ospf 1                         ! remove entire OSPF process
interface Ethernet1
   no ip address                         ! remove IP address

! Deactivate without deleting — EOS uses shutdown for interfaces
interface Ethernet1
   shutdown                              ! admin-down, config preserved
```

---

## 12. Platform & Merchant Silicon Details

Arista relies exclusively on merchant (third-party) silicon for forwarding. This is a deliberate design choice: Arista invests in EOS software differentiation, not ASIC design. The forwarding ASIC determines buffer depth, TCAM size, feature support, and scaling limits. Understanding the silicon is essential when evaluating fit for a given use case.

For detailed per-chipset and per-platform buffer specifications, see: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

### Merchant Silicon Overview

| ASIC Family | Vendor | Typical Buffer | MPLS | TCAM | Primary Use |
|---|---|---|---|---|---|
| Trident3 / Trident4 | Broadcom | Shallow (~32–64MB) | Limited | On-chip | Access/aggregation, VXLAN VTEP |
| Tomahawk3 / Tomahawk4 | Broadcom | Shallow (~64MB) | No | On-chip | Hyperscale, 400G density |
| Jericho / Jericho2 / Jericho2c+ | Broadcom | Deep (HBM, GBs) | Full | External (eTCAM) | Metro, WAN, core, full MPLS |
| Tofino / Tofino2 | Intel/Barefoot | Configurable | Via P4 | Programmable | Programmable forwarding research/production |

### Platform Hardware Overview

| Platform | Role | ASIC | Key Interfaces | Notes |
|---|---|---|---|---|
| 7050X4 | Data center ToR | Trident4 | 48×25G + 8×100G | Shallow buffer — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7060X5 | High-density 400G | Tomahawk4 | 32×400G | No MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7280R3 | Metro/WAN PE | Jericho2 | 48×100G + 8×400G | Deep buffer, full MPLS — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7500R3 | Modular core | Jericho2 | Modular, up to 400G | Large chassis, full MPLS+SR — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7800R3 | Large modular core | Jericho2c+ | Modular, 400G/800G | SP-grade, full feature set — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7170 | Programmable | Tofino2 | 32×100G | P4-programmable pipeline — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 720DP | Deep-buffer access | Trident4 | 48×25G + 8×100G | Extended on-chip buffer variant — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7130 | Precision timing | FPGA | 1G/10G | Sub-microsecond timing appliance |

### Feature Matrix by Silicon Family

| Feature | Trident3/4 | Tomahawk3/4 | Jericho/Jericho2 | Tofino2 |
|---|---|---|---|---|
| L3 routing (OSPF/IS-IS/BGP) | Yes | Yes | Yes | Via P4 |
| MPLS / LDP | Limited | No | Full | Via P4 |
| RSVP-TE | No | No | Full | Via P4 |
| Segment Routing (SR-MPLS) | Limited | No | Full | Via P4 |
| EVPN / VXLAN VTEP | Yes | Yes | Yes | Via P4 |
| L3VPN | Yes (IP-based) | Limited | Full MPLS | Via P4 |
| PTP / IEEE 1588v2 | BC (some) | No | BC + GM option | No |
| SyncE | Some models | No | Yes | No |
| External TCAM (eTCAM) | No | No | Yes (Jericho2) | N/A |
| Buffer depth | Shallow | Shallow | Deep (HBM) | Configurable |
| Coherent optics (400ZR) | No | No | Yes (7280R3) | No |
| In-Service SW Upgrade | Yes | Yes | Yes | Yes |

---

### Buffer Characteristics and Why They Matter

Merchant silicon buffer sizing is one of the most consequential design choices for a given deployment. Arista's use of commodity ASICs means buffer depth varies dramatically by platform and chipset family.

- **Shallow-buffer platforms** (Trident, Tomahawk): Optimized for low-latency, high-throughput workloads where traffic is already paced (data center leaf/spine). Microburst absorption is limited. Total on-chip buffer is typically 16–64MB shared across all ports. At 100G line rate, this equals a few hundred microseconds of absorption.

- **Deep-buffer platforms** (Jericho/Jericho2): Use High Bandwidth Memory (HBM) mounted adjacent to the ASIC, providing gigabytes of buffer. This is essential for WAN, metro, and any topology with large RTTs or bursty traffic patterns. 7280R3 and 7500R3 use HBM2 for this reason.

For specific buffer allocation, per-queue sizing, and VOQ (Virtual Output Queue) behavior by platform, see: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

---

### EVPN / VXLAN (All ASIC Families)

EVPN with VXLAN is Arista's primary L2VPN technology and is supported across all silicon families with VTEP capability.

```
! Verify EVPN state
show bgp evpn summary
show bgp evpn
show vxlan vtep
show vxlan vni
show vxlan address-table
show vxlan flood vtep                    ! BUM flooding list per VNI
```

**EVPN-VXLAN Configuration:**

```
! VXLAN interface
interface Vxlan1
   vxlan source-interface Loopback0
   vxlan udp-port 4789
   vxlan vlan 100 vni 10100
   vxlan vlan 200 vni 10200
   vxlan learn-restrict any              ! disable data-plane MAC learning (BGP EVPN control)

! BGP EVPN underlay/overlay
router bgp 65000
   neighbor EVPN-PEERS peer group
   neighbor EVPN-PEERS remote-as 65000
   neighbor EVPN-PEERS update-source Loopback0
   neighbor EVPN-PEERS send-community extended
   neighbor EVPN-PEERS maximum-routes 12000
   neighbor 10.0.0.2 peer group EVPN-PEERS
   !
   address-family evpn
      neighbor EVPN-PEERS activate
   !
   vlan 100
      rd 65000:10100
      route-target both 65000:10100
      redistribute learned

! Symmetric IRB (L3 EVPN — Type-5)
interface Vlan100
   ip address 10.100.0.1/24
   varp ip 10.100.0.254                  ! virtual ARP gateway (anycast)

ip virtual-router mac-address 00:1c:73:aa:bb:cc
```

---

### Timing and Synchronization (7280R3 / 7130 Series)

Timing is supported on specific platforms. The 7280R3 (Jericho2) supports IEEE 1588v2 PTP Boundary Clock and optionally a GNSS module for Grandmaster capability. The 7130 is a precision timing appliance with sub-microsecond accuracy.

```
! PTP show commands
show ptp
show ptp clock                           ! local clock identity, domain, class
show ptp interface                       ! per-interface PTP state and role
show ptp interface Ethernet1 detail      ! offset, path delay, role
show ptp counters                        ! per-interface PTP message counters
show ptp monitor                         ! clock servo offset and lock state
show ptp clock master-slave              ! master/slave hierarchy

! SyncE
show interfaces Ethernet1 | include SyncE
show sync                                ! SyncE source and quality level
```

**PTP Configuration:**

```
! PTP Boundary Clock
ptp profile ieee1588-2008
ptp domain 24
ptp priority1 128
ptp priority2 128
ptp source ip 192.0.2.1

! Slave interface (toward grandmaster)
interface Ethernet1
   ptp slave
   ptp transport ipv4

! Master interface (toward downstream slaves)
interface Ethernet2
   ptp master
   ptp transport ipv4

! SyncE
interface Ethernet1
   speed forced 10000full
   ! SyncE is enabled by hardware profile on supported platforms
```

---

### Carrier Ethernet OAM

Arista EOS supports IEEE 802.1ag CFM and ITU-T Y.1731 for carrier Ethernet services on platforms that support it (primarily Jericho-based).

```
! CFM show commands
show ethernet oam cfm domain             ! all maintenance domains
show ethernet oam cfm mep               ! all MEPs
show ethernet oam cfm mep detail        ! MEP detail, continuity check state
show ethernet oam cfm database          ! remote MEP discovery

! Y.1731 delay measurement
show ethernet oam cfm delay-measurement ! frame delay and variation results
```

**CFM Configuration:**

```
ethernet cfm domain CARRIER level 4
   service MA-SVC-100 vlan 100
      continuity-check interval 1s
      mep crosscheck
   mep domain CARRIER service MA-SVC-100
      mep 1 interface Ethernet1 direction down
```

---

### Chassis and Hardware Commands

```
show version                             ! EOS version, model, serial number
show inventory                           ! all hardware: modules, transceivers, PSU, fans
show environment all                     ! temperature, fans, power supply state
show environment temperature             ! per-sensor temperatures
show environment power                   ! power consumption and capacity
show environment cooling                 ! fan state and speed
show platform fap 0                      ! forwarding ASIC info (platform-specific)
show platform fap 0 counters             ! ASIC-level packet counters
show platform jericho2 packet-buffer     ! buffer utilization (7280/7500/7800R)
show platform trident forwarding-table   ! TCAM utilization (Trident platforms)
show hardware capacity                   ! TCAM and FIB table utilization
show hardware capacity detail
show interface Ethernet1 transceiver     ! DOM: optic Rx/Tx power, temp, voltage
```

### Interface Naming

EOS interface names are logical and consistent across all platforms:

```
Ethernet1            ! physical port 1 (fixed chassis)
Ethernet1/1          ! modular chassis: module 1, port 1
Ethernet2/1/1        ! modular: slot 2, module 1, port 1 (some chassis)
Management1          ! out-of-band management port
Loopback0            ! software loopback (no hardware resource)
Port-Channel1        ! link aggregation group (LAG)
Vlan100              ! SVI for VLAN 100 (L3 gateway)
Vxlan1               ! VXLAN tunnel interface
```

---

### Class of Service (QoS)

EOS CoS behavior is directly constrained by the underlying ASIC. Queue count, scheduling precision, and WRED support vary by chipset. See [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/) for queue architecture by platform.

```
show qos interface Ethernet1             ! QoS maps applied to interface
show qos maps                            ! all QoS map definitions
show interfaces Ethernet1 queues         ! per-queue depth and drop counters
show platform qos                        ! hardware QoS state
```

**Basic CoS Configuration:**

```
! Define traffic class maps
qos map dscp 46 to traffic-class 7 drop-precedence low  ! EF -> TC7
qos map dscp 34 to traffic-class 4 drop-precedence low  ! AF41 -> TC4
qos map dscp 0 to traffic-class 0 drop-precedence low   ! BE -> TC0

! Scheduler (WFQ/DWRR per queue)
policy-map type qos PM-SCHED
   class VOICE
      priority
      bandwidth percent 30
   class BEST-EFFORT
      bandwidth percent 70

! Apply to interface
interface Ethernet1
   service-policy type qos input PM-SCHED

! DSCP remarking
policy-map type qos PM-REMARK
   class VOICE
      set dscp ef
   class DATA
      set dscp af41
```

---

### EOS-Specific Operational Tips

```
! Drop to Linux shell (use with care — not for routine ops)
bash

! eAPI — JSON-RPC access (must be enabled)
management api http-commands
   no shutdown
   protocol http
   protocol https ssl profile eAPI-PROFILE

! Access eAPI interactively
show management api http-commands       ! eAPI state and access URLs

! CloudVision integration
show cvx connections                    ! CloudVision state (if CVX enabled)

! Verify TCAM utilization before deploying ACLs
show hardware capacity detail | include acl|route|mac

! Check platform ASIC type
show version | include ASIC

! Monitor interface counters live
watch 2 show interfaces Ethernet1 counters rates

! Check EVPN MAC learning
show vxlan address-table | include <mac-or-vtep>

! SR-MPLS label forwarding verification (Jericho platforms)
show mpls lfib route | include 16[0-9][0-9][0-9]   ! typical SRGB range

! Verify PTP offset before activating a timing-dependent service
show ptp monitor

! Confirm BGP EVPN peers are up
show bgp evpn summary | include Estab

! Identify hardware dropping traffic
show platform fap 0 counters drop | exclude " 0$"
```

### Licensing

EOS uses a feature license model. Some capabilities require an active license:

```
show license                             ! installed licenses and status
show license detail                      ! feature-level license state
```

Key licensed features (varies by platform):
- **Base** — L2/L3 forwarding, standard routing protocols
- **Advanced** — BGP, extended route scale, additional protocol features
- **MPLS** — LDP, RSVP-TE (Jericho platforms)
- **CloudVision** — telemetry streaming, topology awareness
- **EVPN** — BGP EVPN control plane (may be included in Advanced)
- **Cognitive WiFi** — for campus platforms

---

## 13. Cross-Platform Command Reference

### General & Interface Commands

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| Show interfaces brief | `show interfaces status` | `show interfaces terse` | `show ip interface brief` | `show ipv4 interface brief` |
| Show interface detail | `show interfaces Ethernet1` | `show interfaces ge-0/0/0` | `show interface GigE0/0/0` | `show interface GigE0/0/0/0` |
| Show interface counters | `show interfaces Ethernet1 counters` | `show interfaces statistics` | `show interface GigE0/0/0` | `show interface GigE0/0/0/0` |
| Show all MAC addresses | `show mac address-table` | `show ethernet-switching table` | `show mac address-table` | `show l2vpn forwarding bd-mac-address` |
| Disable interface | `shutdown` (interface mode) | `set interfaces ge-0/0/0 disable` | `shutdown` (interface mode) | `shutdown` (interface mode) |
| Show running config | `show running-config` | `show configuration` | `show running-config` | `show running-config` |
| Show config section | `show running-config \| section bgp` | `show config protocols bgp` | `show running-config \| section bgp` | `show running-config \| formal` |
| Enter config mode | `configure terminal` | `configure` | `configure terminal` | `configure terminal` |
| Save config | `write memory` | `commit` | `write memory` | `commit` |
| Rollback config | `configure replace checkpoint:X` | `rollback 1` + `commit` | `copy startup running` (limited) | `rollback 1` |
| Config diff | `show running-config diff` | `show config \| compare` | *(no native equivalent)* | `show commit changes diff` |
| Validate config | `configure session` + `show session-config diffs` | `commit check` | *(limited)* | `commit` (always validates) |
| Candidate config | `configure session <name>` | `configure private` | *(not native)* | native always |

### Routing Protocol — OSPF

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| OSPF neighbors | `show ip ospf neighbor` | `show ospf neighbor` | `show ip ospf neighbor` | `show ospf neighbor` |
| OSPF neighbor detail | `show ip ospf neighbor detail` | `show ospf neighbor detail` | `show ip ospf neighbor detail` | `show ospf neighbor detail` |
| OSPF interfaces | `show ip ospf interface` | `show ospf interface` | `show ip ospf interface` | `show ospf interface` |
| OSPF LSDB | `show ip ospf database` | `show ospf database` | `show ip ospf database` | `show ospf database` |
| OSPF routes | `show ip route ospf` | `show route protocol ospf` | `show ip route ospf` | `show route ospf` |
| OSPF summary | `show ip ospf` | `show ospf overview` | `show ip ospf` | `show ospf` |
| OSPFv3 neighbors | `show ipv6 ospf neighbor` | `show ospf3 neighbor` | `show ipv6 ospf neighbor` | `show ospfv3 neighbor` |

### Routing Protocol — IS-IS

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| IS-IS adjacencies | `show isis neighbors` | `show isis adjacency` | `show isis neighbors` | `show isis adjacency` |
| IS-IS adjacency detail | `show isis neighbors detail` | `show isis adjacency detail` | `show isis neighbors detail` | `show isis adjacency detail` |
| IS-IS interfaces | `show isis interface` | `show isis interface` | `show isis interface` | `show isis interface` |
| IS-IS LSDB | `show isis database` | `show isis database` | `show isis database` | `show isis database` |
| IS-IS LSDB detail | `show isis database detail` | `show isis database detail` | `show isis database verbose` | `show isis database detail` |
| IS-IS routes | `show ip route isis` | `show route protocol isis` | `show ip route isis` | `show route isis` |
| IS-IS overview | `show isis summary` | `show isis overview` | `show isis` | `show isis` |

### Routing Protocol — BGP

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| BGP summary | `show bgp summary` | `show bgp summary` | `show ip bgp summary` | `show bgp summary` |
| BGP neighbors | `show bgp neighbors` | `show bgp neighbor` | `show ip bgp neighbors` | `show bgp neighbors` |
| BGP neighbor detail | `show bgp neighbors 10.0.0.2` | `show bgp neighbor 10.0.0.2` | `show ip bgp neighbors 10.0.0.2` | `show bgp neighbors 10.0.0.2` |
| BGP routes | `show bgp ipv4 unicast` | `show route protocol bgp` | `show ip bgp` | `show bgp` |
| BGP route detail | `show bgp ipv4 unicast 10.0.0.0/8` | `show route 10/8 detail` | `show ip bgp 10.0.0.0/8` | `show bgp 10.0.0.0/8` |
| Routes received | `show bgp neighbors X received-routes` | `show bgp neighbor X received-routes` | `show ip bgp neighbors X received-routes` | `show bgp neighbors X received` |
| Routes advertised | `show bgp neighbors X advertised-routes` | `show bgp neighbor X advertised-routes` | `show ip bgp neighbors X advertised-routes` | `show bgp neighbors X advertised` |
| VPN routes | `show bgp vpnv4 unicast vrf CUST-A` | `show route table CUST-A.inet.0` | `show ip bgp vpnv4 vrf CUST-A` | `show bgp vrf CUST-A` |

### MPLS

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| LDP neighbors | `show mpls ldp neighbor` | `show ldp neighbor` | `show mpls ldp neighbor` | `show mpls ldp neighbor` |
| LDP label bindings | `show mpls ldp bindings` | `show ldp database` | `show mpls ldp bindings` | `show mpls ldp bindings` |
| MPLS label table | `show mpls lfib route` | `show route table mpls.0` | `show mpls forwarding-table` | `show mpls forwarding` |
| RSVP sessions | `show mpls rsvp session` | `show rsvp session` | `show ip rsvp session` | `show rsvp session` |
| TE tunnels | `show mpls traffic-eng tunnels` | `show mpls lsp` | `show mpls traffic-eng tunnels` | `show mpls traffic-eng tunnels` |
| TE database | `show mpls traffic-eng topology` | `show ted database` | `show mpls traffic-eng topology` | `show mpls traffic-eng topology` |

### VLANs / L2

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| Show VLANs | `show vlan brief` | `show vlans` | `show vlan brief` | `show l2vpn bridge-domain brief` |
| VLAN detail | `show vlan 100` | `show vlans VLAN100` | `show vlan id 100` | `show l2vpn bridge-domain name BD100 detail` |
| Spanning tree | `show spanning-tree` | `show spanning-tree bridge` | `show spanning-tree` | `show spanning-tree` |
| MAC table | `show mac address-table` | `show ethernet-switching table` | `show mac address-table` | `show l2vpn forwarding bd-mac-address` |
| LACP status | `show lacp interface Port-Channel1` | `show lacp interfaces ae0` | `show lacp interface Po1` | `show lacp interface Bundle-Ether1` |
| L3 VLAN gateway | `interface Vlan100` (SVI) | `irb unit 100` | `interface Vlan100` (SVI) | `interface BVI100` |

### IPv6

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| Show IPv6 interfaces | `show ipv6 interface brief` | `show interfaces terse` (includes inet6) | `show ipv6 interface brief` | `show ipv6 interface brief` |
| IPv6 NDP table | `show ipv6 neighbors` | `show ipv6 neighbors` | `show ipv6 neighbors` | `show ipv6 neighbors` |
| IPv6 route table | `show ipv6 route` | `show route table inet6.0` | `show ipv6 route` | `show route ipv6` |
| IPv6 default route | `show ipv6 route ::/0` | `show route ::/0` | `show ipv6 route ::/0` | `show route ipv6 ::/0` |
| IPv6 BGP routes | `show bgp ipv6 unicast` | `show route table inet6.0 protocol bgp` | `show bgp ipv6 unicast` | `show bgp ipv6 unicast` |
| OSPFv3 neighbors | `show ipv6 ospf neighbor` | `show ospf3 neighbor` | `show ipv6 ospf neighbor` | `show ospfv3 neighbor` |
| IS-IS IPv6 routes | `show ipv6 route isis` | `show route table inet6.0 protocol isis` | `show ipv6 route isis` | `show route ipv6 isis` |
| IPv6 ping | `ping ipv6 2001:db8::1` | `ping 2001:db8::1` | `ping ipv6 2001:db8::1` | `ping 2001:db8::1` |
| IPv6 traceroute | `traceroute ipv6 2001:db8::1` | `traceroute 2001:db8::1` | `traceroute ipv6 2001:db8::1` | `traceroute 2001:db8::1` |
| IPv6 static route | `ipv6 route ::/0 <next-hop>` | `set routing-options rib inet6.0 static route` | `ipv6 route ::/0 <next-hop>` | `router static address-family ipv6` |

### System & Diagnostics

| Function | EOS | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|---|
| Ping | `ping 8.8.8.8 repeat 5` | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 repeat 5` | `ping 8.8.8.8 count 5` |
| Traceroute | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` |
| Show ARP | `show arp` | `show arp` | `show ip arp` | `show arp` |
| Show routes | `show ip route` | `show route` | `show ip route` | `show route` |
| Disable paging | `terminal length 0` | `set cli screen-length 0` | `terminal length 0` | `terminal length 0` |
| Show version | `show version` | `show version` | `show version` | `show version` |
| Show hardware | `show inventory` | `show chassis hardware` | `show inventory` | `show inventory` |
| Logs | `show logging` | `show log messages` | `show logging` | `show logging` |
| Follow logs live | `bash tail -f /var/log/messages` | `monitor start messages` | `terminal monitor` | `terminal monitor` |
| CPU/memory | `show processes top` | `show chassis routing-engine` | `show processes cpu` | `show processes cpu` |
| Reboot | `reload` | `request system reboot` | `reload` | `reload` |
| Save config | `write memory` | `commit` | `write memory` | `commit` |
| Grep equivalent | `show ... \| include <regex>` | `show ... \| match <regex>` | `show ... \| include <regex>` | `show ... \| include <regex>` |
| Exclude equivalent | `show ... \| exclude <regex>` | `show ... \| except <regex>` | `show ... \| exclude <regex>` | `show ... \| exclude <regex>` |
| Section of config | `show running-config \| section <regex>` | `show config \| find <string>` | `show running-config \| section <regex>` | `show running-config \| formal` |
| Count lines | `show ... \| count` | `show ... \| count` | `show ... \| count` | `show ... \| utility wc` |

---

## 14. Quick Reference Card

### Top 20 Daily-Driver Commands

```bash
# System health
show version                              # EOS version, model, serial
show environment all                      # temperature, fans, power
show logging | tail 100                   # recent syslog

# Interfaces
show interfaces status                    # all interfaces, one line each
show interfaces Ethernet1                 # full interface detail
show interfaces Ethernet1 counters rates  # live traffic rates

# Routing
show ip route                             # full routing table
show ip route summary                     # route count by protocol
show ip route bgp                         # all BGP routes
show arp                                  # ARP table

# BGP / OSPF / IS-IS
show bgp summary                          # BGP peer state at a glance
show ip ospf neighbor                     # OSPF adjacencies
show isis neighbors                       # IS-IS adjacencies

# MPLS (Jericho platforms)
show mpls traffic-eng tunnels             # RSVP-TE tunnels
show mpls ldp neighbor                    # LDP sessions
show mpls lfib route | head 30           # top of MPLS FIB

# Config workflow
show running-config | no-more            # full running config
show running-config | section bgp        # BGP config block
configure session CHANGE | show session-config diffs  # staged changes
```

### Useful One-Liners

```bash
# Count BGP prefixes per peer
show bgp summary | include "^\d{1,3}\."

# Show only established BGP sessions
show bgp summary | exclude "Idle|Active|Connect"

# Find interfaces that are down (not admin-down)
show interfaces status | include notconnect

# Show OSPF neighbors that are not Full
show ip ospf neighbor | exclude Full

# Find which IS-IS L2 adjacencies are up
show isis neighbors | include "UP.*L2"

# Get all config referencing a specific IP
show running-config | include 192.0.2.1

# Tail syslog live (from bash)
bash tail -f /var/log/messages | grep BGP

# Show commit history (configuration sessions)
show configuration sessions history

# TCAM utilization check
show hardware capacity | include route|acl|mac

# Watch interface counters refresh every 2 seconds
watch 2 show interfaces Ethernet1 counters rates

# Verify EVPN MAC table
show vxlan address-table

# Check buffer utilization (Jericho platforms)
show platform jericho2 packet-buffer
```

### EOS Mental Models

| Concept | EOS Way | Notes |
|---|---|---|
| Config takes effect immediately | Type in config mode → active | No commit required unless using sessions |
| Configuration sessions | `configure session` → `commit` | Optional candidate-config model, like JunOS |
| Checkpoints as rollback points | `copy running-config checkpoint:X` | Must be created manually before risky changes |
| VRFs | `vrf instance NAME` + `rd`/`route-target` | Similar to JunOS routing-instances of type VRF |
| SVI (L3 VLAN gateway) | `interface Vlan100` | Equivalent to JunOS IRB (`irb unit 100`) |
| Port-Channel (LAG) | `interface Port-Channel1` | Equivalent to JunOS `ae0` |
| Sysdb | Central in-memory state store | All EOS agents read/write here; not user-visible |
| Merchant silicon | ASIC defines feature set | Buffer depth, MPLS support, TCAM all ASIC-determined |
| eAPI | JSON-RPC over HTTP/HTTPS | Enables automation; requires `management api http-commands` |
| `do` in config mode | `do show ...` | Equivalent to JunOS `run show ...` |
| `bash` | Drops to Linux shell | Avoid for routine ops; useful for automation scripts |
| Routing protocols | All use Linux-based daemons via Sysdb | No hard RE/PFE boundary; ASIC driver is a Sysdb agent |
| Buffer sizing | Entirely ASIC-determined | See [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) for specifics |

---

*Curriculum version: 1.0 | Target: Arista EOS — 7050/7060/7170/7280/7500/7800 platforms*
*Reference platforms for comparison: Juniper JunOS MX/ACX, Cisco IOS-XE 17.x, Cisco IOS-XR 7.x*
*Chipset buffer details: [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)*

---
title: JunOS basics
date: 2026-05-05
author: Nick Buraglio
layout: page
---

# JunOS Basics:

A practical curriculum for network engineers learning Juniper JunOS, with emphasis on operational commands, usability features, and cross-platform translation from IOS-XR and IOS-XE.

---

## Table of Contents

1. [JunOS Fundamentals](#1-junos-fundamentals)
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
12. [ACX Platform-Specific Details](#12-acx-platform-specific-details)
13. [Cross-Platform Command Reference](#13-cross-platform-command-reference)
14. [Quick Reference Card](#14-quick-reference-card)

---

## 1. JunOS Fundamentals

### Architecture Overview

JunOS separates the control plane (Routing Engine, RE) from the forwarding plane (Packet Forwarding Engine, PFE). This separation is reflected in the CLI: you are always on the RE, and `show pfe` commands query the PFE directly.

JunOS runs on FreeBSD. You can drop to a Unix shell with `start shell` and use standard Unix tools (`grep`, `awk`, `tail -f`, etc.) against log files in `/var/log/`.

### Operational vs. Configuration Mode

```
user@router>          # operational mode prompt (>)
user@router#          # configuration mode prompt (#)
```

| Action | Command |
|--------|---------|
| Enter configuration mode | `configure` or `edit` |
| Enter configuration mode exclusively | `configure exclusive` |
| Enter configuration mode privately | `configure private` |
| Return to operational mode | `exit` or `quit` |
| Run operational command from config mode | `run show ...` |
| Run config command from op mode | Not supported — must enter config mode |

### Configuration Mode Variants

- `configure` — shared, others can also edit
- `configure exclusive` — locks config, prevents others from editing
- `configure private` — each user edits their own candidate config; useful on shared devices

---

## 2. CLI Navigation & Usability

### Tab Completion & Help

```
show route ?              # show all options at this level
show route <Tab>          # complete the command or show options
show r<Tab>               # completes to 'show route' if unambiguous
show interfaces ge-?      # show valid interface name patterns
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Complete command |
| `Space` | Complete command (same as Tab in most contexts) |
| `?` | Show context-sensitive help |
| `Ctrl+A` | Move cursor to beginning of line |
| `Ctrl+E` | Move cursor to end of line |
| `Ctrl+U` | Delete from cursor to beginning of line |
| `Ctrl+K` | Delete from cursor to end of line |
| `Ctrl+W` | Delete previous word |
| `Ctrl+R` | Reverse search command history |
| `Ctrl+C` | Abort current command |
| `Ctrl+D` | Exit CLI (if line is empty) |
| `Ctrl+Z` | Exit to top of configuration hierarchy |
| `Ctrl+L` | Redraw screen |
| Up/Down arrows | Navigate command history |
| `Ctrl+P` / `Ctrl+N` | Previous/Next command in history |

### Configuration Navigation

```
edit protocols ospf                 # descend into hierarchy
up                                  # go up one level
top                                 # go to top of config
exit                                # exit config mode
show                                # show current hierarchy level
show | compare                      # diff candidate vs. active config
```

### Abbreviations

JunOS allows unambiguous abbreviations for almost any command:

```
sh ro                    # show route
sh int terse             # show interfaces terse
sh bgp sum               # show bgp summary
sh mpls lsp              # show mpls lsp
conf                     # configure
```

### Operational Mode History

```
show cli history          # show command history
set cli history-size 500  # increase history buffer (default 100)
```

### Terminal & Display Settings

```
set cli screen-length 0       # disable pagination (like 'terminal length 0')
set cli screen-length 50      # set page length to 50 lines
set cli screen-width 250      # wider output (useful for tables)
set cli timestamp             # prefix output with timestamps
set cli complete-on-space off # disable space-as-tab-complete
```

---

## 3. Pipe Commands & Output Filtering

Pipes in JunOS are extremely powerful. Chain multiple filters for surgical output control.

### Core Pipe Commands

```
show route | ?                         # show all available pipe commands
```

| Pipe Command | Description | Example |
|---|---|---|
| `match <regex>` | Show lines matching pattern (like grep) | `show route \| match 10.0` |
| `except <regex>` | Exclude lines matching pattern | `show bgp summary \| except Idle` |
| `find <string>` | Jump to first occurrence | `show config \| find ospf` |
| `count` | Count matching lines | `show route \| count` |
| `last <n>` | Show last N lines | `show log messages \| last 50` |
| `head <n>` | Show first N lines | `show route \| head 20` |
| `trim <n>` | Remove first N characters from each line | `show route \| trim 5` |
| `no-more` | Disable pagination for this command | `show route \| no-more` |
| `display set` | Show config as flat set commands | `show config \| display set` |
| `display set relative` | Show config as set commands from current level | `show config protocols \| display set relative` |
| `display detail` | Show additional detail | `show route \| display detail` |
| `display xml` | Show output as XML | `show route \| display xml` |
| `display json` | Show output as JSON | `show route \| display json` |
| `terse` | Condensed output (command option, not always a pipe) | `show interfaces terse` |
| `save <file>` | Save output to file | `show config \| save /tmp/config-backup.txt` |

### Chaining Pipes

```
show route | match 192.168 | count
show bgp summary | except "^$" | match "Establ|Peer"
show config | display set | match "policy-statement"
show interfaces | match "ge-|ae-" | except "Physical"
```

### `display set` — The Most Important Pipe

`display set` converts the JunOS hierarchical config into flat, one-line `set` commands. This is invaluable for:
- Copying/pasting specific config blocks
- Diffing configs between devices
- Documentation
- Understanding exactly what commands built a config

```
show configuration | display set
show configuration protocols bgp | display set
show configuration interfaces ge-0/0/0 | display set
show configuration | display set | match "192.0.2"
show configuration | display set relative   # from within a hierarchy level
```

Example output:
```
set interfaces ge-0/0/0 unit 0 family inet address 192.0.2.1/30
set interfaces ge-0/0/0 unit 0 family mpls
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
```

### Regex in `match` / `except`

JunOS uses POSIX extended regex:

```
show route | match "^192\."              # anchored match
show route | match "10\.(0|1|2)\."       # alternation
show bgp summary | match "[0-9]+\s+Establ"  # established peers
show interfaces | except "(Physical|Logical|Input|Output|Traffic)"
```

### Watching Output Repeatedly

```
monitor interface ge-0/0/0            # live interface stats (Ctrl+C to stop)
monitor interface traffic             # live traffic across all interfaces
monitor traffic interface ge-0/0/0    # tcpdump-style packet capture
```

---

## 4. Interface Commands

### Show Commands

```
show interfaces                          # full detail all interfaces
show interfaces terse                    # one-line summary per interface/unit
show interfaces ge-0/0/0                 # detail for specific interface
show interfaces ge-0/0/0 detail          # more detail (queues, errors)
show interfaces ge-0/0/0 extensive       # everything including optics, MAC
show interfaces ge-0/0/0.0               # specific logical unit
show interfaces routing                  # routing-relevant interface info
show interfaces statistics               # counter summary
show interfaces queue ge-0/0/0           # queue depth and drops

# Aggregated Ethernet (LAG)
show interfaces ae0
show interfaces ae0 detail               # includes member link status
show lacp interfaces ae0                 # LACP PDU stats and state

# Optical / SFP
show interfaces ge-0/0/0 media           # optic type and media info
show chassis pic fpc 0 pic 0             # PIC/optic inventory
```

### Terse Output Fields

```
show interfaces terse
```
```
Interface               Admin Link Proto    Local                 Remote
ge-0/0/0                up    up
ge-0/0/0.0              up    up   inet     192.0.2.1/30
                                   iso
                                   mpls
ge-0/0/1                up    down
```

### Configuration Examples

```
# Basic L3 interface
set interfaces ge-0/0/0 description "To-Peer-Router"
set interfaces ge-0/0/0 unit 0 family inet address 192.0.2.1/30
set interfaces ge-0/0/0 unit 0 family iso           # enable IS-IS
set interfaces ge-0/0/0 unit 0 family mpls          # enable MPLS

# Loopback
set interfaces lo0 unit 0 family inet address 10.0.0.1/32
set interfaces lo0 unit 0 family iso address 49.0001.0100.0000.0001.00

# Disable interface
set interfaces ge-0/0/0 disable
```

---

## 5. VLAN Commands

### Ethernet Switching (EX / QFX / MX with bridge domains)

```
# Show VLAN table
show vlans                               # all VLANs
show vlans vlan-name VLAN100             # specific VLAN by name
show vlans 100                           # specific VLAN by ID

# MAC table
show ethernet-switching table            # MAC address table (EX/QFX)
show ethernet-switching table vlan VLAN100
show ethernet-switching table interface ge-0/0/1
show ethernet-switching table detail

# Spanning Tree
show spanning-tree bridge                # STP bridge state
show spanning-tree interface             # per-interface STP state
show spanning-tree mstp                  # MSTP specifics

# Interface VLAN membership
show ethernet-switching interface        # per-interface mode and VLANs
show ethernet-switching interface ge-0/0/1
```

### MX Router — Bridge Domains

```
show bridge domain                       # all bridge domains
show bridge domain BD100                 # specific domain
show bridge mac-table                    # MAC table across all BDs
show bridge mac-table bridge-domain BD100
show bridge statistics                   # per-BD packet counters
show bridge flooding                     # BUM flooding state
```

### VLAN Configuration Examples

```
# EX/QFX — define VLANs
set vlans VLAN100 vlan-id 100
set vlans VLAN100 description "Production"
set vlans VLAN100 l3-interface irb.100    # L3 gateway (IRB)

# Access port
set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode access
set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members VLAN100

# Trunk port
set interfaces ge-0/0/2 unit 0 family ethernet-switching interface-mode trunk
set interfaces ge-0/0/2 unit 0 family ethernet-switching vlan members [VLAN100 VLAN200 VLAN300]

# IRB (Integrated Routing and Bridging) — routed VLAN interface
set interfaces irb unit 100 family inet address 10.100.0.1/24

# MX — bridge domain
set bridge-domains BD100 vlan-id 100
set bridge-domains BD100 routing-interface irb.100
set bridge-domains BD100 interface ge-0/0/1.0
```

### Q-in-Q / VLAN Stacking

```
show interfaces ge-0/0/0 detail          # shows encapsulation type
# Config
set interfaces ge-0/0/0 encapsulation flexible-ethernet-services
set interfaces ge-0/0/0 unit 100 encapsulation vlan-bridge
set interfaces ge-0/0/0 unit 100 vlan-tags outer 100 inner 200
```

---

## 6. OSPF Commands

### Show Commands

```
show ospf overview                       # OSPF process summary, router-id, areas
show ospf neighbor                       # neighbor adjacencies
show ospf neighbor detail                # detailed neighbor state
show ospf neighbor instance all          # neighbors in all routing instances
show ospf interface                      # per-interface OSPF state
show ospf interface detail               # DR/BDR, hello/dead timers, costs
show ospf route                          # OSPF topology database routes
show ospf route detail                   # individual route details
show ospf database                       # LSDB summary
show ospf database detail                # full LSDB
show ospf database router detail         # Router LSAs only
show ospf database network detail        # Network LSAs only
show ospf database summary detail        # Summary LSAs
show ospf database external detail       # External (Type-5) LSAs
show ospf database area 0.0.0.0          # LSDB for specific area
show ospf statistics                     # packet and SPF counters
show ospf log                            # SPF and adjacency event log
```

### Route Table Integration

```
show route protocol ospf                 # OSPF routes in inet.0
show route protocol ospf detail
show route 10.0.0.0/8 detail            # check how a prefix was learned
```

### OSPFv3 (IPv6)

```
show ospf3 neighbor
show ospf3 interface
show ospf3 database
show ospf3 route
```

### Configuration Examples

```
# Basic OSPF
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
set protocols ospf area 0.0.0.0 interface lo0.0 passive

# Area types
set protocols ospf area 0.0.0.1 stub
set protocols ospf area 0.0.0.2 nssa

# Authentication (MD5)
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0 authentication md5 1 key "secretkey"

# Interface cost
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0 metric 10

# Redistribute connected
set policy-options policy-statement CONNECTED-TO-OSPF term 1 from protocol direct
set policy-options policy-statement CONNECTED-TO-OSPF term 1 then accept
set protocols ospf export CONNECTED-TO-OSPF

# Reference bandwidth (for cost calculation)
set protocols ospf reference-bandwidth 100g
```

---

## 7. ISIS Commands

### Show Commands

```
show isis overview                       # IS-IS process, NET, levels, interfaces
show isis adjacency                      # IS-IS neighbor adjacencies
show isis adjacency detail               # state, hold time, circuit type
show isis interface                      # per-interface IS-IS config and state
show isis interface detail               # metrics, timers, circuit type
show isis database                       # link-state PDU database (LSDB)
show isis database detail                # full TLV details
show isis database <system-id>           # specific LSP
show isis database level 2              # Level-2 LSDB only
show isis route                          # IS-IS computed routes
show isis route detail
show isis statistics                     # SPF runs, PDU counters
show isis log                            # adjacency and SPF events
show isis hostname                       # dynamic hostname mappings
show isis spf log                        # SPF computation history
show isis backup coverage               # LFA/RLFA backup coverage
```

### Route Table Integration

```
show route protocol isis
show route protocol isis detail
show route 10.0.0.0/8                   # check IS-IS learned routes
```

### Configuration Examples

```
# NET address: 49.AREA.SYSID.00
# Area: 49.0001, System ID from loopback 10.0.0.1 -> 0100.0000.0001
set interfaces lo0 unit 0 family iso address 49.0001.0100.0000.0001.00

# Enable IS-IS
set protocols isis interface ge-0/0/0.0
set protocols isis interface ge-0/0/0.0 level 2 metric 10
set protocols isis interface lo0.0 passive

# Level configuration
set protocols isis level 1 disable          # L2-only router
set protocols isis level 2 wide-metrics-only

# Authentication
set protocols isis interface ge-0/0/0.0 level 2 authentication-key "secretkey"
set protocols isis interface ge-0/0/0.0 level 2 authentication-type md5

# Redistribute routes
set policy-options policy-statement CONNECTED-TO-ISIS term 1 from protocol direct
set policy-options policy-statement CONNECTED-TO-ISIS term 1 then accept
set protocols isis export CONNECTED-TO-ISIS

# Segment Routing (SR-MPLS)
set protocols isis source-packet-routing srgb start-label 16000 index-range 8000
set protocols isis interface ge-0/0/0.0 level 2 post-convergence-lfa

# Node SID
set protocols isis source-packet-routing node-segment ipv4-index 1
```

---

## 8. BGP Commands

### Show Commands

```
show bgp summary                         # all peers, state, prefix counts
show bgp neighbor                        # all neighbor details
show bgp neighbor 192.0.2.2              # specific neighbor
show bgp neighbor 192.0.2.2 detail       # full neighbor detail + timers
show bgp group                           # peer groups and member counts
show bgp group IBGP detail
show bgp replication                     # BGP route reflection state

# Route table views
show route protocol bgp                  # all BGP routes in inet.0
show route protocol bgp detail           # with full path attributes
show route 10.0.0.0/8                    # lookup specific prefix
show route 10.0.0.0/8 detail            # detail with communities, AS path
show route 10.0.0.0/8 extensive         # everything including RPKI, etc.

# BGP-specific route views
show bgp neighbor 192.0.2.2 received-routes    # routes received from peer
show bgp neighbor 192.0.2.2 advertised-routes  # routes sent to peer
show bgp neighbor 192.0.2.2 accepted-routes    # received and passing policy

# Route tables beyond inet.0
show route table bgp.l3vpn.0             # L3VPN RIB
show route table inet.3                  # MPLS tunnel endpoints (BGP NH resolution)
show route table mpls.0                  # MPLS forwarding table

# Communities and attributes
show route community 65000:100 detail
show route aspath-regex "^65000 .*"
```

### Debugging BGP

```
show bgp neighbor 192.0.2.2 | match "State|Hold|Prefix"
show log bgpd                            # BGP process log
show log messages | match BGP

# Tracing (caution: verbose)
set protocols bgp traceoptions file bgp-trace
set protocols bgp traceoptions flag open
set protocols bgp traceoptions flag update
set protocols bgp traceoptions flag state
```

### Configuration Examples

```
# Basic iBGP
set protocols bgp group IBGP type internal
set protocols bgp group IBGP local-address 10.0.0.1
set protocols bgp group IBGP neighbor 10.0.0.2

# eBGP
set protocols bgp group EBGP type external
set protocols bgp group EBGP peer-as 65001
set protocols bgp group EBGP neighbor 192.0.2.2

# Local AS and router-id
set routing-options autonomous-system 65000
set routing-options router-id 10.0.0.1

# Route reflector
set protocols bgp group IBGP cluster 10.0.0.1

# Apply policy
set protocols bgp group EBGP import IMPORT-POLICY
set protocols bgp group EBGP export EXPORT-POLICY

# Next-hop self
set protocols bgp group IBGP next-hop-self

# MD5 authentication
set protocols bgp group EBGP neighbor 192.0.2.2 authentication-key "secret"

# BFD for BGP
set protocols bgp group EBGP neighbor 192.0.2.2 bfd-liveness-detection minimum-interval 300
set protocols bgp group EBGP neighbor 192.0.2.2 bfd-liveness-detection multiplier 3

# ADDPATH
set protocols bgp group IBGP family inet unicast add-path send path-count 6
```

### Policy and Communities

```
# Match community
set policy-options community MY-COMM members 65000:100
set policy-options policy-statement IMPORT term match-comm from community MY-COMM
set policy-options policy-statement IMPORT term match-comm then accept

# Set local-preference
set policy-options policy-statement IMPORT term set-localpref then local-preference 200

# AS path prepend
set policy-options policy-statement EXPORT term prepend then as-path-prepend "65000 65000"
```

---

## 9. MPLS Commands

### Show Commands

```
# LDP
show ldp neighbor                        # LDP session state
show ldp neighbor detail
show ldp session                         # LDP session detail
show ldp interface                       # LDP-enabled interfaces
show ldp database                        # LDP label bindings (local and remote)
show ldp database session 10.0.0.2      # bindings from specific peer
show ldp statistics                      # LDP PDU counters
show ldp route                           # FECs and next-hop resolution

# RSVP / Traffic Engineering
show rsvp session                        # all RSVP LSP sessions
show rsvp session detail                 # with ERO, RRO, bandwidth
show rsvp session name <LSP-name>
show rsvp neighbor                       # RSVP neighbors
show rsvp interface                      # RSVP-enabled interfaces
show rsvp statistics                     # RSVP signaling counters

# MPLS LSPs (RSVP-TE)
show mpls lsp                            # all LSPs, state, bandwidth
show mpls lsp detail                     # ERO, path, CSPF detail
show mpls lsp name <LSP-name>
show mpls lsp ingress                    # LSPs originating here
show mpls lsp egress                     # LSPs terminating here
show mpls lsp transit                    # LSPs passing through
show mpls lsp statistics                 # per-LSP traffic counters
show mpls lsp extensive                  # everything

# MPLS forwarding
show mpls interface                      # MPLS-enabled interfaces
show route table mpls.0                  # MPLS label forwarding table
show route table mpls.0 detail
show route label 300016                  # specific label lookup

# Path computation
show ted database                        # Traffic Engineering Database (TED)
show ted database detail                 # full TED including TE metrics
show ted link                            # TE link state

# Segment Routing
show spring-traffic-engineering lsp      # SR-TE LSPs
show spring-traffic-engineering lsp detail
show route table inet.3                  # colored (ODN) next-hops
```

### L3VPN

```
show route table <vpn-name>.inet.0      # VRF routing table
show bgp neighbor 10.0.0.2 received-routes table <vpn-name>.inet.0
show l3vpn vpn-instance <name>          # Not JunOS — see below

# JunOS VRF view
show route instance                      # all routing instances
show route instance <VPN-NAME>
show route instance <VPN-NAME> detail
show route table <VPN-NAME>.inet.0
```

### Configuration Examples

```
# Enable MPLS on interface
set interfaces ge-0/0/0 unit 0 family mpls
set protocols mpls interface ge-0/0/0.0

# LDP
set protocols ldp interface ge-0/0/0.0
set protocols ldp interface lo0.0

# RSVP-TE LSP
set protocols mpls label-switched-path TO-R2 to 10.0.0.2
set protocols mpls label-switched-path TO-R2 primary PATH-TO-R2
set protocols mpls path PATH-TO-R2 10.0.1.1 strict
set protocols mpls path PATH-TO-R2 10.0.0.2 strict

# RSVP
set protocols rsvp interface ge-0/0/0.0

# L3VPN
set routing-instances CUST-A instance-type vrf
set routing-instances CUST-A interface ge-0/0/1.0
set routing-instances CUST-A route-distinguisher 65000:100
set routing-instances CUST-A vrf-target target:65000:100
set routing-instances CUST-A protocols bgp group CE type external
set routing-instances CUST-A protocols bgp group CE peer-as 65100
set routing-instances CUST-A protocols bgp group CE neighbor 172.16.0.2
```

---

## 10. IPv6 Commands

### Key IPv6 Concepts in JunOS

In JunOS, IPv4 and IPv6 are handled as separate protocol families (`inet` vs `inet6`) within the same interface unit. IPv6 routes live in `inet6.0` (the primary IPv6 RIB), and each routing protocol has a distinct IPv6 variant (`ospf3`, `family inet6` under BGP, IS-IS topology `ipv6-unicast`).

```
# IPv4 → inet family,  inet.0 RIB
# IPv6 → inet6 family, inet6.0 RIB
# Both can coexist on the same interface unit simultaneously
```

### IPv6 Interface Show Commands

```
show interfaces terse                            # shows inet6 addresses alongside inet
show interfaces ge-0/0/0                         # includes IPv6 link-local and global
show interfaces ge-0/0/0 detail                  # full detail with inet6 stats
show interfaces routing                          # routing-relevant info including inet6

# Confirm IPv6 is enabled on a unit
show interfaces ge-0/0/0.0 | match inet6
```

Sample `show interfaces terse` with dual-stack:
```
Interface               Admin Link Proto    Local                 Remote
ge-0/0/0.0              up    up   inet     192.0.2.1/30
                                   inet6    2001:db8:1::1/64
                                            fe80::1/64
                                   mpls
                                   iso
```

### IPv6 Addresses — NDP (Neighbor Discovery)

NDP is the IPv6 replacement for ARP. JunOS uses `show ipv6 neighbors` and related commands.

```
show ipv6 neighbors                              # NDP neighbor cache (like show arp)
show ipv6 neighbors detail                       # state, flags, interface
show ipv6 neighbors interface ge-0/0/0           # NDP table for specific interface
show ipv6 neighbors 2001:db8::1                  # lookup specific neighbor

# Router advertisements
show ipv6 router-advertisement                   # RA state per interface
show ipv6 router-advertisement interface ge-0/0/0
```

NDP neighbor states:
```
Incomplete  # MAC not yet resolved
Reachable   # recently confirmed reachable
Stale       # reachability not confirmed recently (still usable)
Delay       # waiting to probe
Probe       # actively probing
```

### IPv6 Routing Table

```
show route table inet6.0                         # full IPv6 routing table
show route table inet6.0 summary                 # prefix count by protocol
show route table inet6.0 protocol bgp            # IPv6 BGP routes
show route table inet6.0 protocol ospf           # OSPFv3 routes
show route table inet6.0 protocol isis           # IS-IS IPv6 routes
show route table inet6.0 protocol direct         # directly connected IPv6

# Shorthand — JunOS infers inet6 when given an IPv6 prefix
show route 2001:db8::/32
show route 2001:db8::1/128 detail
show route 2001:db8::/32 exact
show route ::/0                                  # IPv6 default route

# Active route details
show route 2001:db8:100::/48 detail
show route 2001:db8:100::/48 extensive           # all path attributes, RPKI state
```

### IPv6 Ping and Traceroute

```
ping 2001:db8::1                                 # IPv6 ping
ping 2001:db8::1 count 5
ping 2001:db8::1 source 2001:db8:1::1            # specify source address
ping 2001:db8::1 routing-instance CUST-A         # ping from VRF

traceroute 2001:db8::1
traceroute 2001:db8::1 source 2001:db8:1::1
```

### OSPFv3 (OSPF for IPv6)

JunOS uses `ospf3` for OSPFv3. It is a completely separate process from `ospf`.

```
show ospf3 overview                              # OSPFv3 process summary
show ospf3 neighbor                              # OSPFv3 adjacencies
show ospf3 neighbor detail                       # state, timers, DR/BDR
show ospf3 neighbor instance all                 # neighbors across all instances
show ospf3 interface                             # per-interface OSPFv3 state
show ospf3 interface detail                      # hello/dead timers, cost, DR/BDR
show ospf3 database                              # OSPFv3 LSDB summary
show ospf3 database detail                       # full LSDB with all TLVs
show ospf3 database router detail                # Router LSAs
show ospf3 database network detail               # Network LSAs
show ospf3 database inter-area-prefix detail     # Inter-Area Prefix LSAs (replaces Summary)
show ospf3 database external detail              # AS External LSAs
show ospf3 database area 0.0.0.0                # LSDB for specific area
show ospf3 route                                 # OSPFv3 computed routes
show ospf3 route detail
show ospf3 statistics                            # PDU and SPF counters
show ospf3 log                                   # adjacency and SPF events

# OSPFv3 routes in the routing table
show route table inet6.0 protocol ospf
```

**OSPFv3 Configuration:**

```
# OSPFv3 uses inet6 family — interfaces need family inet6
set interfaces ge-0/0/0 unit 0 family inet6 address 2001:db8:1::1/64

# Enable OSPFv3
set protocols ospf3 area 0.0.0.0 interface ge-0/0/0.0
set protocols ospf3 area 0.0.0.0 interface lo0.0 passive

# Area types
set protocols ospf3 area 0.0.0.1 stub
set protocols ospf3 area 0.0.0.2 nssa

# Interface cost
set protocols ospf3 area 0.0.0.0 interface ge-0/0/0.0 metric 10

# Authentication (IPsec-based in OSPFv3)
set protocols ospf3 area 0.0.0.0 interface ge-0/0/0.0 ipsec-sa OSPFv3-SA
set security ipsec security-association OSPFv3-SA mode transport
set security ipsec security-association OSPFv3-SA manual direction bidirectional
set security ipsec security-association OSPFv3-SA manual direction bidirectional protocol ah
set security ipsec security-association OSPFv3-SA manual direction bidirectional spi 256
set security ipsec security-association OSPFv3-SA manual direction bidirectional authentication hmac-md5-96 key "secretkey"

# Redistribute into OSPFv3
set policy-options policy-statement V6-CONNECTED term 1 from protocol direct
set policy-options policy-statement V6-CONNECTED term 1 from family inet6
set policy-options policy-statement V6-CONNECTED term 1 then accept
set protocols ospf3 export V6-CONNECTED

# Reference bandwidth
set protocols ospf3 reference-bandwidth 100g
```

### IS-IS with IPv6

IS-IS natively supports both IPv4 and IPv6 in the same adjacency. In JunOS, you enable the `ipv6-unicast` topology or use the default multi-topology extension.

```
# Show IS-IS IPv6 topology info
show isis overview                               # includes ipv6 topology state
show isis adjacency                              # same adjacency serves both families
show isis database detail                        # look for TLV 236 (IPv6 reachability)
show isis route                                  # IPv4 routes
show route table inet6.0 protocol isis           # IPv6 routes via IS-IS
show isis spf log                                # SPF for both topologies

# Confirm IPv6 reachability TLVs in LSDB
show isis database detail | match "IPv6\|2001"
```

**IS-IS IPv6 Configuration:**

```
# Interface must have both iso and inet6 families
set interfaces ge-0/0/0 unit 0 family iso
set interfaces ge-0/0/0 unit 0 family inet6 address 2001:db8:1::1/64

# IS-IS with wide metrics (required for multi-topology IPv6)
set protocols isis level 2 wide-metrics-only

# Enable IPv6 topology (MT-ISIS)
set protocols isis topologies ipv6-unicast

# Per-interface IPv6 metric (optional)
set protocols isis interface ge-0/0/0.0 level 2 ipv6-unicast-metric 10

# IPv6 loopback for IS-IS advertisement
set interfaces lo0 unit 0 family inet6 address 2001:db8:0:1::1/128
set protocols isis interface lo0.0 passive

# Redistribute IPv6 routes into IS-IS
set policy-options policy-statement V6-TO-ISIS term 1 from protocol direct
set policy-options policy-statement V6-TO-ISIS term 1 from family inet6
set policy-options policy-statement V6-TO-ISIS term 1 then accept
set protocols isis export V6-TO-ISIS
```

### BGP for IPv6

JunOS BGP uses `family inet6 unicast` for IPv6 address family (AFI 2 SAFI 1). IPv6 BGP peers can be configured on the same group as IPv4 or in a dedicated group.

```
# BGP IPv6 summary (inet6.0 table)
show bgp summary                                 # shows all families including inet6
show route table inet6.0 protocol bgp            # all BGP IPv6 routes
show route table inet6.0 protocol bgp detail     # with full attributes

# Per-neighbor IPv6 route views
show bgp neighbor 2001:db8::2 received-routes
show bgp neighbor 2001:db8::2 advertised-routes
show bgp neighbor 2001:db8::2 accepted-routes

# Specific prefix lookup
show route 2001:db8:100::/48 detail
show route 2001:db8:100::/48 extensive           # AS path, communities, RPKI

# BGP communities on IPv6 routes
show route table inet6.0 community 65000:100 detail

# inet6.3 — IPv6 MPLS tunnel table (6PE next-hops)
show route table inet6.3
```

**BGP IPv6 Configuration:**

```
# iBGP with IPv6 address family
set protocols bgp group IBGP-V6 type internal
set protocols bgp group IBGP-V6 local-address 2001:db8:0:1::1
set protocols bgp group IBGP-V6 family inet6 unicast
set protocols bgp group IBGP-V6 neighbor 2001:db8:0:2::1

# eBGP IPv6 peer
set protocols bgp group EBGP-V6 type external
set protocols bgp group EBGP-V6 peer-as 65001
set protocols bgp group EBGP-V6 family inet6 unicast
set protocols bgp group EBGP-V6 neighbor 2001:db8:peer::2

# Dual-stack BGP group (IPv4 peer, carry both families)
# Uses RFC 5549 (IPv6 NH for IPv4 routes) or separate groups
set protocols bgp group DUAL-STACK family inet unicast
set protocols bgp group DUAL-STACK family inet6 unicast
set protocols bgp group DUAL-STACK neighbor 192.0.2.2

# next-hop-self for IPv6 iBGP
set protocols bgp group IBGP-V6 next-hop-self

# Apply policy to IPv6 group
set protocols bgp group EBGP-V6 import V6-IMPORT
set protocols bgp group EBGP-V6 export V6-EXPORT

# BGP multipath for IPv6
set routing-options rib inet6.0 multipath

# Route reflector for IPv6
set protocols bgp group IBGP-V6 cluster 10.0.0.1
```

### 6PE and 6VPE (IPv6 over MPLS)

6PE carries IPv6 prefixes across an IPv4/MPLS core using BGP labeled-unicast. 6VPE does the same for VPN customers.

```
# 6PE route table — labeled IPv6 unicast
show route table inet6.0 protocol bgp            # 6PE routes appear here
show route table inet6.3                         # labeled IPv6 routes (tunnel table)
show bgp neighbor 10.0.0.2 received-routes table inet6.0

# 6VPE — IPv6 VPN RIB
show route table CUST-A.inet6.0                  # IPv6 VRF table
show route instance CUST-A
show route instance CUST-A detail

# Verify MPLS label for IPv6 prefix
show route 2001:db8:100::/48 detail | match label
```

**6PE Configuration:**

```
# BGP family for 6PE (labeled IPv6)
set protocols bgp group 6PE type internal
set protocols bgp group 6PE family inet6 labeled-unicast
set protocols bgp group 6PE neighbor 10.0.0.2

# 6VPE — routing instance with inet6
set routing-instances CUST-A instance-type vrf
set routing-instances CUST-A interface ge-0/0/1.0
set routing-instances CUST-A route-distinguisher 65000:200
set routing-instances CUST-A vrf-target target:65000:200
set routing-instances CUST-A protocols bgp group CE-V6 type external
set routing-instances CUST-A protocols bgp group CE-V6 peer-as 65100
set routing-instances CUST-A protocols bgp group CE-V6 family inet6 unicast
set routing-instances CUST-A protocols bgp group CE-V6 neighbor 2001:db8:ce::2
```

### IPv6 Firewall Filters

```
# Show IPv6 firewall filter counters
show firewall filter V6-FILTER                   # hit counts per term
show firewall filter V6-FILTER detail
show firewall log                                # recent filter log entries (inet and inet6)
```

**IPv6 Firewall Filter Configuration:**

```
# IPv6 uses 'family inet6' — separate from IPv4 'family inet' filters
set firewall family inet6 filter V6-FILTER term ALLOW-ICMPV6 from next-header icmpv6
set firewall family inet6 filter V6-FILTER term ALLOW-ICMPV6 from icmp-type [echo-request echo-reply neighbor-solicit neighbor-advertisement router-advertisement]
set firewall family inet6 filter V6-FILTER term ALLOW-ICMPV6 then accept

set firewall family inet6 filter V6-FILTER term BLOCK-BOGONS from source-address 2001:db8::/32
set firewall family inet6 filter V6-FILTER term BLOCK-BOGONS then discard

set firewall family inet6 filter V6-FILTER term ACCEPT-ALL then accept

# Apply to interface (separate from inet filter)
set interfaces ge-0/0/0 unit 0 family inet6 filter input V6-FILTER
```

### DHCPv6 and Router Advertisements (RA)

```
# Show RA configuration and state
show ipv6 router-advertisement
show ipv6 router-advertisement interface ge-0/0/0

# DHCPv6 local server (EX/QFX access layer)
show dhcpv6 server binding                       # active DHCPv6 leases
show dhcpv6 server binding detail
show dhcpv6 server statistics
show dhcpv6 relay statistics                     # if acting as DHCPv6 relay
```

**RA and DHCPv6 Configuration:**

```
# Enable RA on interface (SLAAC)
set protocols router-advertisement interface ge-0/0/0.0 prefix 2001:db8:100::/64

# RA with managed flag (M-bit) — tells clients to use DHCPv6 for address
set protocols router-advertisement interface ge-0/0/0.0 managed-configuration

# RA with other flag (O-bit) — use DHCPv6 for options only (DNS, etc.)
set protocols router-advertisement interface ge-0/0/0.0 other-stateful-configuration

# RA interval and lifetime
set protocols router-advertisement interface ge-0/0/0.0 max-advertisement-interval 30
set protocols router-advertisement interface ge-0/0/0.0 default-lifetime 200

# DHCPv6 local server
set system services dhcp-local-server dhcpv6 group LAN interface ge-0/0/0.0
set access address-assignment pool V6-POOL family inet6 prefix 2001:db8:100::/64
set access address-assignment pool V6-POOL family inet6 range CLIENT-RANGE low 2001:db8:100::100
set access address-assignment pool V6-POOL family inet6 range CLIENT-RANGE high 2001:db8:100::1ff
set access address-assignment pool V6-POOL family inet6 dhcp-attributes dns-server [2001:db8:53::1]

# DHCPv6 relay
set forwarding-options dhcp-relay group V6-RELAY active-server-group V6-SERVERS
set forwarding-options dhcp-relay group V6-RELAY interface ge-0/0/1.0
set forwarding-options dhcp-relay server-group V6-SERVERS 2001:db8:dhcp::1
```

### IPv6 Configuration Reference

```
# Dual-stack interface — most common pattern
set interfaces ge-0/0/0 unit 0 family inet  address 192.0.2.1/30
set interfaces ge-0/0/0 unit 0 family inet6 address 2001:db8:1::1/64

# IPv6-only interface
set interfaces ge-0/0/0 unit 0 family inet6 address 2001:db8:1::1/64

# Link-local only (auto-generated — no config needed, but can be set explicitly)
set interfaces ge-0/0/0 unit 0 family inet6 address fe80::1/64

# IPv6 loopback
set interfaces lo0 unit 0 family inet6 address 2001:db8:0:1::1/128

# Static IPv6 default route
set routing-options rib inet6.0 static route ::/0 next-hop 2001:db8:1::2

# Static IPv6 route
set routing-options rib inet6.0 static route 2001:db8:100::/48 next-hop 2001:db8:1::2

# IPv6 multipath
set routing-options rib inet6.0 multipath

# Aggregate/summary route
set routing-options rib inet6.0 aggregate route 2001:db8::/32
```

### IPv6 Cross-Platform Comparison

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| Show IPv6 interfaces | `show interfaces terse` (includes inet6) | `show ipv6 interface brief` | `show ipv6 interface brief` |
| IPv6 NDP table | `show ipv6 neighbors` | `show ipv6 neighbors` | `show ipv6 neighbors` |
| IPv6 route table | `show route table inet6.0` | `show ipv6 route` | `show route ipv6` |
| IPv6 default route | `show route ::/0` | `show ipv6 route ::/0` | `show route ipv6 ::/0` |
| IPv6 BGP summary | `show bgp summary` (all families) | `show bgp ipv6 unicast summary` | `show bgp ipv6 unicast summary` |
| IPv6 BGP routes | `show route table inet6.0 protocol bgp` | `show bgp ipv6 unicast` | `show bgp ipv6 unicast` |
| OSPFv3 neighbors | `show ospf3 neighbor` | `show ipv6 ospf neighbor` | `show ospfv3 neighbor` |
| OSPFv3 database | `show ospf3 database` | `show ipv6 ospf database` | `show ospfv3 database` |
| IS-IS IPv6 routes | `show route table inet6.0 protocol isis` | `show ipv6 route isis` | `show route ipv6 isis` |
| IPv6 ping | `ping 2001:db8::1` | `ping ipv6 2001:db8::1` | `ping 2001:db8::1` |
| IPv6 traceroute | `traceroute 2001:db8::1` | `traceroute ipv6 2001:db8::1` | `traceroute 2001:db8::1` |
| RA config | `protocols router-advertisement` | `ipv6 nd ra ...` (interface) | `ipv6 nd ra ...` (interface) |
| IPv6 firewall | `firewall family inet6 filter` | `ipv6 access-list` | `ipv6 access-list` |
| DHCPv6 relay | `forwarding-options dhcp-relay` | `ipv6 dhcp relay destination` | `ipv6 dhcp relay destination` |
| 6PE | `family inet6 labeled-unicast` | `address-family ipv6 vrf` (with MPLS) | `address-family ipv6 unicast` (with MPLS) |
| IPv6 static route | `set routing-options rib inet6.0 static route` | `ipv6 route` | `router static address-family ipv6` |

---

## 11. Configuration Management  

### Viewing and Comparing Configuration

```
show configuration                       # full active config (hierarchical)
show configuration | display set         # flat set-command format
show configuration | display set | no-more
show configuration protocols ospf        # specific section
show configuration | compare             # diff candidate vs active
show configuration | compare rollback 1  # diff active vs rollback 1
show system commit                       # commit history
rollback ?                               # show available rollback points (0–49)
```

### Commit Operations

```
commit                                   # apply candidate config
commit confirmed 5                       # commit, auto-rollback in 5 min if not confirmed
commit confirmed 10 comment "testing OSPF change"
commit comment "adding new BGP peer"    # commit with log message
commit check                             # validate without applying
commit and-quit                          # commit and return to op mode
rollback 1                               # revert to previous config
rollback 5                               # revert to 5 commits ago
```

### Editing Configuration

```
# Set commands
set protocols ospf area 0 interface ge-0/0/0.0
delete protocols ospf area 0 interface ge-0/0/1.0
rename interfaces ge-0/0/0 to ge-0/0/5   # rename stanzas

# Edit and show within hierarchy
edit protocols bgp group IBGP
show                                     # show current stanza
set neighbor 10.0.0.5                    # relative to current level
top                                      # return to root

# Deactivate without deleting
deactivate protocols ospf area 0.0.0.1
activate protocols ospf area 0.0.0.1
```

### Load and Save

```
save /var/tmp/config-backup.txt          # save config to file
load override /var/tmp/config-backup.txt # replace entire config
load merge /var/tmp/additions.txt        # merge into existing config
load patch /var/tmp/diff.txt             # apply a diff/patch
load factory-default                     # reset to factory config
```

### Rescue Configuration

```
request system configuration rescue save    # save current as rescue config
request system configuration rescue delete  # delete rescue config
rollback rescue                             # load rescue config
```

---

## 12. ACX Platform-Specific Details

The ACX (Access Cloud Exchange) series is Juniper's metro and access aggregation router family. It runs full JunOS but has distinct hardware capabilities, feature profiles, and operational considerations compared to the MX.

### ACX Hardware Overview

| Platform | Role | Key Interfaces | Notes |
|---|---|---|---|
| ACX500 | Ultra-compact access | 8×GE + 2×SFP | Fanless, wall-mount; PTP slave only |
| ACX1000 | Access aggregation | 16×GE + 2×10GE | Fixed form factor |
| ACX2000 | Metro aggregation | 20×GE + 4×10GE | SyncE + PTP BC |
| ACX4000 | Multi-service edge | Modular, up to 40×10GE | Full timing stack, pseudowires |
| ACX5048 / ACX5096 | High-density access | 48/96×GE + 10GE uplinks | Data-center-style density |
| ACX6360 | 100G metro aggregation | 36×100GE | High-scale MPLS + timing |
| ACX7024 / ACX7100 | Next-gen access | 24–48×25GE + 400GE uplinks | SR-MPLS, EVPN, segment routing |
| ACX7509 | Next-gen aggregation | Modular, 400GE | Full SR-MPLS, EVPN, telemetry |

### ACX Feature Profile vs. MX

| Feature | ACX (older: 1K–4K) | ACX7000 series | MX |
|---|---|---|---|
| L3 routing (OSPF/IS-IS/BGP) | Yes | Yes | Yes |
| MPLS / LDP / RSVP-TE | Yes | Yes | Yes |
| Segment Routing (SR-MPLS) | Limited | Full | Full |
| EVPN | Limited/no | Full | Full |
| L2circuit (pseudowire) | Yes | Yes | Yes |
| VPLS | Yes | Yes | Yes |
| PTP / IEEE 1588v2 | BC + OC | BC + TC + OC | BC (with timing card) |
| SyncE | Yes | Yes | Yes |
| GNSS/GPS | External (ACX4000+) | Internal option | With timing card |
| BITS timing | Yes | Yes | Yes |
| CFM / Y.1731 OAM | Yes | Yes | Yes |
| Subscriber management | No | Limited | Full (with MS-MPC) |
| Firewall filter scale | Smaller TCAM | Larger TCAM | Very large TCAM |
| IRB (L3 on bridge domain) | Limited | Yes | Yes |

---

### Timing and Synchronization

Timing is the defining capability of the ACX series for metro/access deployments. ACX routers are commonly deployed as IEEE 1588v2 Boundary Clocks (BC) and SyncE sources for mobile fronthaul/backhaul (4G/5G) and financial networks.

#### Clock Hierarchy

```
GNSS/GPS / BITS  →  Grand Master (GM)  →  ACX Boundary Clock (BC)  →  Slave devices
SyncE flows independently on the physical layer alongside PTP messages
```

#### PTP Show Commands

```
show ptp clock                                   # local clock identity, domain, state
show ptp master-slave-table                      # all PTP master/slave relationships
show ptp master-slave-table detail               # offset, path delay, interface
show ptp port                                    # per-port PTP state (Master/Slave/Passive)
show ptp port detail                             # announce interval, sync interval, role
show ptp statistics                              # per-port message counters
show ptp statistics detail
show ptp lock-status                             # clock servo lock state (LOCKED/HOLDOVER/FREERUN)
show ptp global-information                      # domain, clock class, priority1/2
show ptp path-trace                              # path trace TLV (if enabled)
```

PTP lock states:
```
ACQUIRING    # searching for master, not yet locked
PHASE_LOCKED # synchronized to master
HOLDOVER     # master lost, coasting on local oscillator
FREERUN      # no master, running on internal clock only
```

#### SyncE Show Commands

```
show synchronization                             # overall sync source and status
show synchronization detail                      # SSM QL values, interface states
show interfaces ge-0/0/0 detail | match "Clock\|Sync\|ESMC"
show chassis synchronization                     # chassis-level sync state (some platforms)
```

SSM Quality Levels (QL) in priority order:
```
QL-PRC   # Primary Reference Clock (highest quality, from GNSS)
QL-SSU-A # Synchronization Supply Unit - Type A
QL-SSU-B # Synchronization Supply Unit - Type B
QL-EEC1  # Ethernet Equipment Clock - Option 1
QL-DNU   # Do Not Use (loop prevention)
```

#### GNSS Show Commands (ACX with GNSS module)

```
show chassis gnss                                # satellite lock, signal quality
show chassis gnss detail                         # satellite count, fix type, coordinates
show chassis gnss satellites                     # per-satellite SNR and status
```

#### BITS Show Commands

```
show chassis synchronization                     # BITS input/output state and QL
```

#### Timing Configuration

```
# PTP Boundary Clock — basic setup
set protocols ptp clock-mode boundary
set protocols ptp domain 24
set protocols ptp priority1 128
set protocols ptp priority2 128
set protocols ptp local-ip-address 192.0.2.1     # source IP for PTP messages

# PTP slave interface (toward GM)
set protocols ptp interface ge-0/0/0.0 role slave
set protocols ptp interface ge-0/0/0.0 transport ipv4
set protocols ptp interface ge-0/0/0.0 unicast-mode master-ip 192.0.2.100

# PTP master interface (toward downstream slaves)
set protocols ptp interface ge-0/0/1.0 role master
set protocols ptp interface ge-0/0/1.0 transport ipv4

# SyncE — enable on interface
set interfaces ge-0/0/0 synchronous-ethernet

# SyncE — set QL threshold and source
set protocols synchronous-ethernet interface ge-0/0/0 wait-to-restore 300
set protocols synchronous-ethernet interface ge-0/0/0 priority 1

# GNSS as timing source (ACX4000/7000 with GNSS)
set chassis gnss-options source primary          # use GNSS as primary timing ref

# BITS input
set chassis synchronization bits-in-1 interface bits-0/0/0
```

---

### Carrier Ethernet OAM

ACX routers are central to MEF-compliant Carrier Ethernet services. OAM is essential for SLA monitoring and fault isolation.

#### CFM / 802.1ag Show Commands

```
show oam ethernet connectivity-fault-management  # all CFM domains and MAs
show oam ethernet connectivity-fault-management mep interface ge-0/0/0.0
show oam ethernet connectivity-fault-management mep detail
show oam ethernet connectivity-fault-management continuity-check  # CC state per MEP
show oam ethernet connectivity-fault-management database          # remote MEP entries
show oam ethernet connectivity-fault-management linktrace         # LTR results
show oam ethernet connectivity-fault-management loopback          # LBR results
```

CFM/OAM key terms:
```
MD   Maintenance Domain (carrier, service, customer — levels 0–7)
MA   Maintenance Association (one per service/VLAN within an MD)
MEP  Maintenance End Point (at service edge — generates/terminates CCMs)
MIP  Maintenance Intermediate Point (transparent to CCMs, responds to LTR)
CCM  Continuity Check Message (periodic heartbeats, default 1s)
LBM  Loopback Message (like ping between MEPs)
LTR  Linktrace Reply (like traceroute between MEPs)
```

#### Y.1731 Performance Monitoring Show Commands

```
show oam ethernet connectivity-fault-management delay-statistics   # frame delay (FD)
show oam ethernet connectivity-fault-management delay-variation    # frame delay variation (FDV)
show oam ethernet connectivity-fault-management loss-statistics    # frame loss ratio (FLR)
show oam ethernet connectivity-fault-management detail interface ge-0/0/0.0
```

#### CFM / Y.1731 Configuration

```
# Maintenance Domain
set protocols oam ethernet connectivity-fault-management maintenance-domain CARRIER level 4

# Maintenance Association
set protocols oam ethernet connectivity-fault-management maintenance-domain CARRIER maintenance-association MA-SVC-100 continuity-check interval 1s
set protocols oam ethernet connectivity-fault-management maintenance-domain CARRIER maintenance-association MA-SVC-100 mep 1 interface ge-0/0/0.0 direction down
set protocols oam ethernet connectivity-fault-management maintenance-domain CARRIER maintenance-association MA-SVC-100 mep 1 auto-discovery

# Y.1731 delay measurement (ETH-DM)
set protocols oam ethernet connectivity-fault-management maintenance-domain CARRIER maintenance-association MA-SVC-100 mep 1 performance-monitoring sla-iterator-profiles DELAY-PROFILE
set protocols oam ethernet connectivity-fault-management sla-iterator-profiles DELAY-PROFILE measurement-type two-way-delay
set protocols oam ethernet connectivity-fault-management sla-iterator-profiles DELAY-PROFILE iteration-period 1s
```

#### TWAMP (Two-Way Active Measurement Protocol)

TWAMP is used on ACX for IP performance monitoring (latency, jitter, packet loss) toward other network elements.

```
show services rpm twamp                          # TWAMP server and client state
show services rpm twamp client sessions          # active TWAMP-Light client sessions
show services rpm twamp server sessions          # TWAMP server sessions
show services rpm twamp client probe-results     # per-probe delay and loss results
show services rpm probe-results                  # RPM probe results (all types)
show services rpm history-results                # historical RPM results
```

**TWAMP Configuration:**

```
# TWAMP server
set services rpm twamp server authentication-mode none
set services rpm twamp server port 862

# TWAMP client (probe toward remote server)
set services rpm probe TWAMP-TEST test LATENCY-CHECK probe-type twamp
set services rpm probe TWAMP-TEST test LATENCY-CHECK target address 192.0.2.100
set services rpm probe TWAMP-TEST test LATENCY-CHECK probe-count 10
set services rpm probe TWAMP-TEST test LATENCY-CHECK probe-interval 1
set services rpm probe TWAMP-TEST test LATENCY-CHECK test-interval 60
set services rpm probe TWAMP-TEST test LATENCY-CHECK source-address 192.0.2.1
```

---

### L2 Services (Pseudowire and VPLS)

ACX routers are primary PE devices for MEF E-Line (VPWS) and E-LAN (VPLS) services.

#### L2circuit (Pseudowire / VPWS / E-Line)

```
show l2circuit connections                       # all pseudowire connections and state
show l2circuit connections detail                # label, interface, VC ID, neighbor
show l2circuit connections neighbor 10.0.0.2    # pseudowires to specific PE
show l2circuit connections interface ge-0/0/1.0 # pseudowires on specific interface
show l2circuit statistics                        # per-VC packet/byte counters
```

Pseudowire states:
```
Up      # forwarding
Dn      # down — check interface, LDP session, remote PE
WE      # waiting for remote end
NC      # not connected
OL      # out of memory / overloaded
```

**L2circuit Configuration:**

```
# VLAN-based pseudowire (E-Line over MPLS)
set interfaces ge-0/0/1 encapsulation flexible-ethernet-services
set interfaces ge-0/0/1 unit 100 encapsulation vlan-ccc
set interfaces ge-0/0/1 unit 100 vlan-id 100
set interfaces ge-0/0/1 unit 100 family ccc

set protocols l2circuit neighbor 10.0.0.2 interface ge-0/0/1.100 virtual-circuit-id 100
set protocols l2circuit neighbor 10.0.0.2 interface ge-0/0/1.100 encapsulation-type ethernet-vlan
```

#### VPLS (E-LAN)

```
show vpls connections                            # all VPLS instances and PE neighbors
show vpls connections detail                     # label, state, MAC count per instance
show vpls connections instance VPLS-SVC-A       # specific VPLS instance
show vpls mac-table                              # MAC table for all VPLS instances
show vpls mac-table instance VPLS-SVC-A         # MAC table for specific instance
show vpls statistics                             # per-instance traffic counters
show bridge domain                               # bridge domain state (MX-style on newer ACX)
```

**VPLS Configuration:**

```
set routing-instances VPLS-SVC-A instance-type vpls
set routing-instances VPLS-SVC-A interface ge-0/0/1.200
set routing-instances VPLS-SVC-A route-distinguisher 65000:200
set routing-instances VPLS-SVC-A vrf-target target:65000:200
set routing-instances VPLS-SVC-A protocols vpls site CE-SITE-1 site-identifier 1
set routing-instances VPLS-SVC-A protocols vpls site CE-SITE-1 interface ge-0/0/1.200
set routing-instances VPLS-SVC-A protocols vpls mesh-group MESH-1 neighbor 10.0.0.3
set routing-instances VPLS-SVC-A protocols vpls mesh-group MESH-1 neighbor 10.0.0.4
```

---

### EVPN (ACX7000 Series)

ACX7000-series routers support full EVPN with BGP control plane.

```
show evpn instance                               # all EVPN instances and state
show evpn instance detail                        # per-instance detail, VNI, RT
show evpn database                               # EVPN MAC/IP table
show evpn database instance EVPN-SVC-A          # per-instance MAC/IP
show evpn database mac-address aa:bb:cc:dd:ee:ff # lookup specific MAC
show evpn l3-context                             # IRB/L3 VRF bindings
show evpn neighbor                               # EVPN BGP neighbors
show evpn multicast-snooping                     # IGMP/MLD snooping state
show evpn statistics                             # EVPN control-plane counters

# EVPN route types in the BGP table
show route table bgp.evpn.0                      # all EVPN NLRIs
show route table bgp.evpn.0 detail               # type 1–5 route detail
show route table bgp.evpn.0 | match "Type"       # count routes by type
```

EVPN Route Types:
```
Type 1  Ethernet Auto-Discovery (A-D) — per-EVI or per-ES
Type 2  MAC/IP Advertisement
Type 3  Inclusive Multicast Ethernet Tag (IMET) — BUM flooding
Type 4  Ethernet Segment — ES election
Type 5  IP Prefix Advertisement — L3 EVPN
```

**EVPN Configuration (ACX7000):**

```
# EVPN-VXLAN (data-center interconnect / metro)
set routing-instances EVPN-SVC-A instance-type evpn
set routing-instances EVPN-SVC-A route-distinguisher 65000:300
set routing-instances EVPN-SVC-A vrf-target target:65000:300
set routing-instances EVPN-SVC-A protocols evpn extended-vni-list 10300
set routing-instances EVPN-SVC-A protocols evpn encapsulation vxlan
set routing-instances EVPN-SVC-A bridge-domains BD300 vlan-id 300
set routing-instances EVPN-SVC-A bridge-domains BD300 vxlan vni 10300
set routing-instances EVPN-SVC-A bridge-domains BD300 routing-interface irb.300

# BGP family for EVPN
set protocols bgp group IBGP family evpn signaling
```

---

### ACX Chassis and Hardware Commands

```
show chassis hardware                            # all FRUs, serial numbers, part numbers
show chassis hardware detail                     # firmware versions, revision info
show chassis routing-engine                      # RE CPU, memory, uptime, mastership
show chassis fpc                                 # FPC/PIC state (modular ACX platforms)
show chassis fpc detail
show chassis fpc pic-status                      # PIC state per FPC slot
show chassis environment                         # temperature, fan, PSU state
show chassis environment cb                      # control board environment
show chassis environment fpc                     # per-FPC temperatures
show chassis power                               # power consumption and capacity
show chassis alarms                              # active hardware alarms
show system alarms                               # active software alarms
show chassis craft-interface                     # front-panel LEDs and alarm state

# Interface/optic details
show interfaces ge-0/0/0 extensive | match "Laser|Rx power|Tx power|Temperature"
show chassis pic fpc 0 pic 0                     # optic detail for a PIC slot
```

### ACX Interface Naming

ACX interface naming follows the standard JunOS FPC/PIC/PORT schema, but fixed-port platforms always use FPC 0:

```
ge-0/0/0     # GigE, FPC 0, PIC 0, port 0
xe-0/0/0     # 10GE SFP+
et-0/0/0     # 100GE / 400GE (ACX6360, ACX7000)
```

On the ACX7509 (modular chassis), FPC slots are numbered by physical slot:
```
et-2/0/0     # 400GE on FPC in slot 2
```

---

### ACX Class of Service (CoS)

CoS on ACX is essential for meeting MEF SLA guarantees (CIR/EIR, frame delay, frame loss).

```
show class-of-service interface ge-0/0/0         # CoS applied to interface
show class-of-service interface ge-0/0/0 comprehensive  # classifiers, schedulers, rewrite
show interfaces queue ge-0/0/0                   # queue depth, drops, transmit rates
show interfaces queue ge-0/0/0 detail
show class-of-service forwarding-class           # defined forwarding classes
show class-of-service scheduler-map              # scheduler maps
show class-of-service code-point-aliases dscp   # DSCP alias definitions
show class-of-service code-point-aliases ieee-802.1 # 802.1p alias definitions
```

**Basic CoS Configuration Pattern:**

```
# Define forwarding classes
set class-of-service forwarding-classes class VOICE queue-num 0
set class-of-service forwarding-classes class VIDEO queue-num 1
set class-of-service forwarding-classes class DATA  queue-num 2
set class-of-service forwarding-classes class BEST-EFFORT queue-num 3

# Classifier — map DSCP to forwarding class
set class-of-service classifiers dscp DSCP-CLASSIFY forwarding-class VOICE loss-priority low code-points ef
set class-of-service classifiers dscp DSCP-CLASSIFY forwarding-class VIDEO loss-priority low code-points af41
set class-of-service classifiers dscp DSCP-CLASSIFY forwarding-class BEST-EFFORT loss-priority high code-points be

# Scheduler — CIR/PIR per queue
set class-of-service schedulers VOICE-SCHED transmit-rate percent 30
set class-of-service schedulers VOICE-SCHED priority strict-high
set class-of-service schedulers BE-SCHED transmit-rate remainder

# Scheduler map
set class-of-service scheduler-maps SCHED-MAP forwarding-class VOICE scheduler VOICE-SCHED
set class-of-service scheduler-maps SCHED-MAP forwarding-class BEST-EFFORT scheduler BE-SCHED

# Apply to interface
set class-of-service interfaces ge-0/0/0 unit 0 classifiers dscp DSCP-CLASSIFY
set class-of-service interfaces ge-0/0/0 scheduler-map SCHED-MAP
```

---

### ACX-Specific Operational Tips

```
# Verify timing lock before turning up a service
show ptp lock-status
show ptp master-slave-table detail | match "Offset\|Delay\|State"

# Check all alarms before maintenance
show chassis alarms
show system alarms

# Verify pseudowire status across all neighbors
show l2circuit connections | match "ge-|xe-|et-|Dn\|Up"

# Check OAM CCM state for all MEPs
show oam ethernet connectivity-fault-management continuity-check | match "Remote\|Local"

# Confirm SyncE SSM quality on uplinks
show synchronization | match "QL\|Source\|Interface"

# Monitor queue drops in real time
monitor interface ge-0/0/0

# ACX7000: verify SR-MPLS label forwarding
show route table mpls.0 detail | match "16[0-9]{3}"   # SRGB range
show spring-traffic-engineering lsp detail

# Confirm EVPN MAC learning (ACX7000)
show evpn database | match "MAC\|aa:bb"
```

### ACX Licensing

```
show system license                              # all installed license keys and features
show system license usage                        # which features are in use vs licensed
```

Key ACX licensed features (varies by platform):
- L3 routing (sometimes base or enhanced scale)
- MPLS (may require add-on)
- Timing/PTP (may require add-on on some platforms)
- EVPN (ACX7000)
- Subscriber management

---

## 13. Cross-Platform Command Reference

### General & Interface Commands

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| Show interfaces brief | `show interfaces terse` | `show ip interface brief` | `show ipv4 interface brief` |
| Show interface detail | `show interfaces ge-0/0/0` | `show interface GigE0/0/0` | `show interface GigE0/0/0/0` |
| Show interface counters | `show interfaces statistics` | `show interface GigE0/0/0` | `show interface GigE0/0/0/0` |
| Show all MAC addresses | `show ethernet-switching table` | `show mac address-table` | `show l2vpn forwarding bd-mac-address` |
| Disable interface | `set interfaces ge-0/0/0 disable` | `shutdown` (interface mode) | `shutdown` (interface mode) |
| Show running config | `show configuration` | `show running-config` | `show running-config` |
| Show config as flat cmds | `show config \| display set` | `show running-config` (already flat) | `show running-config` (already flat) |
| Enter config mode | `configure` | `configure terminal` | `configure terminal` |
| Save config | `commit` | `write memory` / `copy run start` | `commit` |
| Rollback config | `rollback 1` + `commit` | `copy startup running` (limited) | `rollback 1` |
| Config diff | `show config \| compare` | *(no native equivalent)* | `show commit changes diff` |
| Validate config | `commit check` | *(limited)* | `commit` (always validates) |

### Routing Protocol — OSPF

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| OSPF neighbors | `show ospf neighbor` | `show ip ospf neighbor` | `show ospf neighbor` |
| OSPF neighbor detail | `show ospf neighbor detail` | `show ip ospf neighbor detail` | `show ospf neighbor detail` |
| OSPF interfaces | `show ospf interface` | `show ip ospf interface` | `show ospf interface` |
| OSPF LSDB | `show ospf database` | `show ip ospf database` | `show ospf database` |
| OSPF routes | `show route protocol ospf` | `show ip route ospf` | `show route ospf` |
| OSPF summary | `show ospf overview` | `show ip ospf` | `show ospf` |
| OSPFv3 neighbors | `show ospf3 neighbor` | `show ipv6 ospf neighbor` | `show ospfv3 neighbor` |

### Routing Protocol — IS-IS

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| IS-IS adjacencies | `show isis adjacency` | `show isis neighbors` | `show isis adjacency` |
| IS-IS adjacency detail | `show isis adjacency detail` | `show isis neighbors detail` | `show isis adjacency detail` |
| IS-IS interfaces | `show isis interface` | `show isis interface` | `show isis interface` |
| IS-IS LSDB | `show isis database` | `show isis database` | `show isis database` |
| IS-IS LSDB detail | `show isis database detail` | `show isis database verbose` | `show isis database detail` |
| IS-IS routes | `show route protocol isis` | `show ip route isis` | `show route isis` |
| IS-IS overview | `show isis overview` | `show isis` | `show isis` |

### Routing Protocol — BGP

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| BGP summary | `show bgp summary` | `show ip bgp summary` | `show bgp summary` |
| BGP neighbors | `show bgp neighbor` | `show ip bgp neighbors` | `show bgp neighbors` |
| BGP neighbor detail | `show bgp neighbor 10.0.0.2` | `show ip bgp neighbors 10.0.0.2` | `show bgp neighbors 10.0.0.2` |
| BGP routes | `show route protocol bgp` | `show ip bgp` | `show bgp` |
| BGP route detail | `show route 10/8 detail` | `show ip bgp 10.0.0.0/8` | `show bgp 10.0.0.0/8` |
| Routes received | `show bgp neighbor X received-routes` | `show ip bgp neighbors X received-routes` | `show bgp neighbors X received` |
| Routes advertised | `show bgp neighbor X advertised-routes` | `show ip bgp neighbors X advertised-routes` | `show bgp neighbors X advertised` |
| BGP groups | `show bgp group` | *(peer-groups in config only)* | *(peer-groups in config only)* |
| VPN routes | `show route table CUST-A.inet.0` | `show ip bgp vpnv4 vrf CUST-A` | `show bgp vrf CUST-A` |

### MPLS

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| LDP neighbors | `show ldp neighbor` | `show mpls ldp neighbor` | `show mpls ldp neighbor` |
| LDP sessions | `show ldp session` | `show mpls ldp neighbor` | `show mpls ldp neighbor` |
| LDP label bindings | `show ldp database` | `show mpls ldp bindings` | `show mpls ldp bindings` |
| MPLS label table | `show route table mpls.0` | `show mpls forwarding-table` | `show mpls forwarding` |
| RSVP sessions | `show rsvp session` | `show ip rsvp session` | `show rsvp session` |
| TE LSPs | `show mpls lsp` | `show mpls traffic-eng tunnels` | `show mpls traffic-eng tunnels` |
| TE LSP detail | `show mpls lsp detail` | `show mpls traffic-eng tunnels detail` | `show mpls traffic-eng tunnels detail` |
| TE database | `show ted database` | `show mpls traffic-eng topology` | `show mpls traffic-eng topology` |
| SR-MPLS labels | `show route table mpls.0` | `show mpls forwarding-table` | `show mpls forwarding` |

### VLANs / L2

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| Show VLANs | `show vlans` | `show vlan brief` | `show l2vpn bridge-domain brief` |
| VLAN detail | `show vlans VLAN100` | `show vlan id 100` | `show l2vpn bridge-domain name BD100 detail` |
| Spanning tree | `show spanning-tree bridge` | `show spanning-tree` | `show spanning-tree` |
| STP interface | `show spanning-tree interface` | `show spanning-tree interface Gi0/0` | `show spanning-tree interface Gi0/0` |
| MAC table | `show ethernet-switching table` | `show mac address-table` | `show l2vpn forwarding bd-mac-address` |
| LACP status | `show lacp interfaces ae0` | `show lacp interface Po1` | `show lacp interface Bundle-Ether1` |

### System & Diagnostics

| Function | JunOS | IOS-XE | IOS-XR |
|---|---|---|---|
| Ping | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 repeat 5` | `ping 8.8.8.8 count 5` |
| Traceroute | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` |
| Show ARP | `show arp` | `show ip arp` | `show arp` |
| Show routes | `show route` | `show ip route` | `show route` |
| Show route detail | `show route 10/8 detail` | `show ip route 10.0.0.0` | `show route 10.0.0.0/8 detail` |
| Disable paging | `set cli screen-length 0` | `terminal length 0` | `terminal length 0` |
| Show version | `show version` | `show version` | `show version` |
| Show chassis | `show chassis hardware` | `show inventory` | `show inventory` |
| Logs | `show log messages` | `show logging` | `show logging` |
| Follow logs live | `monitor start messages` | `terminal monitor` | `terminal monitor` |
| CPU/memory | `show chassis routing-engine` | `show processes cpu` | `show processes cpu` |
| Reboot | `request system reboot` | `reload` | `reload` |
| Save config | `commit` | `write memory` | `commit` |
| Grep equivalent | `show ... \| match <regex>` | `show ... \| include <regex>` | `show ... \| include <regex>` |
| Exclude equivalent | `show ... \| except <regex>` | `show ... \| exclude <regex>` | `show ... \| exclude <regex>` |
| Count lines | `show ... \| count` | `show ... \| count` | `show ... \| utility wc` |

---

## 14. Quick Reference Card

### Top 20 Daily-Driver Commands

```bash
# System health
show chassis routing-engine               # CPU, memory, uptime
show version                              # software version, model
show log messages | last 100             # recent syslog

# Interfaces
show interfaces terse                     # all interfaces, one line each
show interfaces ge-0/0/0 detail           # full interface detail

# Routing
show route                                # full routing table
show route summary                        # route count by protocol
show route protocol bgp | no-more        # all BGP routes
show route 0.0.0.0/0 exact               # default route
show arp                                  # ARP table

# BGP / OSPF / IS-IS
show bgp summary                          # BGP peer state at a glance
show ospf neighbor                        # OSPF adjacencies
show isis adjacency                       # IS-IS adjacencies

# MPLS
show mpls lsp                             # all RSVP LSPs
show ldp session                          # LDP sessions
show route table mpls.0 | head 30        # top of MPLS FIB

# Config workflow
show configuration | display set | no-more   # running config as set cmds
show configuration | compare                  # staged vs active diff
commit check                                  # validate before committing
```

### Useful One-Liners

```bash
# Count BGP prefixes per peer
show bgp summary | match "^\d{1,3}\."

# Show only established BGP sessions
show bgp summary | except "Idle|Active|Connect"

# Find interfaces that are down
show interfaces terse | match "down"

# Show OSPF neighbors that are not Full
show ospf neighbor | except "Full"

# Show all IS-IS L2 adjacencies only
show isis adjacency | match "L2\|Up"

# Find which LSP carries traffic to a destination
show route 10.0.0.5/32 detail | match "label|via"

# Get config for a specific IP anywhere in the config
show configuration | display set | match "192.0.2.1"

# Tail syslog live
show log messages | match BGP | last 20
monitor start messages                    # live tail (Ctrl+C to stop)

# Show commit log
show system commit

# Diff last two commits
show configuration | compare rollback 1
```

### JunOS-Specific Mental Models

| Concept | JunOS Way | Notes |
|---|---|---|
| Config is always candidate | Edit → commit to apply | Nothing takes effect until `commit` |
| Routing instances | `set routing-instances <NAME>` | VRFs, L2 circuits, VPLS all use this |
| Policy framework | `policy-options policy-statement` | Import/export applied per-protocol |
| Communities | Defined globally under `policy-options community` | Referenced in policy terms |
| Firewall filters | `firewall family inet filter` | Applied to interface units as input/output |
| CoS | `class-of-service` hierarchy | Classifiers, schedulers, rewrite rules |
| `family inet` vs `family inet6` | Separate address families per logical unit | Both can be on the same unit |
| `unit 0` | Default logical interface number | Like a subinterface; required even for physical |
| `lo0.0` | Loopback always on unit 0 | Multiple addresses supported |
| PFE vs RE | `show pfe ...` for hardware FIB | RE runs routing protocols; PFE forwards |

---

*Curriculum version: 1.2 | Target: Juniper JunOS — MX/EX/QFX/PTX/ACX platforms*
*Reference platforms for comparison: Cisco IOS-XE 17.x, Cisco IOS-XR 7.x*

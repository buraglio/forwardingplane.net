---
title: Nokia SR OS MD-CLI Basics
date: 2026-05-06
author: Nick Buraglio
layout: page
---

# Nokia SR OS MD-CLI Basics

A practical curriculum for network engineers learning Nokia SR OS with the Model-Driven CLI (MD-CLI), with emphasis on operational commands, usability features, and cross-platform translation from JunOS, Arista EOS, and IOS-XE/XR. Covers Nokia's proprietary FP silicon and the merchant-silicon IXR variant platforms.

---

## Table of Contents

1. [SR OS / MD-CLI Fundamentals](#1-sr-os--md-cli-fundamentals)
2. [CLI Navigation & Usability](#2-cli-navigation--usability)
3. [Pipe Commands & Output Filtering](#3-pipe-commands--output-filtering)
4. [Port and Interface Commands](#4-port-and-interface-commands)
5. [L2 Services — VPLS, EPIPE, and VLANs](#5-l2-services--vpls-epipe-and-vlans)
6. [OSPF Commands](#6-ospf-commands)
7. [ISIS Commands](#7-isis-commands)
8. [BGP Commands](#8-bgp-commands)
9. [MPLS Commands](#9-mpls-commands)
10. [IPv6 Commands](#10-ipv6-commands)
11. [Configuration Management](#11-configuration-management)
12. [Platform & Silicon Details](#12-platform--silicon-details)
13. [Cross-Platform Command Reference](#13-cross-platform-command-reference)
14. [Quick Reference Card](#14-quick-reference-card)

---

## 1. SR OS / MD-CLI Fundamentals

### Architecture Overview

Nokia SR OS (Service Router Operating System) runs on a Linux-based kernel with a fully custom, vertically integrated forwarding plane. The control plane runs on the **CPM** (Control Processor Module), which hosts routing daemons, the management plane, and the CLI. The forwarding plane runs on one or more **FP** (Forwarding Processor) ASICs — Nokia's proprietary silicon — on separate line cards or IMMs (Integrated Module Modules).

```
┌────────────────────────────────────────────────────────────┐
│                      CPM (Control Processor Module)        │
│   Management/CLI ─── Routing daemons ─── Policy engine    │
└─────────────────────────────┬──────────────────────────────┘
                              │  IPC / distributed state
┌─────────────────────────────▼──────────────────────────────┐
│               FP ASIC (Forwarding Processor)               │
│   Nokia FP4/FP5 — proprietary VOQ architecture             │
│   7250 IXR exception: Broadcom Jericho2 (merchant silicon) │
└────────────────────────────────────────────────────────────┘
```

This CPM/FP separation is analogous to JunOS's RE/PFE model and provides the same fundamental guarantee: control-plane events (routing reconvergence, management traffic) cannot starve the forwarding plane. Nokia's FP ASICs implement **VOQ (Virtual Output Queuing)** — every ingress port maintains separate queues per egress port, eliminating head-of-line blocking. This architecture is distinct from merchant silicon platforms (Broadcom Trident/Tomahawk) and is one of Nokia's core differentiation points.

SR OS runs a similar "hypervisor + guest OS" model to JunOS and Arista EOS, where routing software runs as a process set on top of the Linux kernel, and hardware access is mediated through drivers. Nokia's vSIM (virtual SR OS simulator) and containerized variants follow this same model. The forwarding plane software (datapath) runs as a separate protected domain.

### MD-CLI vs. Classic CLI

SR OS has two distinct CLI modes:

- **Classic CLI** — The original IOS-inspired CLI. Uses `no` prefix to negate, `configure` for config mode, `exit all` to return to root. Still supported but not receiving new feature coverage.
- **MD-CLI** — Model-Driven CLI, introduced in SR OS 16.0. Built directly on YANG data models (Nokia-native and OpenConfig). All configuration is expressed as a candidate config committed atomically. Preferred for new deployments and automation.

This guide covers **MD-CLI exclusively**. If you are on Classic CLI, the configuration syntax is substantially different even though most operational (`show`) commands are shared.

### Service Model

Nokia SR OS uses a strict **service model** that is fundamentally different from JunOS routing-instances and Arista EOS VRFs. Understanding it is prerequisite to understanding everything else.

| Layer | Nokia Concept | Analogous JunOS | Analogous EOS |
|---|---|---|---|
| L3 default routing | Base router (`router "Base"`) | `inet.0` / default VRF | default VRF |
| L3 VPN | VPRN (service type, numbered) | routing-instance type vrf | vrf instance |
| L2 point-to-point | EPIPE (Ethernet pseudowire) | l2circuit | — |
| L2 multipoint | VPLS (Virtual Private LAN Service) | routing-instance type vpls | — |
| EVPN control plane | Works with VPLS or VXLAN | routing-instance type evpn | EVPN-VXLAN |
| Service attachment | SAP (Service Access Point): `port:vlan` | interface unit with family ccc | N/A |

Services are referenced by integer IDs (`service id 100`) and optionally named (`service name "CUST-A"`). All services live under `/configure service`.

### Operational vs. Configuration Mode

```
A:router>           # operational (show) mode
[ex:/configure]
A:router#           # MD-CLI configuration mode (exclusive shown)
```

| Action | Command |
|--------|---------|
| Enter config mode (exclusive) | `edit-config exclusive` |
| Enter config mode (global, shared) | `edit-config global` |
| Enter config mode (private candidate) | `edit-config private` |
| Return to operational mode | `exit` |
| Run operational command from config mode | type `show ...` directly |
| Apply candidate configuration | `commit` |
| Validate without committing | `validate` |
| Show pending diff | `compare` |
| Discard all pending changes | `discard` |

The bracket at the MD-CLI prompt shows mode and current path:
```
[ex:/configure router "Base"]
A:router#
```
`ex` = exclusive, `pr` = private, `gl` = global.

---

## 2. CLI Navigation & Usability

### Tab Completion & Help

```
show router ?                    # list all sub-commands at this level
show router bgp <Tab>            # complete or list options
show router b<Tab>               # completes to 'bgp' if unambiguous
/configure router "Base" o<Tab>  # completes to 'ospf'
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Complete command or show options |
| `?` | Context-sensitive help |
| `Ctrl+A` | Move cursor to beginning of line |
| `Ctrl+E` | Move cursor to end of line |
| `Ctrl+U` | Delete from cursor to beginning of line |
| `Ctrl+K` | Delete from cursor to end of line |
| `Ctrl+W` | Delete previous word |
| `Ctrl+R` | Reverse search command history |
| `Ctrl+C` | Abort current command |
| `Ctrl+D` | Exit CLI (if line is empty) |
| `Ctrl+Z` | Return to top of configuration hierarchy |
| `Ctrl+L` | Redraw screen |
| Up/Down arrows | Navigate command history |

### Configuration Mode Navigation

```
/configure                              # jump to config root
/configure router "Base"               # jump to base router config
/configure router "Base" ospf 0        # jump directly to OSPF context
back                                    # go up one level in the hierarchy
exit                                    # exit configuration mode entirely
top                                     # go to top of config hierarchy (/configure)
pwd                                     # show current path
info                                    # show config at current hierarchy level
info detail                             # show all attributes including defaults
info flat                               # show as flat absolute-path commands
```

### Abbreviations

MD-CLI supports unambiguous abbreviations:

```
sh ro int                       # show router interface
sh ro bgp sum                   # show router bgp summary
sh ro ro-t                      # show router route-table
sh ser id 100 b                 # show service id 100 base
```

### Terminal & Display Settings

```
environment more false          # disable pagination (like 'terminal length 0')
environment more true           # re-enable pagination
environment screen-length 50    # set page length
environment screen-width 250    # wider output
```

---

## 3. Pipe Commands & Output Filtering

SR OS MD-CLI supports Unix-style pipe filtering on both operational and `info` output.

### Core Pipe Commands

| Pipe Command | Description | Example |
|---|---|---|
| `\| match <regex>` | Show lines matching pattern (grep) | `show router interface \| match 10.0` |
| `\| match <regex> invert-match` | Exclude matching lines | `show router bgp summary \| match "Establ" invert-match` |
| `\| count` | Count lines | `show router route-table \| count` |
| `\| head <n>` | Show first N lines | `show router route-table \| head 20` |
| `\| tail <n>` | Show last N lines | `show log 99 \| tail 50` |
| `\| more` | Enable pagination for this command | `show router route-table \| more` |
| `\| no-more` | Disable pagination for this command | `show router route-table \| no-more` |
| `\| as-json` | Output as JSON | `show router interface \| as-json` |
| `\| as-xml` | Output as XML | `show router interface \| as-xml` |
| `\| detail` | More verbose output (context-dependent) | `show router ospf neighbor \| detail` |

### Chaining Pipes

```
show router route-table | match 192.168 | count
show router bgp summary | match "Establ|Up"
show router ldp session | match "Establ" invert-match
show router interface | match "10\.|192\."
```

### `info flat` — The Most Useful Config Display

`info flat` displays the current configuration hierarchy as absolute-path one-liners, analogous to JunOS `display set` and useful for the same purposes: diffing, documentation, and copy-paste operations.

```
[ex:/configure router "Base"]
A:router# info flat
    /configure router "Base" interface "system" ipv4 primary address 10.0.0.1
    /configure router "Base" interface "system" ipv4 primary prefix-length 32
    /configure router "Base" interface "to-peer" port 1/1/1:0
    /configure router "Base" interface "to-peer" ipv4 primary address 192.0.2.1
    /configure router "Base" interface "to-peer" ipv4 primary prefix-length 30
    /configure router "Base" ospf 0 area 0.0.0.0 interface "system" passive true
    /configure router "Base" ospf 0 area 0.0.0.0 interface "to-peer" interface-type point-to-point
```

### JSON / XML Output

```
show router interface | as-json
show router bgp summary | as-json
show router route-table | as-json
info | as-json                   # current config context as JSON
```

SR OS also supports NETCONF and gNMI for programmatic access — the same YANG models underlie the MD-CLI, NETCONF, and gRPC telemetry interfaces.

### Watching Output Repeatedly

```
# No native 'watch' command — use the 'repeat' utility
tools perform router "Base" repeat-command "show router bgp summary" interval 5
# Or use external polling via NETCONF/gNMI
```

---

## 4. Port and Interface Commands

Nokia SR OS makes a critical distinction between **ports** and **interfaces** that does not exist in JunOS, EOS, or IOS:

- **Port** — the physical layer object (`port 1/1/1`). Configured under `/configure port`.
- **Router Interface** — a named logical L3 object under `/configure router "Base" interface "name"`. Bound to a port via a port-unit reference (`port 1/1/1:0`).
- **SAP** (Service Access Point) — `port:vlan-tag` notation used to attach L2 services to ports. Not a router interface.

### Port Show Commands

```
show port                               # all ports, operational state
show port 1/1/1                         # detail for specific port
show port 1/1/1 detail                  # extended detail
show port 1/1/1 optical                 # DOM: Rx/Tx power, temperature
show port 1/1/1 statistics              # packet/byte/error counters
show port 1/1/1 statistics detail
show port 1/1/c1/1                      # breakout port (CFP-based)
show lag 1                              # LAG detail
show lag 1 detail                       # member link status, LACP state
show lacp port 1 statistics             # LACP PDU counters per member
```

### Router Interface Show Commands

```
show router interface                   # all interfaces in Base router
show router interface "to-peer"         # specific named interface
show router interface "system"          # loopback (always named "system")
show router interface detail            # full detail including statistics
show router arp                         # ARP table for Base router
show router arp interface "to-peer"     # ARP entries for specific interface
show router neighbor                    # IPv6 NDP neighbor cache (Base router)
```

### Port Naming Conventions

```
1/1/1          # slot 1, MDA 1, port 1   (standard card)
1/1/c1/1       # slot 1, MDA 1, connector 1, breakout lane 1  (CFP/QSFP breakout)
A/1            # CPM port (management on some platforms)
```

Port types by hardware:
```
# Fixed (7250 IXR, 7220 IXR)
1/1/1          # port 1 on the fixed system

# Modular (7750 SR, 7950 XRS)
1/1/1          # slot 1, MDA 1, port 1
2/3/5          # slot 2, MDA 3, port 5
```

### Port Configuration Examples

```
# Enable physical port and set description
/configure port 1/1/1 {
    admin-state enable
    description "To-Peer-Router"
    ethernet {
        mode hybrid         # hybrid: can carry both routed and service traffic
        encap-type dot1q    # 802.1q encapsulation on this port
    }
}

# 100G port with autoneg off
/configure port 1/1/1 {
    admin-state enable
    ethernet {
        mode network        # purely routed (no SAPs, no dot1q)
        autonegotiate false
        speed 100000        # 100G in Mbps
    }
}

# LAG configuration
/configure lag 1 {
    admin-state enable
    mode active-active
    lacp {
        mode active
        administrative-key 1
    }
    port 1/1/1 { }
    port 1/1/2 { }
}
```

### Router Interface Configuration Examples

```
# Basic L3 interface on a routed port
/configure port 1/1/1 {
    admin-state enable
    ethernet { mode network }
}
/configure router "Base" {
    interface "to-peer" {
        port 1/1/1
        ipv4 {
            primary {
                address 192.0.2.1
                prefix-length 30
            }
        }
    }
}

# L3 interface on a dot1q unit (hybrid port)
/configure router "Base" {
    interface "to-peer-tagged" {
        port 1/1/2:100       # port 1/1/2, dot1q tag 100
        ipv4 {
            primary {
                address 192.0.2.1
                prefix-length 30
            }
        }
    }
}

# Loopback (always use "system" interface for router-id/loopback)
/configure router "Base" {
    interface "system" {
        ipv4 {
            primary {
                address 10.0.0.1
                prefix-length 32
            }
        }
    }
}

# Disable interface
/configure router "Base" interface "to-peer" admin-state disable
```

---

## 5. L2 Services — VPLS, EPIPE, and VLANs

Nokia SR OS does not have traditional VLAN-based switching in the main router context. Layer 2 services are defined as **numbered service instances** under `/configure service`. Each service is an isolated L2 domain with its own MAC table, flooding behavior, and control plane.

### Key L2 Service Types

| Type | Purpose | Topology | Analogous JunOS |
|---|---|---|---|
| EPIPE | Point-to-point Ethernet pseudowire | 2 endpoints | `l2circuit` |
| VPLS | Multipoint L2 service (L2VPN) | Hub-and-spoke or full mesh | `routing-instance type vpls` |
| EVPN (with VPLS) | BGP EVPN control for VPLS | BGP-based | `routing-instance type evpn` |
| VXLAN (with EVPN) | EVPN with VXLAN data plane | BGP-based | — |
| IES | L3 service with SAP-based interfaces | L3 gateway | IRB interface |

### SAP Notation

A **SAP** (Service Access Point) binds a service to a physical port:

```
sap 1/1/1:0       # port 1/1/1, inner tag 0 (untagged or null-tagged)
sap 1/1/1:100     # port 1/1/1, dot1q tag 100
sap 1/1/1:100.200 # port 1/1/1, outer tag 100, inner tag 200 (QinQ)
sap lag-1:100     # LAG 1, dot1q tag 100
```

### L2 Service Show Commands

```
# EPIPE
show service id 100 base                # EPIPE or VPLS service summary
show service id 100 all                 # full service detail
show service id 100 endpoint            # endpoint and SAP status
show service epipe                      # all EPIPE services

# VPLS
show service id 200 base
show service id 200 all
show service id 200 fdb                 # MAC forwarding database (like show mac address-table)
show service id 200 fdb detail
show service id 200 sap                 # SAP detail within service
show service vpls                       # all VPLS services

# EVPN
show service id 300 evpn                # EVPN state for a service
show service id 300 evpn routes         # EVPN BGP routes for service
show service id 300 evpn mac            # EVPN learned MAC/IP entries
show evpn                               # global EVPN state

# Spanning Tree (within VPLS)
show service id 200 stp                 # STP state for VPLS

# VXLAN
show service id 300 vxlan               # VXLAN VTEPs and state
```

### EPIPE (Pseudowire / E-Line) Configuration

```
/configure service {
    epipe 100 {
        admin-state enable
        customer "default"
        service-mtu 1514
        sap 1/1/1:100 {
            admin-state enable
        }
        spoke-sdp 200:100 {             # SDP = Service Distribution Point (MPLS tunnel)
            admin-state enable
        }
    }
}

# SDP (MPLS tunnel toward remote PE)
/configure service {
    sdp 200 {
        admin-state enable
        description "To-PE2"
        far-end {
            ip-address 10.0.0.2
        }
        ldp true                        # use LDP-signaled LSP
        signaling tldp                  # or: bgp, none
    }
}
```

### VPLS (E-LAN) Configuration

```
/configure service {
    vpls 200 {
        admin-state enable
        customer "default"
        service-mtu 1514
        sap 1/1/1:200 {
            admin-state enable
        }
        sap 1/1/2:200 {
            admin-state enable
        }
        spoke-sdp 201:200 {             # mesh-SDP or spoke-SDP to remote PE
            admin-state enable
        }
    }
}
```

### EVPN-VXLAN Configuration

```
/configure service {
    vpls 300 {
        admin-state enable
        customer "default"
        vxlan {
            instance 1 {
                vni 10300
            }
        }
        routed-vpls {
            vprn 1000                   # attach to VPRN for IRB (L3 gateway)
            vprn-interface "irb-vlan300"
        }
        bgp 1 {
            route-distinguisher 65000:300
            route-target {
                export "target:65000:300"
                import "target:65000:300"
            }
        }
        bgp-evpn {
            evi 300
            vxlan 1 {
                admin-state enable
            }
        }
        sap 1/1/3:300 {
            admin-state enable
        }
    }
}

# VTEP source interface
/configure router "Base" {
    interface "system" {
        ipv4 {
            primary {
                address 10.0.0.1
                prefix-length 32
            }
        }
    }
}
```

---

## 6. OSPF Commands

### Show Commands

```
show router ospf overview                # OSPF process summary, router-id, areas
show router ospf neighbor                # neighbor adjacencies
show router ospf neighbor detail         # detailed neighbor state
show router ospf neighbor "to-peer"      # specific neighbor by interface name
show router ospf interface               # per-interface OSPF state
show router ospf interface detail        # DR/BDR, hello/dead timers, metrics
show router ospf database                # LSDB summary
show router ospf database detail         # full LSDB
show router ospf database type router    # Router LSAs only
show router ospf database type network   # Network LSAs only
show router ospf database type summary   # Summary (Type-3) LSAs
show router ospf database type external  # External (Type-5) LSAs
show router ospf statistics              # SPF runs, PDU counters
show router ospf spf-log                 # SPF computation log
```

### Route Table Integration

```
show router route-table protocol ospf           # OSPF routes in RIB
show router route-table 10.0.0.0/8 longer       # OSPF learned routes under prefix
show router route-table 10.0.0.0/8 detail       # route detail
```

### OSPFv3 (IPv6)

```
show router ospf3 overview
show router ospf3 neighbor
show router ospf3 interface
show router ospf3 database
show router ospf3 route
```

### Configuration Examples

```
/configure router "Base" {
    ospf 0 {
        admin-state enable
        router-id 10.0.0.1
        reference-bandwidth 100000000   # 100G in kbps for cost calculation

        area 0.0.0.0 {
            interface "system" {
                passive true
            }
            interface "to-peer" {
                interface-type point-to-point
                metric 10
                hello-interval 10
                dead-interval 40
                authentication {
                    key-chain "OSPF-KEY"
                }
            }
        }

        area 0.0.0.1 {
            stub true
            default-metric 10
        }
    }
}

# Authentication key chain
/configure router "Base" {
    key-chain "OSPF-KEY" {
        direction bidirectional
        key 1 {
            key-value "secretkey"
            algorithm hmac-sha-256
        }
    }
}

# Redistribute connected into OSPF
/configure router "Base" {
    ospf 0 {
        export-policy ["CONNECTED-TO-OSPF"]
    }
}

/configure policy-options {
    policy-statement "CONNECTED-TO-OSPF" {
        entry 10 {
            from {
                protocol {
                    name [direct]
                }
            }
            action {
                action-type accept
            }
        }
    }
}
```

---

## 7. ISIS Commands

### Show Commands

```
show router isis overview                # IS-IS process, NET, levels
show router isis adjacency               # IS-IS neighbor adjacencies
show router isis adjacency detail        # state, hold time, circuit type
show router isis interface               # per-interface IS-IS state
show router isis interface detail        # metrics, timers, circuit type
show router isis database                # LSDB summary
show router isis database detail         # full TLV details
show router isis database level 2        # Level-2 only
show router isis database <system-id>    # specific LSP
show router isis routes                  # IS-IS computed routes
show router isis routes ipv4-unicast     # IPv4 routes
show router isis routes ipv6-unicast     # IPv6 routes
show router isis statistics              # PDU counters, SPF runs
show router isis hostname                # dynamic hostname mappings
show router isis spf-log                 # SPF computation history
show router isis lfa-coverage            # LFA/TI-LFA backup coverage
show router isis segment-routing prefix-sids  # SR prefix SIDs
```

### Route Table Integration

```
show router route-table protocol isis
show router route-table ipv6 protocol isis
show router route-table 10.0.0.0/8 detail
```

### Configuration Examples

```
/configure router "Base" {
    isis 0 {
        admin-state enable
        level-capability level-2          # L2-only router
        area-address [49.0001]

        traffic-engineering true          # enable TE extensions
        wide-metrics-only true

        interface "system" {
            passive true
            ipv4-node-sid {
                index 1                   # SR node SID
            }
        }

        interface "to-peer" {
            circuit-type point-to-point
            level 2 {
                metric 10
                hello-authentication-key "secretkey"
                hello-authentication-type message-digest
            }
        }

        level 2 {
            wide-metrics-only true
        }

        segment-routing {
            admin-state enable
            prefix-sid-range {
                global-block {
                    start-label 16000
                    max-index 8000
                }
            }
        }

        export-policy ["CONNECTED-TO-ISIS"]
    }
}
```

---

## 8. BGP Commands

### Show Commands

```
show router bgp summary                          # all peers, state, prefix counts
show router bgp neighbor                         # all neighbor details
show router bgp neighbor 192.0.2.2              # specific neighbor
show router bgp neighbor 192.0.2.2 detail       # full neighbor detail + timers
show router bgp group "IBGP"                    # peer group details
show router bgp group "IBGP" detail

# Route views
show router bgp routes                           # BGP routes (inet.0 equivalent)
show router bgp routes ipv4                      # IPv4 unicast routes
show router bgp routes ipv6                      # IPv6 unicast routes
show router bgp routes vpn-ipv4                  # VPNv4 routes
show router bgp routes evpn                      # EVPN NLRI
show router bgp routes 10.0.0.0/8 detail        # specific prefix with attributes
show router bgp routes community 65000:100 detail

# Per-neighbor route views
show router bgp neighbor 192.0.2.2 received-routes ipv4   # routes received
show router bgp neighbor 192.0.2.2 advertised-routes ipv4 # routes advertised

# VPN-specific
show router 100 bgp summary                      # BGP summary within VPRN 100
show router 100 route-table                      # VPRN 100 routing table
```

### Debugging BGP

```
show router bgp neighbor 192.0.2.2 | match "State|Hold|Prefix"
show log 99 | match BGP
show log 99 | tail 100                           # recent log entries

# Detailed tracing (use with care)
debug router bgp neighbor 192.0.2.2 update
debug router bgp neighbor 192.0.2.2 open
debug router bgp neighbor 192.0.2.2 keepalive
no debug router bgp                              # disable all BGP debug
```

### Configuration Examples

```
/configure router "Base" {
    autonomous-system 65000
    router-id 10.0.0.1

    bgp {
        admin-state enable
        rapid-withdrawal true
        rapid-update evpn true

        group "IBGP" {
            type internal
            local-address 10.0.0.1
            family {
                ipv4 true
                vpn-ipv4 true
                evpn true
            }
            send-communities large true
            next-hop-self true
            cluster 10.0.0.1              # route reflector
            neighbor 10.0.0.2 { }
            neighbor 10.0.0.3 { }
        }

        group "EBGP" {
            type external
            family {
                ipv4 true
            }
            neighbor 192.0.2.2 {
                peer-as 65001
                local-address 192.0.2.1
                import-policy ["IMPORT-POLICY"]
                export-policy ["EXPORT-POLICY"]
                authentication-key "secret"
                bfd-liveness-detection {
                    admin-state enable
                    min-interval 300
                    multiplier 3
                }
            }
        }
    }
}

# Add-path / multipath
/configure router "Base" bgp {
    multipath {
        max-paths-level-1 8
        max-paths-level-2 8
    }
    group "IBGP" {
        add-paths {
            ipv4 {
                send 6
                receive true
            }
        }
    }
}
```

### Policy and Communities

```
/configure policy-options {
    community "MY-COMM" {
        member "65000:100" { }
    }

    policy-statement "IMPORT" {
        entry 10 {
            from {
                community {
                    name "MY-COMM"
                }
            }
            action {
                action-type accept
                local-preference 200
            }
        }
    }

    policy-statement "EXPORT" {
        entry 10 {
            action {
                action-type accept
                as-path-prepend {
                    as-path "65000 65000"
                }
            }
        }
    }

    prefix-list "MY-PREFIXES" {
        prefix 10.0.0.0/8 type longer { }
    }
}
```

---

## 9. MPLS Commands

Nokia SR OS is distinguished by its complete, deeply integrated MPLS stack — LDP, RSVP-TE, SR-MPLS, and SRv6 are all first-class features on FP-based platforms. The FP ASIC was designed from the ground up to support large-scale MPLS forwarding with deep buffers and VOQ. This contrasts with merchant silicon platforms where MPLS support depends on chipset capability.

### Show Commands

```
# LDP
show router ldp session                          # LDP session state
show router ldp session detail
show router ldp neighbor                         # LDP neighbors
show router ldp interface                        # LDP-enabled interfaces
show router ldp bindings                         # LDP label bindings (local + remote)
show router ldp bindings detail
show router ldp statistics                       # LDP PDU counters

# RSVP / TE
show router rsvp session                         # RSVP sessions
show router rsvp session detail
show router rsvp neighbor                        # RSVP neighbors
show router rsvp interface                       # RSVP-enabled interfaces
show router rsvp statistics                      # RSVP signaling counters
show router mpls lsp                             # all LSPs, state, bandwidth
show router mpls lsp detail                      # ERO, path, CSPF detail
show router mpls lsp ingress                     # LSPs originating here
show router mpls lsp egress                      # LSPs terminating here
show router mpls lsp transit                     # LSPs passing through
show router mpls lsp "TO-R2" detail             # specific LSP
show router mpls lsp statistics                  # per-LSP traffic counters
show router mpls interface                       # MPLS-enabled interfaces

# TE Database
show router te-database                          # Traffic Engineering Database
show router te-database detail
show router cspf to 10.0.0.2                    # CSPF path computation

# Label forwarding
show router fib 1 summary                        # FIB summary (FIB instance 1)
show router tunnel-table                         # tunnel/NHLFE table (like mpls.0)
show router tunnel-table detail

# Segment Routing
show router isis segment-routing prefix-sids     # SR prefix SIDs
show router sr-te lsp                            # SR-TE LSPs
show router sr-te lsp detail
show router sr policy                            # SR policies
show router sr policy detail

# SRv6
show router srv6 locator                         # SRv6 locators
show router srv6 sid                             # SRv6 SIDs
```

### L3VPN (VPRN)

```
show router 100 interface                        # VPRN 100 interfaces
show router 100 route-table                      # VPRN 100 routing table
show router 100 bgp summary                      # BGP in VPRN 100
show service id 100 base                         # VPRN service summary
show service vprn                                # all VPRN services
show router 100 route-table protocol bgp         # BGP routes in VPRN
```

### Configuration Examples

```
# Enable MPLS on interface and enable LDP
/configure router "Base" {
    mpls {
        admin-state enable
        interface "to-peer" {
            admin-state enable
        }
    }
    ldp {
        admin-state enable
        interface "to-peer" {
            admin-state enable
        }
        interface "system" {
            admin-state enable
        }
    }
    rsvp {
        admin-state enable
        interface "to-peer" {
            admin-state enable
        }
    }
}

# RSVP-TE LSP
/configure router "Base" {
    mpls {
        lsp "TO-R2" {
            admin-state enable
            to 10.0.0.2
            primary "PATH-TO-R2" {
                admin-state enable
            }
        }
        path "PATH-TO-R2" {
            admin-state enable
            hop 1 {
                ip-address 10.0.1.1
                type strict
            }
            hop 2 {
                ip-address 10.0.0.2
                type strict
            }
        }
    }
}

# SR-MPLS with IS-IS
/configure router "Base" {
    isis 0 {
        segment-routing {
            admin-state enable
        }
    }
}
/configure router "Base" {
    interface "system" {
        ipv4-node-sid {
            index 1
        }
    }
}

# L3VPN (VPRN)
/configure service {
    vprn 100 {
        admin-state enable
        customer "default"
        route-distinguisher "65000:100"
        vrf-target {
            community "target:65000:100"
        }
        interface "to-ce" {
            port 1/1/5:0
            ipv4 {
                primary {
                    address 172.16.0.1
                    prefix-length 30
                }
            }
        }
        bgp {
            group "CE-PEERS" {
                family {
                    ipv4 true
                }
                neighbor 172.16.0.2 {
                    peer-as 65100
                }
            }
        }
    }
}
```

---

## 10. IPv6 Commands

### Key IPv6 Concepts in SR OS

SR OS handles IPv4 and IPv6 as separate address families on the same interface, similar to JunOS. IPv6 routes live in the main routing table alongside IPv4. All routing protocols have native IPv6 support. The distinction between `family ipv4` and `family ipv6` appears throughout configuration.

### IPv6 Interface Show Commands

```
show router interface                            # shows both IPv4 and IPv6 when configured
show router interface "to-peer" detail           # full detail with IPv6 addresses
show router neighbor                             # NDP neighbor cache (like show ipv6 neighbors)
show router neighbor "to-peer"                   # NDP for specific interface
show router neighbor detail
```

Sample interface output with dual-stack:
```
===============================================================================
Interface Table (Router: Base)
===============================================================================
Interface-Name    Adm   Opr(v4/v6)  Mode   Port/SapId        IPv4 Addr/mask
                                                               IPv6 Addr/mask
-------------------------------------------------------------------------------
system            Up    Up/Up       NKBL   system            10.0.0.1/32
                                                               2001:db8:0:1::1/128
to-peer           Up    Up/Up       NKBL   1/1/1             192.0.2.1/30
                                                               2001:db8:1::1/64
                                                               fe80::1/64(LL)
```

### IPv6 Routing Table

```
show router route-table ipv6                     # full IPv6 RIB
show router route-table ipv6 2001:db8::/32       # specific prefix
show router route-table ipv6 ::/0                # IPv6 default route
show router route-table ipv6 protocol bgp        # IPv6 BGP routes
show router route-table ipv6 protocol ospf3      # OSPFv3 routes
show router route-table ipv6 protocol isis       # IS-IS IPv6 routes
```

### IPv6 Ping and Traceroute

```
ping 2001:db8::1
ping 2001:db8::1 count 5
ping 2001:db8::1 source 2001:db8:1::1
ping router-instance 100 2001:db8::1             # ping from VPRN

traceroute 2001:db8::1
traceroute 2001:db8::1 source 2001:db8:1::1
```

### OSPFv3 (OSPF for IPv6)

```
show router ospf3 overview
show router ospf3 neighbor
show router ospf3 neighbor detail
show router ospf3 interface
show router ospf3 database
show router ospf3 route
```

**OSPFv3 Configuration:**

```
/configure router "Base" {
    ospf3 0 {
        admin-state enable
        router-id 10.0.0.1
        area 0.0.0.0 {
            interface "system" {
                passive true
            }
            interface "to-peer" {
                interface-type point-to-point
                metric 10
            }
        }
    }
}

# Interface requires IPv6 address
/configure router "Base" {
    interface "to-peer" {
        ipv6 {
            address 2001:db8:1::1 {
                prefix-length 64
            }
        }
    }
}
```

### IS-IS with IPv6

IS-IS natively supports both IPv4 and IPv6 under the same adjacency. Multi-topology IS-IS for IPv6 is configured per the `ipv6-unicast` topology.

```
show router isis routes ipv4-unicast
show router isis routes ipv6-unicast             # IS-IS IPv6 routes
show router route-table ipv6 protocol isis
```

**IS-IS IPv6 Configuration:**

```
/configure router "Base" {
    isis 0 {
        ipv6-routing mt-ipv6                     # multi-topology IS-IS for IPv6
        level 2 {
            wide-metrics-only true
        }
        interface "to-peer" {
            ipv6-unicast-metric 10
        }
    }
}

/configure router "Base" {
    interface "to-peer" {
        ipv6 {
            address 2001:db8:1::1 {
                prefix-length 64
            }
        }
    }
    interface "system" {
        ipv6 {
            address 2001:db8:0:1::1 {
                prefix-length 128
            }
        }
    }
}
```

### BGP for IPv6

```
show router bgp summary                          # shows all address families
show router bgp routes ipv6                      # BGP IPv6 unicast routes
show router bgp routes ipv6 2001:db8:100::/48   # specific prefix
show router bgp neighbor 2001:db8::2 received-routes ipv6
show router bgp neighbor 2001:db8::2 advertised-routes ipv6
```

**BGP IPv6 Configuration:**

```
/configure router "Base" {
    bgp {
        group "IBGP-V6" {
            type internal
            local-address 2001:db8:0:1::1
            family {
                ipv6 true
            }
            next-hop-self true
            neighbor 2001:db8:0:2::1 { }
        }

        group "EBGP-V6" {
            type external
            family {
                ipv6 true
            }
            neighbor 2001:db8:peer::2 {
                peer-as 65001
            }
        }
    }
}
```

### 6PE / 6VPE (IPv6 over MPLS)

```
# 6PE — labeled IPv6 over IPv4/MPLS core
show router bgp routes label-ipv6                # labeled IPv6 routes

# 6VPE — IPv6 within a VPRN
show router 100 route-table ipv6
```

**6PE Configuration:**

```
/configure router "Base" {
    bgp {
        group "6PE" {
            type internal
            family {
                label-ipv6 true                  # labeled unicast IPv6
            }
            neighbor 10.0.0.2 { }
        }
    }
}
```

### IPv6 Configuration Reference

```
# Dual-stack interface
/configure router "Base" {
    interface "to-peer" {
        ipv4 {
            primary {
                address 192.0.2.1
                prefix-length 30
            }
        }
        ipv6 {
            address 2001:db8:1::1 {
                prefix-length 64
            }
        }
    }
}

# Static IPv6 routes
/configure router "Base" {
    static-routes {
        route "::/0" route-type unicast {
            next-hop "2001:db8:1::2" {
                admin-state enable
            }
        }
        route "2001:db8:100::/48" route-type unicast {
            next-hop "2001:db8:1::2" {
                admin-state enable
            }
        }
    }
}
```

### IPv6 Cross-Platform Comparison

| Function | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|
| Show IPv6 interfaces | `show router interface` | `show interfaces terse` | `show ipv6 interface brief` |
| IPv6 NDP table | `show router neighbor` | `show ipv6 neighbors` | `show ipv6 neighbors` |
| IPv6 route table | `show router route-table ipv6` | `show route table inet6.0` | `show ipv6 route` |
| IPv6 BGP routes | `show router bgp routes ipv6` | `show route table inet6.0 protocol bgp` | `show bgp ipv6 unicast` |
| OSPFv3 neighbors | `show router ospf3 neighbor` | `show ospf3 neighbor` | `show ipv6 ospf neighbor` |
| IS-IS IPv6 routes | `show router route-table ipv6 protocol isis` | `show route table inet6.0 protocol isis` | `show ipv6 route isis` |
| IPv6 ping | `ping 2001:db8::1` | `ping 2001:db8::1` | `ping ipv6 2001:db8::1` |

---

## 11. Configuration Management

### Viewing and Comparing Configuration

```
info                                    # current config context (hierarchical)
info detail                             # all attributes including defaults
info flat                               # flat absolute-path format (like display set)
info | as-json                          # JSON representation
compare                                 # diff candidate vs committed (active)
compare baseline                        # diff candidate vs session baseline
compare committed                       # same as 'compare' — committed = active
```

### Commit Operations

```
commit                                  # apply candidate config atomically
commit confirmed 300                    # commit, auto-rollback in 300 seconds
commit confirmed 300 persist            # make commit persistent even after reboot
commit confirmed-accept                 # confirm a 'commit confirmed'
validate                                # validate syntax without committing
discard                                 # discard all pending changes
discard stay                            # discard changes but stay in config mode
```

### Editing Configuration

MD-CLI configuration uses curly-brace block syntax or inline path notation:

```
# Block style (navigate to context first)
/configure router "Base" ospf 0
  area 0.0.0.0 {
      interface "to-peer" {
          metric 20
      }
  }

# Inline path style (absolute path from anywhere)
/configure router "Base" ospf 0 area 0.0.0.0 interface "to-peer" metric 20

# Delete a list entry
delete /configure router "Base" ospf 0 area 0.0.0.0 interface "to-peer"

# Delete a leaf value (restore to default)
/configure router "Base" ospf 0 area 0.0.0.0 interface "to-peer" metric 1
# or
delete /configure router "Base" ospf 0 area 0.0.0.0 interface "to-peer" metric
```

### Save and Load Configuration

```
# Save running config to file
admin save cf3:\backups\config-backup.cfg

# Load/restore from file
admin revert cf3:\backups\config-backup.cfg    # full config replacement

# Show saved config files
file list cf3:\

# Configuration rollback (uses committed checkpoints)
tools rollback compare 1                       # show diff vs rollback 1
tools rollback revert 1                        # revert to rollback checkpoint 1
```

### Configuration Checkpoints and Rollback

SR OS automatically saves configuration checkpoints on each commit. You can also manually create named checkpoints.

```
show system rollback                            # list available rollback checkpoints
tools rollback compare 1                        # diff active vs rollback 1
tools rollback compare 0 2                      # diff rollback 0 vs rollback 2
tools rollback revert 1                         # revert to rollback checkpoint 1
tools rollback revert latest-rb                 # revert to most recent rollback
```

### Rescue Configuration

```
admin display-config                            # display entire active config
admin rollback revert                           # rollback to last committed (emergency)
```

---

## 12. Platform & Silicon Details

Nokia's platform strategy differs fundamentally from Arista's merchant-silicon-only approach. Nokia designs its **FP (Forwarding Processor) ASICs** in-house — the FP4 and FP5 are Nokia proprietary silicon with architectures specifically optimized for deep buffering, VOQ, and service provider feature breadth. Nokia also offers IXR-series platforms built on Broadcom merchant silicon for cost-sensitive segments.

For detailed per-chipset and per-platform buffer specifications, see: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

### Silicon Overview

| Silicon | Vendor | Type | Buffer Architecture | MPLS | Notes |
|---|---|---|---|---|---|
| FP4 | Nokia | Proprietary | VOQ, deep distributed | Full | 7750 SR, 7950 XRS |
| FP5 | Nokia | Proprietary | VOQ, deep distributed, 400G | Full | 7750 SR-1se, 7750 SR-1-24D |
| Jericho2 | Broadcom | Merchant | Deep HBM external | Full | 7250 IXR-R6, IXR-ec |
| Jericho2c | Broadcom | Merchant | Deep HBM external | Full | 7250 IXR-ec variants |
| Trident3 | Broadcom | Merchant | Shallow on-chip | Limited | 7220 IXR-D |
| Tomahawk3 | Broadcom | Merchant | Shallow on-chip | No | 7220 IXR-H |

### Platform Hardware Overview

| Platform | Role | Silicon | Key Interfaces | Notes |
|---|---|---|---|---|
| 7750 SR-1 | Edge/aggregation | FP4 | 2×FP4 IMMs, up to 400G | Full service set, compact |
| 7750 SR-7/12 | Core/edge | FP4 | Modular, 10G–400G | Workhorse SP router |
| 7750 SR-1se | Next-gen edge | FP5 | 400G native, 800G-capable | FP5 silicon — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7950 XRS-20/40 | Core routing | FP4/FP5 | High-density 400G | Large chassis core |
| 7250 IXR-R6 | IP/MPLS edge | Jericho2 | 6-slot, 400G | Merchant silicon — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7250 IXR-ec | Compact edge | Jericho2c | Fixed 100G/400G | Deep-buffer, merchant — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-D | Data center leaf | Trident3 | 48×25G + 8×100G | Shallow buffer — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7220 IXR-H | Data center spine | Tomahawk3 | 32×100G or 8×400G | Shallow buffer — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| 7705 SAR-8/18 | Mobile aggregation | Purpose-built | Mixed interface types | Mobile fronthaul/backhaul |
| 7210 SAS | Service access | FP3 | Various 1G–10G | MEF Carrier Ethernet access |
| 1830 PTS | Precision timing | FPGA | 1G/10G | Sub-100ns timing appliance |

### FP4 / FP5 Architecture (Nokia Proprietary)

Nokia's FP ASIC family is the primary differentiator for the 7750 SR and 7950 XRS platforms. Key architectural properties:

- **Virtual Output Queuing (VOQ)**: Every ingress port maintains separate per-egress-port queues. Eliminates head-of-line blocking under any traffic pattern.
- **Deep distributed buffers**: Memory is distributed across the switch fabric and line cards, not concentrated on a single ASIC.
- **Programmable pipelines**: FP4/FP5 support flexible protocol processing including SRv6, BIER, and emerging protocols.
- **High-scale forwarding tables**: eTCAM or equivalent provides millions of forwarding entries without on-chip TCAM constraints.
- **Fabric redundancy**: Full mesh switch fabric with N+1 redundancy in modular chassis.

For per-platform VOQ configuration, queue depth, and buffer sizing details: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

### Feature Matrix by Silicon

| Feature | FP4/FP5 (7750/7950) | Jericho2 (7250 IXR) | Trident3 (7220 IXR-D) |
|---|---|---|---|
| L3 routing (OSPF/IS-IS/BGP) | Yes | Yes | Yes |
| MPLS / LDP / RSVP-TE | Full | Full | No |
| SR-MPLS | Full | Full | No |
| SRv6 | Full | Yes | Limited |
| EVPN (MPLS data plane) | Yes | Yes | No |
| EVPN-VXLAN | Yes | Yes | Yes |
| L3VPN (VPRN) | Yes | Yes | Yes |
| VPLS / EPIPE | Yes | Yes | Limited |
| PTP Grandmaster | Yes (with GNSS) | Yes (with GNSS) | No |
| PTP Boundary Clock | Yes | Yes | No |
| SyncE | Yes | Yes | No |
| BITS | Yes | No | No |
| Y.1731 / CFM | Yes | Yes | Limited |
| Subscriber management | Full (ESM) | Limited | No |
| Buffer depth | Very deep (VOQ) | Deep (HBM) | Shallow |
| External TCAM | Yes (eTCAM) | Yes (eTCAM) | No |
| NSR (Non-Stop Routing) | Yes | Yes | No |

---

### Timing and Synchronization (7750 SR / 7705 SAR / 7250 IXR)

Nokia is widely regarded as the industry leader in network timing. The 7750 SR and 7705 SAR platforms support the full ITU-T timing hierarchy including IEEE 1588v2 Grandmaster (with GNSS), Boundary Clock (Class B/C per G.8273.2), SyncE, and BITS. The 1830 PTS appliance provides FPGA-based sub-100ns precision.

#### Clock Hierarchy

```
GNSS → Grandmaster (7750 SR with GNSS card) → Boundary Clocks → Slave devices
SyncE flows independently on the physical layer alongside PTP messages
BITS provides building-integrated timing for telco environments
```

#### PTP Show Commands

```
show router ptp clock                            # local clock identity, domain, state
show router ptp port                             # per-port PTP state (Master/Slave/Passive)
show router ptp port detail                      # announce interval, sync interval, role
show router ptp statistics                       # per-port message counters
show router ptp statistics detail
show router ptp path-trace                       # path trace TLV (if enabled)
show router ptp servo                            # clock servo state, frequency offset
show router ptp peer                             # all known PTP peers/masters
```

PTP clock states:
```
Locking     # searching for master, phase alignment in progress
Locked      # synchronized to master, servo stable
Holdover    # master lost, coasting on local oscillator (OCXO)
Free-run    # no master, internal clock only
```

#### SyncE Show Commands

```
show router sync-if-timing                       # SyncE source and QL status
show router sync-if-timing detail                # per-interface SSM QL values
show port 1/1/1 detail | match Sync             # SyncE state on a port
```

#### GNSS Show Commands (7750 SR with GNSS option)

```
show chassis gnss                                # satellite lock, fix type
show chassis gnss detail                         # satellite count, signal quality, coordinates
```

#### Timing Configuration

```
# PTP Boundary Clock
/configure router "Base" {
    ptp {
        admin-state enable
        clock {
            domain 24
            priority1 128
            priority2 128
            profile ieee1588-2008
        }
        port 1 {
            admin-state enable
            role slave
            address {
                ip-address 192.0.2.1
            }
            unicast-master {
                address 192.0.2.100 { }
            }
        }
        port 2 {
            admin-state enable
            role master
        }
    }
}

# SyncE — enable on interface
/configure port 1/1/1 {
    ethernet {
        sync-e-profile option1              # SONET/SDH SSM option 1
    }
}
/configure router "Base" {
    sync-if-timing {
        ref-order [port-1 port-2]
        ref1 {
            source-port 1/1/1
        }
        ref2 {
            source-port 1/1/2
        }
    }
}
```

---

### Carrier Ethernet OAM

Nokia SR OS supports IEEE 802.1ag CFM, ITU-T Y.1731, and TWAMP for Carrier Ethernet SLA monitoring.

#### CFM / 802.1ag Show Commands

```
show oam eth-cfm domain "CARRIER"              # maintenance domain state
show oam eth-cfm domain "CARRIER" association "MA-SVC-100"  # MA detail
show oam eth-cfm mep domain "CARRIER" association "MA-SVC-100" mep 1
show oam eth-cfm mep domain "CARRIER" association "MA-SVC-100" mep 1 detail
show oam eth-cfm ccm-defects                   # continuity check defects
```

#### Y.1731 Performance Monitoring

```
show oam eth-test results                      # ETH-Test results
show oam y1731 delay results                   # frame delay and delay variation
show oam y1731 loss results                    # frame loss ratio
```

#### CFM Configuration

```
/configure eth-cfm {
    domain "CARRIER" {
        level 4
        format none
        association "MA-SVC-100" {
            format icc-based
            name "MA-SVC-100"
            ccm-interval 1
            bridge-identifier 200 {
                vlan 100
            }
            mep 1 {
                admin-state enable
                direction down
                port 1/1/1
                vlan 100
                auto-discovery true
                y1731-perf-enabled true
            }
        }
    }
}
```

#### TWAMP (Two-Way Active Measurement Protocol)

```
show oam twamp-light session                   # TWAMP-Light session state
show oam twamp-light session detail            # per-session delay and loss
show oam twamp-light statistics                # aggregate statistics
```

---

### Chassis and Hardware Commands

```
show chassis                                     # chassis state, uptime
show chassis detail                              # firmware, hardware revision
show chassis environment                         # temperature, fan, power
show chassis environment all
show chassis power-supply                        # PSU state and capacity
show card                                        # all line cards and IMMs
show card detail
show mda                                         # all MDAs (media-dependent adapters)
show mda detail
show system alarms                               # active alarms
show card 1 fp detail                            # FP ASIC state on card 1
show card 1 fp 1 stats                           # FP forwarding counters
show port 1/1/1 optical                          # transceiver DOM
show system cpu                                  # CPM CPU utilization
show system memory-pools                         # CPM memory usage
```

### Hardware and Interface Naming

SR OS hardware naming:

```
1/1/1          # slot 1, MDA 1, port 1 (modular chassis)
1/1/c1/1       # slot 1, MDA 1, QSFP/CFP connector 1, breakout 1
A              # CPM card A (primary)
B              # CPM card B (secondary / standby)
```

MDA types affect available port speeds and form factors. Port speed and mode are configured at `/configure port`:

```
/configure port 1/1/1 {
    admin-state enable
    description "100G to Peer"
    ethernet {
        speed 100000             # 100G
        mode network
    }
}
```

---

### Class of Service (QoS)

Nokia SR OS CoS is built on a rich, policy-based model that abstracts physical queue characteristics from the policy definition. The FP4/FP5 VOQ architecture means queuing decisions are made at ingress based on egress port state — there is no blocking on a congested egress. Buffer allocation and queue configuration are decoupled from the CoS policy itself.

For queue count, VOQ sizing, and per-port scheduling parameters by platform and FP generation: **[https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)**

```
show qos sap-ingress 1                           # SAP ingress QoS policy
show qos sap-egress 1                            # SAP egress QoS policy
show qos network-queue 1                         # network queue policy
show qos network 1                               # network ingress policy
show port 1/1/1 access egress                    # applied egress CoS state
show port 1/1/1 access egress queue              # per-queue statistics
show port 1/1/1 network egress queue             # network-side queue stats
```

**Basic CoS Configuration Pattern:**

```
# Network queue policy (for router interfaces and network-side ports)
/configure qos {
    network-queue "CORE-QUEUES" {
        queue 1 {
            rate {
                percent-rate 30.00
                percent-burst 50.00
            }
            priority strict-high
        }
        queue 8 {
            rate {
                percent-rate 100.00
                percent-burst 100.00
            }
        }
    }
}

# DSCP-to-FC (Forwarding Class) mapping
/configure qos {
    dscp-table "DSCP-MAP" {
        dscp ef {
            fc "ef"
            profile out
        }
        dscp af41 {
            fc "af"
            profile out
        }
    }
}

# Apply to network interface
/configure router "Base" {
    interface "to-peer" {
        qos {
            network-policy 1
        }
    }
}
```

---

### SR OS Operational Tips

```
# Verify PTP timing lock before activating a service
show router ptp servo
show router ptp port detail | match "State|Offset|Delay"

# Check all active alarms before maintenance
show system alarms

# Verify pseudowire status across all services
show service epipe | match "Up|Down|Id"

# Check OAM CCM defects
show oam eth-cfm ccm-defects

# Confirm SyncE QL on uplinks
show router sync-if-timing detail | match "QL|Source|Interface"

# Monitor FP ASIC forwarding counters
show card 1 fp 1 stats

# Verify SR-MPLS label forwarding table
show router tunnel-table detail | match "1600"

# Check EVPN MAC/IP routes
show service id 300 evpn mac

# Confirm VPRN routing table
show router 100 route-table

# Tail the main event log
show log 99 | tail 50

# View all log events matching BGP
show log 99 | match BGP

# Verify RSVP-TE LSP status
show router mpls lsp detail

# Confirm CSPF path to destination
show router cspf to 10.0.0.2

# Non-Stop Routing (NSR) state
show system nsr
```

### Licensing

Nokia SR OS is feature-licensed per platform. License validation is enforced at startup and feature activation.

```
show system license                              # installed licenses
show system license detail                       # per-feature license state
```

Key licensed features (varies by platform):
- **Base** — OSPF, IS-IS, BGP, static routing, basic L2
- **Advanced Routing** — MPLS, LDP, RSVP-TE, SR-MPLS
- **Services** — VPRN, VPLS, EPIPE, IES
- **EVPN** — BGP EVPN control plane
- **Timing** — PTP, SyncE (sometimes included in hardware SKU)
- **Subscriber Management** — ESM, RADIUS, BNG capability

---

## 13. Cross-Platform Command Reference

### General & Interface Commands

| Function | Nokia SR OS MD-CLI | JunOS | EOS | IOS-XE |
|---|---|---|---|---|
| Show interfaces brief | `show router interface` | `show interfaces terse` | `show interfaces status` | `show ip interface brief` |
| Show interface detail | `show router interface "to-peer" detail` | `show interfaces ge-0/0/0` | `show interfaces Ethernet1` | `show interface Gi0/0/0` |
| Show port counters | `show port 1/1/1 statistics` | `show interfaces statistics` | `show interfaces Ethernet1 counters` | `show interface Gi0/0/0` |
| Show all MAC addresses | `show service id 200 fdb` | `show ethernet-switching table` | `show mac address-table` | `show mac address-table` |
| Disable interface/port | `/configure port 1/1/1 admin-state disable` | `set interfaces ge-0/0/0 disable` | `shutdown` (interface mode) | `shutdown` (interface mode) |
| Show running config | `info flat` (config mode) | `show configuration` | `show running-config` | `show running-config` |
| Show config section | `info` (at context) | `show config protocols bgp` | `show running-config \| section bgp` | `show running-config \| section bgp` |
| Enter config mode | `edit-config exclusive` | `configure exclusive` | `configure terminal` | `configure terminal` |
| Save config | `admin save` | `commit` | `write memory` | `write memory` |
| Commit / apply | `commit` | `commit` | `write memory` (immediate) | immediate |
| Rollback | `tools rollback revert 1` | `rollback 1` + `commit` | `configure replace checkpoint:X` | copy startup-config |
| Config diff | `compare` | `show config \| compare` | `show running-config diff` | no native equivalent |
| Validate | `validate` | `commit check` | `configure session` + diffs | limited |

### Routing Protocol — OSPF

| Function | Nokia SR OS MD-CLI | JunOS | EOS | IOS-XE |
|---|---|---|---|---|
| OSPF neighbors | `show router ospf neighbor` | `show ospf neighbor` | `show ip ospf neighbor` | `show ip ospf neighbor` |
| OSPF neighbor detail | `show router ospf neighbor detail` | `show ospf neighbor detail` | `show ip ospf neighbor detail` | `show ip ospf neighbor detail` |
| OSPF interfaces | `show router ospf interface` | `show ospf interface` | `show ip ospf interface` | `show ip ospf interface` |
| OSPF LSDB | `show router ospf database` | `show ospf database` | `show ip ospf database` | `show ip ospf database` |
| OSPF routes | `show router route-table protocol ospf` | `show route protocol ospf` | `show ip route ospf` | `show ip route ospf` |
| OSPF summary | `show router ospf overview` | `show ospf overview` | `show ip ospf` | `show ip ospf` |
| OSPFv3 neighbors | `show router ospf3 neighbor` | `show ospf3 neighbor` | `show ipv6 ospf neighbor` | `show ipv6 ospf neighbor` |

### Routing Protocol — IS-IS

| Function | Nokia SR OS MD-CLI | JunOS | EOS | IOS-XE |
|---|---|---|---|---|
| IS-IS adjacencies | `show router isis adjacency` | `show isis adjacency` | `show isis neighbors` | `show isis neighbors` |
| IS-IS adjacency detail | `show router isis adjacency detail` | `show isis adjacency detail` | `show isis neighbors detail` | `show isis neighbors detail` |
| IS-IS interfaces | `show router isis interface` | `show isis interface` | `show isis interface` | `show isis interface` |
| IS-IS LSDB | `show router isis database` | `show isis database` | `show isis database` | `show isis database` |
| IS-IS LSDB detail | `show router isis database detail` | `show isis database detail` | `show isis database detail` | `show isis database verbose` |
| IS-IS routes | `show router route-table protocol isis` | `show route protocol isis` | `show ip route isis` | `show ip route isis` |
| IS-IS overview | `show router isis overview` | `show isis overview` | `show isis summary` | `show isis` |

### Routing Protocol — BGP

| Function | Nokia SR OS MD-CLI | JunOS | EOS | IOS-XE |
|---|---|---|---|---|
| BGP summary | `show router bgp summary` | `show bgp summary` | `show bgp summary` | `show ip bgp summary` |
| BGP neighbors | `show router bgp neighbor` | `show bgp neighbor` | `show bgp neighbors` | `show ip bgp neighbors` |
| BGP neighbor detail | `show router bgp neighbor 10.0.0.2` | `show bgp neighbor 10.0.0.2` | `show bgp neighbors 10.0.0.2` | `show ip bgp neighbors 10.0.0.2` |
| BGP routes | `show router bgp routes ipv4` | `show route protocol bgp` | `show bgp ipv4 unicast` | `show ip bgp` |
| BGP route detail | `show router bgp routes 10.0.0.0/8 detail` | `show route 10/8 detail` | `show bgp ipv4 unicast 10.0.0.0/8` | `show ip bgp 10.0.0.0/8` |
| Routes received | `show router bgp neighbor X received-routes ipv4` | `show bgp neighbor X received-routes` | `show bgp neighbors X received-routes` | `show ip bgp neighbors X received-routes` |
| Routes advertised | `show router bgp neighbor X advertised-routes ipv4` | `show bgp neighbor X advertised-routes` | `show bgp neighbors X advertised-routes` | `show ip bgp neighbors X advertised-routes` |
| VPN routes | `show router 100 route-table` | `show route table CUST-A.inet.0` | `show bgp vpnv4 unicast vrf CUST-A` | `show ip bgp vpnv4 vrf CUST-A` |

### MPLS

| Function | Nokia SR OS MD-CLI | JunOS | EOS | IOS-XE |
|---|---|---|---|---|
| LDP neighbors | `show router ldp neighbor` | `show ldp neighbor` | `show mpls ldp neighbor` | `show mpls ldp neighbor` |
| LDP label bindings | `show router ldp bindings` | `show ldp database` | `show mpls ldp bindings` | `show mpls ldp bindings` |
| MPLS label table | `show router tunnel-table` | `show route table mpls.0` | `show mpls lfib route` | `show mpls forwarding-table` |
| RSVP sessions | `show router rsvp session` | `show rsvp session` | `show mpls rsvp session` | `show ip rsvp session` |
| TE LSPs | `show router mpls lsp` | `show mpls lsp` | `show mpls traffic-eng tunnels` | `show mpls traffic-eng tunnels` |
| TE LSP detail | `show router mpls lsp detail` | `show mpls lsp detail` | `show mpls traffic-eng tunnels detail` | `show mpls traffic-eng tunnels detail` |
| TE database | `show router te-database` | `show ted database` | `show mpls traffic-eng topology` | `show mpls traffic-eng topology` |

### L2 Services / VLANs

| Function | Nokia SR OS MD-CLI | JunOS | EOS |
|---|---|---|---|
| L2 service summary | `show service id 100 base` | `show vpls connections` / `show l2circuit connections` | `show vxlan vtep` |
| MAC table | `show service id 100 fdb` | `show ethernet-switching table` | `show mac address-table` |
| L2 neighbor MAC | `show service id 100 fdb detail` | `show ethernet-switching table detail` | `show mac address-table detail` |
| Pseudowire state | `show service epipe` | `show l2circuit connections` | N/A |
| Spanning tree | `show service id 100 stp` | `show spanning-tree bridge` | `show spanning-tree` |
| EVPN routes | `show service id 100 evpn routes` | `show route table bgp.evpn.0` | `show bgp evpn` |
| L3 VPN table | `show router 100 route-table` | `show route table CUST-A.inet.0` | `show ip route vrf CUST-A` |
| All VPNs | `show service vprn` | `show route instance` | `show vrf` |

### System & Diagnostics

| Function | Nokia SR OS MD-CLI | JunOS | EOS | IOS-XE |
|---|---|---|---|---|
| Ping | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 count 5` | `ping 8.8.8.8 repeat 5` | `ping 8.8.8.8 repeat 5` |
| Traceroute | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` | `traceroute 8.8.8.8` |
| Show ARP | `show router arp` | `show arp` | `show arp` | `show ip arp` |
| Show routes | `show router route-table` | `show route` | `show ip route` | `show ip route` |
| Route detail | `show router route-table 10.0.0.0/8 detail` | `show route 10/8 detail` | `show ip route 10.0.0.0/8` | `show ip route 10.0.0.0` |
| Disable paging | `environment more false` | `set cli screen-length 0` | `terminal length 0` | `terminal length 0` |
| Show version | `show version` | `show version` | `show version` | `show version` |
| Show hardware | `show chassis detail` | `show chassis hardware` | `show inventory` | `show inventory` |
| Logs | `show log 99` | `show log messages` | `show logging` | `show logging` |
| Follow logs live | `debug router ... ` (structured) | `monitor start messages` | `bash tail -f /var/log/messages` | `terminal monitor` |
| CPU/memory | `show system cpu` | `show chassis routing-engine` | `show processes top` | `show processes cpu` |
| Reboot | `admin reboot` | `request system reboot` | `reload` | `reload` |
| Save config | `admin save` | `commit` | `write memory` | `write memory` |
| Grep equivalent | `show ... \| match <regex>` | `show ... \| match <regex>` | `show ... \| include <regex>` | `show ... \| include <regex>` |
| Exclude equivalent | `show ... \| match <regex> invert-match` | `show ... \| except <regex>` | `show ... \| exclude <regex>` | `show ... \| exclude <regex>` |
| Count lines | `show ... \| count` | `show ... \| count` | `show ... \| count` | `show ... \| count` |
| JSON output | `show ... \| as-json` | `show ... \| display json` | `show ... \| json` | limited |

---

## 14. Quick Reference Card

### Top 20 Daily-Driver Commands

```bash
# System health
show version                              # SR OS version, model, serial
show chassis environment                  # temperature, fans, power
show log 99 | tail 100                   # recent syslog events
show system alarms                        # active platform alarms

# Ports and interfaces
show port                                 # all ports and link state
show router interface                     # all L3 interfaces

# Routing
show router route-table                   # full routing table
show router route-table summary           # route count by protocol
show router route-table protocol bgp      # BGP routes in RIB
show router arp                           # ARP table

# BGP / OSPF / IS-IS
show router bgp summary                   # BGP peer state at a glance
show router ospf neighbor                 # OSPF adjacencies
show router isis adjacency                # IS-IS adjacencies

# MPLS
show router mpls lsp                      # RSVP-TE LSP state
show router ldp session                   # LDP sessions
show router tunnel-table | head 30        # top of label forwarding table

# Config workflow (MD-CLI)
info flat | no-more                       # running config as flat commands
compare                                   # staged vs committed config diff
validate                                  # validate before committing
```

### Useful One-Liners

```bash
# Count BGP prefixes in RIB
show router route-table protocol bgp | count

# Show only established BGP sessions
show router bgp summary | match "Establ"

# Show all BGP sessions NOT established
show router bgp summary | match "Establ" invert-match

# Find interfaces that are operationally down
show router interface | match "Down"

# Find ports that are link-down
show port | match "down"

# Show OSPF neighbors not in Full state
show router ospf neighbor | match "Full" invert-match

# Get config for a specific IP anywhere in config
info flat | match "192.0.2.1"

# Check MPLS tunnel table for a specific label range
show router tunnel-table | match "1600[0-9]"

# Tail event log for BGP events
show log 99 | tail 50 | match BGP

# Check PTP servo offset and lock state
show router ptp servo

# Verify all EPIPE pseudowires up
show service epipe | match "Up\|Dn"

# Confirm SR-MPLS node SID advertisement
show router isis segment-routing prefix-sids | match "system"

# Diff current candidate vs committed
compare

# Show FP ASIC forwarding drops
show card 1 fp 1 stats | match "drop\|Drop"
```

### Nokia SR OS MD-CLI Mental Models

| Concept | Nokia SR OS Way | Notes |
|---|---|---|
| Config is always a candidate | Edit → `commit` to apply | `validate` checks syntax without applying |
| MD-CLI uses YANG paths | `/configure router "Base" ospf 0 area 0.0.0.0` | Named objects always quoted, integer IDs never |
| `info flat` = `display set` | Flat, absolute-path config representation | Essential for documentation and diffing |
| `compare` = config diff | Shows pending changes vs committed | Equivalent to JunOS `show config \| compare` |
| `back` / `top` navigation | Like JunOS `up` / `top` | `exit` leaves configure mode entirely |
| Port ≠ Interface | Port is physical; interface is L3 named object | Must bind interface to port explicitly |
| "system" interface = loopback | Always named `"system"` in Base router | Like JunOS `lo0` |
| SAP notation | `port:vlan-tag` = service attachment | `1/1/1:100` = port 1/1/1, dot1q 100 |
| Services are numbered | `vprn 100`, `vpls 200`, `epipe 300` | Service ID is the primary reference |
| VOQ architecture | Per-egress queuing at ingress | Deep buffers, no HOL blocking — see [port-buffers.forwardingplane.net](https://port-buffers.forwardingplane.net/) |
| NSR (Non-Stop Routing) | CPM failover without routing reconvergence | Requires redundant CPM — check `show system nsr` |
| FP4/FP5 vs. IXR | Nokia proprietary vs. Broadcom merchant silicon | Feature set and buffers differ significantly |
| `tools perform` | Operational actions that modify state | Debug clear, TWAMP start, rollback revert |
| `admin save` | Write config to flash | Equivalent to JunOS `commit` persistence |

---

*Curriculum version: 1.0 | Target: Nokia SR OS MD-CLI — 7750 SR / 7950 XRS / 7250 IXR / 7220 IXR platforms*
*Reference platforms for comparison: Juniper JunOS MX/ACX, Arista EOS, Cisco IOS-XE 17.x*
*Platform buffer and silicon details: [https://port-buffers.forwardingplane.net/](https://port-buffers.forwardingplane.net/)*

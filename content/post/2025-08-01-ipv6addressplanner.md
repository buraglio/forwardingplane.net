---
title: IPv6Planner - a basic IPv6 subnet planning tool
date: 2025-08-01
author: Nick Buraglio
layout: post
categories:
    - addressplanning
    - ipv6
    - golang
tags:
    - ipv6
    - basics
    - programming
---


There are so many ways to create IPv6 Subnet plans. As discussed in [IPv6 Buzz 180](https://packetpushers.net/podcasts/ipv6-buzz/ipb180-ipv6-basics-deployment/), an address plan is one of, if not the first step. Because getting started in the IPv6 subnet planning can be somewhat daunting, I wrote this go application to help bootstrap the process. [This open source tool](https://github.com/buraglio/ipv6planner) can be used along with the [web version of ipv6utils](https://tools.forwardingplane.net), or the CLI tool.

It's not the Swiss army knife, but it's enough to build a starting point. It currently supports:

- Generating IPv6 address plans from a base subnet
- Supports multiple Points of Presence (POPs)
- Creates hierarchical subnet levels within each POP
- Calculates and displays available subnet counts at each level
- Multiple output formats (text, JSON, HTML)
- Interactive mode for guided input
- Comprehensive help system

Example output:

```
This tool is not intended to provide a comprehensive address plan.
It should be used to generate a top level heirarchy of IPv6 address plans.
IPv6 Address Plan
Base Subnet: 3fff:db8::/32
Number of POPs: 10
Preferred POP subnet size: /40
Subnet levels: /[48 52 56 64]

Global Subnet Counts:
  /48: 65536 available subnets
  /52: 1048576 available subnets
  /56: 16777216 available subnets
  /64: 4294967296 available subnets

POP Allocations:

POP 1: 3fff:db8::/40
  Level 1 (/48): 3fff:db8::/48 (Available: 256)
  Level 2 (/52): 3fff:db8::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8::/64 (Available: 16777216)

POP 2: 3fff:db8:8000::/40
  Level 1 (/48): 3fff:db8:8000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:8000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:8000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:8000::/64 (Available: 16777216)

POP 3: 3fff:db8:4000::/40
  Level 1 (/48): 3fff:db8:4000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:4000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:4000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:4000::/64 (Available: 16777216)

POP 4: 3fff:db8:c000::/40
  Level 1 (/48): 3fff:db8:c000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:c000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:c000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:c000::/64 (Available: 16777216)

POP 5: 3fff:db8:2000::/40
  Level 1 (/48): 3fff:db8:2000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:2000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:2000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:2000::/64 (Available: 16777216)

POP 6: 3fff:db8:a000::/40
  Level 1 (/48): 3fff:db8:a000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:a000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:a000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:a000::/64 (Available: 16777216)

POP 7: 3fff:db8:6000::/40
  Level 1 (/48): 3fff:db8:6000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:6000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:6000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:6000::/64 (Available: 16777216)

POP 8: 3fff:db8:e000::/40
  Level 1 (/48): 3fff:db8:e000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:e000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:e000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:e000::/64 (Available: 16777216)

POP 9: 3fff:db8:1000::/40
  Level 1 (/48): 3fff:db8:1000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:1000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:1000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:1000::/64 (Available: 16777216)

POP 10: 3fff:db8:9000::/40
  Level 1 (/48): 3fff:db8:9000::/48 (Available: 256)
  Level 2 (/52): 3fff:db8:9000::/52 (Available: 4096)
  Level 3 (/56): 3fff:db8:9000::/56 (Available: 65536)
  Level 4 (/64): 3fff:db8:9000::/64 (Available: 16777216)
```

Download it [here](https://github.com/buraglio/ipv6planner).
---
title: Go IPv6 utilities 
date: 2025-04-06
author: Nick Buraglio
layout: post
categories:
    - golang
    - ipv6
tags:
    - ipv6utils
    - nix4neteng
    - golang
    - ipv6
---

After spending some time with Python, I moved to Go, which seems to suit the way my brain works slightly better (make no mistake, I am still a poor developer). Keeping in line with the work done on [this](https://github.com/buraglio/ipv6-subnet-planner), I endeavored to re-write this in Golang, mostly because the subnet generation in python had some resource issues with large blocks. 

And off I went. With the help of an LLM to get me past weird errors and inability to compile, the resulting code is surprisingly efficient and useful - available [here](https://github.com/buraglio/ipv6utils)

### IPv6 Subnet Generator & RFC 6052 Converter 

#### Current capabilities:

A command-line utility for IPv6 subnet generation and IPv4/IPv6 address translation using RFC 6052.
The pre-compiled binary is compiled for Apple silicon, but since it's go it can be run on pretty much anything with minimal resource footprint.

## Features
- **IPv6 Subnet Generation** 
  - Generate subnets from an IPv6 prefix. 
  - Optionally limit output using `-l` flag.
- **IPv4 ↔ RFC 6052 IPv6 Conversion** 
  - Convert IPv4 to a synthesized IPv6 address (`-s IPv4`). 
  - Convert an RFC 6052 IPv6 address back to IPv4. 
- **Custom Prefix Support** (`-k`) 
  - Allows non-well-known prefixes.
- **Decode MAC address from SLAAC address** (-m)
  - Decode MAC addresses from non-privacy SLAAC addresses
- **Decode link local addresses** (-a)
  - Decode link local address to MAC, and MAC to link local
---

Because why not, I also forked this and made a webified version that is available with essentially the same functionality [here](https://tools.forwardingplane.net).
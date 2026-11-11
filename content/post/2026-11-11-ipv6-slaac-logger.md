---
title: "ipv6-slaac-logger - accountability for SLAAC addresses with RFC 9686"
date: 2026-11-11
author: Nick Buraglio
layout: post
draft: false
categories:
    - golang
    - ipv6
    - security
    - monitoring
tags:
    - golang
    - ipv6
    - slaac
    - dhcpv6
    - rfc9686
    - security
---

One of the most common objections I hear to SLAAC, and frankly one of the most legitimate ones, is accountability. "If the host picks its own address, how do I know who had `3fff:db8:10::5c1e:9aff:fe3b:21aa` last Tuesday at 21:00?" With DHCPv6 IA_NA you get a lease log - this is what everyone is used to with legacy IP, and why so many enterprises ask for DHCPv6 support. With SLAAC, and especially with temporary/privacy addresses rotating underneath you, you get... whatever you can scrape out of neighbor caches before they age out. We talked about exactly this visibility gap on [IPv6 Buzz 208](https://packetpushers.net/podcasts/ipv6-buzz/ipb208-ipv6-address-management-is-broken/), and it's a real blocker for a lot of security and compliance teams.

[RFC 9686](https://datatracker.ietf.org/doc/rfc9686/) (Registering Self-Generated IPv6 Addresses Using DHCPv6) is the standards-track answer: a host that builds its own address tells a DHCPv6 server about it with an `ADDR-REG-INFORM` message, and the server logs it - operators get an analog to what they had with legacy IP, for the most part. The problem is that the client side barely exists at this time. Kea has server support, Android rollout has been announced, systemd-networkd has an open PR, and macOS and Windows don't have it at all. Seeing a significant missing piece here, I built [ipv6-slaac-logger](https://github.com/buraglio/ipv6-slaac-logger) to close that gap now, instead of waiting for every OS vendor to catch up. Do I expect anyone to roll this out in production at scale? Probably not. However, it is a working implementation that they can point to and tell their vendors "we need that as a native feature, here is an example".

## What it does

The goal is simple to state: **for any IPv6 address seen during a time window, answer which DUID, MAC(s) and hostname held it, from when to when, and what evidence each claim rests on.** It's written in Go, pure Go with `CGO_ENABLED=0`, and ships as two binaries.

* **collector** - an RFC 9686 server, an option 148 responder, a passive ND/RA sniffer, a SQLite store, syslog forwarding, and a query CLI. Linux only for now. Pretty easily ported to windows if someone were so inclined or I get a few hours. 
* **agent** - a small user-space RFC 9686 client for **Linux, macOS, and Windows**. It finds the host's self-generated addresses (SLAAC, temporary, and static, ULA included) and registers each one with the collector.

So there are three ways an address ends up in the database:

1. **Native RFC 9686 clients** register with the collector exactly as they would with any RFC 9686 server.
2. **Hosts running the agent** register on behalf of an OS that can't do it yet.
3. **Everything else** (printers, IoT stuff that can actually do IPv6, the thermostat nobody admits to owning) gets picked up by the **sniffer** watching Neighbor Discovery traffic. These sightings carry MAC ↔ address only, no DUID, but that's still a lot more than nothing.

```
  Native RFC 9686 clients ─┐
  Agents (mac/win/linux) ──┼── multicast ff02::1:2:547 ──┐
                           ├── unicast collector:547 ────┼──> collector ──> SQLite (truth) ──> syslog/rsyslog
  Remote links ── relay ───┴── Relay-Forward ────────────┘        ^
  All hosts (incl. IoT) ── ND/RA on the wire ── SPAN/trunk ── sniffer
```

The collector accepts direct multicast, direct unicast, and relayed registrations, so it works on a single flat lab network or behind DHCPv6 relays on a campus. Full disclosure: relay needs tested. If you test and this is working, please do let me know. If it has problems, let me know that too. I'll get around to testing it eventually.

## Logs are the product

This is a forensic tool, so the output has to fit into what people already run. SQLite is the source of truth, with 400 days of retention by default, and every event is forwarded as JSON with an `@cee:` prefix so rsyslog's `mmjsonparse` can handle it, and from there your SIEM or whatever. A registration looks like this:

```json
{"ts":"2026-11-08T21:14:03.412Z","event":"reg.add","addr":"3fff:db8:10::5c1e:9aff:fe3b:21aa",
 "duid":"00:03:00:01:5c:1e:9a:3b:21:aa","duid_type":"LL","mac":"5c:1e:9a:3b:21:aa",
 "mac_src":"duid","origin":"agent","host":"lab-mbp","via":"multicast","link":"en0/3fff:db8:10::/64",
 "preferred_lft":14400,"valid_lft":86400,"xid":"a1b2c3"}
```

Events cover registrations (`reg.add`, `reg.change`, `reg.expire`, `reg.conflict`, `reg.reject`), sniffer sightings (`nd.new`, `nd.conflict`, `nd.expire`), and router advertisements (`ra.seen`, `ra.change`). That last pair turns out to be a nice side benefit: you get a log entry whenever a new router shows up on a link or an existing one flips its M/O flags or prefix set. That's useful for rogue RA detection in its own right.

Repeat sightings and refreshes only update `last_seen` in the database. They never generate syslog lines, so a busy link doesn't bury the events you actually care about, or as a mentor once taught me "never alarm on non-actionable stuff". I try to keep that ethos alive. 

Answering the "who had this address" question is one command:

```sh
slaac-logger-collector query -addr 3fff:db8:10::5 -at 2026-11-08T21:00:00Z
```

## The agent

Getting the agent going is pretty painless:

```sh
slaac-logger-agent list                       # show local addresses and which would be registered
slaac-logger-agent -config agent.toml install # install as a service
slaac-logger-agent start
```

It runs as a systemd unit with `DynamicUser=yes` and only `CAP_NET_BIND_SERVICE` on Linux, a launchd daemon on macOS, and a Windows Service as `LocalService`. It tries to reuse the OS's own DHCPv6 DUID (from the Windows registry, macOS's `DUID_IA.plist`, or dhclient's leases) so that its records line up with any existing DHCPv6 server logs. If it can't, it generates a DUID-LLT and persists it, so the identity survives restarts *and* MAC randomization. That last part matters a lot when every phone and laptop on the network is rotating its MAC.

A few deliberate choices worth calling out:

* **Temporary/privacy addresses are registered too.** They're the ones you most need a record of.
* **No de-registration.** This departs from the RFC on purpose. Once the OS removes an address it can't be used as a source, and de-registering at shutdown would falsely claim the host stopped using it. End of use is inferred from `last_seen` plus lifetime. 
* **The heartbeat defaults to 1 hour**, shorter than the RFC's lifetime-based refresh, to bound the uncertainty about when an address stopped being used.
* The agent identifies itself in Vendor Class (option 16) with enterprise number **67611**, the IANA PEN assigned to this project. That marker is advisory, since anyone can spoof a Vendor Class, and the logs record `origin` with that in mind.

## The sniffer

Give a collector interface the `sniff` role and it watches DAD, NS, NA, and RS traffic to learn MAC ↔ address pairs. A few things I learned building it that are worth passing along:

* **MLD snooping will hide most of what you want to see.** On an access port, most DAD and solicited-node traffic never reaches you. Use a SPAN/mirror port or a trunk.
* It reads 802.1Q tags the kernel strips into socket metadata (raw `AF_PACKET` with `PACKET_AUXDATA`), so VLANs are recorded correctly, plus one in-frame tag for QinQ (not fully tested).
* It's built to survive hostile links. Live sightings are capped (100k by default), event rates are token-bucketed, and a MAC claiming more than 32 addresses on a link is flagged as a probable proxy-ND router rather than flooding the logs. Conflicts, where an address moves to a new MAC, are logged as `nd.conflict` with the previous MAC attached.
* All of this is exported as counters in a periodic `stats` event, so you can tell "nothing happened" apart from "the sniffer can't see anything."

## Caveats

This is new, and I want to be upfront about the edges:

* The collector, including the sniffer, is **Linux only** for now. The agent is cross-platform.
* **Native clients only register after a DHCPv6 server hands them option 148.** If there's no other DHCPv6 server on the link, give the collector the `responder` role and **set the O flag in your RAs**. Don't run the responder on the same link as a Kea server that also answers registrations, or you'll get two servers answering.
* On Linux, the agent only reads dhclient's DUID. On systemd-networkd or NetworkManager hosts, set `duid` in the config if you need it to match.
* Windows can't tell temporary addresses apart from stable-privacy ones, so both are reported as `slaac`. Both are still registered.

```sh
CGO_ENABLED=0 go build -o bin/slaac-logger-collector ./cmd/collector
CGO_ENABLED=0 go build -o bin/slaac-logger-agent ./cmd/agent
```

There's a unit test suite, a Linux network-namespace end-to-end test, and a CI interop job that runs the agent against ISC Kea 3.0, so it isn't only tested against itself. As with some of my other recent projects, LLM tooling, soecificallt Claude was used during development to help me make my own code "suck less", and to aid in some of the more complex things I am still learning, and a human reviewed all of it - I want to learn as much as I can from "companion coding"; the README says so plainly.

## Why bother?

For me, the larger point is that "we can't track SLAAC addresses" has been a reason, or at least an excuse, to keep DHCPv6-only or IPv4-only policies around for far too long. RFC 9686 is the right long-term answer, and as native client support lands this tool should mostly fade into the background as a plain RFC 9686 collector. Until then, an agent plus a sniffer plus a sane log format gets you most of the way there today.

The code is at [github.com/buraglio/ipv6-slaac-logger](https://github.com/buraglio/ipv6-slaac-logger). Kick the tires, break it, and open issues. I'm especially interested in hearing from anyone testing native Android registrations or the systemd-networkd client.

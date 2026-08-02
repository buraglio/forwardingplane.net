---
title: piccolo-perf - a perfSONAR-lite for routers and SBCs
date: 2026-08-02
author: Nick Buraglio
layout: post
categories:
    - golang
    - ipv6
    - monitoring
    - perfsonar
tags:
    - golang
    - ipv6
    - monitoring
    - nix4neteng
    - perfsonar

---

I have a soft spot for [perfSONAR](https://www.perfsonar.net). It's the gold standard for research and education network performance measurement, and if you run a network that touches ESnet, Internet2, or any of the big R&E backbones, you've probably got a perfSONAR node (or ten) somewhere. The problem is that perfSONAR is heavy. It wants a full OS, a stack of services, and real resources. That's fine for a dedicated measurement box and that has served perfSonar well for 20 years, but it's a non-starter for a router, a Raspberry Pi at a remote site, or anything else you'd call "constrained."

That gap is exactly what [piccolo-perf](https://github.com/retecolo/piccolo-perf) is going after. It's a single static Go binary, no runtime dependencies, that gives you TWAMP-Light, TCP bandwidth, traceroute, MTU discovery, and DNS latency measurements, plus an agent mode that turns a fleet of these into a lightweight distributed mesh - InfluxDB and Prometheus included. Dual stack throughout, which matters to me more than it probably should. Honestly, I have been working on this for 15+ years, from trying to run OWAMP on a rpi1, to helping distribute mac minis for perfSonar tools into campuses, to even running lightweight versions of the toolkit on actual L3 switchines in the early days of virtualized NOSs'. This project has been a labor of love and with my recent endeavor to teach myself golang, I thought "why not give it a try with this"? The results are surprisingly useful. 

The measurement set:

* **twamp** - RTT, jitter, and packet loss via TWAMP-Light (RFC 5357 §5). No TCP control session, pure UDP test packets, so it's cheap to run and interoperable with other TWAMP-Light endpoints.
* **bw** - TCP throughput, either a native Go implementation or iperf3 if it's present on the box.
* **trace** - per-hop RTT and path topology via ICMP TTL/HopLimit probing, IPv4 and IPv6.
* **mtu** - effective path MTU via ICMP binary search (DF-bit on v4, Packet Too Big on v6). Useful for finding where a WireGuard tunnel or a double-encapsulated path quietly knocked your MTU down - very common in managed-service-paths.
* **dns** - A successor to [DNS test](https://dns.qosbox.com) resolver latency and success rate, independent of the system resolver.
* **agent** - runs all of the above on a schedule, reflects TWAMP for peers, and ships results to InfluxDB and/or exposes them as Prometheus metrics.

Anything that needs raw sockets (mtu, trace) degrades gracefully without `CAP_NET_RAW` rather than failing outright - it just reports `skipped=true`. That's a small detail, but it's the kind of thing that tells you someone has actually run this on a box they don't have root on. I'd be open to better ways to handle that.

Getting it running is a one-liner:

```sh
/bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/retecolo/piccolo-perf/main/install.sh)"
```

and a one-shot test looks like this:

```sh
piccolo-perf twamp -mode client -server 2001:db8::1
```

```
[TWAMP-Light-Client] Starting TWAMP-Light test to 2001:db8::1 (count=10 interval=1s timeout=5s padding=0)
[TWAMP-Light-Client] seq=1 RTT=0.823ms
...
[TWAMP-Light-Client] === TWAMP-Light Test Statistics ===
[TWAMP-Light-Client] Packets sent:     10
[TWAMP-Light-Client] Packets received: 10
[TWAMP-Light-Client] Packet loss:      0.0%
[TWAMP-Light-Client] RTT min/avg/max:  0.778 / 0.812 / 0.857 ms
[TWAMP-Light-Client] Mean jitter:      0.018 ms
```

The part I find more interesting than the one-shot CLI use is agent mode, and this harkens back to the inspiration for this peoject, perfSonar. Point a handful of hosts at a config server serving a JSON topology file, and each host stands up a TWAMP reflector, a bandwidth sink, and per-measurement schedulers, then pushes results upstream:

```
┌─────────────────────────────────────────┐
│            Each Probe Host              │
│  piccolo-perf agent                     │
│  ├── TWAMP-Light reflector (UDP)        │
│  ├── BwServer (TCP sink, port 5201)     │
│  ├── Per-measurement schedulers         │
│  ├── Config poller (HTTP, live-reload)  │
│  ├── InfluxDB writer                    │
│  ├── Prometheus /metrics                │
│  └── Local JSONL resilience store       │
└──────────┬──────────────────┬───────────┘
           │ pull config      │ push metrics
           ▼                  ▼
  ┌──────────────┐    ┌──────────────┐
  │ Config Server│    │   InfluxDB   │◀─── Grafana
  └──────────────┘    │  Prometheus  │
                       └──────────────┘
```

Topology can be full mesh (every host probes every other host) or hub-and-spoke, which is the more realistic shape for most of us - a handful of spokes reporting back to a hub instead of an N² mesh. There's also a local JSONL ring buffer for intermittently-connected edge devices, so a probe that loses its uplink keeps measuring and replays results once connectivity comes back instead of just dropping data on the floor.

## Where this actually fits

A few use cases jump out:

* **IPv6 test pods and lab networks.** If you listened to [IPB173](https://packetpushers.net/podcasts/ipv6-buzz/ipb173-the-ipv6-test-pod-project/) or any of the recent IPv6 Buzz episodes on lab builds, this is a natural fit for exactly that kind of environment - dual-stack RTT, jitter, and MTU measurement without standing up a perfSONAR node for every pod. Hey James, lets test this out =)
* **CPE and branch office monitoring.** Since it compiles to a static binary across amd64, arm64, arm, mips, ppc64le, and riscv64, it'll run on the kind of small router or SBC that lives at a remote site where you have no business installing a full measurement stack.
* **VPN and tunnel path MTU troubleshooting.** The mtu subcommand's binary search is a fast way to confirm whether a WireGuard or other tunnel is silently truncating your effective MTU, without reaching for tcpdump and doing the math by hand.
* **A perfSONAR-adjacent mesh on a budget.** Agent mode with hub-and-spoke topology and Grafana on top gets you a reasonable approximation of a perfSONAR mesh dashboard for a fraction of the deployment overhead, which is appealing if you want visibility into a network that doesn't justify (or fit) the full perfSONAR toolkit.

It's early days for the project, but the design choices - graceful degradation without root, IPv6 treated as a first-class citizen rather than an afterthought, and a resilience store for flaky links - suggest someone building this against real constraints rather than a whiteboard. Worth a look if smokeping and perfSONAR are two ends of a spectrum you've been missing the middle of.

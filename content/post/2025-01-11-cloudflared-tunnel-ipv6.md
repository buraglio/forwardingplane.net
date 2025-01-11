---
title: Mikrotik Winbox linux .desktop file
date: 2025-01-11
author: Nick Buraglio
layout: post
categories:
    - configuration
    - ipv6
tags:
    - linux
    - cloudflared
    - vpn
    - ipv6
---

Cloudflare offers a [powerful tunneling service](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) that allows for a host on a private network to expose a service but retain protection using cloudflare's powerful CDN tools. At the time of this post that service is a lagacy IP first service, but with one minor tweak it can operate with IPv6-only hosts. Meaning one can provision an IPv6-only host, but provide a dual stacked service. If that sounds powerful, that's because it is. This is especially useful for environments where they may be limited in their legacy IP allocations, mandated to keep a single IPv6 stack, or, if they just don't want to bother with legacy IP and potentially NAT to keep the network stack simple, secure, and clean.
The cloudflare tunneling can be found in your cloudflare account under ZeroTrust > Networks > Tunnels. 


Making this work is remarkably simple, but the how-to is buried in a [GitHub issue](https://github.com/cloudflare/cloudflared/issues/842).

This configuration tweak assumes the use of a Linux service and the cloudflared package. In order to enable IPv6 tunne;l connectivity, simply edit the cloudflared.service as such:

`sudo systemctl edit --full cloudflared.service` and edit the ExecStart to include `--edge-ip-version 6`

the final edit should look something like:

```
[Unit]
Description=cloudflared
After=network-online.target
Wants=network-online.target

[Service]
TimeoutStartSec=0
Type=notify
ExecStart=/usr/bin/cloudflared --edge-ip-version 6 --no-autoupdate tunnel run --token <redacted-tunnel-token>
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

Simply restart the service `systemctl restart cloudflared` and verify the tunnel is up the cloudflare dashboard and by checking the status:

```
systemctl status cloudflared
● cloudflared.service - cloudflared
     Loaded: loaded (/etc/systemd/system/cloudflared.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2025-01-11 12:31:42 CST; 2h 54min ago
   Main PID: 3656192 (cloudflared)
      Tasks: 11 (limit: 9250)
     Memory: 17.3M
        CPU: 24.316s
     CGroup: /system.slice/cloudflared.service
             └─3656192 /usr/bin/cloudflared --edge-ip-version 6 --no-autoupdate tunnel run --token <redacted-tunnel-token>
```
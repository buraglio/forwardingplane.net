---
id: 2589
title: 'PODCAST: MODEM.show, DHCP option 108'
date: '2023-07-14T14:12:43-05:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2589'
permalink: /2023/07/14/podcast-modem-show-dhcp-option-108/
autopostToMastodon-post-status:
    - 'off'
autopostToMastodonshare-lastSuccessfullTootURL:
    - 'https://dial.modem.show/@forwardingplane/110714025890153262'
Views:
    - '571'
    - '571'
image: /wp-content/uploads/2023/07/DHCP-Option-108.png
categories:
    - IPv6
    - 'Lab Time'
tags:
    - IPv6
    - Podcast
---

<!-- wp:paragraph -->
<p>Over the last year there has been a slow hum, quietly building around the notion of building what has been called an "IPv6-mostly" network. What does this term mean? How do we do it? Why bother? Well, let me attempt to answer those questions. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First, what is IPv6-mostly? Thankfully, it is pretty much what it sounds like - a network segment (i.e. a LAN segment) that is mostly IPv6, and only legacy IPv4 where it has to be. This is better described to in the RFC that defines the "how", <a href="https://datatracker.ietf.org/doc/html/rfc8925">RFC8925</a>: </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I<em>t would be beneficial for IPv6 deployment if operators could implement IPv6-mostly (or IPv4-on-demand) segments where IPv6-only hosts coexist with legacy dual-stack devices. </em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In practice, this works with IPv4-only devices just as well as dual-stack devices. I like to think of it as a network allowing a system to "operate at its highest level of network stack evolution". Because I had a bit of a time finding examples of how this is implemented in practice (the KEA docs are fantastic, but also very, very deep and comprehensive - a bit much to weed through when looking for a working example.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>{
        "Dhcp4":
                {
                "hooks-libraries": &#91;
                        {
                                "library": "/usr/lib/x86_64-linux-gnu/kea/hooks/libdhcp_stat_cmds.so"
                        },
                        {
                                "library": "/usr/lib/x86_64-linux-gnu/kea/hooks/libdhcp_lease_cmds.so"
                        }
                ],
                "interfaces-config": {
                    "interfaces": &#91; "eth0/10.9.9.5" ]
                },
                "control-socket": {
                     "socket-type": "unix",
                     "socket-name": "/tmp/kea4-ctrl-socket"
                },
                "renew-timer": 1000,
                "rebind-timer": 2000,
                "valid-lifetime": 86400,
                "expired-leases-processing": {
                        "reclaim-timer-wait-time": 10,
                        "flush-reclaimed-timer-wait-time": 25,
                        "hold-reclaimed-time": 3600,
                        "max-reclaim-leases": 100,
                        "max-reclaim-time": 250,
                        "unwarned-reclaim-cycles": 5
                },
                "lease-database": {
                     "type": "memfile",
      		     "persist": true,
      		     "name": "/var/lib/kea/dhcp4.leases"
                },

                "subnet4": &#91;
                  {
                        "id": 4,
                        "subnet": "10.209.4.0/25",
                        "pools": &#91;
                                { "pool": "10.9.4.100 - 10.9.4.120" }
                        ],
                        "interface": "eth0",
                        "option-data": &#91;
                                {
                                        "name": "domain-name-servers",
                                        "code": 6,
                                        "space": "dhcp4",
                                        "csv-format": true,
                                        "data": "10.9.9.126, 10.9.9.53, 10.9.9.2, 10.9.6.2"
                                },
                                {
                                        "name": "routers",
                                        "code": 3,
                                        "space": "dhcp4",
                                        "csv-format": true,
                                        "data": "10.9.4.1"
                                }
                        ]
                  }
                  {
                        "id": 6,

                        "subnet": "10.9.6.0/25",

                        "pools": &#91;
                                { "pool": "10.9.6.30 - 10.9.6.120" }
                        ],
                        "interface": "eth0",
                        "option-data": &#91;
                                {
                                        "name": "domain-name-servers",
                                        "code": 6,
                                        "space": "dhcp4",
                                        "csv-format": true,
                                        "data": "10.9.6.2, 10.9.9.126, 10.9.9.53, 10.9.9.2"
                                },
                                {
                                        "name": "routers",
                                        "code": 3,
                                        "space": "dhcp4",
                                        "csv-format": true,
                                        "data": "10.9.6.1"
                                }
                        ]
                  },

                ],
        "loggers": &#91;
                {
                "name": "kea-dhcp4",
                "output_options": &#91;
                        {
                        "output": "/var/log/kea/dhcp4.log"
                        }
                ],
                "severity": "DEBUG",
                "debuglevel": 0
                }
          ]
        }
}
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This KEA configuration assumed that that dhcp is centralized and being relayed via a router relay / ip helper. As mentioned in this <a href="https://blog.apnic.net/2022/11/21/deploying-ipv6-mostly-access-networks/">APNIC blog</a>, option 108 is still a work in progress. It's still got <a href="https://issuetracker.google.com/issues/291235541">some issues with certain clients</a>, and is completely absent in all versions os Microsoft windows. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We have recently recorded <a href="https://www.modem.show/post/s03e03/">an episode of MODEM</a> on my recent experience building and running an IPv6-mostly network, and there is <a href="https://packetpushers.net/podcast/ipv6-buzz-110-the-peculiar-power-of-dhcpv6-option-108/">a great IPv6 Buzz Podcast</a> on the same topic that is very good. You can take a listen here, or in your favorite podcatcher, or streamed below. </p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<iframe src="https://podcasters.spotify.com/pod/show/modulate-demodulate/embed/episodes/What-the-heck-is-DHCP-option-108-and-how-do-I-use-it-e26r773" height="150px" width="400px" frameborder="0" scrolling="no"></iframe>
<!-- /wp:html -->
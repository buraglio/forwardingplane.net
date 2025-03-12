---
title: DNS over HTTPS and DNS over TLS Bind9 and Unbound Configuration examples
date: 2024-12-21
author: Nick Buraglio
layout: page
categories:
    - configuration
tags:
    - dns
    - configuration
---

This contains the syntax for running a DNS over HTTPS and a DNS over DOT for Bind9 and Unbound. It does not contain the processes for installing the software or obtaining the SSL certificate. That information can be found elsewhere. These were tested on Ubuntu 22.04 running the latest versions of bind9 available in the repo, but for Unbound the DoH only works with a compiled build (1.22) since the Ubuntu repo version is very, very, *very* old. 


## Bind9 
Within `/etc/bind/named.conf.options` add the following. 

```
tls local-tls {
   key-file "/etc/letsencrypt/live/ns1.example.org/privkey.pem"; # Your SSL certificates
   cert-file "/etc/letsencrypt/live/ns1.example.org/fullchain.pem";
};

options {
   directory "/var/cache/bind";
   recursion yes;
   allow-recursion { 127.0.0.1; ::1; 100.64.0.0/10; 3fff::/20;}; # client networks that will query 
   listen-on { any; }; 
   listen-on-v6 { any; };  
   dnssec-validation auto;
   listen-on port 443 tls local-tls http default {any;};
   listen-on-v6 port 443 tls local-tls http default {any;};
   listen-on port 853 tls local-tls {any;};
   listen-on-v6 port 853 tls local-tls {any;};
};
```

Unbound

For unbound add the following to `/etc/unbound/unbound.conf`

```
# The following line includes additional configuration files from the
# /etc/unbound/unbound.conf.d directory.
include-toplevel: "/etc/unbound/unbound.conf.d/*.conf"

server:
      # the working directory.
      directory: "/etc/unbound"

      # run as the unbound user
      username: unbound

      verbosity: 2      # uncomment and increase to get more logging.

      interface: 0.0.0.0@853
      interface: 0.0.0.0@53
      interface: ::0@853
      interface: ::0@53
      interface: 0.0.0.0@443
      interface: ::0@443
      prefetch: yes

      access-control: 100.64.0.0/10 allow # all RFC 6598, change to your legacy address block
      access-control: 127.0.0.1/24 allow # legacy ip localhost
      access-control: ::1/0 allow # ipv6 localhost
      access-control: 3fff::/20 allow  # Replace with your IPv6 block
      access-control: fc00::/7 allow # ULA, remove if not in use, refine if in use

      hide-identity: yes
      hide-version: yes
      do-ip4: yes
      do-udp: yes
      do-tcp: yes
      do-ip6: yes
      prefer-ip6: yes
      harden-glue: yes
      harden-dnssec-stripped: yes
      # DoH and DoT stuff
      tls-service-key: "/etc/letsencrypt/live/ns1.example.org/privkey.pem"
      tls-service-pem: "/etc/letsencrypt/live/ns1.example.org/fullchain.pem"
      tls-port: 853
      https-port: 443

# enable logging

     logfile: /var/log/unbound.log
     verbosity: 1
     log-queries: no

remote-control:
      # Enable remote control with unbound-control(8) here.
      control-enable: no

      # what interfaces are listened to for remote control.
      # give 0.0.0.0 and ::0 to listen to all interfaces.
      # set to an absolute path to use a unix local name pipe, certificates
      # are not used for that, so key and cert files need not be present.
      # control-interface: 127.0.0.1
      control-interface: ::1

      # port number for remote control operations.
      control-port: 8953
      ```
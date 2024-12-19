---
title: Testing DNS
date: 2024-12-18
author: Nick Buraglio
layout: page
---

DNS is an absolutely critical part of using any modern data network. However, in the past decade, the complexity of DNS has exploded, and not just in function. Some applications, and especially browsers, have opted to reference their own DNS resolvers that may be outside of your network, counter to policy, or simply unknown to any given user.
In addition to added complexity, browsers have begun to support, and sometimes use by default, DNBS over HTTPS. This may circumvent policy, and while obfuscating DNS queries to a different resolver, it also causes DNS to pass unnoticed to some users without the benefit of enriched data from netflow or packet inspectors with intelligence feeds. These complexities can be frustrating to understand and painful to troubleshoot. So, here are some commands to help ease the burden of some of the looking around. All commands are testing on a unix based system. 

## Redirecting to HTTPS? 

Is your traffic being automatically redirected to https? That doesn't mean that the web server is telling it to. It may be an HTTPS record. You can check for one by doing a dig against any resolver you have access to with the following command: 

```
dig @nameserver www.cloudflare.com -t https
```

```
buraglio@rdns4 ~ % dig @dot.cmi.mpls.rsvp www.cloudflare.com -t https

; <<>> DiG 9.16.50-Debian <<>> @dot.cmi.mpls.rsvp www.cloudflare.com -t https
; (2 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23462
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;www.cloudflare.com.		IN	HTTPS

;; ANSWER SECTION:
www.cloudflare.com.	300	IN	HTTPS	1 . alpn="h3,h2" ipv4hint=104.16.123.96,104.16.124.96 ipv6hint=2606:4700::6810:7b60,2606:4700::6810:7c60

;; Query time: 60 msec
;; SERVER: 203.23.160.12#53(203.23.160.12)
;; WHEN: Wed Dec 18 21:21:02 CST 2024
;; MSG SIZE  rcvd: 120
```

If that output is too complex, just add `+short`

```
buraglio@rdns4 ~ % dig @dot.cmi.mpls.rsvp www.cloudflare.com -t https +short
1 . alpn="h3,h2" ipv4hint=104.16.123.96,104.16.124.96 ipv6hint=2606:4700::6810:7b60,2606:4700::6810:7c60
```

## Testing DoH

```bash
# json
curl -H 'accept: application/dns-json' 'https://doh.cmi.mpls.rsvp/dns-query?name=www.forwardingplane.net.&type=AAAA' | jq .
# dns wireformat
curl -H 'accept: application/dns-message' 'https://dns.google/dns-query?dns=q80BAAABAAAAAAAAA3d3dwdleGFtcGxlA2NvbQAAAQAB'  | hexdump -c
```
## Testing DoT
This requires installation of a package to perform. The dns resolver package [knot](https://www.knot-dns.cz/) provides a tool called kdig, which can test against DoT. The knot package is available for at least linux and OSX within package managers. 

`kdig -d @dot.chi.mpls.rsvp +tls-ca +tls-host=dot.chi.mpls.rsvp buraglio.com -t aaaa`

```
└─[$] kdig -d @dot.chi.mpls.rsvp +tls-ca +tls-host=dot.chi.mpls.rsvp buraglio.com -t aaaa                                                                                                                  [21:29:42]
;; DEBUG: Querying for owner(buraglio.com.), class(1), type(28), server(dot.chi.mpls.rsvp), port(853), protocol(TCP)
;; DEBUG: TLS, imported 152 system certificates
;; DEBUG: TLS, received certificate hierarchy:
;; DEBUG:  #1, CN=doh.chi.mpls.rsvp
;; DEBUG:      SHA-256 PIN: fq+yQslBNefS15sp4TN+ZKVf5JJ8yhC3KLwtajv4jAM=
;; DEBUG:  #2, C=US,O=Let's Encrypt,CN=R10
;; DEBUG:      SHA-256 PIN: K7rZOrXHknnsEhUH8nLL4MZkejquUuIvOIr6tCa0rbo=
;; DEBUG: TLS, skipping certificate PIN check
;; DEBUG: TLS, The certificate is trusted.
;; TLS session (TLS1.3)-(ECDHE-X25519)-(RSA-PSS-RSAE-SHA256)-(AES-256-GCM)
;; ->>HEADER<<- opcode: QUERY; status: NOERROR; id: 9985
;; Flags: qr rd ra ad; QUERY: 1; ANSWER: 2; AUTHORITY: 0; ADDITIONAL: 1

;; EDNS PSEUDOSECTION:
;; Version: 0; flags: ; UDP size: 1232 B; ext-rcode: NOERROR
;; PADDING: 367 B

;; QUESTION SECTION:
;; buraglio.com.       		IN	AAAA

;; ANSWER SECTION:
buraglio.com.       	300	IN	AAAA	2600:1f18:16e:df02::65
buraglio.com.       	300	IN	AAAA	2600:1f18:16e:df01::65

;; Received 468 B
;; Time 2024-12-18 21:29:49 CST
;; From 2001:19f0:5c01:ca2::53@853(TLS) in 69.6 ms
```

and the `+short` version

```└─[$] kdig -d @dot.chi.mpls.rsvp +tls-ca +tls-host=dot.chi.mpls.rsvp buraglio.com -t aaaa +short                                                                                                           [21:29:49]
;; DEBUG: Querying for owner(buraglio.com.), class(1), type(28), server(dot.chi.mpls.rsvp), port(853), protocol(TCP)
;; DEBUG: TLS, imported 152 system certificates
;; DEBUG: TLS, received certificate hierarchy:
;; DEBUG:  #1, CN=doh.chi.mpls.rsvp
;; DEBUG:      SHA-256 PIN: fq+yQslBNefS15sp4TN+ZKVf5JJ8yhC3KLwtajv4jAM=
;; DEBUG:  #2, C=US,O=Let's Encrypt,CN=R10
;; DEBUG:      SHA-256 PIN: K7rZOrXHknnsEhUH8nLL4MZkejquUuIvOIr6tCa0rbo=
;; DEBUG: TLS, skipping certificate PIN check
;; DEBUG: TLS, The certificate is trusted.
2600:1f18:16e:df02::65
2600:1f18:16e:df01::65
```

## Testing UDP DNS (Default)

## Testing TCP DNS

How does the browser know to look for DoH?!?! More DNS! 
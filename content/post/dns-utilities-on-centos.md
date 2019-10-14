---
title: 'DNS utilities on CentOS'
date: Fri, 04 Jan 2013 10:13:28 +0000
draft: false
tags: [Lab Time, UNIX]
---

It's always annoying to me, being a convert from \*BSD to Linux, that tools lke dig and host aren't in the minimal base install.  I realise that this makes me somewhat of a hypocrite, as I prefer an additive system rather than a subtractive base OS.  Nevertheless, I'm continually surprised that "host" isn't available after installing a minimal CentOS system without adding an additional package.  So, since I always forget, here is a quick blog post to remind me and any other converts how to install those tools:```
 yum -y install bind-utils
```That's it.  Tragedy avoided.  Now I can make sure my AAAA records are working.```
\[buraglio@cupcake httpd\]# dig www.forwardingplane.net -t AAAA
; <<>> DiG 9.8.2rc1-RedHat-9.8.2-0.10.rc1.el6\_3.6 <<>> www.forwardingplane.net -t AAAA
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47725
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.forwardingplane.net. IN AAAA
;; ANSWER SECTION:
www.forwardingplane.net. 86364 IN AAAA 2607:f2f8:4980::2
;; Query time: 1 msec
;; SERVER: 10.209.209.1#53(10.209.209.1)
;; WHEN: Thu Jan 3 22:49:35 2013
;; MSG SIZE rcvd: 69
```
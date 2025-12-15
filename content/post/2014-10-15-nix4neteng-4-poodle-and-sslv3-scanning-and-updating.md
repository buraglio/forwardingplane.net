---
id: 1100
title: 'NIX4Neteng #4: POODLE and SSLv3, scanning and updating'
date: '2014-10-15T11:36:54-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1100'
permalink: /2014/10/15/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/
themeblvd_title:
    - 'NIX4Neteng #4: POODLE, SSLv3, scanning and updating '
themeblvd_keywords:
    - 'NIX4Neteng, POODLE, SSLv3, nmap scanning, apache updating, burglio, sdn, security, openflow, whitehat, unix, linux, centos, debian, ubuntu, poodle scanning, poodle exploit, sslv3 poodle, sslv3 scanning,patching poodle, patching sslv3, nmap poodle, nmap sslv3'
themeblvd_description:
    - 'NIX4Neteng #4: POODLE vulnerability for SSLv3, scanning and enumerating your network and patching your services. '
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3120196518'
Views:
    - '100'
categories:
    - How-To
    - NIX4NetEng
    - Security
    - UNIX
---

With the recent release of the [POODLE SSLv3 vulnerability](https://www.openssl.org/~bodo/ssl-poodle.pdf), folks are scrambling around trying to figure out what runs what and where.  Running a handful of things that do SSL, I was obligated, both personally and professionally, to figure out an easy way to drill down and figure out what does what and then fix the vulnerable services.  When there are a lot of devices, this can seem like a daunting task, and it is if you're trying to do it manually.  This is where [NMAP](http://nmap.org/) comes into play.  NMAP is an extremely powerful tool for scanning and enumerating your own network, not just a tool for the script kiddies to port scan.
Since there is no SSL patch at the time of this writing, and since SSLv3 is old and depricated, it is a good idea to see what services support it and then squish them in favor of TLS 1+.  Thankfully, smarter folks than myself have done most of the legwork for accomplishing this task and written most of it down [here](http://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html). NMAP has a wealth of cool scripts and bolt ons that extend it in amazing ways.  To accomplish our tasks we'll ned to do a few things.
Install nmap. I ran into issues with the [nselibs](http://nmap.org/book/nse-library.html) being incomplete, so I grabbed the source and built it that way as opposed to using yum.

```
git clone git@github.com:nmap/nmap.git
```

We then need to build it from source which requires the dev tools:

```
sudo yum -y groupinstall 'Development Tools'
cd nmap
./configure
sudo make
```

and alternatively

```
sudo make install
```

I like to just run it from my directory since there are path considerations.

```
(~/nmap) v-chimera $ ./nmap --script ssl-enum-ciphers -p 443 10.14.14.0/27
Starting Nmap 6.46 ( http://nmap.org ) at 2014-10-15 12:21 CDT
Nmap scan report for gw.test (10.14.14.1)
Host is up (0.0028s latency).
PORT STATE SERVICE
443/tcp closed https
Nmap scan report for ssldevice.test (10.14.14.2)
Host is up (0.0042s latency).
PORT STATE SERVICE
443/tcp open https
| ssl-enum-ciphers:
| SSLv3:
| ciphers:
| TLS_RSA_WITH_RC4_128_MD5 - strong
| TLS_RSA_WITH_RC4_128_SHA - strong
| compressors:
| NULL
| TLSv1.0:
| ciphers:
| TLS_RSA_WITH_RC4_128_MD5 - strong
| TLS_RSA_WITH_RC4_128_SHA - strong
| compressors:
| NULL
|_ least strength: strong
Nmap scan report for nossl.test (10.14.14.3)
Host is up (0.00049s latency).
PORT STATE SERVICE
443/tcp closed https
```

From here we can see that there is a host that needs to be updated. There are a wealth of docs out there for changing out the supported version. Most of my stuff is apache so I used [this guide](https://zmap.io/sslv3/). For embedded devices, the best option is to filter access [which you should probably be doing anyway] until there is a patched firmware version.
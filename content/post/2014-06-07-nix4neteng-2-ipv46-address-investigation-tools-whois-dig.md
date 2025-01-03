---
id: 1018
title: 'NIX4NetEng #2 IPv4/6 address investigation tools &#8211; whois + dig'
date: '2014-06-07T13:54:41-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1018'
permalink: /2014/06/07/nix4neteng-2-ipv46-address-investigation-tools-whois-dig/
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'investigating IPv4/6 address investigation tools - whois + dig'
themeblvd_keywords:
    - 'NIX4Neteng, buraglio, SDN, UNIX, Networking, SDN, buraglio, nick buraglio, whois, dig, howto, networking howto, unix howto, dig howto, whois howto, OpenFlow, Cisco, Juniper, Brocade, devops'
themeblvd_description:
    - 'Utilizing unix tools has long been a critical part of network engineering. This editin of NIX4NetEng explores the dig and whois tools. '
dsq_thread_id:
    - '2745145103'
Views:
    - '251'
categories:
    - NIX4NetEng
    - Routing
    - Security
    - UNIX
---

I don't care what your vendor alignment of choice is, Cisco, Juniper, Brocade, Alcatel....it doesn't matter. At one point or another you're going to need to bird dog an address to see where it's coming from, who owns it, what it's DNS name is or what path you're taking to get to it.  We've already talked about <a title="BGP tools; troubleshooting and monitoring external routing in a nutshell" href="http://www.forwardingplane.net/2014/03/bgp-tools-troubleshooting-and-monitoring-external-routing-in-a-nutshell/" target="_blank" rel="noopener noreferrer">BGP tools</a>, they're a great choice for checking routes across the internet. Hunting down addresses is an interesting one, though, as address management and lookups  can bleed into other aspects of networking like path selection, latency, jitter and many other things.  I'm going to touch on a few things and give generalizations on a few others.  First, querying where things originate and who has ownership is infinitely useful, especially if your job description has "security" anywhere in it, written or implied.  I like to use a range of services, all of which are from the CLI (for speed and scriptability).  My go-to tools for this are the venerable <a href="http://en.wikipedia.org/wiki/Whois" target="_blank" rel="noopener noreferrer">whois</a> and dig tools.
Lets say I want to check on the address 192.80.96.88.
First, lets figure out if it's got a name.  dig is your friend here.
<pre>(~) jumphost $ dig -x 192.80.96.88
; &lt;&lt;&gt;&gt; DiG 9.8.3-P1 &lt;&lt;&gt;&gt; -x 192.80.96.88
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 29443
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;88.96.80.192.in-addr.arpa. IN PTR
;; ANSWER SECTION:
88.96.80.192.in-addr.arpa. 7145 IN PTR local.forwardingplane.net.
;; Query time: 2 msec
;; SERVER: 10.209.209.1#53(10.209.209.1)
;; WHEN: Sat May 31 11:43:18 2014
;; MSG SIZE rcvd: 82
</pre>
Dig is an incredibly powerful DNS tool. I'd recommend learning it as well as you possibly can. <a href="http://linux.die.net/man/1/dig" target="_blank" rel="noopener noreferrer"><em>man dig</em></a> on any good unix box should give you a good start,<a href="http://www.thegeekstuff.com/2012/02/dig-command-examples/" target="_blank" rel="noopener noreferrer"> this site</a> has some good examples too, I can't even scratch the surface of how useful DNS tools are, probably a great subject for another NIX4NetEng.  Here we see that the address has reverse DNS (PTR record) of local.forwardingplane.net.  We can poke a bit more at this using DNS, too.
<pre>(~) jumphost $ dig -t ANY local.forwardingplane.net +noall +answer
; &lt;&lt;&gt;&gt; DiG 9.8.3-P1 &lt;&lt;&gt;&gt; -t ANY local.forwardingplane.net +noall +answer
;; global options: +cmd
local.forwardingplane.net. 221 IN AAAA 2607:dd00:8000:18::88
local.forwardingplane.net. 221 IN A 192.80.96.88</pre>
Well, we can see here we have a dual stacked host.  We'll look at that more later.
Let's see who owns this address space. Whois is the way to go here.  I always start with querying ARIN and go from there.
&nbsp;
<pre>(~) jumphost $ whois -h whois.arin.net 192.80.96.88
#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/whois_tou.html
#
#
# Query terms are ambiguous.  The query is assumed to be:
#     "n 192.80.96.88"
#
# Use "?" to get help.
#
#
# The following results may also be obtained via:
# http://whois.arin.net/rest/nets;q=192.80.96.88?showDetails=true&amp;showARIN=false&amp;ext=netref2
#
NetRange:       192.80.96.0 - 192.80.111.255
CIDR:           192.80.96.0/20
OriginAS:       AS10932
NetName:        UC2B-1
NetHandle:      NET-192-80-96-0-1
Parent:         NET-192-0-0-0-0
NetType:        Direct Allocation
RegDate:        2013-02-27
Updated:        2013-02-27
Ref:            http://whois.arin.net/rest/net/NET-192-80-96-0-1
OrgName:        UC2B
OrgId:          CCLAUBBC
Address:        102 North Neil Street
City:           Champaign
StateProv:      IL
PostalCode:     61820
Country:        US
RegDate:        2012-02-28
Updated:        2014-02-19
Ref:            http://whois.arin.net/rest/org/CCLAUBBC
OrgAbuseHandle: UCBTE-ARIN
OrgAbuseName:   uc2b-tech
OrgAbusePhone:  +1-217-265-4226
OrgAbuseEmail:  uc2b-tech@uc2b.net
OrgAbuseRef:    http://whois.arin.net/rest/poc/UCBTE-ARIN
OrgNOCHandle: UCBTE-ARIN
OrgNOCName:   uc2b-tech
OrgNOCPhone:  +1-217-265-4226
OrgNOCEmail:  uc2b-tech@uc2b.net
OrgNOCRef:    http://whois.arin.net/rest/poc/UCBTE-ARIN
OrgTechHandle: UCBTE-ARIN
OrgTechName:   uc2b-tech
OrgTechPhone:  +1-217-265-4226
OrgTechEmail:  uc2b-tech@uc2b.net
OrgTechRef:    http://whois.arin.net/rest/poc/UCBTE-ARIN
#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/whois_tou.html
#</pre>
The first 7 lines of this are the most important.
Here we can see that the address space is owned by an entity called <a href="http://www.uc2b.net" target="_blank" rel="noopener noreferrer">UC2B</a>, it is part of a /20 that the origin ASN is 10932 and that it is a direct allocation (as opposed to assigned space from an upstream provider).
<pre>NetRange:       192.80.96.0 - 192.80.111.255
CIDR:           192.80.96.0/20
OriginAS:       AS10932
NetName:        UC2B-1
NetHandle:      NET-192-80-96-0-1
Parent:         NET-192-0-0-0-0
NetType:        Direct Allocation</pre>
I could tell you some horror stories about getting this address space assigned. It took me 7 months to get that allocation from ARIN.......but I digress.  From here we can query the ASN, also using whois, again, the first few lines are generally the most useful.
<pre>(~) jumphost $ whois -h whois.arin.net 10932
ASNumber: 10932
ASName: UC2B
ASHandle: AS10932
RegDate: 2012-06-28
Updated: 2012-06-28
Ref: http://whois.arin.net/rest/asn/AS10932</pre>
We can use this information to track down responsible parties, addresses, etc.  It's a great resource for knowing both technical and non-technical details about address space.
<a href="http://www.team-cymru.org/Services/ip-to-asn.html#whois" target="_blank" rel="noopener noreferrer">Team Cymru has an extremely powerful whois service</a> that allows for significantly more flexibility including time and date.
<pre>(~) jumphost $ whois -h whois.cymru.com " -v 192.80.96.88"
AS      | IP               | BGP Prefix          | CC | Registry | Allocated  | AS Name
10932   | 192.80.96.88     | 192.80.96.0/20      | US | arin     | 2013-02-27 | UC2B - UC2B,US</pre>
As you can imagine, this can be a robust way to track changes and re-allocations of ASNs and address blocks, especially with the dwindling amounts of IPv4 and the re-assignment of ASNs.  One can see when ownership has changed and verify the correct origin of address blocks.  Great for validation and correlation.
These services also work for IPv6. We can see if the V6 space is coming from the same ASN or if it's a different entity (like a <a href="http://www.tunnelbroker.net" target="_blank" rel="noopener noreferrer">tunnel</a> or a totally different provider).
<pre>[buraglio@local ~]$ whois -h whois.cymru.com " -v 2607:dd00:8000:18::88"
[Querying whois.cymru.com]
[whois.cymru.com]
AS      | IP                                       | BGP Prefix          | CC | Registry | Allocated  | AS Name
10932   | 2607:dd00:8000:18::88                    | 2607:dd00::/32      | US | arin     | 2012-07-23 | UC2B - UC2B,US</pre>
&nbsp;
<p style="text-align: left;">This is really just the tip of the iceberg in this kind of toolset.  There are <em>countless </em>scripts, binaries and  shell hacks to do no end of interesting and useful things and gather information.  Have some other, better uses or tools?  Post them in the comments!</p>
<p style="text-align: center;"></p>
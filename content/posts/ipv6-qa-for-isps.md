---
title: 'IPv6 Q&A for ISPs'
date: Sat, 15 Dec 2018 01:21:09 +0000
draft: false
tags: [IPv6, IPv6, Strategy Series]
---

As a follow on to my post on [why small to medium ISPs should deploy IPv6](https://www.forwardingplane.net/2018/09/as-a-small-to-medium-isp-why-you-should-deploy-ipv6/) and the associated [APNIC blog post,](https://blog.apnic.net/2018/12/13/three-reasons-why-ipv6-is-worth-the-effort/) I have begun to compile a list of commonly asked questions IPv6 and their answers in relation to how a small to medium sized ISP can (and should) deploy IPv6. Expect this list to change and grow over time. 

\------  
**Q: Is there DHCP in IPv6? **  
\------

A:  There are [multiple DHCPv6 implementations](https://en.wikipedia.org/wiki/DHCPv6), the one I like to use is isc-dhcpd as it tends to have the best standard support, is incredibly feature rich and well documented and is very scalable, but there are multiple options.   
\-------  
**Q: How does one know what IP address the CPE has?**  
\------  
A: DUID (DHCP Unique Identifier), PPPoE, etc. There are several ways.   
\-------  
**Q: How does one perform traffic shaping for the entire /64 (or /48, or other nibble boundary block) assigned to the customer?**  
\------  
A: Don’t shape on L3, it doesn’t scale. Shape on L2 at the CPE or use PPPoE.   
\------  
**Q) Can a dynamic CPE environment where devices can pull addresses with minimal input and work from the provider still work?**  
\------  
A: Yes, DHCPv6 and [DHCPv6-PD](https://en.wikipedia.org/wiki/Prefix_delegation) handle these functions. There are well traveled and well vetted how-to’s for this. It is how the large incumbent providers work, regardless of delivery last mile (DSL, DOCSIS, Fixed wireless, etc.) 

\-------  
**Q: How does the host configure a host address? **  
\-------

A: Most devices will use what is called SLAAC. Addresses are auto-generated based on a MAC. A given host will have multiple IPv6 addresses and this is normal. There will also be the following on a HOST:  
A link local address on every interface (starts with fe80: and is used for any communication on the same L2 segment)  
A privacy address that rotates which much of the traffic will be worked from  
An EUI-64 address (the auto configured address)  
Potentially, but only when configured:  
A DHCPv6 assigned address.   
A Static Address

  
On the ISP side, you’ll see any or all of the following:  
A link local address (starts with fe80:)  
An EUI-64 address  
A static address  
A prefix delegated prefix

———  
Other commonly questions and advice

  
Come up with a reasonable IPv6 address plan before you start - work through it as you can. Start with your backbone  
You will no longer memorize addresses (which you should not do anyway), instead, do two things:

Think of all prefixes like you would consider a unique IPv4 address 4.2.2.2/32 ==2001:db8:44:22::/64  
IPv6 addresses are written with the CIDR prefix (see above)

Use DNS for everything you can - an IPAM like NetBox is your friend  
It’s ok if your customers prefix delegation does not have reverse DNS  
It’s ok to publicly address your infrastructure with IPv6. Use a single /48 dedicated for all infrastructure and then create an ACL at the network border to limit access  
Public addresses for your customers are ok.   
There is no NAT as in the IPv4 world, and there should not be NAT for IPv6. Period.   
Yes, you want to dual-stack. It’s ok to have RFC1918 space plus public IPv6. In fact, that’s the most prevalent model (look at your cell phone)  
You will have devices that won’t do IPv6. That’s expected.   
Yes, you can do IPv6 only, but it’s significantly harder to manage than a standard dual stack network.
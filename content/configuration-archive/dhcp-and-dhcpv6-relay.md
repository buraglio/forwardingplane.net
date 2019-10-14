---
id: 1640
title: ISC dhcp and dhcpv6 relay
date: 2019-03-16T10:00:52-06:00
author: Nick Buraglio
excerpt: When deploying dual stack, dhcpv6 is a crucial piece of the puzzle. ISC DHCPd provides a robust and stable server for this endeavor.
layout: page
guid: https://www.forwardingplane.net/?page_id=1640
---
When deploying dual stack, dhcpv6 is a crucial piece of the puzzle.  I personally prefer to run the dhcp process on a linux system and relay it for both v4 and v6. 

Assuming you are installing isc-dhcpd, the following configurations can be used to delegate host addresses for both IPv4 and IPv6

 

<pre>#<br /># Sample configuration file for ISC dhcpd for Debian / Ubuntu<br /># Examples provided without support by buraglio@forwardingplane.net<br /># Use at your own risk<br /># https://www.forwardingplane.net<br />#<br /># Attention: If /etc/ltsp/dhcpd.conf exists, that will be used as<br /># configuration file instead of this file.<br />#<br />#<br /><br /># The ddns-updates-style parameter controls whether or not the server will<br /># attempt to do a DNS update when a lease is confirmed. We default to the<br /># behavior of the version 2 packages ('none', since DHCP v2 didn't<br /># have support for DDNS.)<br />ddns-update-style none;<br /><br /><br />default-lease-time 259200;<br />max-lease-time 345600;<br /><br /># If this DHCP server is the official DHCP server for the local<br /># network, the authoritative directive should be uncommented.<br />authoritative;<br /><br /># Use this to send dhcp log messages to a different log file (you also<br /># have to hack syslog.conf to complete the redirection).<br />log-facility local7;<br /><br /># No service will be given on this subnet, but declaring it helps the <br /># DHCP server to understand the network topology. Errors will occur if not set, <br /># but functionality will remain intact<br /><br />#subnet 10.152.187.0 netmask 255.255.255.0 {<br />#}<br /><br /># Primary LAN Scope<br /><br />subnet 10.254.209.0 netmask 255.255.255.192 {<br />range 10.254.209.30 10.254.209.57;<br />option routers 10.254.209.1;<br />#option domain-name-servers resolver.anycast.my-isp.net, resolver2.dc1.my-isp.net;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />#option domain-name-servers 10.254.209.14;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># LAN scope 1<br />subnet 10.254.3.0 netmask 255.255.255.224 {<br />range 10.254.3.10 10.254.3.25;<br />option routers 10.254.3.1;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># POP scope 1<br />subnet 10.254.5.0 netmask 255.255.255.224 {<br />range 10.254.5.10 10.254.5.25;<br />option routers 10.254.5.1;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># POP Scope 2<br />subnet 10.254.6.0 netmask 255.255.255.224 {<br />range 10.254.6.5 10.254.6.27;<br />option routers 10.254.6.1;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># POP Scope 3<br />subnet 10.254.7.0 netmask 255.255.255.224 {<br />range 10.254.7.10 10.254.7.25;<br />option routers 10.254.7.1;<br />#option domain-name-servers resolver1.opendns.com, resolver1.ipv6-sandbox.opendns.com;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># POP Scope 4<br />subnet 10.254.4.0 netmask 255.255.255.224 {<br />range 10.254.4.10 10.254.4.25;<br />option routers 10.254.4.1;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># POP Scope 5<br />subnet 10.254.8.0 netmask 255.255.255.224 {<br />range 10.254.8.3 10.254.8.30;<br />option routers 10.254.8.1;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># POP Scope 6<br />subnet 10.254.9.0 netmask 255.255.255.224 {<br />range 10.254.9.10 10.254.9.25;<br />option routers 10.254.9.1;<br />option domain-name-servers resolver.anycast.my-isp.net;<br />option domain-name "dhcp.my-isp.net";<br />}<br /><br /># Static IPv4 addresses<br /><br />host business-customer1 {<br />hardware ethernet ff:ff:ff:f3:3d:9f;<br />fixed-address 10.254.4.9;<br />}<br /><br />host business-customer2 {<br />hardware ethernet ff:ff:ff:f3:3d:90;<br />fixed-address 10.254.4.11;<br />}<br /><br />host business-customer3 {<br />hardware ethernet ff:ff:ff:f3:3d:9a;<br />fixed-address 10.254.209.5;<br />}<br /><br />host wap1 {<br />hardware ethernet ff:ff:ff:40:d6:b0;<br />fixed-address 10.254.209.4;<br />}<br /><br />host wap2 {<br />hardware ethernet ff:ff:ff:46:76:DC;<br />fixed-address 10.254.209.7;<br />}<br /><br />host wap3 {<br />hardware ethernet ff:ff:ff:1d:d1:6a;<br />fixed-address 10.254.209.3;<br />}<br /><br /><br /></pre>

 

For IPv6, this configuration will provide host addresses to any devices requesting them

&nbsp;

<pre><br />#<br /># Sample configuration file for ISC dhcpd for Debian / Ubuntu<br /># Examples provided without support by buraglio@forwardingplane.net<br /># Use at your own risk<br /># https://www.forwardingplane.net<br />#<br /><br />default-lease-time 600;<br />max-lease-time 7200; <br />log-facility local7; <br />authoritative;<br /><br /><br /># Primary LAN IPv6 Scope<br /><br />option dhcp6.name-servers 2001:db8:f00d::e9::a;<br />option dhcp6.domain-search "dhcp.my-isp.net";<br /><br />option dhcp6.info-refresh-time 21600;<br /><br /># The subnet where the server is attached<br />subnet6 2001:db8:f00d::e9::/64 {<br />range6 2001:db8:f00d::e9:d::2 2001:db8:f00d::e9:d::ffff;<br />}<br /><br /># Other Nets<br /><br /># Primary LAN Scope<br />option dhcp6.name-servers 2001:db8:f00d::e9::a;<br />option dhcp6.domain-search "dhcp.my-isp.net";<br />option dhcp6.info-refresh-time 21600;<br /><br />subnet6 2001:db8:f00d::e0::/64 {<br />range6 2001:db8:f00d::e0:d::2 2001:db8:f00d::e0:d::ffff;<br />}<br /><br /># Pop scope 4<br />option dhcp6.name-servers 2001:db8:f00d::e9::a;<br />option dhcp6.domain-search "dhcp.my-isp.net";<br />option dhcp6.info-refresh-time 21600;<br /><br />subnet6 2001:db8:f00d::e4::/64 {<br />range6 2001:db8:f00d::e4:d::2 2001:db8:f00d::e4:d::ffff;<br />}<br /><br /># Pop Scope 5<br /><br />option dhcp6.name-servers 2001:db8:f00d::e9::a;<br />option dhcp6.domain-search "dhcp.my-isp.net";<br />option dhcp6.info-refresh-time 21600;<br />subnet6 2001:db8:f00d::e8::/64 {<br />range6 2001:db8:f00d::e8:d::2 2001:db8:f00d::e8:d::ffff;<br />}<br /><br /># Pop Scope 2<br />option dhcp6.name-servers 2001:db8:f00d::e9::a;<br />option dhcp6.domain-search "dhcp.my-isp.net";<br />option dhcp6.info-refresh-time 21600;<br />subnet6 2001:db8:f00d::e6::/64 {<br />range6 2001:db8:f00d::e6:d::2 2001:db8:f00d::e6:d::ffff;<br />}<br /><br /># Pop scope 3<br />option dhcp6.name-servers 2001:db8:f00d::e9::a;<br />option dhcp6.domain-search "dhcp.my-isp.net";<br />option dhcp6.info-refresh-time 21600;<br />subnet6 2001:db8:f00d::e7::/64 {<br />range6 2001:db8:f00d::e7:d::2 2001:db8:f00d::e7:d::ffff;<br />}<br /><br /># Fixed host section<br /><br /># this needs fixed<br />#host host1 {<br /># #host-identifier option dhcp6.client-id "\000\000\000\000\000\001\000\001 ;\232\351h[5\204\270\024";<br /># host-identifier option dhcp6.client-id "00010001 203b9ae9 685b3584 b814";<br /># fixed-address6 2001:db8:f00d::e0:0:d::9;<br /># }<br /><br />#}</pre>

\# For most ISPs, you&#8217;ll want to delegate prefixes. ARIN recommends a /48 but in most cases the de facto standard is a /59 or /56. These are significantly more sane # # prefixes. A single /64 is not sufficient, and basic IPv6 connectivity should \*never\* be a revenue generating option.

<pre># dhcpv6-pd - this needs to match the ipv6 scope of the interface, given here as a poor example that needs adjusted<br /># delegate /56's from this /40 block (65K /56's, a /56 is 256 /64's)<br />prefix6 2001:db8:f00d::  2001:db8:ff00:: /56;<br />}</pre>

This linux configuration can be leveraged by any modern router, below is the Mikrotik configuration.

For IPv6, please note that the managed flag must be set for relay, and that you may not want to set that flag for all interfaces depending on your environment

<pre>/ipv6 dhcp-relay<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.4 name=vlan4-dhcpv6<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1 name=vlan0-dhcpv6<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.6 name=vlan6-dhcpv6<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.5 name=vlan5-dhcpv6<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.7 name=vlan7-dhcpv6<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.9 name=vlan9-dhcpv6<br />add dhcp-server=2001:db8:f00d:e9::a interface=sfpplus1.8 name=vlan8-dhcpv6<br /><br />/ipv6 nd<br />set [ find default=yes ] managed-address-configuration=yes</pre>

&nbsp;

For IPv4:

<pre>/ip dhcp-relay<br />add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.9 local-address=10.254.9.1 name=dhcp-vlan9<br />add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.8 local-address=10.254.8.1 name=dhcp-vlan8<br />add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.6 local-address=10.254.6.1 name=dhcp-vlan6<br />add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.4 local-address=10.254.4.1 name=dhcp-vlan4<br />add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1.7 local-address=10.254.7.1 name=dhcp-vlan7<br />add dhcp-server=10.254.9.10 disabled=no interface=sfpplus1 local-address=10.254.209.1 name=dhcp-vlan209</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1640" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1640" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1640" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1640" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/dhcp-and-dhcpv6-relay/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
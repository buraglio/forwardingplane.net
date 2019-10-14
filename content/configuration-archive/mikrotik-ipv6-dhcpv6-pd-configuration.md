---
id: 1600
title: Mikrotik IPv6 DHCPv6-PD configuration
date: 2019-02-18T13:26:52-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1600
---
For a small to medium ISPs (especially WISPs) looking to move to IPv6 dual-stack, the right way to deploy is to use DHCPv6 prefix delegation. Here is an example of how to do this in-skin (i.e. on the mikrotik itself rather than a relay). 

<pre class="wp-block-preformatted">/ipv6 dhcp-server<br /> add address-pool=vl100-v6-pd-pool interface=ether5.100 name=vl100-v6-pd<br /> add address-pool=vl101-v6-pd-pool interface=ether3.101 name=vl101-v6-pd<br /> add address-pool=vl102-v6-pd-pool interface=ether2.102 name=vl102-v6-pd<br /> add address-pool=vl106-v6-pd-pool interface=ether1.106 name=vl106-v6-pd<br /> add address-pool=vl108-v6-pd-pool interface=ether4.108 name=vl108-v6-pd</pre>

<pre class="wp-block-preformatted">/ipv6 pool<br />
add comment="VLAN103 IPv6 prefix delegation pool" name=vl103-v6-pd-pool prefix=2001:db8:1a:b000::/48 prefix-length=59<br />
add comment="VLAN100 IPv6 prefix delegation pool" name=vl100-v6-pd-pool prefix=2001:db8:1a:8800::/48 prefix-length=59<br />
add comment="VLAN101 IPv6 prefix delegation pool" name=vl101-v6-pd-pool prefix=2001:db8:1a:9000::/48 prefix-length=59<br />
add comment="VLAN106 IPv6 prefix delegation pool" name=vl106-v6-pd-pool prefix=2001:db8:1a:9800::/48 prefix-length=59<br />
add comment="VLAN108 IPv6 prefix delegation pool" name=vl108-v6-pd-pool prefix=2001:db8:1a:a000::/48 prefix-length=59<br />
add comment="VLAN102 IPv6 prefix delegation pool" name=vl102-v6-pd-pool prefix=2001:db8:1a:a800::/48 prefix-length=59</pre>

<pre class="wp-block-preformatted">/ipv6 address<br />
add address=2001:db8:1a:103::1 disabled=yes interface=bridge.103<br />
add address=2001:db8:1a:106::1 interface=ether1.106<br />
add address=2001:db8:1a:102::1 interface=ether2.102<br />
add address=2001:db8:1a:101::1 interface=ether3.101<br />
add address=2001:db8:1a:108::1 interface=ether4.108<br />
add address=2001:db8:1a:100::1 interface=ether5.100<br />
add address=2001:db8:1a:ffff::1/128 advertise=no comment=loopback0 interface=loopback.0<br />
add address=2001:db8:1a:fffe::2/127 advertise=no comment="point to point to tower1-gw" interface=ether7</pre>

Adjust firewall filters for IPv6 as policy dictates. Do not filter ICMP

<pre class="wp-block-preformatted">/ipv6 firewall filter<br /> add action=accept chain=forward comment="Allow all IPv6"</pre>

<pre class="wp-block-preformatted">/ipv6 nd<br />
add interface=ether5.100 managed-address-configuration=yes other-configuration=yes<br />
add interface=ether3.101 managed-address-configuration=yes other-configuration=yes<br />
add interface=ether2.102 managed-address-configuration=yes other-configuration=yes<br />
add interface=ether1.106 managed-address-configuration=yes other-configuration=yes<br />
add interface=ether4.108 managed-address-configuration=yes other-configuration=yes</pre>

<pre class="wp-block-preformatted">/ipv6 nd prefix<br />
add autonomous=no disabled=yes interface=ether5.100<br />
add autonomous=no disabled=yes interface=ether3.101<br />
add autonomous=no disabled=yes interface=ether2.102<br />
add autonomous=no disabled=yes interface=ether1.106<br />
add autonomous=no disabled=yes interface=ether4.108</pre>

<pre class="wp-block-preformatted">/ipv6 route<br />
add comment="IPv6 Default Route for static deployments" distance=1 gateway=fe80::2a7:42ff:fe2d:3574%bridge.10</pre>

Tunable based on deployment model  


<pre class="wp-block-preformatted">/ipv6 settings<br /> set max-neighbor-entries=1024</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1600" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1600" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1600" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1600" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-ipv6-dhcpv6-pd-configuration/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
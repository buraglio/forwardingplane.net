---
id: 1595
title: Mikrotik Routed VLANs (non-CRS)
date: 2019-02-18T11:57:21-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1595
---
Add a simple set of VLANs to a CCR or other non-CRS RouterBoard. 



<pre class="wp-block-preformatted">/interface vlan <br />add interface=sfpplus1 name=sfpplus1.4 vlan-id=4 comment="VLAN ID 4"<br />add interface=sfpplus1 name=sfpplus1.5 vlan-id=5 comment="VLAN ID 5"<br />add interface=sfpplus1 name=sfpplus1.6 vlan-id=6 comment="VLAN ID 6"<br />add interface=sfpplus1 name=sfpplus1.7 vlan-id=7 comment="VLAN ID 7"<br />add interface=sfpplus1 name=sfpplus1.8 vlan-id=8 comment="VLAN ID 8"<br />add interface=sfpplus1 name=sfpplus1.9 vlan-id=9 comment="VLAN ID 9"</pre>

Add IP addressing to each VLAN

<pre class="wp-block-preformatted">/ipv6 address <br />add address=2001:db8:c33e:f0::1/64 advertise=no<br />add address=2001:db8:c:f4::1/64 advertise=yes interface=sfpplus1.4 <br />add address=2001:db8:c:f5::1/64 advertise=yes interface=sfpplus1.5 add address=2001:db8:c:f6::1/64 advertise=yes interface=sfpplus1.6 <br />add address=2001:db8:c:f7::1/64 advertise=yes interface=sfpplus1.7 <br />add address=2001:db8:c:f8::1/64 advertise=yes interface=sfpplus1.8 <br />add address=2001:db8:c:f9::1/64 advertise=yes interface=sfpplus1.9 </pre>

Add legacy IPv4 addressing for each VLAN

<pre class="wp-block-preformatted">/ip address<br />add address=10.2.200.1/26 interface=sfpplus1 comment="Native VLAN"<br />add address=10.2.4.1/25 interface=sfpplus1.4 <br />add address=10.2.5.1/25 interface=sfpplus1.5  <br />add address=10.2.6.1/25 interface=sfpplus1.6  <br />add address=10.2.7.1/25 interface=sfpplus1.7 <br />add address=10.2.8.1/25 interface=sfpplus1.8 <br />add address=10.2.9.1/25 interface=sfpplus1.9 </pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1595" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1595" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1595" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1595" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-routed-vlans-non-crs/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
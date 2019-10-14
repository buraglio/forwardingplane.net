---
id: 1632
title: Enabling LLDP
date: 2019-03-06T20:00:11-06:00
author: Nick Buraglio
excerpt: Configuration archive for enabling LLDP on various platforms such as Nokia SROS, JunOS, Mikrotik ROS, Linux
layout: page
guid: http://www.forwardingplane.net/?page_id=1632
---
Enabling LLDP can aid in understanding network and system topologies, I am very much in favor of running it and largely dismiss the perceived security issues surrounding it, when done correctly and with full knowledge of what it is being enabled. 

Enable LLDP on a SROS based Nokia (formerly Alcatel-Lucent). It is per physical port, so replace 1/1/1 with your physical port and replicate on every port you want it to run on

<pre class="wp-block-preformatted">/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system <br />/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-cap sys-desc <br />/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge admin-status tx-rx </pre>

Enable LLDP on a Juniper is by interface or global

<pre class="wp-block-preformatted">set protocols lldp advertisement-interval 30 <br />set protocols lldp interface all <br /></pre>

Mikrotik switch to LLDP as the discovery protocol in 6.something. MNDP/LLDP is on by default but can be changed by configuring the discover-interface-list 

<pre class="wp-block-preformatted">/ip neighbor discover-interface-list</pre>

Brocade VDX. This is a little dated but I suspect it&#8217;s still correct. 

<pre class="wp-block-preformatted">conf t <br />protocol lldp <br />&nbsp;hello 180 <br />&nbsp;advertise dcbx-tlv <br />&nbsp;advertise optional-tlv management-address <br />&nbsp;advertise optional-tlv port-description <br />&nbsp;advertise optional-tlv system-capabilities <br />&nbsp;advertise optional-tlv system-description <br />&nbsp;advertise optional-tlv system-name <br />&nbsp;system-name dnoc960-sw1-mgmt <br />&nbsp;system-description Brocade VDX switch <br />exit<br />copy running-config startup-config </pre>

Ubuntu / Debian Linux

<pre class="wp-block-preformatted">apt install lldpd<br />service lldpd start</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1632" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1632" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1632" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1632" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enabling-lldp/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
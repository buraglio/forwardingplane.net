---
id: 1597
title: Comcast Business IPv6 Prefix Delegation
date: 2019-02-18T12:58:29-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1597
---
Comcast Business class service has some quirks when using the Cisco branded business gateway. Essentially, the prefix delegation will not work without very specific configuration options on the client. In order to run your own network border (i.e. not using their device as the first hop router for your LAN(s)), the following is required. In addition, with static IP addresses also comes with a static IPv6 prefix delegation. 

For Ubiquity EdgeOS (or a derivative like a Unifi USG) the following needs to be set (eth2 is the port facing the comcast router)

<pre class="wp-block-preformatted">set interfaces ethernet eth2 dhcpv6-pd prefix-only <br />set interfaces ethernet eth2 dhcpv6-pd rapid-commit disable </pre>

Mikrotik RouterOS

<pre class="wp-block-preformatted">/ipv6 dhcp-client<br />
add add-default-route=yes comment="Native Comcast IPv6 External" interface=ether2 pool-name=comcast-ipv6 pool-prefix-length=59 request=prefix use-peer-dns=no</pre>

Essentially, the trick is make sure you do the following: 

disable rapid-commit 

request a prefix-length of exactly 59

It won&#8217;t work any other way. Requesting an address (as opposed to an address+prefix or a different prefix hint essentially breaks the request. 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1597" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1597" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1597" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1597" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/comcast-business-ipv6-prefix-delegation/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
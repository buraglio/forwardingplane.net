---
id: 1606
title: Mikrotik OpenVPN server
date: 2019-02-18T14:14:40-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1606
---
Mikrotik is one of my favorite routing and MPLS platforms for doing lab and small ISP work. This one is pretty darned easy if you&#8217;re willing to use self-signed certificates, and pretty trivial to add legitimate certificates if you are so inclined. 

<pre class="wp-block-preformatted">/certificate add name=ca common-name=ca key-usage=key-cert-sign,crl-sign<br />/certificate sign ca ca-crl-host=10.255.255.4 name=ca<br />/certificate export-certificate ca<br />/certificate add name=gw-dsl common-name=gw.yourcompany.com<br />/certificate add name=vpnclient1 common-name=client1<br />/certificate sign gw-dsl ca=ca name=gw.yourcompany.com<br />/certificate sign vpnclient1 ca=ca name=client1 <br />/ip pool add name=ovpn-pool range=10.2.98.2-10.2.98.19<br />/ppp profile add name=ovpn local-address=10.2.98.1 remote-address=ovpn-pool<br />/ppp secret add name=buraglio profile=ovpn password=ExamplePasswordDude<br />/interface ovpn-server server set enabled=yes certificate=server auth=sha1 cipher=aes256 port=1194 netmask=24 require-client-certificate=yes mode=ip<br />/certificate export-certificate client1  export-passphrase=ExamplePasswordDude</pre>

Largely based on [this example](https://delphinus.qns.net/xwiki/bin/view/Blog/Mikrotik%20OpenVPN%20in%2090%20seconds)

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1606" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1606" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1606" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1606" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/mikrotik-openvpn-example/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
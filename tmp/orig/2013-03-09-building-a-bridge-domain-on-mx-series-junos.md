I started working on Juniper equipment around 2002. At my employer, we had an M40 with the serial number 256.  We did Layer3 only.  I had no idea if the Juniper even did layer2.  It certainly wasn&#8217;t a layer3 switch like a 6500 like I was used to.  It was like a deliciously robust version of any Layer 3 router I&#8217;d worked on previously.  Over the years <a href="http://www.juniper.net/us/en/" target="_blank">Juniper</a> has added a <a href="http://www.juniper.net/us/en/products-services/switching/ex-series/" target="_blank">switching line</a> utilizing their FreeBSD based OS, <a href="http://www.juniper.net/us/en/products-services/nos/junos/" target="_blank">JunOS</a>.

All that being said, I&#8217;d never really messed with doing a layer2 transit VLAN on a JunOS routing platform.  Lets say we want to make 2 VLANs and transit them up through the WAN.  Here is how to make it work on an MX:

Create the bridge domains:

<pre>set bridge-domains vlan-123 domain-type bridge
set bridge-domains vlan-123 vlan-id 123
set bridge-domains vlan-124 domain-type bridge
set bridge-domains vlan-123 vlan-id 124
</pre>

Configure the interfaces facing south (LAN) to nbe members of the VLAN:

<pre>set interfaces xe-1/0/0 description "SW1 xe-1/1/0"
set interfaces xe-1/0/0 mtu 9192
set interfaces xe-1/0/0 unit 0 description "Untagged VLAN 123"
set interfaces xe-1/0/0 unit 0 family bridge interface-mode access
set interfaces xe-1/0/0 unit 0 family bridge vlan-id 123

set interfaces xe-1/0/1 description "SW1 xe-1/1/1"
set interfaces xe-1/0/1 mtu 9192
set interfaces xe-1/0/1 unit 0 description "Untagged VLAN 123"
set interfaces xe-1/0/1 unit 0 family bridge interface-mode access
set interfaces xe-1/0/1 unit 0 family bridge vlan-id 123

set interfaces xe-1/0/2 description "SW2 xe-1/1/2"
set interfaces xe-1/0/2 mtu 9192
set interfaces xe-1/0/2 unit 0 description "Untagged VLAN 124"
set interfaces xe-1/0/2 unit 0 family bridge interface-mode access
set interfaces xe-1/0/2 unit 0 family bridge vlan-id 124

set interfaces xe-1/0/3 description "SW2 xe-1/1/3"
set interfaces xe-1/0/3 mtu 9192
set interfaces xe-1/0/3 unit 0 description "Untagged VLAN 124"
set interfaces xe-1/0/3 unit 0 family bridge interface-mode access
set interfaces xe-1/0/3 unit 0 family bridge vlan-id 124
</pre>

Now add it to the uplink (that in this case has a layer3 instance on it as well):

<pre>set interfaces et-5/0/0 description "100G North"
set interfaces et-5/0/0 vlan-tagging
set interfaces et-5/0/0 mtu 9192
set interfaces et-5/0/0 unit 123 description "L3 testing vlan 123"
set interfaces et-5/0/0 unit 123 family bridge interface-mode trunk
set interfaces et-5/0/0 unit 123 family bridge vlan-id-list 123
set interfaces et-5/0/0 unit 124 description "L3 testing vlan 124"
set interfaces et-5/0/0 unit 124 family bridge interface-mode trunk
set interfaces et-5/0/0 unit 124 family bridge vlan-id-list 124
set interfaces et-5/0/0 unit 100 description "VLAN100 Layer3 Peering"
set interfaces et-5/0/0 unit 100 vlan-id 100
set interfaces et-5/0/0 unit 100 family inet mtu 9000
set interfaces et-5/0/0 unit 100 family inet address 10.100.100.1/30
set interfaces et-5/0/0 unit 100 family inet6 mtu 9000
set interfaces et-5/0/0 unit 10 family inet6 address 2001:fd8:a100:100::1/64
</pre>

Now check your bridge table:

<pre>buraglio@mx480> show bridge domain    

Routing instance        Bridge domain            VLAN ID     Interfaces
default-switch          vlan-123                 123      
                                                             et-5/0/0.123
                                                             xe-1/0/0.0
                                                             xe-1/0/1.0
                                                            
default-switch          vlan-124                 124      
                                                             et-5/0/0.124
                                                             xe-1/0/2.0
                                                             xe-1/0/3.0
                                                        
</pre>

That&#8217;s it. Pretty straightforward. 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-527" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-527" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-527" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-527" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/03/building-a-bridge-domain-on-mx-series-junos/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

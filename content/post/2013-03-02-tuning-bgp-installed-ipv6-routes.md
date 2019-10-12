I&#8217;ve recently run into a situation where there was no longer enough space in the FIB to handle both the full IPv4 global table and the full IPv6 global table.  We prefer to run a default-free network within this particular SP network, but in this case, until a hardware refresh can happen, we&#8217;ll need to adjust that.  Given what we knew about the size of both tables, it made more sense to take a default IPv6 route from one transit provider and filter the rest.  How we did this isn&#8217;t a groundbreaking marvel by any means, but it&#8217;s probably worth writing down for someone else to reference since it also applies to IPv4.

Since we already have global tables, a request to add IPv6 default to our existing full IPv6 table was made to one transit provider.  After that request was fulfilled, filter adjustments were made.  It should be note that all of these configs were generated off of Brocade MLX routers, so they may look a tad different than an IOS device.

Create a prefix list to reference that will allow default:

<pre>ipv6 prefix-list V6-PERMIT-DEFAULT seq 5 permit ::/0</pre>

Create the route map:

<pre>route-map IPv6-TRANSIT-DEFAULT-IN permit 100
match ipv6 address prefix-list IPv6-PERMIT-DEFAULT</pre>

Add the route-map to the peer:

<pre>neighbor 2001:fd8:e00::2 route-map in IPv6-TRANSIT-DEFAULT-IN</pre>

Before:

<pre>Neighbor Address AS#  State Time  Rt:Accepted Filtered Sent ToSend
2001:fd8:e00::2 65001 ESTAB 15d10h34m  12003    0       14    0</pre>

After:

<pre>Neighbor Address AS#  State Time  Rt:Accepted Filtered Sent ToSend
2001:fd8:e00::2 65001 ESTAB 15d10h34m     1    12002     14    0</pre>

Now we&#8217;ll need to filter the prefixes of every other peer to allow for only IPv6 routes sized /32 or larger:

<pre>route-map IPv6-BILAT-IN permit 100
 match ipv6 address prefix-list IPv6-PERMIT-ANY-32
 set community 65403:1425
 set local-preference 200 

ipv6 prefix-list IPv6-PERMIT-ANY-32 seq 5 permit ::/0 le 32</pre>

Once applied to the peers this will limit the routes installed into the FIB.

Install them by adding the route-map to the appropriate peers:

<pre>neighbor 2001:db8:0:300e::1 route-map in IPv6-BILAT-IN</pre>

<pre>SSH@RTR7#sh ipv6 bgp summary 
  BGP4 Summary 
  Router ID: 10.6.16.10   Local AS Number: 65403
  Confederation Identifier: not configured
  Confederation Peers: 
  Maximum Number of IP ECMP Paths Supported for Load Sharing: 1
  Number of Neighbors Configured: 16, UP: 16
  Number of Routes Installed: 15297, Uses 1315542 bytes
  Number of Routes Advertising to All Neighbors: 50641 (5632 entries), Uses 270336 bytes
  Number of Attribute Entries Installed: 26036, Uses 2343240 bytes
  Neighbor Address  AS#         State     Time     Rt:Accepted Filtered Sent     ToSend

  2001:db8:1900:b::2
                      65531       ESTAB    56d 8h52m    14       0        2        0        
  2001:db8:f000:213a::1
                      65164       ESTAB     3d19h31m    4187     4535     2        0        
  2001:db8:0:300e::1
                      65381       ESTAB    56d 8h35m    5087     6532     2        0        
  2001:db8:5fff:1::1
                      65237       ESTAB   149d16h18m    11       0        2        0        
  2001:db8:1:102::1
                      65100       ESTAB    24d16h55m    3        0        2        0        
  2001:db8:f10:1::1   65403       ESTAB   453d12h42m    3        0        5625     0        
  2001:db8:f10:1::2   65403       ESTAB   101d21h24m    2        0        5625     0        
  2001:db8:f10:1::3   65403       ESTAB   453d11h29m    1        0        5625     0        
  2001:db8:f10:1::4   65403       ESTAB   453d11h 8m    1        0        5625     0        
  2001:db8:f10:1::5   65403       ESTAB   453d12h17m    1        0        5625     0        
  2001:db8:f10:1::6   65403       ESTAB   453d12h 3m    1        0        5625     0        
  2001:db8:f10:1::7   65403       ESTAB   453d11h36m    1        0        5625     0        
  2001:db8:f10:1::8   65403       ESTAB   160d17h52m    5078     0        5625     0        
  2001:db8:f10:1::9   65403       ESTAB   453d11h 3m    1        0        5625     0        
  2001:db8:f10:6013::2
                      65532       ESTAB    15d19h50m    904      3        2        0        
  2001:db8:f10:6016::2
                      65527       ESTAB   126d15h29m    1        0        2        0</pre>

As you can see, peers on AS65164 and AS65381 are both filtering a large amount of traffic that is smaller than /32. Couple that with the inclusion of a default route and the traffic has a good deal of best path and a default for everything else. Its not exactly the most elegant, but it does solve a problem that folks may be seeing on aging equipment with limited resources.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-485" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-485" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-485" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-485" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/03/tuning-bgp-installed-ipv6-routes/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

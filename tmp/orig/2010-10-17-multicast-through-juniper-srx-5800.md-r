We&#8217;ve been working toward a more simplified model for our network path, and in doing so, we desired a congruent path for IPv6, IPv4 Multicast and IPv4 Unicast.  
However, this is actually pretty hard when dealing with the link speeds, amounts of traffic and flows that we do, in conjunction with Firewall&#8230;..and IDP/IPS&#8230;  
Lots of research, reading and testing was done.  
Juniper SRX series has full support for 90% of this, with IPv6 IDP coming in Q2 of 2011.

IPv4 Multicast is that unpleasant, poorly understood beast that most folks try to ignore. Nevertheless, we need it. So, we had to make this work through our SRX (in the past IPv4 multicast took a different path in/out of our network. 

<div>
  I&#8217;m going to glaze over the multicast bits on our Juniper MX routers, if you&#8217;re doing multicast already, this should already be working and Juniper has well documented and well implemented multicast capabilities.
</div>

<div>
  On the SRX, luckily, it&#8217;s pretty similar.
</div>

<div>
</div>

<div>
</div>

<div>
  <div>
    <span style="font-size: small;"><span>buraglio@srx5800> show configuration protocols pim </span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>rib-group inet multicast-rpf-rib;</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>rp {</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span> static {</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span> address 10.16.0.145;</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span> }</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>}</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>interface xe-1/1/0.0;</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>interface xe-2/1/0.0;</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>interface xe-10/1/0.0;</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>interface xe-13/1/0.0;</span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span><br /></span></span>
  </div>
  
  <div>
    <span style="font-size: small;"><span>{primary:node0}</span></span>
  </div>
</div>

<div>
</div>

<div>
  <span style="font-size: medium;">Make sure you are importing the routes into the tables by configuring your RIB groups</span>
</div>

<div>
</div>

<div>
  <div>
    <span><span style="font-size: small;">buraglio@srx5800> show configuration routing-options rib-groups </span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;">igp-rib {</span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;"> import-rib [ inet.0 inet.2 ];</span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;">}</span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;">multicast-rpf-rib {</span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;"> export-rib inet.2;</span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;"> import-rib inet.2;</span></span>
  </div>
  
  <div>
    <span><span style="font-size: small;">}</span></span>
  </div>
</div>

<div>
</div>

<div>
  <span style="font-size: medium; "><span>You&#8217;ll need to make sure that there is a firewall policy to permit your multicast to actually flow. For arguments sake, I&#8217;m assuming you have an outbound policy that is less than or equal to this in terms of policy allowed.</span></span>
</div>

<div>
  <span><br /></span>
</div>

<div>
  <span></p> 
  
  <div>
    <span><span style="font-size: small;"></p> 
    
    <div>
      {primary:node0}
    </div>
    
    <div>
      buraglio@srx5800> show configuration security policies from-zone Untrust to-zone Trust policy Multicast-permit
    </div>
    
    <div>
      match {
    </div>
    
    <div>
      source-address any;
    </div>
    
    <div>
      destination-address multicast_224_0_0_0_4;
    </div>
    
    <div>
      application junos-udp-any;
    </div>
    
    <div>
      }
    </div>
    
    <div>
      then {
    </div>
    
    <div>
      permit;
    </div>
    
    <div>
      log {
    </div>
    
    <div>
      session-init;
    </div>
    
    <div>
      }
    </div>
    
    <div>
      }
    </div>
    
    <div>
    </div>
    
    <p>
      </span></span></div> 
      
      <div>
        <span style="font-size: medium;"><span>Thats pretty much it as far as the SRX goes (assuming I&#8217;m remembering correctly, it&#8217;s been a while since we did it and I don&#8217;t know multicast as well as I&#8217;d like). </span></span><span style="font-size: medium;"><span>Using the </span></span><a href="http://globalnoc.iu.edu/i2network/multicast-cookbook.html"><span style="font-size: medium;"><span>cookbook from Internet2</span></span></a><span style="font-size: medium;"><span> one should be enough to get Multicast working with your SRX as long as you have your policy set to allow it. </span></span>
      </div>
      
      <p>
        </span></div> 
        
        <div>
        </div>
        
        <div>
        </div>
        
        <div>
          <span><span style="font-size: small;">buraglio@srx5800> show multicast statistics</span></span>
        </div>
        
        <div>
          <span><span style="font-size: small;">&#8230;snip&#8230;</span></span>
        </div>
        
        <div>
          <div>
            <span><span style="font-size: small;">Interface: xe-10/1/0.0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Routing protocol: PIM Mismatch error: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Mismatch: 8 Mismatch no route: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Kernel resolve: 287 Routing notify: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Resolve no route: 0 Resolve error: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Resolve filtered: 0 Notify filtered: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> In kbytes: 4273 In packets: 45042</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Out kbytes: 18014398509409554 Out packets: 18446744073709258616</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;">Interface: xe-1/1/0.0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Routing protocol: PIM Mismatch error: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Mismatch: 11786 Mismatch no route: 3</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Kernel resolve: 323210 Routing notify: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Resolve no route: 0 Resolve error: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Resolve filtered: 0 Notify filtered: 0</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> In kbytes: 100127811 In packets: 1164651571</span></span>
          </div>
          
          <div>
            <span><span style="font-size: small;"> Out kbytes: 10827919 Out packets: 80039321</span></span>
          </div>
        </div>
        
        <div>
          <span><span style="font-size: small;">&#8230;snip&#8230;</span></span>
        </div>
        
        <div>
          [[ This is a content summary only. Visit my website for full links, other content, and more! ]]
        </div>
        
        <div class="sharedaddy sd-sharing-enabled">
          <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
            <h3 class="sd-title">
              Share this:
            </h3>
            
            <div class="sd-content">
              <ul>
                <li class="share-twitter">
                  <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-47" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
                </li>
                <li class="share-email">
                  <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
                </li>
                <li class="share-print">
                  <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/" target="_blank" title="Click to print"><span>Print</span></a>
                </li>
                <li class="share-linkedin">
                  <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-47" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
                </li>
                <li class="share-facebook">
                  <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-47" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
                </li>
                <li class="share-reddit">
                  <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
                </li>
                <li class="share-tumblr">
                  <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
                </li>
                <li class="share-pinterest">
                  <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-47" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
                </li>
                <li class="share-pocket">
                  <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2010/10/multicast-through-juniper-srx-5800/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
                </li>
                <li class="share-end">
                </li>
              </ul>
            </div>
          </div>
        </div>
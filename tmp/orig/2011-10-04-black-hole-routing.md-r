It&#8217;s no secret or ground breaking area to do black hole routing. 

<div>
  ISPs and NSPs have been doing it forever to allow for a very low cost, very scriptable and very effective way to wholesale block a layer3 address. However, it can seem like a bit of a black box to anyone who has never done it. </p> 
  
  <div>
    I recently did some work spinning this up in a good sized network that it didn&#8217;t currently exist, and remembered how monumentally useful (and simple) it actually is.
  </div>
  
  <div>
    There are lots of ways to do this. There are a lot of different <a href="http://packetlife.net/blog/2009/jul/6/remotely-triggered-black-hole-rtbh-routing/">articles</a> written about how to do it. Cisco includes it in their CCIE Security track.
  </div>
  
  <div>
    The idea is a pretty simple one. Run <a href="http://en.wikipedia.org/wiki/Reverse_path_forwarding#Unicast_RPF_.28uRPF.29">uRPF</a> on your eBGP speakers. Create a peering with a router on the inside. For my purposes I used a private ASN and peered it with eBGP to my border devices. Create a static route to null0 on the BHR (Black Hole Router), which then sends the route (possibly tagged with a community) to the eBGP speakers. They see an internal route for this external host, so any packets that come from that host on the outside get dropped on the floor by uRPF. In theory it&#8217;s all handled in hardware so the overhead is minimal and the blocks are as fast as a BGP route advertisement/withdrawal.
  </div>
  
  <div>
  </div>
  
  <div>
    There are, of course, lots of caveats to this, like, what if you are taking default on your eBGP speakers? How is that handled. One of the places I recently set this up takes default, one takes full tables. I suggest reading <a href="http://www.cisco.com/web/about/security/intelligence/unicast-rpf.html">this page</a> if you aren&#8217;t experienced with uRPF, it explains how cissco handles it and is a decent primer on uRPF in general.
  </div>
  
  <div>
  </div>
  
  <div>
    I&#8217;m a simple guy and I like things to be easy to support, so my designs tend to be those that can easily be maintained by someone that !=me and not so overly complicated that they can be reverse engineered in case of emergency or replicated if need be.
  </div>
  
  <div>
    That said, I&#8217;ve chosen to do it in a pocketbook friendly way. It probably stems from cutting my teeth at a decent sized mom and pop ISP that had a very small operating budget so we did things in creative and cost savings ways while still keeping them simple and supportable. I&#8217;m not sure why, but it makes more sense to me to run a software router like <a href="http://www.blogger.com/www.quagga.net">Quagga</a> or <a href="http://www.openbgpd.org/">OpenBGPd</a> that I can run as a VM and connect to my IGP and EGP, scripting the adds and removal of the routes we want to blackhole. It can also be done with an actual router, but I personally prefer to drop it in as a software router.
  </div>
  
  <div>
  </div>
  
  <div>
    The use of a linux box allows for a bunch of neat options. You can use the iproute2 package to watch changes to the routing table, you can run it in a virtual machine, it can be done in a very economical way, etc.
  </div>
  
  <div>
    Using Quagga has its pros and its cons. Quagga is a great platform, but it is an open source project. Their ISISd support is a bit lacking, so if your IGP is ISIS, it will work, but it feels half baked to me (and there is zero documentation that I could find). The ospf[v2 and v3] versions work fine. BGPd works well enough. It can be put into RANCID for configuration management and it is easily scriptable using vtysh and its IOS-like interface.
  </div>
</div>

<div>
</div>

<div>
  <div>
    Here is a basic design for a black hole router running inside a network with an external peering with something like a bogon route server:
  </div>
</div>

<div>
  </p> 
  
  <div style="clear: both; text-align: center;">
    <a href="http://4.bp.blogspot.com/-5lZmt2zsQ3Y/T3oMBMHyysI/AAAAAAABIS4/T5lzIgb0I2I/s1600/BHR+Example.jpg" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="320" src="http://4.bp.blogspot.com/-5lZmt2zsQ3Y/T3oMBMHyysI/AAAAAAABIS4/T5lzIgb0I2I/s320/BHR+Example.jpg" width="269" /></a>
  </div>
  
  <p>
    </div> 
    
    <div>
    </div>
    
    <div>
      This just shows a basic setup, one site border router and a black hole box. In this example, the BHR is also peered with an external &#8220;service&#8221; like a bogon route server. This is a value-add, and not required.
    </div>
    
    <div>
      Any traffic that comes in can be routed to null0 on the bhr. This, in turn, sends a routes to the SBR. The SBR then installs it as an internal route. Now, any traffic that comes in from this route outside will looked like spoofed traffic and uRPF will discard it.
    </div>
    
    <div>
      Very simple, very effective.
    </div>
    
    <div>
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
              <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-29" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
            </li>
            <li class="share-email">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
            </li>
            <li class="share-print">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/" target="_blank" title="Click to print"><span>Print</span></a>
            </li>
            <li class="share-linkedin">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-29" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
            </li>
            <li class="share-facebook">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-29" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
            </li>
            <li class="share-reddit">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
            </li>
            <li class="share-tumblr">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
            </li>
            <li class="share-pinterest">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-29" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
            </li>
            <li class="share-pocket">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/10/black-hole-routing/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
            </li>
            <li class="share-end">
            </li>
          </ul>
        </div>
      </div>
    </div>
<div>
  Edit: <em>Going against my normal “just get the content out there” methodology, I’ve been mulling over this blog post since July of 2016.  Segment routing is such a beautifully elegant solution I have had trouble articulating that fact. WAN technologies are squarely within my wheelhouse, and this one fits in so well I was going over and over the post never really satisfied with it, continuing to find mistakes and decided to just get it out there. </em>
</div>

<div>
</div>



<div>
  As a WAN guy by chance and opportunity, and a service provider engineer and architect by choice (and also chance and opportunity), segment routing (SR) is one of those wonderful new technologies that keeps rearing its head over and over in recent days &#8211; and it&#8217;s already playing in the big leagues. SR is supported by many of the large network equipment providers including Cisco, Juniper, and Nokia (Alcatel-Lucent), and as I have just learned, Arista.
</div>



<div>
  Why is this a notable tech you may want to pay attention to? Wide area and service provider networks have a longer mean time before replacement. They don’t change topology or architecture nearly as often and the gear typically has higher cost due to things like deeper interface buffers, more complex feature sets, larger TCAM for things like route tables, as well as increased redundancy features. Managing a WAN has a different feel and a different set of problems. Complex overlays and traffic engineering often play a role in wide area networks. Many an attempt to reduce the the complexity of WANs has been made and SDN is creeping its way into some pretty large networks. When a network of any size is built, there comes a tipping point when managing things by hand, even with great documentation, is too daunting and cannot be done efficiently. Automation is key. Simplicity is paramount. Anyone that has ever managed a large MPLS network knows this. So, when I started looking at segment routing, I was cautiously optimistic &#8211; it had many attributes that were comfortable to a seasoned WAN engineer and yet abstracted many of the complexities of the networks that we&#8217;d been running for years. In order to really understand the benefits that SR brings to the table, it&#8217;s important to understand the current landscape. When one builds a large MPLS network there are incremental elements that all build from each other in order to work. If one is broken or problematic, the problem will trickle up the stack. Fundamentally, the stack for a very vanilla MPLs WAN contains the following elements (top down):
</div>

<div>
</div>

  * Client service interface
  * Overlay, L3VPN, VPLS, ePIPE/PseudoWire/VLL
  * BGP
  * Label Distribution, LDP, etc.
  * IGP, IS-IS or OSPFv2/3
  * Ethernet, SONET, DS1/DS3/E1
  * Optical transport or other last mile and long haul outside plant

<div>
</div>

<div>
  Add into this list the complications of traffic engineering, and you&#8217;ve got a mix of things that are fairly daunting to all but the most experienced engineers. What segment routing provides is a way to remove several layers of this and simplify what is arguably the most complex and least understood element: Traffic Engineering. Segment routing allows for the selection of an entire path, from the ingress of the network to the egress port, all outside of the IGPs shortest path table. It is often labeled as &#8220;source routing&#8221; which will inevitably create feeling of disgust, dread, and distain from a network engineer and panic from the security folks. I choose not to label SR as &#8220;source routing&#8221; because of the negative connotation associated with that technological approach. Instead, I would rather use the term &#8220;deliberate path selection&#8221;.
</div>

<div>
  Oh, and this can be automated. That&#8217;s right. It&#8217;s &#8220;SDN&#8221;. Utilizing a tool called a path computational engine or &#8220;PCE&#8221;, these paths can be selected based on any number of criteria including latency, hop count, load, time of day, phase of the moon, mood of the boss, etc.
</div>

<div>
</div>

<div>
  I was lucky enough to get to spend some quality time at a <a href="http://techfieldday.com/event/srr1/">special event</a> recently. Interesting discussions were had, many a thing was learned. A few of the other attendees wrote up some great info on segment routing, including some use cases, which can be found here
</div>

<div>
</div>

<div>
  <div>
    Terry Slattery on No Jitter
  </div>
  
  <div>
    <a href="http://www.nojitter.com/post/240171828/segment-routing-inside-a-new-sdn-technology" target="_blank" rev="en_rl_small">http://www.nojitter.com/post/240171828/segment-routing-inside-a-new-sdn-technology</a>
  </div>
  
  <div>
  </div>
  
  <div>
    Carl Niger on Come Route With Me
  </div>
  
  <div>
    <a href="https://comeroutewithme.com/2016/07/24/post-tfd-segment-routing-roundtable-thoughts/" target="_blank" rev="en_rl_small">https://comeroutewithme.com/2016/07/24/post-tfd-segment-routing-roundtable-thoughts/</a>
  </div>
  
  <div>
  </div>
  
  <div>
    Russ White on Net Work
  </div>
  
  <div>
    <a href="http://ntwrk.guru/dc-fabric-segment-routing-use-case-1/" target="_blank" rev="en_rl_small">http://ntwrk.guru/dc-fabric-segment-routing-use-case-1/</a>
  </div>
  
  <div>
    <div>
      <a href="http://ntwrk.guru/dc-fabric-segment-routing-use-case-2/" target="_blank" rev="en_rl_small">http://ntwrk.guru/dc-fabric-segment-routing-use-case-2/</a>
    </div>
    
    <div>
      <div>
        I highly recommend taking a view of the talks from some folks using SR on some pretty significant networks &#8211; it&#8217;s worth your time if you&#8217;re really interested in throwing down with segment routing.  But what did this tell <b><i>me</i></b>? Lets look further into SR and see why it&#8217;s become so attractive to large, geographically diverse networks. First, SR builds on an existing knowledgeable. Far more people exist in the market that already know MPLS. The understand labels, they understand overlays, and they have vast experience with virtual circuits. Service providers are very likely MPLS based if they operate at any scale and offer typical ISP services. MPLS is well traveled, and even though there may be reasons that&#8217;s not perfect, it&#8217;s the devil we know. Other SDN technologies are either fairly green (l<a href="http://blog.ipspace.net/2015/12/running-open-daylight-in-production.html#more">et me tell you about running a production openflow experience</a>) or are primarily focused on the data center, which as I will adamantly insist is a very different beast.
      </div>
    </div>
    
    <div>
      <span style="color: #222222; font-family: arial, sans-serif;">Large scale service providers have a very different redundancy model. Attempting to apply campus or enterprise redundancy to a service provider does not scale and it certainly isn&#8217;t affordable. SR leverages the same models that MPLS does, it realies heavily on the IGP, leveraging a TLV within IS-IS. That brings me to IS-IS. Most service providers leverage IS-IS as their internal gateway protocol due to it&#8217;s ability to carry multiple routed protocols at once, leverage multi-topology, and the fact that it does not rely on the protocol it is routing for connectivity like OSPF does. SR is more-or-less an extension to IS-IS. Overlapping skill set #2. The other option, and this is a big one, is that there are multiple vendors that supported, as stated above. This is a big deal as int provides that &#8220;throat to choke&#8221; that a lot of emerging technologies just do not really have yet.</span>
    </div>
    
    <div>
      <span style="color: #222222; font-family: arial, sans-serif;">Did I mention that it &#8220;fails open”? What’s not to love about falling back to an IGP rather than ceasing to process packets?  Lets do a for-instance use-case. Within your SR network you provision a path that takes a path with more hops but has less congestion. Create your label stack and away you go* Of that path fails, the traffic falls back to the standard routing table.</span>
    </div>
    
    <div>
      <span style="color: #222222; font-family: arial, sans-serif;">Much like MPLS (of which I am a fan, FWIW), this technology is better suited for a larger network with multiple paths, this could be any number of  environments such as large camps networks, large scale data centers geographically diverse environments connected by multiple WAN circuits, and of course, service and content providers. This tech is quite simply full of win. </span>
    </div>
    
    <div>
    </div>
    
    <div>
      *greatly <span style="color: #222222; font-family: arial, sans-serif;">simplified =)</span>
    </div>
    
    <div>
    </div>
  </div>
</div>

<div>
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1365" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1365" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1365" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1365" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2016/10/care-segment-routing/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
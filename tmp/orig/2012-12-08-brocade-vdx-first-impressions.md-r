I recently had the opportinity to work with the much-anticipated [Brocade VDX &#8220;Ethernet Fabric&#8221;](http://www.brocade.com/launch/cloud-clarity/solutions-technology-innovation.html) platform.  I do admit tha tI&#8217;m intrigued by this product.  I&#8217;d seen it work multiple times in demos and it worked so well and looked to easy that we actively tried to throw curve balls at the demo organizer to prove it wasn&#8217;t canned.

<img class="aligncenter" src="http://www.brocade.com/images/products/vdx-6720-dc-switches/VDX6720-24_front_large.jpg" alt="" width="375" height="240" /> 

It succeeded.

The hardware hashing across the VLAGs is very slick.  The VMware VSwitch integration worked well and was handy.  With the movement to virtualization, this is an important piece for most data center folks.

That being said, some people have very specific data center requirements that aren&#8217;t really the same as an enterprise.  For example:

  * Don&#8217;t firewall everything at the DC. That&#8217;s right. I said it.  Firewalls don&#8217;t solve all security problems.  Take that &#8220;defense in depth&#8221;!
  * A potential need to do non-standard or experimental protocols.
  * A lot of line rate 10G internally and to the rest of network.
  * Integration with legacy, existing and or in-house written tools
  * Need for GSLB/SLB
  * Self Healing
  * Ease of fabric upgrade (software upgrade doesn&#8217;t cause fabric isolation)
  * Ease of fabric upgrade (increase LAG numbers and capacity easily)
  * Multi-Homed hosts
  * IPv4
  * IPv6
  * IPv4 Multicast
  * Future SDN support
  * NAT
  * Public Address space
  * All at the same time

<div>
  But I digress.  We can get into the Data Center design details later.  Below would be a theoretical data center reference design for a fabric deployment.  Please bear in mind that I mostly like to focus on the WAN and SP bits, so take my data center speculations and musings with a grain of salt.
</div>

<div>
</div>

<div>
</div>

[<img class="alignnone  wp-image-149" title="Flexible DC" src="http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC.jpg" alt="" width="508" height="576" srcset="http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC.jpg 635w, http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC-264x300.jpg 264w, http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC-550x623.jpg 550w" sizes="(max-width: 508px) 100vw, 508px" />](http://www.forwardingplane.net/wp-content/uploads/2012/11/Flexible-DC.jpg)

&nbsp;

The Brocade VDX does most of what can be expected of a layer 2 fabric.  It really is the &#8220;easy&#8221; part of a DC design.  If you can avoid STP, I would heavily recommend it.  I have an unnatural dislike for spanning tree.

The unexpected things I ran into with my very brief hands-on with the VDX were just that, unexpected.  I could reliably crash ssh on the boxes by sending a public key at login, which is default behavior for a normal ssh client.  This was very annoying and implied that they don&#8217;t yet support ssh keys for authentication.  One can work around it by doing _ssh -o PubkeyAuthentication=no -l <name>_ and worked with the newest version of putty, which I don&#8217;t use.  The version of OpenSSH on my Mac running 10.8.2 had an issue with it, as did the linux jumphost I used.

There is no way, in current software to manage this centrally like you can with qfabric.  Each device is an individual switch.  I suspect this will change since it&#8217;s pretty inconvenient and I know many folks have asked for it.  This was my biggest issue with it.

It doesn&#8217;t run spanning tree.  It has a loop detection mechanism, but it isn&#8217;t spanning tree.  It&#8217;s not meant to have anything but end hosts or other VDX plugged into it from what I gather, other than uplinks.

Unknown SDN roadmap.  Currently it&#8217;s unsupported but with the level of commitment that Brocade has given to SDN so far, I&#8217;m cautiously optimistic.

Untested Layer 3 capabilities.  It&#8217;s a new platform and they&#8217;ve just added layer3 into it.  I have no intention of testing the layer3 capabilities since I doubt that I&#8217;d want to route on them.

Unknown IPv6 RA guard status.  Tis is important and I&#8217;m fairly certain they&#8217;ll add it, but it wasn&#8217;t in the code load that we had at SC12, at least that I could find.

It is easily integrated into RANCID. [I hacked together a script to do this](http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/) in about 10 minutes and I&#8217;m an awful programmer.

It looks EXACTLY like IOS so folks familiar with Ciscos venerable IOS command line will have absolutely no issue picking this right up.

Some of the things I didn&#8217;t get to do during this first run were to put a packet cannon like an IXIA on it and jam traffic up to, and ideally beyond the limits and see how it reacts and to point existing SNMP based tools at it (other than basic up/down status).  I&#8217;d also like to push the limits of the interconnect between geographic locations and see the latency and efficiency of the VLAG ports when moving traffic and virtual machines.  With luck these will happen at some point soon.

Bear in mind that this is a relatively new product.  I would probably place the best competitor for this as the Juniper Qfabric or Microfabric, bith of which are a larger scale product and suffer from some of the same issues.  I&#8217;m excited to see more about it, it did its job pretty well.  Juniper and cisco take notice, these bits are important and [more than just brocade are working on it](http://www.plexxi.com).

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-8" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-8" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-8" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-8" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
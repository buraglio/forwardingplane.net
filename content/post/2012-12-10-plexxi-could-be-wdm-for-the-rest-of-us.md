[Plexxi](http://www.plexxi.com) is an interesting product that has recently emerged in the data center space.  While data center, fabric and cloud are all the rage in the buzzword world of data networking, this one caught my attention because it was something unique that I&#8217;d not seen before.  Their TOR boxes have a few interesting additions to them, the first of which is a WDM port on the back. Now, I&#8217;m not really a stranger to the WDM world.  I&#8217;ve been helping maintain a DWDM network in one capacity or another for a little over a decade, but seeing this, by default, in a data center positioned switch?  Now that got my attention.

For those that don&#8217;t know what that is, [Wave Division Multiplexing](http://en.wikipedia.org/wiki/Wavelength-division_multiplexing) the ability to slice up light into what telco (and other networking folks) call waves. Each wave is a different &#8220;color&#8221; or wavelength.  Plexxi calls their flavor &#8220;Affinity Networking&#8221; and it allows for the ability to provision more bandwidth over a single pair of fiber, just like typical WDM.

For example, say you have a pair of fiber from one data center to another, either in the same facility or across your city (distances up to 10K now, 70K on the roadmap).  You&#8217;d normally plug in a 1G or 10G (or 100G if you&#8217;re really, really well funded) and provision service over that pair of fiber, assuming it is in within distance and optical power spec of the other side.  You&#8217;re stuck with that interface speed, right?  Wrong. Enter WDM.   On WDM systems you have the ability to provision channels, sometimes in huge amounts, over the same pair.  I&#8217;ve seen multiple 100G waves, OC192 Waves, a plethora of 10G waves and a few 1G waves all working fine over the same pair of fiber, and where fiber is sparse or prohibitively expensive, this is a big deal.

[<img class="aligncenter size-full wp-image-163" title="prism4c" src="http://www.forwardingplane.net/wp-content/uploads/2012/12/prism4c.gif" alt="" width="400" height="300" srcset="http://www.forwardingplane.net/wp-content/uploads/2012/12/prism4c.gif 400w, http://www.forwardingplane.net/wp-content/uploads/2012/12/prism4c-300x225.gif 300w" sizes="(max-width: 400px) 100vw, 400px" />](http://www.forwardingplane.net/wp-content/uploads/2012/12/prism4c.gif)

Plexxi &#8220;Affinity Networking&#8221; boasts the ability to do WDM right in the back of their 32 port 10G switches.

Very slick.  But that&#8217;s not all.  Enter part 2.  They also boast software defined (but not OpenFlow) control over the product, enabling dynamic provisioning of  bandwidth, on demand.. They&#8217;ve purpose built their own proprietary and described as &#8220;extended&#8221; version of SDN, geared toward a bigger picture of their network equipment and what it can do.  Their  SDN is called called &#8220;Plexxi Control&#8221; and it ties all of their switches together, allowing for a flattening of the network.  I find this approach intriguing, I&#8217;m a fan of the fabric approach to layer 2 a la [Juniper Qfabric](http://www.juniper.net/us/en/products-services/switching/qfx-series/) or [Brocade VDX](http://www.forwardingplane.net/2012/12/brocade-vdx-first-impressions/), but the WDM port and the decoupled control together is unique &#8230;.and enthralling.

Now, I have not yet had my hands on these boxes, but I think that they will be a piece in what has become a rapidly changing landscape of data centers.  WDM has been around forever in the service provider wide area, but the ability to change bandwidth allocations using WDM on the fly in a commercially supportable commoditized box is game changing.  There have been several research projects in the past that have attempted to do this, the [DRAGON project](http://dragon.maxgigapop.net/twiki/bin/view/DRAGON/WebHome), of which one of the sites I helped maintain was a member, attempted to do something like this using [GMPLS](http://en.wikipedia.org/wiki/Generalized_Multi-Protocol_Label_Switching)  on the WAN gear.

Doing it in the data center?  That&#8217;s new.

I look forward to seeing some of these boxes function up close and personal.  I&#8217;m especially interested in the longer distance pieces of these for remote data centers and DR locations.

For a comprehensive write up, see [this article](http://searchnetworking.techtarget.com/news/2240173858/Plexxi-SDN-includes-tiered-controller-data-center-based-WDM) by [Shamus McGillicuddy](http://searchnetworking.techtarget.com/contributor/Shamus-McGillicuddy).  [ ](http://searchnetworking.techtarget.com/news/2240173858/Plexxi-SDN-includes-tiered-controller-data-center-based-WDM)

### 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-147" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-147" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-147" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-147" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/12/plexxi-could-be-wdm-for-the-rest-of-us/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

<div>
       I was recently at a meeting where BGP RPKI was the topic de jour. While this has been a topic that I have visited on occasion of the last few years and something I wanted to spend significant time on, I have found that setting aside the time has been difficult and sparse, much like the deployment of BGP RPKI. In order to better understand the options available, it&#8217;s important to break down the pieces and terminology involved; BGP is daunting enough to those unfamiliar with it and adding PKI on top of that can be even more so. So, what are these bits and pieces and why have we not done more to adopt it?
</div>

  * **BGP** &#8211; the venerable and foundational protocol that quite literally runs the internet. BGP allows an organization to announce and exchange it’s IPv4 and IPv6 resources with other organizations.
  * [**Resource Public Key Infrastructure**](https://www.arin.net/resources/rpki/) &#8211; From [ARIN](https://www.arin.net/resources/rpki/): _Using cryptographically verifiable certificates, RPKI allows IP address holders to specify which Autonomous Systems (AS&#8217;s) are authorized to originate their IP address prefixes. These statements, known as Route Origin Authorizations (ROAs), allow network operators to make informed routing decisions, and help secure Internet routing in general. _
  * **ROA** &#8211; Route Origin Authorizations &#8211; Who is authorized to originate or source these prefixes?
  * **ROV** &#8211; Route Origin Validation &#8211; Can we validate, cryptographically, that the origin of this resource (for example, 8.8.8.8) is authorized to originate or source these prefixes?

<div>
       Many of the details of RPKI are actually not even technical, both with ARIN and with vendors, there exists complications that make the technical pieces look like child’s play. Legality of the licensing and housing of authoritative certificates are complicated, shrouded in legalese due to the nature of what they represent. This proves to be a show stopper for a lot of older organizations that have grandfathered address space and may not have gone through the ARIN agreement process any time in the recent past [note: supposedly this process is required for ARIN IPv6 space, so most of that <i>should</i> be covered. Other regions may have easier, lower hurdles &#8211; I’ve heard good things about RIPE’s process &#8211; but I have no experience with it. The legal issues with contracts and signing certificates may also prove to be troublesome to enterprises, most of which are very conservative and slow to adopt anything new ::cough:: IPv6 ::cough::.  Certificate generation and maintenance is also considered difficult in many cases, the details can be confusing and the documentation overwhelming or difficult to find.
</div>

<div>
  On top of those non-technical issues, platforms with large install bases are sparsely supported &#8211; although this is changing.
</div>

<div>
       There have been a <a href="http://www.bgpmon.net/large-scale-bgp-hijack-out-of-india/">number</a> of <a href="http://www.bgpmon.net/large-hijack-affects-reachability-of-high-traffic-destinations/">recent</a>, high profile route hijacks. If you’re ever curious to see what they were, BGPMon typically has a post-mortem shortly after they occur. This is a big deal. There are a number of ways they could have been prevented, too one of which is BGP RPKI. Is that worth the overhead? I think anyone that has had to scramble to figure out what was going on during one of these events would argue yes. But even with that, we have minimal adoption. With the significant movement to cloud based work, enterprises, service providers, academic institutions and even savvy end users should ask themselves a few important questions before doing your risk analysis:
</div>

<div>
</div>

  * Do your cloud providers do RPKI?
  * Does your upstream service provider or peering partner honor invalid routes?
  * Does your upstream service provider or peering partner even support prefix or AS-Path filtering?
  * How does the effect BGP blackhole routing for security filtering?
  * How do you deal with invalid routes? (alert, set preference, drop, etc.)
  * How do you handle invalid routes that may be more specific?
  * Why have I not deployed BGP RPKI yet?

<div>
</div>

<div>
  <strong>My perspective:</strong>
</div>

<div>
</div>

<div>
      Unfortunately, the feeling I get is very similar to that of things [that we actually need] such as IPv6 and DNSSec. Tools that make our resources safer,  but are often overlooked due to increased operational complexity.
</div>

<div>
  It is really about risk analysis: Is the risk of not having this worth the effort of maintaining it?  Since we [as an internetworking ecosystem] been clear in our actions that necessary things as obvious and straightforward as appropriate prefix filtering and IPv6 deployment are in many cases above and beyond, it should come as no surprise that adding complexity on top of “stuff that just works” is’t happening on a large scale. Even with repeated proof that changes would alleviate risk, we don’t do it because what we have has been deemed “good enough”* and change is scary and hard.
</div>

<div>
  What do we need? We need tools. The <a href="http://rpki.surfnet.nl/">RPKI dashboard</a> that SURFnet has available is a fantastic example of an easy to use tool that makes a ton of information available. We need a <b><i>very easy</i></b> way to deploy this. BGP is actually a pretty simple protocol to make work, which is why is hasn’t changed much in the  extremely long tenure it has had as foundation of the internet. We need a very, very straightforward way to get the non-technical pieces done.
</div>

<div>
</div>

**Disclaimer:**

This is just the tip of the iceberg and I am but a novice with this tech &#8211; but my gut feelings are typically right about this type of thing.

<div>
</div>

<div>
  * &#8220;Good enough” is almost never good enough.
</div>

<div>
</div>

<div>
  <h6>
    Image created from SURFNet RPKI page.
  </h6>
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1351" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1351" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1351" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1351" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
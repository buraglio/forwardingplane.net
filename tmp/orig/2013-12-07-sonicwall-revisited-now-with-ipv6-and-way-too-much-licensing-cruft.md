About a year ago [I did a brief review of the &#8220;new Sonicwall&#8221;](http://www.forwardingplane.net/2012/12/sonicwall-old-dog-learns-some-new-tricks/ "Sonicwall – Old dog learns [some] new tricks"), specifically a smaller branch office device that was said should have had all of the features of the larger devices.  I proposed that it had some significant limitations (much to the disagreement of a great deal of folks).  However, I stand by my statements.  If you ignore the fact that firewalls often cause more problems than they solve, that NAT is a nightmarish kludge (and not a security mechanism), and [will likely be phased out for better options eventually](http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/ "Why hardware firewalls are the walking dead"), the SonicOS I tested was pretty limited as far as what I believe should be features.

Let&#8217;s be clear, I&#8217;m mostly talking about IPv6.  I&#8217;ve ranted and raved that anyone not doing IPv6 is already years behind.  Get on the ball, you&#8217;re already late to the game.  Yesterday, a colleague said something that resonated with me regarding this and it got me thinking about how much IPv6 support SonicOS had added.  Many folks that aren&#8217;t doing IPv6 think that instead of doing something that may be a little hard that they&#8217;re just not going to do anything.   They&#8217;re dead wrong.  They&#8217;re forcing themselves to do something else like CGN or multi-layer NAT, or something else equally (or more) unpleasant.  And then they&#8217;ll do IPv6 anyway after that. It **is** inevitable. 

But I digress….

I pulled my old TZ-210 out and upgraded it to SonicOS Enhanced 5.9.0.2-107o.  What a pleasant surprise!  A **huge** amount of IPv6 support added!  [<img class=" wp-image-840 alignright" alt="sonicwall-v6-v4" src="http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4.png" width="551" height="50" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4.png 1134w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4-300x27.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4-1024x93.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4-550x50.png 550w" sizes="(max-width: 551px) 100vw, 551px" />](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-v4.png)

They&#8217;ve really done their homework here.  I was very surprised to see things like DHCPv6-PD with interface tracking.  Well done, Dell.  This will allow for small and home offices to take advantage of the Comcast and AT&T DHCPv6-PD that they&#8217;ve been offering for a while now, and lets be honest, once it&#8217;s on, most folks will never even realize they&#8217;re using IPv6.

[<img class="size-medium wp-image-836 alignleft" alt="sonicwall-dhcpv6" src="http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6-257x300.png" width="257" height="300" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6-257x300.png 257w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6-880x1024.png 880w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6-550x639.png 550w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6.png 1200w" sizes="(max-width: 257px) 100vw, 257px" />](http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-dhcpv6.png)

<== This is a giant step forward for reasons that are far beyond simple protocol support.

&nbsp;

<img class="wp-image-839 alignright" alt="sonicwall-v6-fw-rules" src="http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-fw-rules.png" width="537" height="216" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-fw-rules.png 3332w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-fw-rules-300x120.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-fw-rules-1024x410.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/12/sonicwall-v6-fw-rules-550x220.png 550w" sizes="(max-width: 537px) 100vw, 537px" /> 

&nbsp;

I&#8217;m very happy to see this level of support from Dell/Sonicwall.  I expected to put this box in, turn it on, use it for a few days and turn it off.  I set it up in transparent mode, tuned the rules a bit….and I have no real plans of taking it out.  I&#8217;m actually pretty happy with it for the application I&#8217;m using it for.  It doesn&#8217;t seem to really impede anything I want to do (after TCP ssh timeout rules to a reasonable time; BTW, timeouts are one of the reasons I don&#8217;t like firewalls).

&nbsp;

&nbsp;

This brings me to my problem with Sonicwall (and many network and network security vendors).  My licenses have all expired.

I can understand having to license services that cost money because they&#8217;re licensed upstream services.  I get that, I really do.  However,  Some of the things that Dell requires licenses for seem a bit extreme to me.  The fact that I get essentially zero visualization options once the licenses expire is downright shameful.  No worries, I&#8217;ll just export Netflow/IPFIX data.  Nope, also a licensed feature.  You heard that right.  No flow export, no real time monitor.  Heck, I can&#8217;t even look at interface graphs on-box. I have to poll with a 3rd party tool suite.  Realistically, one gets significantly better instrumentation from a default <a href="http://www.pfsense.org" target="_blank">pfSense</a> load.  And pfSense has had IPv6 support for years.

If you take away all of the downright shameful licensing requirements to do anything useful with trending and instrumentation, this is a good platform. Their IPv6 support is solid now.   However, for anyone running  networks  that require instrumentation and visualization, you had better budget for [unnecessary] fees or have 3rd party mechanisms for collecting the data.

&nbsp;

&nbsp;

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-835" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-835" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-835" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-835" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/12/sonicwall-revisited-now-with-ipv6-and-way-too-much-licensing-cruft/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

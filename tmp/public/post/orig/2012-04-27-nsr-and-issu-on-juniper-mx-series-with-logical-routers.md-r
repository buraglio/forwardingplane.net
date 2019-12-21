Lets just say, for instance, that you have an MX series router at somewhere on your network. Lets also say that said router is carved into more than just the main logical system. For the sake of this writing, lets say that your eBGP sessions are in the default logical system and your IGP is in the logical system, lets call it &#8220;internal&#8221;.  
 JunOS has some wonderful mechanisms for keeping things running, one is called [NSR](http://www.juniper.net/techpubs/en_US/junos9.5/information-products/topic-collections/swconfig-high-availability/nsr-overview.html) (Non Stop Routing), the other is called ISSU (In Service Software Upgrade). Typically these are really, really useful for performing non-impacting RE fail overs and software upgrades. Heck, I&#8217;ve upgraded an MX960 in the middle of the day with no impact whatsoever. Thats right, I was that guy. It should be noted, that the MX960s in question didn&#8217;t have any logical systems configured, which brings us to why I jotted this down into this web page.

Now, it&#8217;s no secret that I am a fan of Juniper gear, and [I&#8217;ve talked about this before](http://tech.buraglio.com/2010/12/junos-issu.html). But frankly, our MX series that have logical systems need upgraded so infrequently, I actually forgot about this little tidbit.  For whatever reason, it really surprised me during the last upgrade I did even though it makes perfect sense and I knew about it already. What that time comes that you need to upgrade JunOS, you&#8217;ll have to keep one very important thing in mind:

**You can&#8217;t take advantage of NSR in any logical system that isn&#8217;t the default. **

****Additionally, You can&#8217;t choose the protocol or the logical system that NSR works on, it&#8217;s on for all protocols on the default logical system if you enable it. 

What does this actually mean?  Well, it means that if I do an ISSU (which you should still do even with logical systems), anything outside of my default logical system will re-converge.  If my eBGP sessions are outside, they&#8217;ll drop and have to re-establish.  This isn&#8217;t really that great of an idea if you peer with folks that keep dampen-happy.  Personally, I don;t like my BGP sessions to drop if they don&#8217;t need to.  I&#8217;d rather deal with an IGP adjacency change than a bunch of BGP sessions having to re-establish and churn through potentially a handful of full tables. 

How do we get around the interruption this causes?  Well, the way we&#8217;ve solved it is to have 2 MX480&#8217;s connected redundantly.  That way, even if ISSU is going to cause an interruption due to a peering or adjacency change, the alternate path still exists.  Why do we have this setup?  Well, ideally we&#8217;d have 4 MX480s and wouldn&#8217;t need the logical systems, but hey, they&#8217;re expensive. 

So, what it the take away from this episode of &#8220;as the packet turns&#8221;? 

If you must configure logical systems, know that NSR and ISSU doesn&#8217;t really work as you may think in the non default.  Plan for some interruption, adjacency changes and or BGP sessions to drop. 

Or buy more routers.

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-23" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-23" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-23" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-23" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/04/nsr-and-issu-on-juniper-mx-series-with-logical-routers/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
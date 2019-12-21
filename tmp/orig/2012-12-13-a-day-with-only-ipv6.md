IPv6 is coming.  Like SDN, we can&#8217;t ignore it.  Are you ready?  Are you apps ready?  I&#8217;ll wager the answer is no.  Mine aren&#8217;t.  I&#8217;ve been working on IPv6 for about 11 years, from early days of tunnels to full native IPv6 at home and at work.  In teaching the IPv6 workshop for internet2, one of the things that I always suggest is to have a dual stacked host and an IPv6 only host available for testing.  These can be virtual machines or physical host, the important detail is that that need to be something that is deployed and a known working configuration. Ideally they&#8217;re a mirror or an analog of a typical workstation and or server on your network.

I&#8217;ve been doing this for some time, but I must admit I&#8217;m a little ashamed that I&#8217;ve never tried to do this for my personal day to day workstation, only for one off testing.  Well, that ends now, and the results aren&#8217;t pretty.

[<img class="aligncenter size-full wp-image-258" title="noipv4" src="http://www.forwardingplane.net/wp-content/uploads/2012/12/noipv42.png" alt="" width="431" height="230" srcset="http://www.forwardingplane.net/wp-content/uploads/2012/12/noipv42.png 431w, http://www.forwardingplane.net/wp-content/uploads/2012/12/noipv42-300x160.png 300w" sizes="(max-width: 431px) 100vw, 431px" />](http://www.forwardingplane.net/wp-content/uploads/2012/12/noipv42.png)

<p style="text-align: center;">
  <p>
    My every day workstation is a mac. So, to remain productive, I didn&#8217;t use my primary workstation, but instead I attempted to mirror it as closely as possible.  The chosen analog was a mac mini running MacOS 10.7.  It was immediately clear that this wasn&#8217;t going to be a fully functional workstation.
  </p>
  
  <p>
    Right from the get go there was an issue.  IPv6 doesn&#8217;t do any options in the SLACC implementation that 90% of folks doing dual stack are going to use.  DHCPv6 is still not widely deployed, DHCPv6 relay isn&#8217;t available in a vast swath of network hardware and most folks are going to initially start with stateless auto config, at least until they realize it&#8217;s more or less unmanageable.  Translated: you have no DNS without explicitly setting it statically.
  </p>
  
  <p>
    Yuck.  I strongly discourage statically assigning things.  It makes changes far more painful than they need to be, is a support nightmare at nearly any scale  and decentralizes control. However, I had to for this test.  Fine, an IPv6 resolver was added.
  </p>
  
  <p>
    Next step, run patching.  Nope.  Apple doesn&#8217;t support patching via their automated process via IPv6.  Most of this should be served by Akamai, which does support v6 in many cases, but not this one.  I can&#8217;t even patch the workstation without either running my own IPv6 enabled patch service (which requires manual configuration of a host to utilize), using a thumb drive or IPv6 enabled network mapping to grab the patches or plumbing IPv4 into it.
  </p>
  
  <p>
    After fighting through patching the host, I wanted to actually use it.  This was mostly an exercise in patience as well.  The google based services I used all just worked.  Searches, gmail, blogger, etc.  I didn&#8217;t notice any difference whatsoever. One interesting thing that I noticed right away was that many ads and images on pages I was able to surf to weren&#8217;t working at all.  Ad content providers are behind the curve on delivering over IPv6.  This surprised me a bit since this is a revenue stream that is going to grow, and they&#8217;re missing the boat.  The upside was that I didn&#8217;t need to look at a bunch of ads, potentially distracting images and marketing hype.
  </p>
  
  <p>
    Many of my work services such as exchange aren&#8217;t yet IPv6 enabled, I knew that wasn&#8217;t going to work because it&#8217;s actually on my teams list to remedy, however, I gave it a try anyway.  No go on OWA.  No go on any of the exchange access whatsoever.  NTP sync worked just fine after adding in our NTP server, its been IPv6 ready for a very long time.
  </p>
  
  <p>
    Luckily for me, most of what I do is CLI based and the equipment I need to get into and help maintain has been IPv6 enabled for years.  SSH on this mac worked with absolutely no issues, as expected.  It&#8217;s one of those nice things that I&#8217;d been using IPv6 for in a dual stacked environment for years and is essentially transparent.
  </p>
  
  <p>
    I was able to work on this blog post, since<a href="http://www.forwardingplane.net"> forwardingplane.net</a> has been IPv6 compliant since it&#8217;s inception thanks to the hosting provider, <a href="http://www.arpnetworks.com">arp networks</a>.
  </p>
  
  <p>
    Other services that I use regularly, are a mixed bag.  <a href="http://www.box.net">Box.net</a> has no IPv6 support. <a href="http://www.dropbox.com">Dropbox</a>, which I expected to work since it is hosted in the amazon cloud, doesn&#8217;t but probably trivially could.  <a href="https://spideroak.com">Spideroak</a> didn&#8217;t work with only IPv6.  <a href="http://www.crashplan.com">Crashplan</a> didn&#8217;t work to the cloud or my NAS.  NAS was expected since it doesn&#8217;t do v6.  This is a frightening wake-up call.  Enabling IPv6 support into these every day apps should have been done from the beginning or at the very least before IPv6 day.
  </p>
  
  <p>
    Some other things I noticed, my <a href="http://www.amazon.com/D-Link-DNS-343-Network-Attached-Enclosure/dp/B0019VSU88">2 NAS</a> at home don&#8217;t do IPv6 at all.  The aging Dell powerconnect gig switch I have at home doesn&#8217;t do IPv6.  My <a href="http://o-www.sonicwall.com/us/en/products/TZ_210.html">Sonicwall TZ 210 wireless-N</a> that I&#8217;ve been testing at home has no IPv6 support by default although I think there is Beta code that I&#8217;ve been trying to get my hands on.
  </p>
  
  <p>
    My appleTV, however, does do IPv6 as do my Linux VMs, Windows 7 VM and host Linux system.  My normal gateway device, a <a href="http://www.pfsense.org">pfSense</a> install running on a <a href="http://pcengines.ch/alix.htm">PC Engines ALIX</a> board has done IPv6, correctly mind you, for years, either by code I hacked into it (in the early days) or fully supported by the project.  It supports dhcpv6 server, dhcpv6-pd from my upstream provider and SLAAC.  It also does IPv6 firewall functions better than most commercial firewall devices.
  </p>
  
  <p>
    I&#8217;m 100% sure it&#8217;s just the tip of the iceberg. If you&#8217;re a networking professional and you&#8217;re not learning IPv6, you&#8217;re already 10 years behind.  Head in the sand won&#8217;t make it go away, it&#8217;s happening, just like SDN is happening.  In fact, they&#8217;ll <a href="http://www.openflow.org/wk/index.php/OpenFlow_1_2_proposal#IPv6_support">be happening together in some cases</a>.  Learning new things is fun, and IPv6 is a necessity.  You can hide behind NAT and existing allocations for a while, but believe me, you&#8217;re doing yourself a disservice as well as missing out on some cool stuff if you&#8217;re not talking about your IPv6 plans and learning about this inevitable reality.
  </p>
  
  <div class="sharedaddy sd-sharing-enabled">
    <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
      <h3 class="sd-title">
        Share this:
      </h3>
      
      <div class="sd-content">
        <ul>
          <li class="share-twitter">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-172" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
          </li>
          <li class="share-email">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
          </li>
          <li class="share-print">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/" target="_blank" title="Click to print"><span>Print</span></a>
          </li>
          <li class="share-linkedin">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-172" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
          </li>
          <li class="share-facebook">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-172" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
          </li>
          <li class="share-reddit">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
          </li>
          <li class="share-tumblr">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
          </li>
          <li class="share-pinterest">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-172" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
          </li>
          <li class="share-pocket">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/12/a-day-with-only-ipv6/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
          </li>
          <li class="share-end">
          </li>
        </ul>
      </div>
    </div>
  </div>

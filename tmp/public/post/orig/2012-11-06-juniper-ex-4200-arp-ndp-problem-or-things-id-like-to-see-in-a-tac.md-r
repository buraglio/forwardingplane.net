    Recently we&#8217;ve run into an odd issue while routing on an EX4200 series.  These little JunOS boxes are a nice alternative for an entry level building router, they support L2/L3 functionality, a PVST+-ish protocol and, with advanced licensing, IPv6, ISIS and BGP. They have multi 10G interface options and come in a pluggable fiber option.  We use them all over for light layer 3.  They can also be stacked via stacking cables and fiber, which is very handy and makes them extremely versatile but not really applicable for the purpose of this entry.  Anyway, one of our buildings had some odd issues that popped up from time to time, normally over the course of several months.  How is manifests itself is an apparent corrupted ARP / NDP table.  Clearing both fixed their respective traffic&#8230;.for a while.  While this problem in and of itself is moderately interesting, the real issue arose when, after an extensive JTAC experience, I couldn&#8217;t find any reference to the PR that they said was causing this issue (slow memory leak). PR664807.  Even looking through the <a href="http://www.juniper.net/techpubs/en_US/junos10.4/information-products/topic-collections/release-notes/10.4/index.html?topic-51158.html" target="_blank">techpub notes for the JunOS version 10.4R3</a>, I can&#8217;t find any reference to this PR.

    What I did find was multi-facited.  Either the JTAC engineer was just incorrect and mistyped, or the site is not efficiently relaying information. 

    It&#8217;s no secret that I&#8217;m hyper-critical of support engineers.  I don&#8217;t call any TAC very often, if anyone in my group calls a TAC, it&#8217;s an &#8220;oh sh!t&#8221; moment or we&#8217;ve exhausted all other resources.  We take a lot of pride, myself included, in being good at our jobs.  That being said, lets give the benefit of the doubt and make an assumption that the JTAC engineer gave us the correct PR. 

    The PR search that jtac offers is pretty awful.  It&#8217;s hard to find, can&#8217;t seem to find known PRs and is generally clunky and yuckie.  In their defense, most TAC KBs are not good.  However, and try doing a google search for this and you&#8217;ll find links to <https://www.juniper.net/prsearch/simplesearch.jsp>, which doesn&#8217;t work.  You&#8217;ll also find a lot of reference to that URL when searching the JTAC KB, as noted <a href="http://kb.juniper.net/InfoCenter/index?page=content&#038;id=KB17924&#038;actp=search&#038;viewlocale=en_US&#038;searchid=1352170024537" target="_blank">here</a> under the heading &#8220;<span style="background-color: white;"><span style="font-family: inherit;">Where can I search known Junos bugs?&#8221;</span></span>. 

    I&#8217;m going to make a [giant] assumption that this is **not** user error on my part. ** ** This is a problem that needs fixed.  I&#8217;m into making lists lately, so here is another one:

Things I would like to see in a TAC



  * Competent first level engineers.  
  * Know when to escalate, there is no shame in asking for help. 

  * Engineers that have at least some **soft** skills. 
  * People skills are nearly as important as tech chops, especially in a TAC

  * Efficient troubleshooting process.
  * This can be taught, come on guys, get to it.

  * A decent knowledge base.
  * Quit moving crap around or make the old links forward, this is web programming 101
  * Make searches work easily
  * Allow for multi-faceted searches

  * STOP ASKING FOR INFORMATION YOU ALREADY HAVE
  * We sent in the &#8220;show tech&#8221;, &#8220;request support info&#8221;, etc.  It&#8217;s in the file.  If it&#8217;s not a P1 case, read the freaking notes.  

  * Make sure you follow up with the next engineer.
  * We understand shifts change, please make sure hand off of cases is done correctly

<div>
</div>

<div>
  These would seem like easy things to accomplish, and I have seen them in the past, but they aren&#8217;t the norm.  They should be. 
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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-10" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-10" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-10" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-10" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
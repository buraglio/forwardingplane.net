There has been a lot of buzz about the service provider model, <a href="http://en.wikipedia.org/wiki/Net_neutrality" target="_blank">net neutrality</a> and tiered access for consumers in the past few years.  Just this week <a href="http://www.theverge.com/2013/1/19/3894182/french-isp-orange-says-google-pays-to-send-traffic" target="_blank">Google has been accused of paying Orange</a> (more likely Orange is forcing google) for handling its traffic.  This is a VERY slippery slope that teeters on the edge of what we all want to avoid as consumers or content creators.

This recent story has sparked something I&#8217;ve been thinking about for a very long time.

Rewind to 1999.

I worked for a small, regional broadband provider what seems like a lifetime ago, back when broadband was new and shiny and not terribly common.  We provided ATM based DSL, T1, ISDN and on some occasions dry copper gorilla net access to southern Chicago communities, Champaign-Urbana, IL, Danville, IL, Kankakee, IL,  a bit of west Indiana and a handful of small communities in between.  It was a proving ground for a young, motivated networking guy.  I was the senior network engineer, technical lead and for a while had a handful of direct report employees and students. This was where I really cut my teeth with routing, switching, content delivery and service levels.

I ended up leaving there and moving on to work on a lot of HPC work and bleeding edge WAN stuff (think n x 10Gbps across the country in 2003).  However, one thing I took away from that ISP job was something that wasn&#8217;t really a new idea as much as just a uniquely positioned service and a good idea.  There was this local POP connection run by the university that allowed for exchange of  routes between any network that could pay the local loop charge.  It was a way to get cheap, fast access to anything local.  Unmetered, unfiltered.  Exchange any routes you want (that you own), take whatever routes you need.

This was a clever model because down where we are located, 2.5 hours south of Chicago, transit bandwidth wasn&#8217;t (and isn&#8217;t) cheap.  Every local provider connected as did the community hospital, the university and a handful of others.  We took FULL advantage of fast connectivity between each other and all saved on transit bandwidth.  <a href="http://en.wikipedia.org/wiki/National_research_and_education_network" target="_blank">This kind of thing has been in place in the R&E</a> community for far longer than I&#8217;ve been around.

Fast forward 11 years.

I&#8217;m still a huge fan of bi-lateral BGP peerings.  I want as many as I can get.  As a service provider I want a default free network with a lot of peers in many geographically diverse locations.

I propose a [not-so]new model for service providers.  Create peering points, meet me routers.  Allow any network to connect for a port fee and exchange local routes.  Make these local routes free, unlimited and unfiltered (do your proper capacity planning, of course).  Opening up exchanges promotes better, diverse paths to resources and allows for a better overall user experience.

Data is where the telecom companies make their money nowadays.  Net Neutrality is constantly in the news and in danger of being compromised.  Tiered services are everywhere.  I understand the need to meter service.  I did the ISP thing, I know that 5% of the users use 80% of the bandwidth.  That&#8217;s not new either.  I challenge larger service providers to think about it in a new way, though.  We&#8217;re making it work.  It&#8217;s a smaller scale, but it works.  I think it can scale if architected correctly.  It may have more operational overhead, but I suspect it can also command a bit more in price.  It could also allow for the non-asterisked use of the word &#8220;unlimited&#8221;, so marketing guys will love it.

<div>
  Is it more engineering? Sure.  Is it harder to manage? Maybe, but likely not harder than architecting around content providers that don&#8217;t want to pay.  It is a better idea and promoting better service for both content providers and consumers of their service than making content providers pay for transit?  Absolutely.
</div>

We&#8217;re doing this on <a href="http://uc2b.net" target="_blank">UC2B</a>. It played a part in winning us the <a href="http://www.natoa.org/2012/09/natoa-announces-recipients-of-4.html" target="_blank">Community Broadband Project of the Year award from the NATOA</a>.  It&#8217;s a good idea.

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-330" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-330" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-330" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-330" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/01/alternate-model-for-sp-networks/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

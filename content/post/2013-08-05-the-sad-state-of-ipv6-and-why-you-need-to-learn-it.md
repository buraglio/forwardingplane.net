I have been learning and using IPv6 for a quite a while, even before I worked in research and education, back in the ISP days.  I thought I should learn it because, frankly, I figured we&#8217;d all be converted to it by now, already whole hog using it like it was the layer 3 addressing mechanism that it is.  Flashback: My first IPv6 access was via a tunnel to HE a long, long time ago and before that I was reading what I could about it.  I&#8217;ve been evangelizing IPv6 for about that long, too.  I&#8217;ve taught IPv6 networking workshops on many occasions showing eager network engineers, security engineers, sysadmins, incident responders and even the occasional CIO how to understand, interpret and plumb v6.

Now, I love OpenFlow and SDN as much as the next network geek, and I think it&#8217;s about as disruptive and game changing as the next guy.  However, IPv6 is next.  There.  I said it.  We need it.  Hey, OpenFlow 1.3 supports it so there is your tie in.  We&#8217;re out of v4 for the most part and, lets be honest, NAT is a freaking abomination. It&#8217;s not a solution to anything other than over complicating a transit path with translational mappings.

I recently received an email from a buddy from my first days in tech about <a href="http://www.enhancedip.org/home" target="_blank">a project that some colleagues of his had been working on</a> and while at a base technical level it&#8217;s an interesting concept, this project infuriated me.  This is the problem with the industry, especially in North America.  
The right thing, in my opinion, is to put effort like this aside and concentrate on IPv6 development and deployment. Projects like this, while good intentioned and technically innovative, delay he inevitable and give lazy, &#8220;luddist&#8221; engineers and developers a way to keep ipv4 even longer. [<img class="alignright size-full wp-image-751" alt="alarm_clock" src="http://www.forwardingplane.net/wp-content/uploads/2013/08/alarm_clock.jpg" width="300" height="200" />](http://www.forwardingplane.net/wp-content/uploads/2013/08/alarm_clock.jpg)

I have mostly just kept this to myself publicly.  Sure, I blather on about it the office and preach about IPv6 over beers with networking professionals, but mostly I just suffer and bite my tongue when I hear some enterprise architect talk about firewalls, NAT, IPv4 only security appliances and how &#8220;they don&#8217;t need IPv6&#8221; or how &#8220;the enterprise isn&#8217;t ready&#8221; [for IPv6].

Wake up call, you&#8217;re late. **IPv6 is here**.  It&#8217;s **been** here.  It&#8217;s all over in Asia and other parts of the world.  It&#8217;s supported by default by your consumer service provider.  Guess what?  It&#8217;s too bad that your lazy developers didn&#8217;t code your apps for it. It&#8217;s too bad that your specialized app only supports IPv4 and probably doesn&#8217;t even understand DNS.  You&#8217;ll eventually have to deal with IPv6.  In actuality, you&#8217;re likely already using it and have no idea it is happening.  If someone finally tore that legacy XP machine from your change-despising hands you&#8217;re probably tunneling your traffic.  Unless you explicitly disable IPv6 on a modern operating system, you&#8217;re using it.  It may be just locally on your segment, but it&#8217;s on.  [<img class="alignleft  wp-image-753" alt="borg" src="http://www.forwardingplane.net/wp-content/uploads/2013/08/borg.jpg" width="285" height="189" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/08/borg.jpg 475w, http://www.forwardingplane.net/wp-content/uploads/2013/08/borg-300x198.jpg 300w" sizes="(max-width: 285px) 100vw, 285px" />](http://www.forwardingplane.net/wp-content/uploads/2013/08/borg.jpg) Get on board.  Resistance is futile.  There are great resources for learning IPv6.  Your desktop and server OS have probably supported it for years.  Your routers likely support routing it.  The last parts are going to be the security devices, policy and the legacy apps.  If you&#8217;re a networking guy, go do the <a href="http://ipv6.he.net/certification/" target="_blank">HE tunnelbroker certification process. </a> They have a very good fundamentals tutorial and it covers everything you need to know to get started.  You can also get a cool shirt and some code to shove into your website.  Mine looks like this:

&nbsp;

Take the plunge, get some IPv6 going in your enterprise, home network, lab, whatever.  Learn and educate.  It will only improve your value and you&#8217;re going to have to learn it later anyway.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-724" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-724" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-724" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-724" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/08/the-sad-state-of-ipv6-and-why-you-need-to-learn-it/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

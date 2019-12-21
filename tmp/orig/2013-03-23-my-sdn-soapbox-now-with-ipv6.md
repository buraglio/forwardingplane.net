This week there was a lot of buzz about SDN (as usual). There was a<a href="http://www.lightreading.com/blog/software-defined-networking/sdns-killer-app-more-network-control/240151376" target="_blank"> lightreading thread that I commented on</a> and a fantastic read by <a href="http://www.twitter.com/networkstatic" target="_blank">Brent Salisbury</a> about <a href="http://networkstatic.net/be-the-steamroller-not-the-road/" target="_blank">being the steamroller and not the road</a> that got me thinking about OpenFlow and SDN in a way I had not before.

[<img class="alignright size-full wp-image-550" alt="fearofchange" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/fearofchange.jpg" width="339" height="500" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/fearofchange.jpg 339w, http://www.forwardingplane.net/wp-content/uploads/2013/03/fearofchange-203x300.jpg 203w" sizes="(max-width: 339px) 100vw, 339px" />](http://www.forwardingplane.net/wp-content/uploads/2013/03/fearofchange.jpg)

<soapbox>

All that is old is new again. I remember when internal networks were small and routing protocols were taboo in many internal environments. RIP (AKA routing by rumor) was about as innovative as we got, OSPF was &#8220;too complex&#8221; and was &#8220;software changing the network topology&#8221;, according to some folks I worked with in what seems like a lifetime ago. Clearly they didn&#8217;t have the entire picture and were clouded by FUD. Now using a link state protocol is a standard and one would probably not consider building a complex, production layer 3 network without an IGP like ISIS or OSPFv\[2/3\] (or even EIGRP&#8230;I guess).

This is simple evolution and progression. The more folks try to resist, the further behind they&#8217;ll be left.

SDN and OpenFlow are not unlike IPv6 in many ways when viewed from a technology implementation perspective, and in fact, we can probably learn from the resistance to IPv6 to help us with the acceptance of SDN and OpenFlow. V6 has been coming for years. It&#8217;s _mostly_ here. Backbones have been running it for a very long time and we actually **need** it on the client side to account for the huge number of hosts now connecting to the public Internet.

Many entities, especially very risk averse enterprises, are struggling to resist it (IPv6) and hold onto NAT and IPv4 as long as possible.  While this will almost certainly buy them a handful of years, it&#8217;s futile.  Translation and transition tech geared toward the folks that refuse to adapt will allow them to grasp onto legacy methodologies for a bit longer, but as the Borg say, &#8220;resistance is futile&#8221;.

[<img class="alignleft size-medium wp-image-557" alt="Borg" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg-300x274.jpg" width="300" height="274" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg-300x274.jpg 300w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg-550x502.jpg 550w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg.jpg 1000w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.forwardingplane.net/wp-content/uploads/2013/03/Borg.jpg)

These same things are all going to happen with SDN.

What we say is &#8220;OpenFlow is simply an open protocol for creating flow based forwarding.  It allows for the inclusion of other factors such as Layer4 to make those decisions more tunable and granular.&#8221;

What skeptics hear is &#8220;There is a hole in the boat, we&#8217;re all going to die&#8221; or &#8220;Network Engineers are all going to be out of a job!&#8221; or &#8220;your job is going to be replaced by software&#8221; or even &#8220;software and applications will make the way we think about and do everything obsolete&#8221;, all of which translate to &#8220;dramatic and drastic change&#8221;.

Most of this is just sensationalism and FUD. In my opinion, though, it is all based in truth .  It may be &#8220;drastic&#8221; but it&#8217;s not dramatic.  It&#8217;s natural evolution.  It will happen slowly.  We will have to change they way we do things. The proven fact we as networking and security professionals need to remember is that change going to happen with or without SDN, it&#8217;s the nature of an innovative field like technology to change.  None of us would be doing what we do without being inquisitive enough to figure out problems, challenge norms and shift thinking.

SDN, just like IPv6, is happening.  Personally I&#8217;d rather be knowledgeable about as opposed to in the dark and scrambling to learn about them at the 11th hour.<em id="__mceDel"> </em>

</soapbox>

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-547" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-547" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-547" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-547" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

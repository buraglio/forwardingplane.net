I&#8217;ve been doing a lot of MPLS in the last 45 or so days (which is one of the reasons I have been absentee in the OpenFlow world lately). Having had almost no real world MPLS experience aside from a handful of pseudo-wires and a very small LDP signaled network, I had to spend some time reading, hacking at routers and essentially learning. In doing so, I found a few things.

  * MPLS isn&#8217;t that different than any other networking, it&#8217;s taking a criteria and moving data based on that criteria (duh?!?)
  * Many of the concepts are familiar.  Frame Relay and ATM come to mind.  OpenFlow does as well in certain circumstances.
  * There is a lot of documentation on the MPLS suite of protocols.
  * I didn&#8217;t find a condensed set of data for the information I was looking for.  Jerely Stretch has some of it on his <a href="http://media.packetlife.net/media/library/18/Frame_Mode_MPLS.pdf" target="_blank">cheat sheet</a>, but it&#8217;s not as complete as what I wanted and heavily vendor biased.  I was looking for conceptual information and not necessarily operational commands.

[<img class="alignright size-full wp-image-670" alt="Basic Cloud" src="http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg" width="366" height="392" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg 533w, http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud-280x300.jpg 280w" sizes="(max-width: 366px) 100vw, 366px" />](http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg)

I spent some time coming up with a slide deck I could present to others that, in theory, would build a foundation to work from.  I understand that this may be incomplete and is mostly a compilation of data found elsewhere (there is a reference section).  Using this bootstrap I was able to pick up the concepts well enough to understand when to use what and where as well as build the foundational requirements for a fairly complex MPLS environment.  Feel free to correct anything that is blatantly wrong, send me an email and I&#8217;ll address it.

The slide deck can be found as a PDF <a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/MPLS-101.pdf" target="_blank">here</a>.  If you want the pptx it is available <a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/MPLS-101.pptx" target="_blank">here</a>.   I will continue to update them as I hone the deck and / or find and correct errors.

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-650" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-650" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-650" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-650" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/06/mpls-bootstrap/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
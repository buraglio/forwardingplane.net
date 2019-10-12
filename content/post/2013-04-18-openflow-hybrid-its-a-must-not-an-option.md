OpenFlow is, of course, a hot buzzword.  It&#8217;s the newest, and in my opinion, the most innovative thing to hit data networking since dynamic routing.  The ability to programmatically, systematically and potentially dynamically control traffic at the flow level through a network is innovative, exciting and terrifying [to many network engineers and architects] at the same time.  Allowing applications to touch the network change behavior is something that many engineers are not terribly comfortable with.  I will even admit that a few years ago I was pretty tentative about software changing network hardware.  <a title="Black Hole routing" href="http://www.forwardingplane.net/2011/10/black-hole-routing/" target="_blank">Building a Blackhole router</a> was an easy way for me to acquaint myself with this and get comfortable with software changing things without human interaction.   Most of my discomfort with this process was the fact that I&#8217;m not a good developer.  I can hack scripts and read most basic code in Shell, C, Perl, Python and Ruby but I don&#8217;t actively do anything but an occasional script or <a title="VDXrancid contrib scripts" href="http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/" target="_blank">hack</a> <a title="alurancid and pfrancid" href="http://www.forwardingplane.net/2011/06/alurancid-and-pfrancid/" target="_blank">to</a> <a title="Alcatel Lucent RANCID scripts" href="http://www.forwardingplane.net/2010/12/alcatel-lucent-rancid-scripts/" target="_blank">existing projects</a>.

[<img class="size-medium wp-image-592 alignright" alt="Enterprise Network" src="http://www.forwardingplane.net/wp-content/uploads/2013/04/Enterprise-Network-265x300.jpg" width="265" height="300" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/04/Enterprise-Network-265x300.jpg 265w, http://www.forwardingplane.net/wp-content/uploads/2013/04/Enterprise-Network-550x621.jpg 550w, http://www.forwardingplane.net/wp-content/uploads/2013/04/Enterprise-Network.jpg 606w" sizes="(max-width: 265px) 100vw, 265px" />](http://www.forwardingplane.net/wp-content/uploads/2013/04/Enterprise-Network.jpg)Conversely, we&#8217;re all pretty comfortable with networks as they exist today.  The typical &#8220;enterprise pyramid&#8221; is best practice and works very well.  Good physical design is good physical design.  However, where this, and any other network gets hairy is when it scales to hyper scale or the operations team is thin.

Here is where things get interesting.  Call it what you want, SDN is changing the way we as networking professionals think about this support model.  Remember managing fat wireless access points?  It became unruly and impossible at scale and once wireless ceased to be a convenience network it was nearly impossible.  Enter wireless controllers and thin access points.  5-7 years later this is now the standard.  The differences, though, is that wireless was still a relatively small footprint comparatively speaking and it wasn&#8217;t a critical infrastructure before those changes had to happen.

The problem that we face now is that we have critical infrastructure and legacy support mechanisms.  It is unreasonable to think that we&#8217;ll be ripping out a traditional, functional network and replacing it with a greenfield OpenFlow network, regardless of what the researchers and heavy proponents think.  Just like with the transitional mechanisms used in IPv6 deployments, there needs to be a transitional period where both traditional and OpenFlow networks can coexist.  There are a few options for this, but this is a problem that the <a href="http://networkstatic.net/hybrid-openflow-using-the-normal-action/" target="_blank">OFPP Normal action</a> can potentially solve.     <a href="https://openflow.stanford.edu/static/openflowj/releases/1.0.1/apidocs/org/openflow/protocol/OFPort.html#OFPP_NORMAL" target="_blank">OFPP Normal</a> will send a packet in the openflow pipeline to the native switching mechanisms for traditional forwarding, much like having a default route in an IGP handles anything without a more specific route.

Based on the <a href="http://www.openflow.org/documents/openflow-spec-v1.0.0.pdf" target="_blank">OpenFlow 1.0 spec</a>, an OpenFlow enabled switch is not required to support all actions, **may** support the NORMAL action.  I am here to say that my opinion is that this is something that has to happen.  It&#8217;s is reasonable to say that my understanding of OpenFlow is still evolving, but building networks is something I&#8217;ve been doing for 15 years.  Green fielding a totally OpenFlow network is almost certainly not going to happen in 95% of cases.  Backwards compatibility with existing networking is going to have to happen.

[<img class="alignleft size-full wp-image-594" alt="tantrum" src="http://www.forwardingplane.net/wp-content/uploads/2013/04/tantrum.jpg" width="200" height="183" />](http://www.forwardingplane.net/wp-content/uploads/2013/04/tantrum.jpg)As a case study, lets look at the adoption of IPv6.  We actually \*need\* IPv6.  Has adoption been smooth?  No.  Entities have been dragged into it kicking and screaming and tightly holding on to mechanisms like NAT as a way to delay the inevitable.  I could go on forever about how enterprises, service providers and any other network has caused more harm, pain and unnecessary expense than good by delaying IPv6 over and over&#8230;.but I digress.

We [mostly] don&#8217;t **need** OpenFlow yet.  Yes, it&#8217;s useful.  Yes, it has use cases that make a lot of sense.  Making it easy (read: painless) is the key to deployment.   My first reaction is that hybrid mode is the way to do this.  If your vendor doesn&#8217;t have a hybrid strategy, make them aware that they need one.

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-572" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-572" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-572" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-572" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/04/openflow-hybrid-its-a-must-not-an-option/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

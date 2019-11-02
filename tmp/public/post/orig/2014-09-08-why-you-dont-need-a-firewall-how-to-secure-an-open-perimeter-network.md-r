I admit that the title was meant to be inflammatory.  However, there are use cases that aren&#8217;t terribly uncommon where an in-line security appliance is just not the correct tool for the job.  Someone once told me &#8220;a firewall protects a network like a fuse protects an electrical circuit&#8221;, and it&#8217;s mostly a correct statement.

Firewall vendors will probably argue this and enterprise folks may discount this as heresy and call for burning me at the stake.  I can say, though, that the use of a firewall, IPS or other inline security appliance has presented many problems in many environments in my years as a network and security engineer and architect.    To that end, there are mechanisms for replacing the functions of a firewall and IPS with other options, which in many cases have a lower capital expense [although they may have a higher _initial_ operational expense].  I&#8217;ll outline them here, but before I do I want to re-iterate that NAT (PAT) is not a security tool, it&#8217;s a translation tool.  Nothing more.  So, I will leave that out.  If you don&#8217;t have appropriate IPv4 or IPv6 address space some of these things may need adjustments although they are still accomplishable by doing NAT on a border Layer 3 device.     Below is a talk that I gave at BroCon14 that is a rough outline of how to do this, if you don&#8217;t want to spend 30 minutes listening to me talk about it, the clifs notes are bulleted below, but the context is all in the video so I encourage you to watch it before responding to my post.

For those that want to take a look, here is the talk.



Here are the bullets.

  * **Announce only necessary resources **

<p style="padding-left: 60px;">
  One can utilize routing to only expose the pieces of the network that need to be exposed.  If you have a /16 and on;y a /24 needs to be exposed, only announce that prefix.  This is not that different than a typical DMZ.
</p>

  * **Filter access to network, storage and management hardware**

<p style="padding-left: 60px;">
  Utilize best practice ingress filtering.  Follow <a href="http://tools.ietf.org/html/bcp38" target="_blank">BCP38</a>. You should be doing this anyway.
</p>

  * **Utilize host based firewalls**

<p style="padding-left: 60px;">
  This is a no-brainer.  Firewall as close to the resource as possible.
</p>

  * **Employ central host management**

<p style="padding-left: 60px;">
  Make your life easy.  Cloud providers do it and it&#8217;s well documented nowadays.  There are <a href="http://cfengine.com/" target="_blank">many</a> <a href="http://puppetlabs.com/" target="_blank">options</a>.
</p>

  * **Centralize logging and flow data collection**

<p style="padding-left: 60px;">
  Another no brainer, you should be doing this anyway.
</p>

  * **Create baselines for traffic and activity**

<p style="padding-left: 60px;">
  Data is good.  Knowledge is power.  Baselines are useful for both anomaly detection and forecasting and it&#8217;s not that hard to do it.
</p>

  * **Deploy and tune IDS**

<p style="padding-left: 60px;">
  Passive IDS system[s] off of a TAP or SPAN are key to this kind of architecture.  See video for more details but there are a bunch of good options. I prefer <a href="http://www.bro.org" target="_blank">Bro IDS</a> but there are many players both commercial and FOSS.
</p>

  * **Filter with black hole routing**

<p style="padding-left: 60px;">
  I&#8217;ve<a title="Black Hole routing" href="http://www.forwardingplane.net/2011/10/black-hole-routing/" target="_blank"> talked about this before</a>.  Automating this is key to making it function efficiently and it is a fantastic tool.  This can be done with BGP (traditionally) or with something innovative like OpenFlow.
</p>

  * **Make use of regularly scheduled external vulnerability scanning**

<p style="padding-left: 60px;">
  This is a great way to verify your exposure and works for any sized network.  Highly recommended.
</p>

&nbsp;

Clearly this isn&#8217;t for everyone, and that&#8217;s ok.  For anyone that has struggled with issues involving security appliances either based on protocol, horsepower or interface speeds, there are options.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1051" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1051" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1051" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1051" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/09/why-you-dont-need-a-firewall-how-to-secure-an-open-perimeter-network/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
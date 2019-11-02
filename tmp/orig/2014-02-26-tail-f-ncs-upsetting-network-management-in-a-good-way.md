_“Hopefully there are some things here that will make you really upset in a very good way”_ is how <a href="https://twitter.com/cmoberg" target="_blank">Carl Moberg</a> of Swedish based company <a href="http://www.tail-f.com/" target="_blank">tail-f</a> opened up to the crowd at <a href="http://techfieldday.com/event/nfd7/" target="_blank">Networking Field Day 7</a> on <a href="http://techfieldday.com/appearance/tail-f-systems-presents-at-networking-field-day-7/" target="_blank">Feb 19, 2014</a>.  Tail-f is a sleeper, I had actually never heard of them before NFD7, but they&#8217;ve got a very unique product in <a href="http://www.tail-f.com/network-control-system/" target="_blank">NCS</a> and in my opinion it can change the way existing **and** future networks are managed.  Right now.  It&#8217;s not a platform that is green, unpolished or unfinished.  <a href="http://www.tail-f.com/network-control-system/" target="_blank">NCS</a> is in the ring and it brought its A-game.   Their site describes it better than I ever could:

_&#8220;Tail-f Network Control System, or NCS, enables network operators to manage all of their services and network devices with a single tool.&#8221; _A bold statement, and I tend to be pretty skeptical of such statements. However, I was really intrigued by the NCS platform and as I discovered, it is not hype. Watching the demo of this got my brain racing, it was exciting to think about all of the things it could simplify; I was excited about networking.  So many things In fact, I&#8217;m really just going to scratch the surface of what this software toolkit can tool.

> ## _&#8220;Any network of of ambitious size that needs to get people out of the loop”_

The CTO says that NCS is for &#8220;_Any network of of ambitious size that needs to get people out of the loop_”, and I tend to agree, which is what makes this so powerful. In a world of openflow this and sdn that, most of which is still under heavy development, I can&#8217;t help but think of NCS as a &#8220;rosetta stone&#8221; of network management tools. It’s a controller, but in a different way. Its not openflow, but it knows openflow, so it is looking forward, but it also supports everything that is already there, an absolute necessity for 95% of networks that are not greenfield. From the <a href="http://www.tail-f.com/network-control-system/#which-types-of" target="_blank">NCS FAQ</a>:

> ## _[<img class="alignleft size-full wp-image-920" alt="rose_lg" src="http://www.forwardingplane.net/wp-content/uploads/2014/02/rose_lg.jpg" width="237" height="300" />](http://www.forwardingplane.net/wp-content/uploads/2014/02/rose_lg.jpg)&#8220;Any device that can be remotely configured can be managed by NCS. This includes, routers, switches, load-balancers, firewalls, web servers and a whole host of other devices (both virtual and physical). Since it is not limited to one type of device or particular vendor, NCS allows for management of the entire network from a single pane of glass.&#8221;_

Lets face it, network management is not exactly easy to do in a sane and robust way, there are always quirks, one-offs and proprietary goo. That&#8217;s probably never going to change.  From the open source to the commercial, I&#8217;ve used, evaluated or extended a wide swath of them in my time in the industry, and this one really shocked me in what it was able to do in such a demonstrably elegant way, which we all know is not an easy task since we all have odd, uncommon or sometimes unreasonable requirements.

A few things are really compelling about NCS.  First, it&#8217;s all <a href="http://en.wikipedia.org/wiki/YANG" target="_blank">YANG</a>, meaning it is an established standard for doing exactly this and it can be referenced by any number of protocols for obtaining or setting the desired data or parameters.  This also means that it can very quickly and easily be extended to support new products, software loads, communications mechanisms and features.

Tail-F changed the way I was thinking about network management.  They&#8217;ve taken the religion out of equipment vendors, because you can choose how to interact with them.  They allow for management of a myriad of platforms from an operator-chosen, familiar CLI.  Have guys that like JunOS?  Great, no problem.  Team members that prefer IOS?  No worries.  They can manage the Alcatel-Lucent, Brocade, Extreme Networks or one of the many other CLI variants from their choice of IOS or JunOS-like command sets.   No longer is it important to understand a particular CLI.  I wish I could have had access to this product 5 years ago when, at a previous job, we introduced JunOS to a team that had been working on IOS and Foundry for the majority of their careers.  It would have solved so many issues and driven the learning curve to nil.

The CLI translator is really just the icing.  The configuration validation is immensely powerful and I could easily see it preventing many typos and misconfigurations (you know you&#8217;ve done it, we all have).  It can also provide compliance reporting, service management and configuration reconciliation, all of which are generally in-house written tools or manually accmplished tasks in my experience.

Standardize and deploy ACLs across a range of platforms in geographically diverse areas, provision BGP policy on huge numbers of peers very quickly, reconcile MTUs on interfaces of devices that have been neglected, <a href="https://wiki.openstack.org/wiki/Neutron/ML2/Tail-f-NCS-neutron-ml2-driver" target="_blank">interface with OpenStack Neutron</a>.  The use cases are pretty open ended, really. Anything that needs to be done at scale can be, and it can be error checked in the process.

Don&#8217;t take my word for it, I&#8217;m clearly excited about it and can&#8217;t wait to get my hands on it.  Watch the NCS demo:

<span style="line-height: 1.5em;">Tail-f Systems NCS Demo at Networking Field Day 7</span>



&nbsp;

All of the videos can be found <a href="http://techfieldday.com/appearance/tail-f-systems-presents-at-networking-field-day-7/" target="_blank">here</a>.

Rosetta Stone images courtesy of <a href="http://www.ancientegypt.co.uk/writing/rosetta.html" target="_blank">http://www.ancientegypt.co.uk/writing/rosetta.html</a> and <a href="http://taboodada.wordpress.com/" target="_blank">http://taboodada.wordpress.com/</a>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-908" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-908" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-908" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-908" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/02/tail-f-ncs-upsetting-network-management-in-a-good-way/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

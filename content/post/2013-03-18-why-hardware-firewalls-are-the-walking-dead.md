OK, maybe they&#8217;re not totally dead, but they&#8217;re being demoted. To the mail room.

During the course of my career I&#8217;ve always had at least some responsibility for firewall and security devices.  In those ~15 years, how these boxes are built and function has shifted.  From the perspective of my career, there were IOS ACLs (yes, I know, not a firewall), there was the IOS firewall versions and there were software packages such as gauntlet, checkpoint.  There was the Cisco PIX. One installation I worked on in a past life even chose to use IPFW on BSD boxes.   Then came was the Sonicwall, a newer take on how to manage a security appliance via a web interface. There was the FWSM.  A few things stayed the same. Dedicated hardware.

<img class=" wp-image-535 alignleft" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/Firewall-1024x670.jpg" alt="Free Firewall Clipart Illustrations at http://free.ClipartOf.com/" width="368" height="241" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/Firewall-1024x670.jpg 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Firewall-300x196.jpg 300w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Firewall-550x360.jpg 550w" sizes="(max-width: 368px) 100vw, 368px" /> 

Being a networking guy by nature, it always irritated me that the inline security devices were 3 years behind networking&#8230;.at best. Working in a service provider and in research and education has given me a bit of a different take on firewalls and IPS devices as well and has only solidified this belief.

&nbsp;

There are a few things that make firewalls and IPS devices an unholy thing in the world that I live in. Since I **love** bulleted lists, this is an opportunity to use one:

  * **They get in the way.**  Of course they to, that is their job.  Big data flows, Multicast, jumbo frames, IPv6.  There are boxes that can **finally** do these things, but they are 5-7 years behind and even now are often lacking in support and features.
  * **They&#8217;re expensive.**  When considering CAPEX, they are often prohibitively expensive compared to something like a passive IDS.  Not many budget for a firewall / IPS that can do multi 10G at line rate, IPv6, Multicast and can handle things like GridFTP flows, because until recently they didn&#8217;t exist.
  * **Speeds and Feeds are always first.**  I worked on 10G and OC192 on the WAN around 2002 with 10G on the LAN around the same time.  The first real firewall I saw that could even fall into consideration for that was the <a href="http://webcache.googleusercontent.com/search?q=cache:pLu75PgugigJ:www.force10networks.com/news/pressreleases/2006/pr-2006-08-28_2.asp+&cd=1&hl=en&ct=clnk&gl=us&client=safari" target="_blank">FPGA based P10</a> from Force10 in 2005 (we had an early demo).  It was a really innovative device but even it was very clunky since it was an FPGA and caused service interruptions every time you needed to push rules to the FPGAs.  The Juniper SRX came much later at 2009, and even <a title="Updating SRX IDP signatures" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/" target="_blank">it</a> <a title="Moving JunOS code between SRX cluster nodes" href="http://www.forwardingplane.net/2011/01/moving-junos-code-between-srx-cluster-nodes/" target="_blank">had</a> <a title="Enabling IPv6 on Juniper SRX 5800 cluster" href="http://www.forwardingplane.net/2010/10/enabling-ipv6-on-juniper-srx-5800-cluster/" target="_blank">some</a> <a title="SRX IPv6 flow based processing" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/" target="_blank">issues</a> back then.  There exists a handful of options now, the Sonicwall SuperMassive, the Juniper SRX  and the Palo Alto come to mind but they&#8217;re late.  10G is old hat to some of us.  We&#8217;re on to 40G and 100G.  What now?

So, lets get down to the buzzwords.  Cloud.  Data Center.  Virtualization.  SDN.  OpenFlow.  Ironically enough, being &#8220;buzzword compliant&#8221; is actually relevant to this commentary. With the advent of virtualization of nearly everything, including the network, vendors are adding things like virtualized firewalls.  Juniper has added the <a href="http://www.juniper.net/us/en/dm/edge/products/" target="_blank">JunosV Firefly</a>, Cisco has added the <a href="http://www.cisco.com/en/US/products/ps12233/index.html" target="_blank">VSG</a>.  There are surely others.  This movement is just in it&#8217;s infancy, but it&#8217;s big and I would venture to say that it is game changing.  With the huge amounts of cores and memory in virtual machine hosts, it makes sense that the network become part of that for management, total cost of ownership and usability.

The really interesting part of all of this comes not with the virtualization of firewalls, but with the commoditization of network silicon.  Chip makers that are spinning ASICS need to make sure their ducks are in a row since, in my personal opinion, there are a lot of options for LAN and data center equipment.  <a href="http://www.aristanetworks.com" target="_blank">Arista</a> is already on top of this.  Others vendors will adopt this methodology as merchant silicon adds more abilities.  Firewalls will are on their way now.  Eventually WAN gear will come around.

What I&#8217;m really excited about is the prospect of a merchant silicon based, 40 or 100G OpenFlow based &#8220;Firewall&#8221;.  The foundation is already laid for this.  <a href="http://www.openflowhub.org/display/floodlightcontroller/Firewall+(Dev)" target="_blank">Floodlight already has a dev module for building a firewall with OpenFlow</a>.  I&#8217;ve not tested this extensively yet.  It&#8217;s on my short list but wether it works or not isn&#8217;t really even relevant.  The fact of the matter is that this is the way to a comfortable security perimeter at a reasonable speed for a far more reasonable price tag.

[<img class="wp-image-536 alignright" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall.jpg" alt="OF-Firewall" width="450" height="453" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall.jpg 562w, http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall-150x150.jpg 150w, http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall-297x300.jpg 297w, http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall-45x45.jpg 45w, http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall-550x553.jpg 550w, http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall-200x200.jpg 200w" sizes="(max-width: 450px) 100vw, 450px" />](http://www.forwardingplane.net/wp-content/uploads/2013/03/OF-Firewall.jpg)Think of buying an OpenFlow capable device with 40 and 100G interfaces in it as your firewall and IPS device.  Port cost is very low.  CAPEX is low.  OPEX is also fairly low since it is just a normal piece of network hardware.  Management is accomplished via an OpenFlow controller.

Rules are pushed manually or programmatically based entirely on site policy.  IPS functions can be performed via a passive system like BroIDS or Snort triggering rules in OpenFlow much like is being commonly done with <a title="Black Hole routing" href="http://www.forwardingplane.net/2011/10/black-hole-routing/" target="_blank">black hole routers</a> now.

This will happen.  It&#8217;s already happening.

Firewall vendors take notice.  Have a strategy for Virtualization.  Have a strategy for dealing with OpenFlow and SDN.

It is my belief that once the reporting and management is even half as good as a <a href="http://www.paloaltonetworks.com" target="_blank">Palo Alto</a> or <a href="http://www.sonicwall.com" target="_blank">Sonicwall</a>, the market will start to change based solely on cost.  <a href="http://openflow.marist.edu/avior.html" target="_blank">There is already work being done on this as well</a>.

Am I right?  Time will be the judge, but I suspect I am.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-522" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-522" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-522" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-522" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/03/why-hardware-firewalls-are-the-walking-dead/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

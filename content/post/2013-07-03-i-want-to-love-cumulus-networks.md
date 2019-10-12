_I want to preface this by saying that I have not seen or worked on the cumulus networks system yet. This is a stream of consciousness post on my thoughts and opinions based on what I&#8217;ve read publicly._

Recently a <a href="http://cumulusnetworks.com/" target="_blank">new network player</a> has emerged on the scene with a very simple, straightforward idea. Take linux and put it on a switch. While this isn&#8217;t exactly new (see Juniper and FreeBSD, Arista with Linux, Force10 with NetBSD or the plethora of other vendors using an opensource OS as the underpinnings of their NOS), the angle that cumulus networks is taking is a bit more&#8230;.raw.

Take a standard Cisco or Juniper box. The engineers that work on these devices know a pseudo-programming language. They program the routers using that language and syntax. They&#8217;re familiar with it and it is well documented. Heck, aside from <a href="http://www.juniper.net/us/en/community/junos/training-certification/day-one/fundamentals-series/cli/" target="_blank">JunOS</a>, <a href="http://www.enterasys.com/" target="_blank">Enterasys</a> and the <a href="https://infoproducts.alcatel-lucent.com/html/0_add-h-f/93-0070-10-01/7750_SR_OS_System_Basics_Guide/CLI%20Usage.html" target="_blank">Alcatel-Lucent,</a> 90% of the NOS you see on equipment is arguably derivative of <a href="http://www.cisco.com/" target="_blank">Cisco</a>&#8216;s venerable <a href="http://www.cisco.com/en/US/docs/ios/fundamentals/configuration/guide/cf_cli-basics.html" target="_blank">IOS</a>. Automation is [unfortunately] not nearly as common as it could be on network gear. Sure, there are a handful of opensource tools, overpriced, bloated and [arguably] poorly functioning tools available to &#8220;automate&#8221; and &#8220;manage&#8221; equipment, but none are that great, especially if you have a large, diverse environment.

Enter the sysadmin. Sysadmins have been automating tasks for as long as I&#8217;ve been around. <a href="http://cfengine.com/" target="_blank">cfengine</a>, home grown tools and now <a href="https://puppetlabs.com/" target="_blank">puppet</a> and the like are marvelous tools that are a makeshift &#8220;controller&#8221; for managing distributed systems. Big Iron cluster admins have had tools like this forever as well. How often are these people the same? In a large environment where there is a need for automation I will wager that the answer to that question is &#8220;not very often&#8221;.

This is my concern with cumulus networks. Make no mistake, I love the simplicity and idea behind it. I think that it&#8217;s wonderfully simple and innovative. It&#8217;s the &#8220;duh&#8221; of networking OS choices, but it introduces a lot of issues, many of which aren&#8217;t really pleasant to solve (and only a handful are actually technical). You&#8217;ve got the fractured nature of IT in large environments. Server guys aren&#8217;t often the same as networks guys. Often they are in totally different silos. This is problematic due to territoriality not to mention subject matter expertise. Am I as a network engineer of 15+ years comfortable running *IX systems? Sure. Is everyone? Likely not and even less likely on a large scale like this.

Automation is key, but even running puppet systems isn&#8217;t exactly a network engineers core competency. I think that building those systems will be either cost prohibitive (either time or salary) or will just be a non-started because it&#8217;s &#8220;too different&#8221;. Let me reiterate that I think it&#8217;s a very cool idea and know that it&#8217;d probably take a week or so to make work for any decent sysadmin or system savvy network engineer, but the large swath is going to recoil. The lack of a single configuration file is also off putting to many network engineers. Management systems may be able to handle some of these functions, but nothing is easier than nearly zero touch deployment and a single config file is a poor-mans, widely accepted method.

They have a quagga instance their version which provides a &#8220;non-model CLI&#8221;, and if the quagga is anything like what I&#8217;ve used it can sorta be used to manage the network, but is a poor overlay to the system tools that adds very basic routing protocols. It&#8217;s encouraging, but feels like a bolt on at face value.

Then there is the issue of the raw OS. It&#8217;s just Linux. This statement alone opens up a new vector. Does one need to now worry about having compromised switches? Can my switch be turned into a bit cannon or a warez distribution site? A Tor relay? Hardening a switch or router has always been important, but this feels different to me and how many times has a RE protect ACL or loopback filter been mistakenly forgotten? What happens when there is a kernel exploit? Sure, puppet and cfengine can help with that, but these are also mechanisms and processes that need to be taken into account as far as resources on the switches. How will these extra processes affect the transit traffic? What happens when Linux decides it doesn&#8217;t have enough resources and starts killing off processes?

Now, I think there are good precurser to this model that have been around for quite some time. I&#8217;d really love to see something like <a href="http://www.pfsense.org" target="_blank">pfSense</a> or <a href="http://www.microtic.com" target="_blank">RouterOS</a> on a merchant silicon Layer3 switch. The foundations are already there, they are seasoned, well documented and feature rich platforms. RouterOS even has [<img class="alignleft size-full wp-image-707" alt="pfsense_logo" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/pfsense_logo.jpg" width="90" height="90" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/pfsense_logo.jpg 90w, http://www.forwardingplane.net/wp-content/uploads/2013/07/pfsense_logo-45x45.jpg 45w" sizes="(max-width: 90px) 100vw, 90px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/pfsense_logo.jpg) [<img class="alignright size-full wp-image-708" alt="Vrz21" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/Vrz21.jpg" width="417" height="167" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/Vrz21.jpg 417w, http://www.forwardingplane.net/wp-content/uploads/2013/07/Vrz21-300x120.jpg 300w" sizes="(max-width: 417px) 100vw, 417px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/Vrz21.jpg)OpenFlow support now and I&#8217;d bet money pfSense is looking at integrating SDN of some sort. Both have central management platforms and are Linux or BSD based, so they are very extensible and at their foundation they are Open Source. Both should be portable and most importantly they are more of a intermediate step into a hybrid networking OS.

I know some of this may sound negative, but these are all things that need to be addressed and answered as we move more into the new wave of networking. I am confident that cumulus networks is onto something great with their model. It it too bold? Too soon? I wish I knew.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-678" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-678" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-678" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-678" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/07/i-want-to-love-cumulus-networks/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

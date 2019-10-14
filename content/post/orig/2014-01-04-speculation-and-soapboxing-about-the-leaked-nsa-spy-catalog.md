The buzz as of late around the security and networking communities has been about the <a href="http://www.spiegel.de/international/world/nsa-secret-toolbox-ant-unit-offers-spy-gadgets-for-every-need-a-941006.html" target="_blank">NSA and their catalog or spy toolkit</a>.  I&#8217;ve spent time in my career thinking about and doing infosec and I did a brief stint working for the FBI in a project called <a href="http://gcn.com/articles/2007/08/20/fbi-launches-cybersecurity-project.aspx" target="_blank">NCDIR</a>.  I like to think that I can provide at least a peripherally competent commentary about it [take it with a grain of salt].  Instead of thinking about the morality of it or the violation of privacy that everyone else seems to be focused on, I want to think about the mechanics.

If one takes the emotion and outrage out of the equation, there are some <a href="http://permalink.gmane.org/gmane.comp.encryption.general/17244" target="_blank">really interesting tools here</a>.  My initial thoughts, though, are &#8220;how is the backdoor installed?&#8221; and &#8220;how is the data harvested?&#8221; There are cases where I&#8217;m sure the backdoors are installed via local access and the data is harvested in uninteresting ways like optical taps, wireless bridges, etc., however, what how about in cases where this isn&#8217;t possible?  What about when the equipment is in a bunker with no viable wireless in or out, it&#8217;s have to be done either in-band or via a tap, which would require physical access.   It&#8217;d be interesting to see a <a href="http://www.bro.org/" target="_blank">BroIDS</a> or <a href="http://www.snort.org/" target="_blank">Snort</a> policy for the &#8220;DNT Implant Communications Protocol&#8221; once that is deconstructed.

As far as installation of the backdoor, how about the case about when interception of hardware in transit isn&#8217;t an option and physical access is also not viable?  The implications of remotly exploitable network equipment for things such as this are very-wide scoped and **_extremely_** unpleasant.  One can assume that if our government can exploit something like this, so can another nation-state.  Not good.  Not good at all.  How much of our gear is manufactured abroad?  They have physical access because they **_build_** it, one could assert that it is plausible that &#8220;they&#8221; could insert whatever they wanted in the hardware.  Again, I&#8217;m not a hardware engineer, but I can speculate.

[<img class="alignright size-medium wp-image-859" alt="40g-tap-500x500" src="http://www.forwardingplane.net/wp-content/uploads/2014/01/40g-tap-500x500-300x126.jpg" width="300" height="126" srcset="http://www.forwardingplane.net/wp-content/uploads/2014/01/40g-tap-500x500-300x126.jpg 300w, http://www.forwardingplane.net/wp-content/uploads/2014/01/40g-tap-500x500.jpg 500w" sizes="(max-width: 300px) 100vw, 300px" />](http://www.forwardingplane.net/wp-content/uploads/2014/01/40g-tap-500x500.jpg)

I&#8217;d be really interested in seeing if data is being harvested inline, without a tap and how that is being done.  It&#8217;s implied in some of the descriptions of the *THROUGH listings that there is inline control available.  What I&#8217;d really be interested in seeing is someone that can capture that traffic flow data in an upstream device.  Flow data doesn&#8217;t lie, and it is highly likely that there is a router in the path somewhere exporting flow data that isn&#8217;t obfuscating traffic by being compromised.  Where is the traffic going?  How is it transported (encrypted, for sure, but how?)

How does this change how we, as network engineers, feel about RMA&#8217;d hardware?  If the manufacturers don&#8217;t know about modded boot ROMS, it&#8217;s likely that RMA&#8217;d hardware is being shipped all over with backdoors that were intended for someone else in it.  Oh, and another thing, this is an _old_ document.  2008 is a lifetime ago in terms of networking and computing technology.  I saw no mention of the <a href="http://www.juniper.net/us/en/products-services/security/srx-series/" target="_blank">Juniper SRX</a>, <a href="http://www.juniper.net/us/en/products-services/routing/mx-series/" target="_blank">Juniper MX</a>, <a href="http://www.cisco.com/en/US/products/ps9343/prod_models_comparison.html" target="_blank">Cisco ASR</a>, <a href="http://www.brocade.com/products/all/routers/index.page" target="_blank">Brocade MLX/CES</a> or <a href="http://www.alcatel-lucent.com/" target="_blank">Alcatel-Lucent</a> devices.  I&#8217;d bet real money all of that exists now.

Additionally, what about <a href="http://en.wikipedia.org/wiki/FIPS_140" target="_blank">FIPS 140</a>?  I want to believe this can come into play, but admittedly I don&#8217;t know a lot about FIPS, just what I&#8217;ve read on the <a href="http://csrc.nist.gov/groups/STM/cmvp/standards.html#02" target="_blank">NIST site</a>.  How does FIPS assist in preventing the software hacks? Or does it? As far as most of the the network equipment backdoors, they imply that boot time code modifies the OS, can cryptographic checks aide in rooting some of these out?  I have not done much in this aspect of security, but I have to believe there is a way to detect this kind of boot time modification of the OS.

This opens up an entirely new aspect of SDN, too. When your control plane is decoupled and likely running on a linux box of some sort, the targeting of &#8220;the network&#8221; becomes far more simple of a compromise.  Ever done linux forensics?  Most of the hacks are fairly low-brow.  Root one box and you have access to the control plane of a data center, internet backbone or campus network.  What about all of the white box network devices that are just linux like <a href="http://www.aristanetworks.com/" target="_blank">Arista</a> and <a href="http://cumulusnetworks.com/" target="_blank">Cumulus Networks</a>? Now we&#8217;re managing linux boxes like we are with Juniper and FreeBSD, except they are less customized and more vanilla (read: potentially more likely to be exploitable).  This is a problem.  Think because you have a firewall and a NAT device you&#8217;re safe?  You&#8217;re wrong [clearly].  Hardening controllers will be increasingly important, perhaps even running them on trusted unix platforms.  It&#8217;s a problem that is now much easier than intercepting hardware in transit and installing backdoors into it, but an in-depth SDN security talk is an _entirely_ different can of worms.

This just solidifies my thought that if something is **_so_** critically important that it must remain secret and secure, don&#8217;t put it on a computer.  Especially one with a network connection.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-858" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-858" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-858" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-858" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/01/speculation-and-soapboxing-about-the-leaked-nsa-spy-catalog/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

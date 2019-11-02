There are a vast number of entities that offer the seemingly ubiquitous “cloud”. “SaaS”, “IaaS”, “BLAHaaS”, buzzword compliance is truly a sought after thing by marketing folks. With the proliferation of virtualization, containers and other “time slicing” of hardware by software the chatter can quickly become noise. As technical professionals and the warm bodies with the responsibility for actually making things work and keeping them running, the onus is on us to be able to decipher the useful from the fluff.  
A staggeringly large number of institutions, enterprise, education, research, and government all rely heavily on virtualization as a cornerstone for cost savings and operational ease. This makes sense, there is real cost savings in both operational and capital money.

[Ravello](http://www.ravellosystems.com/).

Recently I was given access to an interesting emerging product brought about by the original developers of the venerable [KVM](http://www.linux-kvm.org/page/Main_Page). Ravello offers something new, something a bit different and something potentially useful for a number of different applications. Ravello is essentially a cloud overlay.  
I find the interfaces for both the Amazon EC2 and Google compute engine clunky and unintuitive from an operational perspective. While APIs are decent, I am a poor developer and really have no desire to write code to their APIs. When I need results now, I want compatibility and a good interface and I’ll wager most other operational folks do too. This is an element that is hard to acheive and where I was a tad surprised by the Ravello platform. The interface for their cloud overlay was quite elegant and **very** intuitive. That’s important. However, what it actually does is more significant.  
The Ravello overlay allows a VM admin to import an existing image in its native form (either VMWare or KVM), deciphers the networking metadata from the images and builds the network for them automatically. This is cool in and of itself, but the real power is the combination of that “admin candy” and the ability to tune the knobs for things like which cloud provider (AWS or GCE) to push your resources to, allow optimization for things like cost or performance and the option to time shutdown of the resources.

For smaller institutions and enterprises the value seems self evident. As an example, lets say you want to model a change to your data center network which includes an SRX firewall, 3 window servers, 10 linux servers and a load balancer. These resources can all be uploaded into the ravello cloud. It does its best to figure out the network, allowing for some reasonably powerful changes to the configuration right from their interface. Snaphot the entire network from their canvas (which looks like a nice network diagramming tool), make the changes and monitor the result. If it doesn’t work you can roll it back or hack at the consoles of the devices using their VNC based console access to figure out what went wrong.  
In addition to the aforementioned benefits, there were some other surprises. The time to provision was quite good, importing at the speed of upload and then fairly quickly deciphering the needed pieces. It is also obviously self service, meaning I can import, enable, tweak and disable within a choice of cloud based hosting services; flexibility is always good, especially when it is well implemented.



Overall my impression of Revello is that is provides some pretty interesting and useful stuff, especially when considering utilizing it as a lab for testing upgrades, changes, etc. Many small to medium sized environments do not have resources to put into a physical lab, virtualizing it for a fraction f the cost has a lot of merit and value. Overflow for event based demand is also an obvious use case and again ease of use implementation is key.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1287" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1287" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1287" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1287" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2015/05/ravello-systems-review-and-use-case-study/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

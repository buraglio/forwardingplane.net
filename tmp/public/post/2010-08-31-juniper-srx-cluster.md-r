I have had the opportunity to work pretty extensively on the Juniper SRX firewall/IDS platform over the last few months.  In doing so, I&#8217;ve found many &#8220;gotchas&#8221; the hard way. 

Here are a few that I&#8217;ve found so far:

Clustering is a beast in and of itself.  I think it needs a bit more polishing, but it could be that we just need to refine our design.

On the SRX 650 it works, but you must be on the right code version (I got it to work under 9.6R2.11 and have left it alone since).

On the 5800 it works a bit better, but if you want to do active/active, it is very lacking in features.  
We have a unique setup where I am employed, and this usually means we are left a bit on our own as far as configurations (although our Juniper SE is amazing and did a lot to get this all working).  
That said, we have a design that isn&#8217;t really fully supported on the SRX yet, although I believe it will be as code matures.  
What we&#8217;ve done is to create a cluster using no reth interfaces.  Instead, we&#8217;re relying on routing to ake the decisions as far as what traffic goes where.  This was a different approach than we had originally used on the smaller 650 cluster elsewhere in the network. 

<div style="clear: both; text-align: center;">
  <a href="http://1.bp.blogspot.com/_t5EEUl7btNU/TH18bIBhtkI/AAAAAAAACn4/wgLW1b-H7Zs/s1600/simplesrx.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/_t5EEUl7btNU/TH18bIBhtkI/AAAAAAAACn4/wgLW1b-H7Zs/s320/simplesrx.png" /></a>
</div>

What this means is multi-faceted.  
Standard jtac isn&#8217;t going to understand what you&#8217;ve done.  Using advanced jtac is the only way to get things moving in a timely fashion should you encounter issues.  We have agility service on ours, so that makes it even easier. 

IDP doesn&#8217;t work asymmetrically.  If an traffic cones in on one node and leaves through the other, IDP doesn&#8217;t apply.  IDP information is not shared through the control link at the time of this writing.  
IDP updates across the cluster don&#8217;t work well in this way.  My &#8220;node0&#8221; node can get the updates but since node0 holds the loopback interface that traffic is sourced from, I cannot get out from node1.  Again, this data is not shared over the control link between the cluster nodes.  There are nasty ways around this with static routes, but I prefer not to use them.    
The best way I found to get around this is to manually fail over the cluster and install the IDP updates on node1 after node0 has installed them and then to fail back.  
This brings me to the next issue we ran into.  Upgrading the cluster junos software.  
Juniper&#8217;s recommended method for upgrading is to upgrade each one, then reboot both at the same time.  
to me this is a bit odd, since the reason most folks want a cluster is to avoid things like this.  Well, I can say for experience, if you upgrade the node0 and reboot it without doing the same to node1, all heck breaks loose.  The cluster won&#8217;t come up cleanly even after the secondary is upgraded and the only way I found to alleviate the off traffic problems we were seeing was to bounce them both at the same time.  Annoying to say the least.  
Oh, if you want to run Active/Active and have it actually work the way we have it set up, you&#8217;ll need at least JunOS 10.2.R2.11. 

That said, I really do believe that the SRX is the best carrier class security appliance on the market.  Our entire network (which is not insignificant or standard in size or traffic patterns), can run off of one box with 4 SPCs and not even touch the processing power.  They are a powerhouse and have that trademark JunOS cli, and all of the advantages that come with it.

<div>
  [[ This is a content summary only. Visit my website for full links, other content, and more! ]]
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-59" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-59" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-59" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-59" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
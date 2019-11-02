One of my biggest complaints about VMware is that it is an enterprise application. It has historically catered to the masses, which I completely understand, but those of us that aren&#8217;t a fortune 500 company are figuratively and operationally shoved into a corner and forced to find hackish ways of doing things to work around the enterprise nature.  
One really, really good example of this is OS dependency. I hated architecture dependencies back in the old days (x86, SPARC, PPC) and I absolutely despise things that are OS platform dependent now.  It&#8217;s inconvenient and just plain sucks for anyone using anything but that required platform. This goes for anything, mac dependent, MS dependent, unix dependent, whatever. I don&#8217;t discriminate in my idealism.  While I realize it is an impossible, idealistic expectation,  I back up my stance 100% regardless.

That being said, one of the most irritating of those in recent memory has been VMware. Managing the VMWare ESXi instances that I run for both lab and production work is a pain. Since I&#8217;m not really a sysadmin or a virtualization engineer my knowledge of this stuff is surely limited I may be going about this in a non-optimal way, but until recently it has required a one-off host or VM running windows with the client to do anything useful. Apparently this has changed with the pay version in 5.something adding a web interface.  Unfortunately this isn&#8217;t an option at this time for me, it&#8217;s cost prohibitive. So, when I found it necessary to do some management without a windows VM or host, I was pleasantly surprised to find that I can do simple tasks via the SSH CLI. was able to query power state, start, stop, etc. using simple CLI tools. Now, these are all documented at the VMware KB, but I wanted to throw together a quick reference sheet for all of them in one place so I started compiling it <a href="http://www.forwardingplane.net/unix/vmware-esxi-cli-reference/" target="_blank">here</a>.  Please feel free to shoot over any additions or quick tips that should be on there. This is just the tip of the iceberg, I suspect (or maybe I&#8217;m just going about my VMware management all wrong; I&#8217;m open to that as well and suggestions on how to remedy).

The most useful for me so far have been inventory and power related.

<pre>List all VMs:
vim-cmd vmsvc/getallvms

List power state of VM:
vim-cmd vmsvc/power.getstate &lt;VM ID&gt;

Power on VM
vim-cmd vmsvc/power.on &lt;VM ID&gt;

Power off VM
vim-cmd vmsvc/power.off &lt;VM ID&gt;

</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-689" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-689" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-689" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-689" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/06/vmware-esxi-cli-reference/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
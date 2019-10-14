I had been working, off and on, on a how-to for building the <a href="http://www.opendaylight.org/" target="_blank">daylight openflow controller</a> under CentOS.  Most openflow docs and dev are done under ubuntu or debian, and while those are both fantastic alternatives, there are a huge number of folks that will want or need to use RHEL or CentOS. So, seeing as that is the case, having someone be mindful of that is important.  When I saw the <a href="http://www.dasblinkenlichten.com/installing-opendaylight-on-centos/" target="_blank">write up</a> by <a href="https://twitter.com/blinken_lichten" target="_blank">Jon Langemak</a>, I scrapped my attempt at a how-to since his was so much better.

If you&#8217;re not following Jon and reading his blog, you should be.  He&#8217;s a sharp guy with interesting things to say.

[<img class="alignleft size-full wp-image-603" alt="projectfloodlight-logo-header" src="http://www.forwardingplane.net/wp-content/uploads/2013/04/projectfloodlight-logo-header.png" width="213" height="124" />](http://www.forwardingplane.net/wp-content/uploads/2013/04/projectfloodlight-logo-header.png)

That got me thinking about references and resources, and I decided that I would take a few of the things I had been working on on my home lab and make them available to the masses.  I&#8217;m a fan of importable base VMs.  So, seeing that I am working on testing openflow controllers, it made sense in my [constantly racing] mind to make the reference, base level VMs available.  If anyone is interested in the <a href="http://www.projectfloodlight.org/floodlight/" target="_blank">floodlight controller</a> running under CentOS 6.3 built using the method documented <a title="Building a Floodlight OpenFlow controller on CentOS 6" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/" target="_blank">here</a>, a KVM image is now available to download from <a href="http://www.forwardingplane.net/wp-content/uploads/vm-images/centos-floodlight-template.tbz" target="_blank">here</a>.  It is, as stated, a KVM image, created by using the method I documented in <a title="CentOS KVM Install – Quick Start to a VM" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/" target="_blank">this post</a> a few months ago.    There is a readme file in the archive wth basic instructions.  You&#8217;ll need a basic understanding of <a href="http://www.linux-kvm.org/page/Main_Page" target="_blank">KVM</a> to make it work, or you can try to convert it to something else like vmware, XEN or virtualbox.

I&#8217;ll be adding one of these soon for <a href="http://www.opendaylight.org/" target="_blank">daylight</a> as well.

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-602" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-602" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-602" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-602" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/04/basic-reference-openflow-controller-vms-running-in-centos-6-for-kvm/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

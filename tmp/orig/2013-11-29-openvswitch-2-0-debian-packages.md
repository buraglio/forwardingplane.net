As part of a larger fun project I&#8217;m working on (OVS for the ALIX platform; more to come on that once I have it 100% working), I have been playing a lot with <a href="http://openvswitch.org/ " target="_blank">OVS</a>.  It&#8217;s a great platform, and <a href="http://networkstatic.net/install-open-vswitch-v2-redhat-fedora-19/" target="_blank">as others have mentioned</a>, it&#8217;s as close to an SDN reference data plane implementation as we have.  I&#8217;d be surprised if many if not all commercial implementations of OpenFlow aren&#8217;t based on OVS.  Anyway, I wanted to build debian packages since I&#8217;d never done it before and thought it&#8217;d be fun.  I wanted to use OVS2 so that I can play with some of the newer features and specifically to see how well the IPv6 support is in 2.0 when paired with <a href="http://www.opendaylight.org/" target="_blank">OpenDaylight</a>(more to come on this, too. I promise =).

This proved to be more simple than I anticipated mostly due to lots of good documentation.  To accomplish it, I decided to start with a VM since I lie to work in virtualized environments for experimentation and lambing. I spun up a Debian 7 VM from scratch and began configuring it as I usually do with the inclusion of the tools necessary to build packages.

_** I originally tried this from the git repo via _git clone git://openvswitch.org/openvswitch_ but kept seeing weird errors so I moved to the 2.0.0 tarball.  _

<pre>apt-get -y install screen sudo vim etckeeper mlocate autoconf2.13 \
libssl-dev graphviz python-all python-qt4 python-zopeinterface \
python-twisted-conch tcpdump build-essential fakeroot debhelper \
gdebi-core pkg-config</pre>

Grab the OVS tarball

<pre>wget <a href="http://openvswitch.org/releases/openvswitch-2.0.0.tar.gz">http://openvswitch.org/releases/openvswitch-2.0.0.tar.gz</a></pre>

<pre>mv openvswitch-2.0.0.tar.gz openvswitch-2.0.0.orig.tar.gz</pre>

<pre>cd openvswitch-2.0.0</pre>

<pre>dpkg-buildpackage -b</pre>

<pre>cd ../</pre>

Install all of the packages

( # Answer Y to all prompts )

<pre>gdebi openvswitch-datapath-source_2.0.0-1_all.deb</pre>

module-assistant auto-install openvswitch-datapath  
gdebi openvswitch-common\_2.0.0-1\_amd64.deb  
gdebi openvswitch-switch\_2.0.0-1\_amd64.deb

<div>
</div>

You should now be able to check the version:

&nbsp;

<pre>buraglio@deb7ovs-vm:/home/buraglio# ovs-vsctl -V
ovs-vsctl (Open vSwitch) 2.0.0
Compiled Nov 29 2013 13:18:32
</pre>

Check the OpenFlow versions supported: 

<pre>buraglio@deb7ovs-vm:/home/buraglio# ovs-ofctl -V
ovs-ofctl (Open vSwitch) 2.0.0
Compiled Nov 29 2013 13:18:32
OpenFlow versions 0x1:0x4
</pre>

More to come on this.  For anyone that doesn&#8217;t want to build the .debs themselves, they&#8217;re available to download from <a href="http://www.forwardingplane.net/wp-content/uploads/OVS2.0/" target="_blank">here</a>, no warranty implied or expressed =)

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-824" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-824" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-824" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-824" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/11/openvswitch-2-0-debian-packages/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

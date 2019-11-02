I am a network engineer by profession, but with the proliferation of SDN and OpenFlow, I have had to spend a lot of time re-learning a lot of system admin skills that I&#8217;d shelved years ago.  Now, I&#8217;ve been a virtualization user forever. From <a href="http://www.vmware.com" target="_blank">VMware</a> (Fusion, ESX), <a href="https://www.virtualbox.org" target="_blank">VirtualBox</a>, to <a href="www.parallels.com" target="_blank">Parallels</a>, I&#8217;ve used them at least in testing if not in production environments.  I&#8217;d not really spent any mentionable amount of time with <a href="http://www.xen.org" target="_blank">XEN</a>, <a href="http://www.qemu.org" target="_blank">qEMU</a> or <a href="www.linux-kvm.org" target="_blank">KVM</a>, but some projects I was working on suggested it for the virtualization mechanism, so I figured I&#8217;d try to pick it up.  I think the hosting provider  of this blog is using it to provide the VPS that this site runs on, so it is clearly production quality.  In looking around for a straightforward how-to, a few things became obvious pretty quickly:

KVM is very robust.

KVM and qEMU have got a lot of documentation, but not all of it is straightforward.

They have a lot of pieces needed to make it work efficiently.

It wasn&#8217;t a plug and run experience, by any means.  I wanted a headless, remotely manageable system that ran on a bare minimum install (i.e. no GUI).  After a late evening of hacking at it,  here is what I finally had to do to get it running and build a functional VM on a fresh install of CentOS 6.3.

Install all the dependancies.  And there were many.  Coming from using the VirtualBox CLI, little things that I expected didn&#8217;t work if I didn&#8217;t have this or that installed.

<pre>yum install -y qemu-kvm.x86_64 qemu-kvm-tools.x86_64 \
kvm libvirt bridge-utils tunctl python-virtinst.noarch avahi</pre>

Restart the deamons

<pre>/etc/init.d/messagebus restart
/etc/init.d/avahi-daemon restart
/etc/init.d/libvirtd restart</pre>

Make the new daemons start at boot:

<pre>/sbin/chkconfig messagebus on
/sbin/chkconfig avahi-daemon on</pre>

<div>
</div>

<div>
  I want to bridge rather than NAT.  My VMs need to have a public (or same LAN segment) address as the rest of the hosts for external management and availability of inbound services.  For this, we need to adjust the interfaces.  I want to run the bridge on a second interface and keep the host system management on a dedicated interface.
</div>

<pre>vi /etc/sysconfig/network-scripts/ifcfg-eth1</pre>

Your file should look something like this when done:

<pre>DEVICE="eth1"
HWADDR="c0:ff:ee:c0:ff:ee" # (leave this as your MAC address)
NM_CONTROLLED="yes"
 BRIDGE=br0
 ONBOOT="yes"
UUID="a9c26927-7650-42e9-a86a-1ae1227eac4b" #leave this as your UUID)</pre>

<pre>vi /etc/sysconfig/network-scripts/ifcfg-br0</pre>

<div>
</div>

<div>
  Your file should look something like this when done:
</div>

<div>
</div>

<pre>DEVICE="br0"
TYPE="Bridge"
BOOTPROTO="static"
IPADDR="10.10.10.50" # Use your own IP address
NETMASK="255.255.255.128"
GATEWAY="10.10.10.1"  # Provide your gateway
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
NM_CONTROLLED="yes"
ONBOOT="yes"</pre>

<div>
  Restart the network to make it active.
</div>

<div>
</div>

<pre>service network restart</pre>

You&#8217;re going to use virt tools and virsh to manipulate the guests.  I tried it a few other ways and this seems far more supportable.  I wanted to install a CentOS 6.3 guest, I grabbed the install media from a <a href="http://cosmos.cites.illinois.edu/pub/centos/6.3/isos/x86_64/" target="_blank">local mirror</a>.  I have a volume mounted as /services that I keep stuff in.

<pre>mkdir /services/vm/template-host
cd /services/vm/template-host
wget http://cosmos.cites.illinois.edu/pub/centos/6.3/isos/x86_64/CentOS-6.3-x86_64-bin-DVD1.iso</pre>

Now use the virt-install command to boot the system with the following parameters:

2G of RAM

50G disk named disk.img

Console redirected to a VNC instance on port 5901

Network interface attached to br0

4 CPUs

CDROM points to install image

<pre>virt-install --name template-host --ram 2048 --disk /home/vm/template-host/disk.img,size=50 \
--graphics vnc,port=5901 --network bridge=br0 --vcpus=4 --os-type=linux \
--cdrom=/home/vm/Install_Media/CentOS-6.3-x86_64-bin-DVD1.iso</pre>

Now, to connect to the console, you&#8217;ll need to tunnel VNC over ssh.  This can be adjusted, but that&#8217;s outside of the scope of this.

I like to redirect real port numbers for my own sanity.

<pre>ssh -N -p 22 -c 3des buraglio@vmhost -L 5901/localhost/5901</pre>

The above command will redirect localhost port 5901 to port 5901 on the host vmhost

Connect to the VNC server:

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.00.37-PM.png"><img class="aligncenter  wp-image-470" alt="Screen Shot 2013-03-01 at 2.00.37 PM" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.00.37-PM.png" width="404" height="251" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.00.37-PM.png 505w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.00.37-PM-300x186.png 300w" sizes="(max-width: 404px) 100vw, 404px" /></a>
</p>

<p style="text-align: left;">
  Once connected you should drop right into the console of the KVM instance. Install as a normal system at that point.
</p>

<p style="text-align: left;">
  Once installed It&#8217;ll appear as a normal host console.
</p>

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.01.21-PM.png"><img class="aligncenter  wp-image-469" alt="Screen Shot 2013-03-01 at 2.01.21 PM" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.01.21-PM.png" width="430" height="253" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.01.21-PM.png 717w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.01.21-PM-300x176.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/03/Screen-Shot-2013-03-01-at-2.01.21-PM-550x323.png 550w" sizes="(max-width: 430px) 100vw, 430px" /></a>
</p>

<p style="text-align: left;">
  I found virsh to be the most useful for manipulating the virtual machine.
</p>

<pre>[root@behemoth Install_Media]# virsh list
Id            Name                                      State

----------------------------------------------------

9              template-host                         running</pre>

Helpful commands I found after 30 minutes of poking around and playing with virsh:

virsh list &#8211;show the list of virtual machines

virsh destroy <vm name> &#8211;hard shut down a host (I believe)

virsh undefine <vm name> &#8211;remove the VM from registration &#8211;this one was hard for me to find.

&nbsp;

<a title="KVM virsh command reference" href="http://www.forwardingplane.net/unix/kvm-virsh-command-referenc/" target="_blank">Here</a> is a complete list of the commands.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-467" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-467" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-467" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-467" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/03/centos-kvm-install-quick-start-to-a-vm/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
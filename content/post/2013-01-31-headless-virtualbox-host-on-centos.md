Starting from a base CentOS system with nothing configured, and referencing the <a href="http://wiki.centos.org/HowTos/Virtualization/VirtualBox" target="_blank">CentOS wiki</a>, here is how I like to set up a headless virtualbox environment:

Disable selinux. It&#8217;s overly cumbersome and is enabled by default in CentOS.  I like to permanently disable it even though the default is permissive.  I ride the edge, I know.

<pre>vi /etc/selinux/config</pre>

<div>
   and change
</div>

<pre>SELINUX=enabled</pre>

<div>
  to
</div>

<pre>SELINUX=disabled</pre>

<div>
  Then reboot.
</div>

Using the methodology I originally found found <a href="http://stackoverflow.com/questions/14016286/how-to-programmatically-install-the-latest-epel-release-rpm-without-knowing-its" target="_blank">here</a>, I like to install the epel repo using this method:

<pre>cat &lt;&lt;EOM &gt;/etc/yum.repos.d/epel-bootstrap.repo
 [epel]
 name=Bootstrap EPEL
 mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=epel-\$releasever&arch=\$basearch
 failovermethod=priority
 enabled=0
 gpgcheck=0
 EOM</pre>

<pre>yum --enablerepo=epel -y install epel-release
 rm -f /etc/yum.repos.d/epel-bootstrap.repo</pre>

Install rpmforge repo

<pre>rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt
 rpm -Uvh http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.x86_64.rpm
 yum clean all</pre>

Install the virtualbox repo

<pre>yum install -y wget
cd /etc/yum.repos.d
wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
yum update</pre>

<pre></pre>

Now the interesting bits, lets get to the vbox install.  Although we have enabled dkms, I like to also install as if we didn&#8217;t.  It populates the system with the pieces we need in a way that I&#8217;m used to.  I&#8217;m not a sysadmin by day, so this may be redundant.  YMMV, etc.   First, install the Development Tools. There are a lot here, it may take a bit depending on machine specs and connectivity speed in relation to mirrors. 

<pre>yum groupinstall "Development Tools"
yum install VirtualBox-4.2</pre>

Then start up the service and you should see something like this:

<pre>service vboxdrv setup
Stopping VirtualBox kernel modules [ OK ]
Uninstalling old VirtualBox DKMS kernel modulesError! There are no instances of module: vboxhost
4.2.6 located in the DKMS tree.
 [ OK ]
Trying to register the VirtualBox kernel modules using DKMS
 [ OK ]
Starting VirtualBox kernel modules [ OK ]</pre>

<pre></pre>

At this point you&#8217;ve got virtualbox done and installed. Now, the _real_ interesting part begins: VMs. I have a centos template that I built on my laptop.  It&#8217;s got the settings I like and I can just import it.  You can also build a new one, but that&#8217;s for a different post.  I moved the template via scp over to the newly anointed VM host. Now, I just need to import it and I can start cloning.  <a href="http://www.virtualbox.org/manual/ch08.html" target="_blank">vboxmanage</a> is the command we&#8217;re going to be utilizing heavily and it&#8217;s really powerful.  

<pre>vboxmanage import /home/buraglio/centos-63-template.ova</pre>

<pre>0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Interpreting /home/buraglio/centos-63-template.ova...
OK.
Disks: vmdisk1 150 1359413248 http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized centos-63-template-disk1.vmdk 512919552 -1 
Virtual system 0:
 0: Suggested OS type: "Linux26_64"
 (change with "--vsys 0 --ostype &lt;type&gt;"; use "list ostypes" to list all possible values)
 1: Suggested VM name "centos-63-template"
 (change with "--vsys 0 --vmname &lt;name&gt;")
 2: Number of CPUs: 2
 (change with "--vsys 0 --cpus &lt;n&gt;")
 3: Guest memory: 4096 MB
 (change with "--vsys 0 --memory &lt;MB&gt;")
 4: Network adapter: orig ur1-vm1 72.36.126.200/29, config 5, extra type=Bridged
 5: CD-ROM
 (disable with "--vsys 0 --unit 5 --ignore")
 6: SCSI controller, type LsiLogic
 (change with "--vsys 0 --unit 6 --scsitype {BusLogic|LsiLogic}";
 disable with "--vsys 0 --unit 6 --ignore")
 7: IDE controller, type PIIX4
 (disable with "--vsys 0 --unit 7 --ignore")
 8: IDE controller, type PIIX4
 (disable with "--vsys 0 --unit 8 --ignore")
 9: Hard disk image: source image=centos-63-template-disk1.vmdk, target path=/home/buraglio/VirtualBox VMs/centos-63-template/centos-63-template-disk1.vmdk, controller=6;channel=0
 (change target path with "--vsys 0 --unit 9 --disk path";
 disable with "--vsys 0 --unit 9 --ignore")
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Successfully imported the appliance.</pre>

<pre></pre>

It&#8217;s there. you should now have a folder in your home directory that has the VM in it. 

<pre></pre>

<pre>ls -la VirtualBox\ VMs/</pre>

<pre>total 12
drwx------ 3 buraglio buraglio 4096 Jan 29 20:23 .
drwx------. 4 buraglio buraglio 4096 Jan 29 20:23 ..
drwx------ 2 buraglio buraglio 4096 Jan 29 20:23 centos-63-template</pre>

to really make this useful, I clone all the VMs to the names I want and don&#8217;t use the template at all.

Now list the vms to verify what you have:

<pre>vboxmanage list vms
"centos-63-template" {4875b540-5514-4d0b-bba8-ce255b7f44a2}</pre>

We have one VM named &#8220;centos-63-template&#8221;, which is exactly what I wanted. Now clone this VM to the first usable VM, I&#8217;m building a floodlight OpenFlow controller, so I&#8217;ll name it accordingly.

<pre>vboxmanage clonevm centos-63-template --name floodlight1 --register
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Machine has been successfully cloned as "floodlight1"</pre>

Now list the vms to make sure it is listed:

<pre>vboxmanage list vms</pre>

<pre>"centos-63-template" {4875b540-5514-4d0b-bba8-ce255b7f44a2}</pre>

<pre>"floodlight1" {8fb4f03d-d117-43d5-b4bf-24cdcc481686}</pre>

Now here is the part I really like about virtualbox headless mode (and yes, I know others like qemu and xen can do this), when a virtual machine is started in headless mode, the console of that host can be redirected to an RDP instance. This makes it very convenient to manage systems on an out of band network like an isolated vlan or other non-routed or non-publically available network. It also makes it very convenient for spinning up a new VM that doesn&#8217;t have an IP stack configured. Its also very handy if you have a bad day and typo a host firewall rule or network config file. This has saved me a trip more than one time.

To do this, you&#8217;ll need the vrdp extension pack.  To list the installed extension packs, once again, use the vboxmanage command

&nbsp;

<pre>VBoxManage list extpacks
Extension Packs: 0</pre>

The extension pack for my version is available <a href="http://download.virtualbox.org/virtualbox/4.2.6/Oracle_VM_VirtualBox_Extension_Pack-4.2.6-82870.vbox-extpack" target="_blank">here</a>.

<pre>sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-4.2.6-82870.vbox-extpack 
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Successfully installed "Oracle VM VirtualBox Extension Pack".</pre>

At this point we&#8217;re ready to fire up the VM and connect to the console.

<pre>vboxheadless -startvm floodlight1 -vrde on -vrdeproperty "TCP/Ports"=3390&
Oracle VM VirtualBox Headless Interface 4.2.6
(C) 2008-2012 Oracle Corporation
All rights reserved.

VRDE server is listening on port 3390.</pre>

The above command will start the VM &#8220;floodlight1&#8221;, enable vrde and set the vrde port to 3390. You should now be able to connect to the console of the host using any free or included RDP compatible client. I use the microsoft office for mac provided rdp client.

<img class="aligncenter size-full wp-image-406" alt="RDC" src="http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC.png" width="469" height="154" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC.png 469w, http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC-300x98.png 300w" sizes="(max-width: 469px) 100vw, 469px" /> 

You&#8217;ll see an error when connecting since the server can&#8217;t be verified.  This is expected.

&nbsp;

&nbsp;

[<img class="aligncenter size-full wp-image-405" alt="RDC Verify" src="http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC-Verify.png" width="497" height="298" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC-Verify.png 497w, http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC-Verify-300x179.png 300w" sizes="(max-width: 497px) 100vw, 497px" />](http://www.forwardingplane.net/wp-content/uploads/2013/01/RDC-Verify.png)

&nbsp;

Hit connect and ta-da! Console on your VM.

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2013/01/Console.png"><img class="aligncenter  wp-image-407" alt="Console" src="http://www.forwardingplane.net/wp-content/uploads/2013/01/Console-1024x658.png" width="491" height="316" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/01/Console-1024x658.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/01/Console-300x193.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/01/Console-550x353.png 550w, http://www.forwardingplane.net/wp-content/uploads/2013/01/Console.png 1153w" sizes="(max-width: 491px) 100vw, 491px" /></a>
</p>

&nbsp;

The best part about this is that it allows for really flexible management of virtual machines from a geographically different location.  Other than the initial install of CentOS 6, this was done 100% remotely, without a windows host and without an expensive hypervisor license. This is perfect for labs and learning virtualization, I&#8217;d even consider this totally fine for production.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-386" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-386" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-386" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-386" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/01/headless-virtualbox-host-on-centos/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

Let me preface this post by saying that I am absolutely not an enterprise IT or systems guy, take everything that I write here on out with that as a side dish.  I&#8217;m also very, very cheap.  
That said, one of the things I really like about KVM is the ability to easily view the console of a guest system using free, non-windows software like VNC. However, much like everything in life, there are reasons to do one thing or another. I love VMware as well. It&#8217;s refined, well documented, incredibly feature rich and works phenomenally well. It&#8217;s also an enterprise app and to get a lot of the elegant features you either need a windows machine or the expensive paid version. Or both.  
I generally have neither money to spend on lab stuff or software licenses, which is why I generally use OSS. VMware, does, however, allow for free limited use of ESXi in such a way that is more than I need for my lab environments.  This is a great compliment to the XEN, KVM and other virtualization stuff I use for entertaining myself, learning new tech and labbing things up.

So, when I wanted to see if I could get to the console of a few VMs I have without the paid app or a windows machine running vsphere, <a href="http://t3chnot3s.blogspot.com/2012/03/how-to-enable-vnc-access-to-vms-on.html" target="_blank">the internets took care of me</a>.  This is actually really straight forward and takes very little time.  I made a quick screen cast of adding it to one of my template VMs.



There are, of course, a few caveats.  Knowing how to <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1714" target="_blank">properly edit the VMX file </a>is important.  Knowing that VNC is insecure is also very important. In my lab, this is all behind my security perimeter and it&#8217;s fairly safe to open it up.

In a nutshell, Here is what you need to do:

<pre>chmod 777 /etc/vmware/firewall/service.xml</pre>

Edit the firewall file:

<pre>vi /etc/vmware/firewall/service.xml</pre>

Add this to the bottom before the last line:

    
    <!-- VNC -->
      <service id="0033">
        <id>VNC</id>
        <rule id='0000'>
            <direction>outbound</direction>
            <protocol>tcp</protocol>
            <porttype>dst</porttype>
            <port>
               <begin>5800</begin>
               <end>5999</end>
            </port>
         </rule>
         <rule id='0001'>
            <direction>inbound</direction>
            <protocol>tcp</protocol>
            <porttype>dst</porttype>
            <port>
               <begin>5800</begin>
               <end>5999</end>
            </port>
         </rule>
         <enabled>true</enabled>
         <required>false</required>
      </service>
    

Make sure the ports are configured at you want them to be. I chose 5900 &#8211; 5999 since it made sense to me.

Then:

<pre>esxcli network firewall refresh
esxcli network firewall ruleset list</pre>

Should now see:

<pre>VNC true</pre>

at the very bottom.

In the .vmx file of each VM:

<pre>RemoteDisplay.vnc.enabled = "TRUE"
RemoteDisplay.vnc.port = 5910
RemoteDisplay.vnc.password = "VNCPassword"</pre>

Directly from the VMware site:

Any manual additions to the .vmx file from ESX/ESXi are overwritten by the entries stored in the vCenter Server database.

If you need to edit a virtual machine&#8217;s .vmx file, first remove it from vCenter Server&#8217;s inventory (right-click it and choose Remove from Inventory). After you edit it, register the virtual machine again from the ESX command line.

<pre>vmware-cmd -s register /vmfs/volumes/datastore/virtual machine directory/virtual machine name.vmx</pre>

Where datastore is the datastore name, virtual machine directory is the directory containing the virtual machine files, and virtual machine name is the name of the virtual machine files. This needs to be the full path, it gave me a weird error trying to do it in the directory without the full path.

For example:

<pre>vim-cmd solo/registervm /vmfs/volumes/Storage1/vm1/vm1.vmx</pre>

Start the VM and connect to the VNC console configured.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-611" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-611" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-611" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-611" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/04/vnc-console-on-vmware-esxi/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
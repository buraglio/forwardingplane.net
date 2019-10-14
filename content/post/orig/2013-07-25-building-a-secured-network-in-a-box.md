In many environments, the move to virtualization is a path well traveled.  My home and lab networks are no exception to this and I&#8217;m sure nearly everyone who reads these pages has at least been exposed to it in one way or another.  I have played with nearly all of the virtualization platforms and am firmly in the camp that there will be a large segment of networking that will move to a virtualized platform especially in the data center and campus segments.  Virtualization of routing tables has existed for a long time, see <a href="http://en.wikipedia.org/wiki/Virtual_Routing_and_Forwarding" target="_blank">VRF-Lite  and MPLS VRF </a>as well as multi-tenancy technologies like Junipers logical systems so the concept, at some level, has existed in networking for quite some time.

&#8220;How is a small to medium sized environment going to take advantage of this and more interestingly, how can it be secured?&#8221;

[<img class="alignleft  wp-image-732" alt="Red_onions" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions-1024x763.jpg" width="368" height="275" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions-1024x763.jpg 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions-300x223.jpg 300w, http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions-550x410.jpg 550w, http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions.jpg 1600w" sizes="(max-width: 368px) 100vw, 368px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/Red_onions.jpg)This is a question I inadvertently found at least one answer to when building out my own network and testing a great little project called <a href="http://securityonion.blogspot.com/" target="_blank">security onion</a>.  I&#8217;d seen and used this platform a bit in the past, but it had been at least a version ago and my exposure was pretty short.

The problem now, though, was that everything I have in use other than a gigabit switch and a NAS is virtualized.  My firewall, my router, all of my dev and test boxes and all but one of my non-portable machines.  All VMs.  I&#8217;d gone back and forth between VMware and KVM, and while I like KVM better, management of edge case or non-standard networking stuff wasn&#8217;t as well documented and <a href="http://openvswitch.org/" target="_blank">OVS</a> either wasn&#8217;t in the build of CentOS I was using or I didn&#8217;t know about its inclusion yet, so I settled on VMware ESXi 5 for this particular box.  I needed to be able to span a port on a vswitch.  My hopes were not high, but I figured there may be an unsupported way.

Interestingly enough, the VMWare operating system has a mechanism for makeshift &#8220;spanning&#8221; a port.  More correctly, it has a way to see &#8220;all vlans&#8221; on a given vswitch, and it&#8217;s quite simple.  Essentially, you have to create a port group on vlan 4095 on the vswitch then set that port group to promiscuous mode. Add the vm NIC that you are going to use to monitor traffic to that port group.  <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1004099" target="_blank">From VMware site</a>:

[<img class=" wp-image-734 aligncenter" alt="VMWare-site" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site.png" width="582" height="211" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site.png 728w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site-300x108.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site-550x199.png 550w" sizes="(max-width: 582px) 100vw, 582px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-site.png)

I was pleasanty surprised at how easy it was and was at the point of telling security onion to have interfaces on both of the vswitches in less than 15 minutes. Configuration, Networking, Properties, Security. VLAN 4095. Done.Here are a few screenshots of my VMware config following the steps laid out above. It&#8217;s far more simple than I could have imagined.

&nbsp;

[<img class="wp-image-735 alignright" alt="VMWAre-config-networking" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking.png" width="564" height="350" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking.png 783w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking-300x186.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking-550x341.png 550w" sizes="(max-width: 564px) 100vw, 564px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWAre-config-networking.png)

[<img class="alignleft  wp-image-736" alt="VMWare-SPAN-WAN1" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1.png" width="452" height="332" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1.png 754w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1-300x220.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1-550x403.png 550w" sizes="(max-width: 452px) 100vw, 452px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-WAN1.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

[<img class=" wp-image-737 alignright" alt="VMWARE-Span-WAN2" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWARE-Span-WAN2.png" width="300" height="373" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWARE-Span-WAN2.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

At this point Security onion was able to see what was going on.  In my case I allowed for visibility on both sides of my routing firewall, so there was a decent amount of data.

&nbsp;

&nbsp;

This is the interesting part, I think.  My initial thoughts are that this could be a &#8220;network in a box&#8221; for small offices.  No router, no servers (other than the VMware host), essentially a fully functional &#8220;enterprise&#8221; network of hosts, including a very high quality IDS device in a single device.  Put whatever firewall / vrouter in there that is supported or familiar, <a href="http://www.pfsense.org" target="_blank">pfsense</a>, <a href="http://www.juniper.net" target="_blank">Juniper vSRX</a>, <a href="http://www.fortinet.com" target="_blank">fortinet</a>, <a href="http://www.paloaltonetworks.com" target="_blank">Palo Alto</a>, they all have virtual devices and they all do a fine job [with the exception of IPv6; the only one I could get DHCPv6-PD to work with was pfsense.  Still need to test the fortinet].

Here is a high level diagram of how mine is put together. [<img class="alignright size-full wp-image-742" alt="VMWare SPAN" src="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN.jpg" width="488" height="425" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN.jpg 488w, http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN-300x261.jpg 300w" sizes="(max-width: 488px) 100vw, 488px" />](http://www.forwardingplane.net/wp-content/uploads/2013/07/VMWare-SPAN.jpg)

Is this a viable option?  I have no idea, but it does work pretty darned well.  In fact, ironically enough, the day I got this working (July 13, 2013), a post went up over at <a href="http://www.geekempire.com/2013/07/virtual-security-onion-via-ubuntu-kvm.html" target="_blank">GeekEmpire</a> doing almost exactly the same thing with KVM and OVS.  The setup is shockingly similar, right down to using pfSense. I was actually a bit envious, not only because his post went up first, but because he did what I had actually wanted to do by using KVM and OVS.  It&#8217;s well done, I recommend reading it.

I think this is a sign of what will come.  &#8220;network in a box&#8221; is an intriguing concept, and I&#8217;m absolutely <a href="https://www.google.com/search?q=network+in+a+box&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb" target="_blank">positive I am not the only one thinking about it</a>.  I think, however, that the important part is to see the options available and make sure the masses know that there are many ways to do it.  It is not VMware or nothing, and it&#8217;s certainly not cisco or the highway.  OpenSource tools like OVS and KVM under a free operating system like Linux can compete at the highest levels and there are documents and how-tos out there.  More importantly, it&#8217;s not hard.  The same goes for security appliances and even vrouters.  Security Onion and pfSense are both viable platforms and they&#8217;re just the tip of the iceberg.  At the end of the day it all comes down to options. Opensource, commercial, they all have virtualization strategies and the more you know the better off you&#8217;ll be in the long run because virt is here to stay.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-731" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-731" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-731" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-731" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

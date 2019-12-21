In the last few years I have moved all of my virtualization to [proxmox](https://www.proxmox.com/en/) and docker. Seeing as I like to look at packets because I am a closet security guy, and being as I have been working off-and-on on a security project in recent times, I wanted to be able to span a port not only from a hardware switch, but also within my software switches. I had been using linux bridge, which I am not a fan of, so when I started down this path I did not look hard to find a way to do so under that platform. Instead I used it as an opportunity to move some of the internal bridges to [OpenVSwitch](http://openvswitch.org/). I wanted to create an OVS span port internally.

I had experience with OVS in the past for SDN work that I was doing, but I had never created a mirror port. I briefly thought about using OpenFlow to do it, but the unnecessary complexity was off putting. Instead I chose to create a simple mirror of a span port from my switch. So, traffic flow goes as such:

[<img class="wp-image-1383 size-full alignleft" src="http://www.forwardingplane.net/wp-content/uploads/2017/03/OVS-SPAN-1.png" alt="" width="573" height="148" />](http://www.forwardingplane.net/wp-content/uploads/2017/03/OVS-SPAN-1.png)

&nbsp;

&nbsp;

This was fairly trivial, and I was seeing packets in no time. I&#8217;m not going to go through creating an OVS bridge in proxmox, there are lots of [documents](https://pve.proxmox.com/wiki/Open_vSwitch) on how to do that. Once you have your switch port SPAN up and running, and the physical interface in the OVS bridge, you essentially just need to add the following:

Create the mirror

<pre>ovs-vsctl -- --id=@m create mirror name=span -- add bridge vmbr1 mirrors @m</pre>

Find your ports that you want to mirror &#8211; you&#8217;ll need the physical port if consuming from a real switch like I am, and the software port of the virtualized analyzer.  Remember, in OVS anything you want to mess with is going to have a UUID. You need to match the interfaces with the UUID to verify.

ovs-vsctl list port  
_uuid : <span style="color: #ff0000;">42dbd5a9-27c6-4f1b-958b-943f67b6801b</span>  
bond_downdelay : 0  
bond\_fake\_iface : false  
bond_mode : []  
bond_updelay : 0  
external_ids : {}  
fake_bridge : false  
interfaces : [<span style="color: #000000;">b155454d-db6e-4bb8-af88-7cd6b544c303</span>]  
lacp : []  
mac : []  
name : &#8220;<span style="color: #ff0000;">eth1</span>&#8221;  
other_config : {}  
qos : []  
statistics : {}  
status : {}  
tag : []  
trunks : []  
vlan_mode : []

_uuid : 85c932b2-4f98-4650-8298-ae9e9ca72796  
bond_downdelay : 0  
bond\_fake\_iface : false  
bond_mode : []  
bond_updelay : 0  
external_ids : {}  
fake_bridge : false  
interfaces : [5219306f-96ec-440a-ac8b-d949ea18d752]  
lacp : []  
mac : []  
name : &#8220;vmbr1&#8221;  
other_config : {}  
qos : []  
statistics : {}  
status : {}  
tag : []  
trunks : []  
vlan_mode : []

_uuid : <span style="color: #ff0000;">d53c7323-517f-48a2-9235-4505e654d4b1</span>  
bond_downdelay : 0  
bond\_fake\_iface : false  
bond_mode : []  
bond_updelay : 0  
external_ids : {}  
fake_bridge : false  
interfaces : [91d52d05-d881-4693-ab5c-fc64b5d87518]  
lacp : []  
mac : []  
name : &#8220;<span style="color: #ff0000;">veth100i9</span>&#8221;  
other_config : {}  
qos : []  
statistics : {}  
status : {}  
tag : []  
trunks : []  
vlan_mode : []

In red we have the interfaces I want to to use. the veth interface is the software port on the VM. Eth1 is the hardware interfce that my switch is spanning traffic to. Pro tip: In OVS, the commands are a little unintuitive to me when talking about mirrors.  &#8220;select\_src\_port&#8221; and &#8220;select\_dst\_port=&#8221; is the destination of the traffic flow from an interface and not source and destination of the traffic you are mirroring from the point of view of the in and out ports. Confusing, right? For instance I can monitor the input from one interface and the output of another in the mirror. What we want is the input and output of the same interface to get both directions of traffic. This is not unlike how span ports are configured on your hardware switch, the nomenclature just threw me off.

<pre>ovs-vsctl set mirror span select_src_port=@eth1 select_dst_port=@eth1</pre>

You can also do this with the UUID

<pre>ovs-vsctl set mirror span select_src_port=42dbd5a9-27c6-4f1b-958b-943f67b6801b select_dst_port=42dbd5a9-27c6-4f1b-958b-943f67b6801b</pre>

Now that we have the source of our mirror we just need to send it somewhere. I wanted mine to go to an internal host running some analytics software (on interface veth100i9)

<pre>ovs-vsctl -- --id=@veth100i9 get port veth100i9 -- set mirror span output-port=@veth100i9</pre>

And that&#8217;s it. Log into your host and do a tcpdump on whatever interface is mapped to veth100i9 and you should see packets flowing. A few tips:

  * Verify your span from the hardware switch is working before diving into the software stack.
  * If you&#8217;re doing this is proxmox, be aware that proxmox networking stack can be unforgiving when you much around outside of their environment.
  * This will not persist across reboots. Add it to /etc/network/interfaces manually to keep it after a restart.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1380" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1380" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1380" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1380" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2017/03/creating-internal-span-port-inside-proxmox-ovs/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
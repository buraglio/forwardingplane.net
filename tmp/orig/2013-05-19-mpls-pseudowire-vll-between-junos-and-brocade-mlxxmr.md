I love to be the &#8220;uncola&#8221; of networking sites.  I like interop and I don&#8217;t do a lot with Cisco because I don&#8217;t have access to much of their gear anymore.  So, that being the case, I had a need to bring up a l2circuit (in JunOS speak), or VLL (in Brocade speak) between an MX480 and an MLX.  Since they are very different platforms, I had to do some digging and playing around to get it to work.  
You should have a rudimentary understanding of MPLS (which is about what I have) to do this. l2circuit / pseudowire / vll are all synonymous for the scope of this post. 

JunOS:

<pre>set protocols l2circuit neighbor interface virtual-circuit-id
set protocols l2circuit neighbor interface encapsulation-type ethernet

set interfaces xe-3/3/0 description
set interfaces xe-3/3/0 vlan-tagging
set interfaces xe-3/3/0 encapsulation flexible-ethernet-services
set interfaces xe-3/3/0 unit encapsulation vlan-ccc
set interfaces xe-3/3/0 unit vlan-id</pre>

Brocade:

<pre>MLX1#show mpls config
router mpls
policy
no propagate-ttl

mpls-interface e1/1
ldp-enable

mpls-interface e1/4
ldp-enable

vll TEST-ICCN-VLL-1 raw-mode
vll-peer
vlan
tagged e 5/2</pre>

Some commands I found helpful for debugging while testing this out:

JunOS:  
Useful for debugging connections that won&#8217;t come up:

<pre>set protocols l2circuit traceoptions file l2-VLL
set protocols l2circuit traceoptions file size 20240
set protocols l2circuit traceoptions flag all
show log l2-VLL</pre>

Brocade:

<pre>logging console
terminal monitor
debug mpls all
debug mpls ldp</pre>

Show commands that are very useful:

JunOS:  
check end to end l2circuit / VLL connectivity

<pre>ping mpls l2circuit interface &lt;interface.unit> detail</pre>

Show detail of l2circuit / pseudowire / vll  
show interfaces <interface.unit> extensive # or detail

Brocade:

<pre>show VLL detail &lt;VLL id></pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-644" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-644" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-644" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-644" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/05/mpls-pseudowire-vll-between-junos-and-brocade-mlxxmr/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

One of our plans is to consolidate as many of the egress trafic paths as possible.  To facilitate this, we had to do some things like buy carrier grade equipment.  Enter the [SRX 5800](http://bit.ly/9jrUiG).  No one really does IPS/IDP+Firewall quite like the SRX.  After extensive research and exhaustive hands on testing with quite a bit of equipment, that is what we settled on.  Even the IBM &#8220;technical evangelist&#8221; guy that came to talk to us said &#8220;No one really does it like they do&#8221; when referring to Juniper and 10G firewall/IPS. 

<div style="clear: both; text-align: center;">
  <a href="http://www.juniper.net/shared/img/products/srx-series/srx5800/lbox-srx5800-left.jpg" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="320" src="http://www.juniper.net/shared/img/products/srx-series/srx5800/lbox-srx5800-left.jpg" width="234" /></a>
</div>

Lets make one thing clear, IPv6 isn&#8217;t going away.  We&#8217;ll all be using in in the next few years, and so, to that end, it needs to work through our network as closely to the way folks are using the current resources as we can make it&#8230;.within the confines of our resources and the limitations of IPv4 and IPv6 respectively.

To make IPv6 process similarly to IPv4 on the SRX 5800 cluster, we have to enable flow based security processing for it.  To make that happen, you have to do the following things, as documented [here](http://bit.ly/9jrUiG):

<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">set security forwarding-options family inet6 mode flow-based</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><br /></span>  
Enabling this actually requires a reboot of the boxes, and on a chassis cluster, I&#8217;ve been told by our Agility JTAC guy (and learned the herd way because I&#8217;m stubborn like that) that you need to reboot both cluster nodes at the same time (which I find dumb since the purpose of a firewall cluster is almost always redundancy).

Regardless, I used the recommended method and kicked the boxes after a commit check. 

<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">commit check</span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>  
<span style="font-family: inherit;">The router then spits out the following information after the commit check:</span>  
<span style="font-family: inherit;"><br /></span>

<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">node0:</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">warning: You have enabled/disabled inet6 flow.</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">You must reboot the system for your change to take effect.</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">If you have deployed a cluster, be sure to reboot all nodes.</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">configuration check succeeds</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;"><br /></span> </span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;"><br /></span> </span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">node1:</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">warning: You have enabled/disabled inet6 flow.</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">You must reboot the system for your change to take effect.</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">If you have deployed a cluster, be sure to reboot all nodes.</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">configuration check succeeds</span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>  
<span style="font-family: inherit;">From here I like to comment all of my commits, as it&#8217;s just good practice and it will be logged on your handy <a href="http://campin.net/syslog-ng/faq.html">syslog server</a> for later use or reference.</span>  
<span style="font-family: inherit;"><br /></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">commit comment &#8220;Enabling Flow-Based Processing for IPv6 Traffic&#8221;</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><br /></span>  
And from there, a reboot of both nodes (at the same time) is necessary..

<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">request system reboot</span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>  
<span style="font-size: small;"><span style="font-family: inherit;">And then, we wait&#8230;&#8230; </span></span>

<span style="font-size: small;"><span style="font-family: inherit;">&#8230;..and wait some more&#8230;</span></span>

<span style="font-size: small;"><span style="font-family: inherit;">&#8230;.and then&#8230;..the prompt on the console is back.</span></span>

<span style="font-size: small;"><span style="font-family: inherit;">&#8230;&#8230;&#8230;..and after about 6-7 minutes, we have OSPF adjacencies and packets are flowing.  The SPCs take a bit to self test, fully boot and start processing traffic, as I would expect from something processing so many pieces of so much traffic.  </span></span>

<span style="font-size: small;"><span style="font-family: inherit;">Now we need to verify that what we did actually worked.  From the SRX, check the security flow status:</span></span>  
<span style="font-size: small;"><span style="font-family: inherit;"><br /></span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">show security flow status</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;"><br /></span></span>

<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">node0:</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">  Flow forwarding mode:</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Inet forwarding mode: flow based</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Inet6 forwarding mode: flow based</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    MPLS forwarding mode: drop</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    ISO forwarding mode: drop</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Flow trace status</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Flow tracing status: off</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;"><br /></span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">node1:</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">  Flow forwarding mode:</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Inet forwarding mode: flow based</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Inet6 forwarding mode: flow based</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    MPLS forwarding mode: drop</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    ISO forwarding mode: drop</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Flow trace status</span></span>  
<span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Flow tracing status: off</span></span>

We&#8217;re looking for:



<div style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;">
  <span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;">    Inet6 forwarding mode: flow based</span></span>
</div>

<div>
  <span style="font-family: 'Courier New', Courier, monospace;"><span style="font-size: small;"><br /></span></span>
</div>

<div>
  <span style="font-family: inherit;">This would have said &#8220;<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;">drop</span></span>&#8221; before the change. </span>
</div>

<div>
  <span style="font-family: inherit;"><br /></span>
</div>

<span style="font-size: small;"><span style="font-family: inherit;">We hope to actually swing over our IPv6 traffic soon and start processing it on the SRXs.  I&#8217;ll post notes as soon as we go forward with that.  </span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>  
<span style="font-size: small;"><span style="font-family: 'Courier New', Courier, monospace;"><br /></span></span>

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-50" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-50" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-50" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-50" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2010/09/srx-ipv6-flow-based-processing/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

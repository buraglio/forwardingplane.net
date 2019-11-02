<span style="font-weight: 400;">    Remember OpenFlow? It was the media and marketing darling for the better part of 5 years as “the machine” conflated OpenFlow with SDN and SDN with &#8211; almost literally &#8211; everything. &#8220;Still Does Nothing&#8221; was a common phrase uttered around those of us that had run large scale, complex networks for a long time. Quietly, </span>[<span style="font-weight: 400;">and mostly</span>](https://faucet-sdn.blogspot.com/)<span style="font-weight: 400;">, out of the fickle media and blogosphere eye, a scrappy little SDN project called </span>[<span style="font-weight: 400;">faucet</span>](https://github.com/faucetsdn/faucet) <span style="font-weight: 400;">has been </span>[<span style="font-weight: 400;">diligently plugging away</span>](https://github.com/faucetsdn/faucet) <span style="font-weight: 400;">&#8212; making easy to use, production quality, well documented, and very stable code that runs OpenFlow networks quite happily in production and at scale. Oh, did I mention that it&#8217;s also got a very small footprint? Did I also mention that we&#8217;ve built a multi-terabit network</span> <span style="font-weight: 400;">that </span><span style="font-weight: 400;">scales, transiting IPv4, IPv6, L2/L3 switching as well as routing? Or that faucet </span><span style="font-weight: 400;">can control switches from multiple vendors, including P4 vendors who provide a P4-to-OF bridge, and interoperates with non-SDN networks? Or (and possibly most importantly) that faucet provides automated integration tests, allowing many bugs to be caught early (sometimes even by the switch vendor) before shipping new releases? </span>

<span style="font-weight: 400;">    Well, I should probably mention those things. I&#8217;ve been lucky enough to have been involved in SDN off and on since around 2009, and I can emphatically say that of the production SDN and OpenFlow networks that I have been intimately involved in, this combination of hardware, software and people has been, hands down, the most rewarding and most supportable. In fact, this has been so supportable and great to work with, we migrated our production branch office over to a set of faucet controlled SDN switches, and will soon migrate first hop routing over to our robust faucet system. &#8220;However did you do this?!?!&#8221; you might be inclined to say. Well, I&#8217;m glad you asked, because I am going to tell you. </span>

 <span style="font-weight: 400;">   First, though, there should be some design goals. As many of the naysayers of SDN will happy point out, &#8220;what problem are you trying to solve?&#8221; to that end, here is what our design goals were:</span>

<li style="font-weight: 400;">
  <span style="font-weight: 400;">Run all layer 2 in via </span><span style="font-weight: 400;">faucet</span>
</li>
<li style="font-weight: 400;">
  <span style="font-weight: 400;">Remove need to log into any network elements after deployment (other than firmware updates)</span>
</li>
<li style="font-weight: 400;">
  <span style="font-weight: 400;">Centralize management</span>
</li>
<li style="font-weight: 400;">
  <span style="font-weight: 400;">Stretch goal to NFV BGP, do first hop L3</span>
</li>

<span style="font-weight: 400;">    Easy enough, right? It really is. For our deployment we leveraged Aruba 2930F switches giving us a wealth of 1G copper ports and a handful of 10G SFP+ ports. Luckily, we already had this gear because as so many that have tried to deploy openflow in the past have seen, all hardware is not created equally. Luckily, the </span>[<span style="font-weight: 400;">faucet foundation</span>](https://www.faucet.org.nz/) <span style="font-weight: 400;">has published a list of requirements for support, and there are a reasonable number of vendors that actually conform. The real key that I learned in this process is that without proper vendor support (which had been several lacking in the past), and without multi-table, OpenFlow is not positioned for success. It comes down to using the right tools for the job, and OpenFlow (as well as SDN) is no different. </span>

<span style="font-weight: 400;">    Originally this post was to detail the process of building this network, much like posts in the past where there has been a “do this, then do that” how-to, it’s more or less unnecessary here. Why? The </span><span style="font-weight: 400;">faucet</span> <span style="font-weight: 400;">project is serious, well documented and generally here to work. The expectation is that this is not an enclave, or a science experiment, or a lab. It’s a production network with real people and real traffic. Read that again. The expectation is that this is stable, supportable, and can do in ready to use day-to-day. And it doesn’t disappoint. Installing is a snap, the</span> [<span style="font-weight: 400;">documentation</span>](https://docs.faucet.nz/en/latest/tutorials/first_time.html) <span style="font-weight: 400;">for </span><span style="font-weight: 400;">faucet</span> <span style="font-weight: 400;">is fantastic and complete. If there is something missing or a question, the developers are incredibly responsive and very quick to answer and address any issues that may arise. It’s extremely low footprint &#8211; it runs very well on a raspberry pi and does not tax a raspberry pi series 2, even with the gauge telemetry interface (there is a</span> [<span style="font-weight: 400;">pre-built pi OS</span>](https://docs.faucet.nz/en/latest/installation.html#installing-on-raspberry-pi) <span style="font-weight: 400;">for anyone that would prefer a more turnkey option). You may be thinking “</span>_<span style="font-weight: 400;">But Nick, I need my CLI!!!</span>_<span style="font-weight: 400;">” You’re covered &#8211; and here is why: the developers use this system. They run real networks with it. Every day. They know what is necessary to manage and maintain a real production network and sometimes that means troubleshooting. Like many engineers that learned on traditional network equipment, most of us prefer a CLI to troubleshoot, so the inclusion of this feature from the controller is not really a surprise. The </span><span style="font-weight: 400;">fctl</span> <span style="font-weight: 400;">command provides a reasonable visibility into the operations of the controller and can be augmented and scripted. </span>

<pre><span style="font-weight: 400;">buraglio@faucet:~ $ /usr/bin/fctl --help</span>

<span style="font-weight: 400;">usage:</span>

<span style="font-weight: 400;">    MACs learned on a DP.</span>

<span style="font-weight: 400;">    /usr/bin/fctl -n --endpoints=</span><a href="http://172.17.0.1:9302"><span style="font-weight: 400;">http://172.17.0.1:9302</span></a><span style="font-weight: 400;"> --metrics=learned_macs --labels=dp_id:0xb827eb608918</span>

<span style="font-weight: 400;">    Status of all DPs</span>

<span style="font-weight: 400;">    /usr/bin/fctl -n --endpoints=</span><a href="http://172.17.0.1:9302"><span style="font-weight: 400;">http://172.17.0.1:9302</span></a><span style="font-weight: 400;"> --metrics=dp_status</span>

<span style="font-weight: 400;">Retrieve FAUCET/Gauge state using Prometheus variables.</span>

<span style="font-weight: 400;">optional arguments:</span>

<span style="font-weight: 400;">  -h, --help            show this help message and exit</span>

<span style="font-weight: 400;">  -n, --nonzero         nonzero results only</span>

<span style="font-weight: 400;">  -e ENDPOINTS, --endpoints ENDPOINTS</span>

<span style="font-weight: 400;">                        list of endpoint URLs to query</span>

<span style="font-weight: 400;">  -m METRICS, --metrics METRICS</span>

<span style="font-weight: 400;">                        list of metrics to query</span>

<span style="font-weight: 400;">  -l LABELS, --labels LABELS</span>

<span style="font-weight: 400;">                        list of labels that must be present</span>

<span style="font-weight: 400;">  --display-labels DISPLAY_LABELS</span>

<span style="font-weight: 400;">                        list of labels to filter display by (default all)</span></pre>

<span style="font-weight: 400;">Monitoring is also taken into account in the form of the gauge interface, which provides a nearly-real-time telemetry stream of important and useful information. Leveraging both the wealth of topological information that the controller has at its disposal and a familiar </span>[<span style="font-weight: 400;">prometheus</span>](https://github.com/prometheus) <span style="font-weight: 400;">/ </span>[<span style="font-weight: 400;">grafana</span>](https://grafana.com/) <span style="font-weight: 400;">back / front end interface, the oft-touted notion of streaming telemetry is fully &#8211; and quite capably &#8211; realized. From the perspective of a networking monitoring and statistics geek, this is the cat’s meow. Very, very data rich.</span>

[<img class="aligncenter size-large wp-image-1501" src="http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap-1024x275.png" alt="" width="735" height="197" srcset="http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap-1024x275.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap-300x80.png 300w, http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap-768x206.png 768w, http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap.png 1600w" sizes="(max-width: 735px) 100vw, 735px" />](http://www.forwardingplane.net/wp-content/uploads/2018/11/grafana-screencap.png)

<span style="font-weight: 400;">A simple diagram of our office network pretty well explains the decoupled control plane architecture. Keep it simple, architect for success. Fundamentally SDN networks should be designed like other networks, redundant systems, good monitoring, out of band access. A good design principle is that if you wouldn’t do it on a traditional network, you probably shouldn’t do it for an SDN based network.   <a href="http://www.forwardingplane.net/wp-content/uploads/2018/11/faunet-office.png"><img class="alignright wp-image-1500" src="http://www.forwardingplane.net/wp-content/uploads/2018/11/faunet-office.png" alt="" width="563" height="703" srcset="http://www.forwardingplane.net/wp-content/uploads/2018/11/faunet-office.png 740w, http://www.forwardingplane.net/wp-content/uploads/2018/11/faunet-office-240x300.png 240w" sizes="(max-width: 563px) 100vw, 563px" /></a></span>

&nbsp;

<span style="font-weight: 400;">Don’t trust me? Fair enough, check out the </span>[<span style="font-weight: 400;">University of Waikato</span>](https://www.waikato.ac.nz/research/units/wand.shtml) <span style="font-weight: 400;">interface </span>[<span style="font-weight: 400;">here</span>](https://grafana.redcables.wand.nz/d/000000003/redcables-bgp?orgId=1)<span style="font-weight: 400;">. For more interface on the deployment at </span>[<span style="font-weight: 400;">WAND</span>](https://wand.net.nz/)<span style="font-weight: 400;">, check</span>[ <span style="font-weight: 400;">this link</span>](https://redcables.wand.nz/)<span style="font-weight: 400;">. You won’t be disappointed.  </span>

&nbsp;

## <span style="font-weight: 400;">My take</span>

###  <span style="font-weight: 400;">Building and running it</span>

 <span style="font-weight: 400;">   The </span>[<span style="font-weight: 400;">documentation for faucet</span>](https://docs.faucet.nz/en/latest/) <span style="font-weight: 400;">is indescribably better than any other SDN</span> <span style="font-weight: 400;">project I have worked with over the span of nearly 10 years.</span> **It’s also supportable.** <span style="font-weight: 400;">My office has been running the enterprise network off of faucet for a while now, without issue, and it meets our design goals [stretch goal of BGP NFV is still in process &#8211; testing is successful]). It is easy to manage and very information rich. I can see security minded folks being very interested in the ACLs and other such options available. </span>

### <span style="font-weight: 400;">Telemetry and analytics    </span>

 <span style="font-weight: 400;">   Where so many others in this space are talking about their Telemetry solution, this one is already here, complete, and usable. Frankly, I am fully comfortable running a production network on this technology, operationally it is truly easier. From a security perspective, the options added scale well and deliver on their promise. Where OpenFlow was once touted as the networking silver bullet (without a lot of real stick time to prove or disprove it), it has now fallen comfortable into a nice, supportable model. </span>

### <span style="font-weight: 400;">Up next….    </span>

 <span style="font-weight: 400;">   If you think this is cool, wait until </span>[<span style="font-weight: 400;">SuperComputing 18</span>](https://sc18.supercomputing.org/)<span style="font-weight: 400;">, where we’re deploying a</span>[ <span style="font-weight: 400;">first-of-it’s kind network</span>](https://www.linkedin.com/feed/update/urn:li:activity:6461072411969363968/)<span style="font-weight: 400;">, all controlled by FAUCET. </span>

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1499" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1499" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1499" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1499" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2018/11/faucet-enterprise-openflow-in-production/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
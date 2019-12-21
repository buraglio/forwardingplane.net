Over the last few days there has been a _**huge**_ amount of FUD and panic surrounding two as-yet-to-be-published CVEs (found [here](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-19298) and [here](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-19299)) related to Mikrotik&#8217;s IPv6 implementation.It is my opinion that this entire process has been poorly handled, and that the community involved tends to be fairly sensitive to issues such as, and the cloak and dagger nature of the two issues has only exacerbated it. Mikrotik, as a company, is well known for being terse in their responses and tight lipped with their internal workings and dealings with these kinds of issues. I take that as a given, that’s their business and realistically we’re entitled to know exactly none of that information, even if it would be nice to have it. The history behind this is discouraging, the original discovery was quite some time ago with reports dating back to 2013, and the person who originally uncovered the issues did so upwards of a year ago, bringing them to Mikrotik at that time, as can be seen in this [thread](https://forum.mikrotik.com/viewtopic.php?f=2&t=125841&p=654116&hilit=ndpexhaust26#p654116). Now, anyone with a passing knowledge of pen testing or IPv6 device load testing can trivially put together the information needed to decipher the problem and replicate it, neither are exactly complicated or [new](https://insinuator.net/2013/03/ipv6-neighbor-cache-exhaustion-attacks-risk-assessment-mitigation-strategies-part-1/). Both can be done in literally one line of [common, open source toolkits.&nbsp;](https://tools.kali.org/information-gathering/thc-ipv6)&nbsp;The issues are not magical and are not even esoteric or cryptic. They are very straightforward, and by reading the threads and understanding how things like route caches and [neighbor discovery](https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol) work, they become very clear.

Since this is IPv6 related I am very interested in it because I feel that WISPs and emerging markets are an excellent environment for moving IPv6 forward, and the equipment and mindset involved makes that fairly straightforward. Reverse engineering these given the information available is pretty straightforward, and [folks other than me have done it](https://www.iparchitechs.com/) too.

I personally do not consider either of these a security vulnerability or a bug, per se. They’re both the result of a short sighted protocol implementation resulting in a very acute, unfortunate event. With the benefit of hindsight, and as an outsider, I can only wonder if this had been handled differently (i.e. not framed as a critical security vulnerability but rather a broken protocol), if the hysteria that resulted could have been quelled. On a [particular forum thread,](https://forum.mikrotik.com/viewtopic.php?f=2&t=147048&start=50) this was likened to the discovery of the “ping of death”, and that feels like a good analogy to me. &nbsp;It probably should have been handled that way.

So, I will post my .02 as to how this kind of even can be handled in the future, in case there is no better process to work with:

1. Involve the vendor early.

2. Involve a trusted third party to validate the result. It’s very easy to miss trees when you’re stuck in a forest. 3rd party validation is pretty important either way as it proves a problem can be repeated independently.

3. Disclose the environment hardware, in detail, that was used to test and confirm the the issue in.

4. Have both validated it with said trusted, embargoed outside source(s). Again, ideally one is the vendor.

5. If unable to define and at least indicate that there is a remediation,&nbsp;leverage outside trusted source to **make sure that’s not possible**. In this case, that seems to be kept between the person who discovered it and the vendor, which as discussed above has a track record of being pretty closed off.

For this particular issue and platform, one can monitor the IPv6 route-cacheing near real-time, here is the command to do it at 1 second intervals

<pre>[buraglio@gw] &gt; /ipv6 route cache print interval=1
cache-size: 190max-cache-size: 1024000</pre>

The ND issue can be mitigated with the following command (obviously adjusted for your own environment).

<pre>/ipv6 firewall filter
add action=drop chain=forward connection-mark=drop connection-state=new
/ipv6 firewall mangle
add action=accept chain=prerouting connection-state=new dst-address=\
2001:db8:3::/64 limit=2,5:packet
add action=mark-connection chain=prerouting connection-state=new dst-address=\
2001:db8:3::/64 new-connection-mark=drop passthrough=yes</pre>

And for those more interested in the actual process, here is a video demonstrating the basic route-cache issue (commands, although very easy to figure out are obfuscated)

<p style="text-align: center;">
</p>

Mikrotik has released a fix as of this morning (4/1/2019), although it is currently beta. ROS 6.45 addresses both the route cache and the neighbor table issue. More details on the discovery will be [disclosed at the UKNOF conference](https://indico.uknof.org.uk/event/46/contributions/speakers).

#### My take:

A problem like this that is as egregious as described needs to be independently validated and ideally a remediation found before disclosure. If a mitigation strategy does not exist, the $vendor takes responsibility by default and realistically, nothing can be done until they fix it. It may also be disclosed as a zero-day-style, weaponized tactic. Obviously that is the worst case. The real point is that we’re a community, and we need to build the trust frameworks to work together on issues such as this without pointing fingers or running around with our hands waving.

This behavior is, sadly, pretty easy to re-create. There is an old thread that implies some of this was triggered by &#8220;real traffic&#8221;, and I have definitely seen an uptick in ipv6 scanning that impacts major vendor router platforms to the point that they get salty about traffic flows and spike CPUs. This feels pretty darned similar, but not the catastrophic event horizon it&#8217;s being played out to be. It&#8217;s still bad, it stinks, and it&#8217;s definitely been handled in a way that is less than optimal. I would also like to point out a few things since there has been a fair amount of hair on fire panic. I realize I am being a tad pedantic, but it&#8217;s important to identify things correctly in order to handle them in the correct manner. This is not a security vulnerability as I would describe it. There is no remote or local execution of code, no raised privileges, no mechanism of compromise. I don&#8217;t think this is a software bug, either. It&#8217;s close, but in reality what this is is a poorly implemented protocol that had what I can only believe was a poverty of testing before release and as such allows for a remotely triggered denial of service.  
Denial of service isn&#8217;t necessarily malicious, it just means exactly what it says: service is denied. As mentioned earlier in the thread, this is like the old ping of death issue: a poorly executed stack.

I&#8217;d like to know who has executed this in the wild and how far back this goes in their code train, references go back as far as 2013, but I suspect they go back to the original support.

#### &#8212;- UPDATE

Mikrotik has addressed this issue with the release of ROS 6.44.2. The prior methodologies no longer exhaust resources and reload devices, as can be seen here



<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1647" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1647" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1647" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1647" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2019/03/soap-box-mikrotik-ipv6-apocalypse-or-maybe-not/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
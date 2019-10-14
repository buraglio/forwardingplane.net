I&#8217;m an awful sysadmin.  Running services permanently isn&#8217;t really my forte, I tend to lean more on the &#8220;I&#8217;ll get this proof of concept all working, prove that it works or doesn&#8217;t, then roll it on for polishing by someone else&#8221; kinda guy.  That final 15% is something I&#8217;m constantly working to refine and better myself at accomplishing.   I&#8217;m decent at debugging network services, and can be handy in a &#8220;oh crap, it&#8217;s down!&#8221; scamerio, but day to day sysadmin&#8230;not really my speciality.  
I know enough programming to be dangerous and have enough experience to know how to set up or fix pretty much any OS with nearly any service on it.  15 years as a slash and burn Network Engineer will often lend itself to that.  That being said, I do enjoy playing with new options, software packages and and LOVE instrumentation.  Then I came across <a href="http://host-sflow.sourceforge.net/" target="_blank">this</a>.     <a href="http://blog.sflow.com/2012/01/host-sflow-distributed-agent.html" target="_blank">Host based sflow</a>&#8230;..for more than just network traffic.  
This idea is **<u>fantastic</u>**.  
**Why** did I never think of it?!?!?!?

Essentially it&#8217;s <a href="http://en.wikipedia.org/wiki/SFlow" target="_blank">sflow</a>, a mechanism for monitoring network traffic, or thats at least how I thought of it being from the network side.  It&#8217;s a lot like Netflow, but an open standard.  Many network devices support it for sampling transit routed packets.  It never occured to me to run it on hosts for other things like&#8230;..http hits, disk utilization&#8230;.memory usage.  This seems perfect for a cloud environment, or for a VM farm&#8230;.or anywhere you don&#8217;t want to run snmpd or some weird commercial agent on a host.  
I already have an <a href="http://nfsen.sourceforge.net/" target="_blank">nfsen</a>/<a href="http://nfdump.sourceforge.net/" target="_blank">nfdump</a> instance, but it should work with any open source or commercial collector that supports sflow, which is a huge number.  Intermapper flow, inmon, there is a long list. 

I had to see this work, since we had just discussed this type of monitoring in our new [broadband project of the year award winning] ISP, <a href="http://www.uc2b.net/" target="_blank">UC2B</a> that I am heavily involved in.  
So, on to the meat and potato..  
I grabbed the dpkg and installed it on my personal ubuntu server. 

<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>sudo dpkg -i hsflowd_1.22.2-1_x86_64.deb </i></span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: inherit;">From there I needed to edit the conf file to point it my test flow collector, which happens to reside on the same box.  Use your favorite editor, I like vi personally but I&#8217;ve been using it for 15 years. </span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>sudo vi /etc/hsflowd.conf</i></span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: inherit;">Change the following lines:</span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>DNSSD = off</i></span>

<div>
  <p>
     <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i> polling = 30</i></span><br /><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>  sampling.http = 10</i></span><br /><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>  sampling.memcache = 500</i></span>
  </p>
</div>

<div>
  <div>
    <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i> collector {</i></span>
  </div>
  
  <div>
    <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>    ip = 127.0.0.1</i></span>
  </div>
  
  <div>
    <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>     udpport = 6997</i></span>
  </div>
  
  <div>
    <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>  }</i></span>
  </div>
</div>

<div>
</div>

<div>
  Close out the file.  I chose to tweak a few of the defaults to see what it&#8217;d yield.  
</div>

<div>
</div>

<div>
  Now edit your nfsen.conf file
</div>

_<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">%sources = (</span>_  
_<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">    &#8216;home&#8217;    => { &#8216;port&#8217; => &#8216;6996&#8217;, &#8216;col&#8217; => &#8216;#0000ff&#8217;, &#8216;type&#8217; => &#8216;netflow&#8217; },</span>_  
_<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">    &#8216;cupcake&#8217;    => { &#8216;port&#8217; => &#8216;6997&#8217;, &#8216;col&#8217; => &#8216;#0000ff&#8217;, &#8216;type&#8217; => &#8216;sflow&#8217; },</span>_  
_<span style="font-family: Courier New, Courier, monospace; font-size: x-small;">);</span>_

<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i>sudo /services/netflow/bin/nfsen reconfig</i></span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: inherit;">This should yield at the very least network data and provide a proof of concept. other services can be monitored by using the json options, but that&#8217;s beyond the scope of this writing.  I could see a big win from this in a home brew cloud environment or a large VM farm since it can provide a very straightforward way to generate very useful data in a standard format that can be very simply monitored, queried and archived.    </span>  
<span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><a href="http://gan.doubleclick.net/gan_click?lid=41000000028007181&#038;pid=UBM9786132095695&#038;adurl=http%3A%2F%2Fwww.cdsbooksdvds.com%2Fproduct.jhtm%3Fsku%3DUBM9786132095695&#038;usg=AFHzDLucmjq8niDqbnNmvyDzFPVpDnuqQQ&#038;pubid=590157" rel="nofollow">Paessler Router Traffic Grapher</a></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><i><br /></i></span>

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-18" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-18" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-18" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-18" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

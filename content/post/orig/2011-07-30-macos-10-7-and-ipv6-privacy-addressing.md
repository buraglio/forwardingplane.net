I&#8217;m not a fan of IPv6 privacy addressing. I understand the logic behind it, I really doo, obfuscate the LLADDR (MAC address) of the host in question, but I really dont&#8217;t see the realistic purpose. If someone wanted to use my mac address, what good would that really get them, unless they&#8217;re on the same layer 2 segment? More importantly, if they;re on the same layer 2 segment, they have my MAC address anyway.  
Privacy addresses cause more heartburn than they cure. How do I track someone who has a rotating address? Am I scraping the neighbor table of my network equipment often enough to have reasonable accountability? Probably, but what if I&#8217;m not? I could go on and on about how I think [RFC4941](http://www.ietf.org/rfc/rfc4941.txt) addresses aren&#8217;t that useful, but instead I&#8217;ll just write down how to disable them (I&#8217;ve always been known as more of a machete than a scalpel anyway =).

With MacOS 10.7 (Lion) it&#8217;s now on by default. To disable it, you need to open a terminal and type:

<span><i>sudo sysctl -w net.inet6.ip6.use_tempaddr=0<br /></i></span>  
Poof! There you go.  [You should be using DHCPv6 anyway](http://tech.buraglio.com/2011/07/osx-107-lion-dhcpv6-client-working-with.html) =)  [](http://events.internet2.edu/2011/jt-uaf/agenda.cfm?go=session&id=10001852&event=1151)[**\*cue vendors getting off their rear ends and implementing dhcpv6 relay\***](http://events.internet2.edu/2011/jt-uaf/agenda.cfm?go=session&id=10001852&event=1151)

<div>
</div>

<div>
  <b>&#8212;edit&#8212;</b>
</div>

<div>
  <b>A good point made by Charley Kline, to make this persist across reboots a line needs to be added to your /etc/sysctl.conf. </b>
</div>

<div>
  <b><br /></b>
</div>

<div>
  <b>To accomplish this, edit /etc/sysctl.conf</b>
</div>

<div>
  <b><br /></b>
</div>

<div>
  <i><b>sudo vi /etc/sysctl.conf</b></i>
</div>

<div>
  <b><br /></b>
</div>

<div>
  <b>Add the following line:</b>
</div>

<div>
  <b><br /></b>
</div>

<div>
  <i><b>net.inet6.ip6.use_tempaddr=0</b></i>
</div>

<div>
  <span style="font-family: Helvetica, Arial, sans-serif; font-size: 13px; line-height: 17px; "><b></p> 
  
  <pre style="padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; text-align: left; overflow-x: auto; overflow-y: auto; font-family: 'Courier New', Courier, monospace; line-height: 1.3; "></pre>
  
  <p>
    </b></span></div> 
    
    <div>
      <b>&#8211;edit&#8211;</b>
    </div>
    
    <div>
    </div>
    
    <div>
      For all you windows users:</p> 
      
      <p>
        XP:
      </p>
      
      <div>
        <span><i>netsh interface ipv6 set privacy state=disabled store=persistent<br />netsh interface ipv6 set privacy state=disabled</i></span></p> 
        
        <p>
          Vista:
        </p>
        
        <p>
          <span><i>netsh interface ipv6 set global randomizeidentifiers=disabled<br />netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent<br />netsh interface ipv6 set privacy disabled</i></span>
        </p>
        
        <p>
          I assume Windows 7 is similar to Vista, but I have not tested.
        </p>
      </div>
    </div>
    
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
              <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-32" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
            </li>
            <li class="share-email">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
            </li>
            <li class="share-print">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/" target="_blank" title="Click to print"><span>Print</span></a>
            </li>
            <li class="share-linkedin">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-32" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
            </li>
            <li class="share-facebook">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-32" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
            </li>
            <li class="share-reddit">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
            </li>
            <li class="share-tumblr">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
            </li>
            <li class="share-pinterest">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-32" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
            </li>
            <li class="share-pocket">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/07/macos-10-7-and-ipv6-privacy-addressing/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
            </li>
            <li class="share-end">
            </li>
          </ul>
        </div>
      </div>
    </div>

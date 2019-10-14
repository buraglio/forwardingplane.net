The sixth [and arguably very overdue] installment of my <a href="https://www.forwardingplane.net/?s=nix4neteng" target="_blank">NIX4NetEng</a> series, this began as an overly complex diatribe about <a href="https://en.wikipedia.org/wiki/Domain_Name_System" target="_blank">DNS</a>. As it evolved, I realized that DNS is so complex and far reaching that it could never be contained in one meager post. DNS is a powerful tool. It has existed for so long that many that have never had the responsibility of running an authoritative or recursive resolver may take for granted the extensive reach of a tool so engrained in the fabric of the internet that it is frequently overlooked, much like a utility such as electricity or running water. Over time DNS has been reviled as the weak link in the chain that is the internet and and revered as the binding agent that makes the internet as we know it function. As someone that has run service provider and large campus resolvers, both recursive and authoritative, my opinion is that it is both. In the old days, and even now, black hat players will often target resolvers to perform DNS poisioning and will employ techniques such as flux and double flux to obfuscate their bot herders. Content providers use DNS tricks and anycast DNS to steer eyeballs to the topologically closest resource. Wifi hotspots use DNS to capture and force users through a captive portal.  
As users at large surf the web, advertisers utilize DNS to deliver advertising. Google does this, Yahoo does it, Hulu and other streaming video services do it. It has also been known to deliver pretty nasty <a href="https://en.wikipedia.org/wiki/Malvertising" target="_blank">malware</a>. That&#8217;s why when internet and security ninja <a href="http://blog.samoehlert.com/" target="_blank">Sam Oehlert</a> pointed me at this project called <a href="https://pi-hole.net/" target="_blank">pi-hole</a>, I knew that it would be a blog post.

Pi-Hole is a recursive resolver based on the venerable <a href="http://www.thekelleys.org.uk/dnsmasq/doc.html" target="_blank">dnsmasq</a> that actively blocks and logs ads. And it WORKS. The initial project was aimed at running this on a raspberry pi as a hardware based resolver for a small network. While this works well, it&#8217;s really just a linux service that can be run as a <a href="https://hub.docker.com/r/diginc/pi-hole/" target="_blank">docker container</a> or a standard LXC container. I decided to set this up as a linux container on my <a href="https://www.proxmox.com/en/" target="_blank">proxmox</a> box. The install is as simple as running a single command and walking through some simple menus.

<h2 class="intro-text" style="text-align: center;">
  curl -L install.pi-hole.net | bash
</h2>

The install is straightforward and allows for both IPv4 <span style="text-decoration: underline;"><strong>and</strong></span> IPv6 ad blocking, should your network support it (which is should!). Like any self funded opensource project, I have found a few caveats and hidden features with it:

  * Scaling the web interface for a network that performs significant numbers of queries is hard. It seems to have a difficult time displaying from large log files. Perhaps they&#8217;ll add something like a sqlite db to make this faster, the web interface seems to be updated frequently.
  * It&#8217;s based on dnsmasq, so adding local hostnames for within your network is a trivial as adding them to the /etc/hosts file on the pihole device. I personally don not like to type IP addresses and my network has been dial stacked with IPv6 for more than a decade, so local DNS resolution is a requirement. I&#8217;m not memorizing v6 addresses.
  * Again, it&#8217;s based on dnsmasq, so the flexibility and features are pretty significant and are as simple as tweaking the config file once it&#8217;s installed.
  * The query log is available. Security professionals are always interested in DNS query logs &#8211; they provide a monumental amount of useful information. With pihole, you have access to that in /etc/log/pihole.log. Here is a snippit of the log

<pre>Feb 27 16:28:04 dnsmasq[7620]: /etc/pihole/gravity.list s.youtube.com is 10.209.209.10
Feb 27 16:28:04 dnsmasq[7620]: query[AAAA] pubads.g.doubleclick.net from 10.209.89.21
Feb 27 16:28:04 dnsmasq[7620]: /etc/pihole/gravity.list pubads.g.doubleclick.net is 2001:470:c03a:809::a
Feb 27 16:28:04 dnsmasq[7620]: query[A] pubads.g.doubleclick.net from 10.209.89.21
Feb 27 16:28:04 dnsmasq[7620]: /etc/pihole/gravity.list pubads.g.doubleclick.net is 10.209.209.10
Feb 27 16:28:04 dnsmasq[7620]: query[A] r2---sn-vgqs7nls.googlevideo.com from 10.209.89.21
Feb 27 16:28:04 dnsmasq[7620]: forwarded r2---sn-vgqs7nls.googlevideo.com to 75.75.76.76
Feb 27 16:28:04 dnsmasq[7620]: query[AAAA] r2---sn-vgqs7nls.googlevideo.com from 10.209.89.21
Feb 27 16:28:04 dnsmasq[7620]: forwarded r2---sn-vgqs7nls.googlevideo.com to 75.75.76.76
Feb 27 16:28:04 dnsmasq[7620]: query[AAAA] manifest.googlevideo.com from 10.209.89.21
Feb 27 16:28:04 dnsmasq[7620]: forwarded manifest.googlevideo.com to 75.75.76.76
Feb 27 16:28:04 dnsmasq[7620]: query[A] manifest.googlevideo.com from 10.209.89.21
Feb 27 16:28:04 dnsmasq[7620]: forwarded manifest.googlevideo.com to 75.75.76.76</pre>

  * It&#8217;s easy to add or remove ad domains. Just edit /etc/pihole/gravity.list

&nbsp;



[Pi-hole Explained](https://vimeo.com/135965232) from [Pi-hole](https://vimeo.com/user40849716) on [Vimeo](https://vimeo.com).

&nbsp;

Completely ignoring the merit or unethical nature of blocking revenue generating advertisements (which I personally make a small amount of money on from on my <a href="https://www.youtube.com/buraglio" target="_blank">youtube channel</a>), this is a recommended project that exposes networking folks to unix, critical network services, as well as security. <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=3J2L3Z4DHW9UY" target="_blank">Throw them some beer or coffee money</a> if you find it useful. They&#8217;ve earned it.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1344" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1344" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1344" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1344" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2016/02/nix4neteng-6-dns-ad-blocking-and-quality-of-experience/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

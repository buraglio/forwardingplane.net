It&#8217;s always annoying to me, being a convert from *BSD to Linux, that tools lke dig and host aren&#8217;t in the minimal base install.  I realise that this makes me somewhat of a hypocrite, as I prefer an additive system rather than a subtractive base OS.  Nevertheless, I&#8217;m continually surprised that &#8220;host&#8221; isn&#8217;t available after installing a minimal CentOS system without adding an additional package.  So, since I always forget, here is a quick blog post to remind me and any other converts how to install those tools:

<pre> yum -y install bind-utils</pre>

That&#8217;s it.  Tragedy avoided.  Now I can make sure my AAAA records are working.

<pre>[buraglio@cupcake httpd]# dig www.forwardingplane.net -t AAAA
; &lt;&lt;&gt;&gt; DiG 9.8.2rc1-RedHat-9.8.2-0.10.rc1.el6_3.6 &lt;&lt;&gt;&gt; www.forwardingplane.net -t AAAA
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 47725
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.forwardingplane.net. IN AAAA
;; ANSWER SECTION:
www.forwardingplane.net. 86364 IN AAAA 2607:f2f8:4980::2
;; Query time: 1 msec
;; SERVER: 10.209.209.1#53(10.209.209.1)
;; WHEN: Thu Jan 3 22:49:35 2013
;; MSG SIZE rcvd: 69</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-316" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-316" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-316" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-316" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/01/dns-utilities-on-centos/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

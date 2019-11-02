With the recent release of the <a href="https://www.openssl.org/~bodo/ssl-poodle.pdf" target="_blank">POODLE SSLv3 vulnerability</a>, folks are scrambling around trying to figure out what runs what and where.  Running a handful of things that do SSL, I was obligated, both personally and professionally, to figure out an easy way to drill down and figure out what does what and then fix the vulnerable services.  When there are a lot of devices, this can seem like a daunting task, and it is if you&#8217;re trying to do it manually.  This is where <a href="http://nmap.org/" target="_blank">NMAP</a> comes into play.  NMAP is an extremely powerful tool for scanning and enumerating your own network, not just a tool for the script kiddies to port scan.

Since there is no SSL patch at the time of this writing, and since SSLv3 is old and depricated, it is a good idea to see what services support it and then squish them in favor of TLS 1+.  Thankfully, smarter folks than myself have done most of the legwork for accomplishing this task and written most of it down <a href="http://nmap.org/nsedoc/scripts/ssl-enum-ciphers.html" target="_blank">here</a>. NMAP has a wealth of cool scripts and bolt ons that extend it in amazing ways.  To accomplish our tasks we&#8217;ll ned to do a few things.

Install nmap. I ran into issues with the <a href="http://nmap.org/book/nse-library.html" target="_blank">nselibs</a> being incomplete, so I grabbed the source and built it that way as opposed to using yum.

<pre>git clone git@github.com:nmap/nmap.git</pre>

We then need to build it from source which requires the dev tools:

<pre>sudo yum -y groupinstall 'Development Tools'
cd nmap
./configure
sudo make</pre>

and alternatively

<pre>sudo make install</pre>

I like to just run it from my directory since there are path considerations.

<pre>(~/nmap) v-chimera $ ./nmap --script ssl-enum-ciphers -p 443 10.14.14.0/27

Starting Nmap 6.46 ( http://nmap.org ) at 2014-10-15 12:21 CDT
Nmap scan report for gw.test (10.14.14.1)
Host is up (0.0028s latency).
PORT    STATE  SERVICE
443/tcp closed https

Nmap scan report for ssldevice.test (10.14.14.2)
Host is up (0.0042s latency).
PORT    STATE SERVICE
443/tcp open  https
| ssl-enum-ciphers:
|   SSLv3:
|     ciphers:
|       TLS_RSA_WITH_RC4_128_MD5 - strong
|       TLS_RSA_WITH_RC4_128_SHA - strong
|     compressors:
|       NULL
|   TLSv1.0:
|     ciphers:
|       TLS_RSA_WITH_RC4_128_MD5 - strong
|       TLS_RSA_WITH_RC4_128_SHA - strong
|     compressors:
|       NULL
|_  least strength: strong

Nmap scan report for nossl.test (10.14.14.3)
Host is up (0.00049s latency).
PORT    STATE  SERVICE
443/tcp closed https</pre>

From here we can see that there is a host that needs to be updated. There are a wealth of docs out there for changing out the supported version. Most of my stuff is apache so I used <a href="https://zmap.io/sslv3/" target="_blank">this guide</a>. For embedded devices, the best option is to filter access [which you should probably be doing anyway] until there is a patched firmware version.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1100" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1100" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1100" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1100" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/10/nix4neteng-4-poodle-and-sslv3-scanning-and-updating/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
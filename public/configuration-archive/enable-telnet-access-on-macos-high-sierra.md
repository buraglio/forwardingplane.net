---
id: 1622
title: Enable Telnet access on MacOS High Sierra
date: 2019-03-02T10:11:38-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1622
---
Lots of things changed under the hood in MacOS high sierra. One of those was to enable a sandbox like environment and to remove insecure communication protocols. This breaks things like console communication to the network modeling and virtualization platform [Eve-NG](https://www.eve-ng.net/). It&#8217;s fairly trivial to re-enable it, however. This can be accomplished by doing the following steps. 

Install [Homebrew](http://www.homebrew.sh). Open your favorite terminal application (I like to use [iTerm2](https://www.iterm2.com/) (also installable via homebrew), but Terminal works fine.) 

<pre class="wp-block-preformatted">1. Reboot your Mac and hold the CMD + R keys <br />2. When presented with the recovery options, click Utilities at the top and choose Terminal <br />3. Type; csrutil disable <br />4. Reboot as normal <br />6. terminal and type; <br />brew install telnet <br />sudo ln -s /usr/local/bin/telnet /usr/bin/telnet <br />7. Again, Reboot your Mac and hold the CMD + R keys <br />8. When presented with the recovery options, click Utilities at the top and choose Terminal <br />9. Type; csrutil enable <br />10. Reboot as normal </pre>

You&#8217;re done. You can have telnet for your internal communication to Eve-NG consoles. **Don&#8217;t use it to talk to production network gear, because it&#8217;s not 1998.** 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1622" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1622" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1622" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1622" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/enable-telnet-access-on-macos-high-sierra/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
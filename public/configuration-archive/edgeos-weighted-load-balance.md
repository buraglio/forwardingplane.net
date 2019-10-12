---
id: 1589
title: EdgeOS weighted load balance
date: 2019-02-18T11:37:39-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1589
---
<pre class="wp-block-preformatted">set load-balance group LoadBalance_WAN interface  route-test initial-delay 15<br />
set load-balance group LoadBalance_WAN interface  route-test interval 5<br />
set load-balance group LoadBalance_WAN interface  route-test type ping target <br />
set load-balance group LoadBalance_WAN interface  weight 95 # weight based on more bandwidth <br />
set load-balance group LoadBalance_WAN interface  route-test initial-delay 15<br />
set load-balance group LoadBalance_WAN interface  route-test interval 5<br />
set load-balance group LoadBalance_WAN interface  route-test type ping target <br />
set load-balance group LoadBalance_WAN interface  weight 5 # weight based on less bandwidth</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1589" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1589" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1589" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1589" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-weighted-load-balance/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
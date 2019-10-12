We are putting a few new SRX 3600 clusters into production soon, and we&#8217;ve had them for about 6 months in boxes. This presented a fairly significant issue, one that I didn&#8217;t think about until it smacked me in the face.  
The code on these boxes was old. Very old. JunOS 9.2 old.  
No problem, lets just upgrade them to 10.4R something. 

<div>
  <b>Wrong</b>.
</div>

<div>
</div>

<div>
  the code that shipped on these boxes was so old, and we waited so long to upgrade them that I was unable to upgrade them straight to anything modern. To compound the issue, the upgrade was only able to be performed from certain code level releases as noted <a href="http://forums.juniper.net/t5/SRX-Services-Gateway/SRX-3400-upgrade-failure/m-p/55416">here</a>.
</div>

<div>
</div>

<div>
  This is a problem. I logged into the Juniper site to get the appropriate code, low and behold, it&#8217;s not available. I had to contact jtac and convince them that the code wasn&#8217;t there (which was a bit frustrating). Once they understood the issue (which took a bit longer than I expected; I don&#8217;t have Agility services on these particular boxes or I would never have had the jtac &#8220;issue&#8221;), they provided me with a download link for junos-srx3000-9.6R4.4-domestic. Once I had that code I was able to upgrade to it and then to 10.4.
</div>

<div>
</div>

<div>
  Not a huge issue, but something that was very annoying to have to jump through since I&#8217;ve never seen this issue upgrading a Juniper device.
</div>

<div>
</div>

<div>
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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-40" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-40" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-40" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-40" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
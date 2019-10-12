*IDP signatures need to be updated often.  On the SRX platform, there is also the notion of a &#8220;detector&#8221;.  This also meeds to be updated on a regular basis. it seems.  Over the past few weeks, we&#8217;ve needed to update the IDP signatures and detector on our SRX 5800 cluster several times, and the results have normally been fine.  
Updating the IDP signatures has never been **that** big of a problem (see postings about updating stuff on cluster nodes).  But we ran into issues due to the fact that we&#8217;d recently disabled application id to troubleshoot another problem.  This was basically causing all of our updates to fail on node1 (the secondary node) when using our [op script](http://www.juniper.net/techpubs/software/junos/junos82/swconfig82-automation/html/op-scripts-overview.html) to push the updates over (sorry, I can&#8217;t share it). 

A few things that I like to make sure to run before and after all of my SRX work are the following:

<span style="font-family: 'Courier New', Courier, monospace;">show chassis cluster status</span>  
<span style="font-family: 'Courier New', Courier, monospace;">show ospf neighbor brief</span>  
<span style="font-family: 'Courier New', Courier, monospace;">show security idp attack table</span>

If I&#8217;m doing work on the IDP engine, I also want to see the status of that:

<span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package download status</span>  
<span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package install status</span>  
<span style="font-family: 'Courier New', Courier, monospace;">show services application-identification counter</span>*

Anyway, for anyone else running into this odd behavior, to finally update it was a simple matter of deleting app-id before running the updates. 

<span style="font-family: 'Courier New', Courier, monospace;">edit </span>  
<span style="font-family: 'Courier New', Courier, monospace;">delete services application-id</span>  
<span style="font-family: 'Courier New', Courier, monospace;">commit comment &#8220;delete services application-id&#8221; </span>  
<span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package download full-update</span>  
<span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package install </span>  
<span style="font-family: 'Courier New', Courier, monospace;">op instlll-idp-updates</span>

At that point run the status commands <span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package install status</span><span style="font-family: Times, 'Times New Roman', serif;">. It should yield something like </span><span style="font-family: 'Courier New', Courier, monospace;">Done;Attack DB update : successful </span><span style="font-family: Times, 'Times New Roman', serif;">on both nodes.</span><span style="font-family: 'Courier New', Courier, monospace;">  </span>  
<span style="font-family: 'Courier New', Courier, monospace;"><br /></span>  
*It should be noted that Application ID is now in services, whereas I believe it used to be down in security.



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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-55" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-55" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-55" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-55" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2010/09/updating-srx-idp-signatures/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
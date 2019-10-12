Let me save you some time&#8230;.Microflow Policing on the Catalyst 6500 / Sup2TXL doesn&#8217;t yet work. Inbound it &#8220;kinda works&#8221;.  You can configure it and it applies as a service policy, but even though outbound is &#8220;supported in hardware on the Supervisor2TXL&#8221;, there is no software support for it in either the 15.0SY or 12.2(50)SY.  It took me a month to suss this out&#8230;..  
Yes, I should have suspected.  I dont work on Cisco every day, I have Juniper MX, Brocade MLX and a multitude of other platforms to work on daily, so it took a bit.  
The short answer is that the capability won&#8217;t be there until 15.1&#8230;.something I&#8217;m not looking forward to since 15.x is very different, and, if you use any of the MLS features, get ready to re-learn them all.  I still have a strong belief that 15.0SY is missing half of the MLS knobs I need to turn. 

Please, someone correct me.  I&#8217;d be **<u>extremely</u>** happy to be wrong about this one.  

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-19" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-19" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-19" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-19" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

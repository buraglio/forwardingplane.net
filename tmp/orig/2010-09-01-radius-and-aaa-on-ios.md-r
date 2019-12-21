I&#8217;m not the greatest at AAA on Cisco&#8217;s IOS. I always have to think about how to order things, and to test fallback (which you should do anyway). One of the caveats that I always overlook, no matter how many times I set this up, is that Cisco IOS software attempts authentication with the next listed authentication method only when there is no response from the previous method. If authentication fails at any point in this cycle—meaning that the security server or local username database responds by denying the user access—the authentication process stops and no other authentication methods are attempted[*](http://www.cisco.com/en/US/docs/ios/12_2/security/configuration/guide/scfaaa.html).  But, as I&#8217;ve said many, many times before, being able to look for documentation and knowing where to find information is just as valuable as having great retention. 

<div>
  I almost always have to go and look for documentation for IOS references.    
</div>

<div>
</div>

<div>
  What I want, really, is for radius to be consulted for all ssh logins, no login on console (this is controlled by a console server that requires other credentials that are not network dependent and maintained separately), and in the event of a RADIUS failure, for the authentication to fall back to the enable password.  For this to work, I had to do the following:
</div>

<div>
</div>

<div>
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">aaa new-model</span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">aaa authentication login default local group radius enable</span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">aaa authentication login console none</span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">aaa authentication enable default enable</span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">aaa authorization exec console none </span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">aaa session-id common</span>
  </div>
</div>

<div>
</div>

<div>
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">ip radius source-interface Loopback0 </span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">radius-server host <radius server ip> auth-port 1812 acct-port 1813 key 0 <plain text key></span>
  </div>
  
  <div>
    <span style="font-family: 'Courier New', Courier, monospace;">radius-server source-ports 1645-1646</span>
  </div>
</div>

<div>
</div>

<div>
  What this does is cause the lines to use  <span style="font-family: 'Courier New', Courier, monospace;">aaa authentication login default local group radius enable</span> for their authentication, expect for console, which uses <span style="font-family: 'Courier New', Courier, monospace;">aaa authentication login console none</span><span style="font-family: Times, 'Times New Roman', serif;">.</span><br /><span style="font-family: Times, 'Times New Roman', serif;"><br /></span><br /><span style="font-family: Times, 'Times New Roman', serif;">The rest of the commands will allow the enable password to work, etc.  I tested and verified this as well. Adding a local user to the box also works for those that are adverse to waiting for RADIUS to timeout to enter the enable password (although I really don&#8217;t see the point).  </span><br /><span style="font-family: Times, 'Times New Roman', serif;"><br /></span><br /><span style="font-family: Times, 'Times New Roman', serif;">Some other good reference material for this is available over at the <a href="http://blog.ioshints.info/2007/03/configure-local-authentication-with-aaa.html">IOS hints blog</a>.</span><br /><span style="font-family: Times, 'Times New Roman', serif;"><br /></span><br /><span style="font-family: Times, 'Times New Roman', serif;"><br /></span>
</div>

<div>
  <span style="font-family: 'Courier New', Courier, monospace;"><br /></span>
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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-56" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-56" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-56" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-56" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2010/09/radius-and-aaa-on-ios/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
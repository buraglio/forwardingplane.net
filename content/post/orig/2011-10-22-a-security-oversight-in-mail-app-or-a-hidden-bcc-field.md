Recently I was poking around Mail.app, setting up my new machine. I like to keep redundant copies of everything, email being no exception. I have backups of all of my email dating back to 1998, for the most part. It has come in handy from time to time and I like it for reference reasons. It&#8217;s a small amount of actual data as far as space goes, and it&#8217;s easy to do. I remembered the days of using mutt for email (which really weren&#8217;t that long ago for me), and really liked the idea of setting a bcc of a separate address, not necessarily myself, but an email address inside of my administrative control, for CYA types of archiving. Upon looking, I saw no way to do this within the default apple Mail.app. 

<div style="clear: both; text-align: center;">
</div>

Doing a bit of google searching, I found that this is pretty easily doable with a default write command. OK, awesome. This is good news. So I applied it:  
(Open Terminal)  
_defaults write com.apple.mail UserHeaders &#8216;{&#8220;Bcc&#8221; = &#8220;archive-address@domain.com&#8221;; }&#8217; _

Done. Great. So, lets test it. Send email and check bcc&#8217;d address.  Email is there.  Strange, however, the bcc field doesn&#8217;t show up, or show anything at all.  That&#8217;s right, there is absolutely no indication that this email is being bcc&#8217;d to another address.  
This isn&#8217;t really a problem for me, since I know that I set it up.  What it does mean, though, is that this could be applied to an unsuspecting user account, with absolutely **no authentication necessary,** and have every outgoing message silently sent to a harvesting account.  There is no easy way to check for this that I have found save for using terminal:

_[buraglio@dalek:~ ] defaults read com.apple.mail UserHeaders                                   _  
_{_  
_    Bcc = &#8220;archive-address@domain.com&#8221;;_  
_}_

<div>
</div>

OK, at least there is a way to tell.  Using the command _defaults read com.apple.mail UserHeaders_ from terminal will show the info, but the fact that it&#8217;s doable in such an obtuse way with no indication that mail is being bcc&#8217;d is a bit scary.  
There is a preference pane that allows for tweaking of some of these &#8220;features&#8221;, it&#8217;s open source available [here](http://secrets.blacktree.com/), called BlackTree Secrets. 



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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-26" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-26" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-26" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-26" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

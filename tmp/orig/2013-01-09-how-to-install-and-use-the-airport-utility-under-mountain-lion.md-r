I have a bunch of Apple wireless gear  at my house.  It&#8217;s inexpensive, feature rich and easy to maintain.  However, with the update to mountain lion a while ago, the ability to install  the older Airport Utility stopped.  This is annoying since I have what apple now considers &#8220;advanced&#8221; features like IPv6 at my home and essentially all my gear here is a lab (except for the plex server =)

I&#8217;ve been spending a lot of time on <a href="http://www.cacti.net" target="_blank">cacti</a> lately, and I wanted to test out the syslog plugin&#8230;.ok, easy.  It&#8217;s all set up.  Then I got to thinking &#8220;why not just let this run and syslog all my gear like the good &#8216;ol days?&#8221;  Nerdy?  Yes, but hey, I collect flow data at home and have a <a href="http://www.forwardingplane.net/homenet/" target="_blank">weathermap</a> of my home network.  It keeps me eating my own dog food with the netflow exporter plugin on <a href="http://www.pfsense.org" target="_blank">pfSense</a> and it&#8217;s fun.

Uh, oh.  No ability to set syslog receiver on the airport gear anymore.  Not cool.  [Guess what, no way to change IPv6 settings anymore either]

No way to do a standard install of the old utility. Lame, Apple, Lame.  After poking around a bit I found a pretty easy way to do it as long as you&#8217;re not afraid of the command line.

Since at least a few other folks will want to do this, here it is:

<a href="http://support.apple.com/kb/DL1536" target="_blank">Download the App</a> from Apple.

Mount the Downloaded disk.

Open Terminal.

Type:

<pre>pkgutil --expand /Volumes/AirPortUtility/AirPortUtility56.pkg
cd ~/Desktop/AirPortTemp~/Desktop/AirPortTemp/AirPortUtility56Lion.pkg/
open Payload
cd "Payload 2 2/Applications/Utilities/"
open .</pre>

[<img class="aligncenter size-full wp-image-341" title="Screen Shot 2013-01-08 at 11.32.08 PM" src="http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.32.08-PM.png" alt="" width="417" height="370" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.32.08-PM.png 417w, http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.32.08-PM-300x266.png 300w" sizes="(max-width: 417px) 100vw, 417px" />](http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.32.08-PM.png)

Done.  That should open a finder window with the App in it.  You can copy it to you /Applications/Utilities folder and use it alongside the newer one.  You&#8217;ll need to authenticate to copy into the /Applications/Utilities directory.

Edits made and Poof!  Now I can see my syslogs from within cacti.

<p style="text-align: center;">
   <a href="http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.44.40-PM.png"><br /> </a>
</p>

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-340" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-340" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-340" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-340" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/01/how-to-install-and-use-the-airport-utility-under-mountain-lion/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
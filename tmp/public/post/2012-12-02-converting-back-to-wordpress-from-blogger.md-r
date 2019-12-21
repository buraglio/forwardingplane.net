For a long time I ran a blog called [tech.buraglio.com](http://www.forwardingplane.net) that was a self hosted wordpress site. After having kids and getting a bit busier at work, I decided to move everything that I had been hosting (images, scripts, hacks, blogs and DNS) to &#8220;the cloud&#8221;. I managed to do this for everything but my primary DNS resolver, which I had always intended to keep, and one [wordpress blog](http://www.shitenonions.com) that I hosted for someone else.

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress.jpg"><img class="size-medium wp-image-84 aligncenter" title="bloggerpress" src="http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress-300x200.jpg" alt="" width="300" height="200" srcset="http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress-300x200.jpg 300w, http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress.jpg 500w" sizes="(max-width: 300px) 100vw, 300px" /></a>
</p>

&nbsp;

I moved my image hosting from gallery2 to flickr (backup on picasaweb), secondary DNS to nether.net and afraid.org, scripts, hacks and the like to google code and my blogs to blogger.  Blogger was **very** easy, stable and highly available.  It was also far less flexible.

<p style="text-align: center;">
  <img class="aligncenter" src="http://www.undertheradarblog.com/wp-content/uploads/2011/12/Top-5-Best-Free-Cloud-Storage-Services-That-You-Need-And-Are-Useful.png" alt="" width="480" height="253" />
</p>

I continued to write from time to time, mostly ramblings or notes on some weird thing I has to set up.  I noticed that a few of my posts were getting a decent amount of traffic, something I was a bit surprised about.  I started to write a bit more&#8230;&#8230;more traffic.  I started cross posting to <a href="http://www.twitter.com/buraglio" target="_blank">twitter</a>.  More traffic.  OK, maybe what I was jotting down was actually useful to someone.  Or I had a stalker.  Probably not the latter.

<img class="alignnone" src="http://blog.dreamhost.com/wp-content/uploads/2009/09/23-wordpress_logo.png" alt="" width="192" height="192" />   <img class="alignnone" src="http://www.decodeunicode.org/en/u+003e/data/glyph/196x196/003E.gif" alt="" width="196" height="196" /><img class="alignnone" src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Blogger.svg/256px-Blogger.svg.png" alt="" width="205" height="205" />

Since I already had apache working and serving other stuff, and one of them is another WP site, I already has MySQL running.  I just enabled SSL for the new domain that I had added and was ready to go.  I&#8217;m a really lazy sysadmin, so I used this as a reference.

First, installing wordpress.  I chose the <a href="http://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion" target="_blank">SVN install</a> for easier upgrades down the road.  Upgrading WP was somethingI alweays hated doing, so I let it languish when I used it before.  At least now I should, in most cases, be able to just type &#8220;_svn update_&#8221; to get it up to date (after verifying a back up, of course).

After using the <a href="http://wordpress.org/extend/plugins/blogger-importer/" target="_blank">blogger importer</a>, I had to go through and set all of my old blogger drafts to draft status again, wordpress has changed them all to published status. A minor detail. the rest  should be pretty straight forward, right?  Maybe not.  I&#8217;ve done a lot of twitter and bit.ly linking to my posts and I had a feedburner and quite a few RSS subscribers.  The feedburner stuff I&#8217;m probably going to have to write off.  The <a href="http://feeds.feedburner.com/forwardingplane/WszR" target="_blank">link</a> needed to be more obvious as to what it was. The biggest thing I have to worry about is that Blogger formats it&#8217;s &#8220;pretty&#8221; links in a different way than wordpress.  Thankfully, however, I&#8217;m self gosting so I can use apache magic to fix this.

_.htaccess_ to the rescue.

For every post, I&#8217;ve had to create a redirect entry in my .htaccess file.  Most of it is done, but for reference, here is what it looks like:

_Redirect 301 /2012/11/sdn-across-domains-in-wan-novice-look.html http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/_  
_Redirect 301 /2012/11/and-purple-pony.html http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/_  
_Redirect 301 /2012/11/using-brocade-mlxe-as-replicator-to-ids.html http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/_  
_Redirect 301 /2012/11/workflow-and-my-every-day-workstation.html http://www.forwardingplane.net/2012/11/workflow-and-my-every-day-workstation-setup/_  
_Redirect 301 /2012/11/vdxrancid-contrib-scripts.html http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/_  
_Redirect 301 /2012/11/scinet-privileged-few.html http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/_  
_Redirect 301 /2012/11/juniper-ex-4200-arp-ndp-problem-or.html http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/_  
_Redirect 301 /2012/11/and-purple-pony.html http://www.forwardingplane.net/2012/11/and-a-purple-pony/_  
_Redirect 301 /2012/10/directionality_31.html http://www.forwardingplane.net/2012/10/directionality/_  
_Redirect 301 /2012/10/juniper-to-ios-conversion-chart.html http://www.forwardingplane.net/2012/10/juniper-to-ios-conversion-chart/_  
_Redirect 301 /2012/10/host-based-sflow-or-sflow-for-more-than.html http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/_

&#8230;.and so on.

I got really used to the google analytics, so I had to add a plugin for that.  I chose <a href="http://wordpress.org/extend/plugins/google-analyticator/" target="_blank">Google Analyticator</a>.  &#8230;.Then I realized that users having to create  accounts is lame, so I added <a href="http://wordpress.org/extend/plugins/social-connect/" target="_blank">Social Connect</a>.

So far, that&#8217;s pretty much it.  However, since this is a public unix box I need to make sure it&#8217;s relatively safe, so I would highly recommend installing <a href="http://www.sshguard.net" target="_blank">sshguard</a> in addition to whatever other firewall rules it can dynamically block offensive hosts and then unblock them after a period of time.  I am also a big fan of <a href="http://www.duosecurity.com" target="_blank">duo security</a> for <a href="http://en.wikipedia.org/wiki/Two-factor_authentication" target="_blank">two factor auth</a>.

We&#8217;ll see how this goes&#8230;&#8230;

&nbsp;

&nbsp;

  


<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-77" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-77" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-77" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-77" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/12/converting-back-to-wordpress-from-blogger/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
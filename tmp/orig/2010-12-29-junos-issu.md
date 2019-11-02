I recently needed to upgrade a few MX480 routers and decided that it would be a good opportunity to get some experience with Juniper&#8217;s in service software upgrade.  
I&#8217;d read a bit about it but I&#8217;d not had the chance to really use it. It&#8217;s pretty straightforward and it does what it claims. The following are my notes from rolling through this on my test lab MX480.

A few things are necessary to get going with ISSU, first and foremost, you need to have a box with two routing engines. Check.  
Second, some configuration is necessary to make this all work.  
The boxes need to be running nonstop-routing, they need to be syncronizing the configs, and they need to have graceful-switchover enabled.

Here are the steps I went through on my vanilla test box to make this work:

root# set chassis redundancy graceful-switchover  
root# set routing-options nonstop-routing  
root# set system commit synchronize

If you already have those options set then you don&#8217;t need to enter those commands.

With those options set, you&#8217;re ready to do the ISSU. 

root> request system software in-service-upgrade /var/tmp/jinstall-10.3R2.11-domestic-signed.tgz  
Chassis ISSU Check Done  
ISSU: Validating Image  
Checking compatibility with configuration  
Initializing&#8230;  
Using jbase-10.1R1.8  
vn\_read\_compressed_block: invalid block index 550  
Verified manifest signed by PackageProduction\_10\_1_0  
Verified jbase-10.1R1.8 signed by PackageProduction\_10\_1_0  
Using /var/tmp/jinstall-10.3R2.11-domestic-signed.tgz  
&#8230;.

This takes a LONG time and generates a lot of scroll.

You&#8217;ll see long pauses and more text like

Saving package file in /var/sw/pkg/jinstall-10.3R2.11-domestic-signed.tgz &#8230;  
Saving state for rollback &#8230;  
Backup upgrade done  
Rebooting Backup RE

Rebooting re1  
ISSU: Backup RE Prepare Done  
Waiting for Backup RE reboot

Then interesting thing start to show up:

GRES operational  
Initiating Chassis In-Service-Upgrade  
Chassis ISSU Started  
ISSU: Preparing Daemons  
ISSU: Daemons Ready for ISSU  
ISSU: Starting Upgrade for FRUs  
ISSU: Preparing for Switchover

This is where the magic starts. The nonstop-routing and hitless failover come into play as the route engines switch over. Very cool. 

On the console of the backup RE (now the master) you&#8217;ll see messages like

Message from syslogd@ at Dec 29 19:11:57 &#8230;  
fpc0 RDP: Remote side reset connection: rdp.(fpc0:22528).(serverRouter:ppm) 

Message from syslogd@ at Dec 29 19:11:57 &#8230;  
fpc1 RDP: Remote side reset connection: rdp.(fpc1:4096).(serverRouter:ppm) 

these are normal. 

Some things that I didn&#8217;t expect, but probably should have:

The old master stays the backup route engine after the ISSU  
The old master does NOT reboot into the new code, instead it stays on the original code requiring a manual reboot (unless, I asume, you add the &#8220;reboot&#8221; command on to the original upgrade command).  
On routers that have logical systems configured on them, only the master logical system supports nonstop active routing.

I did the reboot manually

root> request system reboot  
Reboot the system ? \[yes,no\] (no) yes 

\*\\*\* FINAL System shutdown message from root@ \*\**  
System going down IMMEDIATELY 

Shutdown NOW!  
Reboot consistency check bypassed &#8211; jinstall 10.3R2.11 will complete installation upon reboot  
[pid 65006]

and then did a failover to the old master. 

root> request chassis routing-engine master switch

&#8230;.and thats pretty much it. Upgrade complete. 

This is a really useful tool that allows for very minimal interruption during software upgrades. I&#8217;d recommend reading [this](http://www.juniper.net/us/en/local/pdf/whitepapers/2000280-en.pdf) white paper on ISSU if you&#8217;re interested into diving into deeper details. 

Basically what ISSU does is to install junos on the backup route engine (re1) as normal, reboot it, validate and switch over to re1 and do the upgrade on the primary (now backup) route engine. The entire process took about 40 minutes on my mx480.

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
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-43" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-43" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-43" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-43" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2010/12/junos-issu/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

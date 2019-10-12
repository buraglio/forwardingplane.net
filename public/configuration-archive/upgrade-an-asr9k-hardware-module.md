---
id: 1616
title: Upgrade Single ASR9k hw-module
date: 2019-02-20T13:58:08-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1616
---
ASR9k is a powerful device but management may be daunting to anyone not familiar with IOS-XR. Inserting new line cards in may require a manual upgrade of the module to match the current running code on the chassis

Show all slow and firmware details: 

<pre class="wp-block-preformatted">show hw-module fpd location <em>rack/slot/subslot</em></pre>

In the admin prompt: 

<pre class="wp-block-preformatted">upgrade hw-module fpd all location 0/RSP1/CPU0</pre>

  
During the upgrade, this is the output, it will take a bit of time to perform the update. You may also need to upgrade things like fan trays, etc. 

<pre class="wp-block-preformatted">RP/0/RSP0/CPU0:core-9k(admin)#upgrade hw-module fpd all location 0/RSP1/CPU0Mon Feb 18 09:56:49.201 CST<br />***** UPGRADE WARNING MESSAGE: *****  <br />*  This upgrade operation has a maximum timout of 90 minutes.  *  <br />*  If you are executing the cmd for one specific location and  *  <br />*  card in that location reloads or goes down for some reason  *  <br />*  you can press CTRL-C to get back the RP's prompt.           *  <br />*  If you are executing the cmd for _all_ locations and a node *  <br />*  reloads or is down please allow other nodes to finish the   *  <br />*  upgrade process before pressing CTRL-C.                     *<br />% RELOAD REMINDER: <br /> - The upgrade operation of the target module will not interrupt its normal    operation. However, for the changes to take effect, the target module    will need to be manually reloaded after the upgrade operation. This can    be accomplished with the use of "hw-module &lt;target> reload" command.  <br />- If automatic reload operation is desired after the upgrade, please use    the "reload" option at the end of the upgrade command.  <br />- The output of "show hw-module fpd location" command will not display    correct version information after the upgrade if the target module is    not reloaded.<br /><br />NOTE: Chassis CLI will not be accessible while upgrade is in progress.</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1616" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1616" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1616" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1616" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/upgrade-an-asr9k-hardware-module/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
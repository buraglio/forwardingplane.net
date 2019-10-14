---
id: 1675
title: Renaming interfaces under linux
date: 2019-05-28T07:23:50-06:00
author: Nick Buraglio
layout: page
guid: https://www.forwardingplane.net/?page_id=1675
---
There are many of us that learned Linux in the very early days, and with that history comes habits. One habit I have is to look for spec interface names. In particular, I prefer to have my interfaces named eth* (with some notables exceptions here). Modern linux systems seem to have adopted the BSD methodology of naming the interfaces based on what it is &#8211; and while I did do a fair amount of work in BSD, I still prefer the eth naming scheme. [ZeroTier](https://www.zerotier.com/) has the inconsistency of using zt* on some platforms and ztublkahlah on others. I am sure there is a reason, but I prefer consistency. Here are two ways to rename the interfaces.

This is on a Debuntu system.

Temporarily rename an interface:

<pre>ifconfig ztukuxzo4f down
ip link set ztukuxzo4f name zt0
ifconfig zt0 up</pre>

Rename an interface persistently:

<pre>vi /etc/udev/rules.d/70-persistent-net.rules</pre>

Append:

<pre>SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="96:3c:ee:c0:ff:ee", NAME="zt0"</pre>

Reboot.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1675" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1675" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1675" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1675" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/renaming-interfaces-under-linux/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
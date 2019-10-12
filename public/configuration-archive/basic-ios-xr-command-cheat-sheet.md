---
id: 1618
title: Basic IOS-XR command cheat sheet
date: 2019-02-20T14:05:58-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1618
---
Some basic commands that I have found useful in managing an ASR9K / IOS-XR device. This page is likely to grow and change over time.

Clear ARP

<pre class="wp-block-preformatted">clear arp-cache &lt;interface&gt; &lt;IPv4 addr&gt; location all </pre>

BGP

<pre class="wp-block-preformatted">show bgp all unicast summary </pre>

BGP Routes

<pre class="wp-block-preformatted"><br />show bgp ipv[4/6] unicast neighbors &lt;neighbor&gt; received route<br />show bgp ipv[4/6] unicast advertised neighbor &lt;neighbor&gt; <br />show bgp ipv[4/6] unicast summary<br />show bgp ipv[4/6] unicast summary<br />clear bgp ipv[4/6] unicast &lt;neighbor&gt; soft in<br />show bgp all unicast summary<br />show bgp ipv[4/6] unicast bestpath-compare</pre>

NetFlow

<pre class="wp-block-preformatted">show flow exporter <em>&lt;exporter&gt;</em> location 0/RSP0/CPU0 </pre>

Show all hardware linecards

<pre class="wp-block-preformatted">show hw-module fpd location all</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1618" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1618" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1618" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1618" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/basic-ios-xr-command-cheat-sheet/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
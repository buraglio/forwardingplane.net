---
id: 1608
title: Nokia SROS useful commands
date: 2019-02-19T08:30:08-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1608
---
Nokia (formerly Alcatel-Lucent, formerly Timetra) have an extremely robust routing platform, but it has some notable differences if you&#8217;re coming from a vendor such as Cisco or Juniper (or any vendor platform in the enterprise space, really). Things like &#8220;VLANs&#8221; don&#8217;t really exist, as this is more of a metro / carrier / customer provisioning style device, so modular concepts are expected and baked into the OS at the deepest layers, unlike many of the other vendor platforms that support it but it feels like an add-in or addendum to the base routing instance. Here are a few useful commands that I threw together when I was learning SROS. As Nokia has begun rebuilding the SROS CLI to be less of a one-off, these will become less important, but until SROS is totally gone, someone will need to know them.

Show all installed line cards

<pre class="wp-block-preformatted">show card</pre>

Contextual configuration display. From anywhere in the hierarchy, to show that sections configuration simply type 

<pre class="wp-block-preformatted">info</pre>

To ascertain the service ID of a given SAP (service access point)

<pre class="wp-block-preformatted">show service sap-using</pre>

Similar to a juniper rollback compare, the SROS environment keeps candidate configurations and they can by compared, or diff&#8217;d to the running configuration. This is super useful. 

<pre class="wp-block-preformatted">admin rollback compare active-cfg to latest-rb</pre>

Also similar to juniper, it is possible to monitor the statistics of a given port in near real time

<pre class="wp-block-preformatted">monitor port 3/2/1 interval 3 repeat 999 rate</pre>

SROS is an MPLS powerhouse, knowing how to look at the LSPs is pretty critical

<pre class="wp-block-preformatted">show router mpls lsp terminate <br />show router mpls lsp transit <br />show router mpls lsp<br />show service id &lt;vpls-id&gt; all<br />show service id &lt;vpls-id&gt; fdb detail </pre>

VPRN commands

<pre class="wp-block-preformatted">show port &lt;port&gt; associations <br />show service id &lt;vprn-id&gt; all <br />show router &lt;vprn-id&gt; interface <br />show router &lt;vprn-id&gt; bgp summary <br />show router &lt;vprn-id&gt; route-table <br />show router &lt;vprn-id&gt; route-table protocol bgp-vpn <br />show router &lt;vprn-id&gt; route-table &lt;ip-address&gt; <br />show router &lt;vprn-id&gt; bgp routes &lt;ip-prefix&gt;/&lt;net-size&gt; detail <br />show router &lt;vprn-id&gt; bgp next-hop <br />show router &lt;vprn-id&gt; bgp neighbor &lt;ip-address&gt; received-routes <br />show router &lt;vprn-id&gt; bgp neighbor &lt;ip-address&gt; advertised-routes <br />oam vprn-ping &lt;vprn-id&gt; source &lt;ip-address&gt; destination &lt;ip-address&gt; <br />oam vprn-trace &lt;vprn-id&gt; source &lt;ip-address&gt; destination &lt;ip-address&gt; <br /></pre>

Useful BGP commands

<pre class="wp-block-preformatted">show router bgp summary&nbsp; <br />show router bgp neighbor &lt;neighbor&gt; received-routes &lt;ipv6&gt;&nbsp; </pre>

Showing logs

<pre class="wp-block-preformatted">show log log-id &lt;id&gt;<br />show log log-id 99<br />show log event-control<br /></pre>

Showing environmentals

<pre class="wp-block-preformatted">show chassis environment [power-supply]<br />show router interface [detail] <br />show port&nbsp;&lt;port&gt;&nbsp;optical</pre>

Showing and saving the configuration

<pre class="wp-block-preformatted">admin display-config<br />admin save<br />admin save rollback</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1608" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1608" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1608" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1608" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/nokia-sros-useful-commands/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
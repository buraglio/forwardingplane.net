---
id: 1628
title: FreeRTR basic configurations
date: 2019-03-02T11:00:49-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1628
---
From the [freertr](http://freerouter.nop.hu/) website:

<pre class="wp-block-preformatted">freeRouter is a free, open source router os process<br />it speaks routing protocols, and (re)encapsulates packets on interfaces (a huge list of encapsulation and routing test cases can be found under self-test page)since it handles packets itself, it is independent of underlaying os capabilities(optionally, it can export forwarding tables through openflow to external switch)since it is an unprivilegized process, it receives and sends packets through socketsthere are external, privileged processes that place traffic to these sockets(it means that internet can be used as backplane for router processes) the command line tries to mimic the industry standards with one exception: no global routing table: every routedinterface must be in a virtual routing table positive side effect: there are no vrf-awareness questions</pre>

As notes in my [FreeRTR post](https://www.forwardingplane.net/2019/03/freertr-as-a-lab-environment/), FreeRTR is a wonderful alternative to labbing up protocols and provides an incredible array of protocol support. Below are my three router test configurations from a basic setup. They should be enough to get you started. 

RTR1

<pre class="wp-block-preformatted"><br /> <br />hostname rtr1 <br />buggy <br />! <br />! <br />vrf definition host <br />exit <br />! <br />vrf definition vrf1 <br />rd 1:1 <br />exit <br />! <br />router isis4 1 <br />vrf vrf1 <br />net-id 48.1111.0000.1111.00 <br />traffeng-id :: <br />is-type both <br />redistribute connected <br />exit <br />! <br />router isis6 1 <br />vrf vrf1 <br />net-id 48.1111.0000.1111.00 <br />traffeng-id :: <br />is-type both <br />segrout 10 <br />level2 segrout <br />level1 segrout <br />redistribute connected <br />exit <br />! <br />! <br />interface loopback0 <br />no description <br />vrf forwarding vrf1 <br />ipv4 address 10.99.99.1 255.255.255.255 <br />ipv6 address 2001:db8:1111::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff <br />router isis6 1 enable <br />router isis6 1 circuit both <br />router isis6 1 segrout index 1 <br />router isis6 1 segrout node <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface loopback1 <br />no description <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet1 <br />no description <br />lldp enable <br />vrf forwarding vrf1 <br />ipv4 address 10.1.1.1 255.255.255.252 <br />ipv6 address 2001:db8:1111::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe <br />mpls enable <br />router isis6 1 enable <br />router isis6 1 circuit both <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet2 <br />no to_rt2_ether2 <br />lldp enable <br />vrf forwarding vrf1 <br />ipv4 address 10.1.4.1 255.255.255.252 <br />ipv6 address 2001:db8:1114::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe <br />mpls enable <br />router isis6 1 enable <br />router isis6 1 circuit both <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet20001 <br />no description <br />vrf forwarding host <br />ipv4 address 10.255.255.254 255.255.255.0 <br />no shutdown <br />no log-link-change <br />exit <br />! <br />line tty1 <br />no login authentication <br />exit <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />alias test bash command attach shell1 socat - exec:sh,ctty,pty,stderr <br />alias test bash description <br />alias test bash parameter optional <br />! <br />server telnet host <br />security protocol telnet <br />no login authentication <br />vrf host <br />exit <br />! <br />! <br />end </pre>

RTR2

<pre class="wp-block-preformatted">hostname rtr2 <br />buggy <br />! <br />! <br />vrf definition host <br />exit <br />! <br />vrf definition vrf1 <br />rd 1:1 <br />exit <br />! <br />router isis4 1 <br />no vrf <br />exit <br />! <br />router isis6 1 <br />vrf vrf1 <br />net-id 48.2222.0000.2222.00 <br />traffeng-id :: <br />is-type both <br />segrout 10 <br />level2 segrout <br />level1 segrout <br />redistribute connected <br />exit <br />! <br /><br /><br />interface loopback0 <br />no description <br />vrf forwarding vrf1 <br />ipv4 address 10.99.99.2 255.255.255.255 <br />ipv6 address 2001:db8:2222::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff <br />router isis6 1 enable <br />router isis6 1 circuit both <br />router isis6 1 segrout index 1 <br />router isis6 1 segrout node <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet1 <br />description to_rtr3_ether2 <br />lldp enable <br />vrf forwarding vrf1 <br />ipv4 address 10.1.3.2 255.255.255.252 <br />ipv6 address 2001:db8:1112::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe <br />mpls enable <br />router isis6 1 enable <br />router isis6 1 circuit both <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet2 <br />no to_rt1_ether2 <br />lldp enable <br />vrf forwarding vrf1 <br />ipv4 address 10.1.4.2 255.255.255.252 <br />ipv6 address 2001:db8:1114::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe <br />mpls enable <br />router isis6 1 enable <br />router isis6 1 circuit both <br />no shutdown <br />no log-link-change <br />exit <br /><br /><br />! <br />interface ethernet20001 <br />no description <br />vrf forwarding host <br />ipv4 address 10.255.255.254 255.255.255.0 <br />no shutdown <br />no log-link-change <br />exit <br />! <br />line tty1 <br />no login authentication <br />exit <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />alias test bash command attach shell1 socat - exec:sh,ctty,pty,stderr <br />alias test bash description <br />alias test bash parameter optional <br />! <br />server telnet host <br />security protocol telnet <br />no login authentication <br />vrf host <br />exit <br />! <br />! <br />end </pre>

RTR3

<pre class="wp-block-preformatted">hostname rtr3 <br />buggy <br />! <br />! <br />vrf definition host <br />exit <br />! <br />vrf definition vrf1 <br />rd 1:1 <br />exit <br />! <br />router isis4 1 <br />vrf vrf1 <br />net-id 48.3333.0000.3333.00 <br />traffeng-id :: <br />is-type both <br />redistribute connected <br />exit <br />! <br />router isis6 1 <br />vrf vrf1 <br />net-id 48.3333.0000.3333.00 <br />traffeng-id :: <br />is-type both <br />segrout 10 <br />level2 segrout <br />level1 segrout <br />redistribute connected <br />exit <br />! <br />interface loopback0 <br />no description <br />vrf forwarding vrf1 <br />ipv4 address 10.99.99.3 255.255.255.255 <br />ipv6 address 2001:db8:3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff <br />router isis6 1 enable <br />router isis6 1 circuit both <br />router isis6 1 segrout index 1 <br />router isis6 1 segrout node <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface loopback1 <br />no description <br />no shutdown <br />no log-link-change <br />exit <br />! <br />! <br />interface ethernet1 <br />description to_rtr2_ether1 <br />lldp enable <br />vrf forwarding vrf1 <br />ipv4 address 10.1.3.1 255.255.255.252 <br />ipv6 address 2001:db8:1112::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe <br />mpls enable <br />router isis6 1 enable <br />router isis6 1 circuit both <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet2 <br />description to_rtr1_ether1 <br />lldp enable <br />vrf forwarding vrf1 <br />ipv4 address 10.1.1.2 255.255.255.252 <br />ipv6 address 2001:db8:1111::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe <br />mpls enable <br />router isis6 1 enable <br />router isis6 1 circuit both <br />no shutdown <br />no log-link-change <br />exit <br />! <br />interface ethernet20001 <br />no description <br />vrf forwarding host <br />ipv4 address 10.255.255.254 255.255.255.0 <br />no shutdown <br />no log-link-change <br />exit <br />! <br />line tty1 <br />no login authentication <br />exit <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />! <br />alias test bash command attach shell1 socat - exec:sh,ctty,pty,stderr <br />alias test bash description <br />alias test bash parameter optional <br />! <br />server telnet host <br />security protocol telnet <br />no login authentication <br />vrf host <br />exit <br />! <br />! <br />end </pre>

Helpful show commands for this basic setup

<pre class="wp-block-preformatted">sh ipv4 route vrf1<br /> sh ipv6 route vrf1 </pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1628" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1628" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1628" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1628" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/freertr-basic-configurations/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
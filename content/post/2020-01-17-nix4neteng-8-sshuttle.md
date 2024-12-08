---
id: 2313
title: 'NIX4NetEng #8 &#8211; sshuttle'
date: '2020-01-17T22:36:14-06:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2313'
permalink: /2020/01/17/nix4neteng-8-sshuttle/
Views:
    - '1073'
image: /wp-content/uploads/2020/01/sshuttle-logo.png
categories:
    - NIX4NetEng
    - UNIX
---

<p>VPNs are a critically useful tool for gaining access to resources that cannot be exposed to the public internet for many different reasons, either policy or technical. VPNs can, however, be painful to install, difficult to troubleshoot, and in many cases (e.g. one time triage, single use instances) complete overkill. Providing encrypted access to this gooey center has never been easier, though, through the power of ease of sshuttle. </p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" title="sshuttle logo.png" src="https://forwardingplane.net/wp-content/uploads/2020/01/sshuttle-logo-1.png" alt="Sshuttle logo" width="599" height="474" border="0" /></p>
<p><a href="https://github.com/sshuttle/sshuttle">sshuttle</a> has some very usable capabilities. It was recently introduced to my by a colleague and I find that I use it quite frequently. Most users will find this tool immediately useful - I know I did - the use cases are fairly clear. By their own description, sshuttle is "where transparent proxy meets VPN meets ssh”. Now, you may be thinking, "why would I ever need to do this?”, and again, right from their README.md, sshuttle solves some unique problems: </p>
<blockquote>
<p>Your client machine (or router) is Linux, FreeBSD, or MacOS.<br />You have access to a remote network via ssh.<br />You don't necessarily have admin access on the remote network.<br />The remote network has no VPN, or only stupid/complex VPN protocols (IPsec, PPTP, etc). Or maybe you are the admin and you just got frustrated with the awful state of VPN tools.<br />You don't want to create an ssh port forward for every single host/port on the remote network.<br />You hate openssh's port forwarding because it's randomly slow and/or stupid.<br />You can't use openssh's PermitTunnel feature because it's disabled by default on openssh servers; plus it does TCP-over-TCP, which has terrible performance.</p>
</blockquote>
<p> </p>
<p>Sshuttle is open source, easily available, and <a href="https://sshuttle.readthedocs.io/en/stable/">fairly well documented</a>.  It supports ipv4 and ipv6, and is highly configurable, supporting both full pummeling, split tunnel options, and other nifty little options like tunneling DNS. </p>
<p> </p>
<p>Options I have personally used are things such as </p>
<p>Tunnel all internal address space</p>
<pre>sshuttle -r username@sshserver 10.0.0.0/16 </pre>
<p>Tunnel all traffic</p>
<pre>sshuttle -r username@sshserver 0.0.0.0/0</pre>
<p>Tunnel everything plus my DNS</p>
<pre>sshuttle --dns -r username@sshserver 0/0</pre>
<p> </p>
<p>It probably doesn’t solve all of you VPN woes (especially if you have to deal with IPSec at all, ever) - but this is an extremely useful took to have in your toolbox. </p>
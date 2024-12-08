---
id: 673
title: 'Debugging Brocade MLX/XMR ip_rx CPU issues'
date: '2013-06-16T18:35:42-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=673'
permalink: /2013/06/16/debugging-brocade-mlxxmr-ip_rx-cpu-issues/
themeblvd_title:
    - 'Brocade MLX/XMR management monitor mode'
themeblvd_keywords:
    - 'Brocace, MLX, XMR, ip_rx, dmraw, foundry'
themeblvd_description:
    - 'Gather diagnostic data for the brocade TAC utilizing low level hardware queries. '
themeblvd_noindex:
    - 'true'
Views:
    - '873'
categories:
    - How-To
    - Routing
---

I recently had the need to debug a run away ip_rx process on an older Brocade MLX.  For anyone that has had to do any type of low level debugging on the Brocade (Foundry) platform, you know that there many somewhat deep level diagnostics that are possible.  The debug (like cisco debug) is a bit lacking, but the dm, LP and MP commands are very useful (and a tad scary). Regardless, I've had to utilize them a lot in the last few years so my aversion to using them has been pretty much completely callused over.
So, when there was notification of CPU issues (common on the platform in environments I'm familiar with), I started poking around.  First off, the  <a href="http://www.brocade.com/downloads/documents/product_manuals/B_NetIron/Brocade_XMRMLX_05200_DiagnosticGuide.pdf" target="_blank" rel="noopener noreferrer">diagnostic documents</a> are your friend.  They're fairly deep and wide in scope.  After looking at the cpu, it was pretty clear what the culprit was.
rtr4-2#sh cpu-utilization | e 0
... Usage average for all tasks in the last 1 seconds  ...
==========================================================
Name            us/sec        %
idle                    68435           11
ip_rx                   724619          72
ospf                    36942           3
snmp                    82753           8
I needed to get info on that ip_rx process.  Google actually wasn't terribly helpful, so I dig out what I wanted, except for the process for breaking into the management module monitor mode.  The golden ticket ended up being "ctrl+y m enter" from the console.  That drops you into the OS mode or management module monitor mode that looks like this.<a href="http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM.png"><img class="alignright  wp-image-674" alt="Screen Shot 2013-06-16 at 7.04.20 PM" src="http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM.png" width="552" height="281" /></a>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
Basically this is what I gathered for the Brocade TAC.
<pre>MP-1 OS&gt;set sample-task ip_rx
MP-1 OS&gt;set sample-rate 5
MP-1 OS&gt;show sample
CPU Sample: Trace... (Repeat)
202e4eb8&lt;2021ec08&lt;202e5c18&lt;202e6238&lt;2030c2c4&lt;202ec2d8&lt;202eac00&lt;202eac74
 .....
MP-1 OS&gt;set sample-rate 0
MP-1 OS&gt;exit
Back to Application console...</pre>
Setting the task to sample is pretty simple:set sample-task &lt;task&gt;
<pre>set sample-rate</pre>
to show the sample, simply
<pre>show sample</pre>
and then to disable the sampling
<pre>set sample-rate 0</pre>
This can be used to gather all kinds of disgnostic data for seemingly any running process for the brocade TAC to decipher.
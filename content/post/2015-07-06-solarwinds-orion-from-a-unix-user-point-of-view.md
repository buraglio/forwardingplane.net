---
id: 1292
title: 'Solarwinds Orion from a UNIX user perspective'
date: '2015-07-06T22:08:30-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1292'
permalink: /2015/07/06/solarwinds-orion-from-a-unix-user-point-of-view/
dsq_thread_id:
    - '3911237412'
Views:
    - '254'
categories:
    - Musings
---

Back in February of this year (2015) I was introduced to <a href="http://www.solarwinds.com/">Solarwinds</a> when they presented to us at <a href="http://techfieldday.com/event/nfd9/">Networking Field day 9</a>. Until then I knew of SolarWinds products but only at a cursory level; I had never really seen or used their stuff since it was mostly focused on environments that were either smaller or outside of the networking world that I generally operate in. However, I am a[n insufferable] network monitoring "aficionado" so when the opportunity to play around with it arose, I happily took it.
Now, let me preface what comes next by laying out a few things:
<ol>
	<li>I am not a fan of SNMP. In fact, I hate it. It's the least intuitive, overly complex protocol used for management that we can't get away from. It sucks and is CPU intensive. It is cryptic, dated and we've tried to fix it by bolting on crude, poorly supported security features.</li>
	<li>I don't do windows systems. I have not managed as much as a windows desktop other than an on-demand VM for the occasional DWDM network element manager since 1999. I have no issue with it as a platform but a unix based platform is a better tool for my every day workflow (see <a href="https://www.forwardingplane.net/topics/nix4neteng/">NIX4NetEng</a>)  so I don't have it in my wheelhouse and have no business managing such a system.</li>
	<li>I went into this project completely and totally open minded. These were the canvas, brushes and subject I had to work with and it needed to do what needed done.</li>
</ol>
With that out of the way, my impressions of SolarWinds Orion platform at first glance were: "Wow, this is pretty good".<img class="alignright size-full wp-image-1313" src="http://www.forwardingplane.net/wp-content/uploads/2015/07/Screen-Shot-2015-07-06-at-10.48.05-PM.png" alt="Screen Shot 2015-07-06 at 10.48.05 PM" width="256" height="205" />
I must admit, I was surprised. Although I went in open minded, I knew that Orion is a tool that seemed to be enterprise focused, which was not the application it was being used for. It runs on windows systems, it had "rumored" scaling issues in large environments, and they market it mostly to the enterprise demographic, at least from my point of view. Admittedly I struggled with the configuration. I'm a little old school and I like to kick the tires of a GUI and then to most of the heavy lifting in a conf file or set of files using VI, which I was not able to do here. I found the management a little clunky and sluggish at times, but the data presentation was top shelf and once I figured out the where and how I was able to set up netflow, syslog collection and up/down monitoring in pretty short order. In this environment I didn't yet have IPv6 so no sflow or IPFIX in the mix yet; not sure about IPv6 support in practice.
A rough breakdown of the pros and cons from my inaugural run:
<strong>Pros:</strong>
<ul>
	<li>Elegant Interface</li>
	<li>Eye candy</li>
	<li>One stop shop***</li>
	<li>Good support for common stuff, seems expandable.</li>
	<li>Great <a href="https://thwack.solarwinds.com">community of support</a>; very "FOSS-Like"</li>
	<li>Lots of knobs and dials for tuning.</li>
	<li>Did I say good interface?</li>
	<li>Automated netflow database maintenance is cool.</li>
	<li>Search for flows and syslogs is reasonably fast. - a litmus test for real use.</li>
</ul>
<strong>Cons:</strong>
<ul>
	<li>It's SNMP. We're mostly stuck with that, unfortunately.</li>
	<li>Interface configuration took a little getting used to coming from a CLI background (this is a "me problem")</li>
	<li>Cost; it's a reasonably noticeable capital expenditure.</li>
</ul>
<strong>Unknowns: </strong>
<ul>
	<li>I didn't get to play with the SNMP trap management.</li>
	<li>I kept RANCID for configurations management.</li>
</ul>
The key for this for me was that I did not need to manage the server. I had no access whatsoever to the underlying OS, meaning the responsibility of managing this host OS was completely off the table. I was able to manage the SolarWinds instance from its web interface without issue.
<a href="http://www.forwardingplane.net/wp-content/uploads/2015/07/Screen-Shot-2015-07-06-at-10.47.36-PM.png"><img class="alignright wp-image-1310" src="http://www.forwardingplane.net/wp-content/uploads/2015/07/Screen-Shot-2015-07-06-at-10.47.36-PM.png" alt="Screen Shot 2015-07-06 at 10.47.36 PM" width="354" height="340" /></a>
My summary: If you are comfortable in a windows environment or do not manage the underlying system, don't need granular flow and syslog analysis for forensics and have the cash, it's a full featured, supported platform. I continue to learn more and more about the seemingly endless stuff this platform can do. If you are strapped for cash and/or are comfortable going the FOSS route, you have a lot of options at the expense of configuration time and possible learning curve.
You'll spend the money wither way, either on people time or on licensing. In some cases possibly both.
** I've heard that as a rumor. In my experience with the devices and other network elements it managed it seemed to work pretty well and I had no scaling issues.
*** Depends heavily on needs and requirements.
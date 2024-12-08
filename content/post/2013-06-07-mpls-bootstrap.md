---
id: 650
title: 'MPLS Bootstrap'
date: '2013-06-07T07:04:02-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=650'
permalink: /2013/06/07/mpls-bootstrap/
themeblvd_title:
    - 'MPLS basics; bootstrap your way to label switching'
themeblvd_keywords:
    - 'MPLS, VPLS, Juniper, JunOS, IOS, Cisco, LDP, RSVP-TE, cloud, SDN, label switching'
themeblvd_description:
    - 'MPLS basics; bootstrap your way to label switching.  A basic primer for learning the terminology and concepts of MPLS and associated protocols. '
themeblvd_noindex:
    - 'true'
Views:
    - '102'
categories:
    - How-To
    - Routing
---

I've been doing a lot of MPLS in the last 45 or so days (which is one of the reasons I have been absentee in the OpenFlow world lately). Having had almost no real world MPLS experience aside from a handful of pseudo-wires and a very small LDP signaled network, I had to spend some time reading, hacking at routers and essentially learning. In doing so, I found a few things.
<ul>
	<li>MPLS isn't that different than any other networking, it's taking a criteria and moving data based on that criteria (duh?!?)</li>
	<li>Many of the concepts are familiar.  Frame Relay and ATM come to mind.  OpenFlow does as well in certain circumstances.</li>
	<li>There is a lot of documentation on the MPLS suite of protocols.</li>
	<li>I didn't find a condensed set of data for the information I was looking for.  Jerely Stretch has some of it on his <a href="http://media.packetlife.net/media/library/18/Frame_Mode_MPLS.pdf" target="_blank" rel="noopener noreferrer">cheat sheet</a>, but it's not as complete as what I wanted and heavily vendor biased.  I was looking for conceptual information and not necessarily operational commands.</li>
</ul>
<a href="http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg"><img class="alignright size-full wp-image-670" alt="Basic Cloud" src="http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg" width="366" height="392" /></a>
I spent some time coming up with a slide deck I could present to others that, in theory, would build a foundation to work from.  I understand that this may be incomplete and is mostly a compilation of data found elsewhere (there is a reference section).  Using this bootstrap I was able to pick up the concepts well enough to understand when to use what and where as well as build the foundational requirements for a fairly complex MPLS environment.  Feel free to correct anything that is blatantly wrong, send me an email and I'll address it.
The slide deck can be found as a PDF <a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/MPLS-101.pdf" target="_blank" rel="noopener noreferrer">here</a>.  If you want the pptx it is available <a href="http://www.forwardingplane.net/wp-content/uploads/2013/07/MPLS-101.pptx" target="_blank" rel="noopener noreferrer">here</a>.   I will continue to update them as I hone the deck and / or find and correct errors.
&nbsp;
&nbsp;
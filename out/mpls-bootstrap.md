---
title: 'MPLS Bootstrap'
date: Fri, 07 Jun 2013 13:04:02 +0000
draft: false
tags: [How-To, Routing]
---

I've been doing a lot of MPLS in the last 45 or so days (which is one of the reasons I have been absentee in the OpenFlow world lately). Having had almost no real world MPLS experience aside from a handful of pseudo-wires and a very small LDP signaled network, I had to spend some time reading, hacking at routers and essentially learning. In doing so, I found a few things.

*   MPLS isn't that different than any other networking, it's taking a criteria and moving data based on that criteria (duh?!?)
*   Many of the concepts are familiar.  Frame Relay and ATM come to mind.  OpenFlow does as well in certain circumstances.
*   There is a lot of documentation on the MPLS suite of protocols.
*   I didn't find a condensed set of data for the information I was looking for.  Jerely Stretch has some of it on his [cheat sheet](http://media.packetlife.net/media/library/18/Frame_Mode_MPLS.pdf), but it's not as complete as what I wanted and heavily vendor biased.  I was looking for conceptual information and not necessarily operational commands.

[![Basic Cloud](http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg)](http://www.forwardingplane.net/wp-content/uploads/2013/06/Basic-Cloud.jpg) I spent some time coming up with a slide deck I could present to others that, in theory, would build a foundation to work from.  I understand that this may be incomplete and is mostly a compilation of data found elsewhere (there is a reference section).  Using this bootstrap I was able to pick up the concepts well enough to understand when to use what and where as well as build the foundational requirements for a fairly complex MPLS environment.  Feel free to correct anything that is blatantly wrong, send me an email and I'll address it. The slide deck can be found as a PDF [here](http://www.forwardingplane.net/wp-content/uploads/2013/07/MPLS-101.pdf).  If you want the pptx it is available [here](http://www.forwardingplane.net/wp-content/uploads/2013/07/MPLS-101.pptx).   I will continue to update them as I hone the deck and / or find and correct errors.
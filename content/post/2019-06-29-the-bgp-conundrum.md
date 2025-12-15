---
id: 1685
title: 'The BGP conundrum'
date: '2019-06-29T20:15:32-05:00'
author: buraglio
layout: post
guid: 'https://www.forwardingplane.net/?p=1685'
permalink: /2019/06/29/the-bgp-conundrum/
Views:
    - '557'
categories:
    - Musings
    - Routing
    - 'Soap Box'
---


BGP. It’s that magical protocol that runs the internet. For for as much as BGP is a fundamental, critical, irreplaceable part of the core functioning of the internet, it is a protocol that has not aged well as far as security is concerned. See, BGP was born when the internet was really still an academic experiment. Handshakes and loose agreements were totally fine for connecting a new site. 


Then came the awakening. ![Awakening](https://www.forwardingplane.net/wp-content/uploads/2019/06/Awakening.jpg)


Once the internet was used for more critical things, security was obviously more important. But BGP did not really evolve at the same rate - and more importantly, the security model surrounding it was mostly left behind. The reasons aren't really important, but the fallout absolutely is. Retrofitting security into an externally exposed protocol is demonstrably difficult. It has been [tried](https://tools.ietf.org/html/rfc8205) and [tried](https://tools.ietf.org/html/rfc6810) and [tried](https://tools.ietf.org/id/draft-sa-grow-maxprefix-00.html) and [tried](https://www.radb.net/). The real limit in this space exists because of the nature of the protocol itself - it is external in nature, thereby requiring coordination between multiple parties. The mechanics of this are two fold: personal interaction to agree on the peering, and technical compliance for the protocol to adhere to the agreed upon policy.


Technical limitations imposed by vendors and hardware limits have plagued this space for decades. However, the real problem, as with most things technical, is actually the people. A reluctance to agree on methodology, a refusal to spend the time to work out the procedures, an inability or lack of resources for understanding the steps necessary, an unwillingness (intentional or unintentional) to help the community further the progress. None of this really matters other than knowing where we can improve. So, to that end, I humbly recommend that all BGP operators read and implement best practices. Much of this is spelled out clearly in the [MANRS project](https://www.manrs.org/isps/), and it should be used as a shining example of community based action that can produce actual demonstrable results. If you’re interested in tools for troubleshooting BGP or better understanding the scope and scale of the DFZ (Default Free Zone), check out a past post I did on [BGP tools,](https://www.forwardingplane.net/2014/03/bgp-tools-troubleshooting-and-monitoring-external-routing-in-a-nutshell/) [RPKI](https://www.forwardingplane.net/2016/05/bgp-rpki-why-arent-we-using-it/), and [visibility outside of your network.](https://www.forwardingplane.net/2018/02/strategy-series-view-outside-network/) 


As a follow on to the last global BGP blunder, [Jordan Martin](https://twitter.com/bcjordo?lang=en) and I talk about the how and the what of the event in this quick [Network Collective short take](https://thenetworkcollective.com/2019/06/bgp-blunder/). 

<!-- wp:html -->
<figure><iframe src="https://player.vimeo.com/video/345003832" width="640" height="480" allowfullscreen=""></iframe></figure>
<!-- /wp:html -->
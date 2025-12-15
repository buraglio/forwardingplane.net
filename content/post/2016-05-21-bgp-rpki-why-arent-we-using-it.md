---
id: 1351
title: 'BGP RPKI – why aren&#039;t we using it more?'
date: '2016-05-21T10:33:44-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1351'
permalink: /2016/05/21/bgp-rpki-why-arent-we-using-it/
dsq_thread_id:
    - '4846277776'
Views:
    - '462'
categories:
    - Musings
    - Routing
    - Security
---

<div>     I was recently at a meeting where BGP RPKI was the topic de jour. While this has been a topic that I have visited on occasion of the last few years and something I wanted to spend significant time on, I have found that setting aside the time has been difficult and sparse, much like the deployment of BGP RPKI. In order to better understand the options available, it's important to break down the pieces and terminology involved; BGP is daunting enough to those unfamiliar with it and adding PKI on top of that can be even more so. So, what are these bits and pieces and why have we not done more to adopt it?</div>
<ul>
 	<li><strong>BGP</strong> - the venerable and foundational protocol that quite literally runs the internet. BGP allows an organization to announce and exchange it’s IPv4 and IPv6 resources with other organizations.</li>
 	<li><a href="https://www.arin.net/resources/rpki/"><strong>Resource Public Key Infrastructure</strong></a> - From <a href="https://www.arin.net/resources/rpki/">ARIN</a>: <i>Using cryptographically verifiable certificates, RPKI allows IP address holders to specify which Autonomous Systems (AS's) are authorized to originate their IP address prefixes. These statements, known as Route Origin Authorizations (ROAs), allow network operators to make informed routing decisions, and help secure Internet routing in general. </i></li>
 	<li><strong>ROA</strong> - Route Origin Authorizations - Who is authorized to originate or source these prefixes?</li>
 	<li><strong>ROV</strong> - Route Origin Validation - Can we validate, cryptographically, that the origin of this resource (for example, 8.8.8.8) is authorized to originate or source these prefixes?</li>
</ul>
<div>     Many of the details of RPKI are actually not even technical, both with ARIN and with vendors, there exists complications that make the technical pieces look like child’s play. Legality of the licensing and housing of authoritative certificates are complicated, shrouded in legalese due to the nature of what they represent. This proves to be a show stopper for a lot of older organizations that have grandfathered address space and may not have gone through the ARIN agreement process any time in the recent past [note: supposedly this process is required for ARIN IPv6 space, so most of that <i>should</i> be covered. Other regions may have easier, lower hurdles - I’ve heard good things about RIPE’s process - but I have no experience with it. The legal issues with contracts and signing certificates may also prove to be troublesome to enterprises, most of which are very conservative and slow to adopt anything new ::cough:: IPv6 ::cough::.  Certificate generation and maintenance is also considered difficult in many cases, the details can be confusing and the documentation overwhelming or difficult to find.</div>
<div>On top of those non-technical issues, platforms with large install bases are sparsely supported - although this is changing.</div>
<div>     There have been a <a href="http://www.bgpmon.net/large-scale-bgp-hijack-out-of-india/">number</a> of <a href="http://www.bgpmon.net/large-hijack-affects-reachability-of-high-traffic-destinations/">recent</a>, high profile route hijacks. If you’re ever curious to see what they were, BGPMon typically has a post-mortem shortly after they occur. This is a big deal. There are a number of ways they could have been prevented, too one of which is BGP RPKI. Is that worth the overhead? I think anyone that has had to scramble to figure out what was going on during one of these events would argue yes. But even with that, we have minimal adoption. With the significant movement to cloud based work, enterprises, service providers, academic institutions and even savvy end users should ask themselves a few important questions before doing your risk analysis:</div>
<div></div>
<ul>
 	<li>Do your cloud providers do RPKI?</li>
 	<li>Does your upstream service provider or peering partner honor invalid routes?</li>
 	<li>Does your upstream service provider or peering partner even support prefix or AS-Path filtering?</li>
 	<li>How does the effect BGP blackhole routing for security filtering?</li>
 	<li>How do you deal with invalid routes? (alert, set preference, drop, etc.)</li>
 	<li>How do you handle invalid routes that may be more specific?</li>
 	<li>Why have I not deployed BGP RPKI yet?</li>
</ul>
<div></div>
<div><strong>My perspective:</strong></div>
<div></div>
<div>    Unfortunately, the feeling I get is very similar to that of things [that we actually need] such as IPv6 and DNSSec. Tools that make our resources safer,  but are often overlooked due to increased operational complexity.</div>
<div>It is really about risk analysis: Is the risk of not having this worth the effort of maintaining it?  Since we [as an internetworking ecosystem] been clear in our actions that necessary things as obvious and straightforward as appropriate prefix filtering and IPv6 deployment are in many cases above and beyond, it should come as no surprise that adding complexity on top of “stuff that just works” is’t happening on a large scale. Even with repeated proof that changes would alleviate risk, we don’t do it because what we have has been deemed “good enough”* and change is scary and hard.</div>
<div>What do we need? We need tools. The <a href="http://rpki.surfnet.nl/">RPKI dashboard</a> that SURFnet has available is a fantastic example of an easy to use tool that makes a ton of information available. We need a <b><i>very easy</i></b> way to deploy this. BGP is actually a pretty simple protocol to make work, which is why is hasn’t changed much in the  extremely long tenure it has had as foundation of the internet. We need a very, very straightforward way to get the non-technical pieces done.</div>
<div></div>
<strong>Disclaimer:</strong>
This is just the tip of the iceberg and I am but a novice with this tech - but my gut feelings are typically right about this type of thing.
<div></div>
<div>* "Good enough” is almost never good enough.</div>
<div></div>
<div>
<h6>Image created from SURFNet RPKI page.</h6>
</div>
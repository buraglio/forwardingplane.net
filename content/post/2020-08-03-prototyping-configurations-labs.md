---
id: 2395
title: 'Prototyping, configurations, labs'
date: '2020-08-03T03:16:00-05:00'
author: buraglio
layout: post
guid: 'https://forwardingplane.net/?p=2395'
permalink: /2020/08/03/prototyping-configurations-labs/
Views:
    - '1448'
image: /wp-content/uploads/2020/08/Network-Diagram.png
categories:
    - How-To
    - 'Lab Time'
---

<!-- wp:paragraph -->
<p>It is all too common that smaller shops do not have the resources for a proper test lab. Even with the cost of grey market hardware, and the ease of virtualization, the gap is definitely there - be it time, financial limits, manpower, or even a general malaise toward even asking for something which may get denied. This presents a problem for multiple reasons:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Changes are not staged in a safe environment first - i.e. the production network is the test. This is bad and all too often a sad reality, we do not (and should not) need to explain why. </li><li>There is limited opportunity for learning - this will drive away the best employees. </li><li>It boldly states that the network and IT systems are not important enough to warrant the expenditure - at best this says "we care, but not enough to dedicate resources". </li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The good news is that today this is easy to spin up - even on your own. It does not require a large investment in a pallet of hardware; it is fairly inexpensive to get started. There are many options in this space.  <a href="https://www.eve-ng.net/">Eve-NG</a>, <a href="https://www.gns3.com/">GNS3</a>, even just raw qemu, can aid in getting something very useful up and trucking. Once you have the environment, you need to populate it with images. There are plenty of options for doing so: Juniper, Arista, FreeRTR, Mikrotik, all offer no cost VMs of their platforms for lab environments. It is easy to get started there.  Now that we have some resources we can get rolling, because although it is very important, all that above is not really what this post is about. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This post is about reference configurations and architectures. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://github.com/buraglio/Nokia-SROS-ExampleNet/blob/master/Network%20Diagram.png?raw=true" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For a while now I have had a "<a href="https://forwardingplane.net/configuration-archive/">configuration archive</a>" section of the blog. Mostly drawn from a deep well of junk I threw in <a href="https://www.evernote.com/referral/Registration.action?sig=0eb7394b4a9ae2ca2bb5fff6a3cb5d82c393d801a89a1f8d565d2ee678604dde&amp;uid=19302328">evernote</a> over the last 10+ years, they are "pro-tips", esoteric commands, or tidbits I found otherwise difficult to run down. What I am talking about here, though, are reference architectures. These are configurations that all fit together like a puzzle. I've been throwing them onto my <a href="https://github.com/buraglio">Github</a> for a while now, and as I build more I will add them. If someone were so inclined, they could likely grab the repo and push it out with a "working network" as a result. However, these are not meant to be perfect. They are purposely dirty because they represent a learning process and a safe environment for experimentation which is critical for expanding knowledge.  The list of the newest are below, they will likely change as I experiment with them, but they should provide a basic overview of how to do a few things in a larger environment than just a few nodes, and provide a context to some of the less talked about protocols and how they work together. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://github.com/buraglio/Nokia-SROS-ExampleNet" target="_blank" aria-label="undefined (opens in a new tab)" rel="noreferrer noopener">A Multi Vendor based MPLS network</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://github.com/buraglio/bgp-injector">A poorly written set of tools that will set up an environment for injecting a full DFZ table into GoBGP</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://github.com/buraglio/Nokia-SR-PCE">A multi vendor segment routed network (Primarily Nokia)</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://github.com/buraglio/Juniper-SR-PCE">A  multi vendor Segment Routed network (primarily Juniper)</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://github.com/buraglio/FreeRTR-Examplenet">A freertr based network</a></p>
<!-- /wp:paragraph -->
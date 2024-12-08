---
id: 1330
title: 'Building Interdomain SDN part 3'
date: '2015-11-05T22:37:23-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1330'
permalink: /2015/11/05/building-interdomain-sdn-part-3/
dsq_thread_id:
    - '4294060433'
Views:
    - '66'
categories:
    - Musings
    - Routing
    - SDN
    - 'Soap Box'
---

A few years ago I wrote <a href="http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/">some text</a> on <a href="http://www.forwardingplane.net/2013/01/sdn-across-the-wan-part-deux-primitives/">interdomain SDN</a>. Years later, work is being done, smart people are thinking about it and building ways to make it a reality. Not being one to give up on an idea, I gave <a href="https://docs.google.com/presentation/d/1anAaqWR8wmzKO5fqidDy9QJXW4RiVshX9Miq3PoDv9E/edit">this presentation</a> in may at <a href="http://chinog.org/meetings/chi-nog-05/">ChiNOG</a>  on what my take on what that architecture should be. I (we) propose that the use of existing protocols such as <a href="https://tools.ietf.org/html/rfc5575">BGP FlowSpec</a> will make this realistically deployable and maintainable given some <a href="https://github.com/dwcarder/sdn-ix-demo">simple, pluggable middleware</a>. As work continues to happen on this, my belief is that this is a very sound (and simple) concept. The middleware is modular and flexible enough that it can stand alone or plug into an existing code base such as ODL or Ryu. As <a href="http://sc15blog.blogspot.com/2015/11/simplifying-worlds-most-powerful.html" target="_blank" rel="noopener noreferrer">I work on the SDN deployment</a> for the <a href="http://www.sc15.org">annual international supercomputing conference</a>, and work on the <a href="https://www.es.net/network-r-and-d/workshops/">SDN for scientific networking workshop</a>,  I become more and more convinced that there needs to be an operationally viable and simple way to support these types of networks in ways that are thin and simple since it is a newer concept and some of the protocols involved (e.g. OpenFlow) is still in its infancy.  Here is the video of the talk for anyone interested in listening to me talk about it for 20 minutes.
<iframe src="https://www.youtube.com/embed/pIQ9-WrFHaQ" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
As a reference, this is a great talk from the same conference on BGP FlowSpec that adds a lot of credence to the use of it as a policy dissemination protocol.
<iframe src="https://www.youtube.com/embed/XBM5lgiPXGc" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
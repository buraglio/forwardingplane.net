---
title: 'Strategy Series: What is your netflow strategy?'
date: Mon, 18 Dec 2017 11:15:30 +0000
draft: false
tags: [How-To, Musings, Security, Strategy Series]
---


#### 
[What is your netflow strategy? - Tech Field Day](http://techfieldday.com/2017/netflow-strategy/ "") - <time datetime="2017-12-19 08:11:53">Dec 2, 2017</time>

\[…\] What is your netflow strategy? \[…\]
<hr />
#### 
[Robert Cowart]( "robacj@gmail.com") - <time datetime="2017-12-21 04:24:00">Dec 4, 2017</time>

Nick, thanks for the mention of ElastiFlow. Back when I created it I knew from my past experience that there was a lot of value in flow data. However, I must admit to being surprised with how popular the solution has become. Your criticism of the lacking documentation is fair, and will be addressed in the near future. Additionally, I am available to help any organization looking to leverage the Elastic Stack (formerly ELK) for network infrastructure management, whether that be flow data, SNMP, logs and more.
<hr />
#### 
[Stefan Fouant]( "sfouant@shortestpathfirst.net") - <time datetime="2017-12-26 13:07:00">Dec 2, 2017</time>

Seconded this. Kentik should have been on the list. First to market w/ a SaaS based detection offering... clearly an innovative approach that should not have been overlooked.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2017-12-26 14:53:00">Dec 2, 2017</time>

I don't disagree. As stated, my experience with Kentik is lacking so doing a review of it would have been lacking. Given the amount of heck I've received for \*not\* including it, it certainly has a larger market than I knew of. I will fully admit that my current stance on cloud based flow solutions is evolving, they require a risk assessment that others do not and unless there is diverse connectivity there is a potential to lose access to your analytics (think triage of a DDoS). My plan is to give this a reasonable amount of attention in the next 6-8 weeks.
<hr />
#### 
[samoehlert]( "sam.oehlert@gmail.com") - <time datetime="2017-12-18 13:59:00">Dec 1, 2017</time>

I think of Arbor more like a Jaguar. Beautiful machine, but very expensive and quite often needs attention from a (specialized) mechanic. I have a hard time liking it because if I'm throwing that much money into it, I don't want to do that much hand holding. I like to look at solutions on a continuum of inversely related time and money (ie Splunk vs Elastic Stack). Arbor requiring both is a tough sell.
<hr />
#### 
[Mark Milinkovich]( "mark_milinko@yahoo.com") - <time datetime="2017-12-18 18:34:00">Dec 1, 2017</time>

Nick - Thank you for the shout out for LiveAction LiveUX ! Just a note that LiveNX is our network performance and analytics platform that collects flow data (NetFlow, IPFIX, S-Flow, jflow, NetStream,etc) and SNMP, Cisco AVC, PerfMon, NBAR2, etc telemetry data directly from the underlay infrastructure and with LiveInsight, our machine learning module, provides real-time visibility into the applications across the environment for proactive management. In addition today we publicly announced a key acquisition to expand the portfolio to address service provider requirements. Super stoked, and so are our customers. We would welcome the opportunity to give you a an update. /Mark
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2017-12-18 11:25:00">Dec 1, 2017</time>

A great option for sure. My experience with pmacctd is sadly lacking, but i'd put it up there near nfdump in style but far surpassing it in ability. I am a fan of what I've seen and done with pmacctd but was never able to really give it the time it deserved in replacing my legacy installs. From my point of view it's as much of a flow generation tool in the vein of softflowd or nprobe (both honorable mentionsfor that service). As far as ELK, my opinion is that I don't care what generates the flow data as long as I can collect it, and I'm definitely a fan of ELK for this.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2017-12-18 11:19:34">Dec 1, 2017</time>

I went back and forth on mentioning Kentik. I like what I have seen so far but have very little to no experience with it. It is at the top of my list of platforms to spend some quality time with in the upcoming months. My take was that it was bucking to be a competitor to Arbor, with an original focus on service providers and expanding into enterprise markets. The cloud SaaS offering is interesting and compelling if one can justify and get approval to push flow data into an external infrastructure. My desire would be to work out soft and hard failure modes (as I do with any cloud based service) and then to really exercise the analytics and anomaly detection. I have had several comment on the robustness of the Kentik API, which is very, very high on the list of desirables.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2017-12-18 11:24:00">Dec 1, 2017</time>

I went back and forth on mentioning Kentik. I like what I have seen so far but have very little to no experience with it. It is at the top of my list of platforms to spend some quality time with in the upcoming months. My take was that it was bucking to be a competitor to Arbor, with an original focus on service providers and expanding into enterprise markets. The cloud SaaS offering is interesting and compelling if one can justify and get approval to push flow data into an external infrastructure. My desire would be to work out soft and hard failure modes (as I do with any cloud based service) and then to really exercise the analytics and anomaly detection. I have had several comment on the robustness of the Kentik API, which is very, very high on the list of desirables.
<hr />
#### 
[Justin Ryburn]( "justin@ryburn.org") - <time datetime="2017-12-18 10:10:00">Dec 1, 2017</time>

You might also take a look at Kentik Detect. It is a SaaS based approach to flow collection and analysis. No hardware/software to manage/maintain. Constant improvement in feature set without having to download/upgrade to pick them up. It is a commercial offering but might be worth evaluating if you want more of an easy button. It also provided a RestAPI to allow for integration with other tools. Free trial: https://portal.kentik.com/signup
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2017-12-18 11:14:14">Dec 1, 2017</time>

A great option for sure. My experience with pmacctd is sadly lacking, but i'd put it up there near nfdump in style but far surpassing it in ability. I am a big fan of pmacctd but was never able to really give it the time it deserved in replacing my legacy ndfump installs. From my point of view it's as much of a flow generation tool in the vein of softflowd or nprobe (both honorable mentions in my eyes). As far as ELK, my opinion is that I don't care what generates the flow data as long as I can collect it, and I'm a fan of ELK for this.
<hr />
#### 
[Lorenzo Mainardi]( "lormayna@gmail.com") - <time datetime="2017-12-18 07:37:00">Dec 1, 2017</time>

Why not thinking about pmacct + ELK? pmacct is very powerful and easy to setup and mantain.
<hr />
#### 
[Colin]( "cstubbs@gmail.com") - <time datetime="2018-01-24 04:00:00">Jan 3, 2018</time>

Hi Nick, no mention of vFlow...intentional? Or you just havn't used it? https://github.com/VerizonDigital/vflow
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2018-01-24 16:09:00">Jan 3, 2018</time>

This one is totally new to me. I'll add it to the list!
<hr />
#### 
[Strategy Series: How do you view outside of your network? - The Forwarding Plane | The Forwarding Plane](https://www.forwardingplane.net/2018/02/strategy-series-view-outside-network/ "") - <time datetime="2018-02-10 10:58:39">Feb 6, 2018</time>

\[…\] network works, you have graphing, up/down statistics, traffic baselines and visibility into traffic flow and configurations. Don’t worry, if you don’t have those things you can link to a few \[…\]
<hr />

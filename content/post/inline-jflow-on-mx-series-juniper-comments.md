---
title: 'Inline-jflow on MX series Juniper'
date: Sun, 01 Sep 2013 15:40:29 +0000
draft: false
tags: [How-To, Routing, Security]
---


#### 
[poohead]( "stuff@stuff.com") - <time datetime="2013-09-06 07:41:52">Sep 5, 2013</time>

Great post! Like all SolarWinds products, the Netflow Analyzer is subpar at best. It has major scalability and performance problems (most likely due to to way it uses its SQL database) that make it unusable for actual troubleshooting. And no matter how many new widgets and features they add to their interface, the graphs are still unreadable. I am of the opinion that any network reporting tool that doesn't use the RRD/MRTG-style graphs is almost worthless. Long live Tobi Oetiker! But on the positive side (as a colleague once told me), the SolarWinds Network Traffic Analyzer interface has lots of bright colors that will entertain upper management :).
<hr />
#### 
[tom]( "mraky@mraky.org") - <time datetime="2013-11-24 16:12:15">Nov 0, 2013</time>

solarwinds released new NTA4 who doesnt use sql database as backend for procesing netflow... i am plaing with it two, and it is realy fast ... regarding mrtg - man. did you ever tryed to postprocess data from mrtg ? or change retention in rdd ? ;)) rdd is for fun... i was using rdd for while as reporting, and i hated it... i am using now ms reporting server and it works really well..
<hr />
#### 
[Justin Hickey]( "jickfoo@gmail.com") - <time datetime="2015-04-14 09:54:00">Apr 2, 2015</time>

Hi Nick, I work for a company that just put in an MX480 a couple of weeks ago which connects to Internet2 at 100Gbps. Overall I think the MX is nice. Towards the end of the project I was looking to button up the environment and add some visibility into these large streams. There is very little information about how to make this all work in the MX. I just want the ability to do a show top-talkers in the cli during spikes of utilization. My reseller tells me we may have to pay additional fees for this functionality. Did you have to pay any extra or purchase any specific hardware ? We think this should be included. I just upgraded to the latest code and will give your instructions a shot. Thanks for the info.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2015-04-14 10:48:00">Apr 2, 2015</time>

I believe flow export should just work, I've never had it not work, actually. In addition to that, you should be able to use the "monitor traffic" command without any licensing. Details for that command are available here: https://www.juniper.net/techpubs/software/junos-es/junos-es93/junos-es-admin-guide/using-the-monitor-traffic-command.html
<hr />
#### 
[Mohammad Moghaddas](http://moghaddas.com "mohammad@moghaddas.com") - <time datetime="2015-07-16 07:17:00">Jul 4, 2015</time>

Could you please check if you had S-ACCT-JFLOW-IN license installed? I'm evaluating to do the same, but based on this link, seems that this license is required: https://www.juniper.net/documentation/en\_US/junos12.3/topics/reference/general/mx-series-software-license-features.html
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2015-07-16 07:31:00">Jul 4, 2015</time>

I no longer have access to these boxes but I can tell you for sure that I installed no licenses on this version of JunOS. It was a JunOS install as normal and I enabled the flow generation/export.
<hr />
#### 
[Mohammad Moghaddas](http://moghaddas.com "mohammad@moghaddas.com") - <time datetime="2015-07-16 07:32:00">Jul 4, 2015</time>

Thank you for your fast response Nick :)
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2015-07-16 07:34:00">Jul 4, 2015</time>

For what it is worth, if they are requiring a license for such a base feature no then that is pretty unfortunate. If I were you and the license is in fact required, I would request your sales team include it at no cost. Flow export is a right, not a privilege, especially when lots of gear does it for free.
<hr />

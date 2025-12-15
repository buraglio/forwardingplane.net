---
id: 40
title: 'Upgrading a new SRX 3600'
date: '2011-02-07T16:29:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/02/upgrading-a-new-srx-3600/'
permalink: /2011/02/07/upgrading-a-new-srx-3600/
Views:
    - '72'
categories:
    - Security
---

We are putting a few new SRX 3600 clusters into production soon, and we've had them for about 6 months in boxes. This presented a fairly significant issue, one that I didn't think about until it smacked me in the face. <br />The code on these boxes was old. Very old. JunOS 9.2 old. <br />No problem, lets just upgrade them to 10.4R something. <div><b>Wrong</b>. </div><div><br /></div><div>the code that shipped on these boxes was so old, and we waited so long to upgrade them that I was unable to upgrade them straight to anything modern. To compound the issue, the upgrade was only able to be performed from certain code level releases as noted <a href="http://forums.juniper.net/t5/SRX-Services-Gateway/SRX-3400-upgrade-failure/m-p/55416">here</a>.</div><div><br /></div><div>This is a problem. I logged into the Juniper site to get the appropriate code, low and behold, it's not available. I had to contact jtac and convince them that the code wasn't there (which was a bit frustrating). Once they understood the issue (which took a bit longer than I expected; I don't have Agility services on these particular boxes or I would never have had the jtac "issue"), they provided me with a download link for junos-srx3000-9.6R4.4-domestic. Once I had that code I was able to upgrade to it and then to 10.4. </div><div><br /></div><div>Not a huge issue, but something that was very annoying to have to jump through since I've never seen this issue upgrading a Juniper device. </div><div><br /></div><div><br /></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
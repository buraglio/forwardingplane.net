---
id: 55
title: 'Updating SRX IDP signatures'
date: '2010-09-02T12:16:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/09/updating-srx-idp-signatures/'
permalink: /2010/09/02/updating-srx-idp-signatures/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2010/09/updating-srx-idp-signatures.html
dsq_thread_id:
    - '3627823907'
Views:
    - '1062'
categories:
    - How-To
    - Security
---

*IDP signatures need to be updated often.  On the SRX platform, there is also the notion of a "detector".  This also meeds to be updated on a regular basis. it seems.  Over the past few weeks, we've needed to update the IDP signatures and detector on our SRX 5800 cluster several times, and the results have normally been fine. <br />Updating the IDP signatures has never been <b>that</b> big of a problem (see postings about updating stuff on cluster nodes).  But we ran into issues due to the fact that we'd recently disabled application id to troubleshoot another problem.  This was basically causing all of our updates to fail on node1 (the secondary node) when using our <a href="http://www.juniper.net/techpubs/software/junos/junos82/swconfig82-automation/html/op-scripts-overview.html">op script</a> to push the updates over (sorry, I can't share it). <br /><br />A few things that I like to make sure to run before and after all of my SRX work are the following:<br /><br /><span style="font-family: 'Courier New', Courier, monospace;">show chassis cluster status</span><br /><span style="font-family: 'Courier New', Courier, monospace;">show ospf neighbor brief</span><br /><span style="font-family: 'Courier New', Courier, monospace;">show security idp attack table</span><br /><br />If I'm doing work on the IDP engine, I also want to see the status of that:<br /><br /><span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package download status</span><br /><span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package install status</span><br /><span style="font-family: 'Courier New', Courier, monospace;">show services application-identification counter</span>*<br /><br />Anyway, for anyone else running into this odd behavior, to finally update it was a simple matter of deleting app-id before running the updates. <br /><br /><span style="font-family: 'Courier New', Courier, monospace;">edit </span><br /><span style="font-family: 'Courier New', Courier, monospace;">delete services application-id</span><br /><span style="font-family: 'Courier New', Courier, monospace;">commit comment "delete services application-id" </span><br /><span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package download full-update</span><br /><span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package install </span><br /><span style="font-family: 'Courier New', Courier, monospace;">op instlll-idp-updates</span><br /><br /><br />At that point run the status commands <span style="font-family: 'Courier New', Courier, monospace;">request security idp security-package install status</span><span style="font-family: Times, 'Times New Roman', serif;">. It should yield something like </span><span style="font-family: 'Courier New', Courier, monospace;">Done;Attack DB update : successful </span><span style="font-family: Times, 'Times New Roman', serif;">on both nodes.</span><span style="font-family: 'Courier New', Courier, monospace;">  </span><br /><span style="font-family: 'Courier New', Courier, monospace;"><br /></span><br />*It should be noted that Application ID is now in services, whereas I believe it used to be down in security.<br /><br /><br /><div><br /></div><div><br /></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
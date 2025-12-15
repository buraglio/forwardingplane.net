---
id: 55
title: 'Updating SRX IDP signatures'
date: '2010-09-02T12:16:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/09/updating-srx-idp-signatures/'
permalink: /2010/09/02/updating-srx-idp-signatures/
dsq_thread_id:
    - '3627823907'
Views:
    - '1062'
categories:
    - How-To
    - Security
---

*IDP signatures need to be updated often.  On the SRX platform, there is also the notion of a "detector".  This also meeds to be updated on a regular basis. it seems.  Over the past few weeks, we've needed to update the IDP signatures and detector on our SRX 5800 cluster several times, and the results have normally been fine. **Updating the IDP signatures has never been <b>that** big of a problem (see postings about updating stuff on cluster nodes).  But we ran into issues due to the fact that we'd recently disabled application id to troubleshoot another problem.  This was basically causing all of our updates to fail on node1 (the secondary node) when using our [op script](http://www.juniper.net/techpubs/software/junos/junos82/swconfig82-automation/html/op-scripts-overview.html) to push the updates over (sorry, I can't share it). 

A few things that I like to make sure to run before and after all of my SRX work are the following:

show chassis cluster status
show ospf neighbor brief
show security idp attack table

If I'm doing work on the IDP engine, I also want to see the status of that:

request security idp security-package download status
request security idp security-package install status
show services application-identification counter*

Anyway, for anyone else running into this odd behavior, to finally update it was a simple matter of deleting app-id before running the updates. 

edit 
delete services application-id
commit comment "delete services application-id" 
request security idp security-package download full-update
request security idp security-package install 
op instlll-idp-updates


At that point run the status commands request security idp security-package install status. It should yield something like Done;Attack DB update : successful on both nodes.  


*It should be noted that Application ID is now in services, whereas I believe it used to be down in security.



---
title: 'Updating SRX IDP signatures'
date: Thu, 02 Sep 2010 18:16:00 +0000
draft: false
tags: [How-To, Security]
---


#### 
[Ken](http://www.blogger.com/profile/15119568998718965834 "noreply@blogger.com") - <time datetime="2011-08-04 20:36:06">Aug 4, 2011</time>

Nick - a question for you regarding SRX IDP signature database updates on a Cluster. The 'successful' message you list above indicates both nodes will be updated, however, my understanding is that only the Primary node will be updated,not the Secondary node and that it is necessary to fail over the Primary function and repeat the update procedure in order to update both nodes. The RE is not running on the secondary node, which is the reason for this procedure, as I understand it. I am referring to a srx240 cluster, so it may be different from your 5800 cluster. I believe the workaround is to use the Offline procedure for IDP sgnature database updates... I would appreciate your thoughts and experience. Thank you.  
  
Ken
<hr />
#### 
[Nick Buraglio](http://www.blogger.com/profile/02818854373192493920 "noreply@blogger.com") - <time datetime="2011-08-07 02:53:30">Aug 0, 2011</time>

Ken, that is correct. We have an op script that pushes the updates across the control link on the back end. Failing it over is the supported method, but I find that pretty crummy, so we worked around it.
<hr />

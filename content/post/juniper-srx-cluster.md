---
title: 'Juniper SRX Cluster'
date: Wed, 01 Sep 2010 04:04:00 +0000
draft: false
tags: [Security]
---

I have had the opportunity to work pretty extensively on the Juniper SRX firewall/IDS platform over the last few months.  In doing so, I've found many "gotchas" the hard way.  
  
Here are a few that I've found so far:  
  
Clustering is a beast in and of itself.  I think it needs a bit more polishing, but it could be that we just need to refine our design.  
  
On the SRX 650 it works, but you must be on the right code version (I got it to work under 9.6R2.11 and have left it alone since).  
  
On the 5800 it works a bit better, but if you want to do active/active, it is very lacking in features.  
We have a unique setup where I am employed, and this usually means we are left a bit on our own as far as configurations (although our Juniper SE is amazing and did a lot to get this all working).  
That said, we have a design that isn't really fully supported on the SRX yet, although I believe it will be as code matures.  
What we've done is to create a cluster using no reth interfaces.  Instead, we're relying on routing to ake the decisions as far as what traffic goes where.  This was a different approach than we had originally used on the smaller 650 cluster elsewhere in the network.  
  

[![](http://1.bp.blogspot.com/_t5EEUl7btNU/TH18bIBhtkI/AAAAAAAACn4/wgLW1b-H7Zs/s320/simplesrx.png)](http://1.bp.blogspot.com/_t5EEUl7btNU/TH18bIBhtkI/AAAAAAAACn4/wgLW1b-H7Zs/s1600/simplesrx.png)

  
  
What this means is multi-faceted.  
Standard jtac isn't going to understand what you've done.  Using advanced jtac is the only way to get things moving in a timely fashion should you encounter issues.  We have agility service on ours, so that makes it even easier.  
  
IDP doesn't work asymmetrically.  If an traffic cones in on one node and leaves through the other, IDP doesn't apply.  IDP information is not shared through the control link at the time of this writing.  
IDP updates across the cluster don't work well in this way.  My "node0" node can get the updates but since node0 holds the loopback interface that traffic is sourced from, I cannot get out from node1.  Again, this data is not shared over the control link between the cluster nodes.  There are nasty ways around this with static routes, but I prefer not to use them.    
The best way I found to get around this is to manually fail over the cluster and install the IDP updates on node1 after node0 has installed them and then to fail back.  
This brings me to the next issue we ran into.  Upgrading the cluster junos software.  
Juniper's recommended method for upgrading is to upgrade each one, then reboot both at the same time.  
to me this is a bit odd, since the reason most folks want a cluster is to avoid things like this.  Well, I can say for experience, if you upgrade the node0 and reboot it without doing the same to node1, all heck breaks loose.  The cluster won't come up cleanly even after the secondary is upgraded and the only way I found to alleviate the off traffic problems we were seeing was to bounce them both at the same time.  Annoying to say the least.  
Oh, if you want to run Active/Active and have it actually work the way we have it set up, you'll need at least JunOS 10.2.R2.11.  
  
That said, I really do believe that the SRX is the best carrier class security appliance on the market.  Our entire network (which is not insignificant or standard in size or traffic patterns), can run off of one box with 4 SPCs and not even touch the processing power.  They are a powerhouse and have that trademark JunOS cli, and all of the advantages that come with it.

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
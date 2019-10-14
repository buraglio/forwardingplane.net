---
title: 'I want to love cumulus networks.....'
date: Wed, 03 Jul 2013 22:08:48 +0000
draft: false
tags: [Musings]
---


#### 
[David Hocking]( "davehockingprivate@gmail.com") - <time datetime="2013-07-26 06:07:16">Jul 5, 2013</time>

When I was looking into a free router/fw appliance I could deploy as VMs, I looked at pfSense, but settled with Vyatta. It has the best of both worlds IMHO, you get a near-native linux experience, bash et al, but, with the benefit of a single hierarchical config file that can be diff'd, scp'd and copied between nodes. If you've used JunOS, then you can use vyatta too, I just wish they'd make the break into switching too! - though I guess there's nothing to stop you loading up an old server with QuadPort Nics and creating loads of bridge interfaces, other than the fact that it's a cludge :)
<hr />
#### 
[Darrin]( "Darrin@thethomasons.org") - <time datetime="2013-07-03 23:04:14">Jul 3, 2013</time>

It will also be interesting to see how they deal with state management in the linux kernel. This has been tried before and struggled to scale due to the high amounts of IPC between processes. While it may make sense in some closet access cases, unless you are built to handle failure, this model will be a challenge to implement and scale. Lastly merchant silicon is constantly changing - don't underestimate the maintenance need to maintain a consistent working model. Again, I am not saying that this will fail, I like the validation of the need for a highly extensible and programmable OS. Time will tell whether it is as easy as they propose.
<hr />

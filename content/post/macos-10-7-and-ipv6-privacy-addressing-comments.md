---
title: 'MacOS 10.7 and IPv6 privacy addressing'
date: Sun, 31 Jul 2011 02:40:00 +0000
draft: false
tags: [IPv6, UNIX]
---


#### 
[Charley](https://openid.aol.com/opaque/31092bb2-bd25-11e0-8541-000bcdcb2996 "noreply@blogger.com") - <time datetime="2011-08-02 16:34:03">Aug 2, 2011</time>

I think the real security issue with EUI-64 address assignment is that your IPv6 address contains your same MAC address, wherever you go. So your movements are trackable between home, work, and coffee shop networks. It has less to do with what the L2 address actually is.
<hr />
#### 
[Charley](http://openid.aol.com/cvk256 "noreply@blogger.com") - <time datetime="2011-08-02 16:38:03">Aug 2, 2011</time>

Also, you missed a part of the command to turn it off; it's:  
  
sudo sysctl -w net.inet6.ip6.use\_tempaddr=1  
  
To make it permanent across reboots requires editing /etc/sysctl.conf.
<hr />
#### 
[Nick Buraglio](http://www.blogger.com/profile/02818854373192493920 "noreply@blogger.com") - <time datetime="2011-08-06 20:16:19">Aug 6, 2011</time>

I don't buy the tracking of the mac address. I guess it's feasible, but spoofing a mac is so easy nowadays, I just don't see the point. There are so many ways to track a user via http logs, logged access to shared resources, etc. that I just don't buy that it's any easier than any other mechanism.  
  
sudo sysctl -w net.inet6.ip6.use\_tempaddr=1 wil enable the tempaddr,  
sudo sysctl -w net.inet6.ip6.use\_tempaddr=0 disables it, if I recall correctly. Good point about the /etc/sysctl.conf. I'll add that in.
<hr />

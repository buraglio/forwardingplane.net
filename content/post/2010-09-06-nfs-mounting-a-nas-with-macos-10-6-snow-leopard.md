---
id: 52
title: 'NFS mounting a NAS with MacOS 10.6 (Snow Leopard)'
date: '2010-09-06T05:00:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/09/nfs-mounting-a-nas-with-macos-10-6-snow-leopard/'
permalink: /2010/09/06/nfs-mounting-a-nas-with-macos-10-6-snow-leopard/
Views:
    - '100'
categories:
    - How-To
    - UNIX
---

I know this is [documented elsewhere](http://hints.macworld.com/article.php?story=20090830073912179), but this was a pain for me, so I wanted to take some notes.  I have several Snow Leopard (MAcOS 10.6) Macs and a Netgear DNS-323.  I want to mount the drive using NFS and any good UNIX admin would. 
Unlike older versions of the Mac OS, NFS mounts are now handled under the Disk Utility application (which seems odd to me, but whatever). 
So, to make this work right I had to do the following:
First, I had to make sure that the NFS Add-on was installed on the DNS-323. 
Second, Open up Disk utility and go to file, NFS mounts. 

[![](http://4.bp.blogspot.com/_t5EEUl7btNU/TIR2joSzRDI/AAAAAAAAC_A/jIWYuHwgZ-c/s320/Screen+shot+2010-09-06+at+12.02.59+AM.png)](http://4.bp.blogspot.com/_t5EEUl7btNU/TIR2joSzRDI/AAAAAAAAC_A/jIWYuHwgZ-c/s1600/Screen+shot+2010-09-06+at+12.02.59+AM.png)
This will open up a new window like this:

[![](http://2.bp.blogspot.com/_t5EEUl7btNU/TIR2u9UMXQI/AAAAAAAAC_I/oZBsg4qkZ3Y/s320/Screen+shot+2010-09-06+at+12.03.18+AM.png)](http://2.bp.blogspot.com/_t5EEUl7btNU/TIR2u9UMXQI/AAAAAAAAC_I/oZBsg4qkZ3Y/s1600/Screen+shot+2010-09-06+at+12.03.18+AM.png)
From here, add your NFS mount location that you've specified within the NFS add-on (setting that part up is beyond the scope of this tutorial, you should know how to do that if you've gotten this far).
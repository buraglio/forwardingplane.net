---
id: 52
title: 'NFS mounting a NAS with MacOS 10.6 (Snow Leopard)'
date: '2010-09-06T05:00:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/09/nfs-mounting-a-nas-with-macos-10-6-snow-leopard/'
permalink: /2010/09/06/nfs-mounting-a-nas-with-macos-10-6-snow-leopard/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /feeds/3291015193216494208/posts/default/4274823194488986030
Views:
    - '100'
categories:
    - How-To
    - UNIX
---

I know this is <a href="http://hints.macworld.com/article.php?story=20090830073912179">documented elsewhere</a>, but this was a pain for me, so I wanted to take some notes.  I have several Snow Leopard (MAcOS 10.6) Macs and a Netgear DNS-323.  I want to mount the drive using NFS and any good UNIX admin would. <br />Unlike older versions of the Mac OS, NFS mounts are now handled under the Disk Utility application (which seems odd to me, but whatever). <br />So, to make this work right I had to do the following:<br />First, I had to make sure that the NFS Add-on was installed on the DNS-323. <br />Second, Open up Disk utility and go to file, NFS mounts. <br /><br /><div style="clear: both; text-align: center;"><a href="http://4.bp.blogspot.com/_t5EEUl7btNU/TIR2joSzRDI/AAAAAAAAC_A/jIWYuHwgZ-c/s1600/Screen+shot+2010-09-06+at+12.02.59+AM.png" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" src="http://4.bp.blogspot.com/_t5EEUl7btNU/TIR2joSzRDI/AAAAAAAAC_A/jIWYuHwgZ-c/s320/Screen+shot+2010-09-06+at+12.02.59+AM.png" /></a></div><div style="clear: both; text-align: left;"><br /></div><div style="clear: both; text-align: left;">This will open up a new window like this:</div><div style="clear: both; text-align: left;"><br /></div><div style="clear: both; text-align: left;"><br /><a href="http://2.bp.blogspot.com/_t5EEUl7btNU/TIR2u9UMXQI/AAAAAAAAC_I/oZBsg4qkZ3Y/s1600/Screen+shot+2010-09-06+at+12.03.18+AM.png" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/_t5EEUl7btNU/TIR2u9UMXQI/AAAAAAAAC_I/oZBsg4qkZ3Y/s320/Screen+shot+2010-09-06+at+12.03.18+AM.png" /></a></div><div style="clear: both; text-align: center;"><br /></div>From here, add your NFS mount location that you've specified within the NFS add-on (setting that part up is beyond the scope of this tutorial, you should know how to do that if you've gotten this far).
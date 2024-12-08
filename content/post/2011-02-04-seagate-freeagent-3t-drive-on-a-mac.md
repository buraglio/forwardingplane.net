---
id: 41
title: 'Seagate FreeAgent 3T drive on a mac'
date: '2011-02-04T14:00:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/'
permalink: /2011/02/04/seagate-freeagent-3t-drive-on-a-mac/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2011/02/seagate-freeagent-3t-drive-on-mac.html
Views:
    - '48'
categories:
    - How-To
---

I was recently helping my brother-in-law out with the new <a href="http://www.amazon.com/gp/product/B0045JLPNI?ie=UTF8&tag=nickburaglioc-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B0045JLPNI">Seagate FreeAgent GoFlex Desk 3 TB USB 3.0 External Hard Drive</a><img src="http://www.assoc-amazon.com/e/ir?t=nickburaglioc-20&l=as2&o=1&a=B0045JLPNI" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> he had purchased to do time machine backups on his mac.  I personally have the 2t version and have been pretty happy with it, save for one small incident that I think was my fault that required some basic data recovery.<br />Since the drive comes in a file system that is not HFS+ Journaled, it needed to be reformatted to support time machine backups.<br />Simple, right?  "A five minute process" I told him.<br />Well, I was wrong.  This drive just could <span style="font-weight:bold;">not</span> be formatted or re-partitioned using the standard OSX disk utility.   I walked him through it on the phone.  Partition failure.  It threw some cryptic error that I had not seen before in 15 years of using a mac.  I kinda figured it was something he was missing since I'm pretty awful at phone support, and if it wasn't, I wanted to see the error, so I drive over there.<br />Upon arriving, low and behold, it was in fact an error I'd never seen. I tried 3 more times to partition and format the drive and once just to format it.  Same errors every time, it would start and then throw an error that it had failed or that it had lost communication with the drive.<br />So, to test, I dropped to the trusty cli to see if I could do it from there.<br /><br />From the Terminal app (/Applications/Utilities/Terminal) I issued the command <div><span><br /></span></div><div><span>diskutil eraseDisk HFS+ Backup disk1</span><br /><br />Which was able to quickly accomplish the task.  From there, I was able to mount and manipulate it in the Disk Utility (/Applicaations/Utilities/Disk Utility).  Since I had not enabled the journal from the original command I reformatted the drive with MacOS X Entended (Journaled) and then it was ready to be a Time machine disk.<br /><br />I believe I could have done this all in one step using the command </div><div><span><br /></span></div><div><span><span>diskutil eraseDisk "Journaled HFS+" Backup disk1</span>.</span><br /><br /></div><div>I'm still unsure why Disk Utility would not work.<br /><br /><br /><br /><iframe src="http://rcm.amazon.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=nickburaglioc-20&o=1&p=8&l=as4&m=amazon&f=ifr&asins=B0045JLPNI" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
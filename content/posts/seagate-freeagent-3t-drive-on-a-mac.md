---
title: 'Seagate FreeAgent 3T drive on a mac'
date: Fri, 04 Feb 2011 20:00:00 +0000
draft: false
tags: [How-To]
---

I was recently helping my brother-in-law out with the new [Seagate FreeAgent GoFlex Desk 3 TB USB 3.0 External Hard Drive](http://www.amazon.com/gp/product/B0045JLPNI?ie=UTF8&tag=nickburaglioc-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B0045JLPNI)![](http://www.assoc-amazon.com/e/ir?t=nickburaglioc-20&l=as2&o=1&a=B0045JLPNI) he had purchased to do time machine backups on his mac. I personally have the 2t version and have been pretty happy with it, save for one small incident that I think was my fault that required some basic data recovery.  
Since the drive comes in a file system that is not HFS+ Journaled, it needed to be reformatted to support time machine backups.  
Simple, right? "A five minute process" I told him.  
Well, I was wrong. This drive just could not be formatted or re-partitioned using the standard OSX disk utility. I walked him through it on the phone. Partition failure. It threw some cryptic error that I had not seen before in 15 years of using a mac. I kinda figured it was something he was missing since I'm pretty awful at phone support, and if it wasn't, I wanted to see the error, so I drive over there.  
Upon arriving, low and behold, it was in fact an error I'd never seen. I tried 3 more times to partition and format the drive and once just to format it. Same errors every time, it would start and then throw an error that it had failed or that it had lost communication with the drive.  
So, to test, I dropped to the trusty cli to see if I could do it from there.  
  
From the Terminal app (/Applications/Utilities/Terminal) I issued the command

  

diskutil eraseDisk HFS+ Backup disk1  
  
Which was able to quickly accomplish the task. From there, I was able to mount and manipulate it in the Disk Utility (/Applicaations/Utilities/Disk Utility). Since I had not enabled the journal from the original command I reformatted the drive with MacOS X Entended (Journaled) and then it was ready to be a Time machine disk.  
  
I believe I could have done this all in one step using the command

  

diskutil eraseDisk "Journaled HFS+" Backup disk1.  
  

I'm still unsure why Disk Utility would not work.  
  
  
  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
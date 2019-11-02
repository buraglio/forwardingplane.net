---
title: 'Diff RANCID router configs with SVN'
date: Fri, 25 Jan 2013 00:27:09 +0000
draft: false
tags: [How-To, Lab Time, UNIX]
---

If you are running a network and aren't using [RANCID](http://shrubbery.net/rancid/), you should give it a serious look.  RANCID is a cross platform configuration management toolkit for backing up router configurations and certain environmental and hardware information into version control.  It's been around for as long as I can remember and supports nearly every platform I can think of, including a [few](http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/ "VDXrancid contrib scripts") [modules](http://www.forwardingplane.net/2011/06/alurancid-and-pfrancid/ "alurancid and pfrancid") that I cobbled together myself.  There is are a few nice web based front ends for CVS and SVN, I prefer to use [ViewVC](http://www.viewvc.org) because I have a lot of experience with it, however, there may be cases where a web server isn't a good option, unavailable or just too much work.  In this case, you'll want to know how to diff those configs from the CLI using the existing tools.  I find myself always forgetting the exact syntax of how to do this, so here it is. I prefer to use SVN, so we'll talk about that one here.   svn list will give a list of current devices in version control:```
svn list
``````
rtr1.company.com
rtr2.company.com
rtr3.company.com
sw1.company.com
sw2.company.com
```To look at a router config:```
svn cat <router>
svn cat rtr1.company.com
```See all revisions: svn log <router>```
svn log rtr1.company.com
------------------------------------------------------------------------
r863 | \_rancid | 2013-01-18 12:51:59 -0600 (Fri, 18 Jan 2013) | 1 line
updates - Change made by: buraglio
------------------------------------------------------------------------
r848 | \_rancid | 2013-01-09 14:00:27 -0600 (Wed, 09 Jan 2013) | 1 line
updates
------------------------------------------------------------------------
r847 | \_rancid | 2013-01-09 02:07:42 -0600 (Wed, 09 Jan 2013) | 1 line
updates
------------------------------------------------------------------------
r832 | \_rancid | 2012-12-12 09:42:33 -0600 (Wed, 12 Dec 2012) | 1 line
updates - Change made by: buraglio
------------------------------------------------------------------------
r804 | \_rancid | 2012-11-27 14:00:28 -0600 (Tue, 27 Nov 2012) | 1 line
updates
```Diff revisions: svn diff -r <version1>:<version2> <router>```
svn diff -r r863:r847 rtr1.company.com

Index: 710rtr.ui-iccn.org
===================================================================
--- rtr1.company.com	(revision 863)
+++ rtr1.company.com	(revision 847)
@@ -497,7 +497,6 @@
 !
 interface ethernet 1/1
  port-name rtr2 (1-1-11-2:e1/2)
- enable
  ip ospf area 0
  ip ospf cost 8
  ip address 10.209.143.1/30

```That's basically it. Anything you can do from svn, you can do with your RANCID gathered SVN data.
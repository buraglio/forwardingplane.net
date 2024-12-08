---
id: 389
title: 'Diff RANCID router configs with SVN'
date: '2013-01-24T18:27:09-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=389'
permalink: /2013/01/24/diff-rancid-router-configs-with-svn/
themeblvd_keywords:
    - 'RANCID, Cisco, Brocade, Subversion, bash, terminal, command line, SVN, CVS'
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'Use RANCID SVN data from the command line'
themeblvd_description:
    - 'Use RANCID SVN router configuration data from the command line.'
dsq_thread_id:
    - '3626948880'
Views:
    - '1319'
categories:
    - How-To
    - 'Lab Time'
    - UNIX
---

If you are running a network and aren't using <a href="http://shrubbery.net/rancid/" target="_blank" rel="noopener noreferrer">RANCID</a>, you should give it a serious look.  RANCID is a cross platform configuration management toolkit for backing up router configurations and certain environmental and hardware information into version control.  It's been around for as long as I can remember and supports nearly every platform I can think of, including a <a title="VDXrancid contrib scripts" href="http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/" target="_blank" rel="noopener noreferrer">few</a> <a title="alurancid and pfrancid" href="http://www.forwardingplane.net/2011/06/alurancid-and-pfrancid/" target="_blank" rel="noopener noreferrer">modules</a> that I cobbled together myself.  There is are a few nice web based front ends for CVS and SVN, I prefer to use <a href="http://www.viewvc.org" target="_blank" rel="noopener noreferrer">ViewVC</a> because I have a lot of experience with it, however, there may be cases where a web server isn't a good option, unavailable or just too much work.  In this case, you'll want to know how to diff those configs from the CLI using the existing tools.  I find myself always forgetting the exact syntax of how to do this, so here it is. I prefer to use SVN, so we'll talk about that one here.
&nbsp;
svn list will give a list of current devices in version control:
<pre>svn list</pre>
<pre>rtr1.company.com
rtr2.company.com
rtr3.company.com
sw1.company.com
sw2.company.com</pre>
To look at a router config:
<pre>svn cat &lt;router&gt;
svn cat rtr1.company.com</pre>
See all revisions:
svn log &lt;router&gt;
<pre>svn log rtr1.company.com
------------------------------------------------------------------------
r863 | _rancid | 2013-01-18 12:51:59 -0600 (Fri, 18 Jan 2013) | 1 line
updates - Change made by: buraglio
------------------------------------------------------------------------
r848 | _rancid | 2013-01-09 14:00:27 -0600 (Wed, 09 Jan 2013) | 1 line
updates
------------------------------------------------------------------------
r847 | _rancid | 2013-01-09 02:07:42 -0600 (Wed, 09 Jan 2013) | 1 line
updates
------------------------------------------------------------------------
r832 | _rancid | 2012-12-12 09:42:33 -0600 (Wed, 12 Dec 2012) | 1 line
updates - Change made by: buraglio
------------------------------------------------------------------------
r804 | _rancid | 2012-11-27 14:00:28 -0600 (Tue, 27 Nov 2012) | 1 line
updates</pre>
Diff revisions:
svn diff -r &lt;version1&gt;:&lt;version2&gt; &lt;router&gt;
<pre>svn diff -r r863:r847 rtr1.company.com
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
</pre>
That's basically it.  Anything you can do from svn, you can do with your RANCID gathered SVN data.  
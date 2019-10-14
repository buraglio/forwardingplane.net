---
title: 'sonrancid: A [very] basic RANCID module for sonicwall'
date: Mon, 15 Sep 2014 09:05:13 +0000
draft: false
tags: [How-To, Security, UNIX]
---


#### 
[Les Begnaud]( "lesbegnaud@gmail.com") - <time datetime="2014-12-11 09:00:00">Dec 4, 2014</time>

Hi there, I just implemented your set of scripts and had a couple comments: 1) seems to work just fine on an NSA 3600 2) have you attempted to rebuild a sonicwall based on the output of 'show current-config'? 3) any luck with getting the ever-changing passwords to behave themselves? I am not a fan of constant diffs... defeats the purpose of diffs 4) your github sonrancid script references clogin, and not sonlogin 5) Thanks so much for doing this! Let me know if I can help
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net/ "nick@buraglio.com") - <time datetime="2014-12-11 10:57:00">Dec 4, 2014</time>

I never got the password diffs to work and my TZ210 has died, so I no longer have a good way to test. I also never got an opportunity to restore from the backup due to the failure of the device. Use clogin, the sonlogin piece was unnecessary. In addition, don't upgrade to RANCID 3, it completely breaks this script due to the massive changes made. I'm working on a RANCID replacement as well that should, if we do it right, work on pretty much any gear. https://github.com/buraglio/claw It's pretty raw and not all in github yet, but we do have working proof of concept code that I hope to get up there this week.
<hr />

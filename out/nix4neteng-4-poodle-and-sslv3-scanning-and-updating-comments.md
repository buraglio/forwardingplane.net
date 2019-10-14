---
title: 'NIX4Neteng #4: POODLE and SSLv3, scanning and updating'
date: Wed, 15 Oct 2014 17:36:54 +0000
draft: false
tags: [How-To, NIX4NetEng, Security, UNIX]
---


#### 
[Ryan Harden]( "ancker@ancker.net") - <time datetime="2014-10-15 14:29:00">Oct 3, 2014</time>

I whipped up something in bash. It isn't as automated, but works if you have a list of hostnames/IPs you want to check. #!/bin/sh for i in host1.blah.net host2.blah.net do echo $i echo Q | openssl s\_client -connect $i:443 -ssl3 2> /dev/null | grep Protocol done
<hr />

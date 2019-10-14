---
title: 'Speculation and soapboxing about the leaked NSA spy catalog.'
date: Sat, 04 Jan 2014 17:15:40 +0000
draft: false
tags: [Security, Soap Box]
---


#### 
[Ryan Harden]( "ancker@ancker.net") - <time datetime="2014-01-06 13:48:13">Jan 1, 2014</time>

Not trying to brush this off as not-scary or not-happening, but I'm skeptical of the reality of some of this. Not only would you have to alter the code on a JNPR/CSCO/etc router or switch, but you'd also have to alter the code of any inline firewalls to pass the secret traffic without filtering and/or logging, and alter the code of any flow generation/aggregation/analyzation software to not report on the secret traffic that it might have observed via tap/SPAN/etc. I'm not saying it isn't possible or isn't being done, just that the scope of the compromises would have to be VASTLY larger than anyone has imagined if this is working very well in the real world. Most networks care enough to filter and instrument not only transit but management traffic in fine detail. I'd like to assume that someone running Bro/Snort/homegrown whatever would have noticed FBI/NSA/etc IPs hitting their control plane by bypassing ACLs somewhere.
<hr />
#### 
[Lennie]( "forwardingplaneblog@consolejunkie.net") - <time datetime="2014-01-04 18:16:11">Jan 6, 2014</time>

Judging by all the failed attempts, I think securing the OS or the boot code when someone has physical access to the device have ALL failed. Not one succeeded. I think we can safely say it won't stop experts. Examples of failed attempts are things like the Xbox: https://www.youtube.com/watch?v=82vf0JQS1Sk / https://www.youtube.com/watch?v=hDa-qpsrc4c and the current mess that is UEFI/SecureBoot doesn't sound much better: https://www.youtube.com/watch?v=V2aq5M3Q76U He did believe in 2012 that it might eventually be secure: http://mjg59.dreamwidth.org/12897.html I don't know, maybe it is possible. If all devices (HDD, SSD, Mainboard firmware/BIOS) it talks to include its own (updatable) firmware. Good luck securing that. Even the CPU in your PC/server has microcode that can be updated/replaced (though non-persistant ?). I believe there was a talk about the state of IPMI in servers, but I can't find it right now. This story comes close: http://www.securityweek.com/security-vulnerabilities-baseboard-management-controllers-rampant-research-finds There is a security trade off between updatable and non-updatable. Non-updatable firmware don't get security updates, updatable firmware probably won't get updates either ;-) and an intrusion is permanent. But for manufactures updatable is just a lot cheaper to work with.
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2014-01-06 14:01:04">Jan 1, 2014</time>

That's what I'm saying. I think it's happening, I really do. However, I want to see the data. I want to understand the mechanics. Inbound connectivity is easy to bypass, look at Meraki or a C&C botnet. They do a "phone home for instructions" to it's an outbound connection attempt, not necessarily an inbound traffic query, which is often handled differently in counters and monitoring systems. It's easier to hide outbound because less people, statistically, study their outbound traffic patterns.
<hr />

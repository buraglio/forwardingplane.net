---
id: 19
title: 'MicroFlow policing on Cisco Sup2T'
date: '2012-10-19T01:21:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2012/10/microflow-policing-on-cisco-sup2t/'
permalink: /2012/10/19/microflow-policing-on-cisco-sup2t/
Views:
    - '86'
categories:
    - Routing
---

Let me save you some time....Microflow Policing on the Catalyst 6500 / Sup2TXL doesn't yet work. Inbound it "kinda works".  You can configure it and it applies as a service policy, but even though outbound is "supported in hardware on the Supervisor2TXL", there is no software support for it in either the 15.0SY or 12.2(50)SY.  It took me a month to suss this out.....**Yes, I should have suspected.  I dont work on Cisco every day, I have Juniper MX, Brocade MLX and a multitude of other platforms to work on daily, so it took a bit. 
The short answer is that the capability won't be there until 15.1....something I'm not looking forward to since 15.x is very different, and, if you use any of the MLS features, get ready to re-learn them all.  I still have a strong belief that 15.0SY is missing half of the MLS knobs I need to turn. 

Please, someone correct me.  I'd be 
**extremely**
 happy to be wrong about this one.  
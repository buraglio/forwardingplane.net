---
id: 56
title: 'RADIUS and AAA on IOS'
date: '2010-09-01T18:44:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/09/radius-and-aaa-on-ios/'
permalink: /2010/09/01/radius-and-aaa-on-ios/
Views:
    - '73'
categories:
    - Routing
---

I'm not the greatest at AAA on Cisco's IOS. I always have to think about how to order things, and to test fallback (which you should do anyway). One of the caveats that I always overlook, no matter how many times I set this up, is that Cisco IOS software attempts authentication with the next listed authentication method only when there is no response from the previous method. If authentication fails at any point in this cycle—meaning that the security server or local username database responds by denying the user access—the authentication process stops and no other authentication methods are attempted[*](http://www.cisco.com/en/US/docs/ios/12_2/security/configuration/guide/scfaaa.html).  But, as I've said many, many times before, being able to look for documentation and knowing where to find information is just as valuable as having great retention. 
I almost always have to go and look for documentation for IOS references.    
What I want, really, is for radius to be consulted for all ssh logins, no login on console (this is controlled by a console server that requires other credentials that are not network dependent and maintained separately), and in the event of a RADIUS failure, for the authentication to fall back to the enable password.  For this to work, I had to do the following:
aaa new-modelaaa authentication login default local group radius enableaaa authentication login console noneaaa authentication enable default enableaaa authorization exec console none aaa session-id common
ip radius source-interface Loopback0 radius-server host <radius server ip> auth-port 1812 acct-port 1813 key 0 
radius-server source-ports 1645-1646
What this does is cause the lines to use  aaa authentication login default local group radius enable for their authentication, expect for console, which uses aaa authentication login console none.


The rest of the commands will allow the enable password to work, etc.  I tested and verified this as well. Adding a local user to the box also works for those that are adverse to waiting for RADIUS to timeout to enter the enable password (although I really don't see the point).  


Some other good reference material for this is available over at the [IOS hints blog](http://blog.ioshints.info/2007/03/configure-local-authentication-with-aaa.html).



---
title: 'How to install and use the Airport utility under Mountain Lion'
date: Wed, 09 Jan 2013 09:58:47 +0000
draft: false
tags: [IPv6, Lab Time, Musings]
---

I have a bunch of Apple wireless gear  at my house.  It's inexpensive, feature rich and easy to maintain.  However, with the update to mountain lion a while ago, the ability to install  the older Airport Utility stopped.  This is annoying since I have what apple now considers "advanced" features like IPv6 at my home and essentially all my gear here is a lab (except for the plex server =) I've been spending a lot of time on [cacti](http://www.cacti.net) lately, and I wanted to test out the syslog plugin....ok, easy.  It's all set up.  Then I got to thinking "why not just let this run and syslog all my gear like the good 'ol days?"  Nerdy?  Yes, but hey, I collect flow data at home and have a [weathermap](http://www.forwardingplane.net/homenet/) of my home network.  It keeps me eating my own dog food with the netflow exporter plugin on [pfSense](http://www.pfsense.org) and it's fun. Uh, oh.  No ability to set syslog receiver on the airport gear anymore.  Not cool.  \[Guess what, no way to change IPv6 settings anymore either\] No way to do a standard install of the old utility. Lame, Apple, Lame.  After poking around a bit I found a pretty easy way to do it as long as you're not afraid of the command line. Since at least a few other folks will want to do this, here it is: [Download the App](http://support.apple.com/kb/DL1536) from Apple. Mount the Downloaded disk. Open Terminal. Type:```
pkgutil --expand /Volumes/AirPortUtility/AirPortUtility56.pkg
cd ~/Desktop/AirPortTemp~/Desktop/AirPortTemp/AirPortUtility56Lion.pkg/
open Payload
cd "Payload 2 2/Applications/Utilities/"
open .
```[![](http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.32.08-PM.png "Screen Shot 2013-01-08 at 11.32.08 PM")](http://www.forwardingplane.net/wp-content/uploads/2013/01/Screen-Shot-2013-01-08-at-11.32.08-PM.png) Done.  That should open a finder window with the App in it.  You can copy it to you /Applications/Utilities folder and use it alongside the newer one.  You'll need to authenticate to copy into the /Applications/Utilities directory. Edits made and Poof!  Now I can see my syslogs from within cacti.
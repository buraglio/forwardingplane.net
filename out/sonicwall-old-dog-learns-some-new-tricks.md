---
title: 'Sonicwall - Old dog learns [some] new tricks'
date: Sat, 08 Dec 2012 00:00:26 +0000
draft: false
tags: [Firewall, Security, Security]
---

~12 years ago I had a drinking buddy that worked with me at the regional ISP.   We had a lot in common, he had been an icon back in the [didjits](http://en.wikipedia.org/wiki/The_Didjits) era of punk rock in Champaign Urbana and we had briefly been in a terrible band together.  He introduced me to a dude that to this day I just knew as "Ravi Sonicwall".  He had apparently been recruited from the U of I, written a lot of the low level pieces of the original sonicwall and retired to enjoy life and buy beers (he actually scolded me at a bar for buying him a beer saying "when I'm in town, I buy the beers"). I had purchased a few sonicwall boxes after that, having only really used linux, IOS, checkpoint on nokia boxes and \*_shudder_\* Novell Border manager.  I liked the boxes since they had a GUI and I could hand off day-to-day operations to someone that !=Me.  After a year or so in production, I started to become frustrated with them,  the ones I had lacked a CLI completely and had fallen behind on the things I needed to do with them.   Their cost to feature wasn't there for what I needed and the ones I had purchased systematically had hardware failures all within 7 months.  I wrote off sonicwall completely at that point. Fast forward a decade. Sonicwall purchased by Dell. We've heavily invested in the [Juniper SRX](http://www.juniper.net/us/en/products-services/security/srx-series/). The SRX mostly does what we ask of it (talk to me about Oracle replication through one and their SQL ALG). The SRX has some limitation as far as management and display of eye candy. While I personally like a CLI to rummage around in, not everyone does.  [Palo Alto Networks](http://www.paloaltonetworks.com) has an amazing GUI.  Like, the best I've ever seen.  Sonicwall......well, theirs always left me wanting back in the day.  Now.....wow, a totally different ballgame. Don't get me wrong, I'm not confident that the Sonicwall "Super Massive" won't compete (in this guys opinion) with a Juniper 5800.  **However, **their transparent mode is a tad better and their web management is an order of magnitude better.  Performance?  I don't think anything can touch an SRX loaded with SPCs, but the numbers are impressive.  I'd like to do a bake off once I get some time (and a super massive in my lab) That being said, I gave the Sonicwall we have as a demo a good go around.  I found it's ease of setup pretty refreshing.  For those that have non-networking savvy security folks running these boxes, they'll likely love the interface.  I like the AppFlow Monitor.  It's a nice reprensentation of the transit data in an easy to understand format.  Here is an example of the box in my lab after running a few days. [![](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.41-PM-1024x256.png "SonicWall AppFlow Monitor ")](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.41-PM.png)  [](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.41-PM.png)   The threat reports are nice as well, very eye candy and they seem pretty accurate based on what we threw at it and what we generally see in the wild west.   [![](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.48-PM-1024x256.png "Screen Shot 2012-12-07 at 4.09.48 PM")](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.48-PM.png) [![](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.41-PM1-1024x256.png "Screen Shot 2012-12-07 at 4.09.41 PM")](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.09.41-PM1.png) [![](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.10.00-PM-1024x256.png "Screen Shot 2012-12-07 at 4.10.00 PM")](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.10.00-PM.png)                         The real time monitor reminds me a lot of the Palo Alto.  It gives some serious eye candy, live, realtime graphs of any traffic transiting the box.  Very eye catching and I can see a use case for it. [![](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.48.44-PM-1024x635.png "Sonicwall Real Time Monitor")](http://www.forwardingplane.net/wp-content/uploads/2012/12/Screen-Shot-2012-12-07-at-4.48.44-PM.png) However, I find the management of the interfaces a bit clunky and the lack of non-beta IPv6 support is a but disappointing.  I'll be testing the IPv6 support soon, I'm just waiting on the activation of the box I have to support it. Firmware updates seem to require a registration of the machine in their system, something I understand but the old school networking guy in me really hates feature licensing and remote activation of network hardware.  A lot.  the fact that every vendor seems to be doing it just makes my skin crawl, but such is life. The box comes with an SSL VPN server as well, I've still been twiddling with getting mine working.  The smaller SOHO devices have wifi built in, but that's way outside of my scope, so I'll leave it at that.   The CLI isn't terrible, either.  It's more IOS that I remember, but a far cry from JunOS.  Tab complete works and there are a decent amount of options.  I've not yet tried to configure much with it but have used the show commands some.  Here is an example from the small box we have: _User:admin_ _Password:_ _labfw> show interface sta_ _labfw> show interface statistics _ _Interface statistics for X0_ _ InDiscards : 0_ _ InNUcast : 401464_ _ InUcast : 4921467_ _ InOctets : 2207976060_ _ InErrs : 0_ _ OutDiscards : 37_ _ OutNUcast : 9733_ _ OutUcast : 5407031_ _ OutOctets : 3031626437_ _ OutErrs : 0_ _ InUnkProto : 0_ _ InMcast : 291793_ _ InBcast : 109671_ _ OutMcast : 0_ _ OutBcast : 9733_ _Interface statistics for X1_ _ InDiscards : 0_ _ InNUcast : 5401982_ _ InUcast : 4496250_ _ InOctets : 3192806274_ _ InErrs : 0_ _ OutDiscards : 0_ _ OutNUcast : 54_ _ OutUcast : 4582195_ _ OutOctets : 2114718776_ _ OutErrs : 0_ _ InUnkProto : 0_ _ InMcast : 1500142_ _ InBcast : 3901840_ _ OutMcast : 0_ _ OutBcast : 54_  Overall, not a bad platform.  They've certainly done their homework.
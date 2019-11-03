---
title: 'NSR and ISSU on Juniper MX series with logical routers.'
date: Fri, 27 Apr 2012 22:15:00 +0000
draft: false
tags: [Routing]
---

Lets just say, for instance, that you have an MX series router at somewhere on your network. Lets also say that said router is carved into more than just the main logical system. For the sake of this writing, lets say that your eBGP sessions are in the default logical system and your IGP is in the logical system, lets call it "internal".  
 JunOS has some wonderful mechanisms for keeping things running, one is called [NSR](http://www.juniper.net/techpubs/en_US/junos9.5/information-products/topic-collections/swconfig-high-availability/nsr-overview.html) (Non Stop Routing), the other is called ISSU (In Service Software Upgrade). Typically these are really, really useful for performing non-impacting RE fail overs and software upgrades. Heck, I've upgraded an MX960 in the middle of the day with no impact whatsoever. Thats right, I was that guy. It should be noted, that the MX960s in question didn't have any logical systems configured, which brings us to why I jotted this down into this web page.  
  
Now, it's no secret that I am a fan of Juniper gear, and [I've talked about this before](http://tech.buraglio.com/2010/12/junos-issu.html). But frankly, our MX series that have logical systems need upgraded so infrequently, I actually forgot about this little tidbit.  For whatever reason, it really surprised me during the last upgrade I did even though it makes perfect sense and I knew about it already. What that time comes that you need to upgrade JunOS, you'll have to keep one very important thing in mind:  
  
**You can't take advantage of NSR in any logical system that isn't the default. **  
  
Additionally, You can't choose the protocol or the logical system that NSR works on, it's on for all protocols on the default logical system if you enable it.  
  
What does this actually mean?  Well, it means that if I do an ISSU (which you should still do even with logical systems), anything outside of my default logical system will re-converge.  If my eBGP sessions are outside, they'll drop and have to re-establish.  This isn't really that great of an idea if you peer with folks that keep dampen-happy.  Personally, I don;t like my BGP sessions to drop if they don't need to.  I'd rather deal with an IGP adjacency change than a bunch of BGP sessions having to re-establish and churn through potentially a handful of full tables.  
  
How do we get around the interruption this causes?  Well, the way we've solved it is to have 2 MX480's connected redundantly.  That way, even if ISSU is going to cause an interruption due to a peering or adjacency change, the alternate path still exists.  Why do we have this setup?  Well, ideally we'd have 4 MX480s and wouldn't need the logical systems, but hey, they're expensive.  
  
So, what it the take away from this episode of "as the packet turns"?  
  
If you must configure logical systems, know that NSR and ISSU doesn't really work as you may think in the non default.  Plan for some interruption, adjacency changes and or BGP sessions to drop.  
  
Or buy more routers.

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
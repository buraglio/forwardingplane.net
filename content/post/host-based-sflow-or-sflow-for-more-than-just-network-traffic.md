---
title: 'Host based sflow, or, sflow for more than just network traffic'
date: Sat, 27 Oct 2012 02:33:00 +0000
draft: false
tags: [Routing, UNIX]
---

I'm an awful sysadmin.  Running services permanently isn't really my forte, I tend to lean more on the "I'll get this proof of concept all working, prove that it works or doesn't, then roll it on for polishing by someone else" kinda guy.  That final 15% is something I'm constantly working to refine and better myself at accomplishing.   I'm decent at debugging network services, and can be handy in a "oh crap, it's down!" scamerio, but day to day sysadmin...not really my speciality.  
I know enough programming to be dangerous and have enough experience to know how to set up or fix pretty much any OS with nearly any service on it.  15 years as a slash and burn Network Engineer will often lend itself to that.  That being said, I do enjoy playing with new options, software packages and and LOVE instrumentation.  Then I came across [this](http://host-sflow.sourceforge.net/).     [Host based sflow](http://blog.sflow.com/2012/01/host-sflow-distributed-agent.html).....for more than just network traffic.  
This idea is **fantastic**.  
**Why** did I never think of it?!?!?!?  
  
Essentially it's [sflow](http://en.wikipedia.org/wiki/SFlow), a mechanism for monitoring network traffic, or thats at least how I thought of it being from the network side.  It's a lot like Netflow, but an open standard.  Many network devices support it for sampling transit routed packets.  It never occured to me to run it on hosts for other things like.....http hits, disk utilization....memory usage.  This seems perfect for a cloud environment, or for a VM farm....or anywhere you don't want to run snmpd or some weird commercial agent on a host.  
I already have an [nfsen](http://nfsen.sourceforge.net/)/[nfdump](http://nfdump.sourceforge.net/) instance, but it should work with any open source or commercial collector that supports sflow, which is a huge number.  Intermapper flow, inmon, there is a long list.  
  
I had to see this work, since we had just discussed this type of monitoring in our new \[broadband project of the year award winning\] ISP, [UC2B](http://www.uc2b.net/) that I am heavily involved in.  
So, on to the meat and potato..  
I grabbed the dpkg and installed it on my personal ubuntu server.  
  
_sudo dpkg -i hsflowd\_1.22.2-1\_x86\_64.deb _  
From there I needed to edit the conf file to point it my test flow collector, which happens to reside on the same box.  Use your favorite editor, I like vi personally but I've been using it for 15 years.   
_sudo vi /etc/hsflowd.conf_  
Change the following lines:  
  
_DNSSD = off_  

  
  
  _polling = 30_  
_  sampling.http = 10_  
_  sampling.memcache = 500_  
  
  
  

_ collector {_

_    ip = 127.0.0.1_

_     udpport = 6997_

_  }_

  

Close out the file.  I chose to tweak a few of the defaults to see what it'd yield.  

  

Now edit your nfsen.conf file

  
  
  
_%sources = (_  
_    'home'    => { 'port' => '6996', 'col' => '#0000ff', 'type' => 'netflow' },_  
_    'cupcake'    => { 'port' => '6997', 'col' => '#0000ff', 'type' => 'sflow' },_  
_);_  
  
  
_sudo /services/netflow/bin/nfsen reconfig_  
This should yield at the very least network data and provide a proof of concept. other services can be monitored by using the json options, but that's beyond the scope of this writing.  I could see a big win from this in a home brew cloud environment or a large VM farm since it can provide a very straightforward way to generate very useful data in a standard format that can be very simply monitored, queried and archived.      
_[Paessler Router Traffic Grapher](http://gan.doubleclick.net/gan_click?lid=41000000028007181&pid=UBM9786132095695&adurl=http%3A%2F%2Fwww.cdsbooksdvds.com%2Fproduct.jhtm%3Fsku%3DUBM9786132095695&usg=AFHzDLucmjq8niDqbnNmvyDzFPVpDnuqQQ&pubid=590157)_  
  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
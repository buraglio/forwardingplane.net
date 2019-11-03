---
title: 'JunOS ISSU'
date: Thu, 30 Dec 2010 00:26:00 +0000
draft: false
tags: [How-To, Routing]
---

I recently needed to upgrade a few MX480 routers and decided that it would be a good opportunity to get some experience with Juniper's in service software upgrade.  
I'd read a bit about it but I'd not had the chance to really use it. It's pretty straightforward and it does what it claims. The following are my notes from rolling through this on my test lab MX480.  
  
A few things are necessary to get going with ISSU, first and foremost, you need to have a box with two routing engines. Check.  
Second, some configuration is necessary to make this all work.  
The boxes need to be running nonstop-routing, they need to be syncronizing the configs, and they need to have graceful-switchover enabled.  
  
Here are the steps I went through on my vanilla test box to make this work:  
  
root# set chassis redundancy graceful-switchover  
root# set routing-options nonstop-routing  
root# set system commit synchronize  
  
If you already have those options set then you don't need to enter those commands.  
  
With those options set, you're ready to do the ISSU.  
  
root> request system software in-service-upgrade /var/tmp/jinstall-10.3R2.11-domestic-signed.tgz  
Chassis ISSU Check Done  
ISSU: Validating Image  
Checking compatibility with configuration  
Initializing...  
Using jbase-10.1R1.8  
vn\_read\_compressed\_block: invalid block index 550  
Verified manifest signed by PackageProduction\_10\_1\_0  
Verified jbase-10.1R1.8 signed by PackageProduction\_10\_1\_0  
Using /var/tmp/jinstall-10.3R2.11-domestic-signed.tgz  
....  
  
  
This takes a LONG time and generates a lot of scroll.  
  
  
You'll see long pauses and more text like  
  
  
Saving package file in /var/sw/pkg/jinstall-10.3R2.11-domestic-signed.tgz ...  
Saving state for rollback ...  
Backup upgrade done  
Rebooting Backup RE  
  
Rebooting re1  
ISSU: Backup RE Prepare Done  
Waiting for Backup RE reboot  
  
  
Then interesting thing start to show up:  
  
  
GRES operational  
Initiating Chassis In-Service-Upgrade  
Chassis ISSU Started  
ISSU: Preparing Daemons  
ISSU: Daemons Ready for ISSU  
ISSU: Starting Upgrade for FRUs  
ISSU: Preparing for Switchover  
  
  
This is where the magic starts. The nonstop-routing and hitless failover come into play as the route engines switch over. Very cool.  
  
On the console of the backup RE (now the master) you'll see messages like  
  
  
Message from syslogd@ at Dec 29 19:11:57 ...  
fpc0 RDP: Remote side reset connection: rdp.(fpc0:22528).(serverRouter:ppm)  
  
Message from syslogd@ at Dec 29 19:11:57 ...  
fpc1 RDP: Remote side reset connection: rdp.(fpc1:4096).(serverRouter:ppm)  
  
  
these are normal.  
  
Some things that I didn't expect, but probably should have:  
  
The old master stays the backup route engine after the ISSU  
The old master does NOT reboot into the new code, instead it stays on the original code requiring a manual reboot (unless, I asume, you add the "reboot" command on to the original upgrade command).  
On routers that have logical systems configured on them, only the master logical system supports nonstop active routing.  
  
I did the reboot manually  
  
  
root> request system reboot  
Reboot the system ? \[yes,no\] (no) yes  
  
  
\*\*\* FINAL System shutdown message from root@ \*\*\*  
System going down IMMEDIATELY  
  
  
Shutdown NOW!  
Reboot consistency check bypassed - jinstall 10.3R2.11 will complete installation upon reboot  
\[pid 65006\]  
  
  
and then did a failover to the old master.  
  
  
root> request chassis routing-engine master switch  
  
  
....and thats pretty much it. Upgrade complete.  
  
This is a really useful tool that allows for very minimal interruption during software upgrades. I'd recommend reading [this](http://www.juniper.net/us/en/local/pdf/whitepapers/2000280-en.pdf) white paper on ISSU if you're interested into diving into deeper details.  
  
Basically what ISSU does is to install junos on the backup route engine (re1) as normal, reboot it, validate and switch over to re1 and do the upgrade on the primary (now backup) route engine. The entire process took about 40 minutes on my mx480.

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
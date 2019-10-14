---
title: 'Upgrade Single ASR9k hw-module'
date: Wed, 20 Feb 2019 19:58:08 +0000
draft: false
---

ASR9k is a powerful device but management may be daunting to anyone not familiar with IOS-XR. Inserting new line cards in may require a manual upgrade of the module to match the current running code on the chassis

Show all slow and firmware details:

```
show hw-module fpd location _rack/slot/subslot_
```

In the admin prompt:

```
upgrade hw-module fpd all location 0/RSP1/CPU0
```

  
During the upgrade, this is the output, it will take a bit of time to perform the update. You may also need to upgrade things like fan trays, etc.

```
RP/0/RSP0/CPU0:core-9k(admin)#upgrade hw-module fpd all location 0/RSP1/CPU0Mon Feb 18 09:56:49.201 CST  
\*\*\*\*\* UPGRADE WARNING MESSAGE: \*\*\*\*\*    
\*  This upgrade operation has a maximum timout of 90 minutes.  \*    
\*  If you are executing the cmd for one specific location and  \*    
\*  card in that location reloads or goes down for some reason  \*    
\*  you can press CTRL-C to get back the RP's prompt.           \*    
\*  If you are executing the cmd for \_all\_ locations and a node \*    
\*  reloads or is down please allow other nodes to finish the   \*    
\*  upgrade process before pressing CTRL-C.                     \*  
% RELOAD REMINDER:   
 - The upgrade operation of the target module will not interrupt its normal    operation. However, for the changes to take effect, the target module    will need to be manually reloaded after the upgrade operation. This can    be accomplished with the use of "hw-module <target> reload" command.    
\- If automatic reload operation is desired after the upgrade, please use    the "reload" option at the end of the upgrade command.    
\- The output of "show hw-module fpd location" command will not display    correct version information after the upgrade if the target module is    not reloaded.  
  
NOTE: Chassis CLI will not be accessible while upgrade is in progress.
```
---
id: 689
title: 'VMWare ESXi CLI reference'
date: '2013-06-30T08:24:51-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=689'
permalink: /2013/06/30/vmware-esxi-cli-reference/
themeblvd_title:
    - 'VMWare ESX CLI reference'
themeblvd_keywords:
    - 'VMWare, SSH, CLI, Terminal, ESXi, vmsvc'
themeblvd_description:
    - 'Manage VMWare from the command line using vim-cmd and vmsvc'
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3651387277'
Views:
    - '76'
categories:
    - How-To
    - UNIX
    - Virtualization
---

One of my biggest complaints about VMware is that it is an enterprise application. It has historically catered to the masses, which I completely understand, but those of us that aren't a fortune 500 company are figuratively and operationally shoved into a corner and forced to find hackish ways of doing things to work around the enterprise nature.
One really, really good example of this is OS dependency. I hated architecture dependencies back in the old days (x86, SPARC, PPC) and I absolutely despise things that are OS platform dependent now.  It's inconvenient and just plain sucks for anyone using anything but that required platform. This goes for anything, mac dependent, MS dependent, unix dependent, whatever. I don't discriminate in my idealism.  While I realize it is an impossible, idealistic expectation,  I back up my stance 100% regardless.
That being said, one of the most irritating of those in recent memory has been VMware. Managing the VMWare ESXi instances that I run for both lab and production work is a pain. Since I'm not really a sysadmin or a virtualization engineer my knowledge of this stuff is surely limited I may be going about this in a non-optimal way, but until recently it has required a one-off host or VM running windows with the client to do anything useful. Apparently this has changed with the pay version in 5.something adding a web interface.  Unfortunately this isn't an option at this time for me, it's cost prohibitive. So, when I found it necessary to do some management without a windows VM or host, I was pleasantly surprised to find that I can do simple tasks via the SSH CLI. was able to query power state, start, stop, etc. using simple CLI tools. Now, these are all documented at the VMware KB, but I wanted to throw together a quick reference sheet for all of them in one place so I started compiling it [here](http://www.forwardingplane.net/unix/vmware-esxi-cli-reference/).  Please feel free to shoot over any additions or quick tips that should be on there. This is just the tip of the iceberg, I suspect (or maybe I'm just going about my VMware management all wrong; I'm open to that as well and suggestions on how to remedy).
The most useful for me so far have been inventory and power related.

```
List all VMs:
vim-cmd vmsvc/getallvms
List power state of VM:
vim-cmd vmsvc/power.getstate <VM ID>
Power on VM
vim-cmd vmsvc/power.on <VM ID>
Power off VM
vim-cmd vmsvc/power.off <VM ID>

```

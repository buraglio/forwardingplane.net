---
title: 'Monitoring VMware ESXi with SNMP and Cacti'
date: Mon, 19 Jan 2015 10:02:10 +0000
draft: false
tags: [How-To, Lab Time, UNIX, Virtualization]
---

VMWare is a powerful tool, and monitoring is a critical service. How does one monitor such an integral piece of infrastructure, and what do they monitor it with? There are powerful commercial ways of monitoring [VMware](http://www.vmware.com/), however, for those with existing [SNMP](http://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) based systems in place, specifically [cacti](http://www.cacti.net/), there are options. To that end, I'll set aside my strong distaste for SNMP \[yet again\], because those are for a larger, less useful series of posts.

Luckily for those of us that need it there exists in that vast wilderness we call the internet, a user contributed [cacti](http://www.cacti.net/) template for monitoring basic functionality with SNMP and cacti and it is available [here](http://forums.cacti.net/download/file.php?id=29171&sid=888e5451bc68b1c05a5b7dec6667afd2), and with the full thread being worth a read [here](http://forums.cacti.net/viewtopic.php?f=12&t=52122). Since VMWare ESXi doesn't have SNMP enabled (or really exposed from what I can tell), you have to do some CLI jockeying to make it work. Full disclosure, I'm not a vmware expert by any stretch of the imagination, but I have been hacking at it for a few years because it is low overhead to use comparatively speaking, offers a free version for my lab, makes a nice contrast to my KVM system and is widely deployed, so I want to understand it. Your mileage may vary with what I've got here.

Enabling ssh is beyond the scope of this post but details can be found [here](http://www.thomasmaurer.ch/2014/01/enable-ssh-on-vmware-esxi-5-5/). It's fairly straightforward.[![vmware-snmp-device](http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png)](http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png)

Details of enabling SNMP for vmware 5.5 can be found [here](https://pubs.vmware.com/vsphere-51/index.jsp#com.vmware.vsphere.monitoring.doc/GUID-0EB48A32-34B0-4003-B2D0-ADE3BAFD29F0.html), essentially one simply needs to run the following commands from within an ssh session:

```
esxcli  system snmp set --communities <community>
esxcli system snmp set --port 161
esxcli system snmp set --enable true
```

Getting the cacti scripts in place is a little more involved, but it's still pretty simple. Using the importer just add the new template. [![Screenshot 2015-01-10 10.09.09](http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.09.09.png)](http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.09.09.png)

 Once that is imported you'll need to move some scripts into place within the cacti system as below (adjust your paths as needed; I moved them directly from my workstation into place)

```
scp ss\_esxi\_vhosts.php netmon:/var/lib/cacti/scripts/
scp cacte\_esxi\_template/resource/snmp\_queries/\* netmon:/usr/share/cacti/resource/snmp\_queries/
```

[](http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.10.43.png)[![](http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png)](http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png)

[](http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.13.33.png)

Then adjust the template being used for your ESXi server or add it as a new host if it was not there already. The new template should show up in the list.

Once complete the cacti server should start graphing and checking uptime, etc. IF it does not, make sure the scripts are in place and have the correct permissions. It's also useful (although not required) to add the additional parameters to the host.

Once complete, the cacti system should be able to baseline (and alert if so desited, using thresholds) on any of the newly added variables, including number of VMs, number of VMs using vmware tools, number of VMs running, disk space, processes, network traffic, etc.

![vmware-create-graphs](http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-create-graphs.png)  

I have yet to be able to get successful CPU graphs, but I suspect it is user error on my part and I've not investigated yet. Overall, I'd call it a pretty bigwin for anyone that has an existing cacti installation and wants to include their vmware system(s). It should also be said that the readme that accompanies the template is relatively useful.
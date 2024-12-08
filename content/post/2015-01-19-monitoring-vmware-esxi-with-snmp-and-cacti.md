---
id: 1112
title: 'Monitoring VMware ESXi with SNMP and Cacti'
date: '2015-01-19T04:02:10-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1112'
permalink: /2015/01/19/monitoring-vmware-esxi-with-snmp-and-cacti/
themeblvd_noindex:
    - 'true'
themeblvd_title:
    - 'Basic monitoring of vmware esxi with snmp and cacti '
themeblvd_keywords:
    - 'vmware, esxi, cacti, linux, virtualization, NFV, SDN, openflow, buraglio, nick buraglio, centos, security, monitoring, SNMP'
themeblvd_description:
    - 'enable cacti to monitor and graph vmware esxi with snmp'
dsq_thread_id:
    - '3435229534'
Views:
    - '1726'
categories:
    - How-To
    - 'Lab Time'
    - UNIX
    - Virtualization
---

<div>VMWare is a powerful tool, and monitoring is a critical service. How does one monitor such an integral piece of infrastructure, and what do they monitor it with? There are powerful commercial ways of monitoring <a href="http://www.vmware.com/" target="_blank" rel="noopener noreferrer">VMware</a>, however, for those with existing <a href="http://en.wikipedia.org/wiki/Simple_Network_Management_Protocol" target="_blank" rel="noopener noreferrer">SNMP</a> based systems in place, specifically <a href="http://www.cacti.net/" target="_blank" rel="noopener noreferrer">cacti</a>, there are options. To that end, I'll set aside my strong distaste for SNMP [yet again], because those are for a larger, less useful series of posts.</div>
<div>Luckily for those of us that need it there exists in that vast wilderness we call the internet, a user contributed <a href="http://www.cacti.net/">cacti</a> template for monitoring basic functionality with SNMP and cacti and it is available <a href="http://forums.cacti.net/download/file.php?id=29171&amp;sid=888e5451bc68b1c05a5b7dec6667afd2" target="_blank" rel="noopener noreferrer">here</a>, and with the full thread being worth a read <a href="http://forums.cacti.net/viewtopic.php?f=12&amp;t=52122" target="_blank" rel="noopener noreferrer">here</a>. Since VMWare ESXi doesn't have SNMP enabled (or really exposed from what I can tell), you have to do some CLI jockeying to make it work. Full disclosure, I'm not a vmware expert by any stretch of the imagination, but I have been hacking at it for a few years because it is low overhead to use comparatively speaking, offers a free version for my lab, makes a nice contrast to my KVM system and is widely deployed, so I want to understand it. Your mileage may vary with what I've got here.</div>
<div>Enabling ssh is beyond the scope of this post but details can be found <a href="http://www.thomasmaurer.ch/2014/01/enable-ssh-on-vmware-esxi-5-5/" target="_blank" rel="noopener noreferrer">here</a>. It's fairly straightforward.<a href="http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png"><img class="aligncenter  wp-image-1123" src="http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png" alt="vmware-snmp-device" width="494" height="218" /></a></div>
<div>Details of enabling SNMP for vmware 5.5 can be found <a href="https://pubs.vmware.com/vsphere-51/index.jsp#com.vmware.vsphere.monitoring.doc/GUID-0EB48A32-34B0-4003-B2D0-ADE3BAFD29F0.html" target="_blank" rel="noopener noreferrer">here</a>, essentially one simply needs to run the following commands from within an ssh session:</div>
<div></div>
<pre>esxcli  system snmp set --communities &lt;community&gt;
esxcli system snmp set --port 161
esxcli system snmp set --enable true</pre>
<div>Getting the cacti scripts in place is a little more involved, but it's still pretty simple. Using the importer just add the new template. <a href="http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.09.09.png"><img class="alignright size-full wp-image-1115" src="http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.09.09.png" alt="Screenshot 2015-01-10 10.09.09" width="140" height="58" /></a></div>
<div> Once that is imported you'll need to move some scripts into place within the cacti system as below (adjust your paths as needed; I moved them directly from my workstation into place)</div>
<div>
<div></div>
<pre>scp ss_esxi_vhosts.php netmon:/var/lib/cacti/scripts/
scp cacte_esxi_template/resource/snmp_queries/* netmon:/usr/share/cacti/resource/snmp_queries/</pre>
</div>
<div><a href="http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.10.43.png">
</a><a href="http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png"><img class="alignright wp-image-1123 " src="http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-snmp-device.png" alt="" width="427" height="188" /></a></div>
<div><a href="http://www.forwardingplane.net/wp-content/uploads/2015/01/Screenshot-2015-01-10-10.13.33.png">
</a>
<div>Then adjust the template being used for your ESXi server or add it as a new host if it was not there already. The new template should show up in the list.</div>
<div>Once complete the cacti server should start graphing and checking uptime, etc. IF it does not, make sure the scripts are in place and have the correct permissions. It's also useful (although not required) to add the additional parameters to the host.</div>
<div>Once complete, the cacti system should be able to baseline (and alert if so desited, using thresholds) on any of the newly added variables, including number of VMs, number of VMs using vmware tools, number of VMs running, disk space, processes, network traffic, etc.</div>
<div></div>
<div></div>
<div>
<img class="alignright  wp-image-1122" src="http://www.forwardingplane.net/wp-content/uploads/2015/01/vmware-create-graphs.png" alt="vmware-create-graphs" width="425" height="256" />
&nbsp;
<div></div>
<div>I have yet to be able to get successful CPU graphs, but I suspect it is user error on my part and I've not investigated yet. Overall, I'd call it a pretty bigwin for anyone that has an existing cacti installation and wants to include their vmware system(s). It should also be said that the readme that accompanies the template is relatively useful.</div>
</div>
</div>
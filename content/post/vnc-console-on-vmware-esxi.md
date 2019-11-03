---
title: 'VNC Console on VMware ESXi'
date: Sun, 28 Apr 2013 03:39:54 +0000
draft: false
tags: [How-To, Lab Time, Virtualization]
---

Let me preface this post by saying that I am absolutely not an enterprise IT or systems guy, take everything that I write here on out with that as a side dish.  I'm also very, very cheap. That said, one of the things I really like about KVM is the ability to easily view the console of a guest system using free, non-windows software like VNC. However, much like everything in life, there are reasons to do one thing or another. I love VMware as well. It's refined, well documented, incredibly feature rich and works phenomenally well. It's also an enterprise app and to get a lot of the elegant features you either need a windows machine or the expensive paid version. Or both. I generally have neither money to spend on lab stuff or software licenses, which is why I generally use OSS. VMware, does, however, allow for free limited use of ESXi in such a way that is more than I need for my lab environments.  This is a great compliment to the XEN, KVM and other virtualization stuff I use for entertaining myself, learning new tech and labbing things up. So, when I wanted to see if I could get to the console of a few VMs I have without the paid app or a windows machine running vsphere, [the internets took care of me](http://t3chnot3s.blogspot.com/2012/03/how-to-enable-vnc-access-to-vms-on.html).  This is actually really straight forward and takes very little time.  I made a quick screen cast of adding it to one of my template VMs. There are, of course, a few caveats.  Knowing how to [properly edit the VMX file](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1714) is important.  Knowing that VNC is insecure is also very important. In my lab, this is all behind my security perimeter and it's fairly safe to open it up. In a nutshell, Here is what you need to do:```
chmod 777 /etc/vmware/firewall/service.xml
```Edit the firewall file:```
vi /etc/vmware/firewall/service.xml
```Add this to the bottom before the last line:```
 VNC
    outbound
        tcp
        dst
        5800
           5999 
     inbound
        tcp
        dst
        5800
           5999 
     true
     false 
```Make sure the ports are configured at you want them to be. I chose 5900 - 5999 since it made sense to me. Then:```
esxcli network firewall refresh
esxcli network firewall ruleset list
```Should now see:```
VNC true
```at the very bottom. In the .vmx file of each VM:```
RemoteDisplay.vnc.enabled = "TRUE"
RemoteDisplay.vnc.port = 5910
RemoteDisplay.vnc.password = "VNCPassword"
```Directly from the VMware site: Any manual additions to the .vmx file from ESX/ESXi are overwritten by the entries stored in the vCenter Server database. If you need to edit a virtual machine's .vmx file, first remove it from vCenter Server's inventory (right-click it and choose Remove from Inventory). After you edit it, register the virtual machine again from the ESX command line.```
vmware-cmd -s register /vmfs/volumes/datastore/virtual machine directory/virtual machine name.vmx
```Where datastore is the datastore name, virtual machine directory is the directory containing the virtual machine files, and virtual machine name is the name of the virtual machine files. This needs to be the full path, it gave me a weird error trying to do it in the directory without the full path. For example:```
vim-cmd solo/registervm /vmfs/volumes/Storage1/vm1/vm1.vmx
```Start the VM and connect to the VNC console configured.
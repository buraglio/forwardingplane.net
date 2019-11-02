---
title: 'Juniper to IOS conversion chart'
date: Sat, 27 Oct 2012 20:17:00 +0000
draft: false
tags: [Routing]
---

    Moving to JunOS from IOS can be a daunting task.  It's a completely different command structure and the config, by default, looks like a programming language.  I was fortunate enough to have gotten in on using JunOS very early in my career, 1/3 in to be exact (as of this writing).  Not to mention that wen I got started, IOS wasn't the only game in town.  Remember Xylan?  Gandalf?  OpenRoute? How about Ascend?  
  
    That being said, a conversion chart is a useful thing.  
  
    These are everywhere on the net.  Recently I was asked to provide some of this for my job, so I took most of what I could find on the net and compiled it together using my favorite one as a template adding this and that from my own bag of what I thought was useful, which was very little since the initial one was pretty complete.  I suspect this may migrate to a "page" and not just a post, and will likely be a bit of a living document as I find more and more useful bits and pieces.  
  
  

**Basic CLI and Systems Management Commands**

Junos Command

IOS Command

set date

clock set

ping

ping

request system reboot

reload

request message

send

show system uptime

show clock

show chassis environment

show environment

show cli history

show history

show system statistics

show ip traffic

show logshow log _file name_

show logging

show system processes

show processes

show configuration

show running config

request support information

show tech-support

show system users

show users

show version | show chassis hardware

show version

traceroute

trace

**Switching Commands**

Junos Command

IOS Command

show ethernet-switching interfaces

No equivalent command

show spanning-tree bridge

show spanning-tree

show ethernet-switching table

show mac address-table

show log messages

show logging

**Interface Commands**

Junos Command

IOS Command

clear interface statistics

clear counters

show interfaces  
show interfaces detail  
show interfaces extensive

show interfaces

show interfaces  
show interfaces detail  
show interfaces extensive

show ip interface

show interfaces terse

show ip interface brief

**Routing Protocol Commands**

Junos Command

IOS Command

clear arp

clear arp-cache

show arp

show arp

show route

show ip route

show route summary

show ip route summary

show policy  
show policy _policy-name_

show route-map

show system connections

show tcp

show ospf database

show ip ospf database

show ospf interface

show ip ospf interface

show ospf neighbor

show ip ospf neighbor

clear bgp neighbor

clear ip bgp

clear bgp damping

clear ip bgp dampening

show route protocol bgp

show ip bgp

show route community

show ip bgp community

show route damping decayed

show ip bgp dampened paths

show bgp neighbor

show ip bgp neighbors

show route advertising-protocol bgp_neighbor-address_

show ip bgp neighbors _address_ advertised-routes

show route receive-protocol bgp_neighbor-address_

show ip bgp neighbors _address_ received-routes

show bgp group

show ip bgp peer-group

show route aspath-regex

show ip bgp regexp

show bgp summary

show ip bgp summary

  
**Other Useful JunOS commands**  
  
_show conf | display set_ --display the configuration in a single line per command syntax, useful for cut and paste  
_show conf | display xml_\--display the configuration as XML, useful for programming to the XMLRPC interface  
Adding _| no-more_ to a command such as:  
_request support information | no-more_ --removes the need to space bar through long output.  Can also be used for piping to a file like  
_request support information | no-more | save_

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
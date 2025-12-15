---
id: 42
title: 'Moving JunOS code between SRX cluster nodes'
date: '2011-01-07T20:11:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/01/moving-junos-code-between-srx-cluster-nodes/'
permalink: /2011/01/07/moving-junos-code-between-srx-cluster-nodes/
Views:
    - '255'
categories:
    - How-To
    - Security
---

Regardless of the fact that there is now a good ISSU-like service for the SRX (named Low-Impact Cluster Upgrade; LICU for short), if you're upgrading your Active/Active cluster from something that isn't 10.4, or if you just aren't comfortable with how baked LICU actually is, you'll need to know how to move the junos code around. This is easy if you have physical access to both nodes, but for those that have.
This was a problem for me in that our cluster nodes have geographic diversity. In other words, they're far apart. Being how I am, I don't want to trek all around to hand load code from a USB key and being how the SRX cluster works, I can't easily get to node1 over the network since it's part of a cluster.

Low and behold, there is a very simple way to move this code around over the control network. Enter our old friend [rcp](http://www.mkssoftware.com/docs/man1/rcp.1.asp).
Log into node0 and load the code as normal.

node0>file copy scp://buraglio@desktop.domain.edu/Users/buraglio/Downloads/junos-srx5000-10.4R1.9-domestic.tgz /var/tmp/junos-srx5000-10.4R1.9-domestic.tgz

From here, it's really easy but will require dropping to the unix (FreeBSD, Yay!) shell so I'm always careful of what I'm typing and by all means be careful.

{primary:node0}buraglio@node0> start shell % suPassword: <enter><enter></enter>root@node0% rcp -T /var/tmp/junos-srx5000-10.4R1.9-domestic.tgz node1:/var/tmp/


Thats pretty much it. Upgrade per the normal active/active procedure. 

[Here](http://kb.juniper.net/InfoCenter/index?page=content&id=KB17410&actp=RSS&smlogin=true) is a Juniper knowledge base article on this procedure for second reference.
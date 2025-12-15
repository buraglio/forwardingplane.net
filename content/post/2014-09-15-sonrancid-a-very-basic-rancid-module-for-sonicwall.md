---
id: 1058
title: 'sonrancid: A [very] basic RANCID module for sonicwall'
date: '2014-09-15T03:05:13-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1058'
permalink: /2014/09/15/sonrancid-a-very-basic-rancid-module-for-sonicwall/
themeblvd_title:
    - 'Back up SonicWall configs with RANCID'
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'Sonicwall, SonicOS, RANCID, sonrancid, security, devops, SDN, buraglio, Nick Buraglio, UNIX'
themeblvd_description:
    - 'Back up and archive SonicWall firewall configurations using RANCID. '
dsq_thread_id:
    - '3020195776'
Views:
    - '562'
categories:
    - How-To
    - Security
    - UNIX
---

I know, I know, I'm always saying that you don't need a firewall. That's mostly to get your attention to push my agenda of sane security architecture, I do actually believe that firewalls are appropriate in a great many use cases and I've managed them big and small ranging from <a title="Juniper SRX Cluster" href="http://www.forwardingplane.net/2010/08/juniper-srx-cluster/">Juniper SRX 5800 clusters</a> to tiny purpose built BSD distros on custom hardware. I even managed <a href="http://www.checkpoint.com/" target="_blank" rel="noopener noreferrer">Checkpoint</a> and <a href="http://www.kulichki.com/moshkow/SECURITY/gauntlet.txt" target="_blank" rel="noopener noreferrer">gauntlet firewall</a> back in the 1990s. And <a href="https://www.novell.com/products/bordermanager/" target="_blank" rel="noopener noreferrer">Novell Border manager</a>....good gravy....border manager. I just had a chill, that thing is still around.  They work well when spec'd, designed, maintained correctly and placed in an appropriate location in a network architecture.  That said, I have a few SonicWall devices that I work on occasionally and it has always irritated me that there was not a usable <a href="http://www.shrubbery.net/rancid/" target="_blank" rel="noopener noreferrer">RANCID</a> module for it.  To that end, I hacked up the Cisco RANCID script to support very rudimentary config backups.
<em>&lt;Insert comment about having some DevOps skills is useful, even if they are very basic like mine.&gt;</em>
The script will log in and pull the config and version using the following commands:
<pre>show current-config</pre>
<pre>show version</pre>
I am really hoping that someone else will pick it up and massage it a bit because it is very chatty and will produce a diff every time due to the way SonicOS presents some of its configuration parameters. It also needs tested against larger SonicWall devices as I only have smaller boxes to run against.  I know it works against a TZ210, YMMV. Please post comments on github if you use it with anything else.   The password hash is particularly annoying, it always changes when the configuration is displayed. Some of the framework is there to remove it so I may hack at it a bit more but it's usable in the loosest sense for the short term.  It's available on <a href="https://github.com/buraglio/sonrancid" target="_blank" rel="noopener noreferrer">my github site</a>.
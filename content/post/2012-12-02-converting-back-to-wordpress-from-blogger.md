---
id: 77
title: 'Converting (back) to wordpress from Blogger'
date: '2012-12-02T13:41:08-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=77'
permalink: /2012/12/02/converting-back-to-wordpress-from-blogger/
Views:
    - '63'
categories:
    - Musings
    - UNIX
---

For a long time I ran a blog called [tech.buraglio.com](http://www.forwardingplane.net) that was a self hosted wordpress site. After having kids and getting a bit busier at work, I decided to move everything that I had been hosting (images, scripts, hacks, blogs and DNS) to "the cloud". I managed to do this for everything but my primary DNS resolver, which I had always intended to keep, and one [wordpress blog](http://www.shitenonions.com) that I hosted for someone else.

[![](http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress-300x200.jpg)](http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress.jpg)

 
I moved my image hosting from gallery2 to flickr (backup on picasaweb), secondary DNS to nether.net and afraid.org, scripts, hacks and the like to google code and my blogs to blogger.  Blogger was **very** easy, stable and highly available.  It was also far less flexible.

![](http://www.undertheradarblog.com/wp-content/uploads/2011/12/Top-5-Best-Free-Cloud-Storage-Services-That-You-Need-And-Are-Useful.png)

I continued to write from time to time, mostly ramblings or notes on some weird thing I has to set up.  I noticed that a few of my posts were getting a decent amount of traffic, something I was a bit surprised about.  I started to write a bit more......more traffic.  I started cross posting to [twitter](http://www.twitter.com/buraglio).  More traffic.  OK, maybe what I was jotting down was actually useful to someone.  Or I had a stalker.  Probably not the latter.
![](http://blog.dreamhost.com/wp-content/uploads/2009/09/23-wordpress_logo.png)  ![](http://www.decodeunicode.org/en/u+003e/data/glyph/196x196/003E.gif)![](http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Blogger.svg/256px-Blogger.svg.png)
Since I already had apache working and serving other stuff, and one of them is another WP site, I already has MySQL running.  I just enabled SSL for the new domain that I had added and was ready to go.  I'm a really lazy sysadmin, so I used this as a reference.
First, installing wordpress.  I chose the [SVN install](http://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion) for easier upgrades down the road.  Upgrading WP was somethingI alweays hated doing, so I let it languish when I used it before.  At least now I should, in most cases, be able to just type "*svn update*" to get it up to date (after verifying a back up, of course).
After using the [blogger importer](http://wordpress.org/extend/plugins/blogger-importer/), I had to go through and set all of my old blogger drafts to draft status again, wordpress has changed them all to published status. A minor detail. the rest  should be pretty straight forward, right?  Maybe not.  I've done a lot of twitter and bit.ly linking to my posts and I had a feedburner and quite a few RSS subscribers.  The feedburner stuff I'm probably going to have to write off.  The [link](http://feeds.feedburner.com/forwardingplane/WszR) needed to be more obvious as to what it was. The biggest thing I have to worry about is that Blogger formats it's "pretty" links in a different way than wordpress.  Thankfully, however, I'm self gosting so I can use apache magic to fix this.
*.htaccess* to the rescue.
For every post, I've had to create a redirect entry in my .htaccess file.  Most of it is done, but for reference, here is what it looks like:
*Redirect 301 /2012/11/sdn-across-domains-in-wan-novice-look.html http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/*
*Redirect 301 /2012/11/and-purple-pony.html http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/*
*Redirect 301 /2012/11/using-brocade-mlxe-as-replicator-to-ids.html http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/*
*Redirect 301 /2012/11/workflow-and-my-every-day-workstation.html http://www.forwardingplane.net/2012/11/workflow-and-my-every-day-workstation-setup/*
*Redirect 301 /2012/11/vdxrancid-contrib-scripts.html http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/*
*Redirect 301 /2012/11/scinet-privileged-few.html http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/*
*Redirect 301 /2012/11/juniper-ex-4200-arp-ndp-problem-or.html http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/*
*Redirect 301 /2012/11/and-purple-pony.html http://www.forwardingplane.net/2012/11/and-a-purple-pony/*
*Redirect 301 /2012/10/directionality_31.html http://www.forwardingplane.net/2012/10/directionality/*
*Redirect 301 /2012/10/juniper-to-ios-conversion-chart.html http://www.forwardingplane.net/2012/10/juniper-to-ios-conversion-chart/*
*Redirect 301 /2012/10/host-based-sflow-or-sflow-for-more-than.html http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/*
....and so on.
I got really used to the google analytics, so I had to add a plugin for that.  I chose [Google Analyticator](http://wordpress.org/extend/plugins/google-analyticator/).  ....Then I realized that users having to create  accounts is lame, so I added [Social Connect](http://wordpress.org/extend/plugins/social-connect/).
So far, that's pretty much it.  However, since this is a public unix box I need to make sure it's relatively safe, so I would highly recommend installing [sshguard](http://www.sshguard.net) in addition to whatever other firewall rules it can dynamically block offensive hosts and then unblock them after a period of time.  I am also a big fan of [duo security](http://www.duosecurity.com) for [two factor auth](http://en.wikipedia.org/wiki/Two-factor_authentication).
We'll see how this goes......
 
 
<script type="text/javascript">// <![CDATA[
google_ad_client = "ca-pub-5397547757892743";
/* Wordpress Small */
google_ad_slot = "7170585744";
google_ad_width = 468;
google_ad_height = 15;
// ]]></script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">// <![CDATA[
// ]]></script>
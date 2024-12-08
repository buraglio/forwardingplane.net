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

For a long time I ran a blog called <a href="http://www.forwardingplane.net">tech.buraglio.com</a> that was a self hosted wordpress site. After having kids and getting a bit busier at work, I decided to move everything that I had been hosting (images, scripts, hacks, blogs and DNS) to "the cloud". I managed to do this for everything but my primary DNS resolver, which I had always intended to keep, and one <a href="http://www.shitenonions.com">wordpress blog</a> that I hosted for someone else.
<p style="text-align: center;"><a href="http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress.jpg"><img class="size-medium wp-image-84 aligncenter" title="bloggerpress" src="http://www.forwardingplane.net/wp-content/uploads/2012/12/bloggerpress-300x200.jpg" alt="" width="300" height="200" /></a></p>
&nbsp;
I moved my image hosting from gallery2 to flickr (backup on picasaweb), secondary DNS to nether.net and afraid.org, scripts, hacks and the like to google code and my blogs to blogger.  Blogger was <strong>very</strong> easy, stable and highly available.  It was also far less flexible.
<p style="text-align: center;"><img class="aligncenter" src="http://www.undertheradarblog.com/wp-content/uploads/2011/12/Top-5-Best-Free-Cloud-Storage-Services-That-You-Need-And-Are-Useful.png" alt="" width="480" height="253" /></p>
I continued to write from time to time, mostly ramblings or notes on some weird thing I has to set up.  I noticed that a few of my posts were getting a decent amount of traffic, something I was a bit surprised about.  I started to write a bit more......more traffic.  I started cross posting to <a href="http://www.twitter.com/buraglio" target="_blank" rel="noopener noreferrer">twitter</a>.  More traffic.  OK, maybe what I was jotting down was actually useful to someone.  Or I had a stalker.  Probably not the latter.
<img class="alignnone" src="http://blog.dreamhost.com/wp-content/uploads/2009/09/23-wordpress_logo.png" alt="" width="192" height="192" />  <img class="alignnone" src="http://www.decodeunicode.org/en/u+003e/data/glyph/196x196/003E.gif" alt="" width="196" height="196" /><img class="alignnone" src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Blogger.svg/256px-Blogger.svg.png" alt="" width="205" height="205" />
Since I already had apache working and serving other stuff, and one of them is another WP site, I already has MySQL running.  I just enabled SSL for the new domain that I had added and was ready to go.  I'm a really lazy sysadmin, so I used this as a reference.
First, installing wordpress.  I chose the <a href="http://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion" target="_blank" rel="noopener noreferrer">SVN install</a> for easier upgrades down the road.  Upgrading WP was somethingI alweays hated doing, so I let it languish when I used it before.  At least now I should, in most cases, be able to just type "<em>svn update</em>" to get it up to date (after verifying a back up, of course).
After using the <a href="http://wordpress.org/extend/plugins/blogger-importer/" target="_blank" rel="noopener noreferrer">blogger importer</a>, I had to go through and set all of my old blogger drafts to draft status again, wordpress has changed them all to published status. A minor detail. the rest  should be pretty straight forward, right?  Maybe not.  I've done a lot of twitter and bit.ly linking to my posts and I had a feedburner and quite a few RSS subscribers.  The feedburner stuff I'm probably going to have to write off.  The <a href="http://feeds.feedburner.com/forwardingplane/WszR" target="_blank" rel="noopener noreferrer">link</a> needed to be more obvious as to what it was. The biggest thing I have to worry about is that Blogger formats it's "pretty" links in a different way than wordpress.  Thankfully, however, I'm self gosting so I can use apache magic to fix this.
<em>.htaccess</em> to the rescue.
For every post, I've had to create a redirect entry in my .htaccess file.  Most of it is done, but for reference, here is what it looks like:
<em>Redirect 301 /2012/11/sdn-across-domains-in-wan-novice-look.html http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/</em>
<em>Redirect 301 /2012/11/and-purple-pony.html http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/</em>
<em>Redirect 301 /2012/11/using-brocade-mlxe-as-replicator-to-ids.html http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/</em>
<em>Redirect 301 /2012/11/workflow-and-my-every-day-workstation.html http://www.forwardingplane.net/2012/11/workflow-and-my-every-day-workstation-setup/</em>
<em>Redirect 301 /2012/11/vdxrancid-contrib-scripts.html http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/</em>
<em>Redirect 301 /2012/11/scinet-privileged-few.html http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/</em>
<em>Redirect 301 /2012/11/juniper-ex-4200-arp-ndp-problem-or.html http://www.forwardingplane.net/2012/11/juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac/</em>
<em>Redirect 301 /2012/11/and-purple-pony.html http://www.forwardingplane.net/2012/11/and-a-purple-pony/</em>
<em>Redirect 301 /2012/10/directionality_31.html http://www.forwardingplane.net/2012/10/directionality/</em>
<em>Redirect 301 /2012/10/juniper-to-ios-conversion-chart.html http://www.forwardingplane.net/2012/10/juniper-to-ios-conversion-chart/</em>
<em>Redirect 301 /2012/10/host-based-sflow-or-sflow-for-more-than.html http://www.forwardingplane.net/2012/10/host-based-sflow-or-sflow-for-more-than-just-network-traffic/</em>
....and so on.
I got really used to the google analytics, so I had to add a plugin for that.  I chose <a href="http://wordpress.org/extend/plugins/google-analyticator/" target="_blank" rel="noopener noreferrer">Google Analyticator</a>.  ....Then I realized that users having to create  accounts is lame, so I added <a href="http://wordpress.org/extend/plugins/social-connect/" target="_blank" rel="noopener noreferrer">Social Connect</a>.
So far, that's pretty much it.  However, since this is a public unix box I need to make sure it's relatively safe, so I would highly recommend installing <a href="http://www.sshguard.net" target="_blank" rel="noopener noreferrer">sshguard</a> in addition to whatever other firewall rules it can dynamically block offensive hosts and then unblock them after a period of time.  I am also a big fan of <a href="http://www.duosecurity.com" target="_blank" rel="noopener noreferrer">duo security</a> for <a href="http://en.wikipedia.org/wiki/Two-factor_authentication" target="_blank" rel="noopener noreferrer">two factor auth</a>.
We'll see how this goes......
&nbsp;
&nbsp;
<script type="text/javascript">// <![CDATA[
google_ad_client = "ca-pub-5397547757892743";
/* Wordpress Small */
google_ad_slot = "7170585744";
google_ad_width = 468;
google_ad_height = 15;
// ]]></script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">// <![CDATA[
// ]]></script>
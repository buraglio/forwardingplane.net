---
id: 26
title: 'A security oversight in Mail.app, or, a hidden bcc: field'
date: '2011-10-22T02:40:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/10/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/'
permalink: /2011/10/22/a-security-oversight-in-mail-app-or-a-hidden-bcc-field/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2011/10/security-oversight-in-mailapp-or-hidden.html
dsq_thread_id:
    - '4150996031'
Views:
    - '55'
categories:
    - How-To
    - Musings
---

Recently I was poking around Mail.app, setting up my new machine. I like to keep redundant copies of everything, email being no exception.  I have backups of all of my email dating back to 1998, for the most part.  It has come in handy from time to time and I like it for reference reasons.  It's a small amount of actual data as far as space goes, and it's easy to do.   I remembered the days of using mutt for email (which really weren't that long ago for me), and really liked the idea of setting a bcc of a separate address, not necessarily myself, but an email address inside of my administrative control, for CYA types of archiving.  Upon looking, I saw no way to do this within the default apple Mail.app.   <br /><br /><div style="clear: both; text-align: center;"></div>Doing a bit of google searching, I found that this is pretty easily doable with a default write command.  OK, awesome.  This is good news.  So I applied it:<br />(Open Terminal)<br /><i>defaults write com.apple.mail UserHeaders '{"Bcc" = "archive-address@domain.com"; }' </i><br /><br />Done. Great. So, lets test it. Send email and check bcc'd address.  Email is there.  Strange, however, the bcc field doesn't show up, or show anything at all.  That's right, there is absolutely no indication that this email is being bcc'd to another address. <br />This isn't really a problem for me, since I know that I set it up.  What it does mean, though, is that this could be applied to an unsuspecting user account, with absolutely <b>no authentication necessary, </b>and have every outgoing message silently sent to a harvesting account.  There is no easy way to check for this that I have found save for using terminal:<br /><br /><br /><i>[buraglio@dalek:~ ] defaults read com.apple.mail UserHeaders                                   </i><br /><i>{</i><br /><i>    Bcc = "archive-address@domain.com";</i><br /><i>}</i><br /><div><br /></div><br />OK, at least there is a way to tell.  Using the command <i>defaults read com.apple.mail UserHeaders </i>from terminal will show the info, but the fact that it's doable in such an obtuse way with no indication that mail is being bcc'd is a bit scary. <br />There is a preference pane that allows for tweaking of some of these "features", it's open source available <a href="http://secrets.blacktree.com/">here</a>, called BlackTree Secrets. <br /><br /><br /><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
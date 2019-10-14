---
title: 'Better support for Linux (and annoyed about it)'
date: Mon, 20 Jun 2011 08:43:00 +0000
draft: false
tags: [Musings, UNIX]
---

I've been a \*BSD user since around 1997, when I installed NetBSD on a Mac SE 30 that I got for free. I was always intrigued with alternative operating systems like BeOS, \*BSD, Plan9 and Linux so it made sense that I'd poke around with different systems.

I'd gone back and forth from OpenBSD to FreeBSD but eventually settled on FreeBSD as my OS of choice. I ran it as a desktop before MacOS X came out and was generally happy with it. I learned most of the common flavors of Linux over the years out of curiosity and necessity but always went back to BSD for anything critical.

  

I'm sad to say that I think this is changing.

  

I feel like a bit of a sell out, it was always cool to say I ran FreeBSD and to silently look at Linux users as nerdy dorks that were afraid of girls that lived in their mothers basement and talked about [Linus Torvalds](http://en.wikipedia.org/wiki/Linus_Torvalds) and [Richard Stallman](http://en.wikipedia.org/wiki/Richard_Stallman) like they are demigods.

As I get busier both personally and professionally, it's becoming more of a chore to manage a BSD system or a set of BSD systems. The ports collection is clunky and annoying to use once I saw the elegance of something like apt. The software support for the stuff I do every day either available for linux first or only available under linux. Network tunables like web100 are linux specific. HPC clusters are almost exclusively Linux. The straw that has broken the camels back is [THC-IPv6](http://www.thc.org/thc-ipv6/). I had a need to do some IPv6 testing that required poking at equipment in a way that tests it's metal. I needed tools to try to break the network and do other nefarious things. [THC-IPv6](http://www.thc.org/thc-ipv6/) fits the bill. It works ONLY under Linux due to the use of /proc. Yes, you can make /proc work under FreeBSD, but it's annoying and I'm fairly certain that the code still won't build without hackery that I'm not willing to do.

  

I'd been poking around with Debian for years as an alternative for those things that just don't run under BSD. The tools I need have been building fine under Debian and Ubuntu. It's just \*easy\*.

I'll still hold a place in my heart for BSD, I think the license it FAR superior (GPL has a host of issues that I'm not comfortable with), but for now, Im going to have to "sell out" and use Linux. Mark the calendar, this is the day the music died.

  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
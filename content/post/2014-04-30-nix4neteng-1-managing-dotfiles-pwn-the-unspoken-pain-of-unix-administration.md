---
id: 994
title: 'NIX4NetEng #1 Managing dotfiles; pwn the unspoken pain of UNIX administration'
date: '2014-04-30T20:58:20-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=994'
permalink: /2014/04/30/nix4neteng-1-managing-dotfiles-pwn-the-unspoken-pain-of-unix-administration/
themeblvd_title:
    - 'NIX4NetEng #1 Managing dotfiles; Take control of your environment with git and dotfiles.'
themeblvd_keywords:
    - 'UNIX, SDN, OpenFlow, UNIX, Linux, CentOS, dotfiles, git, repo, security, buraglio, nick buraglio, NIX4NetEng'
themeblvd_noindex:
    - 'true'
themeblvd_description:
    - 'NIX4NetEng #1 Managing dotfiles; own the unspoken pain of UNIX administration.  Use GIT to manage environmental variables stored in dotfles'
dsq_thread_id:
    - '2651737200'
Views:
    - '100'
categories:
    - How-To
    - NIX4NetEng
    - UNIX
---

Many network engineers are also tasked with maintaining systems that provide network services, those things that make the network easier to use such as DNS and DHCP or management systems that perform useful things like monitor the network, collect flow data or bestow access to the equipment by acting as <a href="http://en.wikipedia.org/wiki/Bastion_host" target="_blank" rel="noopener noreferrer">bastion</a> or jump hosts.  In many instances, robust and high availability services run on UNIX, Linux or BSD systems for stability and reliability, so those that manage these systems need to be well versed system admins as well as whatever their other job functions are.  <a href="http://packetpushers.net/are-certifications-tests-still-worth-your-resources-in-the-day-of-hybrid-it/" target="_blank" rel="noopener noreferrer">Hybridization</a>, if you will.  Nothing new, nothing unexpected.  However, one of the banes of these tasks is having a uniform shell environment across platforms and systems. Why create a customized environment with aliases, environmental variables and other personalized settings more than once?
I have struggled with how to do this efficiently across desktop, server, jumphosts and other daily use systems for <strong>years</strong>. Most of the important variables are controlled by dotfiles.   In what I am hoping is the start of a short series of "UNIX stuff for networking folks", I will explain how I did this for myself.
UNIX and Linux admins have been dealing with dotfiles forever. GitHub even has a <a href="http://dotfiles.github.io/" target="_blank" rel="noopener noreferrer">repo dedicated to</a> it.  For my environment, I chose to go with <a href="http://jim.github.io/briefcase/" target="_blank" rel="noopener noreferrer">Briefcase</a> and <a href="http://www.bitbucket.com" target="_blank" rel="noopener noreferrer">BitBucket</a>.  Briefcase because it has mechanisms for stripping out sensitive information if needed and bitbucket because I can have private repos without paying money.  This can all certainly be done with local git repos or github and without briefcase.
Briefcase is really straightforward to install, it's just a ruby gem, so <em>gem install briefcase </em>is all that is needed to get it on your machine<em>. </em> OSX has it by default.  <em> </em>On my machine I needed to to<em> sudo gem update —system </em>before it would install.  Your mileage may vary<em>. </em>
Once it's installed, just add your files.  I switched to bash, so I needed to import .bashrc and .bash_profile, but I wanted to make sure I had a backup just in case.
<pre>mkdir -p tmp/dotfiles
mv .bashrc tmp/dotfiles/
mv .bash_profile tmp/dotfiles/</pre>
<pre>briefcase import ~/.bashrc
briefcase import ~/.bash_profile</pre>
<pre>briefcase git remote add origin git@repo.forwardingplane.net:buraglio/briefcase-dotfiles.git</pre>
<pre>briefcase git commit -am "Initial newhost commit"</pre>
<pre>briefcase git checkout origin master</pre>
Obviously replace the remote repo address with your own repo destination.   You can now check the status:
<pre>briefcase sync</pre>
This should output something like this:
<pre>Synchronizing dotfiles between /Users/buraglio/.dotfiles and /Users/buraglio
Symlink verified: /Users/buraglio/.bash_profile -&gt; /Users/buraglio/.dotfiles/bash_profile
Symlink verified: /Users/buraglio/.bashrc -&gt; /Users/buraglio/.dotfiles/bashrc
Symlink verified: /Users/buraglio/.profile -&gt; /Users/buraglio/.dotfiles/profile
Symlink verified: /Users/buraglio/.README.md -&gt; /Users/buraglio/.dotfiles/README.md</pre>
Getting a new branch for an existing host was the biggest hurdle for me, I want a base .bashrc but may want different environment variables for mac and Linux.  I'm not a git expert by any means, so there may be a better way to do this, but it works well for me. To branch a new host, it's pretty straightforward.  Briefcase is really just a wrapper for git, so prepending "briefcase" before the git commands seems to "just work" (as I learned by trial and error or making this work).
On an existing Host:
<pre>git clone git@your.repoaddress.net:username/reponame.git .dotfiles
mkdir -p tmp/dotfiles
mv .bashrc tmp/dotfiles/
mv .bash_profile tmp/dotfiles/
briefcase sync
briefcase git branch [newhost]
briefcase git checkout [newhost]</pre>
...Make changes...
<pre>briefcase git commit -am "Initial newhost commit"</pre>
briefcase git push origin [newhost]
There you have it, easily backed up and distributed environment control.  I'm planning to add <a href="http://joeyh.name/code/etckeeper/" target="_blank" rel="noopener noreferrer">etckeeper</a> to this process next.
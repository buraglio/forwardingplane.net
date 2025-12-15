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
    - 'NIX4NetEng #1 Managing dotfiles; own the unspoken pain of UNIX administration. Use GIT to manage environmental variables stored in dotfles'
dsq_thread_id:
    - '2651737200'
Views:
    - '100'
categories:
    - How-To
    - NIX4NetEng
    - UNIX
---

Many network engineers are also tasked with maintaining systems that provide network services, those things that make the network easier to use such as DNS and DHCP or management systems that perform useful things like monitor the network, collect flow data or bestow access to the equipment by acting as [bastion](http://en.wikipedia.org/wiki/Bastion_host) or jump hosts.  In many instances, robust and high availability services run on UNIX, Linux or BSD systems for stability and reliability, so those that manage these systems need to be well versed system admins as well as whatever their other job functions are.  [Hybridization](http://packetpushers.net/are-certifications-tests-still-worth-your-resources-in-the-day-of-hybrid-it/), if you will.  Nothing new, nothing unexpected.  However, one of the banes of these tasks is having a uniform shell environment across platforms and systems. Why create a customized environment with aliases, environmental variables and other personalized settings more than once?
I have struggled with how to do this efficiently across desktop, server, jumphosts and other daily use systems for **years**. Most of the important variables are controlled by dotfiles.   In what I am hoping is the start of a short series of "UNIX stuff for networking folks", I will explain how I did this for myself.
UNIX and Linux admins have been dealing with dotfiles forever. GitHub even has a [repo dedicated to](http://dotfiles.github.io/) it.  For my environment, I chose to go with [Briefcase](http://jim.github.io/briefcase/) and [BitBucket](http://www.bitbucket.com).  Briefcase because it has mechanisms for stripping out sensitive information if needed and bitbucket because I can have private repos without paying money.  This can all certainly be done with local git repos or github and without briefcase.
Briefcase is really straightforward to install, it's just a ruby gem, so *gem install briefcase *is all that is needed to get it on your machine*. * OSX has it by default.  * *On my machine I needed to to* sudo gem update —system *before it would install.  Your mileage may vary*. *
Once it's installed, just add your files.  I switched to bash, so I needed to import .bashrc and .bash_profile, but I wanted to make sure I had a backup just in case.

```
mkdir -p tmp/dotfiles
mv .bashrc tmp/dotfiles/
mv .bash_profile tmp/dotfiles/
```


```
briefcase import ~/.bashrc
briefcase import ~/.bash_profile
```


```
briefcase git remote add origin git@repo.forwardingplane.net:buraglio/briefcase-dotfiles.git
```


```
briefcase git commit -am "Initial newhost commit"
```


```
briefcase git checkout origin master
```

Obviously replace the remote repo address with your own repo destination.   You can now check the status:

```
briefcase sync
```

This should output something like this:

```
Synchronizing dotfiles between /Users/buraglio/.dotfiles and /Users/buraglio
Symlink verified: /Users/buraglio/.bash_profile -> /Users/buraglio/.dotfiles/bash_profile
Symlink verified: /Users/buraglio/.bashrc -> /Users/buraglio/.dotfiles/bashrc
Symlink verified: /Users/buraglio/.profile -> /Users/buraglio/.dotfiles/profile
Symlink verified: /Users/buraglio/.README.md -> /Users/buraglio/.dotfiles/README.md
```

Getting a new branch for an existing host was the biggest hurdle for me, I want a base .bashrc but may want different environment variables for mac and Linux.  I'm not a git expert by any means, so there may be a better way to do this, but it works well for me. To branch a new host, it's pretty straightforward.  Briefcase is really just a wrapper for git, so prepending "briefcase" before the git commands seems to "just work" (as I learned by trial and error or making this work).
On an existing Host:

```
git clone git@your.repoaddress.net:username/reponame.git .dotfiles
mkdir -p tmp/dotfiles
mv .bashrc tmp/dotfiles/
mv .bash_profile tmp/dotfiles/
briefcase sync
briefcase git branch [newhost]
briefcase git checkout [newhost]
```

...Make changes...

```
briefcase git commit -am "Initial newhost commit"
```

briefcase git push origin [newhost]
There you have it, easily backed up and distributed environment control.  I'm planning to add [etckeeper](http://joeyh.name/code/etckeeper/) to this process next.
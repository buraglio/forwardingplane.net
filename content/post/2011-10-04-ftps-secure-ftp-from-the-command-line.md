---
id: 28
title: 'ftps (secure ftp) from the command line'
date: '2011-10-04T04:31:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/'
permalink: /2011/10/04/ftps-secure-ftp-from-the-command-line/
dsq_thread_id:
    - '3630858643'
Views:
    - '1450'
categories:
    - Security
    - UNIX
---

I have recently enabled[ Duo Security](http://www.duosecurity.com/) for many of my personal services, and I can't recommend them enough. Personal [two factor authentication](http://en.wikipedia.org/wiki/Two-factor_authentication) is very useful and really powerful. It works on my iPhone and I have yet to run into any real issues....except for one. I can't use automation to scp or sftp anything anymore and keep my two factor auth working in a way I'm comfortable with.


Enter [ftps](http://en.wikipedia.org/wiki/Ftps). FTP is a terrible, yet immensely useful protocol. I chose to use [vsftp](https://security.appspot.com/vsftpd.html) under debian Linux with Implicit TLS/SSL, meaning there is no negotiation of protocol as with explicit ftps (or ftpes). It's secure, or none.


Configuring this is pretty easy, but it does require some editing of the /etc/vsftpd.conf file. I added some stuff to make it do ftpes as such:


*ssl_enable=YES

allow_anon_ssl=NO

force_local_data_ssl=YES

force_local_logins_ssl=YES

rsa_cert_file=/etc/ssl/certs/vsftpd.pem

*


This and a few other tweaks that aren't relevant here, make ftpes work on my machine.


Now, clients are another story. Most of the modern GUI based clients work. I know [filezilla](http://filezilla-project.org/) works, and it's free. The problem I have, is that I need to do this programmatically, via a script.


A bit of digging didn't yield much, however, I did come across [lftp](http://lftp.yar.ru/). lftp is an extremely powerful command line ftp client that has a LOT of features, one of which is ftpes support. Now, the one problem with lftp is that it is extremely full featured. Like, overly featured. So much so, that it can be a bit daunting to make it do what you want, which in my case was pretty simple.


I wrote a simple script to make it do what I wanted, which was just to upload a file and move it around.


*

#!/bin/sh

**/usr/bin/lftp -u user,password remote.host.com ****<
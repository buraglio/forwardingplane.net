---
id: 28
title: 'ftps (secure ftp) from the command line'
date: '2011-10-04T04:31:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/'
permalink: /2011/10/04/ftps-secure-ftp-from-the-command-line/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2011/10/ftps-secure-ftp-from-command-line.html
dsq_thread_id:
    - '3630858643'
Views:
    - '1450'
categories:
    - Security
    - UNIX
---

I have recently enabled<a href="http://www.duosecurity.com/"> Duo Security</a> for many of my personal services, and I can't recommend them enough.   Personal <a href="http://en.wikipedia.org/wiki/Two-factor_authentication">two factor authentication</a> is very useful and really powerful.  It works on my iPhone and I have yet to run into any real issues....except for one.  I can't use automation to scp or sftp anything anymore and keep my two factor auth working in a way I'm comfortable with.
<br />
<br />Enter <a href="http://en.wikipedia.org/wiki/Ftps">ftps</a>.  FTP is a terrible, yet immensely useful protocol.  I chose to use <a href="https://security.appspot.com/vsftpd.html">vsftp</a> under debian Linux with Implicit TLS/SSL, meaning there is no negotiation of protocol as with explicit ftps (or ftpes).  It's secure, or none.
<br />
<br />Configuring this is pretty easy, but it does require some editing of the /etc/vsftpd.conf file.  I added some stuff to make it do ftpes as such:
<br />
<br /><i>ssl_enable=YES
<br />allow_anon_ssl=NO
<br />force_local_data_ssl=YES
<br />force_local_logins_ssl=YES
<br />rsa_cert_file=/etc/ssl/certs/vsftpd.pem
<br /></i>
<br />
<br />
<br />This and a few other tweaks that aren't relevant here, make ftpes work on my machine.
<br />
<br />Now, clients are another story.  Most of the modern GUI based clients work.  I know <a href="http://filezilla-project.org/">filezilla</a> works, and it's free.  The problem I have, is that I need to do this programmatically, via a script.
<br />
<br />A bit of digging didn't yield much, however, I did come across <a href="http://lftp.yar.ru/">lftp</a>.    lftp is an extremely powerful command line ftp client that has a LOT of features, one of which is ftpes support.  Now, the one problem with lftp is that it is extremely full featured.  Like, overly featured.  So much so, that it can be a bit daunting to make it do what you want, which in my case was pretty simple.
<br />
<br />I wrote a simple script to make it do what I wanted, which was just to upload a file and move it around.
<br />
<br /><i>
<br />#!/bin/sh
<br /></i><i>/usr/bin/lftp -u user,password remote.host.com </i><i><eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i=""></eof></i><div style="display: inline !important; "><i><<eof<eof<eof<eof< div=""></eof<eof<eof<eof<></i><i><eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i=""><div>cd data</div><div>lcd /mnt/NAS/files/updates</div><div>put updates.txt</div><div>mv updates.txt data.txt</div><div>quit 0</div><div>EOF</div><div>
<br /></div></eof></i><div><eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i="">This works fine, and since I'm using ftpes, it does all of the negotiation for me.
<br />
<br /></eof><div></div><div><i><eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i="">
<br /></eof></i></div></div></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
---
title: 'ftps (secure ftp) from the command line'
date: Tue, 04 Oct 2011 04:31:00 +0000
draft: false
tags: [Security, UNIX]
---

I have recently enabled [Duo Security](http://www.duosecurity.com/) for many of my personal services, and I can't recommend them enough. Personal [two factor authentication](http://en.wikipedia.org/wiki/Two-factor_authentication) is very useful and really powerful. It works on my iPhone and I have yet to run into any real issues....except for one. I can't use automation to scp or sftp anything anymore and keep my two factor auth working in a way I'm comfortable with.  
  
Enter [ftps](http://en.wikipedia.org/wiki/Ftps). FTP is a terrible, yet immensely useful protocol. I chose to use [vsftp](https://security.appspot.com/vsftpd.html) under debian Linux with Implicit TLS/SSL, meaning there is no negotiation of protocol as with explicit ftps (or ftpes). It's secure, or none.  
  
Configuring this is pretty easy, but it does require some editing of the /etc/vsftpd.conf file. I added some stuff to make it do ftpes as such:  
  
_ssl\_enable=YES  
allow\_anon\_ssl=NO  
force\_local\_data\_ssl=YES  
force\_local\_logins\_ssl=YES  
rsa\_cert\_file=/etc/ssl/certs/vsftpd.pem  
_  
  
  
This and a few other tweaks that aren't relevant here, make ftpes work on my machine.  
  
Now, clients are another story. Most of the modern GUI based clients work. I know [filezilla](http://filezilla-project.org/) works, and it's free. The problem I have, is that I need to do this programmatically, via a script.  
  
A bit of digging didn't yield much, however, I did come across [lftp](http://lftp.yar.ru/). lftp is an extremely powerful command line ftp client that has a LOT of features, one of which is ftpes support. Now, the one problem with lftp is that it is extremely full featured. Like, overly featured. So much so, that it can be a bit daunting to make it do what you want, which in my case was pretty simple.  
  
I wrote a simple script to make it do what I wanted, which was just to upload a file and move it around.  
  
_  
#!/bin/sh  
__/usr/bin/lftp -u user,password remote.host.com_

_<__

cd data

lcd /mnt/NAS/files/updates

put updates.txt

mv updates.txt data.txt

quit 0

EOF

  


_

This works fine, and since I'm using ftpes, it does all of the negotiation for me.  
  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
---
id: 170
title: 'CentOS sshguard install for limiting ssh scans'
date: '2012-12-15T21:18:27-06:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=170'
permalink: /2012/12/15/centos-sshguard-install-for-limiting-ssh-scans/
themeblvd_noindex:
    - 'true'
themeblvd_description:
    - ''
themeblvd_title:
    - ''
themeblvd_keywords:
    - ''
Views:
    - '748'
categories:
    - 'Lab Time'
    - Musings
    - UNIX
---

Securing SSH is a form or art.  It's often debated, much like blocking all ICMP packets (which I normally disagree with).  If you need good proof, read <a href="http://lonesysadmin.net/2012/11/20/changing-sshd-port-numbers-continues-to-be-a-bad-idea/">these</a> <a href="http://lonesysadmin.net/2012/10/19/on-using-alternate-ports-for-ssh/">posts</a> by <a href="https://twitter.com/plankers">Bob Plankers</a>.  There is a camp that likes to promote moving to a non-standard port.  There is a faction that likes to block it completely except from a handful of hosts.  Then there are those that like to leave it open all together.  Running naked in the digital jungle.
I tend to err on the side of blocking except for jump hosts.  This is a pretty time proven methodology.  However, what about the hosts that <strong>need</strong> to be open? A hardened jump host or public shell box comes to mind.
Enter <a href="http://www.sshguard.net">sshguard</a>.
SSH Guard is an amazing little piece of software that takes the heavy lifting out of blocking all of those scans and automates removal of blocks.  It works across a myriad of popular unix platforms.
From <a href="http://www.sshguard.net">http://www.sshguard.net</a>:
<em>Sshguard monitors servers from their logging activity. When logs convey that someone is doing a Bad Thing, sshguard reacts by blocking he/she/it for a bit. Sshguard has a touchy personality: when a naughty tyke insists disturbing your host, it reacts firmer and firmer.</em>
<em>Sshguard supports many services out of the box, recognizes severallog formats, and can operate many firewall systems. Many users appreciate its ease of use, compatibility and feature richness.</em>
I like it because they have not left out some of the less common distros, but sinceI've mostly converted over to CentOS, this focus is how to set it up on Centos 6.3.   We'll assume you have epel repo and rpmforge repo installed.
I prefer <a href="http://www.balabit.com/network-security/syslog-ng">syslog-ng</a> so lets install that.
<pre>sudo yum -y install syslog-ng</pre>
<pre>chkconfig syslog-ng on</pre>
<pre>chkconfig rsyslog off</pre>
This isn't necessary, but I'd recommend it.
Next, I lke to disable selinux.  It's on be default in CentOS and I really don't need what it offers.  I find it annoying and far too restrictive and this won't build correctly without it disabled in my experience.
<pre>sudo vi /etc/selinux/config</pre>
Change the line that reads
<pre><code>SELINUX=enabled</code></pre>
to
<pre><code>SELINUX=disabled</code></pre>
You'll need to reboot to make this take effect. Note that this will disable selinux completely and permanently.  <a href="http://www.revsys.com/writings/quicktips/turn-off-selinux.html">There are ways to temporarily disable it</a> if you would prefer.
<pre>sudo reboot</pre>
Download sshguard.  I didn't find it in any repos for Centos 6.x.  I may be mistaken, but I went this route.
<pre>wget http://sourceforge.net/projects/sshguard/files/sshguard/sshguard-1.5/sshguard-1.5.tar.bz2/download</pre>
Unpack it.
<pre>bunzip2 sshguard-1.5.tar.bz2</pre>
<pre>tar -xvf sshguard-1.5.tar</pre>
<pre>cd sshguard-1.5</pre>
I like to do minimal installs of Linux, so I need to add gcc before I can compile.  This will likely install some dependancies if it's a new minimal install.  Same goes for make
<pre>sudo yum install gcc make</pre>
<pre>sudo ./configure --with-firewall=iptables</pre>
<pre>sudo make &amp;&amp; sudo make install</pre>
OK, you should have it installed at this point.  You can verify by doing:
<pre>ls -la /usr/local/sbin/sshguard</pre>
which should yield something like this:
<pre>-rwxr-xr-x 1 root root 399995 Dec 16 02:28 /usr/local/sbin/sshguard</pre>
<pre></pre>
Great, now we need to create firewall tables for sshguard for IPv4, and if you're keeping up to date, IPv6.
<pre>sudo iptables -N sshguard</pre>
<pre>sudo ip6tables -N sshguard</pre>
Now tell iptables to drop that traffic. Make sure you don't have a permit ssh rule above this line or it won't work.
<pre>sudo iptables -A INPUT -j sshguard</pre>
<pre>sudo ip6tables -A INPUT -j sshguard</pre>
<pre></pre>
Save your config.  
<pre>sudo iptables-save &lt; /etc/sysconfig/iptables</pre>
<pre>sudo ip6tables-save &lt; /etc/sysconfig/ip6tables</pre>
For the examples below, we'll just look at IPv4 to keep the post a bit shorter, but the v6 pieces are all identical save for the file names.  If you're running v6 you should remember to secure it just as you would v4.
Mine ruleset is pretty vanilla, mostly stock with the exception of ssl and dns.
<pre># Completed on Sat Dec 15 21:02:09 2012
# Generated by iptables-save v1.4.7 on Sat Dec 15 21:02:09 2012
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [6585:1425605]
:sshguard - [0:0]
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -j sshguard
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
-A INPUT -p udp -m state --state NEW -m udp --dport 53 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 53 -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT
# Completed on Sat Dec 15 21:02:09 2012</pre>
Note: I did have to relocate the sshguard rule to right below the first INPUT rule to make it actually effective.
<pre></pre>
Now we need to activate it.  This is pretty straightforward.  We essentially need to tell syslog to call sshguard based on activity and it's why I prefer syslog-ng.  It's very flexible and easy to add this stuff right in.  I've been using it for over a decade and it the most flexible syslog server I've found.  
<pre>vi /etc/syslog-ng/syslog-ng.conf</pre>
Based on the <a href="http://www.sshguard.net/docs/setup/getlogs/syslog-ng/">instructions at the sshguard site</a> (which also have details for extending this to more than just ssh; I'll do a post on that for CentOS at some point too), just add the following to the bottom of your syslog-ng.conf file:
<pre># pass only entries with auth+authpriv facilities from programs other than sshguard
filter f_sshguard { facility(auth, authpriv) and not program("sshguard"); };
# pass entries built with this format
destination sshguard {
 program("/usr/local/sbin/sshguard"
 template("$DATE $FULLHOST $MSGHDR$MESSAGE\n")
 );
};
log { source(s_sys); filter(f_sshguard); destination(sshguard); };</pre>
Then restart syslog-ng
<pre>sudo service syslog-ng stop</pre>
<pre>sudo service syslog-ng start</pre>
<div>You'll probably see these errors, they can be ignored if you're not using the afsql module.</div>
<div></div>
<pre>Plugin module not found in 'module-path'; module-path='/lib64/syslog-ng', module='afsql'</pre>
<pre>Starting syslog-ng: Plugin module not found in 'module-path'; module-path='/lib64/syslog-ng', module='afsql'</pre>
ssh into localhost or in from an outside host. This will create a log and cause syslog-ng to call sshguard. At that point you should see this when looking for sshguard:
<pre>ps auxww | grep sshguard</pre>
<pre>root 14010 0.0 0.0 16924 1260 ? Sl 20:49 0:00 /usr/local/sbin/sshguard</pre>
You should see it in your iptables rules:
<pre>[buraglio@centos63 sysconfig]# sudo iptables -L
Chain INPUT (policy ACCEPT)
target prot opt source destination
ACCEPT all -- anywhere anywhere state RELATED,ESTABLISHED
sshguard all -- anywhere anywhere
ACCEPT icmp -- anywhere anywhere
ACCEPT all -- anywhere anywhere
ACCEPT tcp -- anywhere anywhere state NEW tcp dpt:ssh
ACCEPT tcp -- anywhere anywhere state NEW tcp dpt:https
ACCEPT udp -- anywhere anywhere state NEW udp dpt:domain
ACCEPT tcp -- anywhere anywhere state NEW tcp dpt:domain
ACCEPT tcp -- anywhere anywhere state NEW tcp dpt:ndmp
ACCEPT tcp -- anywhere anywhere state NEW tcp dpt:dnp
REJECT all -- anywhere anywhere reject-with icmp-host-prohibited</pre>
<pre>Chain FORWARD (policy ACCEPT)
target prot opt source destination
REJECT all -- anywhere anywhere reject-with icmp-host-prohibited</pre>
<pre>Chain OUTPUT (policy ACCEPT)
target prot opt source destination</pre>
<pre>Chain sshguard (1 references)
target prot opt source destination</pre>
That's pretty much it. Let it sit and wait. It will block scanners automagically and then unblock them after a period of time.
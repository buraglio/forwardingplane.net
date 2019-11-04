---
title: 'Install nfsen and nfdump on CentOS 6.5 for netflow and or sflow collection'
date: Sat, 11 Jan 2014 21:55:24 +0000
draft: false
tags: [How-To, IPv6, Lab Time, Security, UNIX]
---

I am an absolutely **huge** fan of statistical and instrumentation data, especially when it comes to traffic analysis, visualization and baselining.  I've rambled on about the importance of it at [every opportunity](http://searchnetworking.techtarget.com/news/2240212051/The-Der-Spiegel-NSA-revelations-What-network-engineers-need-to-know).  As a result of that, I have been doing work with netflow and netflow-like data for a fairly long time.  My first collector was the [OSU Flow tools](http://www.splintered.net/sw/flow-tools/) based stuff  back around 13 years ago.  From there I played with all kinds of netflow tools, both [commercial](http://www.arbornetworks.com/) and open source, finally settling most of my focus on [nfdump](http://nfdump.sourceforge.net/) and [nfsen](http://nfsen.sourceforge.net/). A bit of history: nfdump was born out of a research network, requiring it to be able to consume huge amounts of flows efficiently.  This makes it very powerful and very useful for nearly anyone, from the small technology tinkerer to to the enterprise network engineer up through the service provider architect.  nfsen is really just a php wrapper for nfdump, however, the really nice thing about it (other then being free, opensource software) is that it is extendable via [plugins](http://sourceforge.net/apps/trac/nfsen-plugins/).  This is really what makes it a serious player from all angles.     From botnet detection to displaying IP geo-data on a map, there is likely a plugin for it.  Not finding what you are looking for?  Write it!  The architecture to use it is already there and documented. For ease of install, I chose CentOS 6.5.  Once you have a system up and running, to get nfsen/nfdump working, here is what you need to do:

```yum install -y httpd php wget gcc make rrdtool-devel \\
rrdtool-perl perl-MailTools perl-Socket6 flex byacc
```
```
vi /etc/selinux/config
set SELINUX=disabled
reboot
```

You'll need to make an iptables rule (I generally make one for ip6tables as well, in case I want to also enable ipv6 transport)

```
sudo iptables -I INPUT -p udp -m state --state NEW -m udp --dport 9995 -j ACCEPT
sudo ipt6ables -I INPUT -p udp -m state --state NEW -m udp --dport 9995 -j ACCEPT
```

Also allow for access to the web server you just installed.

```sudo ip6tables -I INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
sudo ip6tables -I INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT  
sudo iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
sudo iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT  
service iptables save
service ip6tables save
```

Once you enable https you can safely remove the table rules for port 80. Start HTTPd

```sudo service httpd start
```
Enable HTTPd at boot
```chkconfig httpd on
```
Now you need the actual code. I like to grab the latest from sourceforge. (nfdump-1.6.11 and nfsen-1.3.6p1 at the time of this writing)
```wget http://downloads.sourceforge.net/project/nfdump/stable/nfdump-1.6.11/nfdump-1.6.11.tar.gz```
```wget http://downloads.sourceforge.net/project/nfsen/stable/nfsen-1.3.6p1/nfsen-1.3.6p1.tar.gz```

```tar -zxvf nfdump-1.6.11.tar.gz
./configure --enable-nfprofile --enable-nftrack --enable-sflow
make && sudo make install
```
By default 1.6.11 enables v9 and ipfix =)
```adduser netflow
```
```vi /etc/group
```
Add user netflow to group apache
```vi etc/nfsen.conf
```
change www user to apache Add your host to the file to allow for collection, my %sources looks like this:
```%sources = (
    'home'    => { 'port' => '9995', 'col' => '#0000ff', 'type' => 'netflow' },
    'internal'    => { 'port' => '9996', 'col' => '#FF0000', 'type' => 'netflow' },
);
```
As you can see, I have two valid sources with different ports and different colors. You can make all netflow, all sflow, or any combination of protocol. change directory to /home/netflow
```./install.pl etc/nfsen.conf
cd /home/netflow/bin/
./nfsen start
```
Make it start at boot (referenced from [this post](http://sourceforge.net/mailarchive/message.php?msg_id=29434166)).
```vi /etc/init.d/nfsen
```
Add this into the file:
```#!/bin/bash
#
# chkconfig: - 50 50
# description: nfsen

DAEMON=/home/netflow/bin/nfsen

case "$1" in
		start)
		$DAEMON start
		;;
		stop)
		$DAEMON stop
		;;
		status)
		$DAEMON status
		;;
		restart)
		$DAEMON stop
		sleep 1
		$DAEMON start
		;;
		\*)
		echo "Usage: $0 {start|stop|status|restart}"
		exit 1
		;;
esac

exit 0
```
Then chkconfig it on to start it at boot:
```chmod 755 nfsen && chkconfig --add nfsen && chkconfig nfsen on
```

That's pretty much it. Once you configure your netflow or sflow source, you should start seeing data in ~5-10 minutes. Point your browser at your web server and see: Mine is set as https://netmon/nfsen/nfsen.php (you'll need to include the "nfsen.php" uness you edit your apache config to recognize "nfsen.php" as in index.

[![Screen Shot 2014-01-11 at 3.13.53 PM](http://www.forwardingplane.net/wp-content/uploads/2014/01/Screen-Shot-2014-01-11-at-3.13.53-PM-913x1024.png)](http://www.forwardingplane.net/wp-content/uploads/2014/01/Screen-Shot-2014-01-11-at-3.13.53-PM.png)

Common issues: I see this one every time: "ERROR: nfsend connect() error: Permission denied!" It's always a permissions issue, as documented [here](https://code.google.com/p/nfsenplugins/wiki/NFSEN_Installation_Gotchas).  You need to make sure that the nfsen package can read the nfsen.comm socket file. I fixed mine by doing
```chmod g+rwx ~netflow/
```
My nfsen.conf file is using /home/netflow as the $BASEDIR.
 [![Screenshot 2014-01-11 13.04.17](http://www.forwardingplane.net/wp-content/uploads/2014/01/Screenshot-2014-01-11-13.04.17.png)](http://www.forwardingplane.net/wp-content/uploads/2014/01/Screenshot-2014-01-11-13.04.17.png)
You'll likely see "Frontend - Backend version mismatch!", this is a known issue. There is a patch to fix it [here](http://sourceforge.net/p/nfsen/bugs/43/), I never bothered since it did not cause any issues for me. Disk full. Depending on your setup, you may generate a firehose worth of data. I have filled disks in less than a day in the past on a good sized regional WAN. I generally keep a month of data, but you can store as much data as disk you want to buy. I have a script run from cron to prune data, if you want to do the same:
```vi /usr/local/etc/rmflowdata.sh
```
Paste this in:
```#!/bin/bash
# prune flow data
# Usage:
# +30 is the number of days, adjust accordingly.

/bin/find /home/netflow/profiles-data/live -name "nfcapd.\*" -type f -mtime +30 -delete
```

Add this to your crontab:
```@daily /usr/local/bin/rmflowdata.sh
```
Make it executable
```chmod 755 /usr/local/bin/rmflowdata.sh
```
There are probably more elegant ways to do it but this works just fine, is lightweight and can be run manually if needed. There are a lot of great use cases for this.  If you're looking for an SDN tie-in, guess what, there is one.  [OpenVSwitch supports sflow export](http://blog.sflow.com/2010/05/configuring-open-vswitch.html) and low-and-behold, nfsen and nfdump can easily consume and display sflow data. Want flow statistics on your all VM, OVS based SDN lab?  Guess what, you can! There are some other great things you can do with flow data, too, specifically sflow.  It's not just for network statistics, there is a host [based sflow implementation](http://host-sflow.sourceforge.net/) that track any number of interesting metrics.  [blog.sflow.com](http://blog.sflow.com/) is a great resource for all things sflow (also, it does IPv6 by default, as it should). Ok, now you have **absolutely** no good reason not to be collecting flow data.   It's easy, it's useful and almost everything (hosts, routers, virtual switches) supports exporting **_some_** kind of flow information.  You can even generate it from an inline linux box or a box off of an optical tap or a span port running [softflowd](https://code.google.com/p/softflowd/) or [nprobe](http://www.ntop.org/products/nprobe/).   Both of which I can confirm work wonderfully (the above collector is gathering flows from softflowd running on my [security onion box](http://www.forwardingplane.net/2013/07/building-a-secured-network-in-a-box/ "Building a secured network in a box") as well as exported flows from pfflowd on a [pfsense](http://www.pfsense.org/) router).

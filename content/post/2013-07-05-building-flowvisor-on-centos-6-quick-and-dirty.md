---
id: 714
title: 'Building FlowVisor on Centos 6 – quick and dirty'
date: '2013-07-05T04:22:23-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=714'
permalink: /2013/07/05/building-flowvisor-on-centos-6-quick-and-dirty/
themeblvd_title:
    - 'OpenFlow Flowvisor controller under CentOS'
themeblvd_keywords:
    - 'FlowVisor, CentOS, Linux, OpenFlow, Floodlight, Controller'
themeblvd_description:
    - 'Quick and dirty reference to build a Flowvisor instance under CentOS'
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3628037376'
Views:
    - '321'
categories:
    - How-To
    - 'Lab Time'
    - OpenFlow
    - UNIX
---

I had the need to build a FlowVisor instance under CentOS.  Since nearly all of the docs I could find were for debian, I threw this together.  I utilized this [GENI doc](http://groups.geni.net/geni/wiki/FlowVisor) and the [github docs](https://github.com/OPENNETWORKINGLAB/flowvisor/wiki/Installation-from-Source) as a simple reference.  This is the quick and dirty method I used:
Install the prerequisites:

```
sudo yum -y install ant eclipse java-1.6.0-openjdk.x86_64 git
sudo yum -y groupinstall "Development Tools"
```

Create my standard directories:

```
mkdir /services
cd /services
git clone git://github.com/OPENNETWORKINGLAB/flowvisor.git
```

Navigate, add user and install

```
cd flowvisor
adduser flowvisor
sudo make fvuser=flowvisor fvgroup=flowvisor install
```

Here is the relativde output I saw:

```
[root@collector flowvisor]# sudo make fvuser=flowvisor fvgroup=flowvisor install
ant
Buildfile: build.xml
init:
[mkdir] Created dir: /services/flowvisor/build
[mkdir] Created dir: /services/flowvisor/build.tests
compile:
[javac] Compiling 239 source files to /services/flowvisor/build
[javac] Note: /services/flowvisor/src/org/flowvisor/config/LoadConfig.java uses or overrides a deprecated API.
[javac] Note: Recompile with -Xlint:deprecation for details.
dist:
[mkdir] Created dir: /services/flowvisor/dist
[jar] Building jar: /services/flowvisor/dist/flowvisor.jar
[jar] Building jar: /services/flowvisor/dist/flowvisor.jar
BUILD SUCCESSFUL
Total time: 3 seconds
./scripts/install-script.sh
Using source dir: ./scripts/..
Installation prefix (/usr/local):
Install to different root directory ()
Installing FlowVisor into /usr/local with prefix=/usr/local as user/group flowvisor:flowvisor
Updating fvctl-xml.sh to fvctl-xml
Updating fvconfig.sh to fvconfig
Updating flowvisor.sh to flowvisor
Updating envs.sh to envs
Creating directories
Creating /usr/local/bin
Creating /usr/local/sbin
Creating /usr/local/libexec/flowvisor
Creating /usr/local/share/man/man1
Creating /usr/local/share/man/man8
Creating /usr/local/share/doc/flowvisor
Creating /usr/local/share/db/flowvisor
Creating /etc/flowvisor (owned by user=flowvisor  group=flowvisor)
Installing scripts
Installing SYSV startup script (not enabled by default)
Installing jars
Installing flowvisor.jar
Installing manpages
Installing FlowVisorDB
Installing configs
Installing Logrotate config
Installing documentation
Linking fvctl to fvctl-json
ln: creating symbolic link `fvctl': File exists
Generating a default config FlowVisor config
Trying to generate SSL Server Key with passwd from scripts/envs.sh
Generating cert with common name == flowvisor
keytool error: java.lang.Exception: Key pair not generated, alias <mykey> already exists
Enter password for account 'fvadmin' on the flowvisor:
Generating default config in db
Outputing config file /etc/flowvisor/config.json
```

Start the controller:

```
sudo /etc/init.d/flowvisor start
```

Output from controller starting:

```
Starting flowvisor with the configuration stored in DB
If DB unpopulated, load config using 'fvconfig load config.json'
[root@collector flowvisor]#
Message from syslogd@collector at Jul  3 08:49:51 ...
1>Jul  3 08:49:51 flowvisor: ERROR none : log level enabled: CRIT
Message from syslogd@collector at Jul  3 08:49:51 ...
1>Jul  3 08:49:51 flowvisor: ERROR none : log level enabled: ALERT
Message from syslogd@collector at Jul  3 08:49:51 ...
1>Jul  3 08:49:51 flowvisor: WARN none : log level enabled: WARN
```


```
This yields a "working" flow visor.
Lock it down with a password:
```


```
yum -y install pwgen
test -f /etc/flowvisor.passwd || sudo sh -c 'pwgen -sB 24 > /etc/flowvisor.passwd'
service flowvisor restart
```

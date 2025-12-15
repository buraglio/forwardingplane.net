---
id: 762
title: 'Fixing the dreaded "error: could not open configuration database (juniper.data+)" problem.'
date: '2013-08-07T10:52:04-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=762'
permalink: /2013/08/07/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/
themeblvd_title:
    - 'Fixing the dreaded "error: could not open configuration database (juniper.data+)" problem.'
themeblvd_keywords:
    - 'JunOS, error: could not open configuration database (juniper.data+), buraglio, Juniper, routing, UNIX, fsck, MX480, MX240, EX4200, MX960, Nick Buraglio'
themeblvd_description:
    - 'How to fix an inconsistent file system problem in JunOS that manifests itself as the error "error: could not open configuration database (juniper.data+)". '
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '3627600493'
Views:
    - '6922'
categories:
    - 'Lab Time'
    - Routing
    - UNIX
---

Working on some MX series routers recently I encountered a problem I'd never seen before, essentially preventing the configuration from being committed:

```
buraglio@rtr# commit check
re0:
error: could not open configuration database (juniper.data+)
```

This is a very annoying problem and is terribly inconvenient as you can probably imagine. So, my first instinct is to drop down to the shell and starting hacking at it UNIX style.

```
buraglio@rtr>start shell
```

From there I wanted to see the file system and check out the stats of what it thinks we have.

```
buraglio@rtr% df -h
Filesystem     Size    Used   Avail Capacity  Mounted on
/dev/ad0s1a    3.5G    313M    2.9G    10%    /
devfs          1.0K    1.0K      0B   100%    /dev
/dev/md0        63M     63M      0B   100%    /packages/mnt/jbase
/dev/md1        53M     53M      0B   100%    /packages/mnt/jkernel64-12.3R3.4
buraglio@rtr%    82M     82M      0B   100%    /packages/mnt/jpfe-X960-12.3R3.4
/dev/md3       5.0M    5.0M      0B   100%    /packages/mnt/jdocs-12.3R3.4
buraglio@rtr%   104M    104M      0B   100%    /packages/mnt/jroute-12.3R3.4
buraglio@rtr% clearM     28M      0B   100%    /packages/mnt/jcrypto64-12.3R3.4
/dev/md6        38M     38M      0B   100%    /packages/mnt/jpfe-common-12.3R3.4
/dev/md7        92K     92K      0B   100%    /packages/mnt/jplatform-12.3R3.4
/dev/md8       422M    422M      0B   100%    /packages/mnt/jruntime-12.3R3.4
/dev/md9       7.9G     16K    7.2G     0%    /tmp
/dev/md10      7.9G     11M    7.2G     0%    /mfs
/dev/ad0s1e    393M     36K    362M     0%    /config
procfs         4.0K    4.0K      0B   100%    /proc
/dev/ad1s1f     18G    4.2G     12G    26%    /var
```

... and check the mounted partitions.

```
buraglio@rtr% mount
/dev/ad0s1a on / (ufs, local, noatime)
devfs on /dev (devfs, local, multilabel)
/dev/md0 on /packages/mnt/jbase (cd9660, local, noatime, read-only, verified)
/dev/md1 on /packages/mnt/jkernel64-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md2 on /packages/mnt/jpfe-X960-12.3R3.4 (cd9660, local, noatime, read-only)
/dev/md3 on /packages/mnt/jdocs-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md4 on /packages/mnt/jroute-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md5 on /packages/mnt/jcrypto64-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md6 on /packages/mnt/jpfe-common-12.3R3.4 (cd9660, local, noatime, read-only)
/dev/md7 on /packages/mnt/jplatform-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md8 on /packages/mnt/jruntime-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md9 on /tmp (ufs, asynchronous, local, noatime)
/dev/md10 on /mfs (ufs, asynchronous, local, noatime)
/dev/ad0s1e on /config (ufs, local, noatime)
procfs on /proc (procfs, local, noatime)
/dev/ad1s1f on /var (ufs, local, noatime)
```

I ran a fsck to get some stats and see what the problem could be since it appears that there is no free space even though the router reports that it has it.

```
buraglio@rtr% fsck -y -f /dev/ad1s1f
** /dev/ad1s1f (NO WRITE)
** Last Mounted on /var
** Phase 1 - Check Blocks and Sizes
** Phase 2 - Check Pathnames
** Phase 3 - Check Connectivity
** Phase 4 - Check Reference Counts
** Phase 5 - Check Cyl groups
FREE BLK COUNT(S) WRONG IN SUPERBLK
SALVAGE? no
605 files, 2202492 used, 7040218 free (786 frags, 879929 blocks, 0.0% fragmentation)
```

Playing around in the shell presented this error as well

```
/var: create/symlink failed, no inodes free
```

So, it appears as if the /var partition is the issue. On my router /var is mounted as /dev/ad1s1f, so lets unmount this partition and try to fix it. In my experience Juniper will shy away from telling you to do anything in the shell, so do this at your own risk. Rebooting the router would also fix this issue, but I'm a form believer that rebooting networking equipment to fix issues is a lazy way to fix problems and will only serve to atrophy any troubleshooting skills you may have.

```

buraglio@rtr% umount -f /var
```

Now run fsck again to repair the file system

```
buraglio@rtr% fsck -y -f /dev/ad1s1f
** /dev/ad1s1f
** Last Mounted on /var
** Phase 1 - Check Blocks and Sizes
** Phase 2 - Check Pathnames
** Phase 3 - Check Connectivity
** Phase 4 - Check Reference Counts
** Phase 5 - Check Cyl groups
FREE BLK COUNT(S) WRONG IN SUPERBLK
SALVAGE? yes
605 files, 2203376 used, 7039334 free (782 frags, 879819 blocks, 0.0% fragmentation)
***** FILE SYSTEM WAS MODIFIED *****
```

Now that the problematic bits have been repaired, we re-mount the partition

```
buraglio@rtr% mount /dev/ad1s1f /var/
```

Verify the mount

```
buraglio@rtr% mount
/dev/ad0s1a on / (ufs, local, noatime)
devfs on /dev (devfs, local, multilabel)
/dev/md0 on /packages/mnt/jbase (cd9660, local, noatime, read-only, verified)
/dev/md1 on /packages/mnt/jkernel64-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md2 on /packages/mnt/jpfe-X960-12.3R3.4 (cd9660, local, noatime, read-only)
/dev/md3 on /packages/mnt/jdocs-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md4 on /packages/mnt/jroute-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md5 on /packages/mnt/jcrypto64-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md6 on /packages/mnt/jpfe-common-12.3R3.4 (cd9660, local, noatime, read-only)
/dev/md7 on /packages/mnt/jplatform-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md8 on /packages/mnt/jruntime-12.3R3.4 (cd9660, local, noatime, read-only, verified)
/dev/md9 on /tmp (ufs, asynchronous, local, noatime)
/dev/md10 on /mfs (ufs, asynchronous, local, noatime)
/dev/ad0s1e on /config (ufs, local, noatime)
procfs on /proc (procfs, local, noatime)
/dev/ad1s1f on /var (ufs, local, noatime)
```

We should now be able to commit correctly.

```
buraglio@rtr% cli
{master}
buraglio@rtr>
{master}
buraglio@rtr> edit
Entering configuration mode
The configuration has been changed but not committed
{master}[edit]
buraglio@rtr# commit check
re0:
configuration check succeeds
re1:
configuration check succeeds
{master}[edit]
buraglio@rtr# commit
re0:
configuration check succeeds
re1:
commit complete
re0:
commit complete
{master}[edit]
buraglio@rtr#
```

And....you're done. Hopefully this will help someone fight this problem, I only found a [handful](http://www.gns3.net/labs/juniper/jncia-junos/operational-monitoring-and-maintenance/) of [other references](http://forums.juniper.net/t5/Junos-and-Junosphere/Commit-Errors/td-p/17615) to it that was useful but it didn't address my exact scenario.
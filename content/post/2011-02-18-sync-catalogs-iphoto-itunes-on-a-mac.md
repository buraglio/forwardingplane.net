---
id: 39
title: 'Sync catalogs (iPhoto, iTunes) on a mac'
date: '2011-02-18T06:46:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/02/sync-catalogs-iphoto-itunes-on-a-mac/'
permalink: /2011/02/18/sync-catalogs-iphoto-itunes-on-a-mac/
Views:
    - '44'
categories:
    - How-To
    - UNIX
---

I have huge iPhoto and iTunes catalogs. This can present a problem for both loading the applications and for backup. I have learned to deal with the Application load times, but backups are very important to me.**I'd gone through the iPhoto backup process and restore more than once, and I didn't like the fact that I didn't have an offsite backup, so I paid for a flickr pro account ($24/yr, supports iPhoto export and RAW format). I had been simply copying my iTunes over to my NAS for a long time (as well as using Time Machine), but that became a chore because I had not automated it.
After about a month of off-and-on searching, I finally went back to my UNIX roots and decided on rsync.You simply can't beat rsync.I wrote a very simple shell script to call from cron every night to sync whatever IU thought I needed to sync to my NAS (it works to any other source, really, due to rsync's flexibility).This is my simple rsync script:

#!/bin/sh# Sync catalogs to externally mounted volume.# nick@buraglio.com
RSYNC='/usr/bin/rsync'ITUNESSRC='/Users/Shared/iTunes' # iTunes FolderITUNESDST='/Volumes/Volume_1/Catalog\ Backups/iTunes' #Destination for iTunes BackupIPHOTOSRC='/Users/Shared/iPhoto' #iPhoto FolderIPHOTODST='/Volumes/Volume_1/Catalog\ Backups/iPhoto' #Destination for iPhoto BackupPARAMS='--ignore-existing --delete --progress --recursive --perms --times --size-only --whole-file' # Any parameters for rsyncEXCLUDEITUNES='-exclude='.*' -exclude='*.m4v'' # Files or folders for exclusionEXCLUDEIPHOTO='-exclude='.*'' # Files or folders for exclusion
$RSYNC $PARAMS $EXCLUDEITUNES $ITUNESSRC $ITUNESDST
$RSYNC $PARAMS $EXCLUDEIPHOTO $IPHOTOSRC $IPHOTODST
Thats it. Since the "--delete" flag is in place, I recommend use of the "--dry-run" flag the first time to make sure it does what you want, since delete <b>will** remove everything in it's path and make the folder match. I just have this run from cron every day using this line in my users crontab.

@daily /opt/local/bin/rsynccatalogs.sh


---
id: 39
title: 'Sync catalogs (iPhoto, iTunes) on a mac'
date: '2011-02-18T06:46:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/02/sync-catalogs-iphoto-itunes-on-a-mac/'
permalink: /2011/02/18/sync-catalogs-iphoto-itunes-on-a-mac/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2011/02/sync-catalogs-iphoto-itunes-on-mac.html
Views:
    - '44'
categories:
    - How-To
    - UNIX
---

<div><div><div>I have huge iPhoto and iTunes catalogs. This can present a problem for both loading the applications and for backup. I have learned to deal with the Application load times, but backups are very important to me.</div><div><br /></div><div>I'd gone through the iPhoto backup process and restore more than once, and I didn't like the fact that I didn't have an offsite backup, so I paid for a flickr pro account ($24/yr, supports iPhoto export and RAW format). I had been simply copying my iTunes over to my NAS for a long time (as well as using Time Machine), but that became a chore because I had not automated it.</div><div><br /></div><div>After about a month of off-and-on searching, I finally went back to my UNIX roots and decided on rsync.</div><div>You simply can't beat rsync.</div><div>I wrote a very simple shell script to call from cron every night to sync whatever IU thought I needed to sync to my NAS (it works to any other source, really, due to rsync's flexibility).</div></div></div><div>This is my simple rsync script:</div><div><br /><div style="font-size: small; "><br /></div><div><div><span>#!/bin/sh</span></div><div><span># Sync catalogs to externally mounted volume.</span></div><div><span># nick@buraglio.com</span></div><div><span><br /></span></div><div><span>RSYNC='/usr/bin/rsync'</span></div><div><span>ITUNESSRC='/Users/Shared/iTunes' # iTunes Folder</span></div><div><span>ITUNESDST='/Volumes/Volume_1/Catalog\ Backups/iTunes' #Destination for iTunes Backup</span></div><div><span>IPHOTOSRC='/Users/Shared/iPhoto' #iPhoto Folder</span></div><div><span>IPHOTODST='/Volumes/Volume_1/Catalog\ Backups/iPhoto' #Destination for iPhoto Backup</span></div><div><span>PARAMS='--ignore-existing --delete --progress --recursive --perms --times --size-only --whole-file' # Any parameters for rsync</span></div><div><span>EXCLUDEITUNES='-exclude='.*' -exclude='*.m4v'' # Files or folders for exclusion</span></div><div><span>EXCLUDEIPHOTO='-exclude='.*'' # Files or folders for exclusion</span></div><div><span><br /></span></div><div><span>$RSYNC $PARAMS $EXCLUDEITUNES $ITUNESSRC $ITUNESDST</span></div><div><span><br /></span></div><div><span>$RSYNC $PARAMS $EXCLUDEIPHOTO $IPHOTOSRC $IPHOTODST</span></div><div><span><br /></span></div></div><div><div><span>Thats it. Since the "--delete" flag is in place, I recommend use of the "--dry-run" flag the first time to make sure it does what you want, since delete <b>will</b> remove everything in it's path and make the folder match. I just have this run from cron every day using this line in my users crontab.</span></div><div style="font-size: small; "><br /></div><div style="font-size: small; "><br /></div><div><div><div><span>@daily<span style="white-space: pre; ">  </span>/opt/local/bin/rsynccatalogs.sh</span></div></div></div><div style="font-size: small; "><br /></div></div><div><br /></div></div><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
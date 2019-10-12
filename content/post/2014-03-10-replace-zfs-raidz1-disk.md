I recently had the displeasure of dealing with a series of failed disks in my newly created ZFS based NAS.  I had cobbled together roughly 12TB of disk space and jammed them into an old PC, stretching the limits of the platform when I decided to go with ZFS.  I broke all of the rules, underpowered, single core PC, only a handful of GIG of non-ECC RAM, etc.  I&#8217;m sure storage guys are having a coronary after reading that, but it works for me and has minimal issues since I just relatively redundant need bulk storage and it doesn&#8217;t need to be fast (the ethernet connection is only 100M).

Machine stats are as such:

AMD Sempron(tm) Processor 2800+

2G NON-ECC memory

The following disks:

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2014/03/Screenshot-2014-03-10-13.49.35.png"><img class="wp-image-936 aligncenter" alt="Screenshot 2014-03-10 13.49.35" src="http://www.forwardingplane.net/wp-content/uploads/2014/03/Screenshot-2014-03-10-13.49.35-1024x280.png" width="553" height="151" srcset="http://www.forwardingplane.net/wp-content/uploads/2014/03/Screenshot-2014-03-10-13.49.35-1024x280.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2014/03/Screenshot-2014-03-10-13.49.35-300x82.png 300w, http://www.forwardingplane.net/wp-content/uploads/2014/03/Screenshot-2014-03-10-13.49.35-550x150.png 550w, http://www.forwardingplane.net/wp-content/uploads/2014/03/Screenshot-2014-03-10-13.49.35.png 1531w" sizes="(max-width: 553px) 100vw, 553px" /></a>
</p>

The NAS was a long standing device on my network.  I&#8217;ve been using <a href="http://www.nas4free.org/" target="_blank">NAS4FREE</a> for quite some time with fantastic results.  The disks are simply desktop drives, nothing fancy.  When I rebuilt it all using ZFS I found that I had not done 2 things.  I had not documented the warranty status of the devices and I had not enabled SMART monitoring.  I know, amateur hour at its finest; I&#8217;m OK with it, it&#8217;s just for home use and I have offsite storage for anything super important.

*_As an aside, if you&#8217;re looking to build a NAS I would both recommend <a href="http://www.nas4free.org/" target="_blank">NAS4FREE</a> as well as doing something as simple as documenting the warranty information of each disk in the description field._

So, when I enabled SMART monitoring and email reporting. I found that several of my disks were failing their end-to-end tests when this started showing up in my inbox:

&nbsp;

<pre>The following warning/error was logged by the smartd daemon:
Device: /dev/ada1, Failed SMART usage Attribute: 184 End-to-End_Error.
<span style="line-height: 1.5em;">Device info:</span></pre>

<pre>ST2000DM001-1CH164, S/N:xxxxxxxx, WWN:5-000c50-08147e2a4, FW:CC26, 2.00 TB</pre>

&nbsp;

Bad news. However, with ZFS it is supposed to be fantastically easy to do disk replacements.  I had chosen RAIDZ1 for both volumes, so they could each supposedly sustain a single disk failure. There are a lot of online references for zfs. I used <a href="http://panoramicsolution.com/blog/?p=353" target="_blank">this page</a> as a starting point for replacing my disk. I dropped to the shell on the NAS and did the following to identify the right disk to remove:

<pre>nas:~# camcontrol devlist
&lt;ST31000340AS SD15&gt; at scbus0 target 0 lun 0 (ada0,pass0)
&lt;ST2000DM001-1CH164 CC26&gt; at scbus1 target 0 lun 0 (ada1,pass1)
&lt;ST2000DM001-1CH164 CC24&gt; at scbus2 target 0 lun 0 (ada2,pass2)
&lt;ST2000DM001-1CH164 CC26&gt; at scbus3 target 0 lun 0 (ada3,pass3)
&lt;WDC WD20EARS-00MVWB0 51.0AB51&gt; at scbus4 target 0 lun 0 (ada4,pass4)
&lt;ST31500341AS CC1H&gt; at scbus5 target 0 lun 0 (ada5,pass5)
&lt;ST2000DM001-1CH164 CC29&gt; at scbus6 target 0 lun 0 (ada6,pass6)
&lt;ST31500341AS CC1H&gt; at scbus7 target 0 lun 0 (ada7,pass7)
&lt;ST2000DM001-9YN164 CC82&gt; at scbus8 target 0 lun 0 (ada8,pass8)
&lt;TOSHIBA THNCF512MPG 1.00&gt; at scbus11 target 0 lun 0 (ada9,pass9)</pre>

ada8 needs replaced.  The volume it exists in is zfs0.  The formula used is _&#8220;zpool <command> <pool> <device>&#8221;_

<pre>zpool offline zfs0 ada8</pre>

None of my stuff is hot swap, so I have to shut down the box.

<pre>shutdown -h now</pre>

Yank out the old disk and install the new one.

<pre>zpool replace zfs0 ada8</pre>

<pre>zpool online zfs0 ada8</pre>

After that you&#8217;ll see the disk getting resilvered, which will take a while.

<pre>nas:~# zpool status zfs0
pool: zfs0
state: DEGRADED
status: One or more devices is currently being resilvered. The pool will
continue to function, possibly in a degraded state.
action: Wait for the resilver to complete.
scan: resilver in progress since Mon Mar 10 13:39:36 2014
105G scanned out of 3.37T at 75.4M/s, 12h36m to go
17.5G resilvered, 3.04% done
config:

NAME STATE READ WRITE CKSUM
zfs0 DEGRADED 0 0 0
raidz1-0 DEGRADED 0 0 0
ada1 ONLINE 0 0 0
ada2 ONLINE 0 0 0
ada3 ONLINE 0 0 0
ada4 ONLINE 0 0 0
ada6 ONLINE 0 0 0
replacing-5 OFFLINE 0 0 0
6070465578770542405 OFFLINE 0 0 0 was /dev/ada8/old
ada8 ONLINE 0 0 0 (resilvering)

errors: No known data errors</pre>

After the resilvering process you should have a repaired volume.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-935" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-935" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-935" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-935" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
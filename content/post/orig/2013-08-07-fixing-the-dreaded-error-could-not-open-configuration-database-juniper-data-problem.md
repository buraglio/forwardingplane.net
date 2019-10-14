Working on some MX series routers recently I encountered a problem I&#8217;d never seen before, essentially preventing the configuration from being committed:

<pre>buraglio@rtr# commit check
re0:
error: could not open configuration database (juniper.data+)</pre>

This is a very annoying problem and is terribly inconvenient as you can probably imagine. So, my first instinct is to drop down to the shell and starting hacking at it UNIX style.

<pre>buraglio@rtr&gt;start shell</pre>

From there I wanted to see the file system and check out the stats of what it thinks we have.

<pre>buraglio@rtr% df -h
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
/dev/ad1s1f     18G    4.2G     12G    26%    /var</pre>

&#8230; and check the mounted partitions.

<pre>buraglio@rtr% mount
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
/dev/ad1s1f on /var (ufs, local, noatime)</pre>

I ran a fsck to get some stats and see what the problem could be since it appears that there is no free space even though the router reports that it has it.

<pre>buraglio@rtr% fsck -y -f /dev/ad1s1f
** /dev/ad1s1f (NO WRITE)
** Last Mounted on /var
** Phase 1 - Check Blocks and Sizes
** Phase 2 - Check Pathnames
** Phase 3 - Check Connectivity
** Phase 4 - Check Reference Counts
** Phase 5 - Check Cyl groups
FREE BLK COUNT(S) WRONG IN SUPERBLK
SALVAGE? no

605 files, 2202492 used, 7040218 free (786 frags, 879929 blocks, 0.0% fragmentation)</pre>

Playing around in the shell presented this error as well

<pre>/var: create/symlink failed, no inodes free</pre>

So, it appears as if the /var partition is the issue. On my router /var is mounted as /dev/ad1s1f, so lets unmount this partition and try to fix it. In my experience Juniper will shy away from telling you to do anything in the shell, so do this at your own risk. Rebooting the router would also fix this issue, but I&#8217;m a form believer that rebooting networking equipment to fix issues is a lazy way to fix problems and will only serve to atrophy any troubleshooting skills you may have.

<pre>buraglio@rtr% umount -f /var</pre>

Now run fsck again to repair the file system

<pre>buraglio@rtr% fsck -y -f /dev/ad1s1f
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

***** FILE SYSTEM WAS MODIFIED *****</pre>

Now that the problematic bits have been repaired, we re-mount the partition

<pre>buraglio@rtr% mount /dev/ad1s1f /var/</pre>

Verify the mount

<pre>buraglio@rtr% mount
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
/dev/ad1s1f on /var (ufs, local, noatime)</pre>

We should now be able to commit correctly.

<pre>buraglio@rtr% cli
{master}
buraglio@rtr&gt;

{master}
buraglio@rtr&gt; edit
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
buraglio@rtr#</pre>

And&#8230;.you&#8217;re done. Hopefully this will help someone fight this problem, I only found a <a href="http://www.gns3.net/labs/juniper/jncia-junos/operational-monitoring-and-maintenance/" target="_blank">handful</a> of <a href="http://forums.juniper.net/t5/Junos-and-Junosphere/Commit-Errors/td-p/17615" target="_blank">other references</a> to it that was useful but it didn&#8217;t address my exact scenario.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-762" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-762" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-762" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-762" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/08/fixing-the-dreaded-error-could-not-open-configuration-database-juniper-data-problem/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

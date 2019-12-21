If you are running a network and aren&#8217;t using <a href="http://shrubbery.net/rancid/" target="_blank">RANCID</a>, you should give it a serious look.  RANCID is a cross platform configuration management toolkit for backing up router configurations and certain environmental and hardware information into version control.  It&#8217;s been around for as long as I can remember and supports nearly every platform I can think of, including a <a title="VDXrancid contrib scripts" href="http://www.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/" target="_blank">few</a> <a title="alurancid and pfrancid" href="http://www.forwardingplane.net/2011/06/alurancid-and-pfrancid/" target="_blank">modules</a> that I cobbled together myself.  There is are a few nice web based front ends for CVS and SVN, I prefer to use <a href="http://www.viewvc.org" target="_blank">ViewVC</a> because I have a lot of experience with it, however, there may be cases where a web server isn&#8217;t a good option, unavailable or just too much work.  In this case, you&#8217;ll want to know how to diff those configs from the CLI using the existing tools.  I find myself always forgetting the exact syntax of how to do this, so here it is. I prefer to use SVN, so we&#8217;ll talk about that one here.

&nbsp;

svn list will give a list of current devices in version control:

<pre>svn list</pre>

<pre>rtr1.company.com
rtr2.company.com
rtr3.company.com
sw1.company.com
sw2.company.com</pre>

To look at a router config:

<pre>svn cat &lt;router&gt;
svn cat rtr1.company.com</pre>

See all revisions:  
svn log <router>

<pre>svn log rtr1.company.com
------------------------------------------------------------------------
r863 | _rancid | 2013-01-18 12:51:59 -0600 (Fri, 18 Jan 2013) | 1 line
updates - Change made by: buraglio
------------------------------------------------------------------------
r848 | _rancid | 2013-01-09 14:00:27 -0600 (Wed, 09 Jan 2013) | 1 line
updates
------------------------------------------------------------------------
r847 | _rancid | 2013-01-09 02:07:42 -0600 (Wed, 09 Jan 2013) | 1 line
updates
------------------------------------------------------------------------
r832 | _rancid | 2012-12-12 09:42:33 -0600 (Wed, 12 Dec 2012) | 1 line
updates - Change made by: buraglio
------------------------------------------------------------------------
r804 | _rancid | 2012-11-27 14:00:28 -0600 (Tue, 27 Nov 2012) | 1 line
updates</pre>

Diff revisions:

svn diff -r <version1>:<version2> <router>

<pre>svn diff -r r863:r847 rtr1.company.com

Index: 710rtr.ui-iccn.org
===================================================================
--- rtr1.company.com	(revision 863)
+++ rtr1.company.com	(revision 847)
@@ -497,7 +497,6 @@
 !
 interface ethernet 1/1
  port-name rtr2 (1-1-11-2:e1/2)
- enable
  ip ospf area 0
  ip ospf cost 8
  ip address 10.209.143.1/30
</pre>

That&#8217;s basically it. Anything you can do from svn, you can do with your RANCID gathered SVN data. 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-389" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-389" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-389" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-389" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/01/diff-rancid-router-configs-with-svn/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
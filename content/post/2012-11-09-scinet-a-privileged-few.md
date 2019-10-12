     Every year there is an international conference for High Performance Computing, or HPC as it is often called.  This is a bit of a niche in that it&#8217;s something that many enterprises and researchers need but don&#8217;t do themselves and so many don&#8217;t have a grasp as to what all is invoved.  It&#8217;s a specialized,  potentially expensive and very different environment as well as mindset than the general sysadmin or network engineer will ever see.  The compute power is rated on it&#8217;s <a href="http://www.top500.org/" target="_blank">own scale</a> and it is very competitive.  
    While this is a very interesting subject in and of itself, it&#8217;s not really the most compelling part of this corner of the technology world.  What **is** the interesting piece is the foundation needed to make all of this work.  Compute power is obviously integral and I&#8217;ll never try to minimize its importance, but what happens when the huge data sets can&#8217;t get to the compute resources?  How do the big iron machines communicate? 

You guessed it, it&#8217;s the network. 

Over the course of my career I&#8217;ve done a lot of cool networking projects.  One of them, however, stands out far and away more than the others.

<div style="clear: both; text-align: center;">
  <a href="http://1.bp.blogspot.com/-bgjgEnK0U6s/UJyKPx1HLrI/AAAAAAABbBY/5ytF3GHKlX4/s1600/IMG_2417.JPG" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="97" src="http://1.bp.blogspot.com/-bgjgEnK0U6s/UJyKPx1HLrI/AAAAAAABbBY/5ytF3GHKlX4/s400/IMG_2417.JPG" width="400" /></a>
</div>

    Building the network to support this conference is the real gem and real challenge.  A bit of history on this network called <a href="http://en.wikipedia.org/wiki/SCinet" target="_blank">SCinet, can be found on WikiPedia</a>. 



<div>
  <span style="font-family: Times, Times New Roman, serif; font-size: x-small;"><b>&#8220;SCinet</b> is a high-performance <a href="http://en.wikipedia.org/wiki/Computer_networking"><span>network</span></a> that is built, once a year, in support of the annual <i>International Conference for High Performance Computing and Communications</i> also known as the <a href="http://en.wikipedia.org/wiki/Supercomputing_Conference"><span>Supercomputing Conference</span></a>. It is the primary network for the conference and is used by attendees to demonstrate and test high-performance distributed applications.</span>
</div>

<div>
  <span style="font-family: Times, Times New Roman, serif; font-size: x-small;">Originated in 1991 as an initiative within the SC conference to provide networking to attendees, SCinet has grown to become the &#8220;World&#8217;s Fastest Network&#8221; during the duration of the conference. Over the years, SCinet has been used as a platform to test networking technology and applications which have found their way into common use.</span>
</div>

<div>
  <span style="font-family: Times, Times New Roman, serif; font-size: x-small;">At SC|05 <a href="http://www.sc05.org/"><span>[1]</span></a>, SCinet initiated a conference wide <a href="http://en.wikipedia.org/wiki/InfiniBand"><span>InfiniBand</span></a> infrastructure, combining various IB hardware vendors utilizing <a href="http://en.wikipedia.org/w/index.php?title=OpenIB&#038;action=edit&#038;redlink=1"><span>OpenIB</span></a> software.</span>
</div>

<div>
  <span style="font-family: Times, Times New Roman, serif; font-size: x-small;">In previous years, SCinet deployed conference wide networking technologies such as <a href="http://en.wikipedia.org/wiki/Asynchronous_Transfer_Mode"><span>ATM</span></a>, <a href="http://en.wikipedia.org/wiki/Fiber_distributed_data_interface"><span>FDDI</span></a>, <a href="http://en.wikipedia.org/w/index.php?title=HiPPi&#038;action=edit&#038;redlink=1"><span>HiPPi</span></a> before they were deployed commercially.&#8221;</span>
</div>

<div>
  <span style="font-family: Times, Times New Roman, serif; font-size: x-small;"><br /></span>
</div>

<div>
  <span style="font-family: inherit;">    I&#8217;ve been involved since 2003, it made sense since my employer was a major supercomputing center, after all.  </span>
</div>

<div>
  <span style="font-family: inherit;">    Over the years I&#8217;ve participated in different capacities and different roles, Security, Wireless, UNIX services and routing.  The team that builds this amazing network do it because they want to.  It&#8217;s a labor of love.  It&#8217;s also an amazing experience.  This network, called &#8220;The worlds fastest network&#8221; on more than one occasion is built and torn down in less than a month.  The network has more bandwidth than some small countries, and it&#8217;s built specifically to support </span><a href="http://supercomputing.org/" style="font-family: inherit;" target="_blank">this conference</a><span style="font-family: inherit;"> and the big science that gets demonstrated.  It&#8217;s always built with different </span>heterogeneous<span style="font-family: inherit;"> equipment.  It&#8217;s an amazing interoperability experiment that has a <a href="http://sc12.supercomputing.org/content/scinet-contributors" target="_blank">who&#8217;s who of big names</a>.  </span>
</div>

<div>
  <span style="font-family: inherit;">    This is interesting and worth mentioning </span>because<span style="font-family: inherit;"> it is an amazing feat that many never even know happens.  It is happening now.  It will happen again next year.  And it will be in a different location, with different gear and a different </span>architecture.  If that&#8217;s not enough, it&#8217;s also got a <a href="http://sc12.supercomputing.org/content/scinet-research-sandbox" target="_blank">research sandbox</a> for all of your SDN needs.  <span style="font-family: inherit;">   </span>
</div>

<div>
</div>

<div>
</div>

<div>
  <span style="font-family: inherit;"><a href="http://gan.doubleclick.net/gan_click?lid=41000613802463762&#038;pid=UBM9780596100148&#038;adurl=http%3A%2F%2Fwww.cdsbooksdvds.com%2Fproduct.jhtm%3Fsku%3DUBM9780596100148&#038;usg=AFHzDLuaU0JGfNPJeXjijzZ9FD_gtq3QuQ&#038;pubid=590157" rel="nofollow">Junos Cookbook: by Garrett, Aviva [Paperback]</a></span>
</div>

<div>
  <a href="http://gan.doubleclick.net/gan_click?lid=41000613802463762&#038;pid=UBM9780792380979&#038;adurl=http%3A%2F%2Fwww.cdsbooksdvds.com%2Fproduct.jhtm%3Fsku%3DUBM9780792380979&#038;usg=AFHzDLv9M31JF4OoLZwreG26xo5qDVnDJg&#038;pubid=590157" rel="nofollow">Scalable High Performance Computing for Knowledge Discovery and Data Mining</a>
</div>

<div>
  <span style="font-family: inherit;"><br /></span>
</div>

<div>
  <span style="font-family: inherit;"><br /></span>
</div>

<div>
  <span style="font-family: inherit;"><br /></span>
</div>

<div>
  [[ This is a content summary only. Visit my website for full links, other content, and more! ]]
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-9" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-9" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-9" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-9" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/11/scinet-a-privileged-few/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
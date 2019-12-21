It&#8217;s no secret that I&#8217;m a fan of the model <a href="http://www.aristanetworks.com" target="_blank">Arista Networks</a> is using to make gear and provide innovative services and products. In my opinion, they&#8217;re changing the landscape of campus and data center networking gear. I&#8217;m always a fan of the little guy trying to change the world and this falls under that category. For those that don&#8217;t know, Arista Networks is a &#8220;hardware&#8221; networking company that is using merchant silicon wrapped in their custom linux based operating system (which is very much like IOS).

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.jpg"><img class="aligncenter  wp-image-445" alt="ARISTA-TAP" src="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-1024x768.jpg" width="430" height="323" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-1024x768.jpg 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-300x225.jpg 300w, http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-550x412.jpg 550w" sizes="(max-width: 430px) 100vw, 430px" /></a>
</p>

This model does a few things. It takes the time it would normally take a vendor to engineer and spin an ASIC, typically 1-3 years) and completely removes it. Instead, they rely on silicon manufacturers like Intel and <a href="http://www.fulcrummicro.com" target="_blank">Fulcrum</a> for their already engineered and tested chips. Arista is generally touted as an extremely low latency box and has been widely deployed in the financial industry because of this. However, they&#8217;re not a one trick pony, not by any means. Their open architecture and OS allows for <span style="text-decoration: underline;"><strong>heavy</strong></span> customization. In fact, unlike most others, it&#8217;s encouraged. Arista has put together an <a href="https://eos.aristanetworks.com/home.php" target="_blank">ecosystem for extending and expanding</a> their <a href="https://eos.aristanetworks.com/2011/03/eos-so-what-is-it/" target="_blank">EOS</a> networking operating system. Want something added to the CLI? Easy, it&#8217;s all python and can be changed on-box and submitted back to the community. They also have a very, very slick internal mechanism called the sysdb, but that&#8217;s another blog post altogether.

&nbsp;

None of this is really new. Folks have been using merchant silicon forever. What is new and refreshing is the open nature of it. Additionally, the exclusive use of merchant silicon is something [I believe] is now in this class of hardware. With the open nature of this platform, it also lends itself well to the OpenFlow movement in that it&#8217;s essentially a linux box on well documented hardware of which the vendor is encouraging modification. In addition, it is a well tested data center product. I&#8217;m calling it now, this platform is going to go places in it&#8217;s market.

For the newest addition to the capabilities portfolio, this is where it really gets interesting. As of 2/13/2013 Arista has added some very <a href="http://www.aristanetworks.com/en/news/pressrelease/532-pr-20130212-01" target="_blank">compelling tap aggregation options</a>. What this means, is that you can now aggregate Nx1 or 10G at 40G, then symmetrically hash that across another 10G array to an IDS cluster. Why is this important? Monitoring fat links. Have some 100G? Good luck finding a security mechanism to watch that.

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png"><img class="aligncenter  wp-image-440" alt="ARISTA TAP" src="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png" width="467" height="354" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP.png 584w, http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-300x227.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/02/ARISTA-TAP-550x416.png 550w" sizes="(max-width: 467px) 100vw, 467px" /></a>
</p>

Until now the only options for this are players like <a href="http://www.gigamon.com" target="_blank">Gigamon</a>, <a href="http://www.cpacket.com" target="_blank">cPacket</a> and maybe <a href="http://www.mrv.com" target="_blank">MRV</a>. All are very expensive and one-off solutions. Arista offers a standard ethernet switch that can be managed by an existing networking team, integrated into existing network tools and maintained like any other router or switch. OpEx is a wash. Capital expenditure is standard [probably cheaper] than a normal Layer2 switch. It looks JUST like IOS, so the old networking guy that hates change will only complain a little that it&#8217;s not a blue box with a bridge on it.

This may seem like a small deal, but the implications for passive security monitoring are huge. This feature alone will have a trickle down effect over the next few years since it&#8217;s something that is only recently being exercised in enterprise worlds. I suspect this will also have a very large impact to gigamon, who is really the current industry leader in this corner of the market, but is priced well beyond what many can afford.

Arista can now do the symmetric hashing on layer2, layer3 or layer4 parameters. ACL support is also coming, although I&#8217;ve not seen it work like I have the hashing.

&nbsp;

Oh, you want to know how to do it? =) It currently doesn&#8217;t exist in the CLI, but here is basically how it&#8217;s done. Thanks to an awesome Arista rep, the heavy lifting of parsing through the Acons interface is all condensed to a simple script.

from the CLI:

Log in and enable.

<pre>7150-Source#bash
Arista Networks EOS shell
[arista@7150-Source ~]$ cd /mnt/flash

[arista@7150-Source ~]$vi set_hash.sh
#!/bin/ti
rm /mnt/flash/set_hash_log.txt
cat &lt;&lt; EOF | Acons FocalPointV2 &gt;&gt; /mnt/flash/set_hash_log.txt 2&gt;&1
from FmApi import *
fmDbgWriteRegisterField(0,0,0,0,"FM6000_HASH_LAYER3_PROFILE","SymmetrizeL3",1)
fmDbgWriteRegisterField(0,0,0,0,"FM6000_HASH_LAYER3_PROFILE","SymmetrizeL4",1)
fmDbgWriteRegisterField(0,0,0,0,"FM6000_HASH_LAYER2_KEY_PROFILE","SymmetrizeMAC",1)
EOF
exit 0</pre>

Done. This, of course, doesn&#8217;t include any of the port channel and monitor interface configuration, but if you&#8217;re this deep, you probably know how to do that already.

If you&#8217;d like to dump this to a log, add the following lines to the end of the script before the &#8220;EOF&#8221;

<pre>fmDbgDumpRegisterV2(0,0,0,"FM6000_HASH_LAYER2_KEY_PROFILE")
fmDbgDumpRegisterV2(0,0,0,"FM6000_HASH_LAYER3_PROFILE")</pre>

*As the CLI bits become available in EOS 4.12, this post will be amended to the more supportable way of managing this awesome new feature.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-439" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-439" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-439" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-439" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/02/watch-out-gigamon-and-others-arista-is-bringing-their-a-game/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
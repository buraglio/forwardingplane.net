When [NEC](http://necam.com/) began talking about SDN at [Network Field Day 9](http://techfieldday.com/event/nfd9/), I was not sure what to expect. I knew they had been heavily involved with openflow since the early days, and many years ago I was able to get my hands on their early OpenFlow controller and was immediately frustrated by its cryptic nature and frankly, poor documentation. Their switches were fine and were heavily utilized in early OpenFlow deployments. I knew they had decent support and were squarely on board the SDN train. Their controller, in 2010, was not terribly fun to work with. It was (if memory serves) prohibitively expensive and the support manual was nearly as cryptic as the controller. Because it&#8217;s my personality type, I went in with a very open mind, hoping to be surprised. After all, it&#8217;d been 4+ years since I&#8217;d seen that controller.

Well, I am here to report that I will happily eat some crow.

[<img class=" size-full wp-image-1162 aligncenter" src="http://www.forwardingplane.net/wp-content/uploads/2015/02/Eat-Crow.jpg" alt="Eat Crow" width="293" height="200" />](http://www.forwardingplane.net/wp-content/uploads/2015/02/Eat-Crow.jpg)

&nbsp;

A few things became very apparent to me as I sat and watched the presentation from NEC, which you can view in its entirety below:

  * NEC is not messing around with their SDN offering. They&#8217;ve been in the openflow game since the beginning and the polish on their controller shows it. The topology is quite nice and they&#8217;ve got a finished looking product that would find itself at home in a decent sized NOC.
  * NEC is playing well with others. Their demo consisted of both NEC and DELL whitebox switches. To me this is an indication of both great forward thinking and a clear message that the controller is a product that can stand on its own.
  * NEC is setting the barrier of entry low. Very low. They&#8217;ve got an entry level &#8220;SDN in a box&#8221; that consists of their controller and a few switches for like 3k. They&#8217;re also offering a 90 day free trial on their controller that is bundled with [mininet](http://mininet.org/).
  * Like most other controllers, the NEC controller is topology aware and using openflow 1.3 for it&#8217;s communication. Unlike any other demo I&#8217;ve seen, NEC used CLI to make changes and displayed the updates in near realtime on the controller.

They&#8217;ve got a tap product aimed at security tap aggregators a la [gigamon](http://www.gigamon.com/), so they&#8217;re seeing the value of SDN and openflow from a security lens as well as a network operations perspective, a good play in my opinion. SDN and openflow in particular have a great deal to offer the security community (think of all of the wacky stuff your security team has asked for and then map that into an openflow network. You&#8217;ll probably hit 80% match). NEC has done some tight integration with <a href="https://technet.microsoft.com/en-us/windowsserver/dd448604.aspx" target="_blank">microsoft hyper-v</a> too, so environments leveraging hyper-v as a virtualization technology can drop this in to take advantage of the network programmability on top of their virtualization environment. This is something that I&#8217;d not seen before [although it may exist and I just don&#8217;t know it].

In addition, NEC has spun up an &#8220;app store&#8221; for SDN apps and allowed for some cross pollination, with a handful of caveats, with [opendaylight](http://www.opendaylight.org/) for testing.

<speculation>

There are a few things I find interesting about the NEC offering and about NEC in general. Being in a service provider environment off and on for most of my career, the fact that NEC is getting involved so heavily is intriguing. Unlike most of the other DC focused companies, NEC plays in the carrier market. While this particular briefing did not include any carrier updates, it would surprise me if this wasn&#8217;t being investigated behind some big doors. It makes sense to me and it would be a surprise if it did not occur to someone else. The SP market is fickle and slow to change, but ripe for fresh ideas. I see a lot of potential both there and in the DC / campus / enterprise.

</speculation>

&nbsp;  


[Introduction to NEC Networking](https://vimeo.com/119508255) from [Stephen Foskett](https://vimeo.com/sfoskett) on [Vimeo](https://vimeo.com).  


[NEC ProgrammableFlow vCOps Solution](https://vimeo.com/119508725) from [Stephen Foskett](https://vimeo.com/sfoskett) on [Vimeo](https://vimeo.com).  


[ProgrammableFlow SCVMM Demo](https://vimeo.com/119510207) from [Stephen Foskett](https://vimeo.com/sfoskett) on [Vimeo](https://vimeo.com).

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1161" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1161" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1161" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1161" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2015/02/the-nec-surprise/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

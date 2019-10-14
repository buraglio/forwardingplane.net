I was recently granted access to the beta <a href="http://www.bigswitch.com/" target="_blank">BigSwitch Networks</a> lab site, a purpose built classroom in the cloud focused on teaching the BigSwitch SDN environment.  I had seen some of the BSN offerings in the past and always held them in high regard, but I was thoroughly impressed with both the completeness of the lab and how polished the controller environment was.<img class="aligncenter wp-image-1070" src="http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.28.50.png" alt="Screenshot 2014-09-12 10.28.50" width="500" height="308" />

At the time of this writing, the lab consists of 3 modules: Building cloud fabric, monitoring fabric and dynamic provisioning of monitoring fabric.  Since there is quite a lot going on with this cloud based SDN classroom, for the scope of this post I&#8217;ll concentrate on the first, building cloud fabric.  I&#8217;m a big fan of the CLI*, and one thing that jumped right out to me was that they provide the GUI and the CLI, and that the CLI is familiar to anyone that has worked on an IOS device.  The lab is useful, even for someone that has done some SDN, both on production or in a lab, in that it presents the fundamentals in a way that both demonstrates the purpose and function and lays out the technology and product.

From the technology presentation standpoint, the BigSwitch offering is quite impressive.

The reality of it is that, in my experience, GUIs don&#8217;t always have the most intuitive or complete implementations and they&#8217;re hard to automate.  Now, from what I&#8217;ve seen to far the bigswitch offing is the exception to that rule.  The setup is very functional and goes through a range of great material. for comparison, below is the tenants display from the web interface:

[<img class="aligncenter wp-image-1082" src="http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.47.37.png" alt="Screenshot 2014-09-12 10.47.37" width="500" height="307" />](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.47.37.png)

&nbsp;

and the corresponding show command:

[<img class="aligncenter wp-image-1074" src="http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.33.49.png" alt="show tenant" width="500" height="306" />](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.33.49.png)

Nevertheless, part of my usual workflow is to use one to define the other when I can.  What I mean by that is that if I don&#8217;t know exactly how to accomplish my goal in the GUI, I switch to the CLI and see what I can do from there, returning to the GUI to see what has changed and then reverse engineer it from that perspective.  The opposite is also true, I have used the CLI to define the GUI _:cough:_ <a href="http://www.juniper.net/us/en/products-services/security/netscreen/" target="_blank">netscreen</a> _:cough:_. The important thing to note here, though, is that the tools all work as if it is a real environment, because it _is_ a real environment.

The god among men here, really, is the _debug rest_ command.  This command, when issued in the CLI (displayed below) allows the commands sent to the terminal to automatically pop up with the rest interface commands necessary to utilize them.  Wrap your head around that one for a minute.  Are you thinking automation?  Me too; seeing that made me want to go write code, and I am a horrible developer.

<img class="aligncenter wp-image-1084" src="http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.50.19.png" alt="Screenshot 2014-09-12 10.50.19" width="500" height="307" /> 

In the time I&#8217;ve spent within this system I have been thoroughly impressed with how well it functioned.  I had no issues whatsoever with how the training presented the material, executed the commands or displayed the responses.  My only suggestion would be to add a configuration guide for the CLI =)

Below is a quick youtube video of some of the functions.  


&nbsp;

* Yes, I know SDN is supposed to &#8220;kill the CLI&#8221;.  I don&#8217;t by the sensationalism for the short to medium term.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1066" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1066" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1066" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1066" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/09/bigswitch-labs-for-sdn-learning-a-sneak-peek/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
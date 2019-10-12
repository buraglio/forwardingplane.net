A few years ago I wrote [some text](http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/) on [interdomain SDN](http://www.forwardingplane.net/2013/01/sdn-across-the-wan-part-deux-primitives/). Years later, work is being done, smart people are thinking about it and building ways to make it a reality. Not being one to give up on an idea, I gave [this presentation](https://docs.google.com/presentation/d/1anAaqWR8wmzKO5fqidDy9QJXW4RiVshX9Miq3PoDv9E/edit) in may at [ChiNOG](http://chinog.org/meetings/chi-nog-05/)  on what my take on what that architecture should be. I (we) propose that the use of existing protocols such as [BGP FlowSpec](https://tools.ietf.org/html/rfc5575) will make this realistically deployable and maintainable given some [simple, pluggable middleware](https://github.com/dwcarder/sdn-ix-demo). As work continues to happen on this, my belief is that this is a very sound (and simple) concept. The middleware is modular and flexible enough that it can stand alone or plug into an existing code base such as ODL or Ryu. As <a href="http://sc15blog.blogspot.com/2015/11/simplifying-worlds-most-powerful.html" target="_blank">I work on the SDN deployment</a> for the [annual international supercomputing conference](http://www.sc15.org), and work on the [SDN for scientific networking workshop](https://www.es.net/network-r-and-d/workshops/),  I become more and more convinced that there needs to be an operationally viable and simple way to support these types of networks in ways that are thin and simple since it is a newer concept and some of the protocols involved (e.g. OpenFlow) is still in its infancy.  Here is the video of the talk for anyone interested in listening to me talk about it for 20 minutes.



As a reference, this is a great talk from the same conference on BGP FlowSpec that adds a lot of credence to the use of it as a policy dissemination protocol.



<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1330" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1330" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1330" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1330" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2015/11/building-interdomain-sdn-part-3/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
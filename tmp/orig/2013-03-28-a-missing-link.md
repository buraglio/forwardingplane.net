Lately I&#8217;ve been lamenting the fact that there seems to be a lack of options in a very specific product level.  Lets say you have a network that looks like this:

&nbsp;

[<img class="alignleft size-full wp-image-568" alt="10G-Bldg" src="http://www.forwardingplane.net/wp-content/uploads/2013/03/10G-Bldg1.jpg" width="432" height="599" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/03/10G-Bldg1.jpg 432w, http://www.forwardingplane.net/wp-content/uploads/2013/03/10G-Bldg1-216x300.jpg 216w" sizes="(max-width: 432px) 100vw, 432px" />](http://www.forwardingplane.net/wp-content/uploads/2013/03/10G-Bldg1.jpg)Right Away you&#8217;re limited since you need MPLS and more than 2 10G interfaces. Even more so if you require full support for IPv6 and ISIS.

If budget is of any concern, you&#8217;re in real trouble.

For many, Cisco pricing and smartnet is potentially going to exclude anything reasonable from them.  There are a substantial amount of non-enterprise folks out there that can&#8217;t afford the significant Cisco price tag but need the features.  I am here to say, this is a problem.  The attitude of &#8220;if you want the best you have to pay for it&#8221; doesn&#8217;t apply.  There is a real need for viable alternatives, not just because we need them, but because competition is a good thing for everyone.

Juniper has the MX80, but it has a carrier grade price tag as well.  Juniper has limited MPLS support on the EX series, but the EX4200, which is arguably the most tried and true, has only 2 ports of 10G and, as mentioned, limited MPLS support.  The EX4500 is a tad better with its huge amount of 10G ports, but it has the same limited MPLS support and a crippled ARP and FIB table.  The 4550 with it&#8217;s single PFE sounds exciting but it has even less.

Then you have the Brocade CES/R.  It is close.  The newer version has  4 x 10G ports, MPLS support (with a license), more appropriately priced support and, as a value add, very good OpenFlow support.  It is still limited as far as 10G scalability, so adding more access switches could be problematic.

HP has some great products in the Procurve series.  They&#8217;re inexpensive, rock solid and packed with features. Unfortunately, the ones that meet the port density are fairly good sized chassis and none of them have MPLS.  Now, they do have an intriguing line up in the H3C series.  I believe there may be an option there, however, I have no idea on pricing and have yet to see one actually do MPLS (although they claim support).  I&#8217;m cautiously optimistic.

Then you have Alcatel Lucent.   They do MPLS, they&#8217;re carrier devices.  They offer a 1U (  
(<a href="http://www.alcatel-lucent.com/products/7210-service-access-switch" target="_blank">7210 Service Access Switch</a>) device but I have no idea on cost and I&#8217;m still looking for 10G port density.  I suspect it is very reasonable.  Their <a title="Alcatel Lucent RANCID scripts" href="http://www.forwardingplane.net/2010/12/alcatel-lucent-rancid-scripts/" target="_blank">CLI is a bit different</a> but they&#8217;re very robust devices.  I&#8217;ve not used any but the 7750, so I cant comment as to how the smaller ones look.  It&#8217;s a possibility if it has the 10G ports.

Arista is very close but they fall short on the MPLS support.

&nbsp;

The primary take away from this commentary is that there are not a lot of options that meet the following criteria:

  * 1-2U
  * > 4 10G ports
  * MPLS
  * Dual power supplies
  * > 16,000/4,000 IPv4/IPv6 routes
  * IPv6 support
  * ISIS
  * 40G uplink
  * OpenFlow support or roadmap
  * **Reasonably priced**

I keep coming back to the old adage of &#8220;Cheap, Fast, Reliable.  Pick Two&#8221; and it drives me crazy.  We should have more options but I don&#8217;t think we do.  I would absolutely **love** to be wrong, but every time I look at this I feel like I am picking out a cell phone plan.  The affordable ones are never quite enough and the plan above is overkill and too expensive.

&nbsp;

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-564" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-564" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-564" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-564" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/03/a-missing-link/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

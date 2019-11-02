In recent years, the nature of [privacy on the internet](http://fortune.com/2017/11/23/net-neutrality-explained-what-it-means-and-why-it-matters/) has become a very important topic amongst those concerned with the now lack of [net neutrality](https://www.theverge.com/2017/12/14/16776154/fcc-net-neutrality-vote-results-rules-repealed). The de-facto mechanism for dealing with privacy has been to &#8220;[SSL all the things](https://letsencrypt.org/)&#8220;, which I am very much in favor of. What many do not realize, though, is that simply using SSL for the traffic that transits a given ISP still leaves a wealth of thick, rich, delicious personal data still easily available to your ISP to harvest, sell, and do with as they please. This data comes in the form of DNS queries. DNS is the nearly-always-forgotten, crucial aspect of how the internet functions. Without DNS, nothing works. Everything appears broken and manifest as what appears to be a networking problem. ISPs typically provide what is called a [recursive resolver](https://umbrella.cisco.com/blog/2014/07/16/difference-authoritative-recursive-dns-nameservers/), which for most people is handed down by a local provider to the customer premise equipment (CPE; usually a modem or optical terminal of some kind) that they install at a residence. This CPE then hands that resolver to your clients that use it to &#8211; you guessed it &#8211; recursively resolve DNS queries. These queries can be logged and then mined for browsing habits, etc. Anyone that has ever done any network forensics will know straight away that the value of the information contained in DNS query logs is very, very high. 

What this means is that even though a privacy conscious individual is hiding the bulk of their content in SSL, meaning the bulk of what they’re reading, searching for, and doing, is encrypted, the requests for that content or activity is not. For example, an ISP can potentially see that a client is making many, many queries for $onlineshopping.com and begin selling that data to advertisers. If you think they’re not doing this now, [think again](https://www.wired.com/story/can-verizon-build-a-strong-brand-from-the-bones-of-yahoo-and-aol/). 

Great, so $bigbadprovider can see your queries. There are a number of pretty good ways to work around this, and [one of my favorite projects](https://pi-hole.net/) handily deals with one of them with great simplicity. What I am referring to is the newly popular [DNS over HTTPS](https://scotthelme.co.uk/securing-dns-across-all-of-my-devices-with-pihole-dns-over-https-1-1-1-1/), which is supported by the [cloudflare 1.1.1.1 service](https://one.one.one.one/). 

So, as a thought experiment I decided to play Reeses Peanut butter and chocolate with two of my favorite technological creations: the aforementioned PiHole, and [ZeroTier](https://zerotier.com/). Now anyone that isn’t familiar with ZeroTier, you should acquaint yourself &#8211; Packet Pushers did a good [podcast on it back in November of 2017](https://packetpushers.net/podcast/pq-134-meet-zerotier-open-source-networking/). It’s functionally an encrypted overlay supporting dual stack networking with auto configuration and gateway capabilities, and it runs on almost everything. I love this overlay technology and have been using it for a while &#8211; highly recommended.

Back to my peanut butter and chocolate experiment. So, given that I had an existing ZeroTier network and an existing PiHole setup at home, I went over to [Vultr.com](https://www.vultr.com/?ref=7692870) and spun up a small VM for $3.50/mo, integrated it into my fleet with my Ansible and Salt tools, and installed ZeroTier and Pihole. From there I set up this DNS hierarchy. 

<img style="display: block; margin-left: auto; margin-right: auto;" src="https://docs.google.com/drawings/d/e/2PACX-1vS-DsmzNWvE335KZtNo6AHX3SySG-VQWhK7i9sNgT6mFMHC5VzRWtMuJg5JraU2dJTFQT4QIGnfaMFP/pub?w=960&h=720" /> 

<span style="font-family: Helvetica;">What this buys me is a fully encrypted DNS path up through the Vultr.com VM host without modifying the underlying DNS transport. And it works surprisingly well. I ran SmokePing from two hosts &#8211; both leveraging ZeroTier to do their testing, one on my local network and one in the cloud &#8211; to measure latency for a few days before I did this and kept that running after the deployment. Now, it’s not perfect but my family and I have been using this for about a month with minimal issues. Once in a great while we’ll see some slow DNS resolution time, but overall it works fairly well. </span>

 

<span style="font-family: Helvetica; font-size: 12px;"><span style="font-family: Helvetica;"><img style="display: block; margin-left: auto; margin-right: auto;" title="Resolver Queries.png" src="https://www.forwardingplane.net/wp-content/uploads/2018/12/Resolver-Queries.png" alt="Resolver Queries" width="597" height="223" border="0" /></span></span>

<span style="font-family: Helvetica; font-size: 18px;"><strong>My take </strong></span>

<span style="font-family: Helvetica;">The idea of using a public resolver kinda bothers me, I realize it’s probably unfounded, but I know how to and have run resolvers for ISPs and organizations for like 20 years, so I have the burden of knowledge about what is in the logs and how to run my own. Using a secured recursive resolver is simply trading transit privacy for lack of query privacy somewhere else. Then there is the issue of content networks that use DNS queries to take you to the best / topologically closest cache of their content [NOTE: this, along with the forensics data for debugging potential security issues is a <strong>top</strong> reason that all ISPs should run their own resolvers]. I fully realize that a normal end user running their own resolver is unlikely and that this deployment is a bit overkill. However, as I can demonstrably prove, it works. And it works pretty well. It also has the added bonus of allowing me to have internal DNS resolution of my own hosts and any mobile ZeroTier client. Is it for everyone? No way. Does it prove viability for low/medium traffic use? Sure. The point is really just to get folks thinking about information leaking that they may not have considered. The nature of the internet makes true privacy pretty much impossible, but there are a few ways to make your data a little harder to for companies to compile and capitalize on if you truly don’t want them to. </span>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1506" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1506" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1506" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1506" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2018/12/dns-the-treasure-trove-of-information-your-isp-can-see/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
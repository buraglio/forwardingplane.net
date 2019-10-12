Recently, the venerable [Ivan Pepelnjak](https://blog.ipspace.net) published a very insightful article about [automation becoming such a popular topic](https://blog.ipspace.net/2018/10/why-is-network-automation-such-hot-topic.html) that was spawned by an email from one of his readers. I found this article to be spot on, and wanted to add a bit of my own opinion into the automation pie, as I have been spending a lot of time on automation as it related to existing networks as well as into SDN based environments. There is a link, and I wanted to explore it a bit more whilst adding a healthy dose of my opinion.

A very large part of the automation push is the IT pendulum swing. Like those of us that worked in the burgeoning ISP world, automating was born of necessity. Except &#8211; we didn&#8217;t call it automation. Most of us didn&#8217;t call it anything, it was sysadmin scripting at worst and full blown orchestration at best. And there were even commercial platforms (see broadband provisioning tools). However, like many of us that were in the early ISP days, at the very least we had some rudimentary programming and scripting skills because we either had to develop them to stay afloat or we came from an early applied computer science background. Those skills, like a lot of other things, also have the pendulum swing.

##<img class="size-large aligncenter" src="https://media.giphy.com/media/ttTKR0wqCUCt2/giphy.gif" width="400" height="441" /> 

## The pendulum.

Think of the pendulum in terms of computing, as it&#8217;s the easiest to quantify. Computing went from centralized (i.e. the mainframe) to decentralized (i.e. the desktop PC). Now we&#8217;re moving back into the &#8220;centralized&#8221; model in the push to cloud (ok, that may be a tad different, but conceptually it&#8217;s the same &#8211; work with me). Moving computationally expensive operations out of a single, personal system into a larger resource while reducing the overhead of the end station. Think [Chromebook](https://www.amazon.com/Google-Pixelbook-RAM-128GB-GA00122-US/dp/B075JSK7TR/ref=sr_1_4_acs_osp_osp19-42c2a08e-2d_2?s=pc&ie=UTF8&qid=1539871559&sr=1-4-acs&keywords=chromebook&tag=crverifiedexp-20&ascsubtag=42c2a08e-2d48-4a89-8acb-841bc830f277&linkCode=oas&cv_ct_id=amzn1.osp.42c2a08e-2d48-4a89-8acb-841bc830f277&cv_ct_pg=search&cv_ct_wn=osp-search&pf_rd_s=desktop-sx-inline&pd_rd_w=qgIuG&pf_rd_i=chromebook&pd_rd_wg=OLHr0&pf_rd_p=53b688eb-671a-4acd-886f-dc89fa36d3d2&pf_rd_t=301&pd_rd_r=4d4ed571-35bf-4be9-860c-7deaa1ce8cc4&pf_rd_r=QNRHZW6VWAWZ13HMDGF7&pf_rd_m=ATVPDKIKX0DER&creativeASIN=B075JSK7TR&pf_rd_p=53b688eb-671a-4acd-886f-dc89fa36d3d2&pd_rd_wg=OLHr0&pd_rd_i=B075JSK7TR&pf_rd_s=desktop-sx-inline&pf_rd_t=301&pf_rd_i=chromebook&pf_rd_m=ATVPDKIKX0DER&pd_rd_w=qgIuG&pf_rd_r=QNRHZW6VWAWZ13HMDGF7&pd_rd_r=4d4ed571-35bf-4be9-860c-7deaa1ce8cc4) or VDI thin client.

Dramatic changes do not happen quickly in the networking world, and there are a number of simple reasons why

  1. Mean time to replacement is somewhere between 5 and 10 years depending on the environment
  2. Standards for networking take <span style="text-decoration: underline;"><strong>For-ev-er</strong></span>

So, even if the time to replace lifecycle is short, the windows for new tech standards, vendor implementation, and knowledge dissemination to occur rarely, if ever, line up. What this means is that new tech is very slow to adopt in the network world. Even I make the mistake of being far too impatient with this process sometimes, as [Jordan Marti](https://twitter.com/bcjordo?lang=en)n called me out on in a [Network Collective podcast](https://thenetworkcollective.com/2018/02/otc-nfd17/) a few months ago (p.s., it&#8217;s a fun listen &#8211; check it out).

Back to automation. As IT changed in non-service providers from a questionable money sink to a potentially critical revenue generating business and communications environment the generalist IT workers slowly morphed into the specialists. Developers, Network Engineers, Systems Engineers, phone system admins, etc. As this occurred, the disciplines fractured and the skillsets refined, and in many cases lost the generalist foundation in trade for a deeply focused skill set.

## The SDN

After a decade or two of this shift, SDN blows onto the scene. SDN, as it emerges and becomes the new marketing darling of many a start up and huge company alike, promises to destroy boundaries and obsolete basically everything &#8211; equipment, skill sets, people, cars, dogs, cats, water, air&#8230;&#8230;.everything. The issue is that from a few research products that had ground breaking ideas came a monster. As over-hyped, over-marketed, and under developed juggernaut that had a different meaning to anyone you asked. Whole some folks plugged away quietly on [projects that actually wor](https://faucet.nz/)k, and [experimented](http://www.forwardingplane.net/2012/11/sdn-across-domains-in-the-wan-a-novice-look/) with [deployments meant to function in production](https://esnetupdates.wordpress.com/2015/11/03/esnets-nick-buraglio-leading-scinets-first-sdn-effort-at-sc15/), the marketing machines created more and more hype and delivered only a few promises.

This is the far out pendulum swing. Many operators recoiled. Enterprises said &#8220;why?&#8221;, and folks trying to push boundaries with new deployments were saying &#8220;_wait, let&#8217;s figure out &#8220;what&#8221; before we ask &#8220;why?&#8221;_&#8220;. Then the pendulum started swinging back. Automation is back, and now there are [products](https://www.ansible.com/) and tools, and [resources](https://www.ipspace.net/Hands-On_Network_Automation). We&#8217;re centering on a safer alternative that conservative enterprises can deploy safely and without event. We&#8217;re back to the fundamentals and the basics of what worked long ago &#8211; but now we have help.

## My take

Make no mistake, I am still believer in the fundamentals that something resembling SDN brings to the table and have been working on [significant SDN projects even recently](https://sc18.supercomputing.org/blog/), including moving our entire office over to FAUCET controlled switches (more on this soon), and a fair amount of work in the segment routing / PCE space. However, I am not a fan of the marketing machine, especially when there is a poverty of useful data to build said marketing from, and said marketing contains an [overabundance of sensational FUD](https://www.forwardingplane.net/2013/03/my-sdn-soapbox-now-with-ipv6/). New technology needs to be supportable to be deployed, and it happens, very, very slowly. Much like IPv4 to IPv6, Frame Relay to ATM, and circuit switched to packet switched, as SDN technologies become more and more exposed and easier to use, they become &#8220;just another thing&#8221;, and that takes time.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1486" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1486" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1486" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1486" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2018/10/the-rush-to-automation-and-the-it-pendulum/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

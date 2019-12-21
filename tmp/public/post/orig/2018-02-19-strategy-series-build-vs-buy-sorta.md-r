Build vs. buy is an often lamented and always hotly debated question in all aspects of IT, however, if one is able to truly look at all angles the answer is typically straightforward and can be rooted in one simple strategy: don&#8217;t reinvent the wheel.

<h1 style="text-align: center;">
  Don&#8217;t reinvent the wheel
</h1>

Too many times we as an industry don&#8217;t do our homework &#8211; we are all guilty of it &#8211; and we reinvent a wheel. Make no mistake, there are true reasons to revisit, revise and reinvent. Lets use an example that [I](https://github.com/buraglio/pfrancid) [am](https://github.com/buraglio/vdxrancid) [fairly](https://github.com/buraglio/alurancid) [familiar](https://github.com/buraglio/sonrancid) [with](https://github.com/buraglio/cienarancid): RANCID

[RANCID](http://shrubbery.net/rancid/) code is 20+ years old and pretty messy. RANCID3 is a rewrite that in my opinion makes the already confusing ball of Perl, Expect, and shell even more confusing. [Oxidized](https://github.com/ytti/oxidized) made that process more elegant and arguably more flexible and extensible. That was a good call. Build vs buy is a tough question and as an industry we tend to think about resources in a lopsided way, which further increases that complexity. Resources have always been and will always be finite, and no matter if you build or buy, you are expending your resources. Lets break down the resources:

  * Time

That&#8217;s pretty much the extent of it. Everything else is driven by this. Time coasts money. It costs money in the form of salaries, overtime, downtime, etc. In IT we describe things in terms of uptime. Five 9&#8217;s is the uptime we strive for. When we have downtime, it costs money in the form of lost income or expense to repair and often both. Salaries are paid based on time, hourly, weekly, monthly, yearly. Employes trade their time for that salary regardless of how it is structured.

You pay for resources that make more efficient use of time. Employers often fall into one of two buckets:

  * Able to hire FTE (OPEX)
  * Able to pay vendors (CAPEX)

Obviously this isn&#8217;t always the case, but it&#8217;s very common &#8211; and if we conveniently overlook those environments that are jut to conservative to consider OPEX (i.e. they always choose buy and generally fall into the &#8220;able to pay vendors&#8221; category), it&#8217;s fairly easy to map build vs buy into those models. Can you support running open source or white box solutions, operationally? Will the OPEX actually save you money when compared to the CAPEX changes they require to make happen? Should you pay for an off the shelf solution and hope that the support you buy can address the issues you&#8217;ll have? [_My strong opinion is that they almost never can, but the comfort that they provide to legal departments and C level execs is what they actually purchase_]

It is important to note that different environments introduce very different edge cases, and with many highly technical people, these edge cases have a tendency to creep in and drive a large part of our architectures, but it also gives us a veneer over our needs and requirements process that makes it easier to say &#8220;we&#8217;re special and we have hard requirements for not only A and B but also C, D, E and F&#8221;. C, D, E, and F are likely so edge case that we really don&#8217;t \*need\* them. This is where It gets messy and where the hyperscalers have done it right:

Say no.

<center>
</center>

[via GIPHY](https://giphy.com/gifs/reactionseditor-3o7btT1T9qpQZWhNlK)

Interdomain multicast? Nope. Requirements for full global tables on every device? Nope. If we really ask ourselves if the requirements are actually requirements or if they are simply desirable because they may make things easier or may satisfy a 5-10% use use case, then maybe we should revisit how we&#8217;re actually developing our needs and requirements. Mapping business (or other strategic) requirements into technology can be difficult, especially if there is no direct correlation to profit or loss.  
We are a culture of wheel inventors and we embrace it, but 80-85% of the time our wheels can be dead simple and still roll us where we need to go. **_What we get &#8220;for free&#8221; with that is standardization and ease of management_** (lower CAPEX).  
If we look back at history as an example, no sane person wants to run a network that routes AppleTalk, IPX, IPv4, IPv6 and transits DECNet. that sucked. It was too complicated. It was buggy. We simplified it down to IPv[4/6] and low and behold most of the gear got more stable, configurations got simpler, and networks got easier to run. We should learn from that.

Make no mistake, I realize that reinventing wheels to make them roll faster, longer, etc. is called innovation. However, along with our needs and requirements we need to put serious consideration into our business strategy. Is our business to innovate? Are we going to see direct or indirect improvements to CAPEX or OPEX if we _do_ innovate. Are we factoring in the _cost_ of the innovation? Where this starts to get even more fuzzy is in the opensource world. In this space &#8220;build&#8221; can be defined as self supporting, meaning &#8220;use of opensource products with no formal or contractual support structure&#8221;, which a very large amount of organizations are very wary of (and many actively avoid). These are all important questions that must be addresses when deciding on the strategy of build vs buy &#8211; it&#8217;s not as straight forward and simple of a question as &#8220;build or buy&#8221;, it seems.

If you&#8217;re looking for a different perspective on a very similar topic, check [Russ White](https://rule11.tech)&#8216;s (yes, [THAT Russ White](https://www.linkedin.com/in/riw777/)) post on [Enterprise vs. Provider](https://rule11.tech/enterprise-versus-provider/). While not entirely similar, it points out that we have problems and solutions, and that knowing what both of those are is critical to success regardless of their ecosystem. This is key. We need to look at the whole picture.

_<span style="text-decoration: underline;">My take</span>: We need to look at the entire picture. It&#8217;s not as simple as one question. Personally I tend to lean more toward build, but for the majority of my career I was in environments that had extremely clued engineers and support staff. Is this for everyone? Nope. Is it a viable option, absolutely. You invest in people or you invest in contracts. I&#8217;d rather invest in really, really good people. _

_When it comes down to innovation, it&#8217;s a little more complicated:_

_1. if wheel exists don&#8217;t build wheel._  
 _2. If the wheels aren&#8217;t exactly the shape or size you need, augment the wheels and contribute your augmentations back for review and inclusion in the wheel plans and inventory where possible and appropriate._  
 _3. If the wheels don&#8217;t exist, build a wheel and share the plans for the wheel whenever you can._

<pre><span style="font-family: monospace, monospace;">#!/usr/bin/python</span>

if wheel == 'yes':
 print('use existing wheel')
 elseif 'yes, but incomplete':
 print("augment wheel, contribute wheel changes")
 elseif no:
 print("build wheel, share plans")
 print "Miller Time"</pre>

<span style="font-size: xx-small;">* Code is provided as-is and is likely incorrect, we take no responsibility for poor code or fallout from running said code<br /> </span>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1449" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1449" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1449" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1449" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2018/02/strategy-series-build-vs-buy-sorta/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
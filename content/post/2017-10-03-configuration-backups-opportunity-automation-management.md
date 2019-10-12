<div>
  Configuration management is a critical part of successfully and efficiently run any network. From the early days of networking there have been options for doing configuration backup. Several projects have been around for literally decades, enabling the backup of a myriad of critical network devices and providing historical archives. Many of these projects and platforms require a reasonable amount of unix experience and perhaps some development skills. I’m going to give a quick synopsis of my three favorites, these a all very different in execution but provide the same types of services &#8211; configuration backup, diff, and archive (and not much else). While this is important (you’re doing this stuff, right!?!?!)
</div>

<div>
</div>

### [Unimus](https://www.unimus.net)

<div>
  Unimius is a commercial platform (free for up to 5 devices) that runs on-premesis. It provides a very easy to use configuration and management web interface and has wonderfully &#8211; and uncommonly &#8211; responsive help and support. This platform has support for winning on windows, linux, Mac, whatever runs Java. It’s reasonably priced and has a large amount of what I call “hooks” into other things. Unimus also has some an option that is uncommon &#8211; it can back up web based equipment. Unimus has a huge amount of device support as well. I did find a few caveats which I suspect are java limitations. For example, It cannot take an IPv6 address as as a “device” and seems to fall back on v4 if the hosts are dual stacked. I also have yet to find a way to define a specific user for discovery which has resulted in some false positives as far as ssh brute force rules. I like this project quite a bit and think it has a lot of potential to do a lot more from the management perspective should they choose to do so.
</div>

####  Unimus High level

  * Java based
  * Commercial (license based on number of devices)
  * Good web interface for view and configuration
  * Cannot take a v6 address as an input device &#8211; works resolving v6 addresses
  * Multi device config diff
  * Extremely useful configuration search option
  * Multiple notification options (slack, email, etc.)

<div>
</div>

### [RANCID](http://www.shrubbery.net/rancid/)

<div>
  RANCID is the first config backup system I ever used and has been actively developed for decades. It’s written in perl, expect, and shell. I’ve written several modules for RANCID over the years and has an large install base due to it’s longevity. It has has a recent-ish re-write which has made it more scalable but has made it much harder to extend comparatively speaking. It’s also been forked several times adding things like git repo support.
</div>

<div>
  Of the network management options I’ve seen (more on that below), most of the ones not using something like NetConf are leveraging the login scripts from RANCID to do the heavy lifting.
</div>

<div>
</div>

#### RANCID High Level

  * Decent device support
  * Multiple repositories (RCS, SVN, CVS, GIT)
  * Several forks &#8211; can be confusing
  * RANCID 3 changes the architecture and syntax dramatically
  * Has a series of login scripts that are commonly leveraged for performing other actions like pushing configuration
  * Code is crufty &#8211; decades of history rolled into the text
  * Perl, Expect, and shell based
  * Web front end is an add on for viewing the chosen repository
  * Notification typically consists of email diffs
  * Code has a reasonable amount of age on it and can be a bit of a challenge to decipher

<div>
</div>

### [Oxidized](https://github.com/ytti/oxidized)

<div>
  Oxidized is an interesting project. It’s written by a very, very clued network engineer / toolsmith and has a huge amount of device support. Oxidized seems to have flexibility as one of its main driving goals &#8211; it’s crazy flexible and works extremely well. It’s written in ruby and simple setup isn’t hard at all (and is well documented). It integrates in a lot of tools such as <a href="https://www.librenms.org/">librenms</a> and <a href="https://slack.com/">slack</a>. Oxidized required a little bit of knowledge of setting up simple linux services but it feels a <em>lot</em> more modern than some of the legacy tools like RANCID. This has been my go-to for a while now.
</div>

<div>
</div>

#### Oxidized High Level

  * Ruby based
  * Extremely flexible
  * Actively developed
  * Good support
  * Great device support
  * Very modular
  * Code base is clean and streamlined
  * Notifications can be somewhat convoluted to set up

<div>
</div>

<div>
  Network Management as defined by me: Having knowledge of the network ecosystem from the packet flow to the active configuration. Leveraging this knowledge in order to push change to production network equipment either programmatically or on-demand.
</div>

<div>
</div>

<div>
  These items should all be thought of as configuration archiving tools, not as configuration management &#8211; the reason being is that by default none of them push changes. They all grab the configurations, diff against an existing stored configuration and calculate a diff, likely storing it for historical research / baseline research and triage. The lack of what I am describing as “management” is a real opportunity as there is very little available that is available out of the box that is:
</div>

<div>
</div>

<div>
  A. Multiplatform and
</div>

<div>
  B. Actually usable
</div>

<div>
</div>

<div>
  What we have here is an opportunity. An opportunity to add some level of automation or “management” into the existing configuration archiving tools. Look at the attributes of all of these tools:
</div>

  * They’re cross platform, non-vendor specific. I do not know how most people work, but in 20 years I have never worked on a single vendor network. Ever.
  * They have knowledge of some commands in each platform,
  * They’re already trusted to log in and at least read configurations meaning they’re trusted to have access and they’re trusted to know and save the configuration.
  * At least one of them has been historically used to prop up home grown management tools

<div>
</div>

<div>
  This seems self evident. Adding some rudimentary ability to make simple changes to network equipment is a good start.
</div>

<div>
  This could be something as simple as  setting an NTP server or creating a VLAN, but if any of them were to start wrapping these into supported code, make it easy to set up, and easy to use, we’d be well on our way to having “automation for the rest of us”. Once things are trusted enough to make the change the next logical step is allowing those changes to happen autonomously. NTP server deviate from the norm? Change it automatically. This can also be leveraged as a baseline deviation outdoing tool with the integration of a simple “source of truth” for common attributes. The opportunities are ripe and ready to be picked.
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1412" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1412" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1412" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1412" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2017/10/configuration-backups-opportunity-automation-management/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

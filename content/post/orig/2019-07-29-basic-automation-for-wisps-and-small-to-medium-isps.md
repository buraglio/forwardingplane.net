Small to medium ISPs are an interesting phenomenon. Early in my career I was pretty heavily involved in that space, so much of my current thought processes and methodologies are heavily informed by that experience. Something that never ceases to amaze me today is that the practice of scripting and “automating” things seems to have become somewhat of a lost art, or at the very least it is not part of an initial deployment plan. As I learned to operate a network at scale and with efficiency, we used a significant amount of perl to automate repetitive tasks such as user creation for ppp profiles, provisioning DSL CPE, checking status of PRI and ATM VPCs, etc.

In the many years that have passed since my introduction to ISP architecture and operation, the internet has gone from a luxury item to a required utility. In this lapsed time, specialization in networking has become far more prevalent and the generalist role has been significantly diminished. With that specialization and commoditization of IT, the prevalence of the network engineer that could write code became more and more uncommon.

Then came “automation”. As we realized that the ubiquitous nature of IT systems and services was only going to increase, automation platforms and companies operating those platforms started to spring up. No longer was there a need to learn hardcore perl, python, shell programming. There were frameworks such as [cfengine](https://cfengine.com/), [puppet](https://puppet.com/), [salt](https://www.saltstack.com/), and [ansible](https://www.ansible.com/) that could abstract some of that away and provide significant functionality in addition.

I did extensive work with cfengine and did production deployments of salt. In addition, I was around for production deployments of puppet, but it wasn’t until I played with Ansible a few years ago that I got really interested in the automation space &#8211; but not really automation, per se. It was far more interesting to me to work on orchestrating workflows. Ansible was perfect for this due to its extreme flexibility and its ability to natively talk to network hardware. So I wrote some Ansible. Then I was informed that my ansible was poor form (which it definitely was). At that point I spent some time learning and playing. Then other things came along and I set it aside for a few years. Well, this past month my interest has ben re-ignited (mainly due to the inclusion of a [mikrotik routeos ansible module](https://docs.ansible.com/ansible/latest/network/user_guide/platform_routeros.html)). I spent some time with my [local ansible guru](https://twitter.com/samoehlert) and he taught me the best practices and from there I was off to the races. After a bit of re-education, I have compiled a few very simple ansible roles and playbooks focused mostly on the WISP world (because I have a lot of this type of gear in my lab), but I fully expect to expand on them greatly as they are all part of a larger bunch of orchestration parts that I have been writing at night and in my free time. Until then, please feel free to use, modify, or provide patches / input for what I have published thus far.

<img style="display: block; margin-left: auto; margin-right: auto;" title="transparent-ansible-logo.png" src="https://www.forwardingplane.net/wp-content/uploads/2019/07/transparent-ansible-logo.png" alt="Transparent ansible logo" width="361" height="281" border="0" /> 

[mikrotik-armor](https://github.com/buraglio/mikrotik-armor)  
Simple Ansible role and playbook to harden a Mikrotik RouterOS device

[upgrade-mikrotik-routeros](https://github.com/buraglio/upgrade-mikrotik-routeros)  
Simple Ansible playbook and role for setting a software channel and upgrading RouterOS on mikrotik devices

[ubnt-airos-tshaper](https://github.com/buraglio/ubnt-airos-tshaper)  
Ansible playbooks to enable and configure the traffic shaper on Ubiquity AirOS CPE

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1693" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1693" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1693" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1693" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2019/07/basic-automation-for-wisps-and-small-to-medium-isps/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

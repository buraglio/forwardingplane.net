---
id: 1066
title: 'BigSwitch Labs for SDN learning: a sneak peek!'
date: '2014-09-22T04:24:34-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1066'
permalink: /2014/09/22/bigswitch-labs-for-sdn-learning-a-sneak-peek/
themeblvd_noindex:
    - 'true'
themeblvd_keywords:
    - 'BigSwitch networks, SDN, Openflow, floodlight, SDN controller, data center, network fabric, network orchestration, juniper, cumulous networks, cloud, devops'
themeblvd_title:
    - 'Bigswitch Networks provides cloud based tools to learn SDN'
themeblvd_description:
    - 'Bigswitch Networks is piloting a beta cloud based environment for learning SDN, data center fabric and network orchestration. '
dsq_thread_id:
    - '3030377150'
Views:
    - '131'
categories:
    - 'Data Center'
    - 'Lab Time'
    - OpenFlow
    - SDN
---

I was recently granted access to the beta [BigSwitch Networks](http://www.bigswitch.com/) lab site, a purpose built classroom in the cloud focused on teaching the BigSwitch SDN environment.  I had seen some of the BSN offerings in the past and always held them in high regard, but I was thoroughly impressed with both the completeness of the lab and how polished the controller environment was.![Screenshot 2014-09-12 10.28.50](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.28.50.png)
At the time of this writing, the lab consists of 3 modules: Building cloud fabric, monitoring fabric and dynamic provisioning of monitoring fabric.  Since there is quite a lot going on with this cloud based SDN classroom, for the scope of this post I'll concentrate on the first, building cloud fabric.  I'm a big fan of the CLI*, and one thing that jumped right out to me was that they provide the GUI and the CLI, and that the CLI is familiar to anyone that has worked on an IOS device.  The lab is useful, even for someone that has done some SDN, both on production or in a lab, in that it presents the fundamentals in a way that both demonstrates the purpose and function and lays out the technology and product.
From the technology presentation standpoint, the BigSwitch offering is quite impressive.
The reality of it is that, in my experience, GUIs don't always have the most intuitive or complete implementations and they're hard to automate.  Now, from what I've seen to far the bigswitch offing is the exception to that rule.  The setup is very functional and goes through a range of great material. for comparison, below is the tenants display from the web interface:
[![Screenshot 2014-09-12 10.47.37](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.47.37.png)](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.47.37.png)
 
and the corresponding show command:
[![show tenant](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.33.49.png)](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.33.49.png)
Nevertheless, part of my usual workflow is to use one to define the other when I can.  What I mean by that is that if I don't know exactly how to accomplish my goal in the GUI, I switch to the CLI and see what I can do from there, returning to the GUI to see what has changed and then reverse engineer it from that perspective.  The opposite is also true, I have used the CLI to define the GUI *:cough:* [netscreen](http://www.juniper.net/us/en/products-services/security/netscreen/) *:cough:*. The important thing to note here, though, is that the tools all work as if it is a real environment, because it *is* a real environment.
The god among men here, really, is the *debug rest* command.  This command, when issued in the CLI (displayed below) allows the commands sent to the terminal to automatically pop up with the rest interface commands necessary to utilize them.  Wrap your head around that one for a minute.  Are you thinking automation?  Me too; seeing that made me want to go write code, and I am a horrible developer.
![Screenshot 2014-09-12 10.50.19](http://www.forwardingplane.net/wp-content/uploads/2014/09/Screenshot-2014-09-12-10.50.19.png)
In the time I've spent within this system I have been thoroughly impressed with how well it functioned.  I had no issues whatsoever with how the training presented the material, executed the commands or displayed the responses.  My only suggestion would be to add a configuration guide for the CLI =)
Below is a quick youtube video of some of the functions.
<iframe src="//www.youtube.com/embed/gBeQk0W2Cqg" width="500" height="300" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
 
* Yes, I know SDN is supposed to "kill the CLI".  I don't by the sensationalism for the short to medium term.
---
id: 45
title: 'Alcatel Lucent RANCID scripts'
date: '2010-12-06T01:06:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2010/12/alcatel-lucent-rancid-scripts/'
permalink: /2010/12/06/alcatel-lucent-rancid-scripts/
Views:
    - '322'
categories:
    - Routing
    - UNIX
---

At the [2010 Supercomputing conference](https://scinet.supercomputing.org/) this year, one of my tasks was to get [RANCID](http://shrubbery.net/rancid/) working on the Alcatel Lucent 77xx series. for some this may have been a simple task, but for me, a self taught and inefficient programmer, it was something that took some time. 
The Alcatel Lucent boxes were good performers, but their CLI is pretty awful. The prompt changes based on having unsaved configuration items, and can contain things liks an asterisk. The configuration file also displays the # symbol, a very common "enabled" router prompt, making the config a bit different to parse. I'm happy to report that the [RANCID](http://shrubbery.net/rancid/) scripts work for the ALU boxes now. for anyone that wants to use them (since I dont know if they'll be added to the base distribution), they can be found [here](http://www.buraglio.com/scripts/alurancid/).
SVN of this and some other things I hacked into RANCID for the Nexus and the CRS can be found [here](http://buraglio.com/dev/).
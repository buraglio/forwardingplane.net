---
title: 'Alcatel Lucent RANCID scripts'
date: Mon, 06 Dec 2010 07:06:00 +0000
draft: false
tags: [Routing, UNIX]
---

At the [2010 Supercomputing conference](https://scinet.supercomputing.org/) this year, one of my tasks was to get [RANCID](http://shrubbery.net/rancid/) working on the Alcatel Lucent 77xx series. for some this may have been a simple task, but for me, a self taught and inefficient programmer, it was something that took some time.  
The Alcatel Lucent boxes were good performers, but their CLI is pretty awful. The prompt changes based on having unsaved configuration items, and can contain things liks an asterisk. The configuration file also displays the # symbol, a very common "enabled" router prompt, making the config a bit different to parse. I'm happy to report that the [RANCID](http://shrubbery.net/rancid/) scripts work for the ALU boxes now. for anyone that wants to use them (since I dont know if they'll be added to the base distribution), they can be found [here](http://www.buraglio.com/scripts/alurancid/).  
SVN of this and some other things I hacked into RANCID for the Nexus and the CRS can be found [here](http://buraglio.com/dev/).

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
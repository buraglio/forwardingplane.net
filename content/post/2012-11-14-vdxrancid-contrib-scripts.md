---
id: 1710
title: 'VDXrancid contrib scripts'
date: '2012-11-14T16:50:00-06:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2012/11/vdxrancid-contrib-scripts/'
permalink: /2012/11/14/vdxrancid-contrib-scripts/
blogger_blog:
    - www.forwardingplane.net
blogger_author:
    - 'Nick Buraglio'
blogger_permalink:
    - /2012/11/vdxrancid-contrib-scripts.html
geo_latitude:
    - '40.6875665'
geo_longitude:
    - '-111.9335262'
geo_address:
    - 'Palace Way, West Valley City, UT, USA'
dsq_thread_id:
    - '3678950651'
Views:
    - '200'
categories:
    - Routing
---

   For the <a href="http://www.supercomputing.org/" target="_blank" rel="noopener noreferrer">Supercomputing 2012</a> show, as in years past, I was "the guy who installed and maintained <a href="http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&ved=0CEsQFjAC&url=http%3A%2F%2Fwww.shrubbery.net%2Francid%2F&ei=tcWjUOG2AeLCigK4qIGwBw&usg=AFQjCNGsMF1HpROC2BrtIXWL8thUtOKFLQ&sig2=CYLx8RCrdMSiuRuBjPrnaQ" target="_blank" rel="noopener noreferrer">RANCID</a>" as part of my duties for the <a href="http://scinet.supercomputing.org/" target="_blank" rel="noopener noreferrer">SCinet</a> routing team.   If you don't know about RANCID for change management and config back up, check the link.  It's ree and works on a huge amount of gear.  Every year there is a new and interesting platform, this year is was<a href="http://www.juniper.net/us/en/products-services/switching/qfx-series/" target="_blank" rel="noopener noreferrer"> Juniper qfabric</a> and <a href="http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CGIQFjAB&url=http%3A%2F%2Fwww.brocade.com%2Flaunch%2Fcloud-clarity%2Fsolutions-technology-innovation.html&ei=J8ajUOD3Ga3riQLpz4A4&usg=AFQjCNFpE2c-kkCHlqabJFwWu7opXzFiSg&sig2=fEcSzMl2PcCa4ajD-YnMvQ" target="_blank" rel="noopener noreferrer">Brocade VDX</a>.  The Juniper qFabric just worked with the existing jrancid pieces. <br /><br /><div style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/-BtfOWZ0KMHc/TyxvtyBEBYI/AAAAAAAAHc8/xue7_Nqj0DE/s400/Rancid+Urgg.jpg" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="200" src="http://2.bp.blogspot.com/-BtfOWZ0KMHc/TyxvtyBEBYI/AAAAAAAAHc8/xue7_Nqj0DE/s200/Rancid+Urgg.jpg" width="164" /></a><a href="http://webobjects2.cdw.com/is/image/CDW/2273816?$product_large$" style="clear: right; float: right; margin-bottom: 1em; margin-left: 1em;"><img border="0" height="200" src="http://webobjects2.cdw.com/is/image/CDW/2273816?$product_large$" width="200" /></a><a href="http://upload.wikimedia.org/wikipedia/commons/3/35/Plus_sign.jpg" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="165" src="http://upload.wikimedia.org/wikipedia/commons/3/35/Plus_sign.jpg" width="200" /></a></div><div style="clear: both; text-align: left;">    The brocade VDX is different enough that it doesn't work with francid, but was very similar to IOS.  I did some very minor modifications to the original rancid to make it work with the VDX.  The google code page is available <a href="http://bit.ly/vdxrancid" target="_blank" rel="noopener noreferrer">here</a> and the source code is available <a href="http://bit.ly/vdxrancid-source" target="_blank" rel="noopener noreferrer">here</a>.  </div>  You'll have to modify the rancid-fe script to make it work, or use the included one with the source.  It's still very rudimentary, no VCS or platform information is being collected, just the config as of 11/14/2012. <br /><br /><div>[[ This is a content summary only. Visit my website for full links, other content, and more! ]]</div>
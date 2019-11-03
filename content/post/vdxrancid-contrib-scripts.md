---
title: 'VDXrancid contrib scripts'
date: Wed, 14 Nov 2012 16:50:00 +0000
draft: false
tags: [Routing]
---

   For the [Supercomputing 2012](http://www.supercomputing.org/) show, as in years past, I was "the guy who installed and maintained [RANCID](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&ved=0CEsQFjAC&url=http%3A%2F%2Fwww.shrubbery.net%2Francid%2F&ei=tcWjUOG2AeLCigK4qIGwBw&usg=AFQjCNGsMF1HpROC2BrtIXWL8thUtOKFLQ&sig2=CYLx8RCrdMSiuRuBjPrnaQ)" as part of my duties for the [SCinet](http://scinet.supercomputing.org/) routing team.   If you don't know about RANCID for change management and config back up, check the link.  It's ree and works on a huge amount of gear.  Every year there is a new and interesting platform, this year is was [Juniper qfabric](http://www.juniper.net/us/en/products-services/switching/qfx-series/) and [Brocade VDX](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CGIQFjAB&url=http%3A%2F%2Fwww.brocade.com%2Flaunch%2Fcloud-clarity%2Fsolutions-technology-innovation.html&ei=J8ajUOD3Ga3riQLpz4A4&usg=AFQjCNFpE2c-kkCHlqabJFwWu7opXzFiSg&sig2=fEcSzMl2PcCa4ajD-YnMvQ).  The Juniper qFabric just worked with the existing jrancid pieces.  
  

[![](http://2.bp.blogspot.com/-BtfOWZ0KMHc/TyxvtyBEBYI/AAAAAAAAHc8/xue7_Nqj0DE/s200/Rancid+Urgg.jpg)](http://2.bp.blogspot.com/-BtfOWZ0KMHc/TyxvtyBEBYI/AAAAAAAAHc8/xue7_Nqj0DE/s400/Rancid+Urgg.jpg)[![](http://webobjects2.cdw.com/is/image/CDW/2273816?$product_large$)](http://webobjects2.cdw.com/is/image/CDW/2273816?$product_large$)[![](http://upload.wikimedia.org/wikipedia/commons/3/35/Plus_sign.jpg)](http://upload.wikimedia.org/wikipedia/commons/3/35/Plus_sign.jpg)

    The brocade VDX is different enough that it doesn't work with francid, but was very similar to IOS.  I did some very minor modifications to the original rancid to make it work with the VDX.  The google code page is available [here](http://bit.ly/vdxrancid) and the source code is available [here](http://bit.ly/vdxrancid-source).  

  You'll have to modify the rancid-fe script to make it work, or use the included one with the source.  It's still very rudimentary, no VCS or platform information is being collected, just the config as of 11/14/2012.  
  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]
---
title: 'BGP RPKI - why aren''t we using it more?'
date: Sat, 21 May 2016 16:33:44 +0000
draft: false
tags: [Musings, Routing, Security]
---


#### 
[SilentLennie]( "disqus@consolejunkie.net") - <time datetime="2016-05-21 16:40:00">May 6, 2016</time>

It's almost always the organisational part that is the hard part. Look at DNSSEC, the technical part is easy to deploy these days: see PowerDNS for example. Now getting someone in your organisation to deal with DS-record and know what to do when migrating a domain... well, that's a whole process, that's the difficult part of the story. I do however believe it could be simpler though. At least part of it could be automated. Just look at the APIs that are available at top-level-domains. Problem is: most organisations are not direct members/customers/whatever of the top-level-domains. They have a middle man. The registrar. They need to have an automated process with a customer-API as well, many do not. And standardization doesn't seem to exist either.
<hr />
#### 
[Paul Vixie](http://www.farsightsecurity.com "paulvixie@gmail.com") - <time datetime="2016-05-22 17:08:00">May 0, 2016</time>

there's a cost/benefit planning error, similar to DNSSEC. if you deploy BGP RPKI in "hard mode" where correct signatures aren't merely a BGP priority echelon but are \*required\* for a route to make into your FIB, then any time somebody somewhere FUBARs their keys or signatures, they will be unreachable to you. your competitors will, on those days, operate more reliable networks. so (and this again parallels the DNSSEC case) you're left looking at the risks of deploying vs. not. if you deploy, there will be N FUBARs during which your network will be less reliable than your competitors'. if you do not deploy, there will be M attacks in which someone somewhere won't receive all of their own traffic but you and your competitors will be equally unable to reach that victim's network that day. and in any case N is at least an order of magnitude higher than M, and always shall be. the best case scenario is a significant last-mover advantage, wherein we all jostle each other to be the last one into the burning building, but we all get in there eventually, for reasons never feel. there never was a strategic global business plan for RPKI|DNSSEC|IPV6 deployment. we're winging it.
<hr />
#### 
[Doug Montgomery]( "dougm.work@gmail.com") - <time datetime="2016-05-23 06:51:00">May 1, 2016</time>

While in general I agree that what is required are intelligent / mature implementations that mitigate the risk and complexity of deployment / use (I think we are only just getting there with some DNSSEC products), I would like to note that the risk of error here is slightly different than DNSSEC. I have yet to see a RPKI origin validation policy mechanism that is the equivalent of "require valid". Hard mode in RPKI OV is "ignore invalid". FUBARing your own ROA doesn't automatically make your route invalid. It requires another valid ROA created by you or your parent bound to a different origin (or with shorter maxlength than your announcement). If this other covering ROA is for a route that your downstreams receives, even there, all you end up with is an alternate route. Again, fully agreeing that a great deal of focus needs to be given the the robustness, transparency, and security of the underlying trust infrastructure ... just pointing out that shooting yourself in the foot is not as easy, or at least different, than in some other technologies.
<hr />
#### 
[dwcarder]( "dwcarder@wisc.edu") - <time datetime="2016-05-25 14:16:00">May 3, 2016</time>

I have always had a hard time summarizing my thoughts on crypto, but this is a good summary: It's not the crypto, it's all the bad practices that end up surrounding it. I heard about this I think from the main ietf list: http://www.cs.auckland.ac.nz/~pgut001/pubs/crypto\_wont\_help.pdf and I \*think\* this is the same talk: https://www.youtube.com/watch?v=\_ahcUuNO4so There's truth above that would apply to rpki. Sharon Goldberg has done a lot of work here and I share that concern for maleficent actors in a trusted root hierarchy system. There's related concerns at the RIR level wrt how one uses arin's HSM and such. It's not the crypto.
<hr />

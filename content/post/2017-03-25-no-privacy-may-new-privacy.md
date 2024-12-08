---
id: 1389
title: 'No privacy may be the new privacy.'
date: '2017-03-25T12:06:01-05:00'
author: buraglio
layout: post
guid: 'http://www.forwardingplane.net/?p=1389'
permalink: /2017/03/25/no-privacy-may-new-privacy/
dsq_thread_id:
    - '5665362677'
Views:
    - '105'
categories:
    - 'Crystal Ball'
    - Musings
    - Security
    - 'Soap Box'
---

Taking politics and putting them aside, what the new administration has <a href="https://www.nytimes.com/2017/03/23/technology/congress-moves-to-strike-internet-privacy-rules-from-obama-era.html?_r=0">been attempting to change</a> with regard to internet privacy is something we should <em><strong>all</strong></em> be informed about. Wether you have a tin foil hat or don't care, "knowing is half the battle". The other half is doing - which I will also lend some brief insight to (sorta).
What's changing? Nothing yet (as of the time of this writing). What will likely change? The ability of your internet (mobile or not) to sell your browsing habits and personal usage data. What does this mean? Well, it means that if you visit facebook, amazon, JC Penny, or buy-adult-toys.com a lot, that information can be sold to advertisers, private companies, etc., etc. "But I use SSL, I'm safe". Nope. DNS query data - the requests made for a domain name like google.com, used to map a name to an IPvX address - that can be sold too. The content of the browsing is great, but the knowledge that a site was visited is just as useful...and this data is generated not just by traditional "browsing", everything that touches the internet uses it. Apps, Games, everything. Removing these rules also means that there is no oversight into how this collection can be done, what kind of data - sensitive or not - can be collected and sold and to whom.
That's what deregulation looks like, folks.<a href="http://www.forwardingplane.net/wp-content/uploads/2017/03/personal.info_.jpg"><img class="alignright size-full wp-image-1394" src="http://www.forwardingplane.net/wp-content/uploads/2017/03/personal.info_.jpg" alt="" width="299" height="299" /></a>
What does this mean for the average internet user like, say, my Mom or Dad? It means that when they look at ANYTHING online, it's likely going to be collected, indexed, data mined, and then sold to be further data mined and then these users will get targeted for a barrage of advertising. Worse yet, this data is ripe for misuse. What if the data is compromised? Sorry. That'll suck for sure. Even worse that than, what if that data is used by nation states? What if it's misinterpreted? It's a mess.
Has this data been used in this manner in the past? Sure. All of the providers use it internally. <a href="http://money.cnn.com/2016/07/25/technology/yahoo-verizon-deal-sale/">Verizon bought yahoo</a> for this reason.  The real issue is that most people do not understand what all of this means. Since the internet is a completely traceable environment in 99.999% of cases, unlike really anything prior, this is paramount.
What can you do? Well, if you're not technical, good luck. Perhaps if this happens it will spark a new industry of private overlays like Tor to be commercialized and widely adopted. Wait with the FCC leaning toward rolling back net neutrality those services could likely be slowed or blocked completely. Sorry. On the fringes are the mom-and-pop ISPs - they still exist. WISPs, small and rural providers. These are less likely to be the safest bet in the future should this come to pass. Mobile metadata - what will generate the majority of the controversy - is likely to be the most often sold because there will be such a diverse and deep pool of data.
Another of the side effects is this could potentially be an even higher adoption of SSL, which is good, but may also lead to a higher adoption of the vile SSL decryption practice. Lets hope not.
What will I do? Not sure. I have extensive experience running DNS servers and VPNs. I may just start connecting to one of my VPS devices and run everything over OpenVPN from both mobile and traditional connections. There are some super simple <a href="https://github.com/kylemanna/docker-openvpn">docker how-tos</a> out there that Ive used in the past. VPS service are cheap, I have a few but my <a href="https://prgmr.com/xen/">prgmr.com</a> VPS is my favorite. Don't forget to tunnel IPv6 too.
Welcome to 2017.
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
---
title: 'A missing link in small MPLS, 10G devices.'
date: Fri, 29 Mar 2013 04:43:17 +0000
draft: false
tags: [IPv6, Musings, Routing]
---

Lately I've been lamenting the fact that there seems to be a lack of options in a very specific product level.  Lets say you have a network that looks like this:   [![10G-Bldg](http://www.forwardingplane.net/wp-content/uploads/2013/03/10G-Bldg1.jpg)](http://www.forwardingplane.net/wp-content/uploads/2013/03/10G-Bldg1.jpg)Right Away you're limited since you need MPLS and more than 2 10G interfaces. Even more so if you require full support for IPv6 and ISIS. If budget is of any concern, you're in real trouble. For many, Cisco pricing and smartnet is potentially going to exclude anything reasonable from them.  There are a substantial amount of non-enterprise folks out there that can't afford the significant Cisco price tag but need the features.  I am here to say, this is a problem.  The attitude of "if you want the best you have to pay for it" doesn't apply.  There is a real need for viable alternatives, not just because we need them, but because competition is a good thing for everyone. Juniper has the MX80, but it has a carrier grade price tag as well.  Juniper has limited MPLS support on the EX series, but the EX4200, which is arguably the most tried and true, has only 2 ports of 10G and, as mentioned, limited MPLS support.  The EX4500 is a tad better with its huge amount of 10G ports, but it has the same limited MPLS support and a crippled ARP and FIB table.  The 4550 with it's single PFE sounds exciting but it has even less. Then you have the Brocade CES/R.  It is close.  The newer version has  4 x 10G ports, MPLS support (with a license), more appropriately priced support and, as a value add, very good OpenFlow support.  It is still limited as far as 10G scalability, so adding more access switches could be problematic. HP has some great products in the Procurve series.  They're inexpensive, rock solid and packed with features. Unfortunately, the ones that meet the port density are fairly good sized chassis and none of them have MPLS.  Now, they do have an intriguing line up in the H3C series.  I believe there may be an option there, however, I have no idea on pricing and have yet to see one actually do MPLS (although they claim support).  I'm cautiously optimistic. Then you have Alcatel Lucent.   They do MPLS, they're carrier devices.  They offer a 1U ( ([7210 Service Access Switch](http://www.alcatel-lucent.com/products/7210-service-access-switch)) device but I have no idea on cost and I'm still looking for 10G port density.  I suspect it is very reasonable.  Their [CLI is a bit different](http://www.forwardingplane.net/2010/12/alcatel-lucent-rancid-scripts/ "Alcatel Lucent RANCID scripts") but they're very robust devices.  I've not used any but the 7750, so I cant comment as to how the smaller ones look.  It's a possibility if it has the 10G ports. Arista is very close but they fall short on the MPLS support.   The primary take away from this commentary is that there are not a lot of options that meet the following criteria:

*   1-2U
*   \> 4 10G ports
*   MPLS
*   Dual power supplies
*   \> 16,000/4,000 IPv4/IPv6 routes
*   IPv6 support
*   ISIS
*   40G uplink
*   OpenFlow support or roadmap
*   **Reasonably priced**

I keep coming back to the old adage of "Cheap, Fast, Reliable.  Pick Two" and it drives me crazy.  We should have more options but I don't think we do.  I would absolutely **love** to be wrong, but every time I look at this I feel like I am picking out a cell phone plan.  The affordable ones are never quite enough and the plan above is overkill and too expensive.
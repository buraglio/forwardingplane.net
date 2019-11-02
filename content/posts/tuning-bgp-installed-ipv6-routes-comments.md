---
title: 'Tuning BGP installed IPv6 routes'
date: Sat, 02 Mar 2013 13:15:37 +0000
draft: false
tags: [How-To, IPv6, Routing]
---


#### 
[Tyler Christiansen](http://labelswitched.blogspot.com/ "tyler.christiansen@outlook.com") - <time datetime="2013-03-02 07:49:24">Mar 6, 2013</time>

So what happens when the circuit to the one transit provider providing a default IPv6 route drops? Or if instability is otherwise introduced?
<hr />
#### 
[Nick Buraglio](http://www.forwardingplane.net "nick@buraglio.com") - <time datetime="2013-03-02 08:43:44">Mar 6, 2013</time>

That is a known limit. One could have default from >1 provider or not have had to do this in the first place, ideally. In this particular instance, there is only one provider that can truly give default (cogent isn't a full v6 table regardless of what they say) and the rest are close but not full. We ran with essentially a bilateral v6 mesh for a table or years before our transit providers offered v6 and never really experienced issues. Its not ideal, I agree, but as the v4 table grows and shared FIB hardware remains the same, more and more gear is going to run out of resources. This is a problem with the v6 net at large, unfortunately.
<hr />

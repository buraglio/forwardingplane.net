Have you ever needed to replicate a lot of data transparently to an IDS without the use of a rack of optical taps?  Not enough budget for a Gigamon or cPacket?  Have a spare MLXe laying around?  you&#8217;re in luck, we were in that boat too.

Let me first preface this by saying that this would be fairly trivial using OpenFlow / SDN.  That being said, we didn&#8217;t have the time to set that up, so this is what we came with.

<div style="clear: both; text-align: center;">
  <a style="margin-left: 1em; margin-right: 1em;" href="http://3.bp.blogspot.com/-dkBh5cQqBtc/UKPe167KFsI/AAAAAAABbFY/5DP_E2YVWgg/s1600/TransHWFlood.jpg"><img style="border: 0px;" src="http://3.bp.blogspot.com/-dkBh5cQqBtc/UKPe167KFsI/AAAAAAABbFY/5DP_E2YVWgg/s640/TransHWFlood.jpg" alt="" width="407" height="149" border="0" /></a>
</div>

This would also work using an input interface of 100G, but of course the flows would be limited to 10G.

How this works is pretty simple, it just uses a policy based route to direct the flow of traffic out of the desired aggregate interface.  In this real world use case that this was built for, the destination was a Bro cluster, consuming as much of the data as possible.  The config on a brocade is pretty similar to Cisco IOS if you&#8217;re not familiar, but the VLAN bits are a tad different (actually more intuitive in my opinion).  Here are the bits to make all of this work:

Create the vlans and tag them appropriately

<div style="text-align: left;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 15px; text-indent: -24px; vertical-align: baseline;">mlxe8# </span><span style="letter-spacing: 0pt; line-height: 15px; text-indent: -24px; vertical-align: baseline;">conf</span><span style="letter-spacing: 0pt; line-height: 15px; text-indent: -24px; vertical-align: baseline;"> t</span></span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">mlxe8(</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">config</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">)# </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">vlan</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;"> 100</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">mlxe8(config-vlan-100)# </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">un</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">tag </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">ethernet</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;"> 1/1</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">(config-vlan-100)# transparent-hw-flooding</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">mlxe8(config-vlan-100)# router-interface ve 100</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">mlxe8(</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">config</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">)</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;"># </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">vlan 101</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">mlxe8(config-vlan-101)# </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">untag </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">ethernet</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;"> 4/1</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">&#8230;</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">mlxe8(config-vlan-101)# </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; line-height: 95%; text-indent: -0.25in;">untag </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">ethernet</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;"> 4/10</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">mlxe8(config-vlan-101)# router-interface </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;">ve</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in; vertical-align: baseline;"> 101</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">(config-vlan-101)#</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">exit</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in; vertical-align: baseline;">mlxe8(</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in; vertical-align: baseline;">config</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in; vertical-align: baseline;">)#</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">interface </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">ve</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;"> 100</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">(config-vlan-100)#</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">ip</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;"> policy route-map PBR-TRAFFIC</span><br /> <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">(config-vlan-100)#</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">ip</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;"> access-group </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">pbr</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">-traffic-acl</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">(config-vlan-101)#exit</span></span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">(config)#</span>interface ve 101</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">(config)#</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">ip</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;"> address 10.101.101.1/24</span></span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: inherit;">Enable all of the interfaces.</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; font-size: small; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span>interface ethernet 4/1</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">enable</span></span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><br /> </span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;">&#8230;</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><br /> </span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span>interface ethernet 4/10</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;"><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">enable</span></span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;"><br /> </span>
</div>

<div style="direction: ltr; font-size: small; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-align: left; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: inherit; font-size: small;">Create the LAG.</span>
</div>

<span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;"><br /> </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)# lag </span><span style="font-family: Courier New, Courier, monospace; font-size: x-small; text-indent: -0.25in;">“IDS” static</span>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">   mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 95%; text-indent: -0.25in;">ports ethernet 4/1 to 4/10</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">   mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">primary-port 4/1</span>
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">   mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">deploy</span></p> 
  
  <div style="font-family: Times; font-size: medium;">
    <span style="font-family: Courier New, Courier, monospace; font-size: x-small;">s</span>
  </div>
  
  <div style="font-family: Times; font-size: medium;">
    <span style="font-size: 16px; line-height: 15px;">     Create the PBR ACL bits. This can also be done to filter types of traffic using more complex ACLs  if so desired</span>
  </div>
  
  <div style="font-family: Times; font-size: medium;">
    <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">   </span>
  </div>
  
  <p>
    <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;"><span style="font-family: Times; font-size: small;">  </span>  mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small; text-indent: 0px;">access-list </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">pbr</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">-traffic-acl</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small; text-indent: 0px;"> permit ip any any</span>
  </p>
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#exit</span>
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">route-map PBR-TRAFFIC permit 1</span>
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt;">match</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt;"> </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt;">ip</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt;"> </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt;">address </span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">pbr</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">-traffic-acl</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt;"> </span>
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">mlxe8</span><span style="font-family: 'Courier New', Courier, monospace; font-size: x-small; letter-spacing: 0pt; line-height: 12px; text-indent: -0.25in;">(config)#</span><span style="font-family: Courier New, Courier, monospace; font-size: x-small;">set ip next-hop 10.101.101.1</span>
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; font-size: medium; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: inherit; letter-spacing: 0pt;">Create a static ARP entry to tie it all together. </span>
</div>

<div style="direction: ltr; line-height: normal; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: 0px; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; margin-bottom: 0pt; margin-left: 0.25in; margin-top: 7pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
  <span style="font-family: Courier New, Courier, monospace; font-size: x-small;">arp 10.101.101.1 c0ff.eec0.ffee ethernet 1/1</span></p> 
  
  <div style="font-size: medium;">
    <span style="font-size: 16px; line-height: 15px;"><span style="font-family: inherit;"><br /> </span></span>
  </div>
  
  <div style="font-size: medium;">
    <span style="font-size: 16px; line-height: 15px;"><span style="font-family: inherit;">That&#8217;s it, let the security folks drink from the firehose.  =)</span></span>
  </div>
</div>

<div style="direction: ltr; font-size: medium; margin-bottom: 0pt; margin-left: 0.25in; margin-top: 7pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; font-size: medium; margin-bottom: 0pt; margin-left: 0.25in; margin-top: 7pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; font-size: medium; margin-bottom: 0pt; margin-left: 0in; margin-top: 0pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: 95%; margin: 7pt 0in 0pt 0.75in; text-align: left; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: 95%; margin-bottom: 0pt; margin-left: 0.75in; margin-top: 7pt; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: 95%; margin: 7pt 0in 0pt 0.75in; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<div style="direction: ltr; line-height: 95%; margin: 7pt 0in 0pt 0.75in; text-indent: -0.25in; unicode-bidi: embed; word-break: normal;">
</div>

<!--EndFragment-->

<div>
  [[ This is a content summary only. Visit my website for full links, other content, and more! ]]
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-5" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-5" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-5" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-5" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2012/11/using-a-brocade-mlxe-as-a-replicator-to-an-ids/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

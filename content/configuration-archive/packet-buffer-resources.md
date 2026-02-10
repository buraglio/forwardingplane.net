---
title: Packet Buffer Resources
date: 2026-02-10
author: Nick Buraglio
layout: page
categories:
    - configuration
tags:
    - networking
    - buffers
    - switching
---

<table border="1" cellpadding="3" cellspacing="0" id="wp9001370table4000024">
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal;  margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Information here is by <b>rumor, innuendo and extrapolation</b>. Manufacturers used to leave info on packet buffers out of their data sheets. This situation is now much improved. Readers -- be sure to let your suppliers know that you want this info.  There are some <a href="../buffers/Bufs/summary"><b>summary thoughts</b></a></p>
</td>
</tr>
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal;  margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
The <i>buffer size</i> question discussed in 2012 on the
<a href="../buffers/Bufs/nanog-thread">nanog list</a> and is reproduced. 
<a href="../buffers/Bufs/buffer-requirements"><b>Buffer requirements</b></a> 
for long RTT networks is less well understood than you might hope. 
IETF tests for burst management are not as well developed 
as bandwidth tests. There is a 
<a href="../buffers/Bufs/draft-ietf-bmwg-dcbench-methodology-00.pdf">draft</a> 
that hints at progress. 
<a href="http://fasterdata.es.net/network-tuning/packet-pacing/">Packet pacing</a> 
can improve buffer effectiveness by making TCP less bursty. Cisco wrote a 
<a href="../buffers/Bufs/Buffering-WP_August_2017.pdf"> review of the buffer question</a> in 2017.
Geoff Huston wrote <a href="https://blog.apnic.net/2019/12/12/sizing-the-buffer/"><i>Sizing the Buffer</i></a>,
a review published as a blog entry in 2019.

</td></tr>
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal;  margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
Packet buffers and switch performance have shown steady improvement. This <a href="../buffers/Bufs/buf-hist.html"><b>table</b></a> attempts to show this for ASICs with integrated packet buffers and why using crufty old stuff is at your peril.
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal;  margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<a href="../buffers/Bufs/incast.html"><b>Incast</b></a> is a buffer exhaustion phenomena that is one consequence of running out of packet memory.
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<b>Shared memory</b> means that the hardware permits buffers to be used by any port that needs them.
An <a href="../buffers/Bufs/intel-memory-efficiency-paper.pdf">intel white paper</a> 
compares shared memory with other architectures.
In a shared memory design it is not possible to let ALL the memory go to queued packets.  
There would be no room for new arrivals which would lead to head of line blocking. The other major option for a switch fabric is a 
<a href="../buffers/Bufs/crossbar.html"><b>crossbar matrix</b></a>.</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<b>Buffer queue depth monitoring</b> cannot be done directly with SNMP MIB-II polling of the current occupancy of the buffer. 
Even if a buffer depth SNMP poll object existed it would not possible to interrogate it  on a time scale short enough to catch microbursts.  A burst that would fill a 4 MByte buffer would completely
drain in 3.2 mS at 10 Gb/s. You could hope for indirect evidence of buffer exhaustion by monitoring packet drops. 
Bursts too short to cause drops can nonetheless be long enough to affect performance.  <a href="../buffers/Bufs/queue-monitor.html">Direct queue monitoring</a> can thus add valuable information.
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
The switch entries below are organized by switch ASIC families. A Packet Pushers <a href="https://www.youtube.com/watch?v=Ti3t9OAZL3g"> video blog by Pete Lumbis</a> from October 2018 gives a refreshing overview of the evoluton of switch ASICs.
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Some switches have multiple switch ICs that each manage their own memory pool.  Examples are the Brocade FCX648S and the Cisco 3750-48.  Memory from one IC can be shared among the ports in that IC's group but cannot be loaned out to ports controlled by other switch chips. Here we are interested in queue resources that can be claimed by a single flow for burst absorption -- not the total RAM in the system.</p>
</td>
</tr>
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Tolly (tolly.com) occasionally reports on the ability of switches to sustain <a href="../buffers/Bufs/microburst"><b>microbursts</b></a> in his reports on data center switches.  These measurements relate directly to output port buffering. See esp the IBM G8264 below.</p>
</td>
</tr>
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Max buffer queue depth requires that all packet memory can be put into a single queue. QoS schemes divide buffer resources among defined queues. As such, I am not interested in the QoS descriptions and these are even less reliable than the rest of this doc.</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Model</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Port Type</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">RX Queue</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">TX Queue</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Total Buffer</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">RX Buffer</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">TX Buffer</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/trident.html">Trident+</a> Shared Memory</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/accton">Accton 5652</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5? MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/QFX3500.html">Juniper QFX3500</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Juniper-buffers.pdf">5 MB </a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista-note">Arista 7050S-64</a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB/switch</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell.html">Dell 8132F</a> &amp; 4032F</p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+ and 2 x QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dell 8164F &amp; 4064F </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent:
 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 x QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/pica8">Pica8 P-3922</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent:
 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 x QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/pica8">Pica8 P-3930</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent:
 0pt; text-transform: none" class="pChart_bodyCMT">48 10GbaseT and 4 x QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/penguin">Penguin 4804x</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent:
 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 x QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-3064">Cisco Nexus 3064X</a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/super">Supermicro SSE-X3348T</a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 10GTw-Pr and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/super">Supermicro SSE-X3348S</a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/IBM_G8264">IBM G8264</a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB/switch</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/tolly">not on data sheet</a></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-Force10-S4810-Networking-Spec-Sheet.pdf">Force10 S4810</a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Allied Telesis DC2552 </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/allied-2552">5 MB</a></p>
</td>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/NEC">NEC PF5820</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/allied-2552"></a></p>
</td>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HP">HP 5900AF-48XG-4QSFP+</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/allied-2552"></a></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5600.html">Edgecore AS5600-52X</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/allied-2552"></a></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Nexus-3048.html">Cisco Nexus 3048</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T and 4 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB <a href="../buffers/Bufs/Nexus-3048.html"> but see notes</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Brocade TOR custom </p></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade6740.html">Brocade VDX 6740</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/email-6740">Dynamic up to 8 MB</a></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/email-6740">Dynamic up to 8 MB</a></p>
</td></tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade6940.html">Brocade VDX 6940</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">96 SFP+ and 12 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/brocade-queue-limit.html">Dynamic up to 8 MB</a></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/brocade-queue-limit.html">Dynamic up to 8 MB</a></p>
</td></tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/trident2.html">Trident II and II+</a> </p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Champion.html">Champion Trident2</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">varies by model</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Lenovo-G8272.html">Lenovo G8272</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7050X">Arista 7050X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7250X">Arista 7250X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB/ASIC, 48 MB total</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Aurora420.html">netberg Aurora 420</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7250X">Arista 7300X 4/8/16 slot chassis</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 slot: 512 QSFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB/ASIC </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/brocade-7750-26Q">Brocade 7750-26Q</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">26 QSFP+ and slot</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/brocade-7750-48F">Brocade 7750-48F</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+ and expansion</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/brocade-7750-48F">Brocade 7750-48C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 10GbaseT and 6 QSFP+ and expansion</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/quanta-LY8.pdf">Quanta BMS T3048-LY8</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Pluribus-E.html">Pluribus E68</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">44 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Summit770">Extreme Summit 770</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">No info</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">No info</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Cisco3100">Cisco Nexus 3132Q </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+ <b>or</b> 31 QSFP+ and 4 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Cisco3100">Cisco Nexus 3172PQ</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S4048.html">Dell-S4048-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S6000">Dell S6000</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Juniper-5100">Juniper QFX5100-24Q</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 QSFP+ + expansion slots </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Juniper-ex4600.html">Juniper EX4600</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+ + 4 QSFP + expansion slots  </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HP-5930">HP 5930</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/hp5930.html">HP 5930 w 2 modules</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/hp5712.html">HP Altoline 5712</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/hp5712.html">HP Altoline 6712</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5712-54X.html">Accton edgecore AS5712-54X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS6712.html">Accton edgecore AS6712-32X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/supermicro-X3648.pdf">Supermicro SSE-X3648S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Inventec-D6232Q.html">Inventec D6232Q</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/wedge.html">Wedge - Facebook OCP</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12.2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 8 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/trident2.html">Trident II+</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Alpha-net.html">Alpha Networks SNX-60x0-486x</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP28 100G and 2 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/4806xp.html">Artica 4806xp</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP 40G </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Champion.html">Champion Trident2+</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><i>Three switch configurations</i> </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/T2">16 MB</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista7050X2.html">Arista 7050X2 family</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/Arista7050X2.html">see table<a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/T2">16 MB</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-s4048T.html">Dell S4048T-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> 48  10G-BASE-T and 6 x QSFP+ <a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/T2">16 MB</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S6010-ON.html">Dell S6010-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> 32 40-Gbps QSFP<a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/T2">16 MB</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Cisco3100-v.html">Cisco Nexus 3132Q-V</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP+ <b>or</b> 26 QSFP+ and 6 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/T2">16 MB</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Cisco3100-v.html">Cisco Nexus 31108PC-V</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/T2">16 MB</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/NCS5001.html">Cisco NCS5001</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 1/10-Gbps SFP+ and 4 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/NCS5001.html">Cisco NCS5002</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">80 1/10-Gbps SFP+ and 4 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS6812-32X_ONIE.pdf">EdgeCore AS6812-32X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 40-Gbps QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5812.html">Accton edgecore AS5812-54X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/huawei6855.html">Huawei CE6855-48S6Q-HI</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/huawei6855.html">Huawei CE6855-48T6Q-HI</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 10G base-T and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/altoline-6921.html">HPE Altoline 6921-54X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB??</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/juniper5110.html">Juniper QFX5110-48S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP28 100G </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/juniper5110.html">Juniper QFX5110-32Q</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 QSFP+ and 4 QSFP28 100G or 32 QSFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Dynamic up to 12 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VSP8404.html">Extreme Networks VSP 8404C 4-slot modular</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2-port 100Gb/s module, 8-port QSFP module, . . . </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/trident3.html"><b>Trident 3</b></a>  </p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7050X3.html">Arista 7050CX3-32S</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100G QSFP28 and 2 port 10 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">27 MB shared pool</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7050X3.html">Arista 7050SX3-48YC8</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">27 MB shared pool</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/RA-B6510-48V8C.html">Ragile RA-BS6510-48V8C</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">27 MB shared pool</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/celestica-seastone2.html">Celestica Seastone2 Trident3 X7</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100G QSFP28 and 2 port 10 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">27 MB shared pool</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/celestica-Questone2.html">Celestica Questone2 Trident3 X5</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">27 MB shared pool</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7326-56X.html">Edgecore AS7326-56X BCM56873</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7726-32X.html">Edgecore AS7726-32X BCM56870</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100 Gb/s</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5835.html">Edgecore AS5835-54X BCM56771</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10G SFP+ and 6 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5835.html">Edgecore AS5835-54T BCM56771</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10 GBase-T and 6 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS4630.html">Edgecore AS4630-54PE BCM56371</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 X 1000BaseT and 4 X 25 Gb/s SFP28 and 2 x 100Gb/s QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/720XP.html">Arista 720XP family</a>Trident X3</p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 and 24 port, models with uplinks and PoE (varies)</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AGV424.html">Delta/Agema AGV424 BCM56771</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 port 25 Gb/s SFP28 and 4 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/SLX9150.html">Extreme SLX9150</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/SLX9150.html">Extreme SLX9250</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100 Gb/s</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/D6356.html">Inventec D6356</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/D6332.html">Inventec D6332</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100G QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N5860.html">FS.COM N5860-48SC</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10G SFP+ and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N5860.html">FS.COM N8560-48BC</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/qfx5120.html">Juniper QFX5120-48T</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10G Tw-Pr and 6 port 100 Gb/s</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Quanta-Trident3.html">QuantaMesh BMS T4048-IX8</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Quanta-Trident3.html">QuantaMesh BMS T7032-IX7</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100G QSFP28</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/SNC-60x0-488F.html">Alpha SNC-60x0-488F</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/lenovo2580o.html">Lenovo ThinkSystem NE2580o</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 8 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/huawei6855.html">Huawei CE6857-48S6CQ-EI Trident3 X4</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10 Gb/s SFP+ and 6 100 Gb/s QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/huawei6865.html">Huawei CE6865-48S8CQ-EI Trident3 X5</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25 Gb/s SFP28 and 8 100 Gb/s QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S5212.html">Dell S5212-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 port 25 Gb/s SFP28 and 3 100 Gb/s QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S5224.html">Dell S5224-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 port 25 Gb/s SFP28 and 4 port 100G QSFP28</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S5232.html">Dell S5232-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100 Gb/s QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S5248.html">Dell S5248-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25 Gb/s SFP28 and 4 100 G QSFP28 and 2 200 G QSFP</font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S5296.html">Dell S5296-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">96 x 25 Gb/s SFP28 and 8 x  100 G QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/9032v2.html">Delta 9032v2</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100 Gb/s QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C3132C-Z.html">Cisco C3132C-Z</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100 Gb/s QSFP28 </font></p>	
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ICX7850.html">Ruckus ICX 7850-32Q</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 100 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ICX7850.html">Ruckus ICX7850-48FS</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP+ 1/10 Gb/s and 8 x QSFP28 100 G ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ICX7850.html">Ruckus ICX 7850-48F</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 1/10/25 Gb/s and 8 x QSFP28 100 G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/Trident-4.html"><b>Trident 4</b></a>  </p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7050.html">Arista 7050PX4-32S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x OSPF</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7050.html">Arista 7050DX4-32S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP56-DD </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7358x4.html">Arista 7358X4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 slot 16- and 4- port cards </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/5130.html">Juniper QFX5130</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP56-DD </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Z9432.html">Dell Z9432F-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP56-DD </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/aurora830.html">Aurora 830</a> BCM56880</p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP56-DD </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/ufiSpace-9300.html">ufiSpace S9300-32D</a> BCM56880</p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP56-DD </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">132 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/RA-B6520.html">Ragile RA-B6520-24DC8QC BCM56780</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 x QSFP56-DD 400G and 24 × QSFP56 200G </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">82 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/RA-B6520C.html">Ragile RA-B6520-48C8QC BCM56780</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 x QSFP56-DD 400G and 48 × DSFP56 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">82 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/nephos-836x.html"><b>Nephos 8360 Taurus family</b></a>  </p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/aurora705.html">Netberg Aurora 705 NP8367</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100 Gb/s QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">28 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/aurora740.html">Netberg Aurora 740 NP8369</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 port 100 Gb/s QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/CIG-CS6436.html">CIG CS-6436-56P NP8366</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25 Gb/s and 8 ports 100G QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/liteon-LS3048.html">Liteon-LS3048-SN1 NP8363</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10G SFP+ and 6 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 Mbyte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/liteon-LS4048.html">Liteon-LS4048-SN3 NP8365</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 6 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 Mbyte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nephos-as7116.html">Nephos-AS7116-54X NP8365</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 25G SFP28 and 6 port 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">options: 20-50 Mbyte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ingrasys-s9130.html">Ingrasys S9130-32X</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port 100G QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">options: 20-50 Mbyte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ingrasys-s9230.html">Ingrasys S9230-32X</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 port 100G QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">options: 20-50 Mbyte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></font></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/maverick.html">Broadcom Maverick</a> </p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Alpha-maverick.html">Alpha Networks SNX-61A0-486T</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 10G-base-T and 4 QSFP28 and 2 QSFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">?? MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Alpha-maverick.html">Alpha Networks SNX-61A0-486F</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP28 and 2 QSFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">?? MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S4148.html">Dell S4148F-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port SFP+ and 2 QSFP+ and 2 QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S4148.html">Dell S4148T-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port 10BaseT and 2 QSFP+ and 2 QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S4112.html">Dell S4112F-ON and S4112T-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 port SFP28 and 3 QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/QCT-LY7.html">QCT QuantaMesh T3048 LY7</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port SFP+ and 4 QSFP28</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/tomahawk">Broadcom Tomahawk </a> </p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Penguin-3200C.html">Penguin 3200C</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Z9100">Dell Z9100</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dell-6100.html">Dell S6100-ON</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Depends on modules selected.</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S5148.html">Dell S5148</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port SFP28 25 Gb/s + 6 x 100G</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/3232C.html">Cisco Nexus 3232C</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr>
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/NCS5001.html">Cisco NCS5011</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7060CX.html">Arista 7060CX-32</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP28 100 Gb/s and 2 SFP+</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7060CX.html">Arista 7260CX-64</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 port QSFP28 100 Gb/s and 2 SFP+</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7320X.html">Arista 7320X</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">256 port QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/QFX5200.html">Juniper QFX5200-32C</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/QFX5200.html">Juniper QFX5200-64Q</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP28 OR 64 QSFP </font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/aurora620.html">Aurora 620 with ONIE</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28 100 G</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/aurora630.html">Aurora 630 with ONIE</font></a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 16 QSFP28 100 G</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/aurora-720.html">Aurora 720 with ONIE</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Inventec-100.html"> Inventec D7032Q28B</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MByte</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 MByte per core</font></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7700.html">Edgecore AS7710 and AS7712</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/OMP800.html">Edgecore OMP800</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">256 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Champion.html">Champion Tomahawk</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/RA-B6500.html">Ragile RA-B6500-32H</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 X 50 Gb/s and 8 x QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HP6960.html">HP 6960</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/4048T-ON.html">Quanta T7032-IX1</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 100Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/4048T-ON.html">Quanta T4048-IX2</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 + 8 x QSFP28/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Agema.html">Agema AG5648</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 QSFP28 100 Gb/s and 48 SFP28 25 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/supermicro-C3632.pdf">Supermicro SSE-C3632S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Agema.html">Agema AG9032</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/backpack.html">Facebook OCP Backpack</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">128 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">256 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/EC-7812.html">Edgecore 7812-24S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 QSFP28 AND 8 200 Gb/s coherent</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/tomahawk-plus.html">Broadcom Tomahawk-+</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N8500.html">fs.com N8500-48B6C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/QFX5200-2.html">Juniper QFX5200-48Y</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Agema.html">Agema AG5648V1</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7300-54.html">Edgecore AS7312-54XS</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 and 6 QSFP28 </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 4.5 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/alpha-SNC.html">Alpha Networks SNC-60x0-486F</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista7060CX2.html">Arista 7060CX2-32S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 4.5 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Lenovo-NE2572.html">Lenovo NE2572 &amp; NE2572O</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s AND 6 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 4.5 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/tomahawk-ii.html">Broadcom Tomahawk-II</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7260QX-64.html">Arista 7260QX-64</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP 40 Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7260CX3-64.html">Arista 7260CX3-64</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">10.5 Mbyte per slice</p>

</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AG9064.html">Agema AG9064</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 3 Mbyte per core</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7800.html">Edgecore AS7816-64X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 10.5 Mbyte per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C3264C-E.html">Cisco Nexus C3264C-E</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 10.5 Mbyte per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Juniper-5210.html">Juniper QFX5210-64C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 10.5 Mbyte per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-9264.html">Dell Z9264f-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 10.5 Mbyte per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N8560.html">FS.COM N8560-64</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s AND 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 10.5 Mbyte per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/RA-B6910-64C.html">Ragile RA-B6910-64C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Est 10.5 Mbyte per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/tomahawk-3.html">Broadcom Tomahawk 3</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7900.html">Edgecore AS7900-32X &amp; AS9716-32D</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7060-t3.html">Arista 7060PX4-32</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x OSFP 400 Gb/s ports and 2 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7060-t3.html">Arista 7060DX4-32</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports and 2 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/FB-minipack.html">Facebook Minipack</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8-slot chassis: 4x400 Gbps and 16x100 Gbps cards</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/arista-7368.html">Arista 7368X4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8-slot chassis: 4x400 Gbps and 16x100 Gbps cards</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/9032-IX9.html">QuantaMesh BMS 9032-IX9</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/AGC032.html">Delta AGC032</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports and 2 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/Z9332.html">Dell Z9332F-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports and 2 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/aurora820.html">Aurora 820</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/RA-B6920.html">Raigle RA-B6920-32QC2X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP-DD 400 Gb/s ports and 2 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/RA-B6920-4S.html">Raigle RA-B6920-4S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 slots, 32 x QSFP 100 Gb/s cards</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/slingshot.html">HPE Rosetta Slingshot</a> 
</p></p>
</td></tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/marvellCX.html">Marvell family ASICs</a> 
</p></p>
</td></tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/tomahawk4.html">Tomahawk-4</a> 
</p></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/Arista7060X5.html">Arista 7060X5</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 x QSFP-DD 400 Gb/s ports and 2 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">113 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">113 MB</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/Arista7388X5.html">Arista 7388X5</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
8-slot chassis: 8- and 16-port cards</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">113 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">113 MB</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/RA-6930.html">Ragile RA-B6930-64QC</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 x QSFP-DD 400 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">113 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/RA-6930D.html">Ragile RA-B6930-128DC</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">128 x QSFP 200 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">113 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/innovium.html">Innovium Teralynx</a> 
Hot new chip to take over the world [2017 OCP]</p></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/netberg-615.html">Aurora Netberg 615</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 25 Gb/s ports + 8 x QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">45 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/netberg-715.html">Aurora Netberg 715</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 100 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">45 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/3408S.html">Cisco Nexus 3408-S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8-slot chassis w 4-port 400G and 16-port 100G cards</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">70 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/3432D.html">Cisco Nexus 3432D-S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP-DD 400 Gb/s + 2 x SFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">70 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<a href="../buffers/Bufs/dune.html">Broadcom Jericho</a> a member of the StrataDNX DUNE family</p></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/NCS5508.html">Cisco NCS 5508</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">288 QSFP28 100 Gb/s ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GByte per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">VoQ 10 mS per queue</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N9K-96.html"> Cisco Nexus N9K-X9636C-R </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 x 100 Gb/s QSFP28 linecard</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GByte per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">VoQ </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N9K-96.html"> Cisco Nexus N9K-X9636Q-R </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 x 40 Gb/s QSFP linecard</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GByte per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">VoQ </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista7500R.html">Arista 7500R Linecard 36CQ</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 GB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista7500R.html">Arista 7500R Linecard 36Q</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">30 x 40G QSFP and 6 x 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista7500R.html">Arista 7500R Linecard 48S2CQ</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port sfp+ and 2 x 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7280R.html">Arista 7280QR-C36</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 QSFP+ and 12 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB in 2 groups</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7280R.html">Arista 7280QR-C48</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 QSFP+ and 24 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 GB in 8 groups</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/slx-9850.html">Brocade SLX-9850</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 QSFP28 per linecard</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 or 6 GB per 6-port group <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VSP8600.html">Extreme VSP8600 - 8 slot chassis</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">modules: 6 x 100G, 16 x 40G, 24 x 10G</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> </p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<a href="../buffers/Bufs/qumran.html">Broadcom Qumran</a> a member of the StrataDNX DUNE family</p></p>
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/7020.html">Arista 7020SR-24C2</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 x 10G SFP+ and 2 x QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB VoQ</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/7020.html">Arista 7020SR-32C2</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x 10G SFP+ and 2 x QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB VoQ</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/7020.html">Arista 7020TR-48</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x 1GBASE-T and 6 x SFP+</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB VoQ</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/7280R.html">Arista 7280SR-48C6</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x 10 G SFP+ and 6 x QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB VoQ</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/7280R.html">Arista 7280TR-48C6</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x 10GBASE-T and 6 x QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB VoQ</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/NCS5508.html">Cisco NCS 5501</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">six QSFP28 100 Gb/s ports and 48 x 10 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GByte per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">VoQ 10 mS per queue</p>
</td> </tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/slx-9540.html">Brocade SLX-9540 Extreme SLX-9540</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 QSFP28 100/40 Gb/s and 48 10/1 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/slx-9640.html">Extreme SLX-9640</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 QSFP28 100/40 Gb/s and 24 10/1 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5900.html">Edge-Core AS5912-54X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28 Qumran-MX BCM88370</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5916-54XKS.html">Edge-Core AS5916-54XKS (w ext TCAM) aka AGR130</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28 Qumran-MX BCM88375</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS5916.html">Edge-Core AS5916-54XL (no ext TCAM) aka AGR110</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28 Qumran-MX BCM88370</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HPE5980.html">HPE FlexFabric 5980 </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Champion.html">Champion Qumran</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Alpha-STX.html">Alpha STX-60x0-486F Qumran
</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S4200.html">Dell S4248-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AGC7648A.html">Agema AGC7648A BCM88375</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ATT-qumram.html">AT&T; open XGS-PON </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 XFP and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/dcsg.html">Disaggregated Cell Site Gateways</a> 
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dcsg.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/ufiSpace-S9500.html">ufiSpace S9500-22XST</a></font></pre></p> </td> 
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 x 1G RJ-45, 8 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 GB QumranAX BCM88470</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dcsg.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/ufiSpace-S9500-30XS.html">ufiSpace S9500-30XS</a></font></pre></p> </td> 
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB QumranAX BCM88470</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dcsg.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/Delta-.html">Delta AGCV208S</a></font></pre></p> </td> 
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 x 1G RJ45/ 4 x 10G SFP+/ 8 x 25G SFP28/ 2 x 100G QSFP28 </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GB QumranAX BCM88470</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dcsg.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/AS7316.html">Edgecore AS7316-26XB aka CSR320</a></font></pre></p> </td> 
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB QumranAX BCM88470</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/AS7315.html">Edgecore AS7315-27X aka CSR310</a></font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 x 10G SFP+, 4 x 25G SFP28, 3 x 100G QSFP28 </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB QumranAX BCM88470</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/AS7315-30X.html">Edgecore AS7315-30X aka CSR300</a></font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 x 1G RJ45, 16 x 10G SFP+, 8 x 25G SFP28, 2 x 100G QSFP28 </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB QumranAX BCM88470</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/AS5915-18X.html">Edgecore AS5915-18X aka CSR200</a></font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 x 1G RJ45, 8 x 1G SFP, 6 x 10G SFP+ </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 GB QumranUX BCM88272</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/ufiSpace-S9501.html">ufiSpace S9501-18SMT</a></font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 x 1G RJ45, 8 x 1G SFP, 6 x 10G SFP+ </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GB QumranUX BCM88272</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/ufiSpace-S9501-28.html">ufiSpace S9501-28SMT</a></font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 x 1G RJ45, 16 x 2.5G SFP, 6 x 10G SFP+, 2 x 10G SFP+ MACsec</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GB QumranUX BCM88272</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     <a href="../buffers/Bufs/IP-50FX.html">Ceragon IP-50FX</a></font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 x 1G RJ45, 14 x 1/2.5G SFP, 4 x 10G SFP+, 2 x 10G CAT6 PoE</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">QumranUX</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/qumran2c.html">Broadcom Qumran-2C</a> 
a member of the StrataDNX DUNE family </p></p>
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/Qum-2c.html">Agema AGCX422S</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 x QSFP28 100G + 4 x QSFP-DD 400G + 4 x SFP28 10G/25G</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/Qum-2c.html">Agema AGCVA48S</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 + 4 x SFP+ 10G + 10 x QSFP28 100G</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/ufispace-9600.html">UfiSpace S9600-32X</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 100G  </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/AS7946-30XB.html">Edge-core AS7946-30XB</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">22 x QSFP28 100G + 4 x QSFP-DD 400G + 4 x SFP28 10G/25G  </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/jericho-plus.html">Broadcom Jericho+</a> 
a member of the StrataDNX DUNE family </p></p>
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AGC5648.html">Agema AGC5648</a> Jericho+</p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 and 6 QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB per ASIC</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> <a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-3636C.html">Cisco 3636C-R</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 ea QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-55A1.html">Cisco NCS-55A1-36H-S/SE</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 ea QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-55A1.html">Cisco NCS-55A1-24H-S/SE</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 ea QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7280R2.html">Arista 7280SR2A-48YC6 </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x 25 G SFP28 and 6 x QSFP28</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB VoQ</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7500R2.html">Arista 7500R2-36CQ </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 x QSFP28 100 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GByte per ASIC</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/jericho2.html">Broadcom Jericho2</a> 
a 16 nm member of the StrataDNX DUNE family </p></p>
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7926.html">Edgecore AS7926-80X </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">80 x QSFP28 100 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GByte</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS9926.html">Edgecore AS9926 Sw Fabric </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 x 400Gb/s QSFP-DD</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">?</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7926-40XKFB.html">Edgecore AS7926-40XKFB </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 x QSFP28 100 Gb/s + 13 x QSFP-DD 400 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GByte</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S9700-53DX.html">ufiSpace S9700-53DX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 x QSFP28 100 Gb/s ports + 13 x QSFP-DD 400 Gb/s fabric</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GByte</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S9600-48.html">ufiSpace S9600-48X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x QSFP28 100 Gb/s </p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GByte</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/S9700-23D.html">ufiSpace S9700-23D</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
10 x 400 Gb/s QSFP-DD ports and 13 x 400 G QSFP-DD fabric</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GBytes</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/7280R3.html">Arista 7280xR3</a> a family of fixed configuration Jericho2 switches
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     7280CR3-32P4</font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 ports QSFP28 100G + 4 ports OSFP 400G</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GByte - 1 Jericho2 ASIC</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     7280CR3-32D4</font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 ports QSFP28 100G + 4 ports QSFP-DD 400G</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GByte - 1 Jericho2 ASIC</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     7280PR3-24</font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 ports 400 Gb/s, OSFP 400 G</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 GByte - 2 Jericho2 ASICs</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>
<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     7280DR3-24</font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 ports 400 Gb/s QSFP-DD 400 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 GByte - 2 Jericho2 ASICs</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">
</a> <pre><font size="+2">     7280CR3-96</font></pre></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">96 ports QSFP28 100 Gb/s</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 GByte - 2 Jericho2 ASICs</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">Cisco NC57-24X400G-BA linecard </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 ports 400 Gb/s QSFP-DD</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 GByte - 2 Jericho2 ASICs</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cisco-linecard.html">Cisco NC57-18D12TH-SB linecard  </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">18 x 400 Gb/s or 30 x 100/200 Gb/s QSFP-DD</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 GByte - 2 Jericho2 ASICs</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/jericho2c.html">Broadcom Jericho2C</a> 
a 16 nm member of the StrataDNX DUNE family </p></p>
</td></tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/jericho2cplus.html">Broadcom Jericho2C+</a> 
a 7 nm member of the StrataDNX DUNE family </p></p>
</td></tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/S9710-76D.html">ufiSpace S9710-76D</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
36 x 400 Gb/s QSFP-DD ports and 40 x 400 G QSFP-DD fabric</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 GBytes</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top">
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/cisco8000.html"><b>Cisco 8000 Silicon One</b></a> 
 </p></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/8000.html">Cisco 8201 (Q100 ASIC)</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 QSFP56-DD 400 Gb/s and 12 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/8000.html">Cisco 8202 (Q100 ASIC)</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 QSFP56-DD 400 GbE and 60 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/8000.html">Cisco 8201-32FH (Q200 ASIC)</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP56-DD 400 GbE</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Broadcom <a href="../buffers/Bufs/dune.pdf"> ARAD </a>(July 2014)
a member of the StrataDNX DUNE family</p></p>
</td></tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7280SE">Arista 7280E-64</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port SFP+ and 4 x QSFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> 125 MB per 10 gig port</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7280SE">Arista 7280E-68</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port SFP+ and 2 x QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> 125 MB per 10 gig port</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/7280SE">Arista 7280E-72</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port SFP+ and 2 x MXP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> 125 MB per 10 gig port</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista7504">Arista 7504E/7508E</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 port sfp+ line card</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB per each of <a href="../buffers/Bufs/7500E-PP.jpg">3 processors</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">50 MB/port-queue</p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista7504">Arista 7504E Linecard 12CQ</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB per each of <a href="../buffers/Bufs/7500E-PP.jpg">6 processors</a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">500 MB/port-queue</p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/EZchip.html"><b>EZChip NP-5</b?<></p></p>
</td>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/N5R-100.html">PARPRO N5R-100</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 GByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> very large</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/novisw.html">NoviSwitch 2122</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 SFP+ and 2 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> very large</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/novisw.html">NoviSwitch 2128</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 SFP+ and 4 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> very large</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/novisw.html">NoviSwitch 2150</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP and 2 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> very large</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/novisw.html">NoviSwitch 21100</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">96 10/100/1000Base-T and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a> very large</p>
</td> </tr>

<tr>
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/cavium.html">Cavium</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7500.html">edgecore AS7500-32X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS7512.html">edgecore AS7512-54X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 QSFP28 100 Gb/s and 48 SFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Wedge100C.html">Wedge_100C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista7160.html">Arista 7160 family</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/SLX-cavium.html">Brocade SLX-9240</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/SLX-cavium.html">Brocade SLX-9140</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 QSFP28 100 Gb/s and 48 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Pegatron.html">Pegatron w/out model num</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 QSFP28 100 Gb/s and 48 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 MB</p>
</td>
</tr>

<tr>
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/barefoot.html">Barefoot Tofino</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Wedge100BF.html">Wedge 100BF-32X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
32 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">16 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">16 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Wedge100BF.html">Wedge 100BF-65X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">65 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">16 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">16 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/WNC.html">OSW 1800 </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 25G and 6 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">16 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">16 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/IM.html">InterfaceMasters Tahoe 2624 </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 x SFP28 25G and 26 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/aurora610.html">Netberg Aurora 610 Tofino BFN-T10-032D </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 8 x QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Aurora-710.html">Netberg Aurora 710 Tofino BFN-T10-032D </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 and 2x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Aurora-750.html">Netberg Aurora 750 Tofino BFN-T10-064Q </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 x QSFP28 and 2x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">22 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7170.html">Arista 7170-64C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 x QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Stordis.html">Stordis BF2556XT-1T</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 and 8 x QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Stordis-6064.html">Stordis BF6064X-T</a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">65 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/APS2172Q.html">APS Networks APS2172Q</a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 SFP28 1/10/25G and 8 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/APS2140D.html">APS Networks APS2140D</a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 SFP28 1/10/25G and 8 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/APS6120Q.html">APS Networks APS6120Q</a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 QSFP28 100 Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C34180.html">Cisco Nexus C34180</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP28 and 6 x QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">20 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7170.html">Arista 7170-32C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S9180-32X.html">ufiSpace S9180-32X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP28 + 2 x SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">22 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726">20 Mbyte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr>
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/barefoot2.html">Intel Tofino2 </a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS9516-32X.html">Edgecore 9516-32D aka DCS810</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 x QSFP56-DD </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723">64 MByte</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr>
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/cavium.html">A mystery (for now)</a></p></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Telco8100.html">Telco Systems T-Metro-8100</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
2 x QSFP28 100G and 48 x SFP+ 10G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr>
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"> </p></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Huawei6720.html">Huawei S6720-54C-EI-48S</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 2 QSFP and 4 QSFP expansion</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB to 1 port</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Huawei6720.html">Huawei S6720-30C-EI-24S</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+ and 2 QSFP and 4 QSFP expansion</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 MB to 1 port</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/mellanox.html">Mellanox </a><p><p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/mellanox">Mellanox SX1024</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 12 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4.6 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 KB to 1 port</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/mellanox">Mellanox SX1036</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">??</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4.6 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">128 KB to 1 port</p>
</td>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/mellanox-spectrum">Mellanox SN2700 SN2410 SN2100</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/mellanox-2010.html">Mellanox  MSN2010-CB2RC</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">18 SFP28 25G and 4 QSFP28 100Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HPE-spectrum.html">HPE SN2700M SN2410M SN2100iM</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/mellanox-spectrum-2.html">Mellanox Spectrum-2</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/spectrum2-sw.html">Mellanox SN3800</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP28 100Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/spectrum2-sw.html">Mellanox SN3700 and SN3700C</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP56 200Gb/s or QSFP28 100Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/spectrum2-sw.html">Mellanox SN3510</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 QSFP-DD 400 Gb/s + 48 QSFP56 50Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/spectrum2-sw.html">Mellanox SN3420</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 QSFP28 100Gb/s + 48 SFP28</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">42 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/mellanox-spectrum-3.html"><b>Mellanox Spectrum-3</b></a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/SN4700.html">Mellanox SN4700</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 port QSFP-DD 400Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">50 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/SN4600.html">Mellanox SN4600</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 port QSFP56 200Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">50 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/SN4600C.html">Mellanox SN4600C</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 port QSFP28 100Gb/s</p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">50 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">
<a href="../buffers/Bufs/SN4800.html">Mellanox SN4800</a></p> </td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8 slots: 4x400Gb/s, 8x200Gbs, 16x100Gb/s </p> </td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16</p> </td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB</p> </td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p> </td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">50 MB to 1 port?</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/helix.html">Broadcom Helix</a><p><p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista7010t">Arista 7010T</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T + 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB/switch</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade-7150.html">Brocade ICX 7150-24</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">(24+2) 1000-base-T and 4 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade-7250.html">Brocade ICX 7250-24</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">(24+2) 1000-base-T and 4 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade-7650.html">Brocade ICX 7650-48P</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x  1000bsseT and (2 x 40G or 4 x 10G front module) </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade-7650.html">Brocade ICX 7650-48ZP</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 x 1000BaseT and 24 multiGig ports and (1 x 100G or 2 x 40G front module)  </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Altoline-6900.html">HPE Altoline 6900</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T and 4 SFP+ and 2 QSFP stacking ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Champion.html">Champion helix4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T and 4 SFP+ and 2 QSFP stacking ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell-S3048.html">Dell S3048-ON</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T and 4 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Agema-6248.html">Agema AG6248C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T PoE+ w 2 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS4610_Series.pdf">Edgecore 4610-30T Helix4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 1000-base-T  w 4 SFP+ and 2 QSFP stacking ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS4610_Series.pdf">Edgecore 4610-30P Helix4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 1000-base-T PoE+ w 4 SFP+ and 2 QSFP stacking ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS4610_Series.pdf">Edgecore 4610-54T Helix4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T  w 4 SFP+ and 2 QSFP stacking ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/AS4610_Series.pdf">Edgecore 4610-54P Helix4</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T PoE+ w 4 SFP+ and 2 QSFP stacking ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<a href="../buffers/Bufs/hurricane.html"><b>Hurricane: BCM56150, BCM56160, BCM56170</b></a><p><p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/PulseOptics-switch-datasheet.pdf">PulseOptics SW-M24G-4SFP</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 x 1000baseT + 4 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1.5 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/s3910-series-switches-datasheet.pdf">fs.com S3910 series</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 1000-base-T w 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1.5 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/S5860-20SQ.html">fs.com S5860-20SQ</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 1G/10G SFP+ and 4 10G/25G SFP28 and 2 QSFP 40G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td> </tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">
<a href="../buffers/Bufs/Centec.html"><b>Centec</b></a><p><p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Centec580.html">Centec V580-20Q4Z and E580-20Q4Z</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 x QSFP 40G and 4 x SFP+ and 4 x QSFP28 100G </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Centec580.html">Centec V580-48X2Q4Z and  E580-48X2Q4Z</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP+ 10G and 2 x QSFP+ 40G and 4 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Centec350.html">Centec V350-48T4X and E350-48T4X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x 1000baeT and 4 x QSFP+ 40G and 4 x QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Centec330.html">Centec E330-52SX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 x SFP 1G and 4 x SFP+ 10G </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/uadp-family.html">Cisco UADP Catalyst</a></p><p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst <a href="../buffers/Bufs/cat3850"> 3850,</a> 3650 </p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">ASIC support 24 GE ports AND 2 x 10GE</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"><a href="../buffers/Bufs/3850QoS.html">several</a> </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 MB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB per ASIC </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst <a href="../buffers/Bufs/cat3850#code3850"> C3850-12XS</a> </p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 SFP+ (6 ports per ASIC)</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 MB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB per ASIC </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Cat9200.html">Catalyst C9200-family </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24- and 48-port 1-Gb/s access switches + uplinks</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C9300.html">Catalyst C9300-24T </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">ASIC support 24 GE ports AND uplink module</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp2-buf.html">~5 MB</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C9300.html"> Catalyst C9300-48T</a> </p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 GE ports AND uplink module</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp2-buf.html">~5 MB</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C9300.html">Catalyst C9300-24UX</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24  100/1G/2.5G/5G/10G Tw-Pr ports AND uplink module</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp2-buf.html">~5 MB</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C9300.html">Catalyst C9500-24Q</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 QSFP 40 Gb/s </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp2-buf.html">~10 MB</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C9300.html">Catalyst C9500-40X</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+ ports AND uplink module</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp2-buf.html">~10 MB</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp-3.0.html">Catalyst C9500-24Y4C [UADP  3.0]</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP28 ports AND 4 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724">36 MB per ASIC</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">est 23 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp-3.0.html">Catalyst C9500-32QC [UADP  3.0]</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 x QSFP28 100G <b>OR</b> 32 QSFP 40G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724">36 MB per ASIC</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">est 23 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp-3.0.html">Catalyst C9500-32C [UADP  3.0]</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP28 100G ports</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724">36 MB per ASIC</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">est 23 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/uadp-3.0.html">Catalyst C9500-48Y4C [UADP  3.0]</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 ports AND 4 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724">36 MB per ASIC</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">est 23 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/C9600R.html">Catalyst C9600R</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6-slot chassis w 3 ea UADP3.0 ASICs</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723">2P6Q3T </a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724">36 MB per ASIC</a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">est 23 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/WLC.html">Catalyst C9800</a></p> 
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Wi-Fi controller</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/nexus-ACI.html">Cisco Nexus switches w ACI </a>silicon</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9200.html">Cisco Nexus 92160YC-X</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 and 6 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Single ASE3 20 MByte </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">10.2 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9200.html">Cisco Nexus 9272Q</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2RU 72 x 40Gb/s QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Single ASE2 30 Mbyte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5.1 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9200.html">Cisco Nexus 92304QC</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2RU 56 x 40Gb/s QSFP+ and 8 QSFP28</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Single ASE2 30 Mbyte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5.1 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9300">Cisco Nexus 9372TX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 10-Gbps Base-T and 6 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB NFE + 25 MB ALE </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">21 MB max burst</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9300">Cisco Nexus 9396PX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and {12 QSFP+
<font color="red">or</font> 4 CPAK 100G}</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 MB NFE + 40 MB ALE</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">21 MB max burst</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-93180.html">Cisco Nexus 93180YC-EX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 slices x 20 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">17.6 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-93108.html">Cisco Nexus 93108TC-EX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 tw-pr 10 Gb/s and 6 QSFP28
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 slices x 20 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">17.6 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-93180F.html">Cisco Nexus 93180YC-FX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP28 25 Gb/s and 6 QSFP28
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">~35 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-93108F.html">Cisco Nexus 93108TC-FX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 tw-pr 10 Gb/s and 6 QSFP28
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">~35 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9364.html">Cisco Nexus 9364C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 ports QSFP28 100 Gb/s
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">10 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9364.html">Cisco Nexus 9332C</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 ports QSFP28 100 Gb/s
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">10 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-9336C.html">Cisco N9K-9336C-FX2</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">36 ports QSFP28 100 Gb/s
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-93360.html">Cisco N9K-93360YC-FX2</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">96 x 10/25 Gb/s SFP28 + 12 x 40/100 Gb/s QSFP28
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-GX.html">Cisco Nexus N9K-C9316D-GX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 QSFP-DD 400/100 Gb/s
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">80 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-GX.html">Cisco Nexus N9K-C93600CD-GX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">28 SFP28 and 8 QSFP28-DD
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">80 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-GX2.html">Cisco Nexus 9364-GX2A</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 QSFP-DD + 2 SFP+
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">120 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">30 MB per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nexus-GX2.html">Cisco Nexus 9332-GX2B</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 QSFP-DD + 2 SFP+
</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">120 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">60 MB per slice</p>
</td>
</tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Other Shared Memory</p>
</td>
</tr>

<tr align="left" valign="top">

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/cat3550.html">Catalyst 3550-24</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 10/100-base-T + 2 x 1G GBIC</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MByte</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/ciena3930.html">Ciena 3930</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 x SFP+ and 4 SFP and 4 SFP-or-TwPr (10/100/1000)</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"> </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Extreme450.html">Extreme X450-G2-48T-10G</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 1000-base-T + 4 x 10G SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">? </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Extreme620.html">Extreme 620X-16</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 10-Gbps SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Extreme620.html">Extreme 620X-10</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">10 10-Gbps SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB </p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Brocade FCX624S</p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24Gig-E and 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1.04 MB to 1 port</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Ex4300.html">Juniper Ex4300 </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 or 24 Tw-pair, 20 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">undisclosed</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Ex4500.html">Juniper Ex4500 / Ex4550</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">40 SFP+ plus 8 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">230 KBytes</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Brocade-6610.html">Brocade ICX6610-24</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24Gig-E w 8 SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 MB to 1 port</p>
</td> </tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HP3800">HP 3800</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24Gig-E and 4 10Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q or 4Q or 2 Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">0.23 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HP2920">HP 2920-24</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 tw-pr Gig-E and 4 optional 10Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q </p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">11.25 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4.5 MB shared</p>

</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6.75 MB shared</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/HP2824.html">HP 2824</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 tw-pr Gig-E and 4 SFP</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4Q </p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">0.512 MB shared</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">0.512 MB shared</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">HP A5800-24G</p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24Gig-E and 4 10Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">HP E6600-24G-4XG</p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24Gig-E w 2 10Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">18 MB for GE</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">18 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista_7124SX">Arista 7124SX</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB/sw-chip</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">shared</p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1.238 + 0.02 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista_7124SX">Arista 7148SX</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB/sw-chip, 8 MB total</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1.238 + 0.02 MB</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista_7150">Arista DCS-7150S-24</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/FM6000-buf.html">7.5 MB </a></p>
</te>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista_7150">Arista DSC-7150S-52</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">52 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/FM6000-buf.html">7.5 MB </a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/arista_7150">Arista DCS-7150S-64</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/FM6000-buf.html">7.5 MB </a></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>

</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dell-8024.html">Dell 8024</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Dell6248">Dell 6248</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 Gig-E, 4 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">0.75 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">98 KB per port</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/dell7024">Dell 7024</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 Gig-E, 4 x SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/G8052">IBM BNT G8052</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 GE + 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB/switch</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nortel5500"><id="nortel">Nortel 5520-48T ver 1-3</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 GE + 4 SFP shared</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q fixed</p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">786 KB per 12-port</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">131 KB w 8 Queues</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/nortel5500">Nortel 5520-48T ver 4-5</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 GE + 4 SFP shared</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 to 8Q </p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">786 KB per 12-port</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">786 KB w 1 Queue</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst <a href="../buffers/Bufs/small-asic">3750G-48TS, 2960G</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">12 ASICs w/ 4 GE ports ea</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1P3Q3T</p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">576KB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">192KB per ASIC</p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">384 KB per ASIC</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst <a href="../buffers/Bufs/2960S.html">2960S</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Single ASIC: 48 +2 10Gb/s</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1P3Q3T</p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MByte</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MByte</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst 3750E, 3560E, 3750X &amp; 3560X</p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">ASIC support 24 GE ports or 2 x 10G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1P3Q3T</p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2750KB per ASIC</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">750KB per ASIC</p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">2 MB per ASIC</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst <a href="../buffers/Bufs/2960X">2960-X </a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/2960Ports">ASIC support 48 GE ports AND uplink and stack</a></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 MB per ASIC </p>
</td>
</tr>

<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Catalyst 4948E </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 GigE + 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">17.5 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Max 16 MB to 1 port</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Cisco Catalyst <a href="../buffers/Bufs/cat4510E">4510R+E</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Chassis w 8 interface slots -- 12 port SFP+ line card</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1P7Q1T</p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB on Supervisor</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Miercom-4500">Max 14 MB to 1 port</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">Cisco Catalyst <a href="../buffers/Bufs/4500-X">WS-C4500X-32SFP+</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 RU w 32 SFP+ ports and module for 8 more</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1P7Q1T</p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 MB </p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">see note above</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Nexus3548">Cisco Nexus 3548 and 3548X<a> </p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">18 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">5.8 MB</p>
</td>
</tr>

<tr><td> </td></tr>
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/deep-buf">Large queue 1RU switches</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/force10-s60">Force10 S60</a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 Gig-E + 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1250 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">enough</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/Arista-7048">Arista 7048</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 Gig-E + 4 SFP+</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">768 MB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">16 MB/port?</p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">GOBBS</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-2000.html">Corsa DP2100</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 1/10 G SFP+ </p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-buf">see note</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-2000.html">Corsa DP2200</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 1/10 G SFP+ and 2 QSFP28 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-buf">see note</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-2000.html">Corsa DP2400</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">32 1/10 G SFP+ and 2 QSFP28 100G + stack</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">6 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-buf">see note</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-64xx.html">Corsa DP6430</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24 SFP+ and 2 CFP/2 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-buf">see note</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-64xx.html">Corsa DP6440</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">48 SFP+ and 4 CFP/2 100G</p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">20 GB</p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/corsa-buf">see note</p>
</td>
</tr>

<tr><td> </td></tr>
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Virtual Output Port queuing</p>
</td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/MLX">Brocade MLX </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/mlx-2x100-gbe-ds.pdf">2-port 100 Gb/s line card</a></p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">256 MB/port-queue</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/MLX">Brocade MLX </a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8-port 10 Gb/s line card</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">3 GB </p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">256 MB/port-queue</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/MLX">Brocade MLX</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">24-port 1 Gb/s line card</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">1 GB</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">64 MB/port-queue</p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p></td>
</tr>

<tr align="left" valign="top"><td><a name="wp9001720"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/BlackDiamond.html">Extreme BlackDiamond X8</a></p>
</td>
<td><a name="wp9001721"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">96-port SFP+ line card<p>48-port QSFP+ line card<p>4-port CFP2 100 Gb/s line card</p></td>
<td><a name="wp9001722"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</p>
</td>
<td><a name="wp9001723"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p></td>
<td><a name="wp9001724"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">9 MB per 24 10-Gb/s ports<p>9 MB per 6 40-Gb/s ports<p>36 MB per fabric module</p>
</td><td><a name="wp9001725"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001726"></a><p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/BlackDiamond.html">Who knows??</a></p></td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/Cisco-5K">Cisco Nexus 5010</a></p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">26 SFP+</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1 (I think)</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">480 KB per port</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">480 KB</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/Cisco-5548">Cisco Nexus 5548P</a></p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">32 fixed SFP+ and 16-port expansion module</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8 Unicast 8 Multi</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1 (I think)</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">640 KB per port</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">640 KB</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/Cisco-5672UP">Cisco Nexus 5672UP</a></p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">48 fixed SFP+ and 6 QSFP+</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8 Unicast 8 Multi</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1 (I think)</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">25 MB per 12-port 10G ASIC</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">14 MB shared per ASIC</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">3 MB Unicast + 6 MB Multicast</p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/Cisco-6001">Cisco Nexus 6001</a></p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">48 fixed SFP+ and 4 QSFP+</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8 Unicast 8 Multi</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1 (I think)</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">25 MB per 12-port 10G ASIC</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">14 MB shared per ASIC</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">3 MB Unicast + 6 MB Multicast</p>
</td>
</tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/ASR-9000-buffer.html">Cisco ASR-9000</a></p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Chassis solution. 1-6 ports per ASIC</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">ASICs have 0.5 to 3.3 GB/port</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001720"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/QFX10002.html">Juniper QFX10002-36</font></a></p>
</td>
<td><a name="wp9001721"></a>

<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">QSFP: 12 x 100 Gb/s OR 36 x 40 Gb/s</font></p>
</td>
<td><a name="wp9001722"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">8Q</font></p>
</td>
<td><a name="wp9001723"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>
</td>
<td><a name="wp9001724"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT">4 GByte per ASIC</font></p>
</td>
<td><a name="wp9001725"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"></p>

</td>
<td><a name="wp9001726"></a>
<p style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_bodyCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a>  100 mS per port</font></p>
</td>
</tr>

<tr><td></td> </tr>
<section id="xxx">
<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT"><a href="../buffers/Bufs/nexus-7K.html"> Nexus 7000/7700</a></p>
</td>
</tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (M1 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">48-port Tw-Pr GE</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">2q4t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p3q4t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">7.56 MB per port</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">6.15 MB per port</p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (F3 Series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">6-port 100GE CPAK</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">72 MB shared</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (F2 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">48 SFP+ across 12 ASICs</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q1t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p3q1t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">72 MB shared</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (F3 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">12 QSFP+ across 6 ASICs</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q1t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p3q1t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">72 MB shared</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (M1 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">32-port 10GE shared 4-port groups SFP+</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8q2t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p7q4t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">65 MB per group</p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">80 MB per group</p>
</td></tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (M1 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8-port 10GE X2</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8q2t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p7q4t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">92 MB </p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">80 MB </p>
</td></tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (M2 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">2-port 100GE CFP2</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8q2t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p7q4t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">62.46 MB </p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">31.23 MB </p>
</td></tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7000 (M2 series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">24-port 10GE SFP+</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">8q2t</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">1p7q4t</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">5.21 MB </p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">5.21 MB </p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7700 (F3 Series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">12-port 100GE CPAK across 12 ASICs</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>

</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">144 MB shared</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td></tr>
<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7700 (F3 Series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">24-port 40GE QSFP+ across 12 ASICs</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>
</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">144 MB shared</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">Cisco Nexus 7700 (F3 Series)</p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">48-port 10GE SFP+ across 6 ASICs</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">4q</p>
</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">144 MB shared</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/VoQ.html">VoQ</a></p>
</td></tr>

<tr><td></td></tr>

<tr align="left" valign="top">
<td><a name="wp9001370"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"><a href="../buffers/Bufs/6807xl.html">Cisco C6807-xl w Sup-6T</a></p>
</td>
<td><a name="wp9001371"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">7-slots w 5 line card slots</p>
</td>
<td><a name="wp9001372"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001373"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001374"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT">interface dependent</p>
</td>
<td><a name="wp9001375"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td>
<td><a name="wp9001376"></a>
<p style="font-style: normal; font-variant: normal; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-indent: 0pt; text-transform: none" class="pChart_headCMT"></p>
</td></tr>

<tr align="left" valign="top">
<td colspan="7" rowspan="1"><a name="wp9001552"></a>
<p style="font-style: normal; font-variant: normal; font-weight: bold; margin-bottom: 3pt; margin-left: 3pt; margin-right: 3pt; margin-top: 3pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pChart_subheadCMT">Cisco <a href="../buffers/Bufs/catalyst6500">Catalyst 6500</a> gets its own table</p>
</td>
</tr>

</table>

<p style="font-size: 10pt; font-style: normal; font-variant: normal; font-weight: bold; margin-left: 0pt; margin-right: 0pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pSubhead1CMT">Comments, suggestions, corrections to warner@ucsc.edu</p>

<div style="font-style: normal; font-variant: normal; font-weight: normal; margin-bottom: 7pt; margin-left: 0pt; margin-right: 0pt; margin-top: 0pt; text-align: left; text-decoration: none; text-indent: 0pt; text-transform: none" class="pBodyCMT">Opinions herein are solely those of jim warner. The University has no opinions, and if they did, these would not be them. </div>
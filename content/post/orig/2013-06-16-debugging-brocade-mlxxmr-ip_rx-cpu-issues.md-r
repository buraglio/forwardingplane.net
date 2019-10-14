I recently had the need to debug a run away ip_rx process on an older Brocade MLX.  For anyone that has had to do any type of low level debugging on the Brocade (Foundry) platform, you know that there many somewhat deep level diagnostics that are possible.  The debug (like cisco debug) is a bit lacking, but the dm, LP and MP commands are very useful (and a tad scary). Regardless, I&#8217;ve had to utilize them a lot in the last few years so my aversion to using them has been pretty much completely callused over.

So, when there was notification of CPU issues (common on the platform in environments I&#8217;m familiar with), I started poking around.  First off, the  <a href="http://www.brocade.com/downloads/documents/product_manuals/B_NetIron/Brocade_XMRMLX_05200_DiagnosticGuide.pdf" target="_blank">diagnostic documents</a> are your friend.  They&#8217;re fairly deep and wide in scope.  After looking at the cpu, it was pretty clear what the culprit was.

rtr4-2#sh cpu-utilization | e 0

&#8230; Usage average for all tasks in the last 1 seconds  &#8230;  
==========================================================  
Name            us/sec        %

idle                    68435           11  
ip_rx                   724619          72  
ospf                    36942           3  
snmp                    82753           8

I needed to get info on that ip_rx process.  Google actually wasn&#8217;t terribly helpful, so I dig out what I wanted, except for the process for breaking into the management module monitor mode.  The golden ticket ended up being &#8220;ctrl+y m enter&#8221; from the console.  That drops you into the OS mode or management module monitor mode that looks like this.[<img class="alignright  wp-image-674" alt="Screen Shot 2013-06-16 at 7.04.20 PM" src="http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM.png" width="552" height="281" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM.png 789w, http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM-300x152.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM-550x280.png 550w" sizes="(max-width: 552px) 100vw, 552px" />](http://www.forwardingplane.net/wp-content/uploads/2013/06/Screen-Shot-2013-06-16-at-7.04.20-PM.png)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

Basically this is what I gathered for the Brocade TAC.

<pre>MP-1 OS&gt;set sample-task ip_rx
MP-1 OS&gt;set sample-rate 5
MP-1 OS&gt;show sample
CPU Sample: Trace... (Repeat)
202e4eb8&lt;2021ec08&lt;202e5c18&lt;202e6238&lt;2030c2c4&lt;202ec2d8&lt;202eac00&lt;202eac74
 .....
MP-1 OS&gt;set sample-rate 0
MP-1 OS&gt;exit
Back to Application console...</pre>

Setting the task to sample is pretty simple:set sample-task <task>

<pre>set sample-rate</pre>

to show the sample, simply

<pre>show sample</pre>

and then to disable the sampling

<pre>set sample-rate 0</pre>

This can be used to gather all kinds of disgnostic data for seemingly any running process for the brocade TAC to decipher.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-673" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-673" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-673" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-673" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/06/debugging-brocade-mlxxmr-ip_rx-cpu-issues/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
I was recently helping my brother-in-law out with the new [Seagate FreeAgent GoFlex Desk 3 TB USB 3.0 External Hard Drive](http://www.amazon.com/gp/product/B0045JLPNI?ie=UTF8&tag=nickburaglioc-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B0045JLPNI)<img src="http://www.assoc-amazon.com/e/ir?t=nickburaglioc-20&#038;l=as2&#038;o=1&#038;a=B0045JLPNI" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> he had purchased to do time machine backups on his mac. I personally have the 2t version and have been pretty happy with it, save for one small incident that I think was my fault that required some basic data recovery.  
Since the drive comes in a file system that is not HFS+ Journaled, it needed to be reformatted to support time machine backups.  
Simple, right? &#8220;A five minute process&#8221; I told him.  
Well, I was wrong. This drive just could <span style="font-weight:bold;">not</span> be formatted or re-partitioned using the standard OSX disk utility. I walked him through it on the phone. Partition failure. It threw some cryptic error that I had not seen before in 15 years of using a mac. I kinda figured it was something he was missing since I&#8217;m pretty awful at phone support, and if it wasn&#8217;t, I wanted to see the error, so I drive over there.  
Upon arriving, low and behold, it was in fact an error I&#8217;d never seen. I tried 3 more times to partition and format the drive and once just to format it. Same errors every time, it would start and then throw an error that it had failed or that it had lost communication with the drive.  
So, to test, I dropped to the trusty cli to see if I could do it from there.

From the Terminal app (/Applications/Utilities/Terminal) I issued the command 

<div>
  <span><br /></span>
</div>

<div>
  <span>diskutil eraseDisk HFS+ Backup disk1</span></p> 
  
  <p>
    Which was able to quickly accomplish the task. From there, I was able to mount and manipulate it in the Disk Utility (/Applicaations/Utilities/Disk Utility). Since I had not enabled the journal from the original command I reformatted the drive with MacOS X Entended (Journaled) and then it was ready to be a Time machine disk.
  </p>
  
  <p>
    I believe I could have done this all in one step using the command
  </p>
</div>

<div>
  <span><br /></span>
</div>

<div>
  <span><span>diskutil eraseDisk &#8220;Journaled HFS+&#8221; Backup disk1</span>.</span></p>
</div>

<div>
  I&#8217;m still unsure why Disk Utility would not work.</p> 
  
  <p>
    </div> 
    
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
              <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-41" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
            </li>
            <li class="share-email">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
            </li>
            <li class="share-print">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/" target="_blank" title="Click to print"><span>Print</span></a>
            </li>
            <li class="share-linkedin">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-41" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
            </li>
            <li class="share-facebook">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-41" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
            </li>
            <li class="share-reddit">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
            </li>
            <li class="share-tumblr">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
            </li>
            <li class="share-pinterest">
              <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-41" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
            </li>
            <li class="share-pocket">
              <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/02/seagate-freeagent-3t-drive-on-a-mac/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
            </li>
            <li class="share-end">
            </li>
          </ul>
        </div>
      </div>
    </div>

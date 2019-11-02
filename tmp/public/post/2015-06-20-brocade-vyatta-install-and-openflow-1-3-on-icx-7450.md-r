I recently had a need to test OpenFlow on the brocade ICX 7450 for a fairly good sized, high visibility [project](http://scinet.supercomputing.org). The basic goal is pretty simple, Layer2 path provisioning. Straightforward and fairly well supported in OpenFlow, even from the early days. To do this, the idea was to use a turnkey platform, that way there is one throat to choke if there are issues. I landed on the [Brocade Vyatta controller](http://www1.brocade.com/forms/jsp/vyatta-controller/download.jsp) (which is essentially ODL), and the ICX. Below is a rough account of getting this up and working to the point of testing. For the purposes of this I used BVC 1.3 and an ICX 7450. The docs for the BVC are actually pretty good if you read them. I found the google searching for the docs led to 9/10 links to brocade being 404 errors. My guess is that they restructured their site and did not alias anything. Minor frustration since my guess is that most folks search using a search engine rather than going to the site and searching from there. The link to the configuration guide I used for the ICX is [here](http://www.brocade.com/content/brocade/en/backend-content/pdf-page.html?/content/dam/common/documents/content-types/configuration-guide/fastiron-08030-sdnguide.pdf).

Once I grabbed the software, which requires registration, I went on to try to build this on CentOS 6.6. After some hurdles that I didn&#8217;t expect, I went and actually read the doc for BVC and found that ubuntu is a requirement. Another minor annoyance, but surmountable pretty easily. Enterprise customers are probably not going to want to have a one-off from RHEL/CentOS even if I don&#8217;t have a strong preference either way. Now that the VM is up and running with just over the minimum requirements, time to log in and get to work. This is assuming you have the code actually on the server already.

<pre>apt-get install -y unzip curl wget python-pip  
curl -sL https://deb.nodesource.com/setup | sudo bash - 
sudo apt-get install -y nodejs 
unzip -o bvc-1.3.0.zip -d /opt 
unzip -o bvc-dependencies-1.3.0.zip -d /opt 
unzip -o bvc-app-pathexplorer-packaging-1.2.0.zip -d /opt 
cd /opt/bvc 
./install
</pre>

The output should look something like this

<pre>root@bvc:/opt/bvc# ./install
 Brocade Vyatta Controller Installation

 Starting @ : 2015-06-17 15:31:15.564202

 Performing prerequisite check ...
 JDK Check ................................ [ OK ]
 CPU Count Check: ......................... [ OK ]
 Memory Size Check: ....................... [ OK ]

 Running pre-install scripts ...

 Unpacking archives ....................... [ OK ]

 Setting up karaf container ............... [ OK ]

 Running controller pre-install scripts ...

 Configuring base features ................ [ OK ]
 Start controller ......................... [ OK ]
 Waiting for base initialization .......... [ OK ]

 Configuring all features ................. [ OK ]
 Adding Repositories ...................... [ OK ]
 Adding Features .......................... [ OK ]

 Running controller post install scripts ...

 Running install scripts ...


 Stopping NODEJS server 9000 .............. [ OK ]
 Starting NODEJS server  .................. [ OK ]
   Server @ http://10.42.44.20:9000/

 Install completed @ :  2015-06-17 15:32:26.464365
</pre>

Monitoring the connection to the controller from the controller can be accomplished by using the included tool: /opt/bvc/bin/taillog which operates just like you think, by tailing a log file.

Checking for capability can be pretty easily accomplished by looking at the restconf modules:

<pre>http://&lt;IP address&gt;:8181/restconf/modules
</pre>

Now, for the ICX, I was under the impression that OpenFlow was in the base code. This is a true statement, however, I made a bad assumption that it was in _all_ code for that platform. Not so. After banging around and reading release notes as well as contacting my SE, I found that the code that it shipped with did _not_ support openflow, so I would need to upgrade it.

_The ICX 7450 (and probably others) requires at least Version 08.0.30aa for OpenFlow support. Earlier versions will be lacking in the entire command hierarchy, even for older versions of OpenFlow._

**Brocade ICX 7450 configuration**

From the console:

<pre>ip address 10.42.44.30 255.255.255.224
no ip dhcp-client enable
ip default-gateway 10.42.44.1
ip dns server-address 10.42.2.2
clock timezone us central
clock summer-time
logging host 10.42.44.7
logging enable user-login
logging enable config-changed
ntp 
server 10.42.2.2

interface ethernet 1/1/1 
port-name port1

crypto key generate rsa modulus 2048
ip ssh  authentication-retries 5
ip ssh timeout 120 
ip ssh key-authentication yes
username buraglio enable
username buraglio privilege 0
username buraglio password brocade

openflow enable ofv130 
openflow controller 10.42.44.20
system-max openflow-flow-entries 3072
</pre>

Thoughts:

OpenFlow wants to use SSL by default. When configuring this it failed in a way that is not intuitive _at all_. To get it running quickly, you need to disable SSL, which I absolutely _do not_ recommended for anything production). If you see anything other than this, the OpenFlow connection isn&#8217;t working

<pre>SSH@icx-of-test#sh openflow controller
Openflow controller information

--------------------------------------------------------------------------------
  Controller   Mode      TCP/SSL   IP-address        Port   Status
--------------------------------------------------------------------------------
  1  (Equal)   active    TCP       10.42.44.20     6653   OPENFLOW_ESTABLISHED
</pre>

This command will make it talk to the BVC over unencrypted TCP:

<pre>openflow controller ip-address 10.42.44.20 no-ssl port 6653 
</pre>

To make this work over SSL requires pulling the certificates into the device from the controller. I am still working on this for consideration in a production environment.

Path explorer has most of the interesting bits in it.

[<img class="alignright size-full wp-image-1297" src="http://www.forwardingplane.net/wp-content/uploads/2015/06/BVC-4.png" alt="BVC-4" width="1080" height="610" />](http://www.forwardingplane.net/wp-content/uploads/2015/06/BVC-4.png)

Other handy commands:

<pre>SSH@icx-of-test#sh openflow inter
  interface     Show interfaces where OpenFlow is enabled
  &lt;cr&gt;
SSH@icx-of-test#sh openflow interface

Total number of Openflow interfaces: 2

Port   Link   Speed Tag MAC            OF-portid   Name           Mode
1/1/1  Up     1G    No  cc4e.248b.4570 1           port1          Hybrid-Layer23
1/1/48 Down   None  No  cc4e.248b.459f 48          port48         Hybrid-Layer23
</pre>

The topology explorer is pretty cool, lots of eye candy.

[<img class="alignright size-full wp-image-1294" src="http://www.forwardingplane.net/wp-content/uploads/2015/06/BVC-1.png" alt="BVC-1" width="996" height="754" />](http://www.forwardingplane.net/wp-content/uploads/2015/06/BVC-1.png)

Random Thoughts:

  * Restarting the BVC causes the topology to need to rebuild, as one would expect. The ICX took longer to show up in the controller than I expected. In fact, it never recovered until I intervened manually.
  * The Brocade ICX randomly rebooted while attempting to scp the bootloader code. I never figured out why.
  * The ICX stopped responding to SSH for some reason. The only way I  
    could recover it was to reboot. Concerning from a management standpoint, but I suspect it was an anomaly.

In the next post I&#8217;ll explore the actual provisioning and the SSL configuration.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1293" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1293" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1293" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1293" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2015/06/brocade-vyatta-install-and-openflow-1-3-on-icx-7450/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
A bit of back history: I came from BSD land. I was a FreeBSD user from way back in the 1990s. BSD land is a land of secure boxes and very high uptimes. It&#8217;s also a land of arguably clunky package support, a lot of compiling by hand and these days, not nearly as encompassing package and network tuning support. [I decided to move to Linux](http://www.forwardingplane.net/2011/06/better-support-for-linux-and-annoyed-about-it/ "Better support for Linux (and annoyed about it)") a while ago, reluctantly, and chose Debian as my flavor of choice. I do love debian, however, I very quiuckly realized that even debian is a bit of a fringe OS build of Linux. Commercial support is nearly all based on RHEL. Folks that run RHEL also run CentOS. We run both in my day job. About a year ago to I, once again, decided I needed to learn CentOS.

There are a lot of posts about building floodlight as an openflow controller. I used this tutorial <a href="http://networkstatic.net/floodlight-openflow-controller-gui-applet/" target="_blank">Brent Salisbury did</a> to build mine. There is a good one on the <a href="http://floodlight.openflowhub.org/getting-started/" target="_blank">openflow hub</a> site as well. I&#8217;ve found that many are based on Debian or Ubuntu, which can be subtly different than a CentOS / RHEL experience.

&nbsp;

In CentOS, log in and sudo -s or su to root. Install the prereqs:

_yum -y install build-essential default-jdk ant python-dev eclipse git_  
_mkdir /services/floodlight_  
_cd /services/floodlight/_  
_git clone git://github.com/floodlight/floodlight.git  
ant_

Start floodlight in the background.  
_./floodlight.sh &_

Because I&#8217;m terrible at looking at directions, I went to the base URL. This will yield an error that looks something like this:  
_{&#8220;name&#8221;:&#8221;Not Found&#8221;,&#8221;error&#8221;:true,&#8221;throwable&#8221;:null,&#8221;description&#8221;:&#8221;The server has not found anything matching the request URI&#8221;,&#8221;success&#8221;:false,&#8221;informational&#8221;:false,&#8221;code&#8221;:404,&#8221;reasonPhrase&#8221;:&#8221;Not Found&#8221;,&#8221;uri&#8221;:&#8221;http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5&#8243;,&#8221;serverError&#8221;:false,&#8221;connectorError&#8221;:false,&#8221;clientError&#8221;:true,&#8221;globalError&#8221;:false,&#8221;redirection&#8221;:false,&#8221;recoverableError&#8221;:false}_  
The right way to access floodlight is to use the entire URL:

http://<address>:8080/ui/index.html

Learn from my stupidity.

&nbsp;

Here is a script to build it for you:

<pre>#!/bin/bash

echo "Installing prerequisits:"
yum -y install build-essential default-jdk ant python-dev eclipse git

echo "Installing floodlight to /services/floodight/"
mkdir /services/floodlight
cd /services/floodlight/
git clone git://github.com/floodlight/floodlight.git
ant

echo "Starting floodlight:"

./floodlight.sh&
echo "Floodlight started, point your beowser at http://&lt;address&gt;:8080/ui/index.html"</pre>

&nbsp;

&nbsp;

&nbsp;

<div id="geo-post-429" class="geo geo-post" style="display: none">
  <span class="latitude">40.072829</span><span class="longitude">-88.245813</span>
</div>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-429" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-429" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-429" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-429" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/02/building-a-floodlight-openflow-controller-on-centos-6/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

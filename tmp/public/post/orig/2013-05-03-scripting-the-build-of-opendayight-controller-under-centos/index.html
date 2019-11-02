<a href="https://twitter.com/blinken_lichten" target="_blank">Jon Langemak</a> has a great write up on <a href="http://www.dasblinkenlichten.com/installing-opendaylight-on-centos/" target="_blank">building the OpenDaylight controller under CentOS</a>. Since I&#8217;ll have to do this a bunch of times, I though tI&#8217;d take what he so generously put online and build a very rudimentary script for deploying ODC under CentOS. The prerequisites are that you already have an account and ssh key at the <a href="https://git.opendaylight.org/" target="_blank">OpenDaylight GIT repo</a> and that you <a href="http://www.revsys.com/writings/quicktips/turn-off-selinux.html" target="_blank">disable SELinux</a>.

Here is the script:

<pre>#!/bin/bash

# Install Opendaylight controller under CentOS
# by nick [at] buraglio.com http://www.twitter.com/buraglio
# http://www.forwardingplane.net
# Based on post by Jon Langemak (http://www.twitter.com/blinken_lichten)
# http://www.dasblinkenlichten.com/installing-opendaylight-on-centos/

yum="/usr/bin/yum"
servivce="/sbin/service"
chkconfig="/sbin/chkconfig"

echo "************************"
echo "************************"
echo "Disable SELINUX before starting this process"
echo "Edit the /etc/selinux/config file and restart the server"
echo "************************"
echo "************************"
echo "Change the username in the GIT section to your own"
echo "you'll need to create it and upload"
echo "your ssh key at git.opendaylight.org"
echo "************************"
echo "************************"

echo "************************"
echo "Installing Development tools and other deps"
echo "************************"
yum install -y wget vim java ant python eclipse-platform git
yum groupinstall -y “Development tools”A

echo "************************"
echo "Downloading and installing maven"
echo "************************"
wget http://www.poolsaboveground.com/apache/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.zip
unzip apache-maven-3.0.5-bin.zip -d /usr/share/
ln -s /usr/share/apache-maven-3.0.5/bin/mvn /usr/bin/mvn

echo "************************"
echo "Downloading GIT code"
echo "************************"
# Change the username here to your own, you'll need to create it and upload
# your ssh key at git.opendaylight.org
mkdir -p /services/opendaylight/
cd /services/opendaylight/
git clone https://buraglio@git.opendaylight.org/gerrit/p/controller.git

echo "************************"
echo "Building OpenDaylight Controller with Maven"
echo "************************"
cd controller/opendaylight/distribution/opendaylight/
mvn clean install

echo "************************"
echo "Configure Java Env variables"
echo "************************"
export JAVA_HOME=/usr/lib/jvm/java-1.6.0-openjdk.x86_64
echo "JAVA_HOME=/usr/lib/jvm/java-1.6.0-openjdk.x86_64" &gt;&gt; /etc/environment

echo "************************"
echo "Load the controller"
echo "************************"
cd /services/opendaylight/controller/opendaylight/distribution/opendaylight/target/distribution.opendaylight-0.1.0-SNAPSHOT-osgipackage/opendaylight

echo "************************"
echo "Start OpenDaylight OF controller"
echo "************************"
./run.sh</pre>

Once up and running, it&#8217;s pretty trivial to point something like an HP switch at the controller.  
For an HP5400, just decide what VLAN(s) you want to use OpenFlow on. I chose 999 as my test VLAN.

<pre>sw-5400-of# conf t
sw-5400-of(config)# vlan 999 name test-openflow999
sw-5400-of(vlan-999)# untagged A3-A4 
sw-5400-of(vlan-999)# exit
sw-5400-of(config)# openflow vlan 999
sw-5400-of(openFlow vlan-999)# enable
sw-5400-of(openFlow vlan-999)# controller "tcp:10.17.4.22:6633"
sw-5400-of(openFlow vlan-999)# exit       
sw-5400-of(openFlow)# exit
sw-5400-of(config)# 
w-5400-of(config)# exit
sw-5400-of# show openflow 

sw-5400-of# show openflow 

 Openflow Configuration

  Openflow aggregate VLANs [Disabled] :           
  Openflow aggregate management VlanId [0] : 0     
  Openflow second aggregate management VlanId [0] : 0     
  Openflow aggregate configuration VlanId [0] : 0     

  VID  State HW  Active controller Pseudo-URL                       Conn
  ---- ----- --- -------------------------------------------------- ----
  666  Off   On                                                     No  
  999  On    On  tcp:10.17.4.22:6633                                Yes</pre>

From here we can see the box in the openflow controller.

&nbsp;

&nbsp;

<p style="text-align: center;">
  <a href="http://www.forwardingplane.net/wp-content/uploads/2013/05/Screen-Shot-2013-05-03-at-4.20.03-PM.png"><img class="wp-image-636 aligncenter" alt="Screen Shot 2013-05-03 at 4.20.03 PM" src="http://www.forwardingplane.net/wp-content/uploads/2013/05/Screen-Shot-2013-05-03-at-4.20.03-PM.png" width="499" height="340" srcset="http://www.forwardingplane.net/wp-content/uploads/2013/05/Screen-Shot-2013-05-03-at-4.20.03-PM.png 1386w, http://www.forwardingplane.net/wp-content/uploads/2013/05/Screen-Shot-2013-05-03-at-4.20.03-PM-300x204.png 300w, http://www.forwardingplane.net/wp-content/uploads/2013/05/Screen-Shot-2013-05-03-at-4.20.03-PM-1024x698.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2013/05/Screen-Shot-2013-05-03-at-4.20.03-PM-550x375.png 550w" sizes="(max-width: 499px) 100vw, 499px" /></a>
</p>

&nbsp;

I&#8217;m still having some issues pushing flows, I&#8217;m sure I can work it out but here is a quick screencast of me trying to push a flow.  More posts will be added as soon as I can get the flows to push correctly.  
  
I suspect it is user error and I just need to read the docs.  More to come for sure.  This controller is very, very slick.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-627" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-627" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-627" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-627" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/05/scripting-the-build-of-opendayight-controller-under-centos/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>

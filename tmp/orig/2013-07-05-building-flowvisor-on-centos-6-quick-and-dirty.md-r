I had the need to build a FlowVisor instance under CentOS.  Since nearly all of the docs I could find were for debian, I threw this together.  I utilized this <a href="http://groups.geni.net/geni/wiki/FlowVisor" target="_blank">GENI doc</a> and the <a href="https://github.com/OPENNETWORKINGLAB/flowvisor/wiki/Installation-from-Source" target="_blank">github docs</a> as a simple reference.  This is the quick and dirty method I used:

Install the prerequisites:

<pre>sudo yum -y install ant eclipse java-1.6.0-openjdk.x86_64 git
sudo yum -y groupinstall "Development Tools"</pre>

Create my standard directories:

<pre>mkdir /services
cd /services
git clone git://github.com/OPENNETWORKINGLAB/flowvisor.git</pre>

Navigate, add user and install

<pre>cd flowvisor
adduser flowvisor
sudo make fvuser=flowvisor fvgroup=flowvisor install</pre>

Here is the relativde output I saw:

<pre>[root@collector flowvisor]# sudo make fvuser=flowvisor fvgroup=flowvisor install
ant
Buildfile: build.xml

init:
[mkdir] Created dir: /services/flowvisor/build
[mkdir] Created dir: /services/flowvisor/build.tests

compile:
[javac] Compiling 239 source files to /services/flowvisor/build
[javac] Note: /services/flowvisor/src/org/flowvisor/config/LoadConfig.java uses or overrides a deprecated API.
[javac] Note: Recompile with -Xlint:deprecation for details.

dist:
[mkdir] Created dir: /services/flowvisor/dist
[jar] Building jar: /services/flowvisor/dist/flowvisor.jar
[jar] Building jar: /services/flowvisor/dist/flowvisor.jar

BUILD SUCCESSFUL
Total time: 3 seconds
./scripts/install-script.sh
Using source dir: ./scripts/..
Installation prefix (/usr/local):
Install to different root directory ()
Installing FlowVisor into /usr/local with prefix=/usr/local as user/group flowvisor:flowvisor
Updating fvctl-xml.sh to fvctl-xml
Updating fvconfig.sh to fvconfig
Updating flowvisor.sh to flowvisor
Updating envs.sh to envs
Creating directories
Creating /usr/local/bin
Creating /usr/local/sbin
Creating /usr/local/libexec/flowvisor
Creating /usr/local/share/man/man1
Creating /usr/local/share/man/man8
Creating /usr/local/share/doc/flowvisor
Creating /usr/local/share/db/flowvisor
Creating /etc/flowvisor (owned by user=flowvisor  group=flowvisor)
Installing scripts
Installing SYSV startup script (not enabled by default)
Installing jars
Installing flowvisor.jar
Installing manpages
Installing FlowVisorDB
Installing configs
Installing Logrotate config
Installing documentation
Linking fvctl to fvctl-json
ln: creating symbolic link `fvctl': File exists
Generating a default config FlowVisor config
Trying to generate SSL Server Key with passwd from scripts/envs.sh
Generating cert with common name == flowvisor
keytool error: java.lang.Exception: Key pair not generated, alias &lt;mykey&gt; already exists
Enter password for account 'fvadmin' on the flowvisor:
Generating default config in db
Outputing config file /etc/flowvisor/config.json</pre>

Start the controller:

<pre>sudo /etc/init.d/flowvisor start</pre>

Output from controller starting:

<pre>Starting flowvisor with the configuration stored in DB
If DB unpopulated, load config using 'fvconfig load config.json'
[root@collector flowvisor]#
Message from syslogd@collector at Jul  3 08:49:51 ...
1&gt;Jul  3 08:49:51 flowvisor: ERROR none : log level enabled: CRIT

Message from syslogd@collector at Jul  3 08:49:51 ...
1&gt;Jul  3 08:49:51 flowvisor: ERROR none : log level enabled: ALERT

Message from syslogd@collector at Jul  3 08:49:51 ...
1&gt;Jul  3 08:49:51 flowvisor: WARN none : log level enabled: WARN</pre>

<pre>This yields a "working" flow visor.

Lock it down with a password:</pre>

<pre>yum -y install pwgen
test -f /etc/flowvisor.passwd || sudo sh -c 'pwgen -sB 24 &gt; /etc/flowvisor.passwd'
service flowvisor restart</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-714" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-714" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-714" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-714" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2013/07/building-flowvisor-on-centos-6-quick-and-dirty/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
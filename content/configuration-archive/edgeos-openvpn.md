---
id: 1604
title: EdgeOS OpenVPN
date: 2019-02-18T14:05:37-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=1604
---
OpenVPN is a great technology but can be a bit of a bear to configure. A large part of the complexity with OpenVPN is the certificates, many are put off my them and for good reason. They can be confusing and hard to follow. The certificates can be generated off box pretty easily and that&#8217;s how I tend to do it. This configuration should work on both [EdgeMAX](https://www.ui.com/products/#edgemax) and [Unifi USG](https://www.ui.com/unifi-routing/unifi-security-gateway-pro-4/) devices, although the latter will require some additional work to make it persist across provisioning events. 

On the linux/mac/unix host:

<pre class="wp-block-preformatted">cd /usr/share/easy-rsa <br />./build-ca</pre>

  
The following is the output from a test run, you will need some information or be willing to make it up. 

<pre class="wp-block-preformatted">Generating a 2048 bit RSA private key<br /> ……………+++++<br /> …………………+++++<br /> writing new private key to 'ca.key'<br /> You are about to be asked to enter information that will be incorporated<br /> into your certificate request.<br /> What you are about to enter is what is called a Distinguished Name or a DN.<br /> There are quite a few fields but you can leave some blank<br /> For some fields there will be a default value,<br /> If you enter '.', the field will be left blank.<br /> Country Name (2 letter code) [US]:US<br /> State or Province Name (full name) [CA]:IL<br /> Locality Name (eg, city) [SanFrancisco]:Champaign<br /> Organization Name (eg, company) [Fort-Funston]:Your ORG Name<br /> Organizational Unit Name (eg, section) [MyOrganizationalUnit]:Network engineering<br /> Common Name (eg, your name or your server's hostname) [Fort-Funston CA]:gw.yourcompany.com<br /> Name [EasyRSA]:OpenVPN CA<br /> Email Address [me@myhost.mydomain]:yourgroupemail@yourcompany.com</pre>

Now build the next pieces:

<pre class="wp-block-preformatted">./build-key-server server <br />Generating a 2048 bit RSA private key<br /> …..+++++<br /> ……………………+++++<br /> writing new private key to 'server.key'<br /> You are about to be asked to enter information that will be incorporated<br /> into your certificate request.<br /> What you are about to enter is what is called a Distinguished Name or a DN.<br /> There are quite a few fields but you can leave some blank<br /> For some fields there will be a default value,<br /> If you enter '.', the field will be left blank.<br /> Country Name (2 letter code) [US]:<br /> State or Province Name (full name) [CA]: IL<br /> Locality Name (eg, city) [SanFrancisco]:Champaign<br /> Organization Name (eg, company) [Fort-Funston]:Your ORG Name<br /> Organizational Unit Name (eg, section) [MyOrganizationalUnit]:Network engineering<br /> Common Name (eg, your name or your server's hostname) [server]:<br /> Name [EasyRSA]:OpenVPN Server<br /> Email Address [me@myhost.mydomain]:yourgroupemail@yourcompany.com<br /> Please enter the following 'extra' attributes<br /> to be sent with your certificate request<br /> A challenge password []:<br /> An optional company name []:<br /> Using configuration from /usr/share/easy-rsa/openssl.cnf<br /> Can't open /usr/share/easy-rsa/keys/index.txt.attr for reading, No such file or directory<br /> 139640007534336:error:02001002:system library:fopen:No such file or directory:../crypto/bio/bss_file.c:72:fopen('/usr/share/easy-rsa/keys/index.txt.attr','r')<br /> 139640007534336:error:2006D080:BIO routines:BIO_new_file:no such file:../crypto/bio/bss_file.c:79:<br /> Check that the request matches the signature<br /> Signature ok<br /> The Subject's Distinguished Name is as follows<br /> countryName           :PRINTABLE:'US'<br /> stateOrProvinceName   :PRINTABLE:'IL'<br /> localityName          :PRINTABLE:'Champaign'<br /> organizationName      :PRINTABLE:'Your ORG Name'<br /> organizationalUnitName:PRINTABLE:'Network engineering'<br /> commonName            :PRINTABLE:'server'<br /> name                  :PRINTABLE:'OpenVPN Server'<br /> emailAddress          :IA5STRING:'yourgroupemail@yourcompany.com'<br /> Certificate is to be certified until Feb 15 19:49:14 2029 GMT (3650 days)<br /> Sign the certificate? [y/n]:y<br /> 1 out of 1 certificate requests certified, commit? [y/n]y<br /> Write out database with 1 new entries<br /> Data Base Updated</pre>

Now build the client certificates

<pre class="wp-block-preformatted">./build-key client1<br /> Generating a 2048 bit RSA private key<br /> .+++++<br /> ……………………………………………………………………….+++++<br /> writing new private key to 'client1.key'<br /> You are about to be asked to enter information that will be incorporated<br /> into your certificate request.<br /> What you are about to enter is what is called a Distinguished Name or a DN.<br /> There are quite a few fields but you can leave some blank<br /> For some fields there will be a default value,<br /> If you enter '.', the field will be left blank.<br /> Country Name (2 letter code) [US]:<br /> State or Province Name (full name) [CA]:IL<br /> Locality Name (eg, city) [SanFrancisco]:Champaign<br /> Organization Name (eg, company) [Fort-Funston]:Your ORG Name<br /> Organizational Unit Name (eg, section) [MyOrganizationalUnit]:Network Engineering<br /> Common Name (eg, your name or your server's hostname) [client1]:<br /> Name [EasyRSA]:OpenVPN Client<br /> Email Address [me@myhost.mydomain]:yourgroupemail@yourcompany.com<br /> Please enter the following 'extra' attributes<br /> to be sent with your certificate request<br /> A challenge password []:<br /> An optional company name []:<br /> Using configuration from /usr/share/easy-rsa/openssl.cnf<br /> Check that the request matches the signature<br /> Signature ok<br /> The Subject's Distinguished Name is as follows<br /> countryName           :PRINTABLE:'US'<br /> stateOrProvinceName   :PRINTABLE:'IL'<br /> localityName          :PRINTABLE:'Champaign'<br /> organizationName      :PRINTABLE:'Your ORG Name'<br /> organizationalUnitName:PRINTABLE:'Network Engineering'<br /> commonName            :PRINTABLE:'client1'<br /> name                  :PRINTABLE:'OpenVPN Client'<br /> emailAddress          :IA5STRING:'yourgroupemail@yourcompany.com'<br /> Certificate is to be certified until Feb 15 19:53:55 2029 GMT (3650 days)<br /> Sign the certificate? [y/n]:y<br /> 1 out of 1 certificate requests certified, commit? [y/n]y<br /> Write out database with 1 new entries<br /> Data Base Updated<br /><br /><br /></pre>

Generate the last piece:

<pre class="wp-block-preformatted">./build-dh<br /> Generating DH parameters, 2048 bit long safe prime, generator 2<br /> This is going to take a long time<br /> …………………………………………………………………+…………………………………………………………………..+…………………….+……………………………………………………………………………….+……………………………………..+………..+………………………………………………………………….+…………………………..+…………………………………………..+……………………………………………………………..+…………………………………….+…………………………………..+……………………………+…………………………………………………..+……………………………………+……………………………………………………………………………………..+………………………………………………………………………………………………………………………………………………………………………………+……+…………………………………………………………………………………………………………………………………………….+……………………………….+……………………………….+………………………………………………………………………………………………………………………………………….+………………………………………………………………….+…+……………………………………………+……………………………………………………………………………………………………….+…………………………………………………………………..+…………………………………………………………………………………………………………………..+……………………………..+….+……………………………………………………………………………………………………………………………………………………………………………………………………………………………………………..+…………………………………………………………………………………………………………………………………………………………………………+………………..++<em>++</em>++<em>++</em><br /></pre>

On the UBNT:

<pre class="wp-block-preformatted">mkdir /config/auth/keys/<br /></pre>

Now that you have all of the files and directory structure, head back to your host and scp them over to the ubiquity into /config/auth/keys

<pre class="wp-block-preformatted">cd /usr/share/easy-rsa/keys<br />scp  * username@ubnt.net:/config/auth/keys/<br /></pre>

Now that the keys are all created and safe, head back over to the UBNT and start configuring the device to support what you just made

<pre class="wp-block-preformatted">set interfaces openvpn vtun0 mode server <br />set interfaces openvpn vtun0 server subnet 172.16.61.0/27 <br />set interfaces openvpn vtun0 tls ca-cert-file /config/auth/keys/ca.crt <br />set interfaces openvpn vtun0 tls cert-file /config/auth/keys/server.crt <br />set interfaces openvpn vtun0 tls key-file /config/auth/keys/server.key <br />set interfaces openvpn vtun0 tls dh-file /config/auth/keys/dh2048.pem <br />set interfaces openvpn vtun0 encryption aes192 <br /><br />set interfaces openvpn vtun0 openvpn-option "--keepalive 8 30" <br />set interfaces openvpn vtun0 openvpn-option "--comp-lzo" <br />set interfaces openvpn vtun0 openvpn-option "--duplicate-cn" <br />set interfaces openvpn vtun0 openvpn-option "--user nobody - group nogroup" <br />set interfaces openvpn vtun0 openvpn-option "--verb 1" <br />set interfaces openvpn vtun0 openvpn-option "--proto udp6" <br />set interfaces openvpn vtun0 openvpn-option "--port 1194" <br />set interfaces openvpn vtun0 server push-route 10.2.0.0/16 <br />set interfaces openvpn vtun0 server name-server 10.2.9.10 <br />set firewall name WAN_LOCAL rule 20 action accept <br />set firewall name WAN_LOCAL rule 20 description "Allow OpenVPN clients in" <br />set firewall name WAN_LOCAL rule 20 destination port 1194 <br />set firewall name WAN_LOCAL rule 20 log disable <br />set firewall name WAN_LOCAL rule 20 protocol udp <br />set service nat rule 5010 description "Masquerade for WAN" <br />set service nat rule 5010 outbound-interface eth0 <br />set service nat rule 5010 type masquerade </pre>

I recommend [Viscosity](https://www.sparklabs.com/viscosity/) as the client &#8211; it&#8217;s inexpensive and very reliable. 

My configuration was largely based on the reference [here](https://medium.com/server-guides/how-to-setup-an-openvpn-server-on-a-unifi-usg-e33ea2f6725d). 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1604" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1604" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1604" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1604" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/edgeos-openvpn/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>
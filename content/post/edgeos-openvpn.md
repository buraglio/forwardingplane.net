---
title: 'EdgeOS OpenVPN'
date: Mon, 18 Feb 2019 20:05:37 +0000
draft: false
---

OpenVPN is a great technology but can be a bit of a bear to configure. A large part of the complexity with OpenVPN is the certificates, many are put off my them and for good reason. They can be confusing and hard to follow. The certificates can be generated off box pretty easily and that's how I tend to do it. This configuration should work on both [EdgeMAX](https://www.ui.com/products/#edgemax) and [Unifi USG](https://www.ui.com/unifi-routing/unifi-security-gateway-pro-4/) devices, although the latter will require some additional work to make it persist across provisioning events.

On the linux/mac/unix host:

```
cd /usr/share/easy-rsa   
./build-ca
```

  
The following is the output from a test run, you will need some information or be willing to make it up.

```
 Generating a 2048 bit RSA private key  
 ……………+++++  
 …………………+++++  
 writing new private key to 'ca.key'  
 You are about to be asked to enter information that will be incorporated  
 into your certificate request.  
 What you are about to enter is what is called a Distinguished Name or a DN.  
 There are quite a few fields but you can leave some blank  
 For some fields there will be a default value,  
 If you enter '.', the field will be left blank.  
 Country Name (2 letter code) \[US\]:US  
 State or Province Name (full name) \[CA\]:IL  
 Locality Name (eg, city) \[SanFrancisco\]:Champaign  
 Organization Name (eg, company) \[Fort-Funston\]:Your ORG Name  
 Organizational Unit Name (eg, section) \[MyOrganizationalUnit\]:Network engineering  
 Common Name (eg, your name or your server's hostname) \[Fort-Funston CA\]:gw.yourcompany.com  
 Name \[EasyRSA\]:OpenVPN CA  
 Email Address \[me@myhost.mydomain\]:yourgroupemail@yourcompany.com
```

Now build the next pieces:

```
 ./build-key-server server   
Generating a 2048 bit RSA private key  
 …..+++++  
 ……………………+++++  
 writing new private key to 'server.key'  
 You are about to be asked to enter information that will be incorporated  
 into your certificate request.  
 What you are about to enter is what is called a Distinguished Name or a DN.  
 There are quite a few fields but you can leave some blank  
 For some fields there will be a default value,  
 If you enter '.', the field will be left blank.  
 Country Name (2 letter code) \[US\]:  
 State or Province Name (full name) \[CA\]: IL  
 Locality Name (eg, city) \[SanFrancisco\]:Champaign  
 Organization Name (eg, company) \[Fort-Funston\]:Your ORG Name  
 Organizational Unit Name (eg, section) \[MyOrganizationalUnit\]:Network engineering  
 Common Name (eg, your name or your server's hostname) \[server\]:  
 Name \[EasyRSA\]:OpenVPN Server  
 Email Address \[me@myhost.mydomain\]:yourgroupemail@yourcompany.com  
 Please enter the following 'extra' attributes  
 to be sent with your certificate request  
 A challenge password \[\]:  
 An optional company name \[\]:  
 Using configuration from /usr/share/easy-rsa/openssl.cnf  
 Can't open /usr/share/easy-rsa/keys/index.txt.attr for reading, No such file or directory  
 139640007534336:error:02001002:system library:fopen:No such file or directory:../crypto/bio/bss\_file.c:72:fopen('/usr/share/easy-rsa/keys/index.txt.attr','r')  
 139640007534336:error:2006D080:BIO routines:BIO\_new\_file:no such file:../crypto/bio/bss\_file.c:79:  
 Check that the request matches the signature  
 Signature ok  
 The Subject's Distinguished Name is as follows  
 countryName           :PRINTABLE:'US'  
 stateOrProvinceName   :PRINTABLE:'IL'  
 localityName          :PRINTABLE:'Champaign'  
 organizationName      :PRINTABLE:'Your ORG Name'  
 organizationalUnitName:PRINTABLE:'Network engineering'  
 commonName            :PRINTABLE:'server'  
 name                  :PRINTABLE:'OpenVPN Server'  
 emailAddress          :IA5STRING:'yourgroupemail@yourcompany.com'  
 Certificate is to be certified until Feb 15 19:49:14 2029 GMT (3650 days)  
 Sign the certificate? \[y/n\]:y  
 1 out of 1 certificate requests certified, commit? \[y/n\]y  
 Write out database with 1 new entries  
 Data Base Updated
```

Now build the client certificates

```
./build-key client1  
 Generating a 2048 bit RSA private key  
 .+++++  
 ……………………………………………………………………….+++++  
 writing new private key to 'client1.key'  
 You are about to be asked to enter information that will be incorporated  
 into your certificate request.  
 What you are about to enter is what is called a Distinguished Name or a DN.  
 There are quite a few fields but you can leave some blank  
 For some fields there will be a default value,  
 If you enter '.', the field will be left blank.  
 Country Name (2 letter code) \[US\]:  
 State or Province Name (full name) \[CA\]:IL  
 Locality Name (eg, city) \[SanFrancisco\]:Champaign  
 Organization Name (eg, company) \[Fort-Funston\]:Your ORG Name  
 Organizational Unit Name (eg, section) \[MyOrganizationalUnit\]:Network Engineering  
 Common Name (eg, your name or your server's hostname) \[client1\]:  
 Name \[EasyRSA\]:OpenVPN Client  
 Email Address \[me@myhost.mydomain\]:yourgroupemail@yourcompany.com  
 Please enter the following 'extra' attributes  
 to be sent with your certificate request  
 A challenge password \[\]:  
 An optional company name \[\]:  
 Using configuration from /usr/share/easy-rsa/openssl.cnf  
 Check that the request matches the signature  
 Signature ok  
 The Subject's Distinguished Name is as follows  
 countryName           :PRINTABLE:'US'  
 stateOrProvinceName   :PRINTABLE:'IL'  
 localityName          :PRINTABLE:'Champaign'  
 organizationName      :PRINTABLE:'Your ORG Name'  
 organizationalUnitName:PRINTABLE:'Network Engineering'  
 commonName            :PRINTABLE:'client1'  
 name                  :PRINTABLE:'OpenVPN Client'  
 emailAddress          :IA5STRING:'yourgroupemail@yourcompany.com'  
 Certificate is to be certified until Feb 15 19:53:55 2029 GMT (3650 days)  
 Sign the certificate? \[y/n\]:y  
 1 out of 1 certificate requests certified, commit? \[y/n\]y  
 Write out database with 1 new entries  
 Data Base Updated  
  
  

```

Generate the last piece:

```
./build-dh  
 Generating DH parameters, 2048 bit long safe prime, generator 2  
 This is going to take a long time  
 …………………………………………………………………+…………………………………………………………………..+…………………….+……………………………………………………………………………….+……………………………………..+………..+………………………………………………………………….+…………………………..+…………………………………………..+……………………………………………………………..+…………………………………….+…………………………………..+……………………………+…………………………………………………..+……………………………………+……………………………………………………………………………………..+………………………………………………………………………………………………………………………………………………………………………………+……+…………………………………………………………………………………………………………………………………………….+……………………………….+……………………………….+………………………………………………………………………………………………………………………………………….+………………………………………………………………….+…+……………………………………………+……………………………………………………………………………………………………….+…………………………………………………………………..+…………………………………………………………………………………………………………………..+……………………………..+….+……………………………………………………………………………………………………………………………………………………………………………………………………………………………………………..+…………………………………………………………………………………………………………………………………………………………………………+………………..++_++_++_++_  

```

On the UBNT:

```
mkdir /config/auth/keys/  

```

Now that you have all of the files and directory structure, head back to your host and scp them over to the ubiquity into /config/auth/keys

```
cd /usr/share/easy-rsa/keys  
scp  \* username@ubnt.net:/config/auth/keys/  

```

Now that the keys are all created and safe, head back over to the UBNT and start configuring the device to support what you just made

```
set interfaces openvpn vtun0 mode server   
set interfaces openvpn vtun0 server subnet 172.16.61.0/27   
set interfaces openvpn vtun0 tls ca-cert-file /config/auth/keys/ca.crt   
set interfaces openvpn vtun0 tls cert-file /config/auth/keys/server.crt   
set interfaces openvpn vtun0 tls key-file /config/auth/keys/server.key   
set interfaces openvpn vtun0 tls dh-file /config/auth/keys/dh2048.pem   
set interfaces openvpn vtun0 encryption aes192   
  
set interfaces openvpn vtun0 openvpn-option "--keepalive 8 30"   
set interfaces openvpn vtun0 openvpn-option "--comp-lzo"   
set interfaces openvpn vtun0 openvpn-option "--duplicate-cn"   
set interfaces openvpn vtun0 openvpn-option "--user nobody - group nogroup"   
set interfaces openvpn vtun0 openvpn-option "--verb 1"   
set interfaces openvpn vtun0 openvpn-option "--proto udp6"   
set interfaces openvpn vtun0 openvpn-option "--port 1194"   
set interfaces openvpn vtun0 server push-route 10.2.0.0/16   
set interfaces openvpn vtun0 server name-server 10.2.9.10   
set firewall name WAN\_LOCAL rule 20 action accept   
set firewall name WAN\_LOCAL rule 20 description "Allow OpenVPN clients in"   
set firewall name WAN\_LOCAL rule 20 destination port 1194   
set firewall name WAN\_LOCAL rule 20 log disable   
set firewall name WAN\_LOCAL rule 20 protocol udp   
set service nat rule 5010 description "Masquerade for WAN"   
set service nat rule 5010 outbound-interface eth0   
set service nat rule 5010 type masquerade 
```

I recommend [Viscosity](https://www.sparklabs.com/viscosity/) as the client - it's inexpensive and very reliable.

My configuration was largely based on the reference [here](https://medium.com/server-guides/how-to-setup-an-openvpn-server-on-a-unifi-usg-e33ea2f6725d).
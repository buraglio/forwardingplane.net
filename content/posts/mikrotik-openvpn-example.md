---
title: 'Mikrotik OpenVPN server'
date: Mon, 18 Feb 2019 20:14:40 +0000
draft: false
---

Mikrotik is one of my favorite routing and MPLS platforms for doing lab and small ISP work. This one is pretty darned easy if you're willing to use self-signed certificates, and pretty trivial to add legitimate certificates if you are so inclined.

```
/certificate add name=ca common-name=ca key-usage=key-cert-sign,crl-sign  
/certificate sign ca ca-crl-host=10.255.255.4 name=ca  
/certificate export-certificate ca  
/certificate add name=gw-dsl common-name=gw.yourcompany.com  
/certificate add name=vpnclient1 common-name=client1  
/certificate sign gw-dsl ca=ca name=gw.yourcompany.com  
/certificate sign vpnclient1 ca=ca name=client1   
/ip pool add name=ovpn-pool range=10.2.98.2-10.2.98.19  
/ppp profile add name=ovpn local-address=10.2.98.1 remote-address=ovpn-pool  
/ppp secret add name=buraglio profile=ovpn password=ExamplePasswordDude  
/interface ovpn-server server set enabled=yes certificate=server auth=sha1 cipher=aes256 port=1194 netmask=24 require-client-certificate=yes mode=ip  
/certificate export-certificate client1  export-passphrase=ExamplePasswordDude
```

Largely based on [this example](https://delphinus.qns.net/xwiki/bin/view/Blog/Mikrotik%20OpenVPN%20in%2090%20seconds)
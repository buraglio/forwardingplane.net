---
title: 'Nokia SROS useful commands'
date: Tue, 19 Feb 2019 14:30:08 +0000
draft: false
---

Nokia (formerly Alcatel-Lucent, formerly Timetra) have an extremely robust routing platform, but it has some notable differences if you're coming from a vendor such as Cisco or Juniper (or any vendor platform in the enterprise space, really). Things like "VLANs" don't really exist, as this is more of a metro / carrier / customer provisioning style device, so modular concepts are expected and baked into the OS at the deepest layers, unlike many of the other vendor platforms that support it but it feels like an add-in or addendum to the base routing instance. Here are a few useful commands that I threw together when I was learning SROS. As Nokia has begun rebuilding the SROS CLI to be less of a one-off, these will become less important, but until SROS is totally gone, someone will need to know them.

Show all installed line cards

```
show card
```

Contextual configuration display. From anywhere in the hierarchy, to show that sections configuration simply type

```
info
```

To ascertain the service ID of a given SAP (service access point)

```
show service sap-using
```

Similar to a juniper rollback compare, the SROS environment keeps candidate configurations and they can by compared, or diff'd to the running configuration. This is super useful.

```
admin rollback compare active-cfg to latest-rb
```

Also similar to juniper, it is possible to monitor the statistics of a given port in near real time

```
monitor port 3/2/1 interval 3 repeat 999 rate
```

SROS is an MPLS powerhouse, knowing how to look at the LSPs is pretty critical

```
show router mpls lsp terminate   
show router mpls lsp transit   
show router mpls lsp  
show service id <vpls-id> all  
show service id <vpls-id> fdb detail 
```

VPRN commands

```
show port <port> associations   
show service id <vprn-id> all   
show router <vprn-id> interface   
show router <vprn-id> bgp summary   
show router <vprn-id> route-table   
show router <vprn-id> route-table protocol bgp-vpn   
show router <vprn-id> route-table <ip-address>   
show router <vprn-id> bgp routes <ip-prefix>/<net-size> detail   
show router <vprn-id> bgp next-hop   
show router <vprn-id> bgp neighbor <ip-address> received-routes   
show router <vprn-id> bgp neighbor <ip-address> advertised-routes   
oam vprn-ping <vprn-id> source <ip-address> destination <ip-address>   
oam vprn-trace <vprn-id> source <ip-address> destination <ip-address>   

```

Useful BGP commands

```
show router bgp summary    
show router bgp neighbor <neighbor> received-routes <ipv6>  
```

Showing logs

```
show log log-id <id>  
show log log-id 99  
show log event-control  

```

Showing environmentals

```
show chassis environment \[power-supply\]  
show router interface \[detail\]   
show port <port> optical
```

Showing and saving the configuration

```
admin display-config  
admin save  
admin save rollback
```
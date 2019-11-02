---
title: 'FreeRTR basic configurations'
date: Sat, 02 Mar 2019 17:00:49 +0000
draft: false
---

From the [freertr](http://freerouter.nop.hu/) website:

```
freeRouter is a free, open source router os process  
it speaks routing protocols, and (re)encapsulates packets on interfaces (a huge list of encapsulation and routing test cases can be found under self-test page)since it handles packets itself, it is independent of underlaying os capabilities(optionally, it can export forwarding tables through openflow to external switch)since it is an unprivilegized process, it receives and sends packets through socketsthere are external, privileged processes that place traffic to these sockets(it means that internet can be used as backplane for router processes) the command line tries to mimic the industry standards with one exception: no global routing table: every routedinterface must be in a virtual routing table positive side effect: there are no vrf-awareness questions
```

As notes in my [FreeRTR post](https://www.forwardingplane.net/2019/03/freertr-as-a-lab-environment/), FreeRTR is a wonderful alternative to labbing up protocols and provides an incredible array of protocol support. Below are my three router test configurations from a basic setup. They should be enough to get you started.

RTR1

```
  
   
hostname rtr1   
buggy   
!   
!   
vrf definition host   
exit   
!   
vrf definition vrf1   
rd 1:1   
exit   
!   
router isis4 1   
vrf vrf1   
net-id 48.1111.0000.1111.00   
traffeng-id ::   
is-type both   
redistribute connected   
exit   
!   
router isis6 1   
vrf vrf1   
net-id 48.1111.0000.1111.00   
traffeng-id ::   
is-type both   
segrout 10   
level2 segrout   
level1 segrout   
redistribute connected   
exit   
!   
!   
interface loopback0   
no description   
vrf forwarding vrf1   
ipv4 address 10.99.99.1 255.255.255.255   
ipv6 address 2001:db8:1111::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff   
router isis6 1 enable   
router isis6 1 circuit both   
router isis6 1 segrout index 1   
router isis6 1 segrout node   
no shutdown   
no log-link-change   
exit   
!   
interface loopback1   
no description   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet1   
no description   
lldp enable   
vrf forwarding vrf1   
ipv4 address 10.1.1.1 255.255.255.252   
ipv6 address 2001:db8:1111::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe   
mpls enable   
router isis6 1 enable   
router isis6 1 circuit both   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet2   
no to\_rt2\_ether2   
lldp enable   
vrf forwarding vrf1   
ipv4 address 10.1.4.1 255.255.255.252   
ipv6 address 2001:db8:1114::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe   
mpls enable   
router isis6 1 enable   
router isis6 1 circuit both   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet20001   
no description   
vrf forwarding host   
ipv4 address 10.255.255.254 255.255.255.0   
no shutdown   
no log-link-change   
exit   
!   
line tty1   
no login authentication   
exit   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
alias test bash command attach shell1 socat - exec:sh,ctty,pty,stderr   
alias test bash description   
alias test bash parameter optional   
!   
server telnet host   
security protocol telnet   
no login authentication   
vrf host   
exit   
!   
!   
end 
```

RTR2

```
hostname rtr2   
buggy   
!   
!   
vrf definition host   
exit   
!   
vrf definition vrf1   
rd 1:1   
exit   
!   
router isis4 1   
no vrf   
exit   
!   
router isis6 1   
vrf vrf1   
net-id 48.2222.0000.2222.00   
traffeng-id ::   
is-type both   
segrout 10   
level2 segrout   
level1 segrout   
redistribute connected   
exit   
!   
  
  
interface loopback0   
no description   
vrf forwarding vrf1   
ipv4 address 10.99.99.2 255.255.255.255   
ipv6 address 2001:db8:2222::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff   
router isis6 1 enable   
router isis6 1 circuit both   
router isis6 1 segrout index 1   
router isis6 1 segrout node   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet1   
description to\_rtr3\_ether2   
lldp enable   
vrf forwarding vrf1   
ipv4 address 10.1.3.2 255.255.255.252   
ipv6 address 2001:db8:1112::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe   
mpls enable   
router isis6 1 enable   
router isis6 1 circuit both   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet2   
no to\_rt1\_ether2   
lldp enable   
vrf forwarding vrf1   
ipv4 address 10.1.4.2 255.255.255.252   
ipv6 address 2001:db8:1114::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe   
mpls enable   
router isis6 1 enable   
router isis6 1 circuit both   
no shutdown   
no log-link-change   
exit   
  
  
!   
interface ethernet20001   
no description   
vrf forwarding host   
ipv4 address 10.255.255.254 255.255.255.0   
no shutdown   
no log-link-change   
exit   
!   
line tty1   
no login authentication   
exit   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
alias test bash command attach shell1 socat - exec:sh,ctty,pty,stderr   
alias test bash description   
alias test bash parameter optional   
!   
server telnet host   
security protocol telnet   
no login authentication   
vrf host   
exit   
!   
!   
end 
```

RTR3

```
hostname rtr3   
buggy   
!   
!   
vrf definition host   
exit   
!   
vrf definition vrf1   
rd 1:1   
exit   
!   
router isis4 1   
vrf vrf1   
net-id 48.3333.0000.3333.00   
traffeng-id ::   
is-type both   
redistribute connected   
exit   
!   
router isis6 1   
vrf vrf1   
net-id 48.3333.0000.3333.00   
traffeng-id ::   
is-type both   
segrout 10   
level2 segrout   
level1 segrout   
redistribute connected   
exit   
!   
interface loopback0   
no description   
vrf forwarding vrf1   
ipv4 address 10.99.99.3 255.255.255.255   
ipv6 address 2001:db8:3333::1 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff   
router isis6 1 enable   
router isis6 1 circuit both   
router isis6 1 segrout index 1   
router isis6 1 segrout node   
no shutdown   
no log-link-change   
exit   
!   
interface loopback1   
no description   
no shutdown   
no log-link-change   
exit   
!   
!   
interface ethernet1   
description to\_rtr2\_ether1   
lldp enable   
vrf forwarding vrf1   
ipv4 address 10.1.3.1 255.255.255.252   
ipv6 address 2001:db8:1112::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe   
mpls enable   
router isis6 1 enable   
router isis6 1 circuit both   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet2   
description to\_rtr1\_ether1   
lldp enable   
vrf forwarding vrf1   
ipv4 address 10.1.1.2 255.255.255.252   
ipv6 address 2001:db8:1111::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe   
mpls enable   
router isis6 1 enable   
router isis6 1 circuit both   
no shutdown   
no log-link-change   
exit   
!   
interface ethernet20001   
no description   
vrf forwarding host   
ipv4 address 10.255.255.254 255.255.255.0   
no shutdown   
no log-link-change   
exit   
!   
line tty1   
no login authentication   
exit   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
!   
alias test bash command attach shell1 socat - exec:sh,ctty,pty,stderr   
alias test bash description   
alias test bash parameter optional   
!   
server telnet host   
security protocol telnet   
no login authentication   
vrf host   
exit   
!   
!   
end 
```

Helpful show commands for this basic setup

```
 sh ipv4 route vrf1  
 sh ipv6 route vrf1 
```
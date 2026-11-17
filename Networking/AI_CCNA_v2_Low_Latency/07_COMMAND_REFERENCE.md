# IOS/IOS XE Command Reference

> Commands vary by platform and release. Use context-sensitive help and verify support.

## CLI and Files

```ios
enable
configure terminal
show running-config
show startup-config
copy running-config startup-config
show history
show version
show inventory
dir flash:
show boot
reload
```

## Interfaces and Neighbours

```ios
show ip interface brief
show ipv6 interface brief
show interfaces
show interfaces status
show interfaces counters errors
show interfaces description
show controllers
show arp
show ipv6 neighbors
show cdp neighbors detail
show lldp neighbors detail
```

## VLANs, Trunks and SVIs

```ios
show vlan brief
show interfaces switchport
show interfaces trunk
show mac address-table
show interfaces Vlan20

vlan 20
 name USERS
interface GigabitEthernet1/0/10
 switchport mode access
 switchport access vlan 20
interface GigabitEthernet1/0/48
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
interface Vlan20
 ip address 10.20.0.1 255.255.255.0
 no shutdown
```

## EtherChannel

```ios
show etherchannel summary
show etherchannel port-channel
show lacp neighbor

interface range GigabitEthernet1/0/47-48
 channel-group 1 mode active
interface Port-channel1
 switchport mode trunk
```

## Spanning Tree

```ios
show spanning-tree
show spanning-tree vlan 20
show spanning-tree root
show spanning-tree inconsistentports

spanning-tree vlan 20 root primary
spanning-tree vlan 20 root secondary
spanning-tree portfast
spanning-tree bpduguard enable
spanning-tree guard root
spanning-tree guard loop
```

## IPv4/IPv6 and Diagnostics

```ios
show ip route
show ip route <address>
show ipv6 route
ping <address>
traceroute <address>

interface GigabitEthernet0/0
 ip address 192.0.2.1 255.255.255.252
 ipv6 address 2001:db8:12::1/64
 no shutdown
ipv6 unicast-routing
```

## DHCP

```ios
show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict

ip dhcp excluded-address 10.20.0.1 10.20.0.20
ip dhcp pool USERS
 network 10.20.0.0 255.255.255.0
 default-router 10.20.0.1
 dns-server 10.1.0.53
interface Vlan20
 ip helper-address 10.1.0.10
```

## Static Routing

```ios
ip route 0.0.0.0 0.0.0.0 192.0.2.2
ip route 10.30.0.0 255.255.0.0 192.0.2.2
ip route 10.30.0.10 255.255.255.255 192.0.2.2
ip route 10.30.0.0 255.255.0.0 198.51.100.2 200
ipv6 route ::/0 2001:db8:12::2
```

## OSPF

```ios
show ip ospf neighbor
show ip ospf interface brief
show ip ospf database
show ip route ospf
show ipv6 ospf neighbor
show ipv6 route ospf

router ospf 10
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3 area 0
interface GigabitEthernet0/0
 ip ospf 10 area 0
 ip ospf network point-to-point
 ipv6 ospf 10 area 0
```

## FHRP

```ios
show standby brief
show standby
show vrrp brief
show vrrp
```

## NAT and ACLs

```ios
show ip nat translations
show ip nat statistics
clear ip nat translation *
show access-lists
show ip interface

ip nat inside source list 10 interface GigabitEthernet0/1 overload
ip access-list standard MGMT
 permit 10.99.0.0 0.0.0.255
ip access-list extended APP
 permit tcp 10.20.0.0 0.0.255.255 host 10.50.0.10 eq 443
 deny ip any any log
interface GigabitEthernet0/0
 ip access-group APP in
```

## Layer 2 Security

```ios
show ip dhcp snooping
show ip dhcp snooping binding
show ip arp inspection
show port-security interface GigabitEthernet1/0/10
show errdisable recovery

ip dhcp snooping
ip dhcp snooping vlan 20
ip arp inspection vlan 20
switchport port-security
switchport port-security mac-address sticky
spanning-tree bpduguard enable
```

## Operations

```ios
show logging
show clock
show ntp associations
show snmp
show aaa servers
terminal monitor
undebug all
copy running-config scp:
copy sftp: flash:
```

## Rapid Troubleshooting Order

```text
show logging
show interfaces status
show interfaces <port>
show interfaces switchport / trunk
show vlan brief
show etherchannel summary
show spanning-tree
show mac address-table
show arp / show ipv6 neighbors
show ip interface brief
show ip route / show ipv6 route
show access-lists
ping with correct source
traceroute
packet capture
```


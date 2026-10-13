# IOS/IOS XE command reference

Commands are examples. Check `?`, release and privilege level on the lab image.

| Need | Useful commands |
|---|---|
| Physical and queue | `show interfaces`, `show interfaces counters errors`, `show platform hardware` (platform dependent) |
| Layer 2 | `show interfaces trunk`, `show etherchannel summary`, `show lacp neighbor`, `show spanning-tree`, `show mac address-table` |
| RIB/FIB | `show ip route <prefix>`, `show ipv6 route`, `show ip cef <dest> detail`, `show adjacency detail` |
| VRF | `show vrf`, `show ip route vrf BLUE`, `ping vrf BLUE <addr>` |
| OSPF | `show ip ospf neighbor detail`, `show ip ospf interface`, `show ip ospf database`, `show ipv6 ospf neighbor` |
| EIGRP | `show ip eigrp neighbors`, `show ip eigrp topology all-links`, `show ip eigrp interfaces detail` |
| BGP | `show ip bgp summary`, `show ip bgp <prefix>`, `show ip bgp neighbors <peer> advertised-routes`, `show ip route bgp` |
| Route policy | `show route-map`, `show ip prefix-list`, `show ip policy`, `show track` |
| Multicast | `show ip igmp groups`, `show ip mroute`, `show ip pim neighbor`, `show ip rpf <source>` |
| VPN | `show interface Tunnel0`, `show dmvpn`, `show ip nhrp`, `show crypto ikev2 sa`, `show crypto ipsec sa` |
| QoS/CoPP | `show policy-map interface <port>`, `show policy-map control-plane` |
| FHRP/time | `show standby brief`, `show vrrp brief`, `show ntp associations`, `show clock detail` |
| Assurance | `show monitor session 1`, `show flow monitor`, `show flow exporter`, `show ip sla statistics`, `show logging` |
| Security/management | `show access-lists`, `show aaa servers`, `show ip ssh`, `show snmp user`, `show users` |

## Route fault sequence

```text
show <protocol> neighbor
show <protocol> database/table
show route-map / prefix-list
show ip route <prefix>
show ip cef <destination> detail
show adjacency detail
ping/traceroute with relevant source/VRF
```

## Before a configuration change

1. Capture running configuration for affected interfaces/protocols.
2. Record current counters, peer state, routes and a time marker.
3. State predicted change and rollback command.
4. Apply in an isolated lab or approved production window.
5. Verify the originally affected flow and unrelated critical flows.

## Useful packet-level probes

```ios
ping 198.51.100.2 source 192.0.2.1
traceroute 203.0.113.9 source 192.0.2.1
ping vrf BLUE 10.10.1.2
```

Large-size, DF-set probes can help diagnose MTU where supported. Exact extended-ping syntax differs by image; use interactive extended ping and capture the chosen parameters.

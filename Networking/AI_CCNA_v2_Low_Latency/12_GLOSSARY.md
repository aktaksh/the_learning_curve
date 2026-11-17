# CCNA v2.0 Glossary and Protocol Reference

## Key Terms

| Term | Definition |
|---|---|
| AAA | Authentication, authorization and accounting |
| ACL | Ordered traffic-matching policy with implicit deny at end |
| AD | Trust preference among route sources for the same prefix |
| ARP | IPv4 address-to-MAC resolution on a local segment |
| BSSID | MAC-like identifier for a wireless basic service set |
| BPDU | Spanning-tree control message |
| Broadcast domain | Set of interfaces receiving a Layer 2 broadcast; normally one VLAN |
| CDP | Cisco proprietary neighbor discovery |
| CIDR | Prefix-length notation and classless addressing |
| Container | Isolated process environment normally sharing host kernel |
| DAI | Dynamic ARP Inspection |
| DHCP | Dynamic address and option assignment protocol |
| DR/BDR | OSPF designated/backup designated router on multiaccess network |
| EtherChannel | Logical interface bundling compatible physical links |
| FHRP | First Hop Redundancy Protocol |
| HSRP | Cisco-origin FHRP using active/standby roles |
| Hypervisor | Platform that creates/runs virtual machines |
| IaC | Infrastructure defined and managed as versioned code |
| LLDP | Standards-based neighbor discovery |
| Longest-prefix match | Selection of the most-specific matching route |
| MAC table | VLAN-scoped mapping of MAC addresses to switchports |
| MIB/OID | SNMP object structure and object identifier |
| MTU | Maximum Layer 3 payload/frame-related transmission size for a path/interface |
| NAT/PAT | Address translation / translation using port-flow differentiation |
| ND | IPv6 Neighbor Discovery |
| OSPF | Link-state interior routing protocol |
| PortFast | Rapid STP edge-port forwarding feature |
| Prefix length | Count of network bits in an IP prefix |
| Rapid PVST+ | Cisco rapid per-VLAN spanning-tree implementation |
| RA Guard | Access-layer protection against unauthorised IPv6 RAs |
| RSSI/SNR | Received signal strength / signal-to-noise ratio |
| SFTP/SCP | Encrypted file-transfer mechanisms |
| SNMP | Network monitoring/management protocol |
| SVI | Layer 3 logical interface for a VLAN |
| Syslog | Standard event-message transport/format family |
| TACACS+/RADIUS | Central AAA protocols |
| Trunk | Link carrying multiple VLANs, normally with 802.1Q tags |
| VLAN | Logical Layer 2 broadcast domain |
| VM | Virtual machine with virtual hardware and guest OS/kernel |
| VRRP | Standards-based FHRP using master/backup roles |

## Common Ports and Protocol Numbers

| Service | Transport/port |
|---|---|
| SSH/SCP | TCP 22 |
| DNS | UDP/TCP 53 |
| DHCPv4 server/client | UDP 67/68 |
| HTTP/HTTPS | TCP 80/443 |
| NTP | UDP 123 |
| SNMP query/trap | UDP 161/162 |
| Syslog | UDP 514 commonly; secure/reliable variants vary |
| TACACS+ | TCP 49 |
| RADIUS authentication/accounting | UDP 1812/1813 |
| OSPF | IP protocol 89, not TCP/UDP |
| ICMP | IP protocol 1 for IPv4 |
| ICMPv6 | IP protocol 58 |
| ESP | IP protocol 50 |

## IPv4 Special Ranges

| Range | Purpose |
|---|---|
| `10.0.0.0/8` | Private |
| `172.16.0.0/12` | Private |
| `192.168.0.0/16` | Private |
| `127.0.0.0/8` | Loopback |
| `169.254.0.0/16` | Link-local |
| `224.0.0.0/4` | Multicast |
| `0.0.0.0/0` | Default/any IPv4 route prefix |

## IPv6 Special Prefixes

| Prefix | Purpose |
|---|---|
| `2000::/3` | Global unicast allocation space |
| `fe80::/10` | Link-local |
| `fc00::/7` | Unique local |
| `ff00::/8` | Multicast |
| `::1/128` | Loopback |
| `::/0` | Default IPv6 route prefix |

## Syslog Severities

`0 Emergency, 1 Alert, 2 Critical, 3 Error, 4 Warning, 5 Notification, 6 Informational, 7 Debugging`


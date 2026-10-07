# CCNA v2.0 Standard Q&A

These are original study questions, not live exam questions. Hide the answer while responding aloud; explain *why* before checking.

## Domain 1 — Infrastructure and Connectivity

1. **What does an increasing CRC counter indicate?** Frame corruption at or before the receiving interface; investigate cable, optic, interference and duplex—not IP routing.
2. **What is the likely meaning of `administratively down/down`?** The interface is shut in configuration.
3. **Why can ping succeed during a duplex mismatch?** Some frames still pass, while collisions/errors destroy throughput and consistency.
4. **Single-mode versus multimode fibre?** Single-mode has a smaller core and longer typical reach; multimode is common for shorter in-building/data-hall links.
5. **What must match for a fibre link?** Speed, optic/wavelength, fibre type, reach, connector/polarity and compatible interfaces.
6. **What is a Type 1 hypervisor?** A hypervisor running directly on hardware.
7. **Key container-versus-VM distinction?** Containers normally share the host kernel; VMs normally run guest kernels.
8. **Network of `192.0.2.141/27`?** `192.0.2.128/27`; broadcast `.159`; usable `.129–.158`.
9. **Usable addresses in conventional `/26`?** 62.
10. **Wildcard for `/27`?** `0.0.0.31`.
11. **Why is longest-prefix match checked before AD?** Prefix specificity determines which destination route competes; AD chooses among sources for the same prefix.
12. **Private IPv4 ranges?** `10/8`, `172.16/12`, `192.168/16`.
13. **Meaning of `169.254/16` on a client?** IPv4 link-local assignment, often indicating DHCP failure.
14. **Does IPv6 use broadcast?** No; it uses multicast and unicast mechanisms.
15. **Purpose of IPv6 link-local addresses?** Same-link communication, including neighbor discovery and many routing adjacencies.
16. **What does modified EUI-64 insert?** `FFFE` into the MAC-derived interface ID and flips the U/L bit.
17. **Why might 2.4 GHz travel farther yet perform worse?** Better propagation but fewer non-overlapping channels and more interference.
18. **RSSI versus SNR?** RSSI is signal strength; SNR measures signal relative to noise and better reflects usable quality.
19. **DHCP DORA order?** Discover, Offer, Request, Acknowledgment.
20. **Where is `ip helper-address` placed?** On the Layer 3 interface receiving the client broadcast.

## Domain 2 — Switching and Access

21. **How does a switch learn MAC addresses?** From source MAC addresses of received frames, associated with ingress port and VLAN.
22. **What happens to unknown unicast?** It is flooded within the VLAN except through the ingress port.
23. **What separates broadcast domains?** A Layer 3 boundary; each VLAN is a separate broadcast domain.
24. **Access versus trunk port?** Access normally carries one untagged data VLAN; trunk carries multiple VLANs using tags, with native-VLAN behaviour.
25. **Risk of native-VLAN mismatch?** Traffic/control frames may enter the wrong VLAN and warnings/inconsistent behaviour occur.
26. **Why can an SVI remain down?** VLAN absent/inactive or no active forwarding member port, depending on platform.
27. **What enables routing between SVIs?** `ip routing` on a capable multilayer switch.
28. **LACP active/passive result?** Forms; passive/passive does not.
29. **Can one flow use all EtherChannel member bandwidth?** Usually no; a hash normally maps one flow to one member.
30. **What must EtherChannel members match?** Layer 2/3 mode and relevant speed, VLAN/trunk and channel attributes.
31. **CDP versus LLDP?** CDP is Cisco proprietary; LLDP is standards-based.
32. **What evidence validates a cabling diagram?** Discovery neighbor, local/remote port, platform/capability and management address.
33. **Why is a Layer 2 loop severe?** Ethernet has no frame TTL, allowing storms, duplicates and MAC flapping.
34. **How is root bridge selected?** Lowest bridge ID.
35. **Root port definition?** Non-root switch port with the best path to the root.
36. **Rapid STP states?** Discarding, learning and forwarding.
37. **Does PortFast disable STP?** No; it accelerates edge-port transition.
38. **BPDU Guard action?** Protects an edge port by err-disabling/blocking it when a BPDU is received.
39. **Root Guard purpose?** Prevents a port from allowing an unexpected switch to become root.
40. **Loop Guard purpose?** Prevents a redundant non-designated port from forwarding when expected BPDUs disappear.

## Domain 3 — IP Routing

41. **What changes at every routed hop?** Layer 2 header and TTL/Hop Limit; end-to-end IPs normally remain unless translated.
42. **AD versus metric?** AD compares route sources for the same prefix; metric compares routes within a protocol.
43. **Purpose of a default route?** Match destinations lacking a more-specific route.
44. **What is a host route?** `/32` for IPv4 or `/128` for IPv6.
45. **Floating static route?** Static route with higher AD than the preferred route, used as backup.
46. **Why specify an interface with an IPv6 link-local next hop?** Link-local addresses are only unique on a link.
47. **What database does OSPF build?** A link-state database used by SPF.
48. **Best practice for router IDs?** Configure them explicitly and uniquely.
49. **Four common OSPF adjacency failures?** Area, timer, subnet/network type, router ID, MTU or passive-interface mismatch; any four.
50. **OSPFv2 versus OSPFv3 in this course?** OSPFv2 carries IPv4; OSPFv3 carries IPv6.
51. **Does point-to-point OSPF elect DR/BDR?** No.
52. **Why elect DR/BDR on broadcast networks?** Reduce adjacency/flooding complexity.
53. **Is DR election preemptive?** No; a later higher-priority router does not automatically replace the existing DR.
54. **Can DROTHER routers remain 2-Way?** Yes, with one another on broadcast segments; Full with DR/BDR.
55. **HSRP versus VRRP terms?** HSRP active/standby; VRRP master/backup.
56. **Purpose of FHRP preemption?** Allow the preferred higher-priority device to retake the forwarding role.

## Domain 4 — Services and Security

57. **AAA meanings?** Authentication, authorization and accounting.
58. **Typical TACACS+ versus RADIUS use?** TACACS+ for device administration; RADIUS commonly for network access/VPN/802.1X.
59. **Why keep local AAA fallback?** Preserve controlled access if the central AAA service is unavailable.
60. **Why prefer SCP/SFTP to TFTP?** Authentication and encrypted transfer.
61. **Inside local versus inside global?** Internal host address before translation versus its externally represented translated address.
62. **What does PAT add to NAT?** Port-based flow differentiation so many hosts share an address.
63. **DNS A versus AAAA?** A maps to IPv4; AAAA maps to IPv6.
64. **CNAME purpose?** Alias one name to a canonical name.
65. **PTR purpose?** Reverse mapping from an address to a name.
66. **Tunnel versus transport IPsec?** Tunnel protects the entire original packet within a new packet; transport protects payload while retaining original outer IP header.
67. **ACL processing rule?** Top-down, first match, then implicit deny.
68. **Standard versus extended IPv4 ACL?** Standard matches source only; extended can match protocol, source, destination and ports.
69. **Where place an extended ACL?** Generally close to source, subject to operational design.
70. **DHCP snooping output used by DAI?** The trusted binding database.
71. **What does DAI mitigate?** Invalid/forged ARP, including ARP spoofing.
72. **Storm-control risk in market-data networks?** A low multicast threshold can drop legitimate bursts.
73. **RA Guard protects against what?** Unauthorised IPv6 Router Advertisements.
74. **Port-security violation modes?** Protect, restrict and shutdown.

## Domain 5 — AI and NetOps

75. **Generative versus agentic AI?** Generative systems produce content; agentic systems can plan and use approved tools in a goal-directed loop.
76. **What makes a safe troubleshooting prompt?** Sanitised context, objective, constraints, evidence, output format and required validation.
77. **Why request read-only commands first?** Reduce blast radius while collecting evidence.
78. **SNMP manager, agent, MIB and OID?** Manager queries; agent exposes data; MIB defines structure; OID identifies an object.
79. **Trap versus inform?** Trap is unacknowledged; inform is acknowledged.
80. **Why prefer SNMPv3?** It supports authentication and privacy.
81. **Ansible idempotency?** Repeated execution converges without unnecessary change.
82. **Syslog severity 0 versus 7?** 0 is Emergency/highest severity; 7 is Debugging/lowest.
83. **Parts of `%LINK-3-UPDOWN`?** Facility LINK, severity 3, mnemonic UPDOWN.
84. **Why is time synchronisation operationally essential?** It allows events across devices to be correlated in the correct order.

## Low-Latency Review

85. **Why can average interface utilisation hide loss?** Microbursts can exhaust a queue between coarse samples.
86. **Why verify a backup path's latency?** Reachability after failover does not prove the same latency/jitter objective.
87. **Why can virtualisation add jitter?** Shared scheduling, vSwitch and resource contention add variability.
88. **Why is LACP not automatic per-packet speed multiplication?** Hashing usually pins a flow to one member.
89. **Why separate management from the hot path?** Bulk transfers, polling and failures should not contend with latency-critical traffic.
90. **Best first response to AI-generated config?** Validate assumptions and commands against observed state/platform before any controlled change.


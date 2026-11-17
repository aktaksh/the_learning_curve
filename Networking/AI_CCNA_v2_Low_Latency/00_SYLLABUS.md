# CCNA 200-301 v2.0 Syllabus — Low-Latency Track

## Contents

- [Course outcomes](#course-outcomes)
- [Official domain weighting](#official-domain-weighting)
- [Module 1 — Network Infrastructure and Connectivity](#module-1--network-infrastructure-and-connectivity-25)
- [Module 2 — Switching and Network Access](#module-2--switching-and-network-access-25)
- [Module 3 — IP Routing](#module-3--ip-routing-20)
- [Module 4 — Network Services and Security](#module-4--network-services-and-security-20)
- [Module 5 — AI, Network Operations and Management](#module-5--ai-network-operations-and-management-10)
- [Low-latency extension](#low-latency-extension)
- [Laboratory sequence](#laboratory-sequence)
- [Twelve-week plan](#twelve-week-plan)
- [Readiness standard](#readiness-standard)

## Course Outcomes

By the end of the course, you should be able to:

1. Diagnose copper, fibre, interface, speed, duplex and signal problems.
2. Calculate and troubleshoot IPv4 subnets without relying on a calculator.
3. Identify and troubleshoot IPv6 addressing, prefixing and modified EUI-64.
4. Explain wireless bands, channels, RF behaviour, security and interference.
5. Troubleshoot wired and wireless clients across Windows, macOS and Linux.
6. Configure and troubleshoot DHCP clients, servers and relays on IOS devices.
7. Configure Layer 2 and Layer 3 interfaces, VLANs, trunks, SVIs and EtherChannels.
8. Validate topology documentation with CDP and LLDP.
9. Configure and troubleshoot Rapid PVST+, including protection features.
10. Interpret routing tables and determine packet-forwarding decisions.
11. Configure and troubleshoot IPv4/IPv6 static routing and floating routes.
12. Configure single-area OSPFv2 and OSPFv3 and diagnose adjacency problems.
13. Interpret HSRP and VRRP state and gateway failover behaviour.
14. Configure secure management, NAT/PAT, ACLs and Layer 2 protections.
15. Diagnose common DNS records and describe IPsec VPN operation.
16. Use SNMP, syslog, Ansible and management architectures appropriately.
17. Evaluate AI-generated network advice safely and write useful prompts.
18. Apply the foundations to low-latency network paths without confusing specialist material with the CCNA blueprint.

## Official Domain Weighting

| Domain | Weight | Recommended course time |
|---|---:|---:|
| Network Infrastructure and Connectivity | 25% | 24 hours |
| Switching and Network Access | 25% | 28 hours |
| IP Routing | 20% | 24 hours |
| Network Services and Security | 20% | 24 hours |
| AI, Network Operations and Management | 10% | 12 hours |
| Integrated labs, review and mock exams | — | 28 hours |
| **Total** | **100%** | **140 hours** |

## Module 1 — Network Infrastructure and Connectivity (25%)

### 1.1 Physical Interfaces and Cabling

- Copper media: UTP/STP, categories, RJ-45, straight-through and crossover logic.
- Fibre media: single-mode, multimode, connectors, transceivers and distance.
- Interface states: administratively down, down/down and up/up.
- Collisions, CRC/input errors, runts, giants, drops and carrier transitions.
- Duplex and speed mismatch symptoms.
- Optical signal levels and receive/transmit power awareness.
- Pinout and wrong-cable diagnosis.
- Verification: `show interfaces`, `show interfaces status`, controller/transceiver output.
- 🟪 Low latency: FEC, optics choice, deterministic physical paths and clean error counters.

### 1.2 Hypervisors, VMs and Containers

- Type 1 and Type 2 hypervisors.
- Virtual switches, virtual NICs and port groups.
- VM isolation and shared-resource effects.
- Containers versus virtual machines.
- Overlay and underlay awareness.
- 🟪 Low latency: vNIC overhead, SR-IOV, CPU/NUMA locality and why bare metal is often preferred.

### 1.3 IPv4 Addressing and Subnetting

- Binary/decimal conversion.
- Network, broadcast and usable ranges.
- CIDR and variable-length subnet masks.
- Public, private, loopback, link-local and special-use addresses.
- Longest-prefix matching.
- Address conflicts, incorrect masks and incorrect gateways.
- Troubleshooting DHCP/static assignment.
- Design exercises from `/8` through `/30`, with `/31` awareness.

### 1.4 IPv6 Addressing and Prefixing

- Global unicast, link-local, unique local, multicast and loopback.
- Prefix length and subnet boundaries.
- Stateless address autoconfiguration concepts.
- Modified EUI-64 construction.
- Neighbor Discovery versus IPv4 ARP.
- Duplicate Address Detection.
- Troubleshooting address, gateway and prefix errors.

### 1.5 Wireless Principles

- 2.4, 5 and 6 GHz characteristics.
- Channel selection, channel width and overlap.
- RSSI, SNR, attenuation, reflection, absorption and interference.
- SSID, BSSID, AP, controller and client roles.
- WPA2/WPA3 and personal versus enterprise authentication.
- Co-channel and adjacent-channel interference.
- 🟪 Low latency: wireless is normally unsuitable for deterministic trading paths.

### 1.6 Client Connectivity Troubleshooting

- Layered workflow: physical → link → addressing → routing → DNS → application.
- Windows: `ipconfig`, `ping`, `tracert`, `arp`, `nslookup`.
- Linux: `ip`, `ping`, `tracepath`, `ip neigh`, `ss`, `dig`.
- macOS: `ifconfig`/`networksetup`, `route`, `ping`, `traceroute`, `dig`.
- Wireless association, authentication and addressing failures.

### 1.7 DHCPv4

- DORA sequence and UDP ports 67/68.
- IOS DHCP pools and excluded ranges.
- DHCP relay and `ip helper-address`.
- Lease, default gateway and DNS options.
- Troubleshooting scope exhaustion, VLAN placement and relay paths.

## Module 2 — Switching and Network Access (25%)

### 2.1 Infrastructure Connectivity

- Layer 2 access/trunk interfaces.
- Routed switch ports using `no switchport`.
- 802.1Q tagging, native VLAN and allowed VLAN lists.
- Layer 2 and Layer 3 LACP EtherChannel.
- Switch virtual interfaces and routing prerequisites.
- Interface consistency requirements.

### 2.2 Edge-Host Connectivity

- Desktop, printer and IoT access ports.
- Standalone and controller-based AP connectivity.
- Voice VLANs and IP phone access-port behaviour.
- Virtualised-host trunks and port channels.
- Network-appliance connectivity.
- PoE concepts, negotiation and power budget.

### 2.3 CDP and LLDP

- Cisco-proprietary CDP versus standards-based LLDP.
- Neighbor identity, local/remote port, capability and management address.
- Comparing live neighbours with diagrams and interface descriptions.
- Security consideration: discovery protocols reveal topology.

### 2.4 Operational Troubleshooting

- `show` commands and log interpretation.
- `ping`, extended ping and traceroute.
- Packet-capture fundamentals.
- MAC-address-table and ARP/neighbor-table diagnosis.
- Structured fault isolation.

### 2.5 Rapid PVST+

- Root bridge selection and bridge IDs.
- Root, designated, alternate and backup ports.
- Discarding, learning and forwarding states.
- Path cost and tie-breakers.
- Root primary/secondary configuration.
- PortFast, root guard, loop guard and BPDU guard.
- 🟪 Low latency: avoid unnecessary Layer 2 diameter; understand reconvergence impact.

## Module 3 — IP Routing (20%)

### 3.1 Routing-Table Interpretation

- Connected, local, static and dynamic routes.
- Prefix/mask, next hop and outgoing interface.
- Administrative distance versus metric.
- Recursive lookup and gateway of last resort.
- Longest-prefix match before administrative distance.

### 3.2 Static Routing

- IPv4 and IPv6 default routes.
- Network and host routes.
- Next-hop, exit-interface and fully specified routes.
- Floating static routes.
- Troubleshooting recursive resolution and wrong next hops.

### 3.3 OSPFv2 and OSPFv3

- Link-state principles and shortest-path calculation.
- Single-area OSPF configuration.
- Router ID selection and manual assignment.
- Neighbor state and adjacency requirements.
- Point-to-point and broadcast network types.
- DR/BDR election on broadcast segments.
- Passive interfaces.
- OSPFv2 for IPv4 and OSPFv3 for IPv6.
- 🟪 Low latency: convergence, ECMP awareness and deterministic-path trade-offs.

### 3.4 First-Hop Redundancy

- HSRP active/standby and virtual IP/MAC concepts.
- VRRP master/backup terminology.
- Priority and preemption.
- Interpreting operational status.
- Failure detection and client default-gateway continuity.

## Module 4 — Network Services and Security (20%)

### 4.1 Secure Device Management and AAA

- Local usernames, privilege and password protection.
- SSH management and VTY restrictions.
- AAA concepts: authentication, authorization and accounting.
- TACACS+ versus RADIUS.
- Configuring an IOS device as an AAA client.

### 4.2 Secure File Operations

- SCP and SFTP roles.
- Configuration and software image transfer.
- Integrity, backups and change control.

### 4.3 NAT and PAT

- Inside local/global and outside local/global terminology.
- Static NAT, dynamic concepts and PAT overload.
- IOS XE configuration and verification.
- NAT order-of-operation awareness.
- Troubleshooting ACL, direction and translation failures.

### 4.4 DNS Diagnosis

- A, AAAA, CNAME, MX, NS and PTR records.
- Recursive resolution and caching.
- Forward and reverse lookup.
- Diagnosing wrong records, missing records and stale caches.

### 4.5 IPsec VPNs

- Remote-access versus site-to-site VPNs.
- Authentication, confidentiality and integrity.
- IKE concepts and IPsec security associations.
- Tunnel versus transport mode.

### 4.6 IPv4 ACLs

- Standard and extended ACLs.
- Numbered and named forms.
- Wildcard-mask calculation.
- Top-down processing, first match and implicit deny.
- Interface direction and placement.
- Verification, counters and safe change practices.

### 4.7 Layer 2 Security

- DHCP snooping trust boundaries and binding database.
- Dynamic ARP Inspection validation.
- Storm control.
- IPv6 RA Guard.
- Port-security modes, limits, sticky learning and violations.
- Interaction and dependency between DHCP snooping and DAI.

## Module 5 — AI, Network Operations and Management (10%)

### 5.1 Agentic AI in Network Operations

- Generative versus agentic systems.
- Observation, planning, tool use and feedback loops.
- Human approval and blast-radius control.
- Hallucination, stale data and unsafe recommendations.

### 5.2 Prompt Selection

- Persona, objective, context, constraints and output format.
- Data classification and secret removal.
- Providing command output without leaking credentials.
- Asking for hypotheses and verification commands rather than blind changes.

### 5.3 Network-Management Approaches

- Device-based management.
- Cloud-based management.
- Controller-based management.
- Automation-based management.
- Infrastructure as code.
- Trade-offs in scale, consistency, auditability and dependence.

### 5.4 SNMP

- Manager, agent, MIB and OID.
- Polling, traps and informs.
- SNMPv2c versus SNMPv3 security.
- Counters, capacity and fault monitoring.

### 5.5 Ansible

- Control node, inventory, modules, tasks and playbooks.
- Idempotency.
- Gathering facts and executing show commands.
- Check mode and controlled rollout.

### 5.6 Syslog

- Message structure, timestamp, facility, severity and mnemonic.
- Severity 0 through 7.
- Local buffering and remote collectors.
- Correlation with interface and routing events.

## Low-Latency Extension

These topics are career-focused supplements, not substitutes for blueprint study:

1. Market-data multicast and order-entry TCP.
2. IGMP snooping and multicast queriers.
3. PTP, hardware timestamping and clock hierarchy.
4. NIC RX/TX rings, RSS and queue placement.
5. Interrupts, NAPI, softirq and CPU affinity.
6. NUMA and PCIe locality.
7. Microbursts, buffering and packet drops.
8. Cut-through switching and deterministic topology.
9. A/B paths and failure-domain isolation.
10. Packet capture, sequence gaps and latency measurement.
11. QoS classification awareness without treating QoS as a cure for congestion.
12. Safe operational change, MOPs and rollback.

## Laboratory Sequence

1. IOS CLI access, baseline configuration and secure SSH.
2. Copper/fibre/interface fault interpretation.
3. IPv4 subnetting and dual-router addressing.
4. IPv6 addressing and modified EUI-64.
5. DHCP server and relay.
6. VLANs, trunks and inter-VLAN routing.
7. L2 and L3 EtherChannel.
8. CDP/LLDP documentation validation.
9. Rapid PVST+ root placement and protection.
10. Static and floating static routes.
11. OSPFv2 and OSPFv3.
12. HSRP/VRRP interpretation.
13. NAT/PAT and ACLs.
14. DHCP snooping, DAI and port security.
15. Syslog, SNMP and Ansible operational workflow.
16. Integrated enterprise troubleshooting.
17. Low-latency design and fault-analysis capstone.

## Twelve-Week Plan

| Week | Focus | Deliverable |
|---:|---|---|
| 1 | Physical networking, OSI/TCP-IP and IOS basics | Baseline lab and interface diagnosis |
| 2 | IPv4 addressing and subnetting | 100 timed subnet calculations |
| 3 | IPv6, clients and DHCP | Dual-stack DHCP lab |
| 4 | VLANs, trunks, SVIs and edge ports | Inter-VLAN topology |
| 5 | EtherChannel, CDP/LLDP and troubleshooting | Redundant switching lab |
| 6 | Rapid PVST+ and protection | Root-placement and loop-prevention lab |
| 7 | Routing tables and static routes | IPv4/IPv6 routing lab |
| 8 | OSPFv2/v3 and FHRP | Resilient routed topology |
| 9 | AAA, secure files, NAT and DNS | Secure branch-services lab |
| 10 | ACLs, VPN concepts and L2 security | Segmentation/security lab |
| 11 | AI, management models, SNMP, Ansible and syslog | Operational automation exercise |
| 12 | Integrated troubleshooting and mock exams | Two timed exams plus weak-area remediation |

## Readiness Standard

You are ready when you can:

- Score at least **85%** on both original practice exams.
- Complete core configurations without copying commands.
- Explain why every command is used.
- Troubleshoot from observed evidence rather than randomly changing configuration.
- Calculate IPv4 ranges and wildcard masks reliably under time pressure.
- Interpret routing, spanning-tree, EtherChannel, OSPF, NAT, ACL and security output.
- Reject unsafe or unsupported AI recommendations and propose verification steps.
- Complete the integrated lab from a blank topology, then repair injected faults.


# CCNA v2.0 Laboratory Workbook

Use Packet Tracer for most labs. Use CML/EVE-NG or real IOS/IOS XE where Packet Tracer lacks a command. Save a clean baseline before injecting faults.

## Standard Lab Method

For every lab submit:

1. Topology and addressing table.
2. Intended forwarding behaviour.
3. Configuration.
4. Verification output.
5. One injected fault, observed symptom and root cause.
6. Rollback or repair.
7. Low-latency implication where applicable.

## Lab 1 — Baseline and Secure Access

**Topology:** one router, one switch, one management PC.

**Tasks:**

- Set hostname, domain, local admin, enable secret and banners.
- Generate RSA keys and allow SSH only.
- Configure management SVI/default gateway.
- Save configuration and transfer a backup with SCP if supported.
- Verify remote access and reject Telnet.

**Faults:** wrong default gateway; VTY permits Telnet but not SSH; missing RSA key.

## Lab 2 — Interface and Cable Diagnosis

**Topology:** two switches with two end hosts.

**Tasks:**

- Record interface state, speed, duplex and counters.
- Cause an administrative-down failure.
- Where supported, cause speed/duplex mismatch.
- Compare counter snapshots under traffic.
- Build a symptom-to-cause table.

**Success:** identify the layer and evidence before fixing it.

## Lab 3 — IPv4 Subnet Design

Given `10.44.0.0/16`, allocate subnets for 500, 200, 60, 30 and two point-to-point links using VLSM.

**Tasks:** assign largest first; document network, prefix, first/last host and broadcast; configure three routed segments; prove route and gateway correctness.

**Faults:** overlapping subnet, wrong host mask and off-subnet gateway.

## Lab 4 — IPv6 Dual Stack

**Tasks:**

- Assign `/64` global prefixes and manual link-local addresses.
- Enable IPv6 routing.
- Inspect EUI-64-derived interface IDs.
- Verify neighbor discovery and routing.
- Compare ARP with `show ipv6 neighbors`.

**Faults:** `/48` host prefix, duplicate address and missing `ipv6 unicast-routing`.

## Lab 5 — DHCP Server and Relay

**Topology:** clients in VLANs 10 and 20; DHCP server/router in VLAN 50.

**Tasks:** create pools, exclusions, gateway/DNS options and relay; inspect bindings; renew clients.

**Faults:** wrong pool mask, exhausted scope, helper on wrong interface, ACL blocking UDP 67/68.

## Lab 6 — VLANs, Trunks and Inter-VLAN Routing

**Topology:** two switches, one multilayer switch/router and clients in VLANs 10/20/30.

**Tasks:** create VLANs; configure access ports and pruned trunks; set native VLAN 999; configure SVIs or router-on-a-stick; verify same- and inter-VLAN paths.

**Faults:** VLAN omitted from allowed list, native mismatch, access VLAN wrong, SVI down, missing `ip routing`.

## Lab 7 — L2 and L3 LACP EtherChannel

Build one Layer 2 port channel and one Layer 3 port channel.

**Tasks:** use active/passive modes; verify bundle members; shut one member and observe continuity; inspect load-sharing method if available.

**Faults:** passive/passive, trunk mismatch, one member left as routed port.

## Lab 8 — CDP/LLDP Documentation Audit

Create a topology diagram containing three deliberate errors. Use CDP, LLDP and interface descriptions to identify them. Produce a corrected link inventory containing local device/port, remote device/port and link purpose.

## Lab 9 — Rapid PVST+

**Topology:** triangle of three switches, VLANs 10 and 20.

**Tasks:** make SW1 root for VLAN 10 and SW2 root for VLAN 20; identify roles/states; enable edge protections; test Root Guard and BPDU Guard safely.

**Faults:** unexpected root, PortFast on inter-switch link, missing guard, blocked link misunderstood as failure.

## Lab 10 — Static Routing

**Topology:** three routers with dual paths.

**Tasks:** configure IPv4/IPv6 network, host and default routes; add a floating backup; fail the primary and observe route installation.

**Faults:** wrong mask, unreachable next hop, backup AD too low, missing return route.

## Lab 11 — OSPFv2 and OSPFv3

**Tasks:** configure area 0, explicit router IDs, point-to-point links, broadcast segment and passive LANs; inspect neighbors and learned routes; control DR election in the initial build.

**Faults:** area mismatch, duplicate router ID, timer mismatch, passive transit link and MTU mismatch where supported.

## Lab 12 — FHRP Interpretation

Where supported, configure HSRP or VRRP for a client VLAN. Record active/master and standby/backup state, priority, virtual IP/MAC and failover behaviour. If unsupported, analyse supplied `show standby` and `show vrrp` samples.

## Lab 13 — NAT/PAT and DNS

**Tasks:** configure PAT for clients and one static translation for a server; validate translations/counters; create or simulate A, AAAA, CNAME and PTR queries.

**Faults:** inside/outside reversed, ACL does not match, missing default route, stale/wrong DNS record.

## Lab 14 — IPv4 ACLs

Implement this policy:

- Users may query the approved DNS server using UDP/TCP 53.
- Users may reach the application server on TCP 443.
- Administrators may SSH to network devices.
- Other user-to-server traffic is denied and counted.

Test permitted and denied paths. Move an ACL to the wrong interface/direction, observe failure, then repair it.

## Lab 15 — Layer 2 Security

Configure DHCP snooping, DAI, BPDU Guard, RA Guard, storm control and port security on a small access topology.

**Validation:** legitimate DHCP/ARP works; rogue DHCP is blocked; static endpoint handling is documented; a simulated BPDU or port-security violation produces the expected state.

## Lab 16 — Syslog, SNMP and Ansible

**Tasks:** synchronise time; send syslog to a collector; identify facility/severity/mnemonic; configure or analyse SNMPv3; run an Ansible read-only playbook to collect interface, STP and routing output.

**Safety:** no plaintext secrets in inventory; begin read-only; preserve output with timestamps.

## Lab 17 — Integrated Troubleshooting

Build two access switches, two distribution/L3 devices and three VLANs with LACP, Rapid PVST+, OSPF, DHCP relay, NAT and ACLs.

Inject eight faults:

1. Wrong access VLAN.
2. VLAN missing from trunk.
3. LACP mismatch.
4. Unexpected STP root.
5. OSPF area mismatch.
6. Wrong static default route.
7. ACL applied in wrong direction.
8. DHCP helper missing.

For each fault record symptom, first failing layer, evidence, root cause, minimal fix and post-check.

## Lab 18 — Low-Latency Capstone

Design—not necessarily configure—a small trading-colocation network:

- Two independent A/B market-data paths.
- Separate order-entry and management paths.
- Redundant switches without a hidden shared failure domain.
- Multicast distribution and IGMP-snooping considerations.
- PTP grandmaster/time path.
- Server dual NICs and documented NUMA/PCIe locality.
- Observability from interface counters, packet capture and precise timestamps.

Answer:

1. Which components are on the latency-critical path?
2. Where can buffering or microbursts occur?
3. What happens after each single failure?
4. Does the backup path meet the same latency objective?
5. How are changes rolled back?
6. Which CCNA features support the design, and which specialist topics go beyond CCNA?

## Lab Completion Scorecard

| Skill | Pass condition |
|---|---|
| Configuration | Built from objectives without copying final config |
| Verification | At least three relevant proof commands per feature |
| Troubleshooting | Root cause derived from evidence |
| Recovery | Minimal fix plus rollback identified |
| Explanation | Packet path explained hop by hop |
| Low latency | Jitter/loss/failure implication stated accurately |


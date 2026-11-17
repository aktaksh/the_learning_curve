# CCNA v2.0 Final Revision Guide

## Seven-Day Plan

| Day | Focus |
|---:|---|
| 7 | Interface/cabling, IPv4 subnetting, IPv6 and DHCP |
| 6 | VLANs, trunks, SVIs, LACP and edge connectivity |
| 5 | Rapid PVST+, discovery and Layer 2 troubleshooting |
| 4 | Routing tables, static routes, OSPFv2/v3 and FHRP |
| 3 | AAA, NAT, DNS, VPN concepts, ACLs and L2 security |
| 2 | AI, management models, SNMP, Ansible, syslog and integrated lab |
| 1 | Light command review, subnet drills, sleep and exam logistics |

## Must-Know Rules

1. Troubleshoot physical/link state before upper layers.
2. Increasing counters matter more than old static totals.
3. Longest prefix wins before AD and metric.
4. `/27` has blocks of 32 and 30 conventional usable addresses.
5. IPv6 uses multicast, not broadcast.
6. DHCP relay belongs on the client-facing Layer 3 interface.
7. VLAN existence does not prove trunk forwarding.
8. LACP needs at least one active side.
9. One EtherChannel flow normally uses one member.
10. STP root is lowest bridge ID.
11. PortFast does not disable STP.
12. BPDU Guard protects edge ports; Root Guard protects root placement; Loop Guard protects redundant STP paths from missing BPDUs.
13. OSPF point-to-point has no DR/BDR.
14. OSPF broadcast DR election is non-preemptive.
15. DROTHER-to-DROTHER 2-Way may be normal.
16. Floating static AD must be worse than the preferred route.
17. HSRP uses active/standby; VRRP uses master/backup.
18. ACL first match wins; implicit deny ends the list.
19. Standard ACL matches source; extended ACL can match protocol, source, destination and ports.
20. DHCP snooping builds bindings; DAI can validate ARP against them.
21. RA Guard blocks unauthorised IPv6 RAs.
22. Syslog lower number means higher severity.
23. SNMP informs are acknowledged; traps are not.
24. Idempotent automation avoids needless repeat changes.
25. AI recommendations require evidence, validation and controlled authority.

## Subnet Speed Table

| Prefix | Block | Usable |
|---:|---:|---:|
| /24 | 256 | 254 |
| /25 | 128 | 126 |
| /26 | 64 | 62 |
| /27 | 32 | 30 |
| /28 | 16 | 14 |
| /29 | 8 | 6 |
| /30 | 4 | 2 |

## Troubleshooting Evidence Map

| Question | Evidence |
|---|---|
| Is the link healthy? | interface state, speed/duplex, error deltas, optics |
| Is Layer 2 correct? | VLAN/trunk, STP, EtherChannel, MAC table |
| Is local Layer 3 correct? | address/prefix, ARP/ND, SVI, gateway |
| Is forwarding correct? | route lookup, next hop, source-aware ping/traceroute |
| Is policy blocking? | ACL/NAT/security counters and logs |
| Is a service failing? | DHCP bindings, DNS queries, AAA/SNMP/syslog state |
| Is recovery complete? | application test, counters, path and recurrence window |

## Exam Technique

- Read the verb: **describe**, **interpret**, **configure**, **troubleshoot**.
- Identify exactly what the question supplies and asks.
- Remove answers that operate at the wrong layer.
- For route questions, write the matching prefixes before considering AD.
- For ACL questions, mark source, destination, protocol, port and direction.
- For STP, identify root first, then path cost and roles.
- For troubleshooting, prefer the safest command that separates hypotheses.
- Do not invent missing facts.
- Flag long questions and return after securing easier marks.

## Low-Latency Sanity Checks

- Average utilisation does not disprove microbursts.
- Redundancy does not guarantee equal failure-path latency.
- Packet loss can matter more than average delay.
- Every path must have accurate time and measurable counters.
- Do not remove security controls without measured evidence and approved design.
- A simple topology with known failure behaviour is often more deterministic.

## Final Readiness

- [ ] 85% or more on both practice exams.
- [ ] 80% or more on scenario rubric.
- [ ] Complete integrated lab without answer configs.
- [ ] Explain every missed question and retest after 48 hours.
- [ ] Subnet `/24`–`/30` quickly and accurately.
- [ ] Interpret all major show outputs.
- [ ] Configure core features from memory.
- [ ] Distinguish CCNA requirements from low-latency extensions.


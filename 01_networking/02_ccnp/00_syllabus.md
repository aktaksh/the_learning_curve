# Syllabus and study plan

## Contents

- [Certification path](#certification-path)
- [ENCOR domain map](#encor-domain-map)
- [ENARSI domain map](#enarsi-domain-map)
- [Learning sequence](#learning-sequence)
- [Readiness criteria](#readiness-criteria)

## Certification path

CCNP Enterprise requires **ENCOR plus one concentration**. This course chooses **ENARSI** because its routing, VPN, troubleshooting, IP SLA, multicast-adjacent and observability skills fit a low latency infrastructure role. ENCOR is 120 minutes; ENARSI is 90 minutes according to Cisco's current exam pages. The sequence below prepares for ENCOR first, then ENARSI.

## ENCOR domain map

| Domain | Weight | What you must do | Course |
|---|---:|---|---|
| Architecture | 15% | Explain campus/fabric/cloud, resilience, SD-WAN, SD-Access, QoS, CEF/FIB/TCAM | 01 |
| Virtualization | 10% | Describe VM/vSwitch, configure VRF and GRE/IPsec, explain LISP/VXLAN | 01 |
| Infrastructure | 30% | Troubleshoot trunks/channels, configure STP, OSPFv2/v3, eBGP, services; wireless analysis | 02 |
| Network assurance | 10% | Use ping/traceroute/debug/SNMP/syslog; configure NetFlow, SPAN, IP SLA, NETCONF/RESTCONF | 03 |
| Security | 20% | Configure AAA, ACL, CoPP; interpret wireless/NAC and security architecture | 03 |
| Automation | 15% | Read Python, construct JSON, explain YANG/APIs, use EEM, compare orchestration | 03 |

## ENARSI domain map

| Domain | Weight | What you must do | Course |
|---|---:|---|---|
| Layer 3 technologies | 35% | Diagnose AD, policy, summarization, redistribution, EIGRP, OSPF, BGP; configure PBR/VRF-Lite | 04 |
| VPN technologies | 20% | Explain MPLS/L3VPN; configure and verify single-hub DMVPN | 05 |
| Infrastructure security | 20% | Troubleshoot AAA, ACL/uRPF/CoPP; explain IPv6 first-hop security | 06 |
| Infrastructure services | 25% | Troubleshoot management, SNMP, logging, DHCP, IP SLA, NetFlow, assurance | 06 |

## Learning sequence

| Weeks | Study | Deliverable |
|---:|---|---|
| 1–2 | Architecture, CEF, QoS, VRF, overlays | Draw control/data plane for three topologies |
| 3–4 | Campus Layer 2, wireless, OSPF, BGP | Labs 1–5 and 23 (if controller available), fault diary |
| 5–6 | Multicast/PTP/NAT/FHRP, assurance | Labs 6–8, counters and timing report |
| 7–8 | Security, APIs, automation | Labs 9–11, ENCOR timed assessment |
| 9–10 | EIGRP, OSPF area types, BGP policy | Labs 12–14, route selection drills |
| 11–12 | Redistribution, PBR, VRF, BFD | Labs 15–17, loop-prevention exercise |
| 13–14 | MPLS concepts, DMVPN, security | Labs 18–20, tunnel fault diary |
| 15–16 | DHCP, IP SLA, NetFlow, troubleshooting | Labs 21–22, ENARSI timed assessment |

For a shorter schedule, keep the order and increase hours rather than dropping domains. Give each topic four passes: concept, configuration/outputs, fault diagnosis, timed recall.

### Learning outcomes

You should be able to explain where forwarding happens (hardware or software), what route enters the RIB, what enters the FIB, and how the packet reaches the next hop; identify failed adjacencies; prove policy impact; and trace both the preferred and failure paths. For wireless, explain and diagnose the blueprint material even if your main role is wired colo networking.

## Readiness criteria

- Explain each blueprint item in your own words, including topics with only “describe” depth.
- Complete every core lab from an objective sheet, then diagnose its injected fault without looking at the answer.
- Reach **85%** on each original practice assessment; use misses to drive focused labs. This is a study target, not a Cisco passing-score claim.
- For every topology, record normal path, failure path, convergence trigger, packet loss and expected latency effect.
- Verify current Cisco blueprint versions again before scheduling.

# Blueprint coverage checklist

Mark a topic complete only after you can explain it, read the relevant output, and complete the associated lab. The numeric IDs follow Cisco's current ENCOR v1.1 and ENARSI v1.1 published topic guides; this checklist paraphrases them.

## ENCOR 350-401

### 1. Architecture — 15%

- [ ] 1.1 Campus two/three-tier, fabric/cloud and availability (FHRP/SSO): [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md)
- [ ] 1.2 WLAN deployment, location and client density: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md), [02](02_ENCOR_INFRASTRUCTURE.md)
- [ ] 1.3 SD-WAN planes, value and limitations: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md)
- [ ] 1.4 SD-Access planes and traditional interoperation: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md)
- [ ] 1.5 Wired/wireless QoS components and policy: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md), [13](13_WORKED_EXAMPLES.md)
- [ ] 1.6 CEF, CAM, TCAM, FIB, RIB, adjacency: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md), [07](07_PACKET_FLOWS_AND_WORKFLOWS.md)

### 2. Virtualization — 10%

- [ ] 2.1 Hypervisors, VMs and vSwitches: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md)
- [ ] 2.2 VRF and GRE/IPsec tunnel configuration/verification: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md), [05](05_ENARSI_VPN.md), labs 2–3 and 19
- [ ] 2.3 LISP and VXLAN concepts: [01](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md)

### 3. Infrastructure — 30%

- [ ] 3.1 Trunks, EtherChannel, RSTP/MST and guards: [02](02_ENCOR_INFRASTRUCTURE.md), labs 4–5
- [ ] 3.2 EIGRP versus OSPF; multi-area OSPFv2/v3, eBGP, PBR: [02](02_ENCOR_INFRASTRUCTURE.md), [04](04_ENARSI_ADVANCED_ROUTING.md), labs 6–7 and 13–18
- [ ] 3.3 RF, AP modes/antennae, discovery/join, roaming, GUI faults, WLAN segments: [02](02_ENCOR_INFRASTRUCTURE.md), lab 23 where available
- [ ] 3.4 NTP/PTP, NAT/PAT, HSRP/VRRP, IGMP/PIM/RPF: [02](02_ENCOR_INFRASTRUCTURE.md), labs 8–9

### 4. Assurance — 10%

- [ ] 4.1 Ping/traceroute, debug, SNMP and syslog diagnosis: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 4.2 Flexible NetFlow: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 10
- [ ] 4.3 SPAN/RSPAN/ERSPAN: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 10
- [ ] 4.4 IP SLA: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 10
- [ ] 4.5 Cisco controller assurance workflows: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 4.6 NETCONF/RESTCONF: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 12

### 5. Security — 20%

- [ ] 5.1 Line/local/AAA authentication and authorization: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 11
- [ ] 5.2 ACL and CoPP: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 11
- [ ] 5.3 REST API security: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 5.4 802.1X, WebAuth, PSK and EAPOL: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 23 where available
- [ ] 5.5 Threat/endpoint/NGFW, TrustSec/MACsec, NAC/MAB: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)

### 6. Automation — 15%

- [ ] 6.1 Read basic Python: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md), lab 12
- [ ] 6.2 Construct JSON: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 6.3 YANG concepts: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 6.4 Controller APIs: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 6.5 REST status/payloads: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 6.6 EEM applet: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)
- [ ] 6.7 Agent/agentless orchestration: [03](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md)

## ENARSI 300-410

- [ ] 1.1–1.8 AD, route maps, loop prevention, redistribution, summarization, PBR, VRF-Lite, BFD: [04](04_ENARSI_ADVANCED_ROUTING.md), [13](13_WORKED_EXAMPLES.md), labs 17–18
- [ ] 1.9 EIGRP classic/named, IPv4/v6, neighbours/auth, RD/FD/FC, stubs, unequal cost, metrics: [04](04_ENARSI_ADVANCED_ROUTING.md), lab 13
- [ ] 1.10 OSPFv2/v3 neighbours/auth, network/area/router types, virtual links and preference: [04](04_ENARSI_ADVANCED_ROUTING.md), lab 14
- [ ] 1.11 BGP IPv4/v6, peering/auth, attributes, reflection and policy: [04](04_ENARSI_ADVANCED_ROUTING.md), labs 15–16
- [ ] 2.1–2.2 MPLS and L3VPN forwarding: [05](05_ENARSI_VPN.md)
- [ ] 2.3 Single-hub DMVPN, GRE/mGRE, NHRP, IPsec, dynamic peers, spoke paths: [05](05_ENARSI_VPN.md), lab 19
- [ ] 3.1–3.4 AAA, IPv4/v6 filters, uRPF, CoPP and IPv6 first hop: [06](06_ENARSI_SECURITY_SERVICES.md), lab 20
- [ ] 4.1–4.7 Management, SNMP, logging/telemetry, DHCPv4/v6, IP SLA, NetFlow/IPFIX and controller assurance: [06](06_ENARSI_SECURITY_SERVICES.md), labs 21–22

**Official sources:** [ENCOR exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/encor.html) and [ENARSI exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/enarsi.html). Check those pages for later revisions.

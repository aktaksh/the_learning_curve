# CCNP Enterprise — ENCOR + ENARSI, with low latency applications

**Track:** 350-401 ENCOR v1.1 (core) + 300-410 ENARSI v1.1 (concentration). Passing both earns CCNP Enterprise. Cisco lists no formal prerequisite for either exam; the CCNA knowledge in your existing course is the assumed starting point.

## Course index

| Order | Document | Outcome |
|---:|---|---|
| 0 | [Syllabus and schedule](00_SYLLABUS.md) | Scope, blueprint map, milestones |
| 1 | [Architecture and virtualization](01_ENCOR_ARCHITECTURE_VIRTUALIZATION.md) | Enterprise design, QoS, SD-WAN/Access, VRF, overlays |
| 2 | [Infrastructure](02_ENCOR_INFRASTRUCTURE.md) | Campus switching, OSPF, eBGP, wireless, services |
| 3 | [Assurance, security and automation](03_ENCOR_ASSURANCE_SECURITY_AUTOMATION.md) | Telemetry, capture, APIs, AAA, CoPP, Python/JSON |
| 4 | [Advanced routing](04_ENARSI_ADVANCED_ROUTING.md) | EIGRP, OSPF, BGP, redistribution, policy |
| 5 | [VPN technologies](05_ENARSI_VPN.md) | MPLS L3VPN, DMVPN, VRF-Lite |
| 6 | [Security and services](06_ENARSI_SECURITY_SERVICES.md) | uRPF, IPv6 first hop, management, DHCP, IP SLA, NetFlow |
| 7 | [Workflows and diagrams](07_PACKET_FLOWS_AND_WORKFLOWS.md) | Packet paths and fault isolation in plain text/Mermaid |
| 8 | [Hands-on labs](08_LABS.md) | Build, break, diagnose, restore |
| 9 | [Commands](09_COMMAND_REFERENCE.md) | IOS/IOS XE checks and safe examples |
| 10 | [Knowledge Q&A](10_QA.md) | Retrieval practice with reasoned answers |
| 11 | [Scenario Q&A](11_SCENARIO_QA.md) | Multi-symptom cases and root cause |
| 12 | [Practice assessments](12_PRACTICE_ASSESSMENTS.md) | Original ENCOR/ENARSI questions and rubric |
| 13 | [Worked examples](13_WORKED_EXAMPLES.md) | Route calculations, policy decisions and packet diagnosis |
| 14 | [Blueprint checklist](14_BLUEPRINT_CHECKLIST.md) | Track each published topic to its lesson and lab |

```mermaid
flowchart LR
  C[CCNA foundations] --> E[ENCOR: broad enterprise core]
  E --> A[ENARSI: advanced routing and services]
  A --> L[Failure labs and path analysis]
  L --> X[Two exams]
  classDef blue fill:#174ea6,color:#fff;
  classDef green fill:#137333,color:#fff;
  classDef purple fill:#6f42a1,color:#fff;
  classDef orange fill:#b06000,color:#fff;
  class C,E blue; class A purple; class L green; class X orange;
```

**Tutor method:** For each topic, explain the packet path, configure a small topology, prove the resulting state, inject one fault, and explain the repair from evidence. Purple **ULL notes** connect a topic to trading networks. They add job depth and should not displace exam coverage.

**Lab notation:** Command examples are illustrative IOS/IOS XE syntax. Features differ by image and release; confirm with `?` and Cisco platform documentation. CML, EVE-NG, or suitable virtual IOS images cover more of this track than Packet Tracer. Lab examples use documentation prefixes (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, `2001:db8::/32`).

**Blueprint sources:** [Cisco CCNP Enterprise certification](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccnp-enterprise/index.html), [ENCOR exam](https://www.cisco.com/site/us/en/learn/training-certifications/exams/encor.html), [ENARSI exam](https://www.cisco.com/site/us/en/learn/training-certifications/exams/enarsi.html). Confirm exam topics before booking; Cisco may revise them.

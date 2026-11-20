# Hands-on labs — build, break, diagnose, restore

## Lab method

Use CML, EVE-NG or supported hardware/images. Save a baseline and use a dedicated lab. Submit for each lab: topology, addressing, initial configuration, three proof commands, injected fault, observed symptom, cause, minimal repair, and after-state. Config snippets in the lessons are starting points; use your image's syntax and document any variation.

| # | Lab | Required proof | Injected fault |
|---:|---|---|---|
| 1 | RIB/FIB/CEF on three routers | Route, CEF entry, resolved adjacency, ping source | Remove ARP/ND resolution or next-hop route |
| 2 | VRF-Lite BLUE/RED with overlapping subnet | Per-VRF route and VRF ping | Put interface in wrong VRF |
| 3 | GRE tunnel over routed underlay | Tunnel state, overlay ping, PMTU test | Wrong destination or blocked large packet |
| 4 | Two-switch trunk + LACP | Trunk VLANs, LACP member status | Passive/passive or VLAN mismatch |
| 5 | MST/RSTP with explicit root | Root/role/state for each VLAN/instance | Region mismatch or superior rogue BPDU |
| 6 | OSPFv2/v3 with areas 0 and 10 | Neighbours, LSDB, interarea routes | Area/timer/MTU mismatch |
| 7 | Direct eBGP plus route policy | Established peer, advertised/received/best/RIB | Missing network route or prefix-list deny |
| 8 | Multicast receiver path | IGMP, mroute, PIM neighbour, RPF | Wrong route toward source |
| 9 | NTP/PTP interpretation and FHRP | Time source/offset, active gateway | Wrong peer priority or tracking |
| 10 | SPAN + Flexible NetFlow + IP SLA | Mirror/capture, flow cache, probe stats | Wrong direction/exporter/track |
| 11 | AAA/CoPP/ACL | Second-session login, class counters, allowed route control | Block OSPF or management source |
| 12 | RESTCONF/NETCONF and JSON | Authenticated GET, parsed field, safe change plan | Bad token or wrong model path |
| 13 | EIGRP successor/feasible successor | Topology all-links, RD/FD, failover | Break successor and inspect active query |
| 14 | OSPF area types and external routes | Stub/NSSA LSAs, E1/E2 routes | Mismatched stub flag or filter |
| 15 | BGP iBGP and route reflector | Reflected prefix and next-hop resolution | Remove next-hop route |
| 16 | BGP attributes and filtering | Weight/local-pref/AS-path decision | Inbound policy sends wrong preferred path |
| 17 | Two-way redistribution | Tagged source routes, no feedback | Remove tag deny and observe loop risk |
| 18 | PBR + VRF + IP SLA tracking | Route-map hits, policy path, fallback | Wrong ingress interface or dead next hop |
| 19 | Single-hub DMVPN | NHRP registration, overlay route, IPsec SA | Wrong NHS or crypto mismatch |
| 20 | uRPF, IPv6 RA Guard and AAA | Allowed traffic, drop counters | Strict uRPF on asymmetric return path |
| 21 | DHCPv4/v6 + management | Lease/options, relay, route, AAA/SSH | Wrong relay or blocked ND |
| 22 | Integrated ULL fault drill | A/B packet path and latency evidence | Queue burst plus route change and clock offset |
| 23 | WLAN controller access and security (where available) | AP join, SSID/profile/tag, 802.1X or PSK client state | Wrong VLAN/security profile or failed RADIUS |

### Example lab 7: eBGP fault worksheet

**Topology:** R1 AS 65001 `192.0.2.1/30` ↔ R2 AS 65002 `192.0.2.2/30`; R1 advertises `203.0.113.0/24`, R2 advertises `198.51.100.0/24`.

1. Configure both peers and add the exact advertised prefixes to each RIB (a loopback or static Null0 lab route is acceptable).
2. Show peer state, BGP table, RIB and forwarding entry.
3. Remove R1's `203.0.113.0/24` origin route. Predict and observe the advertisement change.
4. Restore the origin route and apply a prefix list that denies it outbound. Compare the peer state with route receipt.
5. Restore policy; record what each command proved and why an established session was insufficient.

### Example lab 17: redistribution loop guard

**Topology:** R1/R2 in OSPF domain, R3/R4 in EIGRP domain, two border routers redistributing in both directions.

1. Originate separate prefixes on each side.
2. Set tags on imports and deny those tags on reimport.
3. Inspect RIBs and tags on both borders.
4. Remove one deny in the isolated lab; observe whether a route re-enters with altered metric/AD.
5. Restore policy and test one-link failure.

### Example lab 22: ULL incident

**Traffic:** multicast feed on path A and a redundant path B; TCP order entry on a separate routed link. Introduce a short egress burst, change source route causing RPF failure, and shift one measurement clock. The learner must separate actual packet loss from measured one-way latency error, identify the first drop point and state how each issue is verified. Do not apply all fixes at once; a sequence of one controlled change and post-check per cause earns full credit.

### Scoring

| Criterion | Points |
|---|---:|
| Correct forwarding/control-plane model | 2 |
| Evidence before changes | 2 |
| Minimal technical repair | 2 |
| Return and failure path checked | 2 |
| Post-check, rollback and explanation | 2 |

Target 8/10 per lab. The capstone target is 9/10.

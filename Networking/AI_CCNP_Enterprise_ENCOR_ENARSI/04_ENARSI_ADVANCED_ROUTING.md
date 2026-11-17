# ENARSI 1 — Advanced routing and path control

## Contents

- [Route selection and policy](#route-selection-and-policy)
- [Redistribution and summarization](#redistribution-and-summarization)
- [EIGRP](#eigrp)
- [OSPF advanced](#ospf-advanced)
- [BGP advanced](#bgp-advanced)
- [PBR, VRF-Lite and BFD](#pbr-vrf-lite-and-bfd)

## Route selection and policy

Router lookup order matters: **longest matching prefix → lowest administrative distance for the same prefix → protocol metric → installable next hop → forwarding adjacency**. A BGP table can contain a best path that is absent from the RIB when another source has lower AD for that prefix; a route can be in the RIB but fail forwarding because ARP, ACL, tunnel or egress is broken.

| Source | Typical Cisco AD | Note |
|---|---:|---|
| Connected | 0 | Directly attached |
| Static | 1 | Unless configured otherwise |
| eBGP | 20 | External peer |
| EIGRP internal | 90 | Internal route |
| OSPF | 110 | Intra/inter/external at default AD |
| EIGRP external | 170 | Redistributed route |
| iBGP | 200 | Internal BGP peer |

Do not use AD as a substitute for path policy without understanding all prefixes. Route maps combine `match` and `set`, and are used by redistribution, BGP, PBR and more. A route-map sequence with no match clauses can match all routes, while a `deny` sequence rejects a match. Be precise about the feature applying the route map.

```ios
ip prefix-list CRITICAL seq 10 permit 203.0.113.0/24
route-map SET_TAG permit 10
 match ip address prefix-list CRITICAL
 set tag 100
route-map SET_TAG deny 100
```

### Loop prevention

Split horizon prevents advertising a learned route back through the interface where it was learned in applicable protocols. Route poisoning advertises an unreachable metric. Filtering and **route tags** prevent redistributed routes from returning to their source domain. A tag is metadata; it does not automatically block anything until a policy matches it.

## Redistribution and summarization

Redistribution imports routes from one source into another. Verify source route is actually in the RIB, destination protocol has a usable seed metric/type, and the route is admitted by policy. Observe both directions and the return path.

```text
OSPF domain → ASBR → EIGRP domain
               ↑          |
               └── possible feedback loop if two-way redistribution is unfiltered
```

Example principle: set tag `100` on OSPF-origin routes entering EIGRP; deny tag `100` when importing EIGRP back into OSPF. Use explicit prefix lists and route maps; inspect their hit counters and resulting tables. Protocol-specific metric syntax and defaults vary by IOS mode, so build and verify in the target image.

**Summarization** reduces route-table size and update churn but can create a black hole if a summary survives while a component prefix disappears. A discard/Null0 route may be installed to prevent loops for unmatched addresses inside an advertised summary. Manual versus automatic summarization behaviour differs by protocol/version; inspect configured and advertised prefixes rather than assuming.

## EIGRP

EIGRP uses DUAL. The **successor** is the best loop-free next hop. A **feasible successor** is a prequalified backup whose reported distance (RD) is strictly less than the local feasible distance (FD) for the current successor: `RD < FD`. Equality does not meet the feasible condition. A path can still be loop-free even if it fails FC, but DUAL must query to establish it.

```text
Local FD = 1000
Neighbor A RD = 700  → feasible backup
Neighbor B RD = 1000 → not feasible by strict inequality
```

If no feasible successor exists and the successor fails, a route becomes **active** and queries neighbours. **Stuck in active** indicates queries/replies are not completing in time; inspect reachability, scale, congestion and stub design. A stub limits query propagation at a branch. Variance can install unequal-cost feasible paths; verify actual traffic sharing and whether platform hash behaviour matches intent.

Metric is primarily bandwidth/delay with default K values; mismatched K values prevent adjacency. Classic and named mode have different command structure; learn to recognise both. Authentication, AS/address-family, subnet and passive settings are common neighbour faults.

Minimal classic-mode lab configuration:

```ios
router eigrp 100
 eigrp router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3
 network 10.1.0.0 0.0.255.255
 passive-interface default
 no passive-interface GigabitEthernet0/0
```

For named mode, enter `router eigrp <name>`, then an IPv4/IPv6 address family with an autonomous system. Interface behaviour and topology policy sit under their address-family submodes. The underlying DUAL/FC rules stay the same; exact submode syntax is image dependent. Compare `show running-config | section router eigrp` and neighbour/topology output rather than learning one mode by visual resemblance alone.

```ios
show ip eigrp neighbors
show ip eigrp topology all-links
show ip eigrp interfaces detail
show ip route eigrp
show ipv6 eigrp neighbors
```

🟪 **ULL:** A rapid feasible-successor transition may reduce outage, but the backup path may have different queueing or delay. Measure it.

## OSPF advanced

**Router roles:** internal router has all interfaces in one area; backbone router has an area 0 interface; ABR connects areas; ASBR injects external routes. **Area types:** normal accepts interarea/external; stub removes external LSAs and receives a default; totally stubby further limits interarea LSAs; NSSA permits local external injection as type 7 and translation by an ABR. Know where a virtual link may repair a discontiguous area 0 and why redesign is usually preferable.

**Path preference:** intra-area over interarea over external, subject to OSPF rules; external E1 includes internal cost to ASBR while E2 primarily preserves external metric. Do not confuse OSPF preference with RIB AD comparisons to another protocol.

An ABR lab can attach one interface to area 0 and another to area 10:

```ios
router ospf 10
 router-id 2.2.2.2
 area 10 range 10.10.0.0 255.255.0.0
interface GigabitEthernet0/0
 ip ospf 10 area 0
interface GigabitEthernet0/1
 ip ospf 10 area 10
```

Observe the component prefixes and advertised summary before shutting one area-10 link. The summary may persist while another component remains, so verify the precise site prefix at the receiver.

Troubleshooting sequence:

1. Interface and matching network/prefix.
2. Area, type, timers, options/authentication and router ID.
3. Neighbour state and DR/BDR expectations.
4. LSDB contains the required LSA.
5. Route appears in OSPF calculation and RIB.
6. Next hop resolves and return path exists.

```ios
show ip ospf neighbor detail
show ip ospf interface
show ip ospf database
show ip ospf border-routers
show ip route ospf
```

If the LSDB has the prefix but RIB does not, examine competing route source, area/path preference, summarization/filtering and next-hop resolution. Cisco's [route database troubleshooting](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7112-26.html) covers this distinction.

## BGP advanced

**eBGP** crosses AS boundaries; **iBGP** distributes paths within an AS. iBGP-learned routes are not advertised to other iBGP peers by default; a **route reflector** can remove full-mesh scaling pressure. BGP sessions use TCP 179; establishment does not prove correct policies. Peer with loopbacks using `update-source`; eBGP multihop needs matching TTL/reachability design. BGP authentication and 4-byte AS support depend on configuration/platform.

```text
Peer Established → prefix received → next hop reachable → policy accepted
→ best path selected → RIB installation → FIB/adjacency → data traffic
```

**BGP attributes:** Cisco weight is local-only; local preference influences outbound path across an AS; AS path and origin influence preference; MED can signal preferred entry to a neighbouring AS under comparison rules. The full best-path sequence has exceptions and configuration knobs; use Cisco's [best-path reference](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html) when exact tie-breaks matter. Do not assume increasing MED is preferable; lower commonly wins when compared.

```ios
show ip bgp summary
show ip bgp neighbors 192.0.2.2 received-routes
show ip bgp neighbors 192.0.2.2 advertised-routes
show ip bgp 203.0.113.0/24
show ip route 203.0.113.0
show ip cef 203.0.113.1
```

`received-routes` may require soft reconfiguration or route-refresh support on the platform. Inspect route-map/prefix-list direction and implicit denials. Validate both IPv4 and IPv6 address-family activation. Be careful with broad changes to local preference, route reflection or inbound filtering: they can move many flows.

Example outbound filtering on a lab peer:

```ios
ip prefix-list EXPORT_ONLY seq 10 permit 203.0.113.0/24
route-map EXPORT permit 10
 match ip address prefix-list EXPORT_ONLY
router bgp 65001
 address-family ipv4
  neighbor 192.0.2.2 route-map EXPORT out
```

The `network` statement still requires the exact prefix in the local RIB. A route map without a matching permit silently filters it; verify `advertised-routes` at R1 and receipt at R2. IPv6 requires the corresponding address family and IPv6 prefix matching.

## PBR, VRF-Lite and BFD

**PBR** applies a route map inbound to an interface to select a next hop for matched traffic. A policy can match but fail when next hop becomes unreachable; use tracking or appropriate fallback and verify actual forwarding.

```ios
ip access-list extended SPECIAL_TRAFFIC
 permit ip 10.10.10.0 0.0.0.255 203.0.113.0 0.0.0.255
route-map SPECIAL_PATH permit 10
 match ip address SPECIAL_TRAFFIC
 set ip next-hop 192.0.2.2
interface GigabitEthernet0/1
 ip policy route-map SPECIAL_PATH
show route-map
show ip policy
```

**VRF-Lite** gives multiple independent routing tables without MPLS. Check interface-to-VRF membership, route entries and whether a ping/traceroute specified the right VRF. **BFD** provides fast neighbour failure detection for supported routing protocols, but aggressive timers can increase false positives or CPU load. Distinguish fast detection from actual reconvergence and application recovery.

🟪 **ULL:** Never infer deterministic latency from BGP attribute order or lowest routing metric. The selected path may differ in fibre length, device queueing and exchange handoff; measure both normal and backup routes.

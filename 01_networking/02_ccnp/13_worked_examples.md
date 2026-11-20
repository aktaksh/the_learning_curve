# Worked examples — calculate, configure, verify

## Contents

- [1. Longest prefix, AD and FIB](#1-longest-prefix-ad-and-fib)
- [2. EIGRP feasible successor](#2-eigrp-feasible-successor)
- [3. BGP best-path decision](#3-bgp-best-path-decision)
- [4. OSPF LSDB to RIB](#4-ospf-lsdb-to-rib)
- [5. Redistribution with a tag](#5-redistribution-with-a-tag)
- [6. Multicast RPF](#6-multicast-rpf)
- [7. Overlay MTU](#7-overlay-mtu)
- [8. QoS and IP SLA](#8-qos-and-ip-sla)

## 1. Longest prefix, AD and FIB

A packet is headed for `10.24.18.99`. The router has:

```text
O 10.24.0.0/16     [110/20] via 192.0.2.2
S 10.24.18.0/24    [200/0]  via 192.0.2.6
B 10.24.18.0/24    [20/0]   via 198.51.100.2
```

First compare prefix lengths: `/24` wins over `/16`. Then compare same-prefix route sources: eBGP AD 20 wins over static AD 200. The chosen RIB route points to `198.51.100.2`. Next inspect CEF and the adjacency for that next hop. If the next hop has no ARP entry, correct route selection still cannot forward the packet.

**Tutor check:** If a new static `10.24.18.96/27` route appears at AD 250, which path handles `.99`? The `/27` route: its longer prefix wins before AD. What if the `/27` next hop is unresolved? Check whether it is installed in RIB and what fallback route remains; do not assume the packet automatically uses the `/24` under every platform condition.

## 2. EIGRP feasible successor

Router R1's selected successor for `10.40.0.0/16` has FD 1000. Two alternative neighbours report:

| Neighbour | Reported distance | Local total metric | Meets FC? |
|---|---:|---:|---|
| R3 | 700 | 1200 | Yes (`700 < 1000`) |
| R4 | 1000 | 1050 | No (`1000 < 1000` is false) |

If the successor fails, R3 is a feasible successor and can be installed without DUAL querying. R4 might eventually provide a valid path, but it is not a prequalified feasible successor under current numbers. Inspect `show ip eigrp topology all-links`; the normal topology display may hide non-feasible alternatives.

**Tutor check:** Does the lower *local total* metric of R4 make it feasible? No. FC uses the neighbour's RD against local FD, not only the local total metric.

## 3. BGP best-path decision

R1 receives two valid paths to `203.0.113.0/24`:

| Path | Weight | Local preference | AS path | MED |
|---|---:|---:|---|---:|
| A | 0 | 200 | `65010 65020` | 30 |
| B | 0 | 100 | `65030` | 5 |

Assuming usual Cisco path rules and no earlier override, A wins at local preference even though it has a longer AS path and higher MED. If weight on B becomes 50, B wins at weight before local preference. Always confirm paths are valid, next hops resolve, and platform features have not altered best-path rules. The full order is in Cisco's [BGP best-path guide](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html).

**Tutor check:** Does choosing A prove A has lower latency? No. BGP preference expresses policy; measure the actual physical/queue path.

## 4. OSPF LSDB to RIB

R2 has a Full neighbour relationship and an LSA for `10.60.0.0/16`, but no OSPF route in the RIB. Consider three separate gates:

1. **LSDB/algorithm:** Is the LSA usable in the area and is there a path to its advertising router?
2. **RIB selection:** Does a connected/static/EIGRP route for the same `/16` beat OSPF's AD?
3. **Forwarding:** Does the selected route's next hop resolve in CEF/adjacency?

Probe in that order. A Full neighbour tells you the control-plane exchange works with *that neighbour*; it does not prove this destination is installed or forwarded.

## 5. Redistribution with a tag

Two ASBRs connect OSPF and EIGRP. Both redistribute both ways. Without policy, a route imported from OSPF into EIGRP can return through the other ASBR and look like a new external OSPF route. One approach:

```text
OSPF-origin prefix --import with tag 100--> EIGRP
EIGRP-to-OSPF route map: deny tag 100

EIGRP-origin prefix --import with tag 200--> OSPF
OSPF-to-EIGRP route map: deny tag 200
```

Use explicit prefix lists and seed metrics as needed. Inspect the source route, receiving protocol database, tag and final RIB at each border. A tag on its own is inert; matching deny policy makes it useful. Test a border failure because redundant redistribution is where a hidden loop often appears.

## 6. Multicast RPF

Source `192.0.2.10` sends group `232.10.10.10`. The receiver has joined `(192.0.2.10, 232.10.10.10)`. A last-hop router receives packets on Gi0/1, but its unicast route back to `192.0.2.10` says Gi0/2. RPF fails, so joining the group is insufficient.

```text
Receiver join: correct
PIM neighbour: correct
RPF source-facing interface: Gi0/2
Actual arrival: Gi0/1 → reject
```

Inspect `show ip rpf 192.0.2.10`, `show ip mroute 232.10.10.10` and the route to source. Fix underlay path/PIM design or intentional multicast routing policy. Cisco's [multicast troubleshooting guide](https://www.cisco.com/c/en/us/support/docs/ip/ip-multicast/13726-57.html) describes these checks.

## 7. Overlay MTU

A physical path supports a 1500-byte IP packet. A GRE or GRE+IPsec tunnel adds headers. The effective payload that fits without fragmentation is smaller than 1500. A 64-byte ping may work while a TCP session sending large segments stalls if PMTUD ICMP is blocked.

Test tunnel endpoints and underlay first; then use increasing DF-set probes, inspect fragmentation/ICMP and set a suitable tunnel MTU or TCP MSS according to the chosen encapsulation and actual path. Avoid memorising one universal overhead number; GRE, IPsec mode, IPv4/IPv6 underlay and NAT traversal change it.

## 8. QoS and IP SLA

A branch WAN link is 1 Gbit/s. Order-entry traffic averages 2 Mbit/s; bulk backup occasionally reaches 950 Mbit/s. A strict priority class can protect order traffic during contention, but a too-small policer could drop valid bursts. An IP SLA probe to the branch gateway reports stable RTT, yet order ACK p99 increases.

Check whether the probe uses the same QoS class and path as the application. Inspect egress policy counters, queue drops, route changes, TCP retransmissions and timestamps. A probe with different packet size/DSCP/source may miss the exact problem. Tune only after you locate the queue or path where delay appears.

**Tutor check:** Is a 2 Mbit/s average proof that a 10 Mbit/s priority limit is sufficient? No; microburst peaks and packet sizes determine short-window queue behaviour.

# Module 3 — IP Routing

> **Exam weight:** 20%  
> **Core skill:** Given a destination and routing table, identify the selected route and explain why.

## Packet-Forwarding Decision

A router:

1. Removes the incoming Layer 2 header.
2. Checks the destination IP address.
3. Finds matching routes.
4. Selects the longest matching prefix.
5. Resolves the next hop/outgoing interface.
6. Decrements IPv4 TTL or IPv6 Hop Limit.
7. Re-encapsulates the packet for the next link.

The source and destination IP addresses normally remain end-to-end unless NAT occurs. The Layer 2 source and destination change at every routed hop.

## Reading the Routing Table

```ios
show ip route
show ip route 10.40.8.9
show ipv6 route
show ip protocols
```

Example:

```text
O    10.40.0.0/16 [110/20] via 10.0.0.2, 00:02:10, GigabitEthernet0/0
S    10.40.8.0/24 [1/0] via 10.0.0.6
S*   0.0.0.0/0 [1/0] via 192.0.2.1
```

Traffic to `10.40.8.9` uses `10.40.8.0/24`, not OSPF `/16`, because `/24` is the longer prefix. Administrative distance does not compare routes with different prefix lengths.

### Route Components

- **Source code:** connected, local, static, OSPF and others.
- **Prefix/mask:** destinations matched by the route.
- **Administrative distance:** trustworthiness of the route source.
- **Metric:** preference inside a routing protocol.
- **Next hop:** router to receive the packet.
- **Outgoing interface:** local egress.

### Selection Order

1. Longest prefix match.
2. Lowest administrative distance among routes to the same prefix.
3. Lowest protocol metric among routes learned by the same protocol.
4. Equal-cost paths may be installed together when supported.

Common defaults to recognise: connected 0, static 1 and OSPF 110. Do not infer all values from this short list; verify the platform when operating a real network.

## Static Routing

### IPv4 Default Route

```ios
ip route 0.0.0.0 0.0.0.0 192.0.2.1
```

### IPv4 Network and Host Routes

```ios
ip route 10.20.0.0 255.255.0.0 192.0.2.2
ip route 10.20.30.40 255.255.255.255 192.0.2.2
```

### Exit-Interface and Fully Specified

```ios
ip route 10.30.0.0 255.255.0.0 GigabitEthernet0/0
ip route 10.30.0.0 255.255.0.0 GigabitEthernet0/0 192.0.2.2
```

On multiaccess Ethernet, specifying only an exit interface can trigger ARP for many destination addresses. A next hop or fully specified route is often clearer.

### Floating Static

A floating static route has an administrative distance higher than the preferred route, so it is installed only when the preferred route disappears.

```ios
ip route 10.40.0.0 255.255.0.0 198.51.100.2 200
```

### IPv6 Static Routes

```ios
ipv6 unicast-routing
ipv6 route ::/0 2001:db8:0:1::2
ipv6 route 2001:db8:40::/48 2001:db8:0:1::2
ipv6 route 2001:db8:40::10/128 2001:db8:0:1::2
ipv6 route 2001:db8:50::/48 2001:db8:0:2::2 200
```

When a link-local IPv6 address is the next hop, include the outgoing interface because link-local addresses are not globally unique:

```ios
ipv6 route 2001:db8:60::/48 GigabitEthernet0/0 fe80::2
```

### Static-Route Troubleshooting

1. Does the route appear in the table?
2. Is the next hop recursively reachable?
3. Is the outgoing interface up?
4. Is the mask/prefix correct?
5. Is a more-specific route taking precedence?
6. Is there a return route?
7. Is an ACL or security feature dropping traffic?
8. Does ARP/ND resolve the next hop?

```ios
show running-config | include ^ip route
show running-config | include ^ipv6 route
show ip route static
show ipv6 route static
show arp
show ipv6 neighbors
ping <next-hop>
traceroute <destination>
```

## OSPF Foundations

OSPF is a link-state interior gateway protocol. Routers form adjacencies, exchange link-state information, build a common topology database and run SPF to determine shortest paths.

### Router ID

The router ID is a 32-bit dotted-decimal identifier, not necessarily a reachable IPv4 address. Selection generally prefers:

1. Manually configured router ID.
2. Highest loopback IPv4 address.
3. Highest active physical-interface IPv4 address.

Set it explicitly for predictable operations.

### Neighbor Requirements

Common causes of failed adjacency include:

- Interfaces not operational.
- Different area IDs.
- IPv4 subnet mismatch for OSPFv2.
- Hello/dead timer mismatch.
- Network-type mismatch in some designs.
- Duplicate router IDs.
- Passive interface.
- MTU mismatch, often stalling database exchange.
- ACL/control-plane filtering.

Authentication is excluded from the v2.0 OSPF adjacency objective, but be aware that production networks may use it.

## OSPFv2 for IPv4

### Network-Statement Method

```ios
router ospf 10
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.3 area 0
 network 10.1.0.0 0.0.255.255 area 0
 passive-interface default
 no passive-interface GigabitEthernet0/0
```

The OSPF network statement matches local interface addresses; it is not a route-advertisement statement in the same sense as an ACL.

### Interface Method

```ios
interface GigabitEthernet0/0
 ip address 10.0.12.1 255.255.255.252
 ip ospf 10 area 0
```

### Verification

```ios
show ip ospf neighbor
show ip ospf interface brief
show ip ospf interface GigabitEthernet0/0
show ip ospf database
show ip route ospf
show ip protocols
```

## OSPFv3 for IPv6

```ios
ipv6 unicast-routing
ipv6 router ospf 10
 router-id 1.1.1.1
interface GigabitEthernet0/0
 ipv6 address 2001:db8:12::1/64
 ipv6 ospf 10 area 0
 no shutdown
```

OSPFv3 forms adjacencies using IPv6 link-local addresses. A 32-bit router ID is still required; it has IPv4-like notation but identifies the OSPF process.

```ios
show ipv6 ospf neighbor
show ipv6 ospf interface brief
show ipv6 ospf database
show ipv6 route ospf
```

## OSPF Network Types

### Point-to-Point

There is no DR/BDR election. Two routers can form a full adjacency directly.

```ios
interface GigabitEthernet0/0
 ip ospf network point-to-point
```

### Broadcast

Ethernet defaults to a broadcast network type. OSPF elects a DR and BDR to reduce adjacency and flooding complexity on a shared segment.

Election prefers highest interface priority, then highest router ID. Priority 0 prevents DR/BDR eligibility. Election is non-preemptive; a newly arriving router with a higher value does not automatically replace an established DR.

```ios
interface GigabitEthernet0/1
 ip ospf priority 100
```

🟥 DR/BDR status does not mean the router has the best route or becomes the default gateway. It is an OSPF adjacency/flooding role for that multiaccess segment.

## OSPF Troubleshooting Workflow

1. Check interface state and IP/prefix.
2. Verify each interface is enabled in the intended area.
3. Confirm router IDs are unique.
4. Compare network type and hello/dead timers.
5. Check passive-interface configuration.
6. Observe neighbor state.
7. Inspect logs and database.
8. Confirm expected OSPF routes enter the routing table.
9. Verify data-plane reachability and return path.

Important neighbor states include Down, Init, 2-Way, ExStart, Exchange, Loading and Full. On a broadcast network, DROTHER routers may remain 2-Way with one another while becoming Full with DR/BDR; this can be normal.

## First-Hop Redundancy

Hosts usually configure one default gateway. FHRPs present a virtual gateway backed by multiple routers.

### HSRP

- Cisco-origin protocol.
- Active router forwards for the virtual gateway.
- Standby router is prepared to take over.
- Higher priority is preferred.
- Preemption allows a higher-priority returning router to retake active status.

Illustrative configuration:

```ios
interface Vlan20
 ip address 10.20.0.2 255.255.255.0
 standby 20 ip 10.20.0.1
 standby 20 priority 110
 standby 20 preempt
```

```ios
show standby brief
show standby
```

### VRRP

- Standards-based redundancy protocol.
- Master forwards for the virtual gateway.
- Backup routers can take over.
- Higher priority is preferred.
- The address owner has special priority behaviour.

Illustrative configuration syntax varies by IOS/IOS XE release:

```ios
interface Vlan20
 ip address 10.20.0.3 255.255.255.0
 vrrp 20 ip 10.20.0.1
 vrrp 20 priority 105
 vrrp 20 preempt
```

```ios
show vrrp brief
show vrrp
```

The v2.0 objective says to interpret operational status, so prioritise reading state, virtual IP, active/master peer, priority and timers over memorising release-specific syntax.

### FHRP Troubleshooting

- Verify all peers use the same group and virtual IP.
- Confirm they share the same VLAN/subnet.
- Check priority and preemption expectations.
- Verify the intended forwarding router is active/master.
- Confirm host ARP maps the virtual IP to the virtual MAC.
- Check split-brain caused by VLAN/trunk or control-packet loss.

## Low-Latency Perspective

🟪 Longest-prefix match gives deterministic forwarding only when the control plane and table are stable. Monitor route changes and avoid accidental more-specific routes.

🟪 OSPF convergence is valuable, but a reconverged path can have different latency. Validate both primary and failure paths—not only reachability.

🟪 Equal-cost routes can distribute flows, but per-flow hashing may create different latency or asymmetry. Know the hash and design A/B paths deliberately.

🟪 FHRP failover protects gateway availability but does not guarantee session continuity, equal path latency or zero packet loss. Measure detection and convergence.

🟪 Static routing can be predictable, but excessive static configuration increases operational risk. Choose simplicity with an explicit failure model.

## Module Checklist

- [ ] Select a route using longest prefix, AD and metric in the correct order.
- [ ] Configure IPv4 and IPv6 default, network, host and floating static routes.
- [ ] Troubleshoot next-hop recursion and return routes.
- [ ] Configure single-area OSPFv2 and OSPFv3.
- [ ] Diagnose adjacency failures from output.
- [ ] Explain point-to-point versus broadcast OSPF operation.
- [ ] Interpret HSRP and VRRP state.


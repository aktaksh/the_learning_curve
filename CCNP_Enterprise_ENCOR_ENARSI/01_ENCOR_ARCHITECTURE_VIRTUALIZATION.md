# ENCOR 1 — Architecture and virtualization

## Contents

- [Enterprise design](#enterprise-design)
- [Availability and forwarding](#availability-and-forwarding)
- [QoS](#qos)
- [SD-WAN and SD-Access](#sd-wan-and-sd-access)
- [Virtualization and VRF](#virtualization-and-vrf)
- [GRE, IPsec, LISP and VXLAN](#gre-ipsec-lisp-and-vxlan)
- [Review](#review)

## Enterprise design

**Two-tier campus:** access switches connect directly to a collapsed distribution/core. **Three-tier:** access → distribution → core, used when scale and independent roles justify another layer. **Fabric:** an underlay provides reachability while an overlay carries segments and policy. A cloud connection adds provider, routing and security dependencies; it does not remove the need to design failure domains.

```text
Host -- access -- distribution -- core -- WAN/cloud
         |            |
    port policy    aggregation, L3 boundary, FHRP
```

Capacity planning uses peak plus failure-state traffic, not just average normal traffic. Oversubscription is acceptable only when the applications tolerate it. A design review asks: what fails alone, what fails together, and what path remains after failure?

For WLANs, compare controller-based, cloud-managed and distributed control. AP placement depends on client density, channel reuse, RF obstruction and roaming. Location services need sufficient AP geometry and signal observations. Learn this for ENCOR even when the ULL trading path is wired.

## Availability and forwarding

**FHRP** keeps a virtual default gateway available. **SSO** (stateful switchover) aims to preserve control-plane state across supervisor failover; feature and platform support vary. Neither guarantees that an application sees no packet loss.

The control plane chooses routes. The **RIB** records selected routes; CEF derives the **FIB** (prefix-to-forwarding action) and adjacency information (next-hop rewrite). CAM is commonly associated with Layer 2 MAC lookup; TCAM enables parallel policy and prefix matching in hardware. Packet path:

```text
Routing protocol/static route → RIB → CEF FIB + adjacency → ASIC lookup → egress queue → wire
```

If a route is in BGP but absent from the RIB, check path validity, next-hop reachability and competing sources. If it is in the RIB but traffic fails, check CEF/adjacency, ARP/ND, ACL, tunnel MTU and egress counters.

```ios
show ip route 203.0.113.0
show ip cef 203.0.113.9 detail
show adjacency detail
show platform hardware capacity
```

🟪 **ULL:** Hardware forwarding is fast, but queueing, drops and route churn determine tail latency. Measure path and failure state; do not infer latency from a route's existence.

## QoS

QoS has four steps: **classify/mark**, **queue/schedule**, **police/shape**, **observe**. DSCP marks Layer 3 priority; 802.1p PCP marks tagged Ethernet. A trust boundary determines whether endpoint marks are accepted or rewritten. LLQ offers strict priority subject to policing; CBWFQ divides service among classes. WRED can drop early under congestion. Policing drops or remarks excess traffic; shaping buffers and spaces packets.

```text
Ingress → trust/remark → class-map → policy-map → egress scheduler → counters
```

Illustrative IOS policy:

```ios
class-map match-any ORDER_ENTRY
 match dscp ef
policy-map WAN_OUT
 class ORDER_ENTRY
  priority percent 10
 class class-default
  fair-queue
interface GigabitEthernet0/1
 service-policy output WAN_OUT
show policy-map interface GigabitEthernet0/1
```

Check the interface and platform before using commands. A policy with no matching counters may be attached in the wrong direction, have a wrong class match, or never see traffic. Wireless QoS maps client traffic into access categories; airtime contention still matters.

🟪 **ULL:** QoS can protect a small critical class during contention, but adding a priority queue does not create bandwidth or remove microbursts. Confirm latency percentiles and drop counters for all affected classes.

## SD-WAN and SD-Access

**Cisco SD-WAN:** edge devices forward packets; management/control components distribute policy and reachability. Know controller roles, separation of control/data planes, overlays, transport independence and policy limitations. Avoid assuming an SD-WAN policy is appropriate for an exchange path without measuring encapsulation, path steering and failure behaviour.

**Cisco SD-Access:** fabric edge attaches endpoints, control plane maps endpoint identity/location, border connects outside domains. LISP is used for mapping and VXLAN for overlay forwarding in common fabric designs. Traditional campus segments can interoperate through borders and policy boundaries.

## Virtualization and VRF

A VM runs on a hypervisor, connects through a vSwitch/vNIC and may share CPU, NIC and memory resources. A type 1 hypervisor runs on hardware; type 2 runs over a host OS. A **VRF** creates an independent routing table on the same router. Overlapping addresses can exist in different VRFs because lookups remain separate.

```ios
vrf definition BLUE
 address-family ipv4
 exit-address-family
interface GigabitEthernet0/1
 vrf forwarding BLUE
 ip address 10.10.1.1 255.255.255.0
show ip route vrf BLUE
ping vrf BLUE 10.10.1.2
```

Applying `vrf forwarding` may remove an existing interface IP; configure it in the correct order. VRF isolation is not automatically a firewall. Route leaking requires explicit design and verification.

## GRE, IPsec, LISP and VXLAN

**GRE** adds an outer header so packets can traverse an IP underlay and carry protocols the underlay may not directly support. It offers no confidentiality by itself. **IPsec** supplies encryption/authentication and may protect GRE. Encapsulation reduces effective MTU; a ping with small packets may pass while larger packets fail.

```ios
interface Tunnel10
 ip address 172.16.10.1 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 198.51.100.2
show interface Tunnel10
```

### GRE protected by IPsec: configuration sequence

In an IOS XE lab, first establish routed reachability between the tunnel source and destination. Then build matching IKEv2 identity/authentication, an IPsec transform/profile, and attach the profile to the tunnel. The two peers need reciprocal tunnel source/destination and compatible crypto settings.

```ios
! Example skeleton for one side; use unique lab secrets and matching peer values.
crypto ikev2 keyring LAB_KEYS
 peer REMOTE
  address 198.51.100.2
  pre-shared-key <lab-secret>
crypto ikev2 profile LAB_IKE
 match identity remote address 198.51.100.2 255.255.255.255
 authentication local pre-share
 authentication remote pre-share
 keyring local LAB_KEYS
crypto ipsec transform-set LAB_SET esp-aes esp-sha-hmac
 mode tunnel
crypto ipsec profile LAB_IPSEC
 set transform-set LAB_SET
 set ikev2-profile LAB_IKE
interface Tunnel10
 tunnel protection ipsec profile LAB_IPSEC
```

Prove four layers separately: underlay ping, tunnel/overlay ping, IKEv2 SA, and increasing IPsec encapsulation/decapsulation counters while application traffic flows. If the platform rejects syntax, follow the release-specific [Cisco GRE over IPsec guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr3-fwd/gre/gre-configuration-guide/m-gre-over-ipsec.html). Do not treat a configured profile as evidence of encryption.

**LISP** separates endpoint identity from location through mappings. **VXLAN** uses an overlay identifier (VNI) and encapsulates Layer 2/Layer 3 traffic over an IP network. Understand mapping and encapsulation roles; do not treat either as an automatic speed improvement.

## Review

1. Draw the RIB → FIB → adjacency path, then explain how a route can exist without a usable adjacency.
2. Explain the difference between policing and shaping using an egress queue example.
3. Name two causes of tunnel black-holing with a working small ping.
4. Trace a host in VRF BLUE trying to reach VRF RED. What additional configuration would be needed?
5. State the control and data-plane roles in SD-WAN and SD-Access.

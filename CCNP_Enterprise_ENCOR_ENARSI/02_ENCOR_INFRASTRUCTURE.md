# ENCOR 2 — Infrastructure

## Contents

- [Layer 2 operations](#layer-2-operations)
- [OSPFv2 and OSPFv3](#ospfv2-and-ospfv3)
- [eBGP and policy routing](#ebgp-and-policy-routing)
- [Wireless](#wireless)
- [IP services: time, multicast, NAT and FHRP](#ip-services-time-multicast-nat-and-fhrp)

## Layer 2 operations

For a failed trunk, verify administrative mode, operational mode, native VLAN, allowed VLANs, STP forwarding and MAC learning. DTP dynamic settings may fail to negotiate as expected. Set an explicit mode where the design requires it.

```ios
show interfaces switchport
show interfaces trunk
show vlan brief
show spanning-tree vlan 20
show mac address-table vlan 20
```

For LACP, both ends must agree on Layer 2/Layer 3 mode, speed and trunk/access attributes. At least one side must be active. A single flow normally hashes to one member; the bundle offers aggregate capacity and resilience.

```ios
show etherchannel summary
show lacp neighbor
show interfaces port-channel 1
```

**RSTP** roles are root, designated, alternate and backup; states are discarding, learning and forwarding. **MST** maps VLANs to a smaller number of instances. MST region name, revision and VLAN-to-instance mapping must agree at the boundary. Root Guard prevents an unexpected superior root; BPDU Guard protects true edge ports.

🟪 **ULL:** A loop or unexpected STP transition can overwhelm a feed. Record normal and backup paths and compare their hop count and congestion under failure.

## OSPFv2 and OSPFv3

OSPF is link state. Neighbours exchange LSAs, calculate SPF and install selected routes. ENCOR expects multiple normal areas, ABR summarization, filtering, passive interfaces and network types; ENARSI expands area types and failures.

```ios
router ospf 10
 router-id 1.1.1.1
 passive-interface default
 no passive-interface GigabitEthernet0/0
interface GigabitEthernet0/0
 ip ospf 10 area 0
 ip ospf network point-to-point
```

OSPFv3 carries IPv6 in the course lab; use a unique 32-bit router ID and enable IPv6 routing. IOS/IOS XE also supports address-family style OSPFv3; check image syntax.

```ios
ipv6 unicast-routing
ipv6 router ospf 10
 router-id 1.1.1.1
interface GigabitEthernet0/0
 ipv6 address 2001:db8:12::1/64
 ipv6 ospf 10 area 0
```

On broadcast Ethernet, DR/BDR election reduces full adjacencies. On point-to-point links there is no election. Area 0 is backbone; interarea traffic should traverse it in normal designs. ABR summarization can reduce routes, but a summary may conceal component failure or attract traffic toward a missing specific destination.

```ios
show ip ospf neighbor
show ip ospf interface
show ip ospf database
show ip route ospf
show ipv6 ospf neighbor
```

For adjacency failure, inspect interface/subnet, area, timers, network type, duplicate router ID, MTU, passive status and control-plane filtering. A 2-Way DROTHER relationship on broadcast media can be normal. Cisco's [OSPF troubleshooting guide](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13699-29.html) provides a useful fault list.

## eBGP and policy routing

Directly connected eBGP peers use different AS numbers. Neighbour establishment alone does not guarantee advertisement or installation. A `network` statement needs an exact matching route in the RIB.

```ios
router bgp 65001
 bgp router-id 1.1.1.1
 neighbor 192.0.2.2 remote-as 65002
 address-family ipv4
  network 203.0.113.0 mask 255.255.255.0
  neighbor 192.0.2.2 activate
 exit-address-family
show ip bgp summary
show ip bgp
show ip route bgp
```

Trace BGP in four steps: TCP/peer state → prefix received → path valid/best → RIB/FIB installed. A next hop that cannot resolve blocks installation. Basic best-path factors include weight, local preference, local origination, AS path, origin, MED and eBGP/iBGP status; the exact later tie breakers and exceptions are in Cisco's [best path guide](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html).

**Policy-based routing (PBR)** can choose a next hop based on source/application policy before ordinary destination lookup. It is powerful and can silently create asymmetry. ENCOR requires description; ENARSI requires configure and verify.

## Wireless

RF power, RSSI, SNR, noise, channels and client radio capability determine connection quality. AP modes and antenna patterns affect coverage. An AP discovers and joins a controller, receives configuration and serves clients. Layer 2 roaming stays in a subnet; Layer 3 roaming crosses subnets and needs architecture support. Profiles/tags provide segmentation and policy. Use the WLC GUI to diagnose client association, authentication, DHCP and policy profile; the blueprint explicitly mentions GUI-only WLAN troubleshooting.

```text
Client sees SSID → 802.11 association → authentication → policy/VLAN → DHCP → DNS/application
```

## IP services: time, multicast, NAT and FHRP

**NTP** aligns ordinary device clocks. **PTP** uses a grandmaster and hardware timestamping for much tighter accuracy when correctly engineered. Interpret offset, selected source, clock state and path asymmetry; a locked state alone does not prove end-to-end timestamp accuracy.

**NAT/PAT:** inspect inside/outside roles, matching ACL/policy, translation counters and return routes. **HSRP/VRRP:** inspect virtual gateway, active/master peer, priority, preemption and tracking.

**Multicast:** IGMPv2 joins a group; IGMPv3 can specify a source. PIM builds routed multicast distribution. An RPF check accepts traffic arriving on the interface the unicast route would use toward the source; an unexpected source route can cause valid packets to be discarded.

```text
Publisher → first-hop router → PIM tree → last-hop router → IGMP receiver
             RPF toward source            group/source membership
```

```ios
show ip igmp groups
show ip mroute
show ip pim neighbor
show ip rpf 192.0.2.10
show standby brief
show vrrp brief
show ip nat translations
```

🟪 **ULL:** Exchange market data commonly uses multicast. Distinguish an IGMP join failure, PIM tree failure, RPF failure and switch queue drop from packet evidence; they require different repairs.

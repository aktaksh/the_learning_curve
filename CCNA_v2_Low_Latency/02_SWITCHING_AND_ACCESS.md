# Module 2 — Switching and Network Access

> **Exam weight:** 25%  
> **Core skill:** Configure a switched topology, prove its forwarding state and repair it without creating a loop.

## Ethernet Switching

A switch learns the source MAC address of each received frame and associates it with the ingress port and VLAN. For the destination MAC it:

- Forwards a known unicast only through the learned port.
- Floods an unknown unicast within the VLAN except through the ingress port.
- Floods broadcasts within the VLAN.
- Forwards relevant multicast according to Layer 2 behaviour and features such as IGMP snooping.
- Filters when source and destination are reachable through the same ingress port.

```ios
show mac address-table
show mac address-table dynamic
show mac address-table interface GigabitEthernet1/0/10
clear mac address-table dynamic
```

Each VLAN is a separate broadcast domain. A router or multilayer switch is required for communication between VLANs.

## Interface Modes

### Access Port

```ios
interface GigabitEthernet1/0/10
 description USER-PC-10
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
```

An access port normally carries one untagged data VLAN. Explicit mode avoids negotiation surprises.

### Trunk Port

```ios
interface GigabitEthernet1/0/48
 description TRUNK-TO-SW2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan 10,20,30,999
 no shutdown
```

Some platforms support only 802.1Q and omit the encapsulation command.

An 802.1Q trunk carries multiple VLANs. Frames in the native VLAN are untagged by default. Native-VLAN disagreement can leak traffic into the wrong VLAN and produce control-protocol warnings.

```ios
show interfaces trunk
show interfaces switchport
show vlan brief
```

🟥 A VLAN being present in `show vlan brief` does not prove it is permitted and forwarding over a trunk.

### Routed Port

```ios
interface GigabitEthernet1/0/47
 no switchport
 ip address 10.255.0.1 255.255.255.252
 no shutdown
```

A routed port behaves as a router interface and does not belong to a Layer 2 VLAN.

## Switch Virtual Interfaces

An SVI is a logical Layer 3 interface associated with a VLAN.

```ios
ip routing
vlan 20
 name USERS
interface Vlan20
 ip address 10.20.0.1 255.255.255.0
 no shutdown
```

For an SVI to be operational, the VLAN must exist and normally at least one associated Layer 2 port/trunk must be active and forwarding. `ip routing` is required for a multilayer switch to route between SVIs.

For a Layer 2-only switch management SVI:

```ios
interface Vlan99
 ip address 10.99.0.12 255.255.255.0
 no shutdown
ip default-gateway 10.99.0.1
```

Do not confuse `ip default-gateway` on a non-routing switch with `ip route 0.0.0.0 0.0.0.0` on a router/multilayer switch.

## Edge Device Connectivity

| Device | Typical switchport design |
|---|---|
| Desktop/printer/IoT | Access VLAN, PortFast, BPDU Guard |
| IP phone + desktop | Access VLAN plus voice VLAN |
| Standalone AP | Access or trunk depending on SSID/VLAN design |
| Controller-based AP | Often management access; tunnelling depends on architecture |
| Hypervisor | Trunk and possibly LACP port channel |
| Firewall/router | Routed link or 802.1Q trunk |

### Voice VLAN

```ios
interface GigabitEthernet1/0/12
 switchport mode access
 switchport access vlan 20
 switchport voice vlan 30
 spanning-tree portfast
```

The attached phone can tag voice frames for VLAN 30 while the downstream PC sends untagged data frames assigned to VLAN 20.

### PoE

Power over Ethernet supplies power to phones, APs and IoT devices. Troubleshooting includes port capability, power budget, device class/negotiation, cabling and administrative state.

```ios
show power inline
show power inline interface GigabitEthernet1/0/12
```

## EtherChannel and LACP

EtherChannel bundles compatible physical links into one logical port channel. Benefits include additional aggregate bandwidth and link redundancy. A single flow is normally hashed to one member; one flow does not automatically use the sum of all links.

### Modes

| Mode | Protocol/behaviour |
|---|---|
| `active` | Initiates LACP |
| `passive` | Responds to LACP |
| `on` | Static, no negotiation |

At least one LACP side must be active. Passive/passive does not form.

### Layer 2 EtherChannel

```ios
interface range GigabitEthernet1/0/47-48
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,999
 channel-group 1 mode active
 no shutdown
interface Port-channel1
 description LACP-TRUNK-TO-SW2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,999
```

### Layer 3 EtherChannel

```ios
interface range GigabitEthernet1/0/45-46
 no switchport
 channel-group 10 mode active
 no shutdown
interface Port-channel10
 no switchport
 ip address 10.255.10.1 255.255.255.252
```

### Consistency Requirements

Members should agree on speed, duplex, Layer 2/3 mode, access VLAN or trunk properties and other platform-required attributes. Configure common policy on the port-channel and verify members.

```ios
show etherchannel summary
show etherchannel port-channel
show lacp neighbor
show interfaces port-channel 1
```

Common flags: `P` bundled, `I` stand-alone, `s` suspended, and `D` down. Interpret the legend shown by the device rather than memorising without context.

## CDP and LLDP

CDP is Cisco proprietary. LLDP is an IEEE-standard, multi-vendor discovery protocol. They can reveal neighbor identity, capability, local and remote ports, platform and management address.

```ios
show cdp neighbors
show cdp neighbors detail
show lldp neighbors
show lldp neighbors detail
show interfaces description
```

Use discovery data to validate documentation:

1. Compare the expected neighbor with the discovered device.
2. Compare local and remote ports.
3. Confirm device capabilities fit the diagram.
4. Confirm management address and platform.
5. Investigate missing or duplicate links.

Discovery can be disabled globally or per interface where exposure is inappropriate.

## Rapid PVST+

Spanning Tree Protocol prevents Layer 2 loops by producing a loop-free logical topology. Rapid PVST+ runs a rapid spanning-tree instance per VLAN.

### Why Loops Are Dangerous

Ethernet frames have no Layer 2 TTL. A loop can create broadcast storms, multiple frame copies and MAC-table instability. Control-plane and user traffic can be overwhelmed quickly.

### Root Bridge Election

The switch with the lowest bridge ID becomes root. The bridge ID includes priority and MAC-related system ID information. Lower is better.

```ios
spanning-tree vlan 10 root primary
spanning-tree vlan 10 root secondary
show spanning-tree vlan 10
```

### Port Roles

- **Root port:** best path toward root on a non-root switch.
- **Designated port:** best forwarding port for a segment.
- **Alternate port:** backup path toward root.
- **Backup port:** backup on the same shared segment; uncommon in modern switched designs.

### Port States

Rapid STP uses discarding, learning and forwarding.

- **Discarding:** no user-frame forwarding or MAC learning.
- **Learning:** learns MAC addresses but does not forward user frames.
- **Forwarding:** learns and forwards.

### Selection Logic

Prefer, in order:

1. Lowest root bridge ID.
2. Lowest root path cost.
3. Lowest sender bridge ID.
4. Lowest sender port ID.

### PortFast

PortFast allows an edge port to transition rapidly to forwarding. It does not disable STP. Use it for true end-host-facing ports, not arbitrary switch-to-switch links.

```ios
interface GigabitEthernet1/0/10
 spanning-tree portfast
```

### BPDU Guard

BPDU Guard protects an edge port by err-disabling it if a BPDU arrives.

```ios
interface GigabitEthernet1/0/10
 spanning-tree bpduguard enable
```

### Root Guard

Root Guard prevents a port from accepting a superior BPDU that would move the root behind that port. It places the port in a root-inconsistent state while the superior condition exists.

```ios
interface GigabitEthernet1/0/20
 spanning-tree guard root
```

### Loop Guard

Loop Guard protects non-designated point-to-point links from incorrectly transitioning to forwarding when expected BPDUs stop arriving.

```ios
interface GigabitEthernet1/0/48
 spanning-tree guard loop
```

🟥 Root Guard controls root placement; BPDU Guard protects edge ports; Loop Guard addresses unidirectional/control-plane loss on redundant links.

## Layer 2/Layer 3 Troubleshooting

### Core Commands

```ios
show interfaces status
show interfaces switchport
show interfaces trunk
show vlan brief
show mac address-table
show arp
show spanning-tree
show etherchannel summary
show cdp neighbors detail
show lldp neighbors detail
show ip interface brief
show ip route
show logging
```

### Example: Same-VLAN Hosts Cannot Communicate

1. Confirm both interfaces are physically up.
2. Confirm both are access ports in the expected VLAN.
3. Confirm the VLAN exists and is active.
4. Confirm the VLAN is allowed over intervening trunks.
5. Confirm STP forwards on the path.
6. Check MAC learning for each host.
7. Check host address/mask and local firewalls.

### Example: Inter-VLAN Failure

1. Prove same-VLAN communication first.
2. Check the host default gateway.
3. Check SVI state and address.
4. Confirm `ip routing` on the multilayer switch.
5. Check routing and ACL policy.
6. Verify the return path.

### Ping and Extended Ping

Extended ping can select source address/interface, size and other parameters. This tests the path from the same source identity used by the affected traffic.

### Traceroute

Traceroute reveals responding Layer 3 hops by varying TTL/hop limit. Missing responses do not always mean forwarding failure; devices may filter or deprioritise diagnostic traffic.

### Packet Capture

A capture can prove whether ARP/ND, DHCP, TCP handshakes or ICMP messages appear. Establish capture location and direction before interpreting absence.

## Low-Latency Perspective

🟪 Each extra Layer 2 hop, congested queue or reconvergence event can add variability. Keep the hot path simple and explicitly document forwarding and failure paths.

🟪 LACP adds resiliency and aggregate capacity, but a single market-data flow normally follows one member according to a hash. Confirm the hashing fields and distribution.

🟪 STP remains essential where Layer 2 redundancy exists, but deterministic low-latency designs often minimise Layer 2 failure domains and prefer routed boundaries.

🟪 Native VLANs and broad allowed-VLAN lists increase ambiguity and blast radius. Prune trunks to required VLANs.

🟪 Output drops can result from microbursts even when average utilisation looks low. Interface averages hide short queue bursts.

## Module Checklist

- [ ] Configure access, trunk and routed ports.
- [ ] Configure SVIs and explain their line protocol state.
- [ ] Build L2 and L3 LACP EtherChannels.
- [ ] Connect edge devices using suitable VLAN, voice and PoE settings.
- [ ] Validate diagrams with CDP/LLDP.
- [ ] Determine Rapid PVST+ root, roles, states and tie-breakers.
- [ ] Select PortFast, Root Guard, Loop Guard or BPDU Guard correctly.
- [ ] Troubleshoot VLAN, trunk, MAC, STP and EtherChannel faults.


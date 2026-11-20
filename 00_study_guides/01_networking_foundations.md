# Networking foundations: addressing, switching and STP

## IPv4 addressing and subnet masks

IPv4 addresses contain 32 bits, divided into four 8-bit octets. Each octet ranges from 0 to 255. The complete address space contains 2^32 addresses (4,294,967,296). A prefix length identifies the network bits; the remaining bits identify addresses within that subnet.

For 192.168.1.10/24, the mask is 255.255.255.0, the network is 192.168.1.0, and the broadcast address is 192.168.1.255. This conventional subnet has 254 usable host addresses. The usual 2^host_bits - 2 rule has exceptions: /31 point-to-point links and /32 host routes.

Historical address classes are not a substitute for CIDR prefix lengths. The private ranges are 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16; these must not be confused with historical Class A/B/C boundaries.

## Loopback, TTL and link-local addresses

The 127.0.0.0/8 block is reserved for loopback; 127.0.0.1 is the usual local test address. A successful loopback ping checks the local network stack, not the physical NIC or cable.

IPv4 TTL is an 8-bit field decremented during forwarding. It prevents packets circulating indefinitely. A ping output such as `56(84) bytes` describes packet sizes, not a maximum hop count. `ttl=64` is the received TTL in that response; initial TTL values vary.

IPv4 link-local addressing uses 169.254.0.0/16, subject to address-selection rules. APIPA means Automatic Private IP Addressing. Such an address can appear when a host cannot obtain DHCP configuration; it is not the DHCP server's address.

## Ethernet and MAC learning

A conventional Ethernet MAC address has 48 bits, displayed as six hexadecimal byte pairs. A switch learns the source MAC address and ingress port within the VLAN. It forwards known unicast frames toward the destination MAC's learned port and floods unknown unicast within that VLAN, subject to forwarding state and policy. Layer-2 forwarding does not look up the destination IP address.

The broadcast destination is FF:FF:FF:FF:FF:FF. Multicast forwarding can be constrained using group membership mechanisms such as IGMP snooping; a multicast frame does not necessarily reach only interested hosts on an unconfigured switch.

An untagged Ethernet frame normally spans 64–1518 bytes from destination MAC through FCS. Preamble and SFD are outside that count, and a VLAN tag adds four bytes. These overheads matter when estimating packet rate and wire time.

## Spanning Tree Protocol

STP prevents Layer-2 forwarding loops while retaining redundant physical paths. The lowest bridge ID wins the root election. Compare priority (including the extended system ID where applicable) before the MAC address. The base default priority is 32768; in PVST-style VLAN 1 output, 32769 includes the VLAN ID.

A non-root switch selects a root port using the best received information: root ID, total root-path cost, sender bridge ID and sender port ID, with local port ID as the final tie-break when needed. Cost is not a fixed hop count: 19 is a commonly encountered legacy 100-Mbit/s port cost, not a universal value.

Designated ports forward for their segments. During stable operation, root-bridge ports on normal active segments are designated. RSTP improves convergence using defined port roles and state transitions.

```text
show spanning-tree
show spanning-tree vlan 1
show etherchannel summary
```

Read root ID, local bridge ID, role, state and path cost together. A lower-priority switch can become root even if another switch has a lower MAC address.

## Link aggregation and network hierarchy

LACP negotiates link aggregation; Cisco PAgP is a separate protocol. EtherChannel is Cisco terminology for a logical bundle. Individual flows are generally assigned to members by a hash, so one flow does not automatically gain the sum of all link bandwidths. A member failure can change flow placement and affect latency.

Access connects endpoints, distribution commonly aggregates access and applies routing or policy, and core provides resilient transport. These are design roles rather than absolute restrictions on OSI layers. SPOF means single point of failure.

## Sources and original notes

- [Cisco STP configuration guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/stp/stp-configuration-guide/m-stp.html)
- [Original CCNP class notes](../01_networking/03_class_notes/ccnp_d1.md)
- [Original switching notes](../01_networking/MyNotes/Day1.md)

This article consolidates the rough notes and corrects identifiable factual mistakes. It does not certify the rest of the repository.

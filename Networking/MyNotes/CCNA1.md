# CCNA fundamentals — quick refresher

## Devices and communication
- A switch forwards Ethernet frames using destination MAC addresses within a VLAN.
- A router forwards IP packets between networks using a routing table.
- A firewall enforces traffic policy; capabilities depend on the platform.
- Simplex means one-way communication. Half duplex alternates sending and receiving. Full duplex supports both simultaneously.
- Hostname, MAC address and IP address identify different things; they are not interchangeable.

## Networks, media and topology
- LAN covers a local network; WAN connects geographically separated networks; MAN is metropolitan in scope.
- Guided media includes twisted pair, coaxial cable and fibre. Wireless uses radio or other unguided signals.
- UTP means unshielded twisted pair; STP can mean shielded twisted pair in cabling, or Spanning Tree Protocol in switching.
- Typical copper Ethernet channels support up to 100 m for common twisted-pair standards. Actual speed and reach depend on the Ethernet standard and cable.
- Multimode fibre generally serves shorter links; single-mode supports longer reach. Match the optic, fibre, wavelength and distance.
- Star connects endpoints to a central device. Full mesh connects every pair. Ring connects neighbours in a loop. Bus shares a common medium.

## IPv4 and special ranges
IPv4 has four 8-bit octets: 32 bits total, approximately 4.3 billion addresses. Prefix length determines the network boundary.

| Address or prefix | Meaning |
| --- | --- |
| 10.0.0.0/8 | Private use |
| 172.16.0.0/12 | Private use: 172.16 through 172.31 |
| 192.168.0.0/16 | Private use |
| 127.0.0.0/8 | Loopback |
| 169.254.0.0/16 | IPv4 link-local |
| 0.0.0.0/0 | Default route matching all IPv4 destinations |
| 0.0.0.0 | Unspecified address; meaning depends on context |
| 255.255.255.255 | Limited broadcast |

For 172.1.1.0/24, the mask is 255.255.255.0. It is not in the private 172.16.0.0/12 range.

Historical classes: A used /8, B /16 and C /24 defaults; modern routing uses CIDR. Class D is multicast (224–239 first octet); Class E is reserved (240–255, with special-address exceptions).

Do not decide whether two hosts share a subnet without their masks. At /16, 128.10.5.9 and 128.11.5.10 are different subnets; at /8 they share a prefix.

## Ethernet and switching
Frame layout: destination MAC → source MAC → EtherType/length → payload → FCS. Preamble and SFD precede the frame. EtherType 0x0800 identifies IPv4.

ARP resolves an IPv4 next-hop address to a link-layer address on a local network. Ordinary Layer-2 switching uses MAC addresses, not destination IP lookups. Ethernet and Wi-Fi include both physical and data-link functions.

Circuit switching reserves resources for a circuit. Packet switching sends packets through a network. Message switching stores and forwards whole messages; it is distinct from Ethernet forwarding methods.

## Fault clues
| Symptom | Check first |
| --- | --- |
| Link down | Cable, optic, peer port and administrative state |
| CRC/input errors | Physical quality, optics and link configuration |
| Collisions | Half-duplex/shared media or duplex mismatch |
| Runts | Undersized frames; check physical faults and counters |
| Giants | Oversized frames relative to platform configuration |
| Output drops | Egress congestion, queue pressure and shaping |

Use `show interfaces status` and `show interfaces` on supported Cisco platforms. Interpret counter changes over time, not just lifetime totals. Autonegotiation requirements vary by link standard.

## Routing protocols
- BGP exchanges routing information between autonomous systems and within an AS using iBGP.
- OSPF is a link-state interior gateway protocol.
- PIM builds multicast forwarding distribution trees.
- BFD detects forwarding-path failures quickly; it does not calculate routes.

Reference: [IANA special-purpose IPv4 registry](https://www.iana.org/assignments/iana-ipv4-special-registry).

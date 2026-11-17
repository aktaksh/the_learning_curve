# Module 1 — Network Infrastructure and Connectivity

> **Exam weight:** 25%  
> **Method:** Diagnose first, then configure. A correct answer should identify the failing layer and cite evidence.

## Contents

- [A troubleshooting model](#a-troubleshooting-model)
- [Ethernet and physical media](#ethernet-and-physical-media)
- [Interface diagnosis](#interface-diagnosis)
- [Virtualisation and containers](#virtualisation-and-containers)
- [IPv4 addressing and subnetting](#ipv4-addressing-and-subnetting)
- [IPv6 addressing](#ipv6-addressing)
- [Wireless principles](#wireless-principles)
- [Client troubleshooting](#client-troubleshooting)
- [DHCPv4](#dhcpv4)
- [Low-latency perspective](#low-latency-perspective)

## A Troubleshooting Model

Use the same order every time:

1. **Scope:** one host, one VLAN, one site or everyone?
2. **Physical:** power, cable, optics, interface state and error counters.
3. **Layer 2:** VLAN, trunk, MAC learning, STP and EtherChannel.
4. **Layer 3:** address, mask/prefix, gateway, ARP/ND and route.
5. **Services:** DHCP, DNS, NAT, ACL and authentication.
6. **Application:** port, process, certificate and server response.
7. **Change:** what changed, when and by whom?

🟥 Do not begin with DNS when the interface is down. Do not change configuration until the evidence identifies a likely fault.

## Ethernet and Physical Media

### Ethernet Frame

An Ethernet frame contains a destination MAC, source MAC, EtherType/length, payload and frame check sequence. Switches forward primarily by destination MAC. The FCS detects corruption; it does not repair it.

| Field | Purpose |
|---|---|
| Preamble/SFD | Receiver synchronisation and frame start |
| Destination MAC | Intended Layer 2 destination |
| Source MAC | Sender's Layer 2 address |
| Optional 802.1Q tag | VLAN ID and priority information |
| EtherType | Upper-layer protocol such as IPv4 or IPv6 |
| Payload | Encapsulated packet |
| FCS | CRC-based corruption detection |

The normal Ethernet MTU is 1500 bytes. A larger Layer 2 frame can carry a VLAN tag and other overhead. Jumbo frames are not a single universal size; every hop must support the chosen MTU.

### Copper

- UTP is common; STP adds shielding where interference is a concern.
- Category rating, distance and transceiver capability constrain speed.
- Typical twisted-pair Ethernet segment maximum is 100 metres.
- Auto-MDIX usually removes the practical need to choose crossover cables, but pinout remains exam-relevant.
- Autonegotiation should normally be enabled at both ends.

### Fibre

| Property | Multimode | Single-mode |
|---|---|---|
| Core | Wider | Narrower |
| Typical reach | Shorter | Longer |
| Common use | Building/data hall | Campus, metro, long reach |
| Optics | Usually lower cost | Usually higher reach/cost |

A link requires compatible wavelength, fibre type, connector, speed, reach and optic at both ends. Transmit on one side must reach receive on the other.

### Common Fault Signatures

| Symptom | Likely causes |
|---|---|
| `administratively down/down` | Interface shut down |
| `down/down` | Cable, optic, remote port, power or speed issue |
| `up/down` | Encapsulation, keepalive or Layer 2 issue |
| Increasing CRC/input errors | Corruption, cabling, optic or duplex problem |
| Collisions/late collisions | Duplex mismatch or legacy shared media |
| Runts | Frames below legal minimum, often collision-related |
| Giants | Frames above accepted size/MTU |
| Output drops | Egress congestion or queue exhaustion |
| Flapping | Intermittent cable/optic, power or negotiation problem |

## Interface Diagnosis

```ios
show interfaces status
show interfaces GigabitEthernet1/0/10
show ip interface brief
show interfaces counters errors
show logging
```

Read `show interfaces` systematically:

1. Administrative and protocol state.
2. Configured/negotiated speed and duplex.
3. Last input/output and reset history.
4. Input errors, CRC, frame, overrun and ignored counters.
5. Output errors, collisions and interface resets.
6. Queue drops and traffic rates.

Use two snapshots separated by a known interval. A large historical counter is less useful than a counter actively increasing during the incident.

### Duplex Mismatch

One side full duplex and the other half duplex commonly produces poor throughput, late collisions on the half-duplex side and CRC/input errors on the full-duplex side. Ping may still work, which is why reachability alone does not prove health.

### Optical Power

Where supported, inspect digital optical monitoring data. Compare receive power with the optic's acceptable range. Too little power may indicate excessive loss, dirty connectors, wrong fibre or distance. Excessive power can also be harmful on short links with long-reach optics.

## Virtualisation and Containers

### Hypervisors

- **Type 1:** runs directly on hardware; common in data centres.
- **Type 2:** runs over a host operating system; common for desktop labs.

A VM has virtual CPU, memory, storage and one or more virtual NICs. A virtual switch can connect VMs internally and uplink them to a physical network. VLAN tags may be handled by the guest, virtual switch or physical switch depending on design.

### Containers

Containers share the host kernel and isolate processes using operating-system mechanisms. They usually start faster and consume fewer resources than VMs. A container image packages application files and dependencies, not a complete independent kernel.

| Topic | VM | Container |
|---|---|---|
| Kernel | Normally its own guest kernel | Shares host kernel |
| Isolation | Stronger boundary | Process/namespace boundary |
| Startup | Slower | Faster |
| Footprint | Larger | Smaller |
| Network | vNIC through virtual switch | Namespace/veth/bridge or plugin |

🟥 A container is not simply a lightweight VM. The shared-kernel model is the key distinction.

## IPv4 Addressing and Subnetting

### Address Roles

- **Network address:** all host bits zero.
- **Broadcast address:** all host bits one.
- **Usable hosts:** values between network and broadcast for conventional subnets.
- **Default gateway:** router address used for off-subnet destinations.

Private ranges:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

Other important ranges:

- `127.0.0.0/8`: loopback.
- `169.254.0.0/16`: IPv4 link-local/APIPA.
- `224.0.0.0/4`: multicast.
- `255.255.255.255`: limited broadcast.

### Subnetting Method

For prefix `/p`:

- Host bits = `32 - p`.
- Addresses per subnet = `2^(32-p)`.
- Conventional usable hosts = addresses minus 2.
- Block size in the interesting octet = `256 - mask value`.

Example: `172.16.37.141/27`

1. `/27` mask is `255.255.255.224`.
2. Block size is `32`.
3. Fourth-octet ranges begin 0, 32, 64, 96, 128, 160...
4. `141` lies in `128–159`.
5. Network: `172.16.37.128`.
6. Broadcast: `172.16.37.159`.
7. Usable: `172.16.37.129–158`.

### Prefix Table

| Prefix | Mask | Addresses | Conventional usable |
|---:|---|---:|---:|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |
| /31 | 255.255.255.254 | 2 | Point-to-point use |
| /32 | 255.255.255.255 | 1 | Host route |

### Troubleshooting IPv4

```ios
show ip interface brief
show interfaces
show arp
show ip route
ping 192.0.2.1
traceroute 198.51.100.10
```

Check whether source and destination agree about the subnet. A wrong mask can cause one host to ARP for a remote destination while the other sends traffic through its gateway, producing asymmetric failure.

## IPv6 Addressing

IPv6 addresses are 128 bits. Leading zeros inside a hextet may be omitted, and one continuous run of zero hextets may be compressed with `::` once.

| Type | Typical prefix/example | Purpose |
|---|---|---|
| Global unicast | `2000::/3` | Routable unicast |
| Link-local | `fe80::/10` | Same-link communication |
| Unique local | `fc00::/7` | Private-like internal use |
| Multicast | `ff00::/8` | One-to-many groups |
| Loopback | `::1/128` | Local host |
| Unspecified | `::/128` | No assigned source |

IPv6 has no broadcast. Neighbor Discovery uses ICMPv6 multicast and replaces many ARP-like functions.

### Modified EUI-64

To derive a 64-bit interface ID from a 48-bit MAC:

1. Split the MAC in half.
2. Insert `FFFE` in the middle.
3. Flip the universal/local bit in the first byte.

MAC `00:1C:42:AA:BB:CC` becomes interface ID `021C:42FF:FEAA:BBCC`.

### IOS Example

```ios
configure terminal
ipv6 unicast-routing
interface GigabitEthernet0/0
 ipv6 address 2001:db8:10::1/64
 ipv6 address fe80::1 link-local
 no shutdown
end

show ipv6 interface brief
show ipv6 neighbors
show ipv6 route
ping 2001:db8:10::2
```

## Wireless Principles

### Bands and Channels

- **2.4 GHz:** greater reach, fewer non-overlapping channels, more interference.
- **5 GHz:** more channels and capacity, shorter practical reach.
- **6 GHz:** additional clean spectrum for supported clients; shorter propagation and regulatory constraints apply.

Wider channels can provide more throughput but consume more spectrum and increase overlap risk. In a dense deployment, narrower channels can improve total system capacity.

### RF Concepts

- **RSSI:** received signal strength indicator.
- **Noise floor:** background RF energy.
- **SNR:** signal level relative to noise; often more useful than signal alone.
- **Attenuation:** signal weakens with distance and obstacles.
- **Reflection/multipath:** copies arrive by different paths.
- **Co-channel interference:** devices contend on the same channel.
- **Adjacent-channel interference:** overlapping channels interfere without coordinated contention.

### Security

- Avoid open and obsolete WEP networks.
- WPA2 commonly uses AES/CCMP.
- WPA3 improves modern authentication and protection.
- Personal mode uses a shared secret; enterprise mode normally uses 802.1X with a RADIUS-backed identity system.

## Client Troubleshooting

### Windows

```powershell
ipconfig /all
ping 127.0.0.1
ping <default-gateway>
tracert <destination>
arp -a
route print
nslookup <name>
```

### Linux

```bash
ip link
ip address
ip route
ip neigh
ping -c 4 <default-gateway>
tracepath <destination>
dig <name>
ss -tulpn
```

### Decision Sequence

1. Is the interface enabled and linked/associated?
2. Is the address valid for the expected subnet?
3. Is the default gateway present and on-link?
4. Can the client reach its own gateway?
5. Does the gateway have a route onward?
6. Is the remote IP reachable?
7. Does name resolution return the correct address?
8. Is the application port reachable and the service listening?

## DHCPv4

### DORA

1. **Discover:** client broadcasts from UDP 68 to UDP 67.
2. **Offer:** server proposes an address and options.
3. **Request:** client requests the selected offer.
4. **Acknowledgment:** server confirms the lease.

### IOS Server

```ios
configure terminal
ip dhcp excluded-address 10.10.20.1 10.10.20.20
ip dhcp pool USERS
 network 10.10.20.0 255.255.255.0
 default-router 10.10.20.1
 dns-server 10.10.1.53
 domain-name example.test
 lease 7
end

show ip dhcp pool
show ip dhcp binding
show ip dhcp conflict
```

### Relay

Broadcasts do not cross routers. Configure the helper on the interface receiving client broadcasts:

```ios
interface Vlan20
 ip address 10.10.20.1 255.255.255.0
 ip helper-address 10.10.1.10
```

### DHCP Troubleshooting

- Confirm the client access VLAN.
- Confirm the SVI/router interface is up.
- Confirm the pool network and mask match the client subnet.
- Check exclusions and available addresses.
- Verify the relay address and route to/from the server.
- Check ACLs blocking UDP 67/68.
- Inspect bindings and conflicts.

## Low-Latency Perspective

🟪 A low-latency path starts with physical correctness. CRC errors, intermittent optics and speed mismatches cause retransmission, loss or feed gaps that no application tuning can fix.

🟪 Virtualisation adds scheduling, virtual-switch and shared-resource variability. SR-IOV or kernel bypass may reduce overhead, but they also change observability, security and operational complexity.

🟪 Use static, documented infrastructure addressing for critical systems. DHCP can remain useful for management or provisioning networks, but the design must eliminate unintended dependency from the trading hot path.

🟪 Large MTUs reduce packets per byte transferred, but a mismatched MTU causes black holes or fragmentation. Validate end to end; never assume that configuring one switch is sufficient.

## Module Checklist

- [ ] Diagnose interface and cable issues from output.
- [ ] Explain VM and container networking.
- [ ] Complete IPv4 subnet calculations under one minute each.
- [ ] Identify IPv6 address types and build modified EUI-64.
- [ ] Explain wireless channel/security/interference choices.
- [ ] Troubleshoot a client in a fixed layered order.
- [ ] Configure and troubleshoot IOS DHCP server and relay.


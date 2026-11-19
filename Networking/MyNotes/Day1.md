# Ethernet and MAC learning — quick refresher

## MAC representation
A conventional Ethernet MAC address is 48 bits, displayed as six hexadecimal byte pairs. One hex digit represents four bits.

```text
34:AB:CD:12:34:56
00110100 10101011 11001101 00010010 00110100 01010110
```

## Delivery types
- Unicast targets one destination.
- Broadcast uses FF:FF:FF:FF:FF:FF and is flooded within the VLAN, subject to forwarding state.
- Multicast targets a group. Without group-aware forwarding, a switch may flood it within the VLAN.

## Ethernet fields
| Field | Bytes | Purpose |
| --- | --- | --- |
| Preamble + SFD | 7 + 1 | Synchronisation and frame start |
| Destination MAC | 6 | Destination |
| Source MAC | 6 | Sender |
| EtherType/length | 2 | Protocol or payload length |
| Payload + padding | Typically 46–1500 | Encapsulated data |
| FCS | 4 | CRC error detection |

An untagged frame is normally 64–1518 bytes excluding preamble/SFD. An 802.1Q tag adds four bytes. FCS detects corruption; it does not correct it.

## How a switch learns
```text
Host A — port 1 — Switch — port 2 — Host B
A sends: learn MAC A → port 1 in the VLAN.
B replies: learn MAC B → port 2 in the VLAN.
```

The switch learns from source MACs, then looks up destination MACs. Known unicast goes to the learned forwarding port; unknown unicast floods eligible ports in the VLAN except the ingress port. Entries age out and can move when topology changes.

## Checks
```text
show mac address-table
show interfaces
show vlan brief
```

Check VLAN membership, port state and MAC movement before assuming an IP routing problem.

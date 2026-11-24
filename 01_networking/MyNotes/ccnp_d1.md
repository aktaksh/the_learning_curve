# CCNP class 1 — addressing and spanning tree refresher

## IPv4 essentials
IPv4 has 32 bits split into four 8-bit octets. Each octet holds 0–255; the complete space has 2^32 addresses.

- /16 leaves 16 host bits: 65,536 addresses, normally 65,534 usable hosts.
- Conventional subnet usable-host counts exclude network and broadcast; /31 and /32 have special uses.
- Private ranges: 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16.
- Historical classes and private ranges are different concepts. Modern routing uses CIDR.

## Loopback, TTL and APIPA
127.0.0.0/8 is loopback. Pinging it tests the local stack, not the NIC or cable. IPv4 TTL is an 8-bit field decremented by routers to prevent indefinite loops.

In ping output, 56(84) bytes describes sizes, not hops. ttl=64 is the received TTL value.

APIPA means Automatic Private IP Addressing and uses IPv4 link-local addresses from 169.254.0.0/16, subject to selection rules. A link-local address can indicate DHCP failure; it is not the DHCP server address.

## OSI and campus roles
OSI layers: Application → Presentation → Session → Transport → Network → Data Link → Physical.

Access connects endpoints; distribution aggregates access and often applies routing/policy; core provides resilient transport. These are design roles, not absolute OSI-layer restrictions.

## STP election and port roles
STP prevents Layer-2 loops while retaining physical redundancy.

1. Lowest bridge ID wins the root election: priority/system ID before MAC.
2. Non-root switches select a root port using the best path information.
3. Each segment selects a designated port; redundant paths become non-forwarding as required.

Base priority defaults to 32768. PVST-style VLAN 1 can display 32769 because the extended system ID includes the VLAN number. The MAC address breaks a bridge-ID tie after priority.

Root-port comparison uses root ID, total root-path cost, sender bridge ID and sender port ID, with local port ID as the final tie-break when necessary. A cost of 19 is a legacy 100-Mbit/s example, not 19 hops.

Root-bridge ports on normal active segments are designated. RSTP provides faster convergence with defined roles and state transitions.

## EtherChannel and checks
LACP negotiates aggregation; PAgP is a distinct Cisco protocol. EtherChannel bundles compatible links logically. One flow generally follows one member selected by hashing, rather than using all members at once.

```text
show spanning-tree
show spanning-tree vlan 1
show etherchannel summary
```

Check root ID, bridge ID, cost, role and state. In a four-switch square lab, choose an intended root and confirm which redundant port stops forwarding. Configuration changes can reconverge the network.

SPOF means single point of failure. A redundant cable without loop prevention can create a broadcast storm.

Reference: [Cisco STP guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/stp/stp-configuration-guide/m-stp.html).

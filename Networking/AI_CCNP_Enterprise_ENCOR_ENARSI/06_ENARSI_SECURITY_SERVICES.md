# ENARSI 3 — Security and infrastructure services

## Contents

- [Infrastructure security](#infrastructure-security)
- [Management and telemetry](#management-and-telemetry)
- [DHCP and address delivery](#dhcp-and-address-delivery)
- [IP SLA, tracking and NetFlow](#ip-sla-tracking-and-netflow)
- [Assurance workflow](#assurance-workflow)

## Infrastructure security

**AAA fault isolation:** confirm line method list, server reachability/source interface, shared key, user authorization and local fallback. An SSH TCP connection can open while login fails; distinguish transport from authentication and privilege authorization. Retain console access when testing.

**ACLs:** inspect direction, sequence, counters and implicit deny. For IPv6 traffic filters, remember ND/ICMPv6 is essential to normal operation; a broad ICMPv6 deny can break address discovery. Time-based ACLs depend on a correct clock.

**uRPF:** checks whether the route back to a packet's source uses the expected ingress interface (strict mode) or exists at all (loose mode). Strict uRPF may drop legitimate traffic on asymmetric paths. Check FIB, VRF context and interface mode before applying.

**CoPP:** match traffic to the router's CPU. Monitor drops by class. If OSPF peers flap during a CoPP rollout but transit flows initially continue, inspect routing-control classes before touching interface MTU or process IDs.

**IPv6 first hop protections:** RA Guard, DHCPv6 Guard, ND inspection/snooping, binding tables and source guard mitigate rogue router/address claims. Security features need a correct trust boundary and allowance for static devices.

```text
Packet to router CPU → CoPP → routing/management process
Transit packet → FIB/adjacency → forwarding ASIC → egress
```

## Management and telemetry

Check console/VTY settings, SSH key and version, management VRF, AAA, ACL and route to management station. SCP requires SSH reachability and suitable permissions; TFTP/FTP are less secure and may be limited by policy.

**SNMPv2c** community strings offer weak security; **SNMPv3** supports authentication/privacy. A polling gap can hide a transient failure. Syslog analysis requires source, facility/severity, trustworthy time and device identity. Debug can be costly; use conditional filters and stop it after the investigation.

```ios
show logging
show clock detail
show snmp user
show snmp host
show users
show line
show ip ssh
undebug all
```

Telemetry adds streaming or subscribed operational data where supported. Cisco's minor update notes include telemetry in logging troubleshooting and IPFIX in NetFlow coverage; check current blueprint before exam booking.

## DHCP and address delivery

Diagnose IPv4 DORA and IPv6 address delivery separately. DHCPv4 relay is on the client-facing Layer 3 interface. DHCPv6 can provide addresses or other options, while IPv6 router advertisements supply default-router information; DHCPv6 alone does not normally hand out the default gateway.

```ios
show ip dhcp binding
show ip dhcp pool
show ipv6 dhcp binding
show ipv6 interface GigabitEthernet0/1
show ip interface GigabitEthernet0/1
```

Troubleshooting order: access VLAN → SVI/address → relay destination → server pool/options → route back to relay → ACL/first-hop security → lease/packet capture.

## IP SLA, tracking and NetFlow

IP SLA probes delay, jitter or reachability from a chosen source toward a chosen destination. A track object can change a route/FHRP policy when probe status changes. Verify reachability threshold and probe interval against failure-detection goals; a too-sensitive probe can flap a path.

```ios
show ip sla statistics
show track
show ip route
```

NetFlow v5/v9, Flexible NetFlow and IPFIX export flow records. Diagnose exporter reachability, source interface, record fields, monitor attachment/direction, sampling, cache and collector parsing. An empty collector does not prove no traffic; it may mean no exporter packets or no matching monitor.

```ios
show flow monitor
show flow monitor FLOW_MON cache
show flow exporter
show interfaces
```

For a microburst, flow records can identify high-volume conversations but typically cannot prove sub-millisecond queue behaviour by themselves. Use interface queue drops and high-resolution capture/telemetry.

## Assurance workflow

```text
Client complaint → scope and timestamps → management path independent?
→ physical counters → route/VRF → policy/ACL/uRPF → service (DHCP/DNS/AAA)
→ flow/capture → one discriminating test → controlled repair → post-check
```

🟪 **ULL:** Separate feed loss, clock drift and order-entry delay as distinct symptoms. Align device clocks before correlating events and preserve A/B path identity in every metric.

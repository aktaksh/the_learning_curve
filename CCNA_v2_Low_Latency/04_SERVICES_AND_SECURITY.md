# Module 4 — Network Services and Security

> **Exam weight:** 20%  
> **Principle:** Security controls must be verifiable, least-privileged and recoverable. A control that breaks required traffic is still an operational failure.

## Secure IOS Management

### Local Identity and SSH

```ios
configure terminal
hostname R1
ip domain name lab.example
username netadmin privilege 15 secret <strong-secret>
enable secret <strong-enable-secret>
crypto key generate rsa modulus 2048
ip ssh version 2
line console 0
 login local
 exec-timeout 10 0
line vty 0 4
 transport input ssh
 login local
 exec-timeout 10 0
end
```

Use secrets/hashes supported by the platform; do not rely on reversible password obfuscation. Restrict management reachability with an ACL and use an out-of-band network where possible.

```ios
ip access-list standard MGMT-SOURCES
 permit 10.99.0.0 0.0.0.255
 deny any log
line vty 0 4
 access-class MGMT-SOURCES in
```

## AAA, TACACS+ and RADIUS

AAA means:

- **Authentication:** Who are you?
- **Authorization:** What may you do?
- **Accounting:** What did you do?

| Property | TACACS+ | RADIUS |
|---|---|---|
| Common transport | TCP 49 | UDP 1812/1813 |
| Encryption | Encrypts more of packet body | Primarily protects password field |
| AAA separation | Strong separation | Authentication/authorization commonly combined |
| Typical use | Network-device administration | Network access, VPN, 802.1X |

Illustrative IOS XE configuration:

```ios
aaa new-model
radius server RAD1
 address ipv4 10.99.0.20 auth-port 1812 acct-port 1813
 key <shared-secret>
aaa group server radius RAD-GROUP
 server name RAD1
aaa authentication login default group RAD-GROUP local
aaa authorization exec default group RAD-GROUP local
aaa accounting exec default start-stop group RAD-GROUP
```

The `local` fallback is an operational safety measure. Test AAA in a separate session and retain console access before closing the working session.

```ios
show aaa servers
show radius statistics
test aaa group radius <user> <password> legacy
show logging
```

## Secure File Transfer

SCP and SFTP protect credentials and transferred data, unlike TFTP and plain FTP.

```ios
copy running-config scp:
copy scp: running-config
copy flash: scp:
copy sftp: flash:
dir flash:
verify /md5 flash:<image-name>
```

Operational workflow:

1. Verify free storage.
2. Back up running and startup configuration.
3. Transfer over an authenticated encrypted channel.
4. Validate checksum/hash.
5. Confirm boot variables and platform compatibility.
6. Maintain rollback and console access.

## NAT and PAT

### Terminology

- **Inside local:** inside host address as seen internally.
- **Inside global:** translated inside host address as seen externally.
- **Outside global:** external host address as seen globally.
- **Outside local:** external host address as represented internally.

### Static NAT

```ios
interface GigabitEthernet0/0
 description INSIDE
 ip address 10.10.10.1 255.255.255.0
 ip nat inside
interface GigabitEthernet0/1
 description OUTSIDE
 ip address 198.51.100.2 255.255.255.252
 ip nat outside
ip nat inside source static 10.10.10.10 203.0.113.10
```

### PAT Overload

```ios
access-list 10 permit 10.10.0.0 0.0.255.255
ip nat inside source list 10 interface GigabitEthernet0/1 overload
```

PAT distinguishes flows using transport-layer information so many inside hosts can share one public address.

### Verification

```ios
show ip nat translations
show ip nat statistics
clear ip nat translation *
show access-lists 10
```

Troubleshoot:

1. Correct inside/outside interface roles.
2. Correct translation rule and ACL match.
3. Route to outside destination.
4. Return route toward the inside global address.
5. Translation creation and counters.
6. ACL/firewall restrictions.

🟥 A NAT classification ACL identifies traffic; it is not applied to an interface as a filtering ACL unless separately configured.

## DNS

| Record | Purpose | Example |
|---|---|---|
| A | Name to IPv4 address | `app → 192.0.2.20` |
| AAAA | Name to IPv6 address | `app → 2001:db8::20` |
| CNAME | Alias to canonical name | `www → app.example` |
| MX | Mail exchanger for domain | priority plus mail host |
| NS | Authoritative name server | `ns1.example` |
| PTR | Address to name | reverse zone record |

Diagnosis:

```bash
dig app.example A
dig app.example AAAA
dig example MX
dig example NS
dig -x 192.0.2.20
nslookup app.example
```

Determine whether failure is:

- Client resolver configuration.
- Reachability to the resolver.
- Recursive resolution failure.
- Missing/wrong authoritative record.
- Stale cache/TTL.
- Split-horizon view mismatch.
- Application using an unexpected address family.

🟥 A successful ping by IP with failure by name suggests DNS, but not every application failure is DNS. Check returned records and service port.

## IPsec VPN Concepts

IPsec provides combinations of confidentiality, integrity, origin authentication and anti-replay protection.

- **Remote-access VPN:** an individual client securely connects to an organisation.
- **Site-to-site VPN:** gateways connect networks over an untrusted transport.
- **Transport mode:** protects the IP payload; original IP header remains.
- **Tunnel mode:** protects the entire original IP packet inside a new outer IP packet.

Key concepts:

- IKE negotiates peers, authentication and security associations.
- ESP commonly provides encryption and integrity.
- Security associations are directional.
- Interesting traffic/policy selects what enters the tunnel.
- NAT traversal may encapsulate IPsec for passage through NAT.

At CCNA v2.0, describe protocols and modes; do not overinvest in vendor-specific advanced configuration unless needed for work.

## IPv4 Access Control Lists

ACL rules are processed top-down. The first match wins. An implicit `deny any` exists at the end.

### Wildcard Masks

A wildcard bit of 0 means “must match”; 1 means “ignore.” Subtract a subnet mask from `255.255.255.255`.

| Subnet mask | Wildcard |
|---|---|
| 255.255.255.0 | 0.0.0.255 |
| 255.255.255.192 | 0.0.0.63 |
| 255.255.255.252 | 0.0.0.3 |

### Standard ACL

Matches source IPv4 address only. Place close to destination where practical because it cannot distinguish applications/destinations.

```ios
ip access-list standard BRANCH-USERS
 permit 10.20.0.0 0.0.255.255
 deny any log
interface GigabitEthernet0/1
 ip access-group BRANCH-USERS out
```

### Extended ACL

Matches protocol, source, destination and ports. Place close to source where practical.

```ios
ip access-list extended APP-POLICY
 permit tcp 10.20.0.0 0.0.255.255 host 10.50.0.10 eq 443
 permit udp 10.20.0.0 0.0.255.255 host 10.1.0.53 eq 53
 permit tcp 10.20.0.0 0.0.255.255 host 10.1.0.53 eq 53
 deny ip any any log
interface GigabitEthernet0/0
 ip access-group APP-POLICY in
```

DNS may use UDP or TCP 53. Return traffic must also be permitted according to ACL placement and topology.

### Numbered and Named Forms

```ios
access-list 10 permit 192.168.10.0 0.0.0.255
access-list 110 permit tcp 192.168.10.0 0.0.0.255 host 10.10.10.10 eq 443
```

Named ACLs are easier to understand and edit. Sequence numbers support controlled insertion/removal.

```ios
show access-lists
show ip interface
show running-config | section access-list
```

### ACL Change Safety

1. Document desired flows.
2. Model source, destination, protocol and direction.
3. Add explicit required permits before deny rules.
4. Apply during a controlled window where risk warrants.
5. Verify counters and actual application traffic.
6. Keep rollback access outside the affected path.

## Layer 2 Security

### DHCP Snooping

DHCP snooping classifies switchports as trusted or untrusted, filters rogue DHCP messages and builds a binding database.

```ios
ip dhcp snooping
ip dhcp snooping vlan 10,20
interface GigabitEthernet1/0/48
 ip dhcp snooping trust
interface range GigabitEthernet1/0/1-46
 ip dhcp snooping limit rate 15
```

Trust only ports leading toward legitimate DHCP servers/relays as required by topology—not all trunks automatically.

```ios
show ip dhcp snooping
show ip dhcp snooping binding
```

### Dynamic ARP Inspection

DAI validates ARP messages, commonly against DHCP snooping bindings, to reduce ARP spoofing.

```ios
ip arp inspection vlan 10,20
interface GigabitEthernet1/0/48
 ip arp inspection trust
```

Static-address devices require deliberate handling such as ARP ACLs or bindings according to platform/design. Enabling DAI without accounting for them can break service.

```ios
show ip arp inspection
show ip arp inspection statistics
```

### Storm Control

Storm control limits broadcast, multicast or unknown-unicast traffic crossing configured thresholds.

```ios
interface GigabitEthernet1/0/10
 storm-control broadcast level 1.00 0.50
 storm-control multicast level 2.00 1.00
 storm-control action shutdown
```

Threshold semantics and supported actions vary by platform. Set values from measured baselines, especially where multicast is legitimate.

### IPv6 RA Guard

RA Guard blocks unauthorised IPv6 Router Advertisements on host-facing ports, reducing rogue-router attacks.

```ios
ipv6 nd raguard policy HOST-PORT
 device-role host
interface GigabitEthernet1/0/10
 ipv6 nd raguard attach-policy HOST-PORT
```

Syntax varies by platform; understand the trust-boundary principle.

### Port Security

```ios
interface GigabitEthernet1/0/10
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

Violation modes:

- **Protect:** drop violating traffic with minimal notification.
- **Restrict:** drop and count/log violations.
- **Shutdown:** err-disable the port; common default.

```ios
show port-security
show port-security interface GigabitEthernet1/0/10
show errdisable recovery
```

## Defence-in-Depth Scenario

For a user access port:

1. Explicit access VLAN.
2. PortFast plus BPDU Guard.
3. DHCP snooping on the VLAN and rate limit.
4. DAI for ARP validation.
5. RA Guard for IPv6.
6. Port security if operationally suitable.
7. Storm control based on a measured baseline.
8. Central logs and monitoring.

No single feature replaces correct VLAN design, routing policy or endpoint security.

## Low-Latency Perspective

🟪 Security controls should not be casually removed to chase latency. Measure their actual impact and place them at appropriate boundaries.

🟪 NAT is commonly avoided in latency-sensitive exchange paths because it adds state and complexity, but it remains useful elsewhere. The operational risk is often more important than tiny average processing cost.

🟪 Storm control must be designed carefully for multicast market data. A threshold that is safe for ordinary users may drop valid feed bursts.

🟪 ACLs should be specific and counters monitored. Logging every high-rate denial can overload control-plane/logging systems.

🟪 Management, telemetry and file transfers should be separated from the trading hot path and rate-controlled where necessary.

## Module Checklist

- [ ] Secure IOS access with SSH and local fallback.
- [ ] Explain and configure a device as an AAA client.
- [ ] Compare TACACS+ and RADIUS.
- [ ] Use SCP/SFTP and verify files.
- [ ] Configure and troubleshoot NAT/PAT.
- [ ] Diagnose A, AAAA, CNAME, MX, NS and PTR issues.
- [ ] Describe remote-access/site-to-site IPsec and transport/tunnel mode.
- [ ] Configure standard/extended, named/numbered IPv4 ACLs.
- [ ] Configure and explain DHCP snooping, DAI, storm control, RA Guard and port security.


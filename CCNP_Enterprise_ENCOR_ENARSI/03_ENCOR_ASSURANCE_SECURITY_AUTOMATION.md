# ENCOR 3 — Assurance, security and automation

## Contents

- [Network assurance](#network-assurance)
- [Security](#security)
- [Automation](#automation)
- [Integrated workflow](#integrated-workflow)

## Network assurance

Start with a time window, affected scope and path. Use ping and traceroute with a relevant source address; validate with interface/routing counters and logs. A successful ping tests one packet type and size, not every application or MTU.

**SPAN** mirrors local traffic, **RSPAN** carries mirrored traffic over a VLAN to another switch, and **ERSPAN** uses an IP/GRE transport. Know source/destination, direction, oversubscription and timestamp limitations. A SPAN destination may drop mirrored frames when the source aggregate exceeds its bandwidth.

```ios
monitor session 1 source interface GigabitEthernet1/0/1 both
monitor session 1 destination interface GigabitEthernet1/0/24
show monitor session 1
```

**Flexible NetFlow** observes flows through a record (fields), monitor (record + exporter/cache) and exporter (collector). For traffic diagnosis, include source/destination, ports, protocol, interface and counters. Sampling may miss short or rare events.

```ios
show flow monitor
show flow exporter
show flow monitor TRAFFIC_MON cache
```

**IP SLA** generates synthetic probes (ICMP echo, jitter and others) and can drive tracking objects. A synthetic probe proves the chosen source, destination, method and interval. It cannot by itself prove that a separate market-data multicast flow has the same quality.

```ios
ip sla 10
 icmp-echo 198.51.100.2 source-interface GigabitEthernet0/0
 frequency 5
ip sla schedule 10 life forever start-time now
track 10 ip sla 10 reachability
show ip sla statistics
show track 10
```

**SNMP/syslog/debug:** SNMP reads counters and notifications; syslog records events with severity/facility; conditional debug limits scope but can still increase CPU. Synchronise time and use a short capture window. **Cisco DNA/Catalyst Center assurance** provides device/client health and path views; corroborate dashboard inference with device evidence.

**NETCONF** uses SSH and structured YANG data (commonly XML); **RESTCONF** uses HTTP(S) and YANG model resources. Know read vs change operations, authentication, transaction/error semantics and platform support. A `200` response means the API call succeeded, not that the resulting network intent is correct.

## Security

### Device access and AAA

Use local emergency access, SSH, AAA method lists and accounting. TACACS+ commonly supports device administration; RADIUS is common for network access. Validate central AAA from a second session and preserve console access.

```ios
aaa new-model
username breakglass privilege 15 secret <secret>
aaa authentication login default group tacacs+ local
line vty 0 4
 transport input ssh
 login authentication default
show aaa servers
```

### ACL and CoPP

ACL first-match processing and implicit deny still apply. Evaluate direction and match counters. **Control plane policing (CoPP)** protects traffic punted to the CPU, such as routing packets and management traffic. Classify control protocols carefully; an over-tight CoPP policy can kill OSPF/BGP neighbours while transit forwarding initially continues.

```text
Transit packet → ASIC forwarding
Packet to router CPU → CoPP classify/police → routing or management process
```

```ios
show policy-map control-plane
show access-lists
show logging
```

### Wireless and access security

802.1X uses supplicant, authenticator and authentication server; EAPOL is between client and access device. A WPA four-way handshake derives per-session keys after authentication. PSK shares a secret; WebAuth redirects for portal access. MAB may be a fallback for non-802.1X devices but grants access based on a spoofable MAC, so restrict its policy. TrustSec uses security group policy; MACsec encrypts a supported Ethernet link. Know threat defence, endpoint security and next-generation firewall roles at the “describe” level.

**REST API security:** protect tokens, use HTTPS, least privilege, expiration and audit. Do not paste credentials into logs or notebooks.

## Automation

Python basics: variables, lists, dictionaries, conditionals, loops, functions, exceptions and JSON parsing. Read a small script and predict its output before running it.

```python
import json
payload = '{"interfaces":[{"name":"Gi0/0","state":"up"}]}'
data = json.loads(payload)
for interface in data["interfaces"]:
    if interface["state"] != "up":
        print(interface["name"])
```

The output is empty because the only state is `up`. This course keeps runnable code as fenced examples inside Markdown, matching your Markdown-only preference.

**JSON** uses objects `{}`, arrays `[]`, quoted string keys and lowercase `true`, `false`, `null`. **YANG** models operational/configuration data. Cisco controller APIs and RESTCONF expose resources; interpret verbs, status codes and payload fields. Common HTTP results: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthenticated, 403 Forbidden, 404 Not Found, 409 Conflict, 500 Server Error.

**EEM** reacts to an event and performs an action. Keep applets small, observable and safe from self-triggering loops. Example:

```ios
event manager applet CAPTURE_LINK
 event syslog pattern "LINK-3-UPDOWN"
 action 1.0 cli command "enable"
 action 2.0 cli command "show interfaces summary"
```

**Ansible** generally uses agentless remote connections; Chef/Puppet traditionally have agent-oriented patterns; SaltStack supports several models. Compare how each stores desired state, connects, handles secrets and reports drift. Do not assume any tool makes a non-idempotent command safe.

## Integrated workflow

```text
Alert → exact timestamp and affected flow → device/route/interface evidence
      → hypothesis → read-only discriminating test → candidate change
      → canary → packet/metric post-check → close or rollback
```

🟪 **ULL:** A five-minute SNMP average can hide a 200-microsecond burst. Correlate precise time, switch queue/drop counters, NIC counters and packet capture. Record p50/p99/p99.9 rather than only mean latency.

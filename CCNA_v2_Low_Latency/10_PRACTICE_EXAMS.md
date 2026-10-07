# CCNA v2.0 Practice Exams

These are original study assessments. They do not reproduce live Cisco questions. Allow 60 minutes per 30-question exam. Select the best answer unless stated otherwise. Target **85%**.

## Practice Exam A

1. A port is `up/up`, but CRC errors increase. Which layer should be investigated first?  
   A. DNS · B. Physical/link · C. OSPF · D. NAT
2. What is the network for `172.20.9.77/28`?  
   A. `.64/28` · B. `.72/28` · C. `.76/28` · D. `.80/28`
3. Which IPv6 prefix is link-local?  
   A. `2000::/3` · B. `fc00::/7` · C. `fe80::/10` · D. `ff00::/8`
4. What is the main kernel difference between containers and VMs?  
   A. VMs cannot route · B. Containers normally share the host kernel · C. Containers require a guest kernel · D. VMs use no vNIC
5. A remote VLAN's DHCP clients fail while local clients work. Best first configuration check?  
   A. DNS MX · B. `ip helper-address` · C. STP priority · D. NAT overload
6. Which wireless measurement compares signal with noise?  
   A. SSID · B. RSSI alone · C. SNR · D. BSSID
7. Which command proves VLANs operationally traverse a trunk?  
   A. `show vlan brief` only · B. `show interfaces trunk` · C. `show ip route` · D. `show arp`
8. Which LACP pair forms a channel?  
   A. passive/passive · B. active/passive · C. on/passive · D. desirable/passive
9. An SVI is down/down although `no shutdown` is present. Most likely?  
   A. No active member in the VLAN · B. Wrong DNS · C. OSPF AD · D. PAT absent
10. Which feature shuts an edge port receiving a BPDU?  
    A. Root Guard · B. Loop Guard · C. BPDU Guard · D. Storm control
11. Root Guard is best used to:  
    A. Elect a downstream root · B. Prevent superior BPDUs changing root placement · C. Encrypt BPDUs · D. Bundle links
12. Why might a port-channel remain usable after one member fails?  
    A. STP creates bandwidth · B. Other bundled members forward · C. ARP repairs fibre · D. NAT replaces the link
13. Routes `/16` and `/24` match a packet. Which is chosen?  
    A. Lower AD regardless of prefix · B. `/16` · C. `/24` · D. First configured
14. What is a floating static route?  
    A. AD lower than connected · B. Higher-AD backup · C. Host route · D. Multicast route
15. OSPF neighbours on Ethernet are 2-Way with each other but Full with DR/BDR. Meaning?  
    A. Always an error · B. Normal DROTHER behaviour · C. MTU mismatch · D. Duplicate address
16. Which OSPF network type has no DR/BDR election?  
    A. Broadcast · B. Point-to-point · C. Multiaccess · D. VLAN
17. In HSRP, which role forwards for the virtual gateway?  
    A. Backup · B. Designated · C. Active · D. Root
18. Which protocol is commonly preferred for central network-device administration?  
    A. TACACS+ · B. ARP · C. LLDP · D. DHCP
19. PAT primarily distinguishes translations using:  
    A. VLAN names · B. Transport ports/flow information · C. DNS aliases · D. STP costs
20. Which DNS record maps a name to IPv6?  
    A. A · B. PTR · C. AAAA · D. MX
21. An ACL has no matching permit. What happens?  
    A. Implicit permit · B. Implicit deny · C. NAT · D. Route lookup is skipped
22. DAI most commonly validates ARP against:  
    A. OSPF database · B. DHCP-snooping bindings · C. DNS cache · D. LACP state
23. Which IPsec mode encapsulates the complete original IP packet?  
    A. Access · B. Transport · C. Tunnel · D. Passive
24. Which SNMP message is acknowledged?  
    A. Trap · B. Inform · C. GETNEXT · D. Community
25. Syslog severity 2 is:  
    A. Critical · B. Warning · C. Informational · D. Debugging
26. Which describes Ansible idempotency?  
    A. Every run changes config · B. Repeated runs converge without needless change · C. Devices require agents · D. It replaces routing
27. Safest first request to an AI assistant during an outage?  
    A. Reload all cores · B. Apply its first config · C. Rank hypotheses and provide read-only checks · D. Send all secrets
28. Five-minute utilisation is low but drops rise during bursts. Best inference?  
    A. No congestion is possible · B. Sampling may hide microbursts · C. DNS is slow · D. STP is disabled
29. Why can a surviving LACP bundle have higher latency after failure?  
    A. Reduced capacity can create queueing · B. VLAN IDs grow · C. MAC addresses expire instantly · D. IPv6 turns off
30. What proves incident recovery best?  
    A. Config saved · B. One ping · C. Original symptom gone plus counters/path/SLA stable · D. Ticket closed

### Exam A Answers

1 B—CRC is a physical/link symptom. 2 A—block size 16; 77 lies 64–79. 3 C—`fe80::/10`. 4 B—containers share the host kernel. 5 B—relay is required across routing. 6 C—SNR compares signal/noise. 7 B—shows trunk operational VLAN state. 8 B—at least one side active. 9 A—SVI autostate needs an active VLAN path. 10 C—BPDU Guard. 11 B—prevents unexpected root placement. 12 B—remaining members carry traffic. 13 C—longest prefix. 14 B—higher AD backup. 15 B—normal broadcast OSPF. 16 B—point-to-point. 17 C—active. 18 A—TACACS+. 19 B—ports/flow tuple. 20 C—AAAA. 21 B—implicit deny. 22 B—snooping database. 23 C—tunnel. 24 B—inform. 25 A—critical. 26 B—desired-state convergence. 27 C—bounded evidence-first assistance. 28 B—coarse averages hide bursts. 29 A—less capacity/changed hashing. 30 C—verify service and recurrence indicators.

## Practice Exam B

1. A switch interface shows `administratively down`. First action?  
   A. Add route · B. Check `shutdown` configuration · C. Clear DNS · D. Change STP root
2. How many conventional usable addresses in `/27`?  
   A. 14 · B. 30 · C. 32 · D. 62
3. An IPv6 address beginning `ff` is what type?  
   A. Link-local · B. Global · C. Multicast · D. Loopback
4. Client reaches gateway by IP but not a hostname. Best next check?  
   A. DNS query and resolver · B. Cable pinout · C. STP root · D. LACP mode
5. Which DHCP message does a new client send first?  
   A. ACK · B. Request · C. Discover · D. Offer
6. Which 2.4-GHz issue is common in dense networks?  
   A. Too many non-overlapping channels · B. Channel overlap/interference · C. No propagation · D. No security support
7. Unknown unicast is normally:  
   A. Routed by DNS · B. Flooded within VLAN except ingress · C. Always dropped · D. Sent only to root bridge
8. What is required for inter-VLAN routing on a multilayer switch?  
   A. `ip routing` and operational SVIs · B. BPDU filter · C. PAT · D. CNAME
9. Both LACP sides are passive. Result?  
   A. Bundle forms · B. No negotiation initiator · C. Static bundle · D. STP disabled
10. Which protocol is vendor-neutral for neighbor discovery?  
    A. CDP · B. LLDP · C. HSRP · D. TACACS+
11. Which Rapid STP port is the best path toward root on a non-root switch?  
    A. Designated · B. Root · C. Backup · D. Edge
12. Expected BPDU loss on a redundant link is addressed by:  
    A. Loop Guard · B. NAT · C. DHCP snooping · D. RA Guard
13. A route has `[110/30]`. What is 110?  
    A. Prefix · B. AD · C. VLAN · D. TCP port
14. Why can a configured static route be absent?  
    A. Next hop not resolvable · B. DNS TTL · C. SSID hidden · D. PortFast enabled
15. Which IPv6 next hop normally requires an exit interface in the route?  
    A. Global unicast · B. Link-local · C. Loopback · D. Multicast
16. OSPF neighbours stop at ExStart/Exchange. Common cause?  
    A. MTU mismatch · B. DNS CNAME · C. PAT port · D. Wireless SNR
17. OSPF DR election is:  
    A. Preemptive · B. Non-preemptive · C. Based on lowest priority · D. Used on point-to-point
18. VRRP forwarding role is called:  
    A. Active · B. Root · C. Master · D. Designated
19. Which secure copy method is suitable for IOS files?  
    A. TFTP only · B. SCP/SFTP · C. Telnet · D. CDP
20. A DNS PTR record provides:  
    A. Name-to-IPv4 · B. Address-to-name · C. Mail server · D. Name server authority
21. Standard ACL primarily matches:  
    A. Destination port · B. Source IPv4 · C. OSPF metric · D. VLAN name
22. Which ACL wildcard corresponds to `/26`?  
    A. `0.0.0.31` · B. `0.0.0.63` · C. `0.0.0.127` · D. `255.255.255.192`
23. Rogue DHCP mitigation?  
    A. DHCP snooping · B. Root Guard · C. OSPF · D. CNAME
24. Which feature blocks rogue IPv6 router advertisements?  
    A. DAI · B. RA Guard · C. PAT · D. LACP
25. Syslog `%LINK-3-UPDOWN`: what is `3`?  
    A. Facility · B. Severity · C. Interface · D. OID
26. SNMP object identifier abbreviation?  
    A. OID · B. SVI · C. BSSID · D. FHRP
27. Best way to protect secrets in an AI prompt?  
    A. Include everything · B. Minimise/redact classified data · C. Use debug output only · D. Disable AAA
28. Which management model stores reviewed desired state in version control?  
    A. Infrastructure as code · B. Manual cable map · C. ARP · D. APIPA
29. OSPF failover restores ping but latency SLA fails. Correct conclusion?  
    A. Network is fully healthy · B. Backup path has different performance · C. DNS must be wrong · D. IPv6 caused it
30. What is the strongest troubleshooting habit?  
    A. Random changes · B. Reload first · C. Form and discriminate hypotheses with evidence · D. Trust averages only

### Exam B Answers

1 B—administrative state. 2 B—32 addresses minus network/broadcast. 3 C—`ff00::/8` multicast. 4 A—IP works; validate name resolution. 5 C—Discover. 6 B—limited channels and interference. 7 B—unknown unicast flooding. 8 A—routing and live SVIs. 9 B—no active initiator. 10 B—LLDP. 11 B—root port. 12 A—Loop Guard. 13 B—AD. 14 A—recursive next hop must resolve. 15 B—link-local is link-scoped. 16 A—classic exchange problem. 17 B—non-preemptive. 18 C—master. 19 B—encrypted transfer. 20 B—reverse lookup. 21 B—source only. 22 B—255 minus 192 equals 63. 23 A—DHCP snooping. 24 B—RA Guard. 25 B—severity. 26 A—OID. 27 B—data minimisation. 28 A—IaC. 29 B—reachability is not SLA equivalence. 30 C—evidence-driven diagnosis.

## Remediation Rule

For every wrong answer:

1. Write the governing rule in one sentence.
2. Identify why each distractor is wrong.
3. Run or design one verification lab.
4. Re-answer after 48 hours without notes.


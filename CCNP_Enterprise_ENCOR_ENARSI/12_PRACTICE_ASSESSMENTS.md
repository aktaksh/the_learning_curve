# Original practice assessments

These are original study items, not Cisco exam questions. Work without notes. Suggested time: 30 minutes per set. The sets sample the blueprint; the question bank and labs cover the remaining detail.

## ENCOR set (20 questions)

1. A route exists in the RIB but the next-hop MAC is unresolved. Which table is most useful next? A. CAM only B. CEF adjacency C. BGP peers D. SNMP MIB
2. QoS policy buffers and spaces excess packets. Which action? A. Police B. Shape C. Drop D. Remark only
3. What makes two MST switches members of the same region? A. Same hostname B. Same region name/revision/VLAN map C. Same IP D. Same FHRP
4. A single TCP flow crosses an LACP bundle. Its traffic normally uses: A. all members per packet B. one hash-selected member C. root port D. only standby
5. GRE alone provides: A. encryption B. encapsulation C. AAA D. FEC
6. OSPF point-to-point links elect: A. DR/BDR B. only DR C. neither D. root bridge
7. For BGP `network 203.0.113.0 mask 255.255.255.0`, the local RIB needs: A. any /16 B. exact /24 C. default route D. only connected /32
8. An IGMPv3 receiver can request: A. only VLAN B. source and group C. BGP next hop D. TCP port
9. RPF checks the route toward: A. multicast receiver B. source C. DNS D. default gateway only
10. A PTP clock reports locked. What else should be checked for one-way measurements? A. PHC offset/asymmetry B. NAT pool C. VLAN name D. SSH key
11. Which mirror mechanism can send encapsulated copies across an IP network? A. SPAN B. RSPAN C. ERSPAN D. FHRP
12. What produces a Flexible NetFlow export destination? A. Record B. Exporter C. Monitor alone D. Adjacency
13. IP SLA plus track can influence: A. routing failover B. optical wavelength C. STP region D. MACsec key
14. CoPP governs packets sent to: A. router CPU B. all transit ASIC paths C. DHCP clients D. optical amplifier
15. An EAPOL exchange is between: A. two ASes B. supplicant and authenticator C. two MPLS P routers D. NHRP peers
16. What is valid JSON? A. `{'up': True}` B. `{"up": true}` C. `{up: true}` D. `{"up": True}`
17. HTTP 403 means: A. Created B. Not found C. Forbidden D. Server error
18. YANG defines: A. fibre attenuation B. network data models C. route metric D. switch ASIC
19. What is a risk of oversubscribed SPAN? A. More bandwidth B. Lost mirror packets C. Automatic encryption D. OSPF reset
20. Which route trace is complete? A. neighbour only B. protocol → RIB → FIB/adjacency → egress C. ping only D. syslog only

**Answers:** 1 B (forwarding rewrite unresolved); 2 B (shaping buffers); 3 B (region consistency); 4 B (flow hash); 5 B (GRE encapsulates); 6 C (no DR); 7 B (exact match); 8 B (source-specific membership); 9 B (toward source); 10 A (clock accuracy); 11 C (ERSPAN); 12 B (exporter); 13 A (tracked route); 14 A (control plane); 15 B (802.1X link exchange); 16 B (quoted key/lowercase boolean); 17 C; 18 B; 19 B; 20 B.

## ENARSI set (20 questions)

1. Two routes for identical `/24` prefixes are static AD 200 and OSPF AD 110. Which wins? A. static B. OSPF C. both always D. neither
2. EIGRP FD is 1000, neighbour RD is 1000. Is it a feasible successor? A. yes B. no C. only IPv6 D. if stub
3. A branch EIGRP stub mainly reduces: A. MTU B. query scope C. VLANs D. crypto
4. An OSPF NSSA can inject external routes as: A. Type 7 B. Type 1 only C. BGP only D. ARP
5. Which OSPF external type includes internal path cost to ASBR? A. E2 B. E1 C. L2 D. NSSA-only
6. A route tag prevents feedback only when: A. its policy matches and denies it B. it exists C. VLAN tagged D. CEF enabled
7. What BGP attribute is local to one Cisco router? A. local preference B. MED C. weight D. AS path
8. iBGP learned route is not normally passed to another iBGP peer. Which design helps scale? A. route reflector B. SPAN C. FHRP D. DAI
9. PBR is applied to: A. ingress interface B. only egress C. DNS server D. physical transceiver
10. VRF-Lite provides: A. per-VRF routing table B. MPLS encryption C. wireless roaming D. automatic NAT
11. BFD improves: A. failure detection B. optical power C. route summarization D. encryption
12. MPLS label switching alone gives: A. encryption B. forwarding using labels C. AAA D. end-user Wi-Fi
13. An RD primarily makes VPN prefixes: A. unique B. encrypted C. lower latency D. multicasted
14. An RT primarily decides: A. CPU speed B. VRF import/export membership C. STP root D. IP SLA rate
15. DMVPN NHRP maps: A. DNS to IP B. tunnel to NBMA addresses C. DSCP to queue D. ASN to BGP
16. Strict uRPF can fail with: A. symmetric traffic only B. asymmetric return routing C. correct ACL D. one VLAN
17. DHCPv6 client has address but no default gateway. Check: A. IPv6 RA B. SNMP trap C. BGP weight D. ESP label
18. Five-minute utilisation low, output drops high. Most likely missing evidence? A. microburst counters/timed capture B. CNAME C. EIGRP K values D. DHCP lease
19. OSPF route in LSDB but absent from RIB. What next? A. reload B. compare selected route and next hop C. change VLAN name D. disable CoPP blindly
20. IP SLA tracked route oscillates. Best next check? A. threshold/probe stability B. optical colour only C. LLDP only D. JSON schema

**Answers:** 1 B (lower AD, same prefix); 2 B (strict RD < FD); 3 B; 4 A; 5 B; 6 A; 7 C; 8 A; 9 A; 10 A; 11 A; 12 B; 13 A; 14 B; 15 B; 16 B; 17 A; 18 A; 19 B; 20 A.

## Review method

For each miss, write the rule, explain why each distractor is wrong, perform one related lab check, and retry after 48 hours. A high multiple-choice score without the ability to diagnose the same feature in a topology is not readiness.

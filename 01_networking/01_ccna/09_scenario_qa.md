# CCNA v2.0 Scenario-Based Q&A

For each scenario, state: **scope → evidence → hypotheses → next check → root cause → fix → verification**.

## 1. Interface Up, Performance Poor

**Scenario:** Ping succeeds, but file transfer is extremely slow. One switch side reports late collisions; the peer reports CRC errors.

**Answer:** Duplex mismatch is the leading cause. Verify speed/duplex on both ends, align autonegotiation or explicit settings, then confirm counters stop increasing and throughput recovers.

## 2. Fibre Link Down

**Scenario:** Both ports are enabled, but remain down. One side uses a multimode short-range optic and the other a single-mode long-range optic.

**Answer:** Media/optic incompatibility. Match supported speed, wavelength, fibre and reach; clean/inspect connectors, verify polarity and check optical levels.

## 3. Wrong IPv4 Mask

**Scenario:** Host A `10.1.1.10/24` reaches the gateway. Host B `10.1.2.20/16` intermittently fails to reach A through routing.

**Answer:** Host B treats `10.1.1.10` as on-link and ARPs instead of using its gateway. Correct B's prefix to the intended subnet and clear/relearn neighbor state.

## 4. DHCP Client Gets APIPA

**Scenario:** A Windows client receives `169.254.x.x`. Static-addressed clients in the VLAN work.

**Answer:** DHCP failed. Verify switchport VLAN, pool capacity, relay on the client gateway interface, routes to server and ACLs for UDP 67/68. Confirm DORA in a capture.

## 5. DHCP Works Locally, Not Remotely

**Scenario:** Clients on the DHCP server's VLAN obtain leases; remote VLANs do not.

**Answer:** Broadcasts do not cross routing boundaries. Configure/repair `ip helper-address` on each remote client SVI, then verify server return routes and pools.

## 6. IPv6 Neighbor But No Remote Reachability

**Scenario:** Two hosts see each other in the neighbor table but cannot reach a remote IPv6 prefix.

**Answer:** Same-link ND is working. Check default gateway/router advertisements, `ipv6 unicast-routing`, IPv6 routing table and return path.

## 7. VLAN Exists But Cross-Switch Hosts Fail

**Scenario:** VLAN 20 exists on both switches and access ports are correct. Hosts on different switches cannot communicate.

**Answer:** Inspect the trunk's operational allowed/forwarding VLAN list and STP. Add VLAN 20 to the trunk if omitted; verify MAC learning on both sides.

## 8. Native VLAN Mismatch

**Scenario:** Switch logs report native VLAN mismatch and untagged control traffic behaves unexpectedly.

**Answer:** Configure the same deliberate native VLAN on both ends and verify trunk mode/allowed list. Do not silence the warning without correcting the topology.

## 9. SVI Down

**Scenario:** `Vlan30` is configured and `no shutdown`, but line protocol is down.

**Answer:** Confirm VLAN 30 exists/active and at least one member access/trunk path is operational and forwarding. Then confirm platform autostate behaviour.

## 10. EtherChannel Suspended

**Scenario:** Two links should bundle; one is suspended. The port-channel is a trunk, but the member has a conflicting access setting.

**Answer:** Member consistency failure. Remove conflicting per-member configuration, align channel attributes and verify `show etherchannel summary`/LACP neighbour.

## 11. Passive/Passive LACP

**Scenario:** Both sides use `channel-group 1 mode passive`.

**Answer:** Neither initiates LACP. Change at least one side to active, then verify members show bundled.

## 12. Unexpected STP Root

**Scenario:** An access switch becomes root after a reboot sequence, increasing the path length.

**Answer:** Root placement was not explicitly controlled. Configure intended primary/secondary root priority and Root Guard on boundaries where superior BPDUs must not be accepted.

## 13. Edge Port Err-Disabled

**Scenario:** A user connects a small unmanaged switch; the access port with BPDU Guard becomes err-disabled.

**Answer:** Expected protection triggered by a BPDU. Remove the unauthorised switch, confirm policy, recover the port according to procedure and retain BPDU Guard.

## 14. Static Route Missing

**Scenario:** A configured route via `192.0.2.2` is absent from the table.

**Answer:** Check whether the next hop is recursively reachable and the outgoing interface is up. Correct the connected addressing/route or use a valid fully specified next hop.

## 15. Floating Route Always Preferred

**Scenario:** Backup static route is installed instead of OSPF.

**Answer:** Its AD is lower than OSPF's. Raise the floating static AD above the dynamic route's AD, then verify normal and failure states.

## 16. OSPF Stuck in Init

**Scenario:** R1 sees R2's hello but does not see itself listed by R2.

**Answer:** One-way communication. Investigate ACLs, multicast handling, interface/physical issues and R2's ability to receive/send hellos.

## 17. OSPF ExStart/Exchange Failure

**Scenario:** Neighbours repeatedly reach ExStart/Exchange but not Full.

**Answer:** Check MTU mismatch and duplicate router IDs after basic area/timer/network checks. Align MTU or fix the underlying interface design; verify Full state.

## 18. No Full Adjacency Between DROTHERs

**Scenario:** Two DROTHER routers on Ethernet remain 2-Way with each other but are Full with DR and BDR.

**Answer:** This is normal broadcast-network behaviour. Do not change configuration solely to make every pair Full.

## 19. FHRP Split-Brain

**Scenario:** Both gateways believe they are active/master.

**Answer:** Control messages are not crossing the VLAN. Check trunk/VLAN/STP/ACL connectivity, group and virtual IP. Restore shared-segment communication and verify a single forwarding role.

## 20. PAT Has No Translations

**Scenario:** Inside clients have a default route, but `show ip nat translations` remains empty.

**Answer:** Verify interfaces marked inside/outside and the NAT ACL matches source addresses. Generate traffic, inspect ACL/NAT counters and verify outside routing.

## 21. HTTPS ACL Still Breaks Application

**Scenario:** TCP 443 is permitted outbound, but clients cannot resolve the application name.

**Answer:** Required DNS was omitted. Permit approved DNS using UDP and TCP 53 as appropriate, verify queries and keep the application permit.

## 22. ACL Locks Out Administrator

**Scenario:** A VTY access-class was applied before the management subnet was permitted.

**Answer:** Use retained console/out-of-band access, correct the ACL, validate from a second session and adopt staged AAA/ACL changes with rollback.

## 23. DAI Breaks Static Server

**Scenario:** DHCP clients work after DAI is enabled, but a statically addressed server cannot communicate.

**Answer:** The server has no DHCP-snooping binding. Add an authorised static binding/ARP ACL or appropriate trusted design; do not disable DAI globally without analysis.

## 24. Rogue DHCP Server

**Scenario:** Clients receive the wrong gateway from a user-connected DHCP server.

**Answer:** Enable DHCP snooping on the VLAN, trust only legitimate server-facing paths and rate-limit untrusted access ports. Renew clients and inspect bindings.

## 25. Syslog Sequence Looks Impossible

**Scenario:** A route-down message appears earlier than the interface-down event on another device.

**Answer:** Check clock source, timezone and synchronisation before concluding causality. Correct NTP/time settings and compare timestamp precision.

## 26. AI Suggests Destructive Fix

**Scenario:** An assistant recommends clearing all routes and reloading the core switch based on one log line.

**Answer:** Reject the unsupported, high-blast-radius action. Ask for ranked hypotheses, missing evidence and read-only commands; validate platform/current state and use controlled change procedures.

## 27. SNMP Shows Low Utilisation but Drops Rise

**Scenario:** Five-minute utilisation averages are 15%, while output-drop counters increase during market open.

**Answer:** Short microbursts can exhaust queues between samples. Use higher-resolution telemetry/capture and queue counters; identify burst source and capacity/buffering/path options.

## 28. LACP Member Failure Changes Latency

**Scenario:** Connectivity survives one member failure, but order latency rises.

**Answer:** Remaining capacity/path hashing changed and may cause queueing. Compare member counters, flow placement and queue drops; validate failure-state latency as a design requirement.

## 29. OSPF Converges to Slower Path

**Scenario:** Primary link fails; routes reconverge, but application SLA fails.

**Answer:** Routing restored reachability, not equivalent performance. Measure backup path, adjust topology/cost only with design evidence and provision failure capacity.

## 30. Multicast Storm Control Drops Feed

**Scenario:** Market-data sequence gaps begin immediately after access-switch storm-control rollout.

**Answer:** Compare configured multicast threshold with actual burst rate and violation counters. Roll back safely, baseline legitimate bursts, redesign thresholds and validate in a canary.

## Troubleshooting Scoring Rubric

Score each response from 0–2:

- **Scope/evidence:** identifies affected layer and relevant output.
- **Reasoning:** distinguishes symptom from root cause.
- **Next check:** proposes a safe, discriminating test.
- **Fix:** minimal and technically correct.
- **Verification:** proves recovery and checks for recurrence.

Maximum per scenario: 10. Target: at least 8 without notes.


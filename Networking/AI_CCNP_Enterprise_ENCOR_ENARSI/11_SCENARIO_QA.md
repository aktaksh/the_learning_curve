# Scenario Q&A — diagnose the first broken step

Use the same answer pattern: **observed state → competing hypotheses → one discriminating check → cause → minimal fix → post-check**.

1. **OSPF neighbours Full; `10.40.0.0/16` is in LSDB but absent from RIB.**  
   Check `show ip route 10.40.0.0` for a better AD route, OSPF area preference and next-hop reachability. Full adjacency proves only neighbour exchange. Remove or adjust the competing route/policy after verifying intended design; confirm RIB and forwarding.

2. **OSPF stays in ExStart after increasing one side's MTU.**  
   Compare interface MTUs and database exchange logs. Restore matching end-to-end MTU and verify Full. `mtu-ignore` hides the mismatch and is not the first repair.

3. **MST blocks an uplink only between two switches with matching VLAN lists.**  
   Compare MST region name, revision and VLAN-to-instance map; a region mismatch changes boundary behaviour. Correct the mismatch and verify root/role per instance.

4. **Port-channel is up but one market-data flow drops after a member fails.**  
   Inspect surviving member utilisation, hashing and egress queue counters. Aggregate capacity fell; a single flow's mapping may change. Restore capacity or redesign failure-state traffic, then measure gaps and latency.

5. **BGP is Established; the advertised network is absent at the peer.**  
   Check exact local RIB prefix for the `network` statement, outbound prefix list/route map and address-family activation. Repair the first failing condition; verify advertised-routes and received path.

6. **BGP prefix is received and best but not in the RIB.**  
   Inspect next-hop resolution and a competing lower-AD route for the same prefix. Compare BGP table with `show ip route` and CEF before changing attributes.

7. **Local preference change moves traffic to a slower cross-connect.**  
   Confirm BGP best path, physical path and measured delay. Local preference drives outbound choice across the AS, but the higher-preference path may be physically slower. Revert or set policy per prefix after latency validation.

8. **EIGRP primary fails; route becomes active despite a second path.**  
   Read RD and FD in topology all-links. The second path may fail `RD < FD`; DUAL must query. Do not label it a feasible successor solely because a physical link exists.

9. **Redistributed route bounces between OSPF and EIGRP borders.**  
   Check tags, prefix filters, seed metrics and AD. Set a tag on import and deny that tag on reimport at both borders. Verify one copy of the intended route and fail one border in the lab.

10. **Summary route remains, one site disappears.**  
    Inspect component routes behind the summarizing router and Null0/discard behaviour. Restore the specific route or change advertisement policy; a summary is not proof that every component is alive.

11. **PBR route map matches packets, but source host still fails.**  
    Check specified next-hop reachability, return route and ingress attachment. Use track/fallback or a viable next hop. Check actual CEF/packet path, not only route-map counters.

12. **Ping succeeds in default VRF but fails from a customer VRF.**  
    Verify interface VRF membership, `show ip route vrf` and VRF-aware source ping. The default table is independent. Add the route in the correct VRF or correct attachment.

13. **Multicast receiver joins but feed never arrives after a unicast route change.**  
    Inspect `show ip rpf <source>` and `show ip mroute`. The new route toward source may point to another interface, rejecting multicast on the old ingress. Correct routing/PIM topology and verify `(S,G)` state and sequence continuity.

14. **PTP monitor reports a 50 µs one-way latency jump; RTT and queue counters are stable.**  
    Check grandmaster selection, PHC offset, asymmetry and timestamp source. A clock shift can create apparent one-way delay. Fix time path and compare with independently captured round-trip data.

15. **CoPP change causes OSPF neighbours to flap, while local switching still works.**  
    Inspect control-plane policy counters and OSPF packets to CPU. Restore an appropriate allowance/rate for OSPF, then verify neighbour stability and CPU load.

16. **Strict uRPF drops legitimate orders on one ingress.**  
    Check route back to source in the correct VRF and identify asymmetric return. Use an appropriate policy/loose mode only after design review; confirm anti-spoofing coverage and allowed flow.

17. **DMVPN spokes register with hub but cannot exchange application traffic.**  
    Inspect overlay routes, IPsec SAs and ACLs. If small ping works, probe PMTU/MSS. Check spoke-to-spoke NHRP/phase design separately from hub registration.

18. **MPLS customer prefix is present at one PE but absent at another.**  
    Follow CE advertisement → VRF → MP-BGP → RT export/import → remote VRF. An RT mismatch can isolate a site with healthy core labels. Correct policy and verify VPN route plus data plane.

19. **DHCPv6 clients have addresses but no default route.**  
    Check IPv6 router advertisements and RA Guard, not only DHCPv6 pool. Restore valid RA from the trusted router and verify client default route.

20. **NetFlow collector is empty during a known busy hour.**  
    Confirm monitor attachment and direction, flow cache, exporter source/route, collector port and template/parser compatibility. A populated cache with no collector data points to export/collector, not absence of traffic.

21. **Five-minute interface utilisation is 10%, yet output drops spike at market open.**  
    Compare interval deltas in queue counters with precise packet capture. Microbursts can fill a queue between polls. Size/buffer/rate-control changes need a measured baseline.

22. **An IP SLA tracked route flips repeatedly, causing TCP resets.**  
    Inspect probe destination, source, threshold/frequency and underlying loss. Tune tracking/hysteresis or fix transport; prove both stable control plane and application sessions.

23. **AAA rollout blocks all SSH after central server timeout.**  
    Retain console/OOB access, inspect method list and local fallback, server source interface and route. Repair AAA then test a new session before closing console.

24. **An AI assistant recommends disabling multicast storm control after feed gaps.**  
    Check actual storm-control drops and legitimate burst rate first. If causally linked, adjust threshold under controlled change and validate other VLANs; the recommendation alone is not evidence.

## Scoring rubric

Give 2 points each for correct evidence, discriminating check, causal explanation, minimal repair and post-check. Target 8/10 on every case without consulting the answer.

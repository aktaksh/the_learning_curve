HFT Networking, Solarflare, FPGA & Linux Syllabus

Recommended Learning Order
Ethernet
→ IP
→ UDP/TCP
→ Multicast
→ Linux Packet Path
→ NIC Queues
→ CPU/NUMA/PCIe
→ Solarflare
→ OpenOnload
→ ef_vi
→ DPDK / AF_XDP
→ Linux Low-Latency Tuning
→ PTP
→ Latency Measurement
→ Trading Protocols
→ FPGA Fundamentals
→ FPGA Networking
→ HFT Architecture
→ Hands-On Capstone


1. Ethernet Fundamentals
- Ethernet frame structure
- Source/Destination MAC
- Broadcast / Unicast / Multicast
- ARP
- VLAN / 802.1Q
- MTU / Jumbo Frames
- CRC / FCS
- Duplex / Auto-negotiation
- Link speed
- LLDP

2. IP Networking
- IPv4 / IPv6 basics
- CIDR / Subnetting
- Routing table
- Default gateway
- ARP / Neighbor table
- ICMP
- Fragmentation
- Path MTU Discovery
- Static routing
- ECMP
- Asymmetric routing

3. TCP for Trading Systems
- TCP handshake
- Sequence / ACK numbers
- Sliding window
- Retransmissions
- Congestion control
- Delayed ACK
- Nagle algorithm
- TCP_NODELAY
- Receive / Send buffers
- Connection reset
- TIME_WAIT
- TCP Keepalive

4. UDP Market Data
- UDP characteristics
- Datagram structure
- Packet loss
- Packet reordering
- Duplicate packets
- Sequence numbers
- Gap detection
- Recovery channel
- Snapshot + incremental feeds
- A/B feed arbitration

5. Multicast Engineering
- Multicast addressing
- IGMPv2 / IGMPv3
- IGMP snooping
- Querier
- PIM-SM
- SSM
- RPF
- Multicast routing
- Source / Group concepts
- Multicast join / leave
- Market-data multicast troubleshooting

6. Data-Centre Switching
- L2 switching
- MAC learning
- CAM table
- VLANs
- Trunks
- LACP
- MLAG
- STP / RSTP
- Port channels
- Cut-through switching
- Store-and-forward
- Switch buffers
- Microbursts
- Head-of-line blocking

7. Exchange / Colocation Networking
- Colocation architecture
- Cross-connects
- Exchange handoff
- Market-data networks
- Order-entry networks
- Drop-copy networks
- A/B paths
- Active / Standby connectivity
- Failure-domain separation
- Exchange certification environments

8. Linux Networking Fundamentals
- ip
- ss
- ethtool
- tcpdump
- tshark
- nstat
- tc
- /proc/net/*
- Network namespaces
- Routing tables
- Policy routing
- Bonding
- VLAN interfaces

9. Linux Packet Path
- NIC RX/TX
- DMA
- RX/TX descriptor rings
- Interrupts
- MSI / MSI-X
- NAPI
- SoftIRQ
- ksoftirqd
- SKB
- qdisc
- Routing lookup
- Netfilter
- Socket queues
- User-space delivery

10. NIC Queue Engineering
- RX queues
- TX queues
- RSS
- RSS hash
- Indirection table
- Toeplitz hashing
- Flow steering
- ntuple filters
- RPS
- RFS
- XPS
- IRQ affinity
- Queue-to-core mapping
11. CPU & NUMA Locality
- CPU sockets
- NUMA nodes
- Local vs remote memory
- CPU affinity
- taskset
- numactl
- numastat
- IRQ placement
- NIC NUMA placement
- PCIe topology
- Cross-NUMA latency

12. PCIe / DMA / IOMMU
- PCIe hierarchy
- Root complex
- PCIe lanes
- BAR
- DMA
- IOMMU
- DMA mapping
- MSI-X
- SR-IOV
- Virtual Functions
- PCIe latency considerations

13. Solarflare / AMD NIC Architecture
- Solarflare NIC architecture
- Xilinx / AMD Solarflare evolution
- NIC RX/TX queues
- Event queues
- Hardware filters
- Packet steering
- Hardware timestamping
- Firmware
- NIC buffer configuration
- Driver architecture
- Vendor diagnostics

14. Solarflare OpenOnload
- Kernel bypass concept
- Onload architecture
- Accelerated sockets
- Onload stack
- User-space networking
- Busy polling
- Spin / Interrupt modes
- Stack affinity
- onload
- onload_stackdump
- onload_tool
- Onload environment variables
- TCP acceleration
- UDP acceleration
- Multicast acceleration
- Troubleshooting fallback to kernel stack

15. Solarflare ef_vi
- Virtual Interface concept
- Protection Domain
- Event Queue
- RX ring
- TX ring
- Memory registration
- DMA buffers
- Polling
- Packet transmission
- Packet reception
- Zero-copy concepts
- Hardware filters
- Timestamping
- Direct NIC access

16. Kernel Bypass Technologies
- Kernel networking vs bypass
- OpenOnload
- ef_vi
- DPDK
- AF_XDP
- XDP
- io_uring networking awareness
- RDMA
- Zero-copy
- Busy polling
- Poll-mode drivers

17. DPDK
- EAL
- HugePages
- PMD
- Mempools
- mbufs
- RX/TX rings
- Poll mode
- CPU pinning
- NUMA awareness
- Multi-queue NICs
- Flow rules
- RSS
- DPDK latency tuning

18. AF_XDP / XDP
- XDP hook
- eBPF basics
- XDP_DROP
- XDP_PASS
- XDP_REDIRECT
- UMEM
- Fill / Completion rings
- RX/TX rings
- Zero-copy mode
- Native vs generic XDP
- AF_XDP sockets

19. Linux CPU Scheduling
- Process / Thread
- Context switch
- Scheduler
- CFS / EEVDF basics
- Run queue
- CPU affinity
- Scheduler migrations
- SCHED_FIFO
- SCHED_RR
- Real-time priorities
- Scheduler latency

20. Linux Low-Latency Tuning
- isolcpus
- nohz_full
- rcu_nocbs
- CPU pinning
- IRQ pinning
- C-states
- P-states
- CPU governor
- Turbo
- Hyper-Threading / SMT
- HugePages
- THP
- Swappiness
- mlock
- Kernel boot parameters

21. Interrupt Engineering
- Hardware IRQ
- SoftIRQ
- MSI-X
- IRQ affinity
- irqbalance
- /proc/interrupts
- Network interrupts
- Interrupt moderation
- Adaptive coalescing
- Busy polling
- Polling vs interrupts
22. Memory & Cache Performance
- L1 / L2 / L3
- Cache lines
- Cache misses
- False sharing
- TLB
- Page faults
- HugePages
- Memory locality
- Cache coherence
- MESI
- Memory bandwidth
- Prefetching

23. Linux Performance Analysis
- perf stat
- perf record
- perf report
- perf top
- perf sched
- perf c2c
- pidstat
- mpstat
- vmstat
- sar
- numastat
- FlameGraphs

24. eBPF / BCC / bpftrace
- eBPF architecture
- Tracepoints
- kprobes
- uprobes
- BCC tools
- bpftrace
- Network tracing
- Scheduler tracing
- IRQ tracing
- TCP retransmission tracing
- Latency diagnosis

25. Precision Time Synchronization
- PTP / IEEE 1588
- PHC
- Grandmaster
- Boundary clock
- Transparent clock
- BMCA
- Hardware timestamping
- Software timestamping
- SyncE
- Clock drift
- Offset
- Holdover
- Asymmetry

26. Linux PTP Tools
- ptp4l
- phc2sys
- pmc
- chronyc
- ethtool -T
- PHC inspection
- PTP offset monitoring
- Timestamp verification

27. Latency Measurement
- Latency vs throughput
- Jitter
- Deterministic latency
- P50
- P99
- P99.9
- P99.99
- Histograms
- Coordinated omission
- One-way latency
- Round-trip latency
- Tick-to-trade
- Order-to-ack
- Wire-to-wire

28. Packet Analysis
- Wireshark
- tcpdump
- PCAP
- Packet timestamps
- TCP retransmissions
- UDP sequence gaps
- Multicast analysis
- Microbursts
- Packet drops
- Hardware TAP
- SPAN port limitations

29. FPGA Fundamentals
- FPGA architecture
- LUTs
- Flip-flops
- BRAM
- DSP blocks
- Clock domains
- Pipelines
- Parallelism
- Deterministic processing
- FPGA vs CPU vs GPU

30. FPGA Networking
- Ethernet MAC in FPGA
- Packet parser
- UDP parser
- Multicast parser
- FIX / ITCH parsing
- Market-data decoding
- Packet filtering
- Hardware timestamping
- Line-rate processing
- Cut-through processing

31. FPGA Programming Basics
- Verilog
- SystemVerilog
- VHDL awareness
- RTL
- Combinational logic
- Sequential logic
- Finite State Machines
- Simulation
- Testbench
- Timing constraints
- Synthesis
- Place and Route

32. FPGA HFT Use Cases
- Market-data feed handler
- Order-book preprocessing
- Packet filtering
- Feed arbitration
- Sequence-gap detection
- Risk checks
- Order generation
- Hardware timestamping
- TCP / UDP offload
- FPGA NICs

33. FPGA/NIC Products Awareness
- AMD/Xilinx Alveo
- AMD Solarflare
- Exablaze / Cisco Nexus SmartNIC heritage
- NVIDIA ConnectX
- NVIDIA BlueField
- Intel FPGA
- SmartNIC
- DPU
- FPGA NIC architecture

34. Market Data Protocols
- NASDAQ ITCH
- OUCH
- MoldUDP64
- CME MDP 3.0
- SBE
- FAST awareness
- Binary protocol decoding
- Endianness
- Sequence numbers
- Gap recovery

35. Order Entry & FIX
- FIX protocol
- FIX session
- Tags
- Heartbeat
- Sequence numbers
- Resend request
- Gap fill
- Logon / Logout
- New Order
- Cancel
- Replace
- Execution Report
- Drop Copy

36. HFT Trading Architecture
- Market Data Feed Handler
- Normalizer
- Order Book
- Strategy
- Risk Engine
- Order Gateway
- Exchange Gateway
- Drop Copy
- OMS
- EMS
- Position / PnL
- Replay
- Journal

37. Lock-Free Programming Concepts
- Atomics
- Memory ordering
- CAS
- Spinlocks
- SPSC queue
- MPSC queue
- Ring buffer
- Cache-line padding
- False sharing
- Wait-free concepts

38. C / C++ for Low Latency
- Pointers
- Memory management
- RAII
- Stack vs heap
- STL
- Templates
- Atomics
- Threads
- Memory model
- Custom allocators
- Placement new
- Zero allocation hot path
- Lock-free queues
- Compiler optimization

39. Low-Latency Application Design
- Hot path / Cold path
- Pre-allocation
- Memory pools
- Object reuse
- Zero-copy
- Batching
- Busy spinning
- Cache warming
- Branch prediction
- Avoiding syscalls
- Avoiding locks
- Deterministic execution

40. Observability for HFT
- NIC counters
- Switch counters
- CPU counters
- IRQ counters
- SoftIRQ counters
- Packet drops
- RX ring overflow
- TCP retransmissions
- Latency histograms
- Clock offset
- Hardware health

41. Failure Scenarios
- Link failure
- NIC failure
- Switch failure
- Packet loss
- Packet reordering
- RX ring overflow
- SoftIRQ saturation
- NUMA misplacement
- Multicast RPF failure
- TCP retransmission spike
- PTP drift
- Clock loss
- Feed gap
- Exchange disconnect

42. Troubleshooting Commands
- ip
- ss
- ethtool
- ethtool -S
- ethtool -g
- ethtool -c
- ethtool -l
- ethtool -x
- tcpdump
- tshark
- tc
- nstat
- perf
- numactl
- numastat
- taskset
- chrt
- lspci
- setpci
- hwloc
- ptp4l

43. Hands-On Labs
- Build UDP sender/receiver
- Build multicast sender/receiver
- Capture multicast traffic
- Simulate packet loss
- Detect sequence gaps
- Configure RSS
- Inspect NIC queues
- Pin IRQ to CPU
- Pin application to CPU
- Test NUMA-local vs remote execution
- Configure HugePages
- Test DPDK
- Test AF_XDP
- Install OpenOnload
- Explore ef_vi
- Configure PTP
- Measure jitter
- Benchmark kernel vs bypass networking

44. Capstone Project
- Simulated exchange market-data feed
- UDP multicast market data
- A/B feed handling
- Sequence-gap detection
- Feed handler
- Order book
- Strategy process
- Risk check
- Order gateway
- Solarflare/OpenOnload or DPDK path
- CPU/IRQ pinning
- NUMA-aware deployment
- PTP timestamps
- P50/P99/P99.9 latency measurements
- Packet-loss and failover testing
- Performance report

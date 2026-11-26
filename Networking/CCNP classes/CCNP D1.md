
STP Class A - 10.0.0./8
Class B - 172.0.0.0/16
Class C - 192 to  198.168.0.0/16




IPv0 to IPv15 was done
IPv4 - each ocetet is 32 bit
2^8 = 256 IP == 0 to 255 ips
2^ == 32 billion ip
2^16 = 65536IP s-- usable 65534


011111 = 0x2 + 1X
you canot use first and last ip 
Class	Leading bits	First octet	Default mask
A	0xxxxxxx	0–127	/8

# Loop


loop back address 127.0.0.1 ping self to check nic card
56 hops is msax hops TL control the life to prevent loop foever
127.0.0.(1-254) - starting wiht 127 then its loop back and all can ping  

ping 127.0.0.2
PING 127.0.0.2 (127.0.0.2) 56(84) bytes of data.
64 bytes from 127.0.0.2: icmp_seq=1 ttl=64 time=1.44 ms
64 bytes from 127.0.0.2: icmp_seq=2 ttl=64 time=0.082 ms

# APIPA 
169.254.x.x -- DHCP server ip if it fails
APIPA - Auto priate IP addressing
# subnet mask
subnet mask -  network portion + host range
eg 192.168.1.1 / 255.255.255.0  -- Then 192.168.1 is network portion + 0 - host portion

## OSI layers --
App , Presentation , Session, Transport, network, data link, physical

Network design layer -- 
1. Access L2- point where the device finds it's network, ca be router or switch but ideally should be L2 - gives speed too
2. Distribution L3 - When there multiple switch with HA and cabling is a mess. happens at OSI layer 3. Uses Multi layer swicth like 3560-24PS  
3. Core layer -- Solution which combines all musltilayer switches - provides speed not security

LACP PAP protocol for HA
OPOF - one point of failure.
STP - spanning tree protocol esp when second HA cbale is connected. Hence STP is mandated.
 Orange icon in cable in CPT is  building spaning tree.
All cables are bundles in etherchannel.

## STP and port priority
create STP and loops.

Priority Default 32769, 
root id and bridge id will be visible for MAC in `sh spanning-tree`
If all equiality  deisgn wise and MAC wise -- checks least MAC address and then priority.  
try switch 2960 and join 4 switches in sqaure shape
Add spanning tree vlan 1 priority  - root bridge - root primary command usage.
RB(root base) will be root device - rest are NRB - Non root base
Min no of hops - 19 is the number for one port to another port connection
fastest connection to RB is RP-root port
See th cost value in Switch console.
If there is Tie in cost the root port selection will depend on 1. Cost Then 2. Priority of switch 3. MAC address weightage then 4th low port number id 
Root briodge switch will control the entire Spanning tree.
DP - designated port -- which carries traffic about port and switch health  - it is on segment 
Segmnebnt means connection between two switch
RB all ports are called DP.

# Rapid spanning tree protocol

Normal new device connection time in 30 secs
Port fast is configuration
cross cable UTP
different device with solid cable line in CPT is straight cable.
access port -- for end devices
Trunk port -- for network devices
cofnigure as port fast
BPDM - Bridge prootocl data unit.
BPDU gard wil prevent enabling if you mistkenly connect access port to network device 
Error disable state of port
port fast + BPDU is always enabled
Rapid PVST - Rapid per vlan spanning tree
Spannign tree mode rapid

## VLAN
Works in datalink layer - MAC address - Layer 2 only.
Different Vlan tag with same IP range can be possible
config t - Vlan 10 - name hr. -  swithc port mode access vlan 10 




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

create STP and loops.
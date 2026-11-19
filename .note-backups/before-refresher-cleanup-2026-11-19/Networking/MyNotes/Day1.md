MAC - Media access control are h exadecimal values , Why?

Because a MAC address is 48 bits, and hexadecimal is a compact, human-readable way to represent binary.
Example:
Binary:
00110100 10101011 11001101 00010010 00110100 01010110

Hex:
34:AB:CD:12:34:56
Why hex specifically?
- 1 hex digit = 4 bits
- 2 hex digits = 1 byte
- MAC address = 6 bytes
- So MAC address = 12 hex digits
Example:
AA:BB:CC:DD:EE:FF
Each pair represents one byte:
AA = 10101010
BB = 10111011
Hex is preferred because binary would be too long and decimal would be less convenient for byte-level representation.
So the MAC address is not actually “hexadecimal” internally; it is binary bits on the wire, displayed to humans in hexadecimal.





  











Broadcast --

Destination MAC = FF:FF:FF:FF:FF:FF

Source MAC:      AA:BB:CC:DD:EE:01
Destination MAC: FF:FF:FF:FF:FF:FF

Unicast   → one device
Broadcast → all devices in the VLAN
Multicast → selected group of devices

Ethernet frame - parts

Destination MAC (BB:BB:BB .... )     --- source MAC(AA:AA:AA:.....)

Type -- IPv4/IPv6

Data/Payload

FCS -  Error check

| Preamble | SFD | Destination MAC | Source MAC | EtherType/Length | Payload | FCS |
Typical sizes:
Field	Size	Purpose
Preamble	7 bytes	Synchronizes sender/receiver
SFD	1 byte	Start Frame Delimiter
Destination MAC	6 bytes	Receiver MAC
Source MAC	6 bytes	Sender MAC
EtherType/Length	2 bytes	Identifies upper-layer protocol, e.g. IPv4
Payload	46–1500 bytes	Actual data
FCS	4 bytes	CRC error detection


Example:
[Dst MAC][Src MAC][Type][IP Packet............][FCS]
Important: the normal Ethernet frame size is 64–1518 bytes, excluding preamble/SFD. VLAN tagging usually adds 4 bytes.





  











Switch check which port of physical cable has this destination ip.

A switch learns MAC addresses by looking at the source MAC address of incoming Ethernet frames.
Example:
PC-A ---- Port 1   Switch   Port 2 ---- PC-B
MAC A                      MAC B
When PC-A sends a frame:
Source MAC:      AA:AA:AA:AA:AA:AA
Destination MAC: BB:BB:BB:BB:BB:BB
The switch sees the frame arrive on Port 1 and learns:
MAC Table / CAM Table

AA:AA:AA:AA:AA:AA  → Port 1
Then:
- If destination MAC is already known → send only to that port.
- If destination MAC is unknown → flood to all ports in that VLAN except the incoming port.
- When PC-B replies, switch learns:
BB:BB:BB:BB:BB:BB → Port 2
Now the table is:
MAC Address             Port
AA:AA:AA:AA:AA:AA       1
BB:BB:BB:BB:BB:BB       2
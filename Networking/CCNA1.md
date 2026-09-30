### Types of devices

Switches - catalyst 9200 , 93000, 9400, Meraki MS Ciso Nexus


Routers - ISR 900 series, ISR 1000 series, NCS  5700 sries IR 900

Firewalls - 1100 , 1200 , 1300 series





### Mode of comm

simplex - one way comm -

half duplex - send or receive

full duplex  - either Tx RX - whatsapp vcall

### Identity of host machine

Device name , MAC , IP

IPV4 classes and

networking criteria - Performance , reliability, security

categories of networkng - LAN WAN MAN

Transmission media -

Guided media - Twisted pair , coaxial cable , Optical fiber cable

Unguided media - Radiowaves, Microwaves, infrared

unshielded twisted pair - least expensive - saves the Electro magentic field , limited length oof ttansmission

STP - shielded twisted pair -

Coaxial cable - central copper , insulator layer then braided metal copper and then plastic

More ressistant to  interference - used in cable tv , higher bandwidth

Optical fiber cable- guided light signals

subnet 172.1.1.0

24 bit set 

10101000.0001......,00.....-0000

## Special ips :

0.0.0.0/0   - any not valid

127.0.0.0/8 - loop back

0.0.0.0/32 - this host

255.255.255.255/32 - broadcast  ip

### Private ips

192.168.0.0/16

172.16.0.0/12

10.0.0.0/8

---------
Preamble - SFD -  Desitnation MAC -  SRC MAC - Ethernet  Length - Payload - FCS

00 11 22 33 44 55   AA BB CC DD EE FF   08 00   45 00 00 3C ...   12 34 56 78
| Destination MAC | |   Source MAC    | |Type| |   Payload      | |   FCS    |

ARP  Addess resolution protocol

Protocals in pythical layer -

Etehrnet IEEE 802.3

WIFI - IEEE 802.11

bluetooth IEEE 802.15.1

PTP - point to point 

Mesh topology -  All devices connected directly to another device diretcly


Star topology - Device 1 ,2 ,3 , 4 , 5 all connected via central swtich

BUS topology -  Central line ofnetwork and uses single cable  for distribution
 - coaxial cable
Ring topology - one device fwds to another




Data link layer -

Switching a process of  transfer of data

Frames - MAC - IP forwarding - Table - Frame transimission

## Types of switching --

1. Circuit swithced - eg - telephone - connecation is reserved - dedicated path 

2. Packet switched network - Data borken in paarts ad can go via many paths - reassmbeled at end to form the message again
3. Message switched - entire message is sent to intermediate node

Class A N.H.H.H  3 octets is host PVT. IP - 10.0.0.0  to 10.255.255.255  Range 0 -127
Class B N.N.H.H  2 octets is network. IP 172.16.0.0/16 to 172.31.255.255 - Range 128 to 191
Class C N.N.N.H  eg : 192.168.0.0 to 192.168.255.255 - Range 192 - 223.
Class D                                                 Range - 224 - 239
Class E                                                  Range 240 to 255


128.10.5.9 and 128.11.5.10 are different networks - need router
128.10.5.9 and 128.0.5.10 are same networks - needs only hub or  switch

IP vs4 address == 4.3 bilions

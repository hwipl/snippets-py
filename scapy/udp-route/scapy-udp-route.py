#!/usr/bin/env python3

# Send UDP packet with random data with changed scapy routing table (see code).
# Command line arguments:
# <destination IP> <destination port> <size of random data>

import sys

from scapy.all import conf, IP, UDP, Raw, RandString, sr1

# command line arguments
dst = sys.argv[1]
dport = int(sys.argv[2])
size = int(sys.argv[3])

# set scapy routing for destination address
# conf.route.add(net=dst+"/32", dev="tun0")
conf.route.add(net=dst+"/32", gw="192.168.1.1")
print(conf.route)

# send udp packet
pkt = IP(dst=dst)/UDP(sport=32000, dport=dport)/Raw(RandString(size=size))
r = sr1(pkt, timeout=1)
print(r)

#!/usr/bin/env python3

# Send UDP packet with random data.
# Command line arguments:
# <destination IP> <destination port> <size of random data>

import random
import sys

from scapy.all import IP, UDP, Raw, RandString, sr1

# command line arguments
dst = sys.argv[1]
dport = int(sys.argv[2])
size = int(sys.argv[3])

# send udp packet
ip = IP(dst=dst, flags="DF")
sport = random.randint(1024, 65535)
udp = UDP(sport=sport, dport=dport)
data = Raw(RandString(size=size))
r = sr1(ip/udp/data, timeout=1)
print(r)

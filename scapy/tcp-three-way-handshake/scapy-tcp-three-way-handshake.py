#!/usr/bin/env python3

# Perform a TCP three-way handshake and then send a packet of random data.
# Command line arguments:
# <destination IP> <destination port> <size of random data>
#
# Note: when receiving SYN ACK, OS will send RST to destination IP because it
# does not know the TCP connection we are establishing. You can filter the RST
# with iptables/nftables to make this work.

import random
import sys

from scapy.all import IP, TCP, sr, sr1, send, Raw, RandString

# command line arguments
dst = sys.argv[1]
dport = int(sys.argv[2])
size = int(sys.argv[3])

# three way handshake
ip = IP(dst=dst)
sport = random.randint(1024, 65535)
seq = 1000

# send syn, get synack
syn = TCP(sport=sport, dport=dport, flags="S", seq=seq)
synack = sr1(ip/syn)

# send ack
ack = TCP(sport=sport, dport=dport, flags="A", seq=syn.seq+1, ack=synack.seq+1)
send(ip/ack)

# send packet with random data
tcp = TCP(sport=sport, dport=dport, flags="A", seq=syn.seq+1, ack=synack.seq+1)
data = Raw(RandString(size=size))
pkt=ip/tcp/data
r = sr(pkt, timeout=2)
print(r)

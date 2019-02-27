#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#print str(sys.argv)

packet = bytearray([
    1,      # API version 1

    1,      # Tag 1: Set light color
    0,      # Light number 0
    0,      # Light type 0 = RGB
    int(sys.argv[1]),    # Red
    int(sys.argv[2]),    # Green
    int(sys.argv[3]),    # Blue

#    1,      # Tag 1: Set light color
#    1,      # Light number 1
#    0,      # Light type 0 = RGB (protip: they're all RGB lights)
#    0,      # Red
#    0,      # Green
#    255,    # Blue

    # Exercise 1: Guess what this does.
#    1, 2, 0, 0, 255, 0,
#    1, 3, 0, 255, 0, 255,
])


# The server is running at valot.party:9909 in the party LAN
udp_socket.sendto(packet, ('127.0.0.1', 9909))

udp_socket.close()


#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
import sys


class Instanssi(object):
    """
    Python-luokka Instanssin valojen hallintaan. 
    """

    def __init__(self, nick, ip, port):
        self.ip = ip
        self.port = port
        self.nick = nick

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.reset()

    def reset(self):
        """Resetoi UDP-paketti"""
        self.packet = [ 1 ] # Speksin versio aina yksi

        self.packet.append(0) # Aloita tagi osa
        for char in self.nick:
            # Muunna nickin merkit ascii koodeiksi
            self.packet.append(ord(char))
        self.packet.append(0) # Lopeta tagi osa


    def set(self, i, r, g):
        """Aseta valo i RGB-arvoon"""
        self.packet += [
            1, # Tehosteen tyyppi on yksi eli valo
            i, # Valon indeksi
            0, # Laajennustavu. Aina nolla. Älä välitä tästä
            r, # teho
            g # strobo
        ]

    def send(self):
        """Lähetä asetetut tavut ja nollaa pakettilista"""
        bytes = bytearray(self.packet)
        self.socket.sendto(bytes, (self.ip, self.port))
        self.reset()







valot = Instanssi("instanssilainen", "127.0.0.1", 9909)

# 2 ensimmäistä argumenttia ovat valo josta aloitetaan ja valo johon lopetetaan, 3 viimeistä ovat väriarvot.
for i in range(int(sys.argv[1]), int(sys.argv[2])):
    valot.set(i, int(sys.argv[3]), int(sys.argv[4]))
# Lähetä sinisyys käskyt kaikki kerralla
valot.send()

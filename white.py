#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time


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


    def set(self, i, r, g, b):
        """Aseta valo i RGB-arvoon"""
        self.packet += [
            1, # Tehosteen tyyppi on yksi eli valo
            i, # Valon indeksi
            0, # Laajennustavu. Aina nolla. Älä välitä tästä
            r, # Punaisuus
            g, # Vihreys
            b, # Sinisyys
        ]

    def send(self):
        """Lähetä asetetut tavut ja nollaa pakettilista"""
        bytes = bytearray(self.packet)
        self.socket.sendto(bytes, (self.ip, self.port))
        self.reset()







valot = Instanssi("instanssilainen", "127.0.0.1", 9909)


# Sinistä kansalle. Aseta kaikki valot sinisiksi
for i in range(0, 36):
    valot.set(i, 255, 255, 255)
# Lähetä sinisyys käskyt kaikki kerralla
valot.send()
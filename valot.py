#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
import sys

"""
Yksinkertainen UDP-paketti Instanssin valojen ohjailuun Pythonilla.
UDP-paketti koostuu speksin versiosta, nick-tagista sekä yhdestä tai 
useammasta tehostekäskystä.
Tämä ei ole mitenkään Python spesifinen tapa toteuttaa valojen ohjausta. 
Vastaava onnistuu aivan yhtä helposti millä tahansa ohjelmointikielellä.
Googlaa vain "How send packet over UDP with XXX" tms.
Tämän esimerkin pitäisi toimia millä tahansa alustalla jossa on
Python-tulkki asennettuna.
Monipuolisempi esimerkki jossa UDP-paketti rakennetaan dynaamisesti
löytyy täältä: 
https://github.com/epeli/effectserver/blob/master/examples/instanssi.py
"""



import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet = bytearray([
    1, # Speksin versio aina yksi

    0, # Nick tag
    101, # e
    112, # p
    101, # e
    108, # l
    105, # i
    0, # Nick lopetus

    # Ensimmäinen tehostekäsky
    1, # Tehosteen tyyppi on yksi eli valo
    int(sys.argv[1]), # Ensimmäinen valo löytyy indeksistä nolla
    0, # Laajennustavu. Aina nolla.
    int(sys.argv[3]), # Punaisuus maksimiin
    int(sys.argv[4]), # Vihreys nollaan
    int(sys.argv[5]) # Sinisyys nollaan


    # # Toinen tehostekäsky
    # 1, # Toinen tehoste on myöskin valo eli yksi
    # 1, # Toinen valo on indeksissä yksi
    # 0, # Laajennustavu. Aina nolla.
    # # Ja sit rbg kuten edellä
    # 0,
    # 255,
    # 0,

    # Tähän voisi laittaa vielä n-kappaletta tehostekäskyjä

])


udp_socket.sendto(packet, ('valot.party', 9909))

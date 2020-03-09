#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
import sys
import os
import subprocess

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
a3 = int(sys.argv[3])

b1 = int(sys.argv[4])
b2 = int(sys.argv[5])
b3 = int(sys.argv[6])

speed = float(sys.argv[7])
valo = int(sys.argv[8])


red = 100
green = 100
blue = 100


class Fader(object):

	i = 0.1
	while i < 1:
		print(i)
		red=(a1-b1)*i+b1
		green=(a2-b2)*i+b2
		blue=(a3-b3)*i+b3

		i += 0.05

		intRed=int(red)
		intGreen=int(green)
		intBlue=int(blue)
		
		time.sleep(speed)

		print(str(intRed) + " " + str(intGreen) + " "+ str(intBlue))

		kutsu = ".\/valot.py" + " " + str(valo) + " " + str(valo) + " " + str(intRed) + " " + str(intGreen) + " " + str(intBlue)
	        print(kutsu)

		subprocess.call(kutsu, shell=True)


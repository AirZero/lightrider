#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
import sys
import os
import subprocess

a1 = 255
a2 = 0
a3 = 0

b1 = 0
b2 = 0
b3 = 255

red = 100
green = 100
blue = 100


class Fader(object):

	i = 0.1
	while i < 1:
		print(i)
		i += 0.1
		red=(a1-b1)*i+b1
		green=(a2-b2)*i+b2
		blue=(a3-b3)*i+b3
		
		intRed=int(red)
		intGreen=int(green)
		intBlue=int(blue)
		
		print(str(intRed) + " " + str(intGreen) + " "+ str(intBlue))
		
		#miten muuttujan saa meneen parametrina perille?
		kutsu = ".\/all.py 0 36 " + str(intRed) + " " + str(intGreen) + " " + str(intBlue)
	        print(kutsu)
		#os.system("./all.py 0 36 red green blue")
		#os.system(kutsu)
		#subprocess.call("all.py")
		#subprocess.call(['python', 'all.py', "0 36 255 255 255"])
		subprocess.call(kutsu, shell=True)


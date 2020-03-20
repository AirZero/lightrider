#!/bin/bash

i=0

while [ $i -lt 250 ]
do
	#V=$(80)
	echo $i
	./all.py 0 25 $i 0 0 #$V 0
	((i+=10))
	sleep 0.45*$i
	sleep 0.05
done
./all.py 0 25 0 0 0 

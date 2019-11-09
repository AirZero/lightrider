#!/bin/bash

i=4

while [ $i -ne 244 ]
do
	V=$(((($RANDOM) % 100) - 70))
	./all.py 0 25 $i $V 0
	echo $i
	((i+=10))
	#sleep 0.01
done

#!/bin/bash

i=254

while [ $i -gt 10 ]
do
	V=$(((($RANDOM) % 100) - 80))
	echo $i
	./all.py 0 25 $i $V 0
	((i-=10))
done
./all.py 0 25 0 0 0 

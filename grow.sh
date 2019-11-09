#!/bin/bash

i=4

while [ $i -ne 244 ]
do
	./all.py 0 25 $i 0 0
	echo $i
	((i+=10))
	#sleep 0.01
done

#!/bin/bash

i=254

while [ $i -gt 1 ]
do
	echo $i
	./all.py 0 25 $i 0 0
	((i-=10))
done
./all.py 0 25 0 0 0 

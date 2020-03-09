
#!/bin/bash


while :
./all.py 0 36 0 0 0
do
  x=1
  while [ $x -le 30 ]
  do
	./all.py 0 $x 255 0 0
	x=$(( $x + 1 ))
	sleep 0.2
  done
  ./all.py 0 36 0 0 0

done

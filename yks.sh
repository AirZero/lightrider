
#!/bin/bash


while :
./all.py 0 30 0 0 0
do
  x=-1
  luku=1
  while [ $x -le 30 ]
  do
	luku=$(( $x ))
	x=$(( $x + 1 ))
	./valot.py $x 0 0 255 55
	./valot.py $luku 0 0 0 2
        sleep 0.3
  done
  ./all.py 0 22 0 0 0

done

while [ 1==1 ]
do
	#./all.py 0 25 255 255 255
	./all.py 0 25 0 0 0 
	./all.py 0 25 255 0 0
	sleep 0.2
	./all.py 0 25 255 50 0
	sleep 0.1
	./all.py 0 25 255 180 0
	sleep 0.2
	./all.py 0 25 200 50 0
	sleep 0.1
done

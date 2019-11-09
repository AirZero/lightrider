while [ 1==1 ]

do
	./all.py 0 25 0 100 255
	sleep 0.05
	./all.py 0 25 0 0 0
	sleep 0.05
	./all.py 0 255 255 255
	sleep 0.2
	./all.py 0 25 20 0 255
	sleep 0.05
	./all.py 255 255 255
	sleep 0.05
	./all.py 0 255 0 0 0
	sleep 0.05
	./all.py 255 255 255
done

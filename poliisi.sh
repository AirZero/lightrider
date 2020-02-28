while true; do 
./walker.py 0 0 0 0 0 255 0.001
./all.py 0 36 255 0 0
./walker.py 0 0 0 0 0 255 0.001
./walker.py 255 0 255 0 0 0 0.001
sleep 0.01 & wait
done

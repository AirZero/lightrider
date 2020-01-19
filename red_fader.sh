while true; do 
./walker.py 222 0 0 0 0 0 0.1
./walker.py 0 0 0 222 0 0 0.1
sleep 0.01 &
wait
done

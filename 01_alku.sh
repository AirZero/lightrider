while true; do 
./walker.py 0 120 20 0 120 120 0.3
./walker.py 0 120 120 0 120 20 0.2
sleep 0.01 &
wait
done

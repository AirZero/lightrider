curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"sat":0, "on": true, "bri": 254, "transitiontime":0}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/1/state

curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"sat":0, "on": true, "bri": 254, "transitiontime":0}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/2/state

curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"sat":0, "on": true, "bri": 254, "transitiontime":0}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/3/state


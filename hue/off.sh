curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 20000, "on": false, "transitiontime":0}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/1/state

curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 20000, "on": false, "transitiontime":0}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/2/state

curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 20000, "on": false, "transitiontime":0}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/3/state



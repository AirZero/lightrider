curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 46920, "on": true, "transitiontime":0, "sat":254, "bri":254}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/1/state

curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 46920, "on": true, "transitiontime":0, "sat":254, "bri":254}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/2/state

curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 46920, "on": true, "transitiontime":0, "sat":254, "bri":254}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/3/state

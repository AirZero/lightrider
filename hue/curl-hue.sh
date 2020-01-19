curl -H "Content-Type: application/json" \
  -X PUT \
  --data '{"hue": 50000, "off": true, "bri": 100}' \
  http://127.0.0.1/api/38cbdfe83acb11eabd68b827eb817ef8/lights/1/state

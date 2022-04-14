#esse robo coleta os symbolos das moedas para que possam ser requisitadas

import requests

response = requests.get("https://api.binance.com/api/v3/ticker/price")
response = response.json()

for x in range(0, len(response)):
  #print(response[x]['symbol'])
  if response[x]['symbol'] == 'SANTOSBUSD':
     print(x)
#esse robo lê os valores das moedas e exibe no cmd
import requests
import os
import time


def pricesdash(symbols):

  while (0 == 0):  

    priceList = []

    for x in symbols:
      payloads = {'symbol' : x}
      response = requests.get("https://api.binance.com/api/v3/ticker/price" , params=payloads)
      response = response.json()
      priceList.append(response)

    os.system('cls')
    
    for x in priceList:
      symbol = x['symbol']
      price = x['price']
      print(f'{symbol:<15}', f'{price:<18}' ,  sep='|  ')
      print('-----------------------------------------------------------')

    time.sleep(1)
#esse robo lê os valores das moedas e exibe no cmd
import requests
import os
import time

def pricesdash(symbols,users):

  coin = 'Moeda'
  cotdol = 'Cotação Dollar'
  cotbrl = 'Cotação em real'

  while (0 == 0):  
    #puxa a cotação do real
    brlvalue = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()
    brlvalue = brlvalue['USDBRL']

    #puxa a cotação das cripto
    priceList = []
    for x in symbols:
      payloads = {'symbol' : x}
      response = requests.get("https://api.binance.com/api/v3/ticker/price" , params=payloads).json()
      priceList.append(response)

    os.system('cls')
    
    #gera o cabeçalho da tabela
    print(f'{coin:<15}', f'{cotdol:<18} ' , f'{cotbrl:<18}  ' ,  sep='|  ' , end='')
    for x in users:
      name = x['name']
      print( '|' , f'{name:<15}' , end='')
    print('\n---------------------------------------------------------------------------------')

    for x in priceList:
      symbol = x['symbol']
      price = x['price']
      brlprice = float(price) * float(brlvalue['high'])


      print(f'{symbol:<15}', f'${price:<18}' , f'R${brlprice:<18}'[:20] ,  sep='|  ' , end='')

      for x in users:
        try:
          coins = str(x['coins'][symbol])
          print( '|' , f'{coins:<15}' , end='')
        except Exception:
          pass
          
      print()
      print('---------------------------------------------------------------------------------')

    time.sleep(1)
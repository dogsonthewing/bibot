#anotações

from binance.spot import Spot 

client = Spot()

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
client = Spot(key='', secret='')

# Get account and balance information
print(client.account())



#----------------------
import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

spot_client = Client(key, secret)
logging.info(spot_client.mining_coin_list())

#----------

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

spot_client = Client(base_url="https://testnet.binance.vision")

logging.info(spot_client.avg_price("SHIBBUSD"))



#----

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

spot_client = Client(base_url="https://testnet.binance.vision")

logging.info(spot_client.avg_price())


key = ""
secret = ""
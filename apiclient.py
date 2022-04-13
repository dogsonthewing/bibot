#import os permite que eu pegue a chave de dentro da máquina
import os
import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging


key = os.environ['binance_api']
secret = os.environ['binance_secret']

client = Client(key, secret)
client.API_URL = 'https://api.binance.com'

config_logging(logging, logging.DEBUG)

spot_client = Client(key, secret)
logging.info(spot_client.avg_price("SHIBBUSD"))

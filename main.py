import logging
from dotenv import dotenv_values
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


config = dotenv_values(".env")

BASE_URL = config["BASE_URL"]
KEY = config["API_KEY"]
SECRET = config["SECRET_KEY"]


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':
    binance = BinanceFuturesClient(KEY, SECRET, True)
    bitmex = BitmexClient("", "", True)

    root = Root(binance, bitmex)
    root.mainloop()


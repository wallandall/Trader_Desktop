import tkinter as tk
import logging
from dotenv import dotenv_values
from connectors.binance import get_contracts


config = dotenv_values(".env")

BASE_URL = config["BASE_URL"]
KEY = config["API_KEY"]
SECRET = config["SECRET_KEY"]


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s :: %(message)s")
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance_contracts = get_contracts()

    root = tk.Tk()
    root.configure(bg='gray12')

    i = 0
    j = 0

    calibri_font = ("Calibri", 11, "normal")

    for contract in binance_contracts:
        label_widget = tk.Label(root, text=contract, bg='gray12', fg='SteelBlue1', width=13, font=calibri_font)
        label_widget.grid(row=i, column=j, sticky='ew')

        if i == 4:
            j += 1
            i = 0
        else:
            i += 1

    root.mainloop()

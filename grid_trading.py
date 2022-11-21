from crypt import crypt
from curses import use_default_colors
import numpy as np
import pandas as pd
import yfinance as yf


data = yf.download(
    tickers="ETH-USD", start="2022-01-01", end="2022-11-01", interval="1h"
)


prices = data["Adj Close"]

prices


fiat = 1000
grids = 3
percentage = 0.1

market_prices = [1000, 1100, 1000, 900, 800, 700, 600, 700, 800]

g = np.arange(3) + 1
upper = boundaries = g * percentage
lower = boundaries = (g * (-1)) * percentage
upper, lower

boundaries = np.append(lower, upper)

fiat - (boundaries * fiat)


crypto_wallet = 0.0
fiat_wallet = 1000


def buy(price, fiat):
    global crypto_wallet
    global fiat_wallet
    price = 1100
    investment = fiat / 3
    fiat_wallet = fiat_wallet - investment

    crypto_wallet = crypto_wallet + (investment / price)
    print(f"add {eth_amount} ETH")


buy(1100, fiat_wallet)


def sell(price, fiat):
    global crypto_wallet
    global fiat_wallet
    fiat = crypto_wallet * price
    crypto_wallet = crypto_wallet - crypto_wallet
    fiat_wallet = fiat_wallet + fiat
    print(f"add fiat {fiat} USD")


sell(1300, fiat_wallet)

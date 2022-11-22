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
buy_grid = 3
sell_grid = 0

sales_price = []


def buy(price):
    global crypto_wallet
    global fiat_wallet
    global buy_grid
    global sell_grid
    global sales_price

    if buy_grid == 0:
        print("No money for trade")
        return

    investment = fiat / buy_grid
    fiat_wallet = fiat_wallet - investment
    buy_grid = buy_grid - 1
    sell_grid = sell_grid + 1
    crypto_wallet = crypto_wallet + (investment / price)
    sales_price.append(price)
    print(
        f"add {(investment / price)} ETH, money amount {fiat_wallet}, eth amnount {crypto_wallet}, buy grid {buy_grid} , sell grid {sell_grid}"
    )


def sell(price):
    global crypto_wallet
    global fiat_wallet
    global buy_grid
    global sell_grid
    global sales_price

    if sell_grid == 0:
        print("Nothing to sell")
        return

    fiat = (crypto_wallet / sell_grid) * price
    crypto_wallet = crypto_wallet - crypto_wallet / sell_grid
    fiat_wallet = fiat_wallet + fiat
    buy_grid = buy_grid + 1
    sell_grid = sell_grid - 1

    sales_price.append(price)
    print(
        f"add fiat {fiat} USD, money amount {fiat_wallet}, eth amnount {crypto_wallet}, buy grid {buy_grid} , sell grid {sell_grid}"
    )


buy(800)

sell(1100)

market_price = 1000


if market_price >= min(sales_price) -  min(sales_price)*percentage:
    print('sell')
elif market_price <= max(sales_price) + max(sales_price)*percentage:
    print('buy')
else:
    print('no action')


sales_price

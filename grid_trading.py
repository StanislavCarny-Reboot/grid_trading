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
transactions = [1000]

def buy(price):
    global crypto_wallet
    global fiat_wallet
    global buy_grid
    global sell_grid
    global sales_price

    if buy_grid == 0:
        print("No money for trade")
        return

    investment = fiat_wallet / buy_grid
    fiat_wallet = fiat_wallet - investment
    buy_grid = buy_grid - 1
    sell_grid = sell_grid + 1
    crypto_wallet = crypto_wallet + (investment / price)
    sales_price.append(price)
    global transactions
    transactions.append(fiat_wallet)

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
    transactions.append(fiat_wallet)

    # sales_price.append(price)
    print(
        f"add fiat {fiat} USD, money amount {fiat_wallet}, eth amnount {crypto_wallet}, buy grid {buy_grid} , sell grid {sell_grid}"
    )


    
sales_price =[1000]

crypto_wallet = 0.0
fiat_wallet = 1000
buy_grid = 3
sell_grid = 0

#sales_price = []

fiat_wallet=1000

def make_transaction(market_price,sales_price,percentage):

    if market_price >= min(sales_price) +  max(sales_price)*percentage:
        sell(market_price)
        sales_index = sales_price.index(max(sales_price))
        sales_price.pop(sales_index)
        print('sell')
    elif market_price <= min(sales_price) - min(sales_price)*percentage:
        buy(market_price)
        print('buy')
    else:
        print('no action')

price=[1000,900,800,800,900,1000,1100,1200,1300]

for i in price:
    make_transaction(i,sales_price=[1500],percentage=0.10)

fiat_wallet

import matplotlib.pyplot as plt

graph = pd.DataFrame(zip(price,transactions))

graph.plot()
plt.show()


sorted_prices = prices.sort_values()

transactions=[1000]

crypto_wallet = 0.0
fiat_wallet = 1000
buy_grid = 10
sell_grid = 0

for i in sorted_prices:
    make_transaction(i,sales_price=[2000],percentage=0.01)


graph = pd.DataFrame(zip(transactions))

graph.plot(marker='o')
plt.show()

transactions

fiat_wallet

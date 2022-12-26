
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

crypto_wallet = 0.0
fiat_wallet = 1000
buy_grid = 1
sell_grid = 0

starting_money = fiat_wallet

sales_price = []
transactions = []

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


def make_transaction(market_price,percentage):
    global sales_price

    if sales_price == []:
        sales_price = [market_price]

    print(f'sales_price: {sales_price}')
    sell_test = (min(sales_price) +  (min(sales_price)*percentage))
    buy_test = (min(sales_price) - (min(sales_price)*percentage))
    if market_price >= (min(sales_price) +  (min(sales_price)*percentage)):
        sell(market_price)
        sales_index = sales_price.index(min(sales_price))
        sales_price.pop(sales_index)
        print(f"Market_price{market_price}")
        print(f"Sell_test{sell_test}")
        print('sell')
    elif market_price <= (min(sales_price) - (min(sales_price)*percentage)):
        buy(market_price)
        print('buy')
        print(f"Market_price: {market_price}")
        print(f"Buy_test: {buy_test}")
    else:
        print('no action')



def grid_trading(money,grids,percentage,y1):
    global transactions
    global fiat_wallet
    global buy_grid
    global sell_grid
    global sales_price
    global crypto_wallet



    crypto_wallet = 0.0
    fiat_wallet = money
    buy_grid = grids
    sell_grid = 0
    transactions = []
    sales_price = []


    for i in y1:
        make_transaction(i,percentage=percentage)

    final_return = fiat_wallet - starting_money
    return final_return




data = yf.download(
    tickers="ETH-USD", start="2022-12-01", end="2022-12-31", interval="1h"
)

# est_data = data.tail(1000)

prices = data["Adj Close"]





grid_range = np.arange(1,21,1)
percentage_range = [0.01,0.001,0.0001,0.000001]


final_obj = []
for g in grid_range:
    for p in percentage_range:
        money_return = grid_trading(10000,g,p,prices)
        temp_obj = {'return':money_return,'grid':g,'percentage':p}
        final_obj.append(temp_obj)
        

final_obj
 

# To return a new list, use the sorted() built-in function...
sorted = sorted(final_obj, key=lambda x: x['return'], reverse=True)
best_params = sorted[0]
best_params 




grid_trading(10000,20,0.01,prices)


100*'green'


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import dash_daq as daq
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import yfinance as yf


crypto_wallet = 0.0
fiat_wallet = 1000
buy_grid = 10
sell_grid = 0
transactions = []
sales_price = []
starting_money = fiat_wallet




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

    if market_price >= min(sales_price) +  min(sales_price)*percentage:
        sell(market_price)
        sales_index = sales_price.index(min(sales_price))
        sales_price.pop(sales_index)
        print('sell')
    elif market_price <= min(sales_price) - min(sales_price)*percentage:
        buy(market_price)
        print('buy')
    else:
        print('no action')



data = yf.download(
    tickers="ETH-USD", start="2022-12-14", end="2022-12-31", interval="1h"
)



x = data.index
y1 = data["Adj Close"]

for i in y1:
    make_transaction(i,percentage=0.000001)


def return_figure(x,y_trace1,y_trace2):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y_trace1,
        name = 'ETH Price', 
        connectgaps=True
    ))
    fig.add_trace(go.Scatter(
        x=x,
        y=y_trace2,
        name='Transactions',
        line = dict(color='darkgrey')
    )),
    fig.update_layout(yaxis_type = "log")

    return fig







app = Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Grid Trading'),

        daq.NumericInput(
        id='money',
        value=0,
        max=10000000,
        label='Money:',
        labelPosition='top',
        size=120
    ),


        daq.NumericInput(
        id='grids',
        value=0,
        max=1000,
        min=1,
        label='# Grids:',
        labelPosition='top',
        size=120,
    ),


        daq.NumericInput(
        id='percentage',
        value=0,
        max=100,
        min=0.00001,
        label='Percentage:',
        labelPosition='top',
        size=120
    ),
    html.Center([
    html.H2(id="profit",children='1000 EUR'),
    html.Button('Submit', id='submit-val', n_clicks=0)
    ]
    ),

dcc.Graph(id='scatter')

])

@app.callback(
    Output('scatter', 'figure'),
    Output('profit', 'children'),
    Input('submit-val', 'n_clicks'),
    State('money','value'),
    State('grids','value'),
    State('percentage','value'),
)

def update_figure(n_clicks, money,grids,percentage):
    global transactions
    global fiat_wallet
    global buy_grid
    global sell_grid
    global sales_price
    global crypto_wallet
    starting_money = 0
    profit = 0
    


    if n_clicks >0:
    
        crypto_wallet = 0.0
        fiat_wallet = money
        buy_grid = grids
        sell_grid = 0
        transactions = []
        sales_price = []
        starting_money = fiat_wallet
        profit



        for i in y1:
            make_transaction(i,percentage=percentage)

    profit = fiat_wallet - starting_money
    print(profit, starting_money, fiat_wallet)

    return return_figure(x,y1,transactions),profit

if __name__ == '__main__':
    app.run_server(debug=True)

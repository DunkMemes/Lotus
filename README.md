# Lotus - a fast an effective trading bot

## Installation:
Modules:
alpaca_trade_api: pip3 install alpaca_trade-api
pandas: pip3 intall pandas
dotnev: pip3 install python-dotnev

## Funtions:
### Buying & Selling:
As of now Lotus can only buy and sell manually via an user input.
***buy:***
Params:
- int quantity: number of stocks to buy.
- str stock: defines the stock to buy. ex: 'MNST' or 'GME'

***sell:***
Params:
- int quantity: number of stocks to sell.
- str stock: defines the stoc to sell.

### Collecting usefull data
Lotus can return a plephora of information to the user.
***get_user:***
returns the complete account data for the user.
***get_cash:***
returns the cash left on the account.
***get_equity_***
returns the value of the portfolio.
***get_diff:***
returns the profits or losses of the portfolio.
***get_all_orders:***
returns a list, containing the last submitted orders, the user can choose how many orders he wants returned with the parameter 'quantity'.

## To-Do:
1. implement the logic for the strategy
2. clean up the returned data for orders and user
3. make a nice dashboard that shows: Graph with equity, cash, order history
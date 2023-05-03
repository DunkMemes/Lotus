## Methods:
***__init__(self):*** Initializes the lotus object, including loading API credentials from environment variables and creating a new instance of the Alpaca REST API.
***get_user(self):*** Returns all available account data as a JSON object.
***get_cash(self):*** Returns the amount of cash in the account.
***get_equity(self):*** Returns the portfolio value.
***get_last_equity(self):*** Returns the portfolio value from the last trading day.
***get_diff(self):*** Returns the difference between the portfolio value and an initial value of $100,000.
***get_position(self, stock):*** Returns information about the current position in the specified stock.
***get_all_positions(self):*** Returns a list of all positions held in the account.
***get_stock_value(self, stock):*** Returns the latest market price of the specified stock.
***get_portfolio_daily(self):*** Returns a Pandas DataFrame containing daily equity data for the account's portfolio.
***get_portfolio_hourly(self):*** Returns a Pandas DataFrame containing hourly equity data for the account's portfolio.
***get_portfolio_max(self):*** Returns a Pandas DataFrame containing maximum equity data for the account's portfolio.
***get_all_orders(self, quantity, st):*** Returns information about the last quantity orders, filtered by status st.
***check_market_availability(self):*** Returns True if the market is currently open, False otherwise.
***buy(self, quantity, stock):*** Submits a market buy order for the specified quantity of the specified stock.
***sell(self, quantity, stock):*** Submits a market sell order for the specified quantity of the specified stock.
***movingAverageStrategy(self, stock, timeframe, short_window, long_window, buy_qty):*** Implements a moving average trading strategy for the specified stock, using a short window and a long window to calculate moving averages. Returns a string indicating the action taken (e.g., "buying 100 shares of stock AAPL").
***buy_or_sell(self, target, stock):*** Compares the current position in the specified stock to a target position, and submits a buy or sell order to bring the position to the target. If the position is already at the target, does nothing.

## Dependencies:

- datetime
- random
- dotenv
- alpaca_trade_api
- pandas
- os
- plotly
- json

## Simple Sequence Diagrams:
### buy()
```console
user -> lotus: calls buy(quantity, stock)
lotus -> alpaca_trade_api: submit_order(symbol, quantity, 'buy', 'market', 'day')
alpaca_trade_api -> lotus: returns current_order
lotus -> user: returns confirmation message
```
### sell()
```console
user -> lotus: calls sell(quantity, stock)
lotus -> alpaca_trade_api: submit_order(symbol, quantity, 'sell', 'market', 'day')
alpaca_trade_api -> lotus: returns current_order
lotus -> user: returns confirmation message
```
### get_all_orders()
```console
user -> lotus: calls get_all_orders(quantity, status)
lotus -> alpaca_trade_api: list_orders(status, until, direction, limit, nested)
alpaca_trade_api -> lotus: returns list of orders
lotus -> pandas: create DataFrame from order data
pandas -> lotus: returns DataFrame
lotus -> user: returns DataFrame with order information
```
### MovingAverageStrategy()
```console
user -> lotus: calls movingAverageStrategy(stock, timeframe, short_window, long_window, buy_qty)
lotus -> alpaca_trade_api: check_market_availability()
alpaca_trade_api -> lotus: returns boolean
alt availability is true
lotus -> alpaca_trade_api: get_bars(stock, timeframe, start, limit)
alpaca_trade_api -> lotus: returns barset
lotus -> pandas: create DataFrame from bar data
pandas -> lotus: returns DataFrame
lotus -> pandas: calculate short moving average
pandas -> lotus: returns short moving average
lotus -> pandas: calculate long moving average
pandas -> lotus: returns long moving average
alt short moving average is greater than long moving average and was previously less than or equal to it
lotus -> lotus: calls buy(quantity, stock)
alt short moving average is less than long moving average and was previously greater than or equal to it
lotus -> lotus: calls sell(quantity, stock)
else
lotus -> user: returns message stating to wait for next trade cycle
```
### buy_or_sell()
```console
user -> lotus: calls buy_or_sell(target, stock)
lotus -> alpaca_trade_api: get_position(stock)
alpaca_trade_api -> lotus: returns position information
alt position is 0
lotus -> user: returns message stating there are no stocks to trade
alt target is greater than position
lotus -> lotus: calls buy(target - position, stock)
lotus -> user: returns confirmation message for the buy order
else
lotus -> lotus: calls sell(position - target, stock)
lotus -> user: returns confirmation message for the sell order
```
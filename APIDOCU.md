# Methods:
***__init__(self):*** 
Initializes the lotus object, including loading API credentials from environment variables and creating a new instance of the Alpaca REST API.

***get_user(self):*** 
Returns all available account data as a JSON object.

***get_cash(self):*** 
Returns the amount of cash in the account.

***get_equity(self):*** 
Returns the portfolio value.
***get_last_equity(self):*** 
Returns the portfolio value from the last trading day.

***get_diff(self):*** 
Returns the difference between the portfolio value and an initial value of $100,000.

***get_position(self, stock):*** 
Returns information about the current position in the specified stock.

***get_all_positions(self):*** 
Returns a list of all positions held in the account.

***get_stock_value(self, stock):*** 
Returns the latest market price of the specified stock.

***get_portfolio_daily(self):*** 
Returns a Pandas DataFrame containing daily equity data for the account's portfolio.

***get_portfolio_hourly(self):*** 
Returns a Pandas DataFrame containing hourly equity data for the account's portfolio.

***get_portfolio_max(self):*** 
Returns a Pandas DataFrame containing maximum equity data for the account's portfolio.

***get_all_orders(self, quantity, st):*** 
Returns information about the last quantity orders, filtered by status st.

***check_market_availability(self):*** 
Returns True if the market is currently open, False otherwise.

***buy(self, quantity, stock):*** 
Submits a market buy order for the specified quantity of the specified stock.

***sell(self, quantity, stock):*** 
Submits a market sell order for the specified quantity of the specified stock.

***movingAverageStrategy(self, stock, timeframe, short_window, long_window, buy_qty):*** 
Implements a moving average trading strategy for the specified stock, using a short window and a long window to calculate moving averages. Returns a string indicating the action taken (e.g., "buying 100 shares of stock AAPL").

***buy_or_sell(self, target, stock):*** 
Compares the current position in the specified stock to a target position, and submits a buy or sell order to bring the position to the target. If the position is already at the target, does nothing.

# Dependencies:

- datetime
- random
- dotenv
- alpaca_trade_api
- pandas
- os
- plotly
- json

# Simple Sequence Diagrams:
## buy()
<p>
  <img src="https://github.com/DunkMemes/Lotus/blob/master/seqDia/buy().png?raw=true" />
</p>

## sell()
<p>
  <img src="https://github.com/DunkMemes/Lotus/blob/master/seqDia/sell().png?raw=true" />
</p>

## get_all_orders()
<p>
  <img src="https://github.com/DunkMemes/Lotus/blob/master/seqDia/get_all_orders().png?raw=true" />
</p>

## MovingAverageStrategy()
<p>
  <img src="https://github.com/DunkMemes/Lotus/blob/master/seqDia/movingAverageStrategy().png?raw=true" />
</p>

## buy_or_sell()
<p>
  <img src="https://github.com/DunkMemes/Lotus/blob/master/seqDia/buy_and_sell().png?raw=true" />
</p>
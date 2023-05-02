import datetime
import random
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import pandas as pd
import os
import plotly as pl
import json as js


class lotus(object):
    def __init__(self):
        load_dotenv()
        self.key = os.getenv("API_KEY")
        self.secret = os.getenv("API_SECRET")
        self.endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.endpoint)
        self.current_order = None

    def get_user(self):
        """returns all available account data as a json"""
        return self.api.get_account()

    def get_cash(self):
        """returns the cash on the account"""
        return self.api.get_account().cash

    def get_equity(self):
        """returns the portfolio value"""
        return self.api.get_account().equity

    def get_last_equity(self):
        """returns the portfolio value"""
        return self.api.get_account().last_equity

    def get_diff(self):
        """returns profit/loss"""
        diff = float(self.get_equity()) - 100000
        return round(diff, 2)

    def get_position(self, stock):
        return self.api.get_position(stock)

    def get_all_positions(self):
        return self.api.list_positions()

    def get_stock_value(self, stock):
        price = self.api.get_latest_bar(stock).c
        date = self.api.get_latest_bar(stock).t
        clean_date = date.strftime('%d/%m/%Y')
        return "{}, {}".format(price, clean_date)

    def get_portfolio_daily(self):
        return self.api.get_portfolio_history().equity

    def get_portfolio_hourly(self):
        return self.api.get_portfolio_history(period="1D", timeframe="1H").equity

    def get_portfolio_max(self):
        return self.api.get_portfolio_history(period="365D", timeframe="1D").equity

    def get_all_orders(self, quantity, st):
        """returns the last orders, user can set how many are to be returned"""
        check_for_more = True
        all_orders = []
        time = pd.to_datetime('now', utc=True).isoformat()
        while check_for_more:
            api_orders = self.api.list_orders(status=st,
                                              until=time,
                                              direction='desc',
                                              limit=quantity,
                                              nested=False)
            all_orders.extend(api_orders)

            if len(api_orders) == quantity:
                time = all_orders[-1].submitted_at

            else:
                check_for_more = False
            orders_df = pd.DataFrame([order._raw for order in all_orders])
            orders_df.drop_duplicates('id', inplace=True)
            if orders_df is not None:
                dt = orders_df[["symbol", "qty", "filled_avg_price", "status"]]
                return dt
            else:
                return None

    def check_market_availability(self):
        now = datetime.datetime.now()
        opening = now.replace(hour=15, minute=30, second=0, microsecond=0)
        closing = now.replace(hour=22, minute=0, second=0, microsecond=0)
        if opening < now < closing:
            return True
        else:
            return False

    def buy(self, quantity, stock):
        self.symbol = stock
        self.current_order = self.api.submit_order(self.symbol,
                                                   quantity,
                                                   'buy',
                                                   'market',
                                                   'day')

    def sell(self, quantity, stock):
        self.symbol = stock
        self.current_order = self.api.submit_order(self.symbol,
                                                   quantity,
                                                   'sell',
                                                   'market',
                                                   'day')

    def movingAverageStrategy(self, stock, timeframe,
                              short_window, long_window, buy_qty):
        """uses the moving average strategy to trade stocks
            params:
            stock: str
            timeframe: str
            short_window: int
            long_window: int
        """
        if self.check_market_availability() is True:
            if timeframe == "1D":
                ago = datetime.date.today() - datetime.timedelta(days=long_window)
            elif timeframe == "1H":
                ago = datetime.date.today() - datetime.timedelta(hours=long_window)
            barset = self.api.get_bars(stock,
                                       timeframe,
                                       start=ago,
                                       limit=long_window+1)
            bars = []
            for x in barset:
                bars.append(x._raw)

            c = {'t': [], 'c': []}
            df = pd.DataFrame(bars, columns=c)
            
            short_ma = df['c'].rolling(short_window).mean()
            long_ma = df['c'].rolling(len(df)-1).mean()

            if short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]:
                self.buy(buy_qty, stock)
                return f'buying {qty} shares of stock {stock}'
            elif short_ma.iloc[-1] < long_ma.iloc[-1] and short_ma.iloc[-2] >= long_ma.iloc[-2]:
                try:
                    qty = int(self.get_position(stock).qty)
                    self.sell(qty, stock)
                except:
                    print(f"There are no {stock} stocks to trade!")
                return f'selling {qty} shares of stock {stock}'
            else:
                return f'Waiting for next trade cycle'
        else:
            return "Market is closed at the moment"

    def buy_or_sell(self, target, stock):

        self.position = int(self.api.get_position(stock).qty)

        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)

        change = target - self.position
        buy_quantity = abs(change)
        if change > 0:
            if self.position < 0:
                buy_quantity = min(abs(self.position), buy_quantity)
            print(f'buying {buy_quantity} shares of {stock}')
            self.current_order = self.api.submit_order(stock,
                                                       buy_quantity,
                                                       'buy', 'market', 'day')

        elif change < 0:
            sell_quantity = abs(change)
            if self.position > 0:
                sell_quantity = min(abs(self.position), sell_quantity)
            print(f'selling {sell_quantity} shares of {stock}')
            self.current_order = self.api.submit_order(stock,
                                                       sell_quantity,
                                                       'sell', 'market', 'day')


if __name__ == "__main__":
    lot = lotus()
    lot.movingAverageStrategy('TSLA', "1D", 1, 6, 10)

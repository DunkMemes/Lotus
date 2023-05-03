# Lotus

<p align="center">
  <img src="https://github.com/DunkMemes/Lotus/blob/master/logo.png?raw=true" />
</p>

Welcome to the Lotus ReadME!
This Project is a simple web-based stock trading bot for automatic and manual trading. Lotus has a lot of features, but there are nearly unlimited possibilities to continue development.

The Project is written in Python. It uses the Alpaca-trade-api to connect to the stock market and Streamlit to deliver a simple, yet fully functional interface.

As of now Lotus is only intended to be used with a paper trading account.

## Installation:
Before you can use Lotus you have to install the necessary modules with the command: 
```console
pip3 install -r requirements.txt
```
Further it is required to have an Alpaca-account. This account gives you access to the `API_KEY` and `API_SECRET`. 
You can create an account here: https://app.alpaca.markets/signup

To use your `API_KEY` and `API_SECRET` simply create an `.env` file and insert them like this:
```cosole
API_KEY='your key'
API_SECRET='your secret'
```
## How to start Lotus:
To start Lotus you simply have to open the terminal run the command: 
```console
streamlit run .\Home.py
```

## Pages:
The Lotus Bot offers plenty of pages to the User.
### Dashboard:
The Dasboard offers a quick overview over your portfolio and your positions.
### Mailer:
The mailer offers the user the possibility to enter their email address and receive daily updates about the status about their portfolio.
- ***Your E-Mail-Address***: The e-mail-address to which Lotus will send the daily updates to.
***Disclaimer***: Lotus will send daily updates as long as it is running. After Lotus has been restarted the user has to enter their e-mail-address again.
### Manual Trading:
Enables the user to manually trade stocks by simply entering the symbol and a quantity.
- ***Stock***: The stock the user wants to buy or sell.
- ***Quantity***: The quantity of stocks the user wants to buy or sell.
### Moving Average:
Lotus offers the possibility of automated trading. For this purpose we chose the `Moving Average Strategy`.
The user can start the automatic trading with the strategy from this page. It offers dropdowns and inputs to customize the trading.
- ***stock***: The stock the user wants to trade
- ***buy quantity***: If there are no positions for the chosen stock, Lotus will buy this quantity with the next buy signal
- ***How often would you like to trade?***: Dropdown which lets the user choose how often they want Lotus check the market and make a trade
- ***Select the timeframe for your data***: The user can select the timeframe from which Lotus gathers its data.
### Orders:
Gives the user an overview of the last orders. They can be filtered by quantity, open, closed, all and max.
- ***quantity***: The user can choose how many orders they want to see via the input field
- ***open***: Oders that have not been fulfilled
- ***closed***: All fulfilled orders
- ***all***: Open and closed orders
- ***max***: Displays all orders ever taken
----------------------------------
This project was developed for the webdevelopment course by:
- Andrii Zolotov
- Jan Röderer
- Marco Binder
- David Hentschel
---------------------------------
### Documentation
You can find the documentation under this link: https://github.com/DunkMemes/Lotus/blob/master/APIDOCU.md
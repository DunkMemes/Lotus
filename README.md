# Lotus - a fast an effective trading bot

## Installation:
Install the neccessary modules with the command: pip3 install -r requirements.txt

## How to start Lotus:
To start Lotus you simply have to open the terminal in the "SCP-6488"-Folder and run the command: streamlit run .\Home.py

## Pages:
The Lotus Bot offers a plephora of pages to the User.
### Dashboard:
The Dasboard offers a quick overview over you portfolio and your positions.
### Mailer:
The mailer offers the user the possibility to enter their email address and receive daily updates about the status about their portfolio. As long as Lotus runs it will send out the emails, if Lotus shuts down the user will have to enter their email again.
### Manual Trading:
Enables the user to manually trade stocks by simply entering the symbol and a quantity.
### Moving Average:
The user can start the continuous trading with the strategy from this page. It offer dropdowns and inputs to customize the trading.
### Orders:
Gives the user an overview of the last orders. They can be filtered by quantity, open, closed, all and max.
- quantity: the user can choose how many orders they want to see via the input field
- open: are oders that have not been fulfilled
- closed: all fulfilled orders
- all: open and closed orders
- max: displays all orders taken
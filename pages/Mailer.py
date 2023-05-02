from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import time
import pandas as pd
from api import lotus
import streamlit as st
import threading
import datetime
from plotly.offline import plot
import plotly.graph_objects as go
from IPython.display import Image


def mailer_page():
  rec = st.text_input("Your E-Mail adress:")
  now = datetime.datetime.now()
  run_time = now.replace(hour=22, minute=00, second=0, microsecond=0)
  if st.button("I want to receive E-Mails!"):
    if rec != "":
      while True:
        remaining = (run_time - datetime.datetime.now()).total_seconds()
        if remaining < 0:
            tom = run_time + datetime.timedelta(days=1)
            remaining = (tom - datetime.datetime.now()).total_seconds()
            print(f"waiting for {remaining} seks")
            time.sleep(remaining)
            t1 = threading.Thread(send(rec))
            print("Email sent!")
            t1.start()
        elif remaining > 0:
            print(f"waiting for {remaining} seks")
            time.sleep(remaining)
            t1 = threading.Thread(send(rec))
            print("Email sent!")
            t1.start()


def send(rec):
    lot = lotus()
    sender = 'lotus.trading.bot@gmail.com'
    password = 'dxjllaccwjrzddvj'
    to = rec
    positions = lot.get_all_positions()

    labels = []
    values = []
    for position in positions:
        labels.append(position.symbol)
        values.append(float(position.current_price) * float(position.qty))

    total_equity = lot.get_equity()
    total_profit = lot.get_diff()

    colors = ['#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B']

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        hole=0.7,
        marker=dict(colors=colors),
        textinfo='label+percent',
        textfont=dict(size=15)
    ))

    fig.add_annotation(
        text=f"Total Equity: {total_equity} $<br>Total Profit: {total_profit} $",
        font=dict(size=16),
        showarrow=False
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1.1,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='#F7F7F7'
    )
    fig.write_image("pages/images/newplot.png")
    positionsTable = pd.DataFrame(columns=["Symbol", "Amount", "Value", "Performance %"])

    for position in positions:
        symbol = position.symbol
        amount = int(position.qty)
        price = float(position.current_price)
        value = amount * price
        performance = float(position.unrealized_plpc) * 100

        positionsTable.loc[len(positionsTable)] = [symbol, amount, value, performance]

    positionsTable["Performance %"] = positionsTable["Performance %"].astype(float)

    subject = 'Your daily update from the Lotus Trading Bot!'
    msg = MIMEMultipart()
    html = """\
    <html>
    <head></head>
      <body>
        <h2>Your Equity: {0}$</h2>
        <h2>Your Profit: {1}$</h2>
        <h2>Your Positions:</h2>
        {2}
        <h2>Your Portfolio:</h2>
        <p>You can find it in the attachements!</p>
      </body>
    </html>
    """.format(lot.get_equity(), lot.get_diff(), positionsTable.to_html())

    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    with open('pages/images/newplot.png', 'rb') as fp:
      img = MIMEImage(fp.read())
      img.add_header('Content-Disposition', 'attachment', filename="Portfolio.png")
    msg.attach(img)
    msg['Subject'] = subject

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, to, msg.as_string())


mailer_page()

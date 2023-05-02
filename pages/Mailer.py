import smtplib
import ssl
from email.message import EmailMessage
import time
from api import lotus
import streamlit as st
import threading
import datetime
import schedule



def mailer_page():
  rec = st.text_input("Your E-Mail adress:")
  now = datetime.datetime.now()
  run_time = now.replace(hour=16, minute=30, second=0, microsecond=0)
  if st.button("I want to receive E-Mails!"):
    if rec != "":
      while True:
        remaining = (run_time - datetime.datetime.now()).total_seconds()
        if remaining < 0:
          remaining = run_time + datetime.timedelta(days=1)
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

  subject = 'Your daily update from the Lotus Trading Bot!'
  body = f"""
  Your Equity: {lot.get_equity()} $
  Your Profit: {lot.get_diff()} $
  Your Positions: 12 $
  """

  email = EmailMessage()
  email['From'] = sender
  email['To'] = to
  email['Subject'] = subject
  email.set_content(body)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, to, email.as_string())

mailer_page()
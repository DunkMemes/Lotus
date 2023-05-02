import threading
import time
import streamlit as st
from api import lotus


def pageMV():
    st.title("Moving Average Strategy")
    st.subheader("Customizing you trading strategy")
    running = False
    stock = st.text_input("Stock:")
    buy = st.number_input("Buy Quantity:")
    times = st.selectbox("How often would you like to trade?"
                 , ("Every 15 min", "Every 1 hour", "Every 24 hours"))
    if times == "Every 15 min":
        tt = 20
    elif times == "Every 1 hour":
        tt = 3600
    elif times == "Every 24 hours":
        tt = 86000

    dataTime = st.selectbox("Select the timeframe for your data"
                 , ("Last 24 hours", "Last 7 days", "Last 30 days"))

    if dataTime == "Last 24 hours":
        sw = 1
        lw = 23
        tf = "1H"
    elif dataTime == "Last 7 days":
        sw = 1
        lw = 6
        tf = "1D"
    elif dataTime == "Last 30 days":
        sw = 1
        lw = 29
        tf = "1D"

    def trade(tt):
        print(lotus.movingAverageStrategy(self=lotus(), stock=stock, timeframe=tf, short_window=sw, long_window=lw, buy_qty=buy))
        # st.experimental_rerun()

    col1, col2 = st.columns(2)
    counter = 0
    placeholder = st.empty()
    startButton = st.button("Start")
    stopButton = st.button("Stop", key=counter)
    # placeholder.button("Stop", key=counter)
    with col1:
        if startButton:
            if stock == "":
                st.warning("Please enter a stock first!")
            if tt is None:
                st.warning("Please customize your strategy first!")
            elif stock != "":
                running = 1
            while running == 1:
                if stopButton:
                    running = 0
                    print("Stopping the process!")
                    st.experimental_rerun()
                elif running == 1:
                    time.sleep(tt)
                    counter += 1
                    t1 = threading.Thread(trade(tt))
                    t1.start()


pageMV()

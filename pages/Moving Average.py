from threading import Thread, Event
import time
import streamlit as st
from api import lotus


def pageMV():
    st.title("Moving Average Strategy")
    st.subheader("Customizing you trading strategy")
    stock = st.text_input("Stock:")
    buy = st.number_input("Buy Quantity:")
    times = st.selectbox("How often would you like to trade?"
                         , ("Every 15 min", "Every 1 hour", "Every 24 hours"))
    if times == "Every 15 min":
        tt = 5
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

    def trade():
        print(lotus.movingAverageStrategy(self=lotus(), stock=stock, timeframe=tf, short_window=sw, long_window=lw,
                                          buy_qty=buy))

    col1, col2 = st.columns(2)
    counter = 0
    placeholder = st.empty()

    def start_trading(event: Event, counter: int, tt: int) -> None:
        if stock == "":
            st.warning("Please enter a stock first!")
        if tt is None:
            st.warning("Please customize your strategy first!")
        elif stock != "":
            while True:
                trade()
                time.sleep(tt)
                counter += 1
                time.sleep(3)
                if event.is_set():
                    print("Stopping the process from the start_trading!")
                    break

    event = Event()
    thread = Thread(target=start_trading, args=(event, counter, tt,))

    def set_event():
        event.set()

    with col1:
        if st.button("Start"):
            thread.start()

    with col2:
        st.button("Stop", on_click=set_event, key=counter)


pageMV()

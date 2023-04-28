import streamlit as st
from api import lotus

def pageMV():
    st.title("Moving Average Strategy")
    st.subheader("Customizing you trading strategy")
    running = False
    stock = st.text_input("Stock:")
    time = st.selectbox("How often would you like to trade?"
                 , ("Every 15 min", "Every 1 hour", "Every 24 hours"))
    if time == "Every 15 min":
        tt = 900
    elif time == "Every hour":
        tt = 3600
    elif time == "Once a day":
        tt = 86000

    dataTime = st.selectbox("Select the timeframe for your data"
                 , ("Last 24 hours", "Last 7 days", "Last 30 days"))
    if dataTime == "last 24 hours":
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
        while running:
            time.sleep(tt)
            if running is False:
                break
            else:
                lotus.movingAverageStrategy(stock, tf, sw, lw)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start"):
            if tt is None:
                st.warning("Please customize your strategy first!")
            else:
                running = True
                trade(tt)
    with col2:
        if st.button("Stop"):
            running = False

pageMV()
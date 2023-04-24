import streamlit as st
from api import lotus


def page_trading():
    lot = lotus()
    st.title("Trading")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Manual trading:")
        sym = st.text_input("Stock")
        qty = st.text_input("Quantity")
        ucol1, ucol2, ucol3 = st.columns(3)
        with ucol1:
            if st.button("Buy"):
                lot.buy(qty, sym)
        with ucol2:
            if st.button("Sell"):
                lot.sell(qty, sym)
    with col2:
        st.write("Our trading strategies:")
        st.button("MV-Average")
        st.button("Martingale")


page_trading()

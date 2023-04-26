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
    if len(sym) > 0:
        with col2:
            st.write("Stock price:")
            st.write(lot.api.get_latest_bar(sym).c)
            date = lot.api.get_latest_bar(sym).t
            clean_date = date.strftime('%d/%m/%Y')
            st.write("Price date:")
            st.write(clean_date)

    st.subheader("Our trading strategies:")
    col1, col2 = st.columns(2)
    with col1:
        st.button("MV-Average")
    with col2:
        st.button("Martingale")


page_trading()

import streamlit as st
from api import lotus


def page_trading():
    lot = lotus()
    st.markdown("<h1 style='color: #710000;'>Trading</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Manual trading:")
        st.write("You have :red[{0}$] to trade with!".format(lot.get_cash()))
        sym = st.text_input("Stock")
        qty = st.text_input("Quantity")
        ucol1, ucol2, ucol3 = st.columns(3)
        with ucol1:
            if st.button("Buy"):
                try:
                    lot.buy(qty, sym)
                except:
                    st.error("Not enough Cash!")
        with ucol2:
            if st.button("Sell"):
                lot.sell(qty, sym)
    if len(sym) > 0:
        with col2:
            st.write("Stock price:")
            price = float(lot.api.get_latest_bar(sym).c)
            st.write(f":red[{price}$]")
            date = lot.api.get_latest_bar(sym).t
            clean_date = date.strftime('%d/%m/%Y')
            st.write("Price date:")
            st.write(f":red[{clean_date}]")
            if qty != "":
                st.write("Total price:")
                st.write(f":red[{price * int(qty)}$]")


page_trading()

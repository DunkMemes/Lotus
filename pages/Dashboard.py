import streamlit as st
from api import lotus


def page_dasboard():
    lot = lotus()
    st.title("Lotus Trading Bot")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Cash:")
        st.write(lot.get_cash() + " $")
    with col2:
        st.write("Equity:")
        st.write(lot.get_equity() + " $")
    with col3:
        st.write("Profit:")
        if lot.get_diff() > 0:
            st.write(":green[{} $]".format(lot.get_diff()))
        if lot.get_diff() < 0:
            st.write(":red[{} $]".format(lot.get_diff()))
    st.write("Your postitions:")
    st.write(lot.get_position("MNST"))


page_dasboard()

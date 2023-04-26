import streamlit as st
import pandas as pd
import plotly.express as ple
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
    st.subheader("Portfolio:")
    ucol1, ucol2, ucol3 = st.columns(3)
    month = False
    day = False
    max = False
    with ucol1:
        if st.button("1M"):
            month = True
    with ucol2:
        if st.button("1D"):
            day = True
    with ucol3:
        if st.button("1Y"):
            max = True
    if month:
        pt = pd.DataFrame(lot.get_portfolio_daily())
        line = ple.line(pt)
        line
        month = False
    if day:
        pt = pd.DataFrame(lot.get_portfolio_hourly())
        line = ple.line(pt)
        line
        day = False
    if max:
        pt = pd.DataFrame(lot.get_portfolio_max())
        line = ple.line(pt)
        line
        max = False
    st.subheader("Your postitions:")
    positions = lot.get_all_positions()
    st.write(positions)


page_dasboard()

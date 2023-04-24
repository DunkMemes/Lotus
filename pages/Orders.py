import streamlit as st
from api import lotus


def page_orders():
    lot = lotus()
    orders = lot.get_all_orders(10)
    st.write("Your orders:")
    st.table(orders)


page_orders()

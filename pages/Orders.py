import streamlit as st
from api import lotus


def page_orders():
    lot = lotus()
    st.title(":red[Your orders:]")
    qty = st.text_input("Number of orders")
    sta = ""
    max = False
    all = False
    open = False
    closed = False
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Closed"):
            sta = "closed"
            closed = True
            orders = lot.get_all_orders(qty, sta)
    with col2:
        if st.button("Open"):
            sta = "open"
            open = True
            try:
                orders = lot.get_all_orders(qty, sta)
            except:
                st.error("No open orders!")
    with col3:
        if st.button("All"):
            sta = "all"
            all = True
            orders = lot.get_all_orders(qty, sta)
    with col4:
        if st.button("Max"):
            max = True
    if len(qty) > 0 and (all or closed or open):
        try:
            st.table(orders)
        except:
            ""
    if max:
        orders = lot.get_all_orders(10000, "all")
        st.table(orders)


page_orders()

import streamlit as st
import pandas as pd
import plotly.express as ple
from api import lotus
import plotly.graph_objects as go


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

    st.subheader("Your positions:")

    positions = lot.get_all_positions()

    labels = []
    values = []
    for position in positions:
        labels.append(position.symbol)
        values.append(float(position.current_price) * float(position.qty))

    colors = ['#0074D9', '#FF4136', '#2ECC40', '#FFDC00', '#AAAAAA', '#F012BE', '#FF851B']

    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        hole=0.7,
        marker=dict(colors=colors),
        textinfo='label+percent',
        textfont=dict(size=15)
    ))

    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1.1,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='#F7F7F7'
    )
    st.plotly_chart(fig)

    positionsTable = pd.DataFrame(columns=["Symbol", "Amount", "Value", "Performance %"])

    for position in positions:
        symbol = position.symbol
        amount = int(position.qty)
        price = float(position.current_price)
        value = amount * price
        performance = float(position.unrealized_plpc) * 100

        positionsTable.loc[len(positionsTable)] = [symbol, amount, value, performance]

    positionsTable["Performance %"] = positionsTable["Performance %"].astype(float)

    format_func = lambda x: f"{x:,.2f}"

    positionsTable = positionsTable.sort_values(by="Value", ascending=False).style \
        .applymap(lambda x: "color: red" if x <= 0 else "color: green", subset=["Performance %"]) \
        .format({
        "Value": format_func,
        "Performance %": format_func,
    }) \
        .set_properties(**{'font-weight': 'bold'}, subset=['Symbol']) \
        .set_table_styles([
        {
            'selector': 'th',
            'props': [
                ('font-size', '14px'),
                ('text-align', 'left'),
                ('padding', '6px'),
                ('background-color', '#F2F2F2'),
                ('color', '#333333'),
                ('border-bottom', '1px solid #273346'),
                ('border-right', '1px solid #273346'),
                ('border-left', '1px solid #273346'),
            ]
        },
        {
            'selector': 'td',
            'props': [
                ('font-size', '14px'),
                ('padding', '6px'),
                ('border-bottom', '1px solid #273346'),
                ('border-right', '1px solid #273346'),
                ('border-left', '1px solid #273346'),
            ]
        },
        {
            'selector': 'tbody tr:hover',
            'props': [('background-color', '#273346')]
        },
    ])
    st.table(positionsTable)
    hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

page_dasboard()

import streamlit as st
import pandas as pd
import plotly.express as ple
from api import lotus
import plotly.graph_objects as go

lot = lotus()

def page_dasboard():
    st.title("Portfolio")
    positions = lot.get_all_positions()

    labels = []
    values = []
    for position in positions:
        labels.append(position.symbol)
        values.append(float(position.current_price) * float(position.qty))

    total_equity = lot.get_equity()
    total_profit = lot.get_diff()

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

    fig.add_annotation(
        text=f"Total Equity: {total_equity} $<br>Total Profit: {total_profit} $",
        font=dict(size=16),
        showarrow=False
    )

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

    emptyCol, colDay, colMonth, colMax = st.columns([7, 1, 1, 1])

    pt_daily = pd.DataFrame(lot.get_portfolio_hourly())
    chart = ple.line(pt_daily)

    with emptyCol:
        pass
    with colDay:
        if st.button("1D"):
            pt = pd.DataFrame(lot.get_portfolio_hourly())
            chart = ple.line(pt)
    with colMonth:
        if st.button("1M"):
            pt = pd.DataFrame(lot.get_portfolio_daily())
            chart = ple.line(pt)
    with colMax:
        if st.button("Max"):
            pt = pd.DataFrame(lot.get_portfolio_max())
            chart = ple.line(pt)
    st.plotly_chart(chart)

page_dasboard()

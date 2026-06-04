import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📈 Profitability Analytics")

profit_stats = (
    df.groupby("Profitable")
    .agg(
        Avg_Revenue=("Revenue (M USD)","mean"),
        Avg_Valuation=("Valuation (M USD)","mean"),
        Avg_Funding=("Funding Amount (M USD)","mean")
    )
)

st.dataframe(profit_stats)

fig = px.box(
    df,
    x="Profitable",
    y="Revenue (M USD)",
    color="Profitable",
    title="Revenue by Profitability"
)

st.plotly_chart(fig,use_container_width=True)

fig = px.violin(
    df,
    x="Profitable",
    y="Valuation (M USD)",
    color="Profitable",
    box=True
)

st.plotly_chart(fig,use_container_width=True)

fig = px.scatter(
    df,
    x="Revenue (M USD)",
    y="Valuation (M USD)",
    color="Profitable",
    title="Revenue vs Valuation"
)

st.plotly_chart(fig,use_container_width=True)

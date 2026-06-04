import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🏭 Industry Insights")

industry_stats = (
    df.groupby("Industry")
    .agg(
        Avg_Revenue=("Revenue (M USD)","mean"),
        Avg_Valuation=("Valuation (M USD)","mean"),
        Startups=("Startup Name","count")
    )
    .reset_index()
)

st.dataframe(industry_stats)

fig = px.treemap(
    df,
    path=["Industry"],
    values="Valuation (M USD)",
    color="Revenue (M USD)",
    title="Industry Valuation Treemap"
)

st.plotly_chart(fig,use_container_width=True)

fig = px.bar(
    industry_stats,
    x="Industry",
    y="Avg_Valuation",
    color="Industry",
    title="Average Valuation by Industry"
)

st.plotly_chart(fig,use_container_width=True)

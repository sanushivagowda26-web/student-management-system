import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🌍 Regional Analysis")

region_stats = (
    df.groupby("Region")
    .agg(
        Funding=("Funding Amount (M USD)","sum"),
        Revenue=("Revenue (M USD)","sum"),
        Valuation=("Valuation (M USD)","sum")
    )
    .reset_index()
)

st.dataframe(region_stats)

fig = px.bar(
    region_stats,
    x="Region",
    y="Funding",
    color="Region",
    title="Funding by Region"
)

st.plotly_chart(fig,use_container_width=True)

fig = px.sunburst(
    df,
    path=["Region","Industry"],
    values="Funding Amount (M USD)",
    title="Region vs Industry Funding"
)

st.plotly_chart(fig,use_container_width=True)

fig = px.pie(
    df,
    names="Region",
    title="Startup Regional Distribution"
)

st.plotly_chart(fig,use_container_width=True)

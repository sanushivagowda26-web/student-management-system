import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("📊 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Startups",
    len(df)
)

col2.metric(
    "Total Funding",
    f"${df['Funding Amount (M USD)'].sum():,.0f}M"
)

col3.metric(
    "Avg Valuation",
    f"${df['Valuation (M USD)'].mean():,.0f}M"
)

col4.metric(
    "Profitability Rate",
    f"{df['Profitable'].mean()*100:.1f}%"
)

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    color="Industry",
    size="Revenue (M USD)",
    hover_name="Startup Name"
)

st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("💰 Funding Analytics")

industry_funding = (
    df.groupby("Industry")["Funding Amount (M USD)"]
      .sum()
      .reset_index()
)

fig = px.bar(
    industry_funding,
    x="Industry",
    y="Funding Amount (M USD)",
    color="Industry"
)

st.plotly_chart(fig, use_container_width=True)

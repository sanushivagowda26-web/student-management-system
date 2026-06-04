import plotly.express as px

industry_funding = (
    df.groupby("Industry")
    ["Funding Amount (M USD)"]
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

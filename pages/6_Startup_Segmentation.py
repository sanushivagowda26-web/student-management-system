import streamlit as st
import plotly.express as px

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from utils.data_loader import load_data

df = load_data()

st.title("🚀 Startup Segmentation")

features = df[
[
    "Funding Amount (M USD)",
    "Revenue (M USD)",
    "Valuation (M USD)"
]
]

scaler = StandardScaler()

scaled = scaler.fit_transform(
    features
)

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(
    scaled
)

cluster_summary = (
    df.groupby("Cluster")
    .agg(
        Avg_Funding=("Funding Amount (M USD)","mean"),
        Avg_Revenue=("Revenue (M USD)","mean"),
        Avg_Valuation=("Valuation (M USD)","mean")
    )
)

st.subheader("Cluster Summary")

st.dataframe(cluster_summary)

fig = px.scatter_3d(
    df,
    x="Funding Amount (M USD)",
    y="Revenue (M USD)",
    z="Valuation (M USD)",
    color="Cluster",
    hover_name="Startup Name",
    title="Startup Segmentation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Revenue (M USD)",
    color="Cluster",
    size="Valuation (M USD)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

import streamlit as st
import pandas as pd
import numpy as np


@st.cache_data
def load_data():

    df = pd.read_csv("data/startup_data.csv")

    current_year = 2026

    # -----------------------------------
    # Feature Engineering
    # -----------------------------------

    df["Startup Age"] = (
        current_year -
        df["Year Founded"]
    )

    df["Funding Efficiency"] = (
        df["Revenue (M USD)"] /
        df["Funding Amount (M USD)"]
    )

    df["Valuation Multiple"] = (
        df["Valuation (M USD)"] /
        df["Revenue (M USD)"]
    )

    df["Revenue Per Employee"] = (
        (df["Revenue (M USD)"] * 1_000_000)
        / df["Employees"]
    )

    df["Valuation Efficiency"] = (
        df["Valuation (M USD)"] /
        df["Funding Amount (M USD)"]
    )

    # -----------------------------------
    # Startup Health Score
    # -----------------------------------

    df["Health Score"] = (

        df["Funding Efficiency"]
        .rank(pct=True) * 30

        +

        df["Valuation Multiple"]
        .rank(pct=True) * 30

        +

        df["Revenue Per Employee"]
        .rank(pct=True) * 20

        +

        df["Market Share (%)"]
        .rank(pct=True) * 20

    )

    df["Health Score"] = (
        df["Health Score"]
        .round(2)
    )

    return df

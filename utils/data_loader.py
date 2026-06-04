import pandas as pd

def load_data():

    df = pd.read_csv("data/startup_data.csv")

    df["Startup Age"] = 2026 - df["Year Founded"]

    df["Funding Efficiency"] = (
        df["Revenue (M USD)"] /
        df["Funding Amount (M USD)"]
    )

    df["Revenue Per Employee"] = (
        df["Revenue (M USD)"] * 1000000
    ) / df["Employees"]

    df["Valuation Multiple"] = (
        df["Valuation (M USD)"] /
        df["Revenue (M USD)"]
    )

    return df

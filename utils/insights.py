def generate_insights(df):

    insights = []

    # ----------------------------
    # Highest Valuation Industry
    # ----------------------------

    top_industry = (
        df.groupby("Industry")
        ["Valuation (M USD)"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"🏆 Highest average valuation industry: {top_industry}"
    )

    # ----------------------------
    # Best Revenue Region
    # ----------------------------

    top_region = (
        df.groupby("Region")
        ["Revenue (M USD)"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"🌍 Highest average revenue region: {top_region}"
    )

    # ----------------------------
    # Profitability Rate
    # ----------------------------

    profitability = (
        df["Profitable"]
        .mean() * 100
    )

    insights.append(
        f"💰 Profitability rate across startups: {profitability:.1f}%"
    )

    # ----------------------------
    # Unicorn Startups
    # ----------------------------

    unicorns = len(
        df[
            df["Valuation (M USD)"] >= 1000
        ]
    )

    insights.append(
        f"🦄 Unicorn candidates detected: {unicorns}"
    )

    # ----------------------------
    # Most Efficient Startup
    # ----------------------------

    efficient = (
        df.sort_values(
            "Funding Efficiency",
            ascending=False
        )
        .iloc[0]["Startup Name"]
    )

    insights.append(
        f"🚀 Most capital-efficient startup: {efficient}"
    )

    return insights

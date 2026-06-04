import plotly.express as px


def funding_vs_valuation(df):

    fig = px.scatter(
        df,
        x="Funding Amount (M USD)",
        y="Valuation (M USD)",
        size="Revenue (M USD)",
        color="Industry",
        hover_name="Startup Name",
        title="Funding vs Valuation"
    )

    return fig


def industry_treemap(df):

    fig = px.treemap(
        df,
        path=["Industry"],
        values="Valuation (M USD)",
        color="Revenue (M USD)",
        title="Industry Valuation Treemap"
    )

    return fig


def regional_sunburst(df):

    fig = px.sunburst(
        df,
        path=["Region", "Industry"],
        values="Funding Amount (M USD)",
        title="Regional Funding Distribution"
    )

    return fig


def profitability_box(df):

    fig = px.box(
        df,
        x="Profitable",
        y="Revenue (M USD)",
        color="Profitable",
        title="Revenue Distribution by Profitability"
    )

    return fig


def health_score_chart(df):

    top = df.nlargest(
        15,
        "Health Score"
    )

    fig = px.bar(
        top,
        x="Startup Name",
        y="Health Score",
        color="Health Score",
        title="Top Startup Health Scores"
    )

    return fig


def funding_efficiency_chart(df):

    top = df.nlargest(
        15,
        "Funding Efficiency"
    )

    fig = px.bar(
        top,
        x="Startup Name",
        y="Funding Efficiency",
        color="Industry",
        title="Funding Efficiency Leaders"
    )

    return fig


def revenue_employee_chart(df):

    top = df.nlargest(
        20,
        "Revenue Per Employee"
    )

    fig = px.bar(
        top,
        x="Startup Name",
        y="Revenue Per Employee",
        color="Industry",
        title="Revenue Per Employee"
    )

    return fig

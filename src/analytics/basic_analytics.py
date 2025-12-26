import pandas as pd

def compute_basic_metrics(df):
    metrics = {}

    metrics["date_range"] = (df["date"].min(), df["date"].max())
    if "sku" in df.columns:
        metrics["num_products"] = df["sku"].nunique()
    metrics["num_days"] = df["date"].nunique()

    if "units_sold" in df.columns:
        metrics["total_units_sold"] = df["units_sold"].sum()
        metrics["avg_daily_units"] = df.groupby("date")["units_sold"].sum().mean()

    if "sales_amount" in df.columns:
        metrics["total_sales"] = df["sales_amount"].sum()
        metrics["avg_daily_sales"] = df.groupby("date")["sales_amount"].sum().mean()

    return metrics


def top_products(df, n=10):
    # Only return top products if SKU exists
    if "sku" not in df.columns:
        return None
    
    if "units_sold" in df.columns:
        return (
            df.groupby("sku")["units_sold"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    return (
        df.groupby("sku")["sales_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

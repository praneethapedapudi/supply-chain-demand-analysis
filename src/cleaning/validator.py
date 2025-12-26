def validate(df):
    if df.empty:
        raise ValueError("No valid data after cleaning")

    if "units_sold" in df.columns:
        # Keep only positive demand for forecasting
        df = df[df["units_sold"] > 0]

        if df.empty:
            raise ValueError("All rows removed after filtering returns")

    return df

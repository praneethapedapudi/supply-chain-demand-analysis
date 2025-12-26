def extract_metadata(df, n_samples=3):
    return {
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "sample_values": {
            col: df[col].dropna().astype(str).head(n_samples).tolist()
            for col in df.columns
        }
    }

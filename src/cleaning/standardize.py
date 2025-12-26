import pandas as pd
import warnings

def standardize(df, mapping):
    # mapping: canonical_field -> input_column
    rename_map = {v: k for k, v in mapping.items()}
    df = df.rename(columns=rename_map)

    if "date" not in df.columns:
        raise ValueError("No date column after mapping")

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce",
        dayfirst=True
    )

    if "units_sold" in df.columns:
        df["units_sold"] = (
            df["units_sold"]
            .astype(str)
            .str.replace(r"[^\d.-]", "", regex=True)
            .astype(float)
        )
        required = ["date", "units_sold"]
        if "sku" in df.columns:
            required.append("sku")
        df = df.dropna(subset=required)
        return df[required]

    elif "sales_amount" in df.columns:
        df["sales_amount"] = (
            df["sales_amount"]
            .astype(str)
            .str.replace(r"[^\d.-]", "", regex=True)
            .astype(float)
        )
        required = ["date", "sales_amount"]
        if "sku" in df.columns:
            required.append("sku")
        df = df.dropna(subset=required)
        return df[required]

    else:
        # Automatically infer a measure column from numeric columns
        # Exclude date, sku, and id-like columns
        exclude_patterns = ["date", "sku", "id", "index", "key", "code"]
        numeric_cols = df.select_dtypes(include=['number', 'int64', 'float64', 'int32', 'float32']).columns.tolist()
        
        # Filter out excluded columns
        candidate_cols = [
            col for col in numeric_cols
            if not any(pattern in col.lower() for pattern in exclude_patterns)
        ]
        
        if candidate_cols:
            # Use the first suitable numeric column as units_sold
            inferred_col = candidate_cols[0]
            warnings.warn(
                f"No explicit measure column mapped. Inferring '{inferred_col}' as units_sold.",
                UserWarning
            )
            df["units_sold"] = df[inferred_col].astype(float)
            required = ["date", "units_sold"]
            if "sku" in df.columns:
                required.append("sku")
            df = df.dropna(subset=required)
            return df[required]
        else:
            # Only raise error if no numeric columns exist at all
            raise ValueError("No valid measure column found and no numeric columns available for inference")

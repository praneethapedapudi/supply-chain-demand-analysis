import pandas as pd

def load_file(file):
    name = file.name.lower()

    if name.endswith(".csv"):
        try:
            return pd.read_csv(file)
        except UnicodeDecodeError:
            file.seek(0)
            return pd.read_csv(file, encoding="latin1")

    elif name.endswith((".xls", ".xlsx")):
        return pd.read_excel(file)

    elif name.endswith(".tsv"):
        return pd.read_csv(file, sep="\t")

    elif name.endswith(".json"):
        return pd.read_json(file)

    elif name.endswith(".parquet"):
        return pd.read_parquet(file)

    else:
        raise ValueError("Unsupported file format")

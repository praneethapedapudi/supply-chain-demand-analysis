import os
from src.pipeline import ingest

class DummyLLM:
    def __call__(self, prompt):
        if "InvoiceDate" in prompt:
            return """
            {
              "date": "InvoiceDate",
              "sku": "StockCode",
              "units_sold": "Quantity"
            }
            """
        elif "ORDERDATE" in prompt:
            return """
            {
              "date": "ORDERDATE",
              "sku": "PRODUCTCODE",
              "units_sold": "QUANTITYORDERED"
            }
            """
        elif "Order Date" in prompt:
            return """
            {
              "date": "Order Date",
              "sku": "Product ID",
              "units_sold": "Quantity"
            }
            """
        elif "Weekly_Sales" in prompt:
            return """
            {
              "date": "Date",
              "sku": "Store",
              "sales_amount": "Weekly_Sales"
            }
            """
        else:
            return "{}"

def test_directory(dir_path):
    print(f"\n--- Scanning directory: {dir_path} ---")

    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)

        if not os.path.isfile(file_path):
            continue

        print(f"\n--- Testing file: {file_name} ---")

        try:
            with open(file_path, "rb") as f:
                df = ingest(f, llm_client=DummyLLM())

            print(df.head())
            print("Rows:", len(df))

        except Exception as e:
            print(f"❌ Failed on {file_name}: {e}")


if __name__ == "__main__":
    test_directory("data/raw")

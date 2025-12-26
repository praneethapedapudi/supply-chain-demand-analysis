import streamlit as st
import os
import pandas as pd
from dotenv import load_dotenv
from src.llm.groq_client import GroqLLM

from src.pipeline import ingest

load_dotenv()

st.set_page_config(page_title="Retail Analytics Engine", layout="wide")

st.title("🛒 Retail Data Analytics Engine")
st.write("Upload any retail sales file. Schema is inferred using LLM. Insights are generated automatically.")

uploaded_file = st.file_uploader(
    "Upload CSV / Excel file",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file:
    with st.spinner("Processing file..."):
        llm_client = GroqLLM()
        df_clean, metrics, top_items = ingest(uploaded_file, llm_client=llm_client)

    st.success("File processed successfully!")

    st.subheader("📌 Dataset Summary")
    for k, v in metrics.items():
        st.write(f"**{k}** : {v}")

    st.subheader("📊 Cleaned Data Preview")
    st.dataframe(df_clean.head(50))

    st.subheader("📈 Daily Trend")
    if "units_sold" in df_clean.columns:
        daily = df_clean.groupby("date")["units_sold"].sum()
    else:
        daily = df_clean.groupby("date")["sales_amount"].sum()

    st.line_chart(daily)

    if top_items is not None:
        st.subheader("🏆 Top Selling Products")
        st.bar_chart(top_items)
    else:
        st.subheader("📊 Overall Demand Trend")
        if "units_sold" in df_clean.columns:
            st.write("Aggregate dataset - showing overall demand over time.")
        else:
            st.write("Aggregate dataset - showing overall sales over time.")

    csv = df_clean.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download Cleaned Data",
        csv,
        "cleaned_sales.csv",
        "text/csv"
    )

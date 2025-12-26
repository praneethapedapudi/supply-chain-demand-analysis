# Supply Chain Demand Analysis and Forecasting System

An end-to-end, production-style data analytics system that ingests raw retail sales data (in any format), automatically standardizes it, and generates actionable demand insights for supply chain decision-making.

This project is designed to resemble real-world retail, e-commerce, and logistics analytics pipelines rather than a toy ML demo.

---

## Overview

Retail companies often receive sales data in inconsistent formats with varying column names, encodings, and granularity. This system solves that problem by automatically:

- Ingesting raw CSV or Excel files
- Inferring schema using deterministic heuristics
- Cleaning and standardizing data into a canonical format
- Adapting analytics based on data granularity
- Presenting insights through an interactive dashboard

The system is robust to missing columns, noisy schemas, and mixed aggregation levels.

---

## Key Features

- Accepts arbitrary retail sales datasets (no fixed schema required)
- Automatic column mapping to:
  - `date`
  - `sku` (optional)
  - `units_sold` or `sales_amount`
- Heuristic-first schema inference with confidence scoring
- Optional LLM-based fallback for ambiguous schemas (metadata-only, cost-safe)
- Supports both:
  - SKU-level datasets
  - Aggregate (store-level or overall) datasets
- Defensive data validation and preprocessing
- Interactive analytics dashboard built with Streamlit

---

## System Architecture


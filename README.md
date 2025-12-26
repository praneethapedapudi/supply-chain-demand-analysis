# Supply Chain Demand Analysis and Forecasting System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://supply-chain-demand-analysis.streamlit.app/)

An end-to-end, production-ready data analytics system that ingests raw retail sales data in any format, automatically standardizes it, and generates actionable demand insights for supply chain decision-making.

**Live Application**: [https://supply-chain-demand-analysis.streamlit.app/](https://supply-chain-demand-analysis.streamlit.app/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

Retail companies often receive sales data in inconsistent formats with varying column names, encodings, and granularity levels. This system solves that problem by automatically:

- **Ingesting** raw CSV or Excel files with flexible schema detection
- **Inferring** schema using intelligent heuristics with confidence scoring
- **Standardizing** data into a canonical format (date, SKU, units_sold/sales_amount)
- **Adapting** analytics based on data granularity (SKU-level vs aggregate)
- **Presenting** insights through an interactive Streamlit dashboard

The system is robust to missing columns, noisy schemas, and mixed aggregation levels, making it suitable for real-world production environments.

---

## ✨ Features

### Core Capabilities

- **Schema-Agnostic Ingestion**: Accepts arbitrary retail sales datasets without requiring a fixed schema
- **Intelligent Column Mapping**: Automatically maps columns to canonical fields:
  - `date` (required)
  - `sku` (optional - for SKU-level analysis)
  - `units_sold` or `sales_amount` (required)
- **Dual Schema Inference**:
  - **Heuristic-first approach** with confidence scoring
  - **LLM-based fallback** (Groq/Llama) for ambiguous schemas
- **Flexible Data Support**:
  - SKU-level datasets (product/item granularity)
  - Aggregate datasets (store-level or overall)
- **Defensive Processing**: Robust validation and error handling
- **Interactive Dashboard**: Real-time analytics with Streamlit

### Key Highlights

- ✅ No manual schema configuration required
- ✅ Automatic measure column inference
- ✅ Graceful fallback mechanisms
- ✅ Production-grade error handling
- ✅ Support for multiple file formats (CSV, Excel)

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/praneethapedapudi/supply-chain-demand-analysis.git
   cd supply-chain-demand-analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Note**: The Groq API key is optional. The system will use heuristic mapping if no LLM client is configured. However, for best results with ambiguous schemas, an API key is recommended.

### Getting a Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Add it to your `.env` file

---

## 💻 Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Upload a file**: Click "Upload CSV / Excel file" and select your sales data file
2. **Automatic processing**: The system will:
   - Detect and map columns automatically
   - Clean and standardize the data
   - Generate analytics and visualizations
3. **View insights**: Explore the dashboard for:
   - Dataset summary metrics
   - Daily trend charts
   - Top selling products (if SKU data available)
   - Cleaned data preview
4. **Download results**: Export the cleaned, standardized dataset

### Supported File Formats

- CSV (`.csv`)
- Excel (`.xlsx`, `.xls`)

### Expected Data Structure

Your input file should contain at minimum:
- A date/time column (any format)
- A numeric measure column (quantity, sales amount, revenue, etc.)

Optional:
- Product/SKU identifier column

---

## 📁 Project Structure

```
supply-chain-demand-analysis/
│
├── app.py                      # Streamlit application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .env                        # Environment variables (not tracked)
├── .gitignore                  # Git ignore rules
│
├── src/                        # Source code
│   ├── __init__.py
│   ├── pipeline.py            # Main ingestion pipeline
│   │
│   ├── loaders/               # File loading utilities
│   │   ├── __init__.py
│   │   └── file_loader.py
│   │
│   ├── metadata/              # Metadata extraction
│   │   ├── __init__.py
│   │   └── extractor.py
│   │
│   ├── schema/                # Schema inference
│   │   ├── heuristics.py     # Heuristic mapping
│   │   ├── llm_resolver.py   # LLM-based schema resolution
│   │   └── canonical.py
│   │
│   ├── cleaning/              # Data cleaning and standardization
│   │   ├── __init__.py
│   │   ├── standardize.py
│   │   └── validator.py
│   │
│   ├── analytics/             # Analytics and metrics
│   │   └── basic_analytics.py
│   │
│   └── llm/                   # LLM integration
│       └── groq_client.py
│
├── tests/                     # Test suite
│   ├── __init__.py
│   └── test_ingestion.py
│
├── notebooks/                 # Jupyter notebooks
│   └── 01_eda.ipynb
│
└── data/                      # Data directory (not tracked)
    ├── raw/                   # Raw input files
    └── standardized/          # Processed outputs
```

---

## 🛠️ Technologies

- **Python 3.10+**: Core programming language
- **Streamlit**: Interactive web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Groq API**: LLM integration for schema inference
- **python-dotenv**: Environment variable management
- **Matplotlib/Seaborn**: Data visualization

---

## 🔄 How It Works

### Pipeline Flow

1. **File Ingestion**: Load CSV/Excel file using pandas
2. **Metadata Extraction**: Extract column names, data types, and sample values
3. **Schema Inference**:
   - **Step 1**: Apply heuristic mapping with confidence scoring
   - **Step 2**: If confidence < 0.8, attempt LLM-based inference (if available)
   - **Step 3**: Fall back to heuristic mapping if LLM fails
4. **Data Standardization**: 
   - Rename columns to canonical format
   - Convert date columns to datetime
   - Clean numeric measure columns
   - Infer measure column if not explicitly mapped
5. **Validation**: Remove invalid rows, ensure data quality
6. **Analytics**: Compute metrics and generate visualizations
7. **Presentation**: Display results in Streamlit dashboard

### Schema Inference Strategy

The system uses a **defensive, multi-layered approach**:

- **Primary**: Deterministic heuristics (fast, reliable, free)
- **Fallback**: LLM-based inference (handles edge cases, requires API key)
- **Safety**: Automatic measure column inference if mapping fails
- **Robustness**: Graceful degradation at every step

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Praneeth A Pedapudi**

- GitHub: [@praneethapedapudi](https://github.com/praneethapedapudi)
- Project Link: [https://github.com/praneethapedapudi/supply-chain-demand-analysis](https://github.com/praneethapedapudi/supply-chain-demand-analysis)

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- LLM integration powered by [Groq](https://groq.com/)
- Data processing with [Pandas](https://pandas.pydata.org/)

---

**⭐ If you find this project useful, please consider giving it a star!**

# Mutual Fund Analytics

## Project Overview

The ** Mutual Fund Analytics** project is a data analytics solution designed to analyse mutual fund industry trends, fund performance, investor behaviour, SIP growth and portfolio risk.

The project uses **Python, Pandas, SQL, SQLite, Power BI, REST APIs and GitHub** to build an end-to-end analytics pipeline.

### Objectives

* Analyse mutual fund NAV and performance trends.
* Study AUM and SIP inflow growth.
* Analyse investor demographics and transaction behaviour.
* Compare mutual fund performance with market benchmarks.
* Calculate risk and return metrics.
* Identify high-performing mutual funds.
* Analyse sector concentration and portfolio risk.
* Build interactive Power BI dashboards.
* Provide investor-oriented fund recommendations.

---

## Key Analytics

The project includes the following financial and investor analytics:

* CAGR — 1-year, 3-year and 5-year
* Sharpe Ratio
* Sortino Ratio
* Alpha and Beta
* Maximum Drawdown
* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Fund Performance Scorecard
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector Concentration using HHI
* NAV vs Benchmark Analysis
* Fund Recommendation based on risk appetite

---

## Data Sources

The project uses:

* Mutual fund industry datasets provided for the project.
* Mutual fund NAV data from the **MFAPI REST API**.
* Benchmark index data including NIFTY 50 and NIFTY 100.

The raw datasets contain information about:

* Fund master data
* NAV history
* AUM by fund house
* SIP inflows
* Category-wise inflows
* Industry folio count
* Scheme performance
* Investor transactions
* Portfolio holdings
* Benchmark indices

---

## Project Structure
Project/
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── bluestock_mf_dashboard.pdf
│   ├── Fund_Performance.png
│   ├── Industry_Analytics.png
│   ├── Investor_Analytics.png
│   ├── README.md
│   └── SIP_&_Market_Trends.png
│
├── data/
│   ├── db/
│   │   ├── bluestock_mf.db
│   │   └── README.md
│   │
│   ├── processed/
│   │   ├── Analytics output CSV files
│   │   ├── Cleaned CSV files
│   │   └── README.md
│   │
│   └── raw/
│       ├── README.md
│       └── Raw CSV datasets
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   ├── 06_advanced_analytics.ipynb
│   ├── amfi_validation.ipynb
│   ├── EDA_Findings.ipynb
│   ├── fund_master_eda.ipynb
│   └── README.md
│
├── reports/
│   ├── Bluestock_MF_Presentation.pptx
│   ├── charts/
│   ├── Final_Report.pdf
│   └── README.md
│
├── scripts/
│   ├── data_ingestion.py
│   ├── fetch_5_nav.py
│   ├── live_nav_fetch.py
│   ├── README.md
│   └── recommender.py
│
├── sql/
│   ├── queries.sql
│   ├── README.md
│   └── schema.sql
│
├── README.md
├── requirement.txt
└── run_pipeline.py

## Folder and File Descriptions

### `data/raw/`

Contains the original raw datasets used as the input layer for the project.

The folder contains 10 primary datasets covering mutual funds, NAV, AUM, SIP, categories, folios, performance, transactions, holdings and benchmarks.

Additional NAV data for selected schemes is obtained through the MFAPI REST API.

---

### `data/processed/`

Contains cleaned datasets and analytical outputs.

The cleaned datasets include:

* `clean_fund_master.csv`
* `clean_nav.csv`
* `clean_aum_by_fund_house.csv`
* `clean_monthly_sip.csv`
* `clean_category_inflows.csv`
* `clean_industry_folio_count.csv`
* `clean_performance.csv`
* `clean_transactions.csv`
* `clean_portfolio.csv`
* `clean_benchmark.csv`

Analytical outputs include:

* `returns_computed.csv`
* `cagr_report.csv`
* `sharpe_values.csv`
* `sortino_values.csv`
* `alpha_beta.csv`
* `max_drawdown.csv`
* `fund_scorecard.csv`
* `var_cvar_report.csv`
* `cohort_analysis.csv`
* `sip_continuity.csv`
* `sector_hhi.csv`

---

### `data/db/`

Contains the SQLite analytical database:

```text
bluestock_mf.db
```

The database stores structured mutual fund data for SQL analysis.

---

### `notebooks/`

Contains Jupyter notebooks used for:

* Data ingestion
* Data cleaning
* AMFI validation
* Fund master analysis
* Exploratory Data Analysis
* Performance analytics
* Advanced analytics

---

### `scripts/`

Contains reusable Python scripts.

| Script              | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `data_ingestion.py` | Loads and inspects raw CSV datasets                          |
| `live_nav_fetch.py` | Fetches selected mutual fund NAV data using MFAPI            |
| `fetch_5_nav.py`    | Fetches NAV data for selected schemes                        |
| `recommender.py`    | Recommends top funds based on risk appetite and Sharpe Ratio |

---

### `sql/`

Contains SQL scripts used for database creation and analysis.

* `schema.sql` — Database table schema.
* `queries.sql` — SQL analysis queries.

---

### `dashboard/`

Contains the Power BI dashboard and PDF export.

The dashboard includes four pages:

1. **Industry Overview**
2. **Fund Performance**
3. **Investor Analytics**
4. **SIP & Market Trends**

---

### `reports/`

Contains the final project documentation and visualisation outputs.

* `Final_Report.pdf` — LaTeX source for the final report which converted to pdf
* `charts/` — Charts generated during the analysis.

---

## Technology Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Data processing and analytics  |
| Pandas           | Data cleaning and manipulation |
| NumPy            | Numerical calculations         |
| Matplotlib       | Data visualisation             |
| SQL              | Data analysis                  |
| SQLite           | Analytical database            |
| SQLAlchemy       | Database connection            |
| REST API         | NAV data collection            |
| Jupyter Notebook | Analysis environment           |
| Power BI         | Interactive dashboards         |
| LaTeX            | Final report                   |
| Git & GitHub     | Version control                |

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/Shamithanshetty/Bluestock_MF_Capstone.git
```

Move into the project directory:

```bash
cd Project
```

---

## 2. Check Python

The project uses Python for data ingestion and analytics.

Check the installed version:

```bash
python --version
```

---

## 3. Install Required Libraries

Install the main Python dependencies:

```bash
pip install pandas numpy matplotlib seaborn plotly sqlalchemy requests scipy jupyter
```

---

## 4. Open the Project in VS Code

Open the project folder in VS Code:

```bash
code .
```

Alternatively, open the folder manually through VS Code.

---

# How to Run the ETL Pipeline

The project contains a master script:


run_pipeline.py
```

The master script executes the main Python scripts in the project.

### Step 1: Open the Project Root

Make sure the terminal is inside:

Project/
```

For example:


C:\Users\shami\OneDrive\Desktop\all\fintech\Project>
```

### Step 2: Run the Pipeline

```bash
python run_pipeline.py
```

The pipeline runs:


data_ingestion.py
        ↓
live_nav_fetch.py
        ↓
fetch_5_nav.py
        ↓
recommender.py


The scripts load datasets, fetch selected NAV data, and generate fund recommendations based on the selected investor risk appetite.

When prompted, enter:


Low
```

or


Moderate
```

or


High
```

---

# Running Individual Scripts

Scripts can also be executed individually from the `scripts` folder.

```bash
cd scripts
```

Then:

```bash
python data_ingestion.py
```

```bash
python live_nav_fetch.py
```

```bash
python fetch_5_nav.py
```

```bash
python recommender.py
```

---

# Running the Jupyter Notebooks

Start Jupyter Notebook from the project root:

```bash
jupyter notebook
```

Open the required notebook from the `notebooks` folder.

The notebooks should generally be executed in the project workflow order:

1. `01_data_ingestion.ipynb`
2. `02_data_cleaning.ipynb`
3. `amfi_validation.ipynb`
4. `fund_master_eda.ipynb`
5. `EDA_Findings.ipynb`
6. `04_performance_analytics.ipynb`
7. `05_advanced_analytics.ipynb`

---

# How to Open the Power BI Dashboard

The Power BI dashboard is located in:


dashboard/bluestock_mf.pbix
```

### Steps

1. Open **Microsoft Power BI Desktop**.
2. Select **File → Open**.
3. Navigate to the project folder.
4. Open:


dashboard/bluestock_mf.pbix
```

5. Review the four dashboard pages.

The exported PDF is also available at:


dashboard/bluestock_mf.pdf
```

---

# Dashboard Pages

## 1. Industry Overview

Provides an overview of:

* Total AUM
* SIP inflows
* Folio count
* Number of schemes
* AUM growth by fund house
* Top fund houses by AUM

## 2. Fund Performance

Provides:

* Fund returns
* Risk measures
* Sharpe Ratio
* Fund scorecard
* NAV versus benchmark
* Fund filtering and drill-through analysis

## 3. Investor Analytics

Provides:

* Investor demographics
* Age-group analysis
* Transaction types
* Geographic distribution
* Investor behaviour

## 4. SIP & Market Trends

Provides:

* SIP inflow trends
* SIP versus NIFTY 50
* Category-wise inflows
* SIP account growth

---

# Key Project Findings

* Mutual fund NAVs showed an overall upward trend during the analysed period, with periods of market correction and volatility.
* Industry AUM increased substantially between 2022 and 2025.
* Monthly SIP inflows increased over time and reached approximately **₹31,002 crore in December 2025**.
* Folio count increased from approximately **13.26 crore in January 2022 to 26.12 crore in December 2025**.
* SIP transactions represented the largest transaction type in the investor transaction dataset.
* The **26–35 age group** represented the largest investor transaction group.
* T30 locations represented a significant share of investor activity.
* Fund performance varied across schemes based on return and risk characteristics.
* Risk-adjusted metrics such as Sharpe Ratio and Sortino Ratio provided additional information beyond absolute returns.
* Sector concentration analysis using HHI helped identify portfolio concentration risk.

---

# Project Workflow


Raw CSV Data
     │
     ▼
Data Ingestion
     │
     ▼
Data Cleaning & Validation
     │
     ▼
Processed CSV Files
     │
     ▼
SQLite Database
     │
     ▼
SQL + Python Analytics
     │
     ▼
Performance & Risk Analysis
     │
     ▼
Power BI Dashboard
     │
     ▼
Business Insights & Recommendations


---

# GitHub Usage

Check the current Git status:

```bash
git status
```

Add the project files:

```bash
git add .
```

Commit the changes:

```bash
git commit -m "Final: Complete Bluestock MF
Capstone"
```

Push to the `master` branch:

```bash
git push origin master
```

Create a project release tag if required:

```bash
git tag v1.0
```

Push the tag:

```bash
git push origin v1.0
```

---

# Final Deliverables

The completed project contains:

* Cleaned mutual fund datasets
* SQLite database
* SQL schema and analysis queries
* Python data ingestion scripts
* NAV API integration
* Exploratory Data Analysis
* Performance and risk analytics
* Advanced investor and portfolio analytics
* Power BI dashboard
* Dashboard PDF export
* Final LaTeX report
* Project presentation
* Documentation and README files
* Master pipeline script

---


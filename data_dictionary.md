# Data Dictionary

## Project
Mutual Fund Analytics Project

## Purpose
This document describes the tables, columns, data types, business definitions, and data sources used in the Mutual Fund Analytics project.

---

# 1. dim_fund

**Source:** `data/processed/clean_fund_master.csv`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | TEXT | Unique AMFI code identifying the mutual fund scheme |
| fund_house | TEXT | Name of the mutual fund company |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Main fund category |
| sub_category | TEXT | Sub-category of the fund |
| plan | TEXT | Fund plan such as Direct or Regular |
| launch_date | DATE | Date when the fund was launched |
| benchmark | TEXT | Benchmark index used for comparison |
| expense_ratio_pct | REAL | Annual expense ratio of the fund in percentage |
| exit_load_pct | REAL | Exit load charged on redemption |
| min_sip_amount | REAL | Minimum amount required for SIP |
| min_lumpsum_amount | REAL | Minimum amount required for lumpsum investment |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | Risk classification of the fund |
| sebi_category_code | TEXT | SEBI category code |

---

# 2. dim_date

**Source:** Derived from dates in the cleaned datasets.

| Column | Data Type | Description |
|---|---|---|
| date_key | INTEGER | Unique numeric key for each date |
| full_date | DATE | Calendar date |
| year | INTEGER | Year of the date |
| quarter | INTEGER | Quarter of the year |
| month | INTEGER | Month number |
| month_name | TEXT | Name of the month |
| day | INTEGER | Day of the month |
| day_name | TEXT | Name of the day |

---

# 3. fact_nav

**Source:** `data/processed/clean_nav.csv`

| Column | Data Type | Description |
|---|---|---|
| nav_id | INTEGER | Unique identifier for NAV record |
| amfi_code | TEXT | AMFI code of the fund |
| date_key | INTEGER | Foreign key referencing dim_date |
| nav_date | DATE | Date of the NAV |
| nav | REAL | Net Asset Value of the fund |
| daily_return | REAL | Daily percentage return calculated from NAV |

---

# 4. fact_transactions

**Source:** `data/processed/clean_transactions.csv`

| Column | Data Type | Description |
|---|---|---|
| transaction_id | INTEGER | Unique transaction identifier |
| investor_id | TEXT | Unique investor identifier |
| amfi_code | TEXT | AMFI code of the fund |
| date_key | INTEGER | Foreign key referencing dim_date |
| transaction_date | DATE | Date of transaction |
| transaction_type | TEXT | Type of transaction: SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in Indian Rupees |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification of investor city |
| age_group | TEXT | Age group of investor |
| gender | TEXT | Gender of investor |
| annual_income_lakh | REAL | Annual investor income in lakh INR |
| payment_mode | TEXT | Mode of payment |
| kyc_status | TEXT | KYC verification status |

---

# 5. fact_performance

**Source:** `data/processed/clean_performance.csv`

| Column | Data Type | Description |
|---|---|---|
| performance_id | INTEGER | Unique performance record identifier |
| amfi_code | TEXT | AMFI code of the fund |
| scheme_name | TEXT | Name of the fund scheme |
| fund_house | TEXT | Mutual fund company |
| category | TEXT | Fund category |
| plan | TEXT | Fund plan |
| return_1yr_pct | REAL | One-year return percentage |
| return_3yr_pct | REAL | Three-year return percentage |
| return_5yr_pct | REAL | Five-year return percentage |
| benchmark_3yr_pct | REAL | Three-year benchmark return |
| alpha | REAL | Excess return relative to benchmark |
| beta | REAL | Sensitivity of fund returns to benchmark |
| sharpe_ratio | REAL | Risk-adjusted return measure |
| sortino_ratio | REAL | Downside-risk adjusted return measure |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum observed decline from a peak |
| aum_crore | REAL | Assets under management in crore INR |
| expense_ratio_pct | REAL | Fund expense ratio in percentage |
| morningstar_rating | REAL | Morningstar fund rating |
| risk_grade | TEXT | Risk grade of the fund |

---

# 6. fact_aum

**Source:** `data/processed/clean_aum_by_fund_house.csv`

| Column | Data Type | Description |
|---|---|---|
| aum_id | INTEGER | Unique AUM record identifier |
| date_key | INTEGER | Foreign key referencing dim_date |
| aum_date | DATE | Date of AUM measurement |
| fund_house | TEXT | Mutual fund company |
| aum_lakh_crore | REAL | AUM in lakh crore INR |
| aum_crore | REAL | AUM in crore INR |
| num_schemes | INTEGER | Number of schemes managed by fund house |

---

# 7. monthly_sip_inflows

**Source:** `data/processed/clean_monthly_sip.csv`

| Column | Data Type | Description |
|---|---|---|
| month | DATE | Month of SIP data |
| sip_inflow_crore | REAL | SIP inflow amount in crore INR |
| active_sip_accounts_crore | REAL | Number of active SIP accounts in crore |
| new_sip_accounts_lakh | REAL | Number of new SIP accounts in lakh |
| sip_aum_lakh_crore | REAL | SIP-related AUM in lakh crore INR |
| yoy_growth_pct | REAL | Year-over-year SIP growth percentage |

---

# 8. category_inflows

**Source:** `data/processed/clean_category.csv`

| Column | Data Type | Description |
|---|---|---|
| month | DATE | Month of inflow data |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net inflow amount in crore INR |

---

# 9. industry_folio_count

**Source:** `data/processed/clean_industry_folio_count.csv`

| Column | Data Type | Description |
|---|---|---|
| month | DATE | Month of folio data |
| total_folios_crore | REAL | Total number of folios in crore |
| equity_folios_crore | REAL | Equity folios in crore |
| debt_folios_crore | REAL | Debt folios in crore |
| hybrid_folios_crore | REAL | Hybrid folios in crore |
| others_folios_crore | REAL | Other folios in crore |

---

# 10. portfolio_holdings

**Source:** `data/processed/clean_portfolio.csv`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | AMFI code of the fund |
| stock_symbol | TEXT | Stock exchange symbol |
| stock_name | TEXT | Name of the stock |
| sector | TEXT | Industry sector of the stock |
| weight_pct | REAL | Stock weight in the fund portfolio |
| market_value_cr | REAL | Market value of holding in crore INR |
| current_price_inr | REAL | Current stock price in INR |
| portfolio_date | DATE | Portfolio reporting date |

---

# 11. benchmark_indices

**Source:** `data/processed/clean_benchmark_indices.csv`

| Column | Data Type | Description |
|---|---|---|
| date | DATE | Date of index value |
| index_name | TEXT | Name of benchmark index |
| close_value | REAL | Closing value of the index |

---

# Data Sources

The data used in this project comes from the provided mutual fund CSV datasets and the live NAV data collected during the project.

## Main Sources

- Fund master data
- NAV history
- AUM by fund house
- Monthly SIP inflows
- Category inflows
- Industry folio counts
- Scheme performance
- Investor transactions
- Portfolio holdings
- Benchmark indices
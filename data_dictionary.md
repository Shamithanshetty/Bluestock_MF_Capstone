# Data Dictionary

## Project

**Mutual Fund Analytics Project**

## Purpose

This data dictionary documents all columns used in the Mutual Fund Analytics project, including their data types, business definitions, and source references.

---

# 1. dim_fund

**Description:** Dimension table containing master information about mutual fund schemes.

**Source Reference:** `data/processed/clean_fund_master.csv`

| Column             | Data Type | Business Definition                                                                         | Source Reference      |
| ------------------ | --------- | ------------------------------------------------------------------------------------------- | --------------------- |
| amfi_code          | TEXT      | Unique identifier assigned to a mutual fund scheme by AMFI.                                 | clean_fund_master.csv |
| fund_house         | TEXT      | Name of the mutual fund company managing the scheme.                                        | clean_fund_master.csv |
| scheme_name        | TEXT      | Official name of the mutual fund scheme.                                                    | clean_fund_master.csv |
| category           | TEXT      | Broad investment category of the mutual fund.                                               | clean_fund_master.csv |
| sub_category       | TEXT      | More specific classification within the fund category.                                      | clean_fund_master.csv |
| plan               | TEXT      | Investment plan type, such as Direct or Regular.                                            | clean_fund_master.csv |
| launch_date        | DATE      | Date on which the mutual fund scheme was launched.                                          | clean_fund_master.csv |
| benchmark          | TEXT      | Benchmark index used to evaluate the fund's performance.                                    | clean_fund_master.csv |
| expense_ratio_pct  | REAL      | Annual percentage of fund assets charged as operating expenses.                             | clean_fund_master.csv |
| exit_load_pct      | REAL      | Percentage charged when an investor exits or redeems the fund within the applicable period. | clean_fund_master.csv |
| min_sip_amount     | REAL      | Minimum investment amount required to start a SIP.                                          | clean_fund_master.csv |
| min_lumpsum_amount | REAL      | Minimum amount required for a lumpsum investment.                                           | clean_fund_master.csv |
| fund_manager       | TEXT      | Name of the person responsible for managing the fund.                                       | clean_fund_master.csv |
| risk_category      | TEXT      | Risk classification assigned to the mutual fund scheme.                                     | clean_fund_master.csv |
| sebi_category_code | TEXT      | SEBI classification code associated with the fund category.                                 | clean_fund_master.csv |

---

# 2. dim_date

**Description:** Date dimension used to provide calendar attributes for analytical queries.

**Source Reference:** Derived from date columns in the cleaned datasets.

| Column     | Data Type | Business Definition                                          | Source Reference |
| ---------- | --------- | ------------------------------------------------------------ | ---------------- |
| date_key   | INTEGER   | Unique numeric identifier used to reference a calendar date. | Derived          |
| full_date  | DATE      | Complete calendar date.                                      | Derived          |
| year       | INTEGER   | Calendar year associated with the date.                      | Derived          |
| quarter    | INTEGER   | Quarter of the year, from 1 to 4.                            | Derived          |
| month      | INTEGER   | Month number, from 1 to 12.                                  | Derived          |
| month_name | TEXT      | Name of the calendar month.                                  | Derived          |
| day        | INTEGER   | Day number within the month.                                 | Derived          |
| day_name   | TEXT      | Name of the day of the week.                                 | Derived          |

---

# 3. fact_nav

**Description:** Fact table containing historical Net Asset Value information for mutual fund schemes.

**Source Reference:** `data/processed/clean_nav.csv`

| Column       | Data Type | Business Definition                                                                  | Source Reference |
| ------------ | --------- | ------------------------------------------------------------------------------------ | ---------------- |
| nav_id       | INTEGER   | Unique identifier for each NAV record.                                               | Derived          |
| amfi_code    | TEXT      | Identifier of the mutual fund scheme associated with the NAV.                        | clean_nav.csv    |
| date_key     | INTEGER   | Foreign key linking the NAV record to the date dimension.                            | Derived          |
| nav_date     | DATE      | Date on which the NAV was recorded.                                                  | clean_nav.csv    |
| nav          | REAL      | Net Asset Value per unit of the mutual fund scheme.                                  | clean_nav.csv    |
| daily_return | REAL      | Percentage change in NAV compared with the previous available NAV for the same fund. | Derived          |

---

# 4. fact_transactions

**Description:** Fact table containing investor mutual fund transaction records.

**Source Reference:** `data/processed/clean_transactions.csv`

| Column             | Data Type | Business Definition                                                                | Source Reference       |
| ------------------ | --------- | ---------------------------------------------------------------------------------- | ---------------------- |
| transaction_id     | INTEGER   | Unique identifier for each investor transaction.                                   | Derived                |
| investor_id        | TEXT      | Unique identifier representing the investor.                                       | clean_transactions.csv |
| amfi_code          | TEXT      | Identifier of the mutual fund scheme involved in the transaction.                  | clean_transactions.csv |
| date_key           | INTEGER   | Foreign key linking the transaction to the date dimension.                         | Derived                |
| transaction_date   | DATE      | Date on which the transaction occurred.                                            | clean_transactions.csv |
| transaction_type   | TEXT      | Type of transaction, such as SIP, Lumpsum, or Redemption.                          | clean_transactions.csv |
| amount_inr         | REAL      | Monetary value of the transaction in Indian Rupees.                                | clean_transactions.csv |
| state              | TEXT      | Indian state associated with the investor.                                         | clean_transactions.csv |
| city               | TEXT      | City associated with the investor.                                                 | clean_transactions.csv |
| city_tier          | TEXT      | Classification of the investor's city based on its tier.                           | clean_transactions.csv |
| age_group          | TEXT      | Age-group classification of the investor.                                          | clean_transactions.csv |
| gender             | TEXT      | Gender category recorded for the investor.                                         | clean_transactions.csv |
| annual_income_lakh | REAL      | Investor's annual income expressed in lakh INR.                                    | clean_transactions.csv |
| payment_mode       | TEXT      | Payment method used to complete the transaction.                                   | clean_transactions.csv |
| kyc_status         | TEXT      | Status indicating whether the investor's KYC verification is completed or pending. | clean_transactions.csv |

---

# 5. fact_performance

**Description:** Fact table containing mutual fund performance and risk metrics.

**Source Reference:** `data/processed/clean_performance.csv`

| Column             | Data Type | Business Definition                                                     | Source Reference      |
| ------------------ | --------- | ----------------------------------------------------------------------- | --------------------- |
| performance_id     | INTEGER   | Unique identifier for each fund performance record.                     | Derived               |
| amfi_code          | TEXT      | Identifier of the mutual fund scheme.                                   | clean_performance.csv |
| scheme_name        | TEXT      | Name of the mutual fund scheme.                                         | clean_performance.csv |
| fund_house         | TEXT      | Name of the mutual fund company managing the scheme.                    | clean_performance.csv |
| category           | TEXT      | Broad category of the mutual fund.                                      | clean_performance.csv |
| plan               | TEXT      | Investment plan type of the fund.                                       | clean_performance.csv |
| return_1yr_pct     | REAL      | Percentage return generated by the fund over one year.                  | clean_performance.csv |
| return_3yr_pct     | REAL      | Percentage return generated by the fund over three years.               | clean_performance.csv |
| return_5yr_pct     | REAL      | Percentage return generated by the fund over five years.                | clean_performance.csv |
| benchmark_3yr_pct  | REAL      | Three-year return generated by the fund's benchmark.                    | clean_performance.csv |
| alpha              | REAL      | Measure of the fund's excess performance relative to its benchmark.     | clean_performance.csv |
| beta               | REAL      | Measure of the fund's sensitivity to movements in its benchmark.        | clean_performance.csv |
| sharpe_ratio       | REAL      | Risk-adjusted return measure comparing excess return with volatility.   | clean_performance.csv |
| sortino_ratio      | REAL      | Risk-adjusted return measure that focuses on downside volatility.       | clean_performance.csv |
| std_dev_ann_pct    | REAL      | Annualized standard deviation measuring the volatility of fund returns. | clean_performance.csv |
| max_drawdown_pct   | REAL      | Largest percentage decline from a previous peak value.                  | clean_performance.csv |
| aum_crore          | REAL      | Assets under management expressed in crore INR.                         | clean_performance.csv |
| expense_ratio_pct  | REAL      | Annual fund expenses expressed as a percentage of assets.               | clean_performance.csv |
| morningstar_rating | REAL      | Rating assigned to the fund by Morningstar.                             | clean_performance.csv |
| risk_grade         | TEXT      | Risk grade assigned to the mutual fund scheme.                          | clean_performance.csv |

---

# 6. fact_aum

**Description:** Fact table containing Assets Under Management information by fund house.

**Source Reference:** `data/processed/clean_aum_by_fund_house.csv`

| Column         | Data Type | Business Definition                                       | Source Reference            |
| -------------- | --------- | --------------------------------------------------------- | --------------------------- |
| aum_id         | INTEGER   | Unique identifier for each AUM record.                    | Derived                     |
| date_key       | INTEGER   | Foreign key linking the AUM record to the date dimension. | Derived                     |
| aum_date       | DATE      | Date on which AUM was measured.                           | clean_aum_by_fund_house.csv |
| fund_house     | TEXT      | Name of the mutual fund company.                          | clean_aum_by_fund_house.csv |
| aum_lakh_crore | REAL      | Assets under management expressed in lakh crore INR.      | clean_aum_by_fund_house.csv |
| aum_crore      | REAL      | Assets under management expressed in crore INR.           | clean_aum_by_fund_house.csv |
| num_schemes    | INTEGER   | Number of mutual fund schemes managed by the fund house.  | clean_aum_by_fund_house.csv |

---

# 7. monthly_sip_inflows

**Description:** Monthly data describing Systematic Investment Plan (SIP) activity and inflows.

**Source Reference:** `data/processed/clean_monthly_sip.csv`

| Column                    | Data Type | Business Definition                                                     | Source Reference      |
| ------------------------- | --------- | ----------------------------------------------------------------------- | --------------------- |
| month                     | DATE      | Month for which SIP statistics are reported.                            | clean_monthly_sip.csv |
| sip_inflow_crore          | REAL      | Total SIP inflow during the month in crore INR.                         | clean_monthly_sip.csv |
| active_sip_accounts_crore | REAL      | Number of active SIP accounts during the month, expressed in crore.     | clean_monthly_sip.csv |
| new_sip_accounts_lakh     | REAL      | Number of new SIP accounts created during the month, expressed in lakh. | clean_monthly_sip.csv |
| sip_aum_lakh_crore        | REAL      | SIP-related assets under management expressed in lakh crore INR.        | clean_monthly_sip.csv |
| yoy_growth_pct            | REAL      | Year-over-year percentage growth in SIP inflows.                        | clean_monthly_sip.csv |

---

# 8. category_inflows

**Description:** Monthly net investment inflows grouped by mutual fund category.

**Source Reference:** `data/processed/clean_category.csv`

| Column           | Data Type | Business Definition                                                   | Source Reference   |
| ---------------- | --------- | --------------------------------------------------------------------- | ------------------ |
| month            | DATE      | Month for which category inflow data is reported.                     | clean_category.csv |
| category         | TEXT      | Mutual fund category associated with the inflow.                      | clean_category.csv |
| net_inflow_crore | REAL      | Net amount invested into the category during the month, in crore INR. | clean_category.csv |

---

# 9. industry_folio_count

**Description:** Monthly mutual fund folio counts by investment category.

**Source Reference:** `data/processed/clean_industry_folio_count.csv`

| Column              | Data Type | Business Definition                                     | Source Reference               |
| ------------------- | --------- | ------------------------------------------------------- | ------------------------------ |
| month               | DATE      | Month for which folio statistics are reported.          | clean_industry_folio_count.csv |
| total_folios_crore  | REAL      | Total number of mutual fund folios, expressed in crore. | clean_industry_folio_count.csv |
| equity_folios_crore | REAL      | Number of equity fund folios, expressed in crore.       | clean_industry_folio_count.csv |
| debt_folios_crore   | REAL      | Number of debt fund folios, expressed in crore.         | clean_industry_folio_count.csv |
| hybrid_folios_crore | REAL      | Number of hybrid fund folios, expressed in crore.       | clean_industry_folio_count.csv |
| others_folios_crore | REAL      | Number of other-category folios, expressed in crore.    | clean_industry_folio_count.csv |

---

# 10. portfolio_holdings

**Description:** Fund portfolio holdings showing the stocks held by mutual fund schemes.

**Source Reference:** `data/processed/clean_portfolio.csv`

| Column            | Data Type | Business Definition                                     | Source Reference    |
| ----------------- | --------- | ------------------------------------------------------- | ------------------- |
| amfi_code         | INTEGER   | AMFI identifier of the mutual fund scheme.              | clean_portfolio.csv |
| stock_symbol      | TEXT      | Trading symbol representing the stock.                  | clean_portfolio.csv |
| stock_name        | TEXT      | Name of the company or stock held by the fund.          | clean_portfolio.csv |
| sector            | TEXT      | Industry sector to which the stock belongs.             | clean_portfolio.csv |
| weight_pct        | REAL      | Percentage of the fund portfolio invested in the stock. | clean_portfolio.csv |
| market_value_cr   | REAL      | Market value of the stock holding in crore INR.         | clean_portfolio.csv |
| current_price_inr | REAL      | Current price of the stock in Indian Rupees.            | clean_portfolio.csv |
| portfolio_date    | DATE      | Date associated with the reported portfolio holdings.   | clean_portfolio.csv |

---

# 11. benchmark_indices

**Description:** Historical closing values of selected market benchmark indices.

**Source Reference:** `data/processed/clean_benchmark.csv`

| Column      | Data Type | Business Definition                                         | Source Reference    |
| ----------- | --------- | ----------------------------------------------------------- | ------------------- |
| date        | DATE      | Date on which the benchmark index value was recorded.       | clean_benchmark.csv |
| index_name  | TEXT      | Name of the market benchmark index.                         | clean_benchmark.csv |
| close_value | REAL      | Closing value of the benchmark index on the specified date. | clean_benchmark.csv |



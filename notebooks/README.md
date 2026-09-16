# Notebooks

This folder contains Jupyter notebooks used for data ingestion, data quality validation, exploratory data analysis, fund master analysis, performance analytics, and advanced mutual fund analytics.

## Notebooks

* `01_data_ingestion.ipynb` — Loads and inspects the raw mutual fund datasets.

* `02_data_cleaning.ipynb` — Cleans and validates the mutual fund datasets.

* `amfi_validation.ipynb` — Validates AMFI codes by checking whether all 40 AMFI codes in `fund_master` exist in `nav_history`. The validation found 0 missing codes.

* `fund_master_eda.ipynb` — Analyses the fund master dataset to understand unique fund houses, categories, sub-categories, and risk grades.

* `EDA_Findings.ipynb` — Documents the key findings from the EDA, including NAV trends, AUM growth, SIP inflow growth, category-wise inflows, investor demographics, geographic distribution, folio growth, NAV return correlation, and sector allocation.

* `04_performance_analytics.ipynb` — Calculates mutual fund performance and risk metrics such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown.

* `06_advanced_analytics.ipynb` — Performs advanced risk, investor, SIP, and portfolio analytics including VaR, CVaR, investor cohorts, SIP continuity, and sector concentration.

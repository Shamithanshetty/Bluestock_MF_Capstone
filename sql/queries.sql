-- 1. Top 5 Funds by AUM

SELECT amfi_code, scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month

SELECT strftime('%Y-%m', nav_date) AS month, ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', nav_date)
ORDER BY month;

-- 3. SIP Inflow YoY Growth

WITH yearly_sip AS (
    SELECT
        strftime('%Y', month) AS year,
        SUM(sip_inflow_crore) AS total_sip_inflow
    FROM monthly_sip_inflows
    GROUP BY strftime('%Y', month)
)

SELECT
    year,
    ROUND(total_sip_inflow, 2) AS total_sip_inflow,
    ROUND(
        (total_sip_inflow - LAG(total_sip_inflow) OVER (ORDER BY year))
        * 100.0
        / LAG(total_sip_inflow) OVER (ORDER BY year),
        2
    ) AS yoy_growth_pct
FROM yearly_sip
ORDER BY year;


-- 4. Transactions by State

SELECT state, COUNT(*) AS transaction_count, ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 5. Funds with Expense Ratio < 1%

SELECT amfi_code, scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Average Transaction Amount by Type

SELECT transaction_type, COUNT(*) AS transaction_count, ROUND(AVG(amount_inr), 2) AS average_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY average_amount DESC;

-- 7. Highest Average NAV by Fund

SELECT amfi_code, ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY average_nav DESC
LIMIT 10;

-- 8. Number of Funds by Risk Category

SELECT risk_category, COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category
ORDER BY fund_count DESC;

-- 9. Transaction Amount by City Tier

SELECT city_tier, COUNT(*) AS transaction_count, ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY city_tier
ORDER BY total_amount DESC;

-- 10. Total AUM by Fund House

SELECT fund_house, ROUND(SUM(aum_crore), 2) AS total_aum_crore
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC;
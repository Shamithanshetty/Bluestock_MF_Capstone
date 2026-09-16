"""
Mutual fund recommendation module.

This module recommends the top three mutual funds based on
Sharpe ratio for the investor's selected risk appetite.
"""

# Simple fund recommendation logic:
# Input: investor risk appetite (Low/Moderate/High)
# Output: Top 3 funds by Sharpe ratio within matching risk_grade
# Print recommendation table

import pandas as pd
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
performance = pd.read_csv(
    os.path.join(project_root, "data", "processed", "clean_performance.csv")
)

sharpe = pd.read_csv(
    os.path.join(project_root, "data", "processed", "sharpe_values.csv")
)

# Merge Sharpe ratio with risk grade and fund name
recommendation_data = sharpe.merge(
    performance[["amfi_code", "scheme_name", "risk_grade"]],
    on="amfi_code",
    how="left"
)


def recommend_funds(risk_appetite):
    """
    Recommend the top 3 funds based on Sharpe ratio
    for the selected investor risk appetite.
    """

    filtered = recommendation_data[
        recommendation_data["risk_grade"].str.lower()
        == risk_appetite.lower()
    ]

    top_3 = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    return top_3[
        ["amfi_code", "scheme_name", "risk_grade", "sharpe_ratio"]
    ]


risk_appetite = input(
    "Enter risk appetite (Low/Moderate/High): "
)

recommendation = recommend_funds(risk_appetite)

print("\nTop 3 Fund Recommendations:")
print(recommendation.to_string(index=False))

"""
Data ingestion module for the  Mutual Fund Analytics project.

This module discovers CSV files from the data/raw directory,
loads each dataset using Pandas and displays basic information
about the datasets.
"""

import glob
import os

import pandas as pd


def data_ingestion():
    """
    Load all CSV files from the data/raw directory.

    For each dataset, display its shape, data types, and
    first five rows.

    Returns
    -------
    None
    """

    # Find the project folder
    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Find all CSV files in data/raw
    csv_path = os.path.join(project_root, "data", "raw", "*.csv")
    csv_files = glob.glob(csv_path)

    for file in csv_files:
        print("\nFile:", os.path.basename(file))

        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())


if __name__ == "__main__":
    data_ingestion()


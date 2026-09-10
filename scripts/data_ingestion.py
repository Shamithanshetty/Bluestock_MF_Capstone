import pandas as pd
import glob
import os

# Find the project folder
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Find all CSV files in data/raw
csv_path = os.path.join(project_root, "data", "raw", "*.csv")
csv_files = glob.glob(csv_path)

print("Number of CSV files found:", len(csv_files))

for file in csv_files:
    print("\nFile:", os.path.basename(file))

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
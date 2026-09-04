import pandas as pd
import glob

# Find all CSV files inside data/raw
csv_files = glob.glob("data/raw/*.csv")


for file in csv_files:
    print("\nFile:", file)
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

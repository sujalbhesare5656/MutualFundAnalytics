import pandas as pd
import os

RAW_PATH = "data/raw"

print("="*70)
print("DAY 1 - DATA INGESTION")
print("="*70)

files = sorted([f for f in os.listdir(RAW_PATH) if f.endswith(".csv")])

for file in files:

    print("\n" + "="*70)
    print("FILE:", file)
    print("="*70)

    df = pd.read_csv(os.path.join(RAW_PATH, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

try:

    fund_master = pd.read_csv(
        os.path.join(RAW_PATH, "01_fund_master.csv")
    )

    print("\n\nUNIQUE FUND HOUSES")
    for col in fund_master.columns:

        if "house" in col.lower():
            print(fund_master[col].unique())

    print("\nColumns in Fund Master:")
    print(fund_master.columns.tolist())

except Exception as e:
    print("Fund Master Exploration Error:", e)

try:

    fund_master = pd.read_csv(
        os.path.join(RAW_PATH, "01_fund_master.csv")
    )

    nav_history = pd.read_csv(
        os.path.join(RAW_PATH, "02_nav_history.csv")
    )

    common_cols = list(
        set(fund_master.columns)
        .intersection(set(nav_history.columns))
    )

    print("\nCommon Columns:")
    print(common_cols)

except Exception as e:
    print("Validation Error:", e)
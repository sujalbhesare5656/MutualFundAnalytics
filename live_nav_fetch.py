import pandas as pd
import os

RAW_PATH = "data/raw"

print("=" * 70)
print("DAY 1 - DATA INGESTION")
print("=" * 70)

files = sorted(
    [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]
)

for file in files:

    print("\n" + "=" * 70)
    print(f"FILE: {file}")
    print("=" * 70)

    df = pd.read_csv(os.path.join(RAW_PATH, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())



fund_master = pd.read_csv(
    os.path.join(RAW_PATH, "01_fund_master.csv")
)

print("\n\nUNIQUE FUND HOUSES")
print(fund_master["fund_house"].unique())

print("\nCATEGORIES")
print(fund_master["category"].unique())

print("\nSUB CATEGORIES")
print(fund_master["sub_category"].unique())

print("\nRISK CATEGORIES")
print(fund_master["risk_category"].unique())



try:
    nav_history = pd.read_csv(
        os.path.join(RAW_PATH, "02_nav_history.csv")
    )

    master_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])



    print("\nAMFI VALIDATION")
    print("-" * 50)

    print("Fund Master Codes:", len(master_codes))
    print("NAV History Codes:", len(nav_codes))
    print("Missing Codes:", len(missing_codes))

    if len(missing_codes) == 0:
        print("✓ All AMFI codes validated")
    else:
        print("Missing AMFI Codes:")
        print(sorted(missing_codes))

except Exception as e:
    print("Validation Error:", e)
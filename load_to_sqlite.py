import os
import pandas as pd
from sqlalchemy import create_engine


PROCESSED = "data/processed"
DB_NAME = "bluestock_mf.db"


engine = create_engine(f"sqlite:///{DB_NAME}")


files = [
    "01_fund_master_clean.csv",
    "02_nav_history_clean.csv",
    "03_aum_by_fund_house_clean.csv",
    "04_monthly_sip_inflows_clean.csv",
    "05_category_inflows_clean.csv",
    "06_industry_folio_count_clean.csv",
    "07_scheme_performance_clean.csv",
    "08_investor_transactions_clean.csv",
    "09_portfolio_holdings_clean.csv",
    "10_benchmark_indices_clean.csv"
]

for file in files:
    path = os.path.join(PROCESSED, file)

    if os.path.exists(path):
        df = pd.read_csv(path)

        # Table name = file name without .csv
        table_name = file.replace("_clean.csv", "")

        # Load into SQLite
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f" Loaded {table_name} ({len(df)} rows)")
    else:
        print(f" File not found: {file}")

print("\n All cleaned datasets loaded successfully!")
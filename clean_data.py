import os
import pandas as pd

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)


fund = pd.read_csv(f"{RAW}/01_fund_master.csv")

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund = fund.drop_duplicates()

fund.to_csv(
    f"{PROCESSED}/01_fund_master_clean.csv",
    index=False
)

print("Fund Master cleaned")


nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED}/02_nav_history_clean.csv",
    index=False
)

print("NAV History cleaned")


aum = pd.read_csv(f"{RAW}/03_aum_by_fund_house.csv")

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum = aum.drop_duplicates()

aum.to_csv(
    f"{PROCESSED}/03_aum_by_fund_house_clean.csv",
    index=False
)

print("AUM cleaned")


sip = pd.read_csv(f"{RAW}/04_monthly_sip_inflows.csv")

sip = sip.drop_duplicates()

sip.to_csv(
    f"{PROCESSED}/04_monthly_sip_inflows_clean.csv",
    index=False
)

print("SIP cleaned")


cat = pd.read_csv(f"{RAW}/05_category_inflows.csv")

cat = cat.drop_duplicates()

cat.to_csv(
    f"{PROCESSED}/05_category_inflows_clean.csv",
    index=False
)

print("Category cleaned")


folio = pd.read_csv(f"{RAW}/06_industry_folio_count.csv")

folio = folio.drop_duplicates()

folio.to_csv(
    f"{PROCESSED}/06_industry_folio_count_clean.csv",
    index=False
)

print("Folio cleaned")


perf = pd.read_csv(f"{RAW}/07_scheme_performance.csv")

cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for c in cols:
    perf[c] = pd.to_numeric(
        perf[c],
        errors="coerce"
    )

perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

perf = perf[
    perf["expense_ratio_pct"].between(0.1, 2.5)
]

perf.to_csv(
    f"{PROCESSED}/07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")


txn = pd.read_csv(f"{RAW}/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.upper()
    .replace({
        "LUMP SUM": "LUMPSUM"
    })
)

txn = txn[txn["amount_inr"] > 0]

txn["kyc_status"] = txn["kyc_status"].str.upper()

txn.to_csv(
    f"{PROCESSED}/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")


portfolio = pd.read_csv(f"{RAW}/09_portfolio_holdings.csv")

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

portfolio = portfolio.drop_duplicates()

portfolio.to_csv(
    f"{PROCESSED}/09_portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio cleaned")


bench = pd.read_csv(f"{RAW}/10_benchmark_indices.csv")

bench["date"] = pd.to_datetime(
    bench["date"],
    errors="coerce"
)

bench = bench.drop_duplicates()

bench.to_csv(
    f"{PROCESSED}/10_benchmark_indices_clean.csv",
    index=False
)

print("Benchmark cleaned")

print("\nAll 10 datasets cleaned successfully.")
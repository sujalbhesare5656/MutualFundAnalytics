import pandas as pd
import numpy as np
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
fund = pd.read_csv("data/processed/01_fund_master_clean.csv")
nav["date"] = pd.to_datetime(nav["date"])

nav = nav.merge(
    fund[["amfi_code", "scheme_name", "risk_category"]],
    on="amfi_code",
    how="left"
)

nav = nav.sort_values(["scheme_name", "date"])

nav["daily_return"] = (
    nav.groupby("scheme_name")["nav"]
       .pct_change()
)

nav = nav.dropna()
sharpe = (
    nav.groupby(["scheme_name", "risk_category"])["daily_return"]
       .apply(lambda x: (x.mean() / x.std()) * np.sqrt(252))
       .reset_index(name="Sharpe_Ratio")
)

sharpe = (
    nav.groupby(["scheme_name", "risk_category"])["daily_return"]
       .apply(lambda x: (x.mean() / x.std()) * np.sqrt(252))
       .reset_index(name="Sharpe_Ratio")
)
risk = input("Enter Risk Appetite (Low / Moderate / High): ")

recommend = sharpe[
    sharpe["risk_category"].str.lower() == risk.lower()
]

recommend = recommend.sort_values(
    "Sharpe_Ratio",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds\n")

print(
    recommend[
        ["scheme_name", "risk_category", "Sharpe_Ratio"]
    ]
)


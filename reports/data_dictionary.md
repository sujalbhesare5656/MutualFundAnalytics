
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI code of the mutual fund |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Scheme category |
| launch_date | DATE | Scheme launch date |


| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |


| Column | Data Type | Description |
|--------|-----------|-------------|
| fund_house | TEXT | AMC name |
| aum | REAL | Assets Under Management |
| date | DATE | Reporting date |


| Column | Data Type | Description |
|--------|-----------|-------------|
| year | INTEGER | Calendar year |
| month | TEXT | Month |
| sip_amount | REAL | Monthly SIP inflow |


| Column | Data Type | Description |
|--------|-----------|-------------|
| category | TEXT | Fund category |
| inflow | REAL | Net inflow amount |


| Column | Data Type | Description |
|--------|-----------|-------------|
| category | TEXT | Fund category |
| folio_count | INTEGER | Number of investor folios |


| Column | Data Type | Description |
|--------|-----------|-------------|
| scheme_name | TEXT | Mutual fund scheme |
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| expense_ratio_pct | REAL | Expense ratio (%) |


| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | INTEGER | Investor ID |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount |
| transaction_date | DATE | Date of transaction |
| kyc_status | TEXT | KYC verification status |


| Column | Data Type | Description |
|--------|-----------|-------------|
| scheme_name | TEXT | Mutual fund scheme |
| security_name | TEXT | Stock/Bond name |
| weight | REAL | Portfolio allocation (%) |


| Column | Data Type | Description |
|--------|-----------|-------------|
| index_name | TEXT | Benchmark index |
| date | DATE | Trading date |
| close_price | REAL | Closing index value |
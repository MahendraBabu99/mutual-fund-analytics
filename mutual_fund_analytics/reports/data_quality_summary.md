# Data Quality Summary

## Datasets Loaded
- HDFC_Top100.csv
- SBI_Bluechip.csv
- ICICI_Bluechip.csv
- Nippon_Large_Cap.csv
- Axis_Bluechip.csv
- Kotak_Bluechip.csv

## Findings
- No missing columns observed.
- NAV values appear numeric.
- Date field requires conversion to datetime.
- Additional fund_master and nav_history datasets were not provided.

## Recommendations
- Validate scheme codes against AMFI master list.
- Standardize date formats.
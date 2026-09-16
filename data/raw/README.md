# Raw Data

This folder contains the original raw datasets used in the Mutual Fund Analytics project.

## Datasets

The raw data includes:

* Fund master information
* Mutual fund NAV history
* AUM by fund house
* Monthly SIP inflows
* Category-wise inflows
* Industry folio count
* Scheme performance
* Investor transactions
* Portfolio holdings
* Benchmark indices

Additional NAV data for selected mutual fund schemes was collected using the MFAPI REST API.
HDFC Top 100(125497)
SBI Bluechip (119551)
ICICI Bluechip(120503)
 Nippon Large Cap(118632)
Axis Bluechip (119092)
Kotak Bluechip (120841)

## Purpose

The files in this folder are used as the input layer for the project's data ingestion and ETL processes.

The raw datasets are preserved separately and are not directly modified during analysis. Cleaned and transformed datasets are stored in the `data/processed` folder.

# Scripts

This folder contains Python scripts used for the Mutual Fund Analytics project.

## Files

### `data_ingestion.py`

Loads the raw CSV datasets from the `data/raw` folder using Pandas and displays basic dataset information such as shape, data types and the first five rows.

### `live_nav_fetch.py`

Fetch live NAV from mfapi.in: GET https://api.mfapi.in/mf/125497 (HDFC Top 100) Parse JSON response and saves the results as CSV files in the `data/raw` directory.

### `fetch_5_nav.py`

Fetches NAV data for five selected mutual fund schemes from the MFAPI REST API and saves the results as CSV files in the `data/raw` directory.
Fetch NAV for 5 schemes: SBI Bluechip (119551), ICICI Bluechip (120503), Nippon Large Cap (118632), Axis Bluechip (119092), Kotak Bluechip (120841)

### `recommender.py`

Recommends the top three mutual funds based on Sharpe ratio according to the investor's selected risk appetite: Low, Moderate or High.

## Requirements

The scripts use Python libraries including:

* pandas
* requests

## Usage

Run the scripts from the `scripts` directory:

```bash
python data_ingestion.py
python live_nav_fetch.py
python fetch_5_nav.py
python recommender.py
```

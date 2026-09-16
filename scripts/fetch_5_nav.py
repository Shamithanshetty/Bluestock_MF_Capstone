""" Live NAV data fetching module for the Mutual Fund Analytics project. This module fetches 
mutual fund NAV data from the MFAPI REST API for selected mutual fund schemes and saves the data as CSV files. """

import requests
import pandas as pd

schemes = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

for name, code in schemes.items():
    """ Fetch NAV data for each selected mutual fund scheme using its 
    AMFI scheme code. """

    url = "https://api.mfapi.in/mf/" + code

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    print("\n", name)
    print(df.head())

    df.to_csv("data/raw/" + name + "_nav.csv", index=False)


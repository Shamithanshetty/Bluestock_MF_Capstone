""" Fetch HDFC Top 100 mutual fund NAV data from the MFAPI REST API. This module retrieves NAV data using the 
AMFI scheme code 125497 and saves the result as a CSV file in the data/raw directory. """

import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

print(df.head())

df.to_csv("data/raw/hdfc_top_100_nav.csv", index=False)


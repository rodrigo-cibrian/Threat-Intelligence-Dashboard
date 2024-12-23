import requests
import pandas as pd

#API KEY
API_KEY = "2068e94857a4f793a770a538117e387921df8a0f51dcba7ed798c5b4f5d29bd5"
HEADERS = {"X-OTX-API-KEY": API_KEY}

#API Endpoint
url = "https://otx.alienvault.com/api/v1/indicators/export"

#Fetch data
response = requests.get(url, headers=HEADERS)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data["results"])
    df.to_csv("threat_data.csv", index=False)
    print("Data saved to threat_data.csv")
else:
    print("Error fetching data: {response.status_code}")
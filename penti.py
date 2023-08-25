import requests
import pandas as pd

url = "https://www.penti.com/tr/store-finder/getpos?countryCode=TR&regionCode=34&CSRFToken=2cca32b9-3818-4737-8c5b-e6612c147d6a"

headers = {
  cURL 
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    filtered_data = []

    for entry in data:
        displayName = entry.get("displayName")
        geoPoint = entry.get("geoPoint")
        if geoPoint:
            latitude = geoPoint.get("latitude")
            longitude = geoPoint.get("longitude")
        storeAddress = entry.get("storeAddress")

        filtered_data.append({
            "Display Name": displayName,
            "Latitude": latitude if geoPoint else None,
            "Longitude": longitude if geoPoint else None,
            "Store Address": storeAddress
        })

    df = pd.DataFrame(filtered_data)
    excel_file = "penti.xlsx"
    df.to_excel(excel_file, index=False)
    print(f"Data exported to {excel_file}")
else:
    print("Request failed with status code:", response.status_code)

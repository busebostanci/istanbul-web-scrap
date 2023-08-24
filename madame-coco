import requests
import pandas as pd

headers = {
    cURL
}


url = "https://www.madamecoco.com/stores/?format=json&city=47"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()["results"]

    extracted_data = []
    for store in data:
        name = store.get("name")
        address = store.get("address")
        latitude = store.get("latitude")
        longitude = store.get("longitude")
        extracted_data.append([name, address, latitude, longitude])

    df = pd.DataFrame(extracted_data, columns=["Name", "Address", "Latitude", "Longitude"])

    excel_filename = "madamecoco.xlsx"
    df.to_excel(excel_filename, index=False)
    print(f"Data exported to '{excel_filename}'")
else:
    print("Failed to fetch data")

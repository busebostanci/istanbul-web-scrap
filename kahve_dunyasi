import requests
import pandas as pd


url = "https://core.kahvedunyasi.com/api/stores"
headers = {
    cURL 
}

response = requests.get(url, headers=headers)
data = response.json()

stores = data.get("payload", {}).get("stores", [])

data_list = []  # Initialize an empty list to hold the extracted data

for store in stores:
    branch_name = store.get("branch_name")
    latitude = store.get("latitude")
    longitude = store.get("longitude")
    address = store.get("address")

    if branch_name and latitude and longitude and address:
        data_list.append({
            "AD": branch_name,
            "ENLEM": latitude,
            "BOYLAM": longitude,
            "ADRES": address
        })

df = pd.DataFrame(data_list)

excel_file_path = "kahvedunyasi.xlsx"
df.to_excel(excel_file_path, index=False)
print(f"Data exported to '{excel_file_path}'")

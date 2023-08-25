import json
import requests
import pandas as pd

# Set the cURL headers as a dictionary
headers = {
  cURL
}

url = "https://www.koton.com/stores/?format=json"
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    json_data = response.json()

    # Get the "results" list from the JSON data
    results = json_data.get("results", [])
    filtered_stores = [store for store in results if store.get("township", {}).get("city", {}).get("pk") == 40]

    # Extract latitude, longitude, and store name from filtered_stores
    store_info = []
    for store in filtered_stores:
        latitude = store.get("latitude")
        longitude = store.get("longitude")
        name = store.get("name")
        address = store.get("address")

        # Create a dictionary for each store's information
        store_info.append({
            "name": name,
            "latitude": latitude,
            "longitude": longitude,
            "address": address
        })

        # Create a pandas DataFrame from the store information
        df = pd.DataFrame(store_info)

        # Save the DataFrame to an Excel file
        excel_filename = "koton.xlsx"
        df.to_excel(excel_filename, index=False)

        print(f"Data has been exported to {excel_filename}.")
        print("Total Stores:", len(store_info))
    else:
        print("Request was not successful. Status code:", response.status_code)

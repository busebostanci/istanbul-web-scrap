


import requests
import pandas as pd

# List of district isocodes
district_isocodes = [
    "D_ISTANBUL_ADALAR",
    "D_ISTANBUL_ARNAVUTKOY",
    "D_ISTANBUL_ATASEHIR",
    "D_ISTANBUL_AVCILAR",
    "D_ISTANBUL_BAGCILAR",
    "D_ISTANBUL_BAHCELIEVLER",
    "D_ISTANBUL_BAKIRKOY",
    "D_ISTANBUL_BASAKSEHIR",
    "D_ISTANBUL_BAYRAMPASA",
    "D_ISTANBUL_BESIKTAS",
    "D_ISTANBUL_BEYKOZ",
    "D_ISTANBUL_BEYLIKDUZU",
    "D_ISTANBUL_BEYOGLU",
    "D_ISTANBUL_BUYUKCEKMECE",
    "D_ISTANBUL_CATALCA",
    "D_ISTANBUL_CEKMEKOY",
    "D_ISTANBUL_ESENLER",
    "D_ISTANBUL_ESENYURT",
    "D_ISTANBUL_EYUPSULTAN",
    "D_ISTANBUL_FATIH",
    "D_ISTANBUL_GAZIOSMANPASA",
    "D_ISTANBUL_GUNGOREN",
    "D_ISTANBUL_KADIKOY",
    "D_ISTANBUL_KAGITHANE",
    "D_ISTANBUL_KARTAL",
    "D_ISTANBUL_KUCUKCEKMECE",
    "D_ISTANBUL_MALTEPE",
    "D_ISTANBUL_PENDIK",
    "D_ISTANBUL_SANCAKTEPE",
    "D_ISTANBUL_SARIYER",
    "D_ISTANBUL_SILIVRI",
    "D_ISTANBUL_SULTANBEYLI",
    "D_ISTANBUL_SULTANGAZI",
    "D_ISTANBUL_SILE",
    "D_ISTANBUL_SISLI",
    "D_ISTANBUL_TUZLA",
    "D_ISTANBUL_UMRANIYE",
    "D_ISTANBUL_USKUDAR",
    "D_ISTANBUL_ZEYTINBURNU"
]

# Headers for the cURL command
headers = {
    curl
}

data_list = []

for district_isocode in district_isocodes:
    # Construct the custom cURL command
    url = f"https://www.mavi.com/magazalar/get-stores?province={district_isocode}&district={district_isocode}&page=0"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        all_store_data = data.get("allStoreData", [])

        for store_data in all_store_data:
            results = store_data.get("results", [])

            if not results:
                print("No store data found in the response.")
            else:
                for store in results:
                    display_name = store.get("displayName")
                    latitude = store.get("geoPoint", {}).get("latitude")
                    longitude = store.get("geoPoint", {}).get("longitude")

                    data_list.append({
                        "District Isocode": district_isocode,
                        "Display Name": display_name,
                        "Latitude": latitude,
                        "Longitude": longitude
                    })

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)
    except ValueError as ve:
        print("An error occurred while parsing the JSON response:", ve)

df = pd.DataFrame(data_list)

# Write the DataFrame to an Excel file
excel_filename = "mavi_store_data.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data has been saved to {excel_filename}")

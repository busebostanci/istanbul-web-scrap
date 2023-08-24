import requests
import pandas as pd

base_url = "https://frontend.dominos.com.tr/api/store/availableByUrl-v2"
city_url = "istanbul"

headers = {
   cURL 
}

params = {
    "cityUrl": city_url,
}

# Retrieve district URLs
district_response = requests.get("https://frontend.dominos.com.tr/api/address/searchCityDistricts", headers=headers, params=params)

if district_response.status_code == 200:
    district_data = district_response.json()
    district_names = [district.get("districtUrl") for district in district_data if district.get("districtUrl")]
else:
    print(f"Failed to retrieve district data. Status code: {district_response.status_code}")
    district_names = []

store_info_list = []

for district_name in district_names:
    # Construct the API URL for the specific district
    api_url = f"{base_url}?cityUrl={city_url}&districtUrl={district_name}"

    # Send a GET request to the API
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for store in data:  # Loop through the list of dictionaries directly
            store_info_list.append({
                "StoreName": store.get("name"),
                "Latitude": store.get("lattitude"),
                "Longitude": store.get("longitude"),
            })
    else:
        print(f"Failed to retrieve data for {district_name}")

# Create a DataFrame
df = pd.DataFrame(store_info_list)

# Save DataFrame to Excel
excel_file = "as.xlsx"
df.to_excel(excel_file, index=False)

print(f"Store information saved to {excel_file}")

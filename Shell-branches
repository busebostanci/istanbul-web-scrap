import requests
import pandas as pd

url = "https://shellretaillocator.geoapp.me/api/v2/locations/within_bounds?sw%5B%5D=40.223768&sw%5B%5D=28.212237&ne%5B%5D=41.778278&ne%5B%5D=29.242206&locale=tr_TR&format=json"

headers = {
    cURL. 
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    locations = data.get("locations", [])  # Extract the "locations" list from the data

    extracted_data = []
    for location in locations:
        extracted_location = {
            "name": location.get("name"),
            "lat": location.get("lat"),
            "lng": location.get("lng"),
            "city": location.get("city"),
        }
        extracted_data.append(extracted_location)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(extracted_data)

    # Save the DataFrame to an Excel file
    excel_filename = "extracted_data.xlsx"
    df.to_excel(excel_filename, index=False)

    print(f"Data saved to {excel_filename}")
else:
    print(f"Request failed with status code: {response.status_code}")

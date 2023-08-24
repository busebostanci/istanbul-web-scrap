import requests
import pandas as pd

url = "https://www.tavukdunyasi.com/Restaurant/GetRestaurantByCountyId"
headers = {
   cURL 
}

county_ids = [
    "0e03680f-e7ef-ceeb-4bbc-08d661b7cfaf",
    "50e7fe5f-6fe9-c7f3-3a0e-08d542f68f09",
    "caa4aa86-14c0-ca08-4f2a-08d542f5d4e9",
    "98eb4bf0-66d5-c5f8-a0d0-08dad1673e85",
    "ed551ded-36d4-cd21-91b0-08d542f56d55",
    "041bb722-3fbd-cc52-4df0-08d65aa2f823",
    "4f0ceac4-71db-c256-8043-08d4fc2c8149",
    "27cf7abc-a40c-ce58-9d3c-08d542f66416",
    "71ad6791-8077-c2a0-1ed4-08d542f5cd3f",
    "e9c71226-938d-cd25-acdb-08d5b1934b50",
    "c3b581e7-e06a-c57b-3634-08d5ac4ee13a",
    "767fa506-be61-cef4-d810-08d542f57588",
    "da7a1af1-a268-c829-8d7b-08d93ad845e3",
    "262d0a82-d2a0-cce1-9e59-08d9265d2d41",
    "1424e49d-a91f-c140-c020-08d9d2b50d9a",
    "d8719b00-28cd-ce8a-3b3d-08da59c11dbc",
    "3c1879e6-4f61-c7ac-1fdc-08d542f590ef",
    "c4997c5e-0112-c659-9d14-08d542f5b202",
    "93331360-0235-c695-68a7-08d542f62695",
    "dcf12c74-9b8d-c54f-910b-08d661b6c332",
    "5d401b4a-b6e2-c0cc-d270-08d4f6be739e",
    "54043eef-a473-c1b2-5030-08d542f5c410",
    "00bd16d2-ea82-c7fd-1de2-08d542f63890",
    "653dc0b3-12a1-ca3b-de9c-08d542f59e0a",
    "370f765b-8f4a-c38f-6bac-08d542f66f0a",
    "5bb5a805-68d8-c97a-0708-08d542f65b21",
    "1e2c162c-0674-c706-3a66-08d542f6c470",
    "ff76f6ac-23d7-cb39-958c-08d542f5f4f5",
    "32a86077-6a07-cb56-c4de-08db728c7fde",
    "1134a343-143f-c49f-e631-08d542f5a918",
    "9459b0c5-3759-c95d-ff7c-08d86eb4320a",
    "38126f4d-64f0-ca5a-ab40-08d542f5e7e6",
    "d0b9bb75-e059-c36d-a551-08d542f6da56",
    "456b5e4e-f638-c4fe-52c4-08d542f5dddb",
    "6b052a3d-8066-cba8-ee9c-08d542f582ac",
    "4c2fd982-ed48-c981-5c76-08d542f69f41"
]

city_id = "de179cdb-e881-c42c-34ae-08d4f6bdffae"
country_id = "8b2f74ed-34ca-c1b2-6a50-08d4f6bcdc77"

data_list = []

for county_id in county_ids:
    data = {
        "countyId": county_id,
        "countryId": country_id,
        "cityId": city_id,
    }

    response = requests.post(url, headers=headers, data=data)

    try:
        json_response = response.json()
        restaurant_list = json_response.get("RestaurantList", [])
    except ValueError as e:
        print("Error parsing JSON:", e)
        print("Response content:", response.text)
        restaurant_list = []

    for restaurant in restaurant_list:
        title = restaurant.get("Title")
        longitude = restaurant.get("Longitude")
        latitude = restaurant.get("Latitude")
        address = restaurant.get("Address")
        data_list.append([title, longitude, latitude, address])

# Create a pandas DataFrame from the data list
df = pd.DataFrame(data_list, columns=["Title", "Longitude", "Latitude", "Address"])

# Export the DataFrame to an Excel file
excel_filename = "tavukcuk_dunyasi.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data exported to '{excel_filename}'")

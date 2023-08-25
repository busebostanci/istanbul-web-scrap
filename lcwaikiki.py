import requests
import json
import pandas as pd

url = "https://corporate.lcwaikiki.com/Content/WebService/ClientSiteWebService.asmx/GetStoresByTown"

headers = {
    cURL was removed. insert it. 
}

town_ids = ['1087', '997', '998', '999', '974', '1080', '996', '975', '1078', '977', '991', '979', '1004', '1079', '980', '981', '982', '1000', '992', '993', '985', '986', '1094', '988', '990', '1071', '1073', '983', '984', '1001', '994', '1088', '1002', '1003', '995', '1072']

data_list = []

for town_id in town_ids:
    if town_id in ['1071', '1073', '983', '984', '1001', '994', '1088', '1002', '1003', '995', '1072']:
        city_id = "1"
    else:
        city_id = "247"

    data = {
        "TownID": town_id,
        "CityID": city_id,
        "CountryID": "1",
        "Type": "Bayi"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        stores = result.get("d", [])
        for store in stores:
            data_list.append({
                "TownID": town_id,
                "Name": store.get("Name", ""),
                "Latitude": store.get("Latitude", ""),
                "Longitude": store.get("Longitude", ""),
                "Address": store.get("Address", ""),
            })

# Create a DataFrame from the data
df = pd.DataFrame(data_list)

# Export the DataFrame to an Excel file
excel_file = "LCW3.xlsx"
df.to_excel(excel_file, index=False)

print(f"Data exported to {excel_file}")

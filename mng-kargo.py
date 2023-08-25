import requests
import pandas as pd

headers = {
   curl
}
district_codes = ['100', '101', '94', '95', '96', '97', '98', '99', '23', '24', '25', '26', '27', '29', '32', '35',
                  '38', '41', '44', '50', '51', '53', '56', '57', '59', '61', '64', '67', '68', '70', '73', '76', '77',
                  '79', '81', '82', '84', '87', '93']

url = "https://www.mngkargo.com.tr/DeliveryPoint/GetCloseDeliveryPoint"

data_list = []

for district_code in district_codes:
    data = {
        "cityCode": "34",
        "districtCode": district_code
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_data = response.json()
        for point in json_data:
            address = point.get("address")
            branch_name = point.get("branchName")
            latitude = point.get("latitude")
            longitude = point.get("longitude")
            data_list.append([district_code, address, branch_name, latitude, longitude])
    else:
        print("Request failed for district code:", district_code, "with status code:", response.status_code)

# Create a DataFrame from the data list
df = pd.DataFrame(data_list, columns=['District Code', 'Address', 'Branch Name', 'Latitude', 'Longitude'])

# Export DataFrame to Excel
excel_filename = "mng.xlsx"
df.to_excel(excel_filename, index=False)

print("Data exported to:", excel_filename)

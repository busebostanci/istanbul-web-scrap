import requests
import pandas as pd

ilce_ids = [
    "34000001000",
    "34000033000",
    "34000034000",
    "34000002000",
    "34000004000",
    "34000005000",
    "34000003000",
    "34000035000",
    "34000006000",
    "34000007000",
    "34000008000",
    "34000036000",
    "34000009000",
    "34000029000",
    "34000032000",
    "34000037000",
    "34000027000",
    "34000038000",
    "34000011000",
    "34000012000",
    "34000013000",
    "34000014000",
    "34000015000",
    "34000016000",
    "34000017000",
    "34000018000",
    "34000019000",
    "34000020000",
    "34000039000",
    "34000021000",
    "34000031000",
    "34000028000",
    "34000040000",
    "34000030000",
    "34000022000",
    "34000023000",
    "34000024000",
    "34000025000",
    "34000026000"
]

url = "http://www.suratkargo.com.tr/Default/GetIlceVM"
headers = {
   cURL
}
url = "http://www.suratkargo.com.tr/Default/GetIlceVM"
headers = {
   cURL
}

data_list = []

for ilce_id in ilce_ids:
    data = {
        "ILCE_ID": ilce_id
    }

    response = requests.post(url, headers=headers, data=data, verify=False)

    if response.status_code == 200:
        try:
            json_data = response.json()
            if json_data.get("success") and "message" in json_data:
                locations = json_data["message"]
                for location in locations:
                    adi = location.get("Adi")
                    enlem = location.get("Enlem")
                    boylam = location.get("Boylam")
                    adres = location.get("Adres")

                    data_list.append([ilce_id, adi, enlem, boylam, adres])
        except ValueError:
            print("Error parsing JSON response")

# Create a DataFrame using pandas
df = pd.DataFrame(data_list, columns=["ILCE_ID", "Adi", "Enlem", "Boylam", "Adres"])

# Save the DataFrame to an Excel file
excel_path = "location_data_pandas.xlsx"
df.to_excel(excel_path, index=False)
print("Data saved to", excel_path)

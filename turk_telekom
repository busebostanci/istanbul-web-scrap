import requests
import pandas as pd

url = "https://www.turktelekom.com.tr/_layouts/15/TTWebsite/Partners/Ajax.aspx/GetPartnersAll"
headers = {
    cURL
}

data = {
    "IsCorporate": False,
}

response = requests.post(url, headers=headers, json=data)
json_data = response.json()

# Extract and store specific fields for entries where "City" is "Istanbul"
data_list = json_data.get("d", {}).get("Data", [])
istanbul_data = [entry for entry in data_list if entry.get("City") == "İSTANBUL"]

# Create a DataFrame from the extracted Istanbul data
df = pd.DataFrame(istanbul_data, columns=["CommercialName", "PType", "CoordinateX", "CoordinateY", "City", "District"])

# Save the DataFrame to an Excel file
excel_file_path = "istanbul_partner_data.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Istanbul data saved to '{excel_file_path}'")

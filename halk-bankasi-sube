import json
import pandas as pd


# Your JSON data
json_data = '''
{"data":[{ fill in the response json data at your own. }] '''


data = json.loads(json_data)

branch_data = []
for item in data['data']:
    branch_name = item['branchName']
    address = item['address']
    latitude = item['latitude']
    longitude = item['longitude']
    branch_data.append((branch_name, address, latitude, longitude))

df = pd.DataFrame(branch_data, columns=['Branch Name', 'Address', 'Latitude', 'Longitude'])

# Export DataFrame to Excel
excel_filename = 'halkbankasısube.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data exported to {excel_filename}")

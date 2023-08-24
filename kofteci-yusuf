import json
import pandas as pd

response_json = '''
[{response_json was taken and removed due to sensitive info}]
'''

locations = json.loads(response_json)

data = []

for location in locations:
    title = location["title"]
    latitude = location["latitude"]
    longitude = location["longitude"]
    data.append({"Name": title, "Latitude": latitude, "Longitude": longitude})

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write DataFrame to an Excel file
excel_filename = "kofteciyusuf.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data has been written to {excel_filename}")

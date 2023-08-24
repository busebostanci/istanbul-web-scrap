import pandas as pd

response = [
  response was taken and was removed due to legal purposes. then response was filtered to remove backslashes which were preventing code to run. also "true" and "false" were converted into "True" and "False"
so that python could recognize. 
]
data = []

for branch in response:
    longitude = branch["Longitude"]
    latitude = branch["Latitude"]
    name = branch["Name"]
    address = branch["Address"]

    data.append({
        "Name": name,
        "Address": address,
        "Longitude": longitude,
        "Latitude": latitude
    })

df = pd.DataFrame(data)

# Export DataFrame to Excel
excel_filename = "garanti.xlsx"
df.to_excel(excel_filename, index=False)

print("Data exported to", excel_filename)

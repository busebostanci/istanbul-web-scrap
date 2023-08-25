import pandas as pd



locations = [ {# VERİLER AĞ>DOKUMAN> VAR LOCATION dan çekidi }]

store_names = []
latitudes = []
longitudes = []

for location in locations:
    store_name = location.get('store_name')
    latitude = location.get('latitude')
    longitude = location.get('longitude')

    # Append the extracted information to the lists
    store_names.append(store_name)
    latitudes.append(latitude)
    longitudes.append(longitude)

data = {
    'Store Name': store_names,
    'Latitude': latitudes,
    'Longitude': longitudes
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
excel_filename = 'rosmann.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data has been exported to {excel_filename}")

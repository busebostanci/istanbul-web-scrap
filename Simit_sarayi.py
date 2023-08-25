import requests
import pandas as pd

url = "https://www.simitsarayi.com/Service/GetStores?isLocal=true&lang=tr"

headers = {
    cURL
}

response = requests.get(url, headers=headers)
data = response.json()

filtered_data = []
for store in data:
    if store["city"] == "İSTANBUL":
        filtered_data.append({
            "name": store["name"],
            "address": store["address"],
            "lat": store["lat"],
            "lng": store["lng"]
        })

df = pd.DataFrame(filtered_data)

excel_filename = "simitsarayi.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data exported to '{excel_filename}'")

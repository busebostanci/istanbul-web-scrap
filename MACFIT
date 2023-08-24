import requests
import pandas as pd

url = "https://www.macfit.com/services/branchlist.php"

headers = {
    insert cURL
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    branches = data.get("data", [])  # Access the "data" field or provide an empty list if not present
    istanbul_branches = [branch for branch in branches if branch.get("city") == "İstanbul"]

    istanbul_data = []
    for branch in istanbul_branches:
        name = branch.get("name")
        latitude = branch.get("latitude")
        longitude = branch.get("longitude")
        istanbul_data.append({"Name": name, "Latitude": latitude, "Longitude": longitude})

        df = pd.DataFrame(istanbul_data)

        excel_file = "macfit.xlsx"
        df.to_excel(excel_file, index=False)
        print(f"Data exported to '{excel_file}'")
else:
    print(f"Request failed with status code: {response.status_code}")

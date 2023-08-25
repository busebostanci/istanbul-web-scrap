import requests
import pandas as pd

headers = {
 please insert the cURL here
}


url = "https://www.vestel.com.tr/lookup/offlinestores?cityID=34&districtID=&_=1692268607621"

response = requests.get(url, headers=headers)
data = response.json()
filtered_data = []
for result in data.get("Result", []):
    if result.get("IL") == "İSTANBUL":
        filtered_data.append({
            "ADI": result.get("MAGAZATITLE"),
            "ADRES": result.get("ADRES"),
            "ENLEM": result.get("Lat"),
            "BOYLAM": result.get("Long")
        })

    df = pd.DataFrame(filtered_data)

    # Export to Excel
    excel_file = "vestel.xlsx"
    df.to_excel(excel_file, index=False)

    print("Data exported to", excel_file)

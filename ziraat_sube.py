import requests
import json
import pandas as pd

def get_branches():
    data = requests.get("https://www.ziraatbank.com.tr/tr/_layouts/15/Ziraat/SubeATM/Ajax.aspx/GetAllSubeText")
    data = json.loads(data.text)

    raw_data = data["d"]["Data"]
    data_points = raw_data.split("|")
    num_points = len(data_points)
    parsed_data = []

    for i in range(0, num_points, 8):
        point_data = {
            "Latitude": float(data_points[i+1]),
            "Longitude": float(data_points[i+2]),
            "Branches_Code": float(data_points[i+7])
        }
        parsed_data.append(point_data)

    return parsed_data

def get_atms():
    url = "https://www.ziraatbank.com.tr/tr/_layouts/15/Ziraat/SubeATM/Ajax.aspx/GetAllAtmText"
    headers = {
        'origin': 'https://www.ziraatbank.com.tr',
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    raw_data = data["d"]["Data"]
    data_points = raw_data.split("|")
    num_points = len(data_points)
    parsed_data = []

    for i in range(0, num_points, 7):
        point_data = {
            "latitude": float(data_points[i+1]),
            "longitude": float(data_points[i+2]),
            "Branches_Code": float(data_points[i + 7])
        }
        parsed_data.append(point_data)

    return parsed_data

branches = get_branches()
atms = get_atms()

# Create Excel file and export data to separate sheets
with pd.ExcelWriter('ziraat_data.xlsx') as writer:
    branches_df = pd.DataFrame(branches)
    branches_df.to_excel(writer, sheet_name='Branches', index=False)

    atms_df = pd.DataFrame(atms)
    atms_df.to_excel(writer, sheet_name='ATMs', index=False)

print("Data exported to 'ziraat_data.xlsx' file.")

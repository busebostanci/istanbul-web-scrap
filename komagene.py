import requests
import pandas as pd

# Define the cURL headers and data for the requests
headers = {
    cURL
}

data = {
    "CityId": None,
    "langId": 1,
}

urls = [
    {
        "url": "https://www.komagene.com.tr/tr/Page/GetFranchiseDropDown",
        "CityId": 83,
    },
    {
        "url": "https://www.komagene.com.tr/tr/Page/GetFranchiseDropDown",
        "CityId": 48,
    },
]

responses = []

for url_info in urls:
    data["CityId"] = url_info["CityId"]
    response = requests.post(url_info["url"], headers=headers, data=data)
    responses.append(response.json())

# Create a Pandas DataFrame from the responses
df_list = []

for idx, response in enumerate(responses):
    df = pd.DataFrame(response)
    df["CityId"] = urls[idx]["CityId"]
    df_list.append(df)

final_df = pd.concat(df_list, ignore_index=True)

# Save the DataFrame to an Excel file
excel_file = "output.xlsx"
final_df.to_excel(excel_file, index=False)

print(f"Data saved to {excel_file}")

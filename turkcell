import requests
from bs4 import BeautifulSoup
import pandas as pd

# Part 1: Fetching Option Values
url_option_values = "https://www.turkcell.com.tr/tr/hakkimizda/iletisim/ilceler?cityId=34"
headers_option_values = {
    cURL
}

response_option_values = requests.get(url_option_values, headers=headers_option_values)

if response_option_values.status_code == 200:
    soup_option_values = BeautifulSoup(response_option_values.content, "html.parser")

    options = soup_option_values.find_all("option")  # Adjust the selector as needed
    option_values = []

    for option in options:
        if option.has_attr("value"):
            option_values.append(option["value"])

    print("Option values:", option_values)
else:
    print("Failed to retrieve option values. Status code:", response_option_values.status_code)

# Part 2: Scraping Data for Each County ID
url_base = "https://www.turkcell.com.tr/tr/hakkimizda/iletisim/turkcell-iletisim"

headers = {
    cURL
}

data_list = []

for county_id in option_values:
    data = {
        "type": "SEARCH_TIM",
        "cityId": "34",
        "countyId": county_id,
        "deviceId": ""
    }

    response = requests.post(url_base, headers=headers, data=data)
    soup = BeautifulSoup(response.content, "html.parser")

    store_elements = soup.select(".store")
    for store_element in store_elements:
        data_lat = store_element["data-lat"]
        data_lng = store_element["data-lng"]
        h3_content = store_element.select_one("h3").get_text(strip=True)

        data_list.append({"County ID": county_id, "data-lat": data_lat, "data-lng": data_lng, "h3 content": h3_content})

# Create a pandas DataFrame
df = pd.DataFrame(data_list)

# Export to Excel
excel_filename = "TurkCell_data.xlsx"
df.to_excel(excel_filename, index=False, encoding="utf-8")

print(f"Data exported to {excel_filename}")

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.colins.com.tr/stores/mapstore/?cityId=34"
headers = {
  cURL 
}

response = requests.get(url, headers=headers)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

data = []
for location_item in soup.find_all("li", class_="location-item"):
    data_geo_lat = location_item.get("data-geo-lat")
    data_geo_long = location_item.get("data-geo-long")
    location_title_div = location_item.find("div", class_="location-title")
    location_title = location_title_div.get_text(strip=True) if location_title_div else ""
    location_directions = location_item.find("div", class_="location-directions").get_text(strip=True)

    data.append({
        "data-geo-lat": data_geo_lat,
        "data-geo-long": data_geo_long,
        "location-title": location_title,
        "location-directions": location_directions
    })

df = pd.DataFrame(data)

excel_file = "defactoo.xlsx"
df.to_excel(excel_file, index=False)
print(f"Data exported to {excel_file}")

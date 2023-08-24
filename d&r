import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.dr.com.tr/magazalar"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

store_divs = soup.find_all("div", class_="col-md-6 col-lg-4 col-12")

store_data = []

target_ids = ["tr_İstanbul-Avrupa", "tr_İstanbul-Anadolu"]

for store_div in store_divs:
    store_id = store_div.get("id")
    if store_id in target_ids:
        store_info = store_div.find("div", class_="stores-info")
        store_name = store_info.find("h2").text.strip()
        store_address = store_info.find("p").get_text(separator="\n").strip()

        # Ayırmak için T: ile ayrıştırma yap
        address_parts = store_address.split("T:")
        if len(address_parts) > 1:
            address = address_parts[0].strip()
            phone = "T:" + address_parts[1].strip()
        else:
            address = store_address
            phone = ""

        store_data.append({
            "AD": store_name,
            "ADRES": address,
            "TELEFON": phone
        })

df = pd.DataFrame(store_data)
excel_file = "store_data3.xlsx"
df.to_excel(excel_file, index=False)

print(f"Data saved to {excel_file}")

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def main():
    url = "http://mado.com.tr/yurt-ici-subeler/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content

        soup = BeautifulSoup(html_content, "html.parser")

        h2_elements = soup.find_all("h2", class_="elementor-heading-title")

        branches = []

        for h2 in h2_elements:
            branch_name = h2.text.strip()

            iframe = h2.find_next("iframe")
            if iframe and "title" in iframe.attrs:
                address = iframe["title"]

                branch_data = {
                    "branch_name": branch_name,
                    "address": address
                }

                branches.append(branch_data)

        df = pd.DataFrame(branches)
        df.to_excel("mado.xlsx", index=False)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

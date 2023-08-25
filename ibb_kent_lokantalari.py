from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import geopandas as gpd

GOOGLE_API_KEY = "**************"

browser = webdriver.Chrome()
url = "https://tesislerimiz.ibb.istanbul/kent-lokantasi/"
browser.get(url)

page_source = browser.page_source

soup = BeautifulSoup(page_source, 'html.parser')

lokanta_adlari = soup.find_all('a', {"class": "av-masonry-item-with-image"})
for lokanta in lokanta_adlari:

    link = lokanta.get('href')
    name = lokanta.text.strip()

    browser.get(link)

    lokanta_adres = lokanta.find('h3', {"class": "av-masonry-entry-title"})
    print(lokanta_adres.text.strip())
    page_source = browser.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    adreses = soup.find_all('h3', {"class": "iconbox_content_title"})
    for adres in adreses:
        yeter = adres.text.strip()

        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + name + " " + yeter + "************"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        json_data = response.json()

        try:
            # print(json_data['results'][0]['geometry']['location'])
            lat = json_data['results'][0]['geometry']['location']['lat']
            lng = json_data['results'][0]['geometry']['location']['lng']

            print("lat:",lat)
            print("long:",lng)

        except:
            print("error")

        print(yeter)

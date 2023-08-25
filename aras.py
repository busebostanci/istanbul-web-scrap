import requests

url = "https://kurumsalwebservice.araskargo.com.tr/api/getCityWithTown"
headers = {
  cURL
}

data = {
    "search": "istanbul"
}
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    api_data = response.json()

    for city in api_data:
        town_name = city.get("townName")
        town_ids = city.get("townId")

        print(town_ids)
else:
    print(f"Request failed with status code: {response.status_code}")

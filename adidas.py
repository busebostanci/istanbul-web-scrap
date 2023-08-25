import pandas as pd
import requests

# Define the CURL command as a dictionary
headers = {
    cURL 
}


url = "https://placesws.adidas-group.com/API/search?brand=adidas&geoengine=google&method=get&category=store&latlng=41.08940927626936%2C28.873032820369126%2C61&page=1&pagesize=500&fields=name%2Cstreet1%2Cstreet2%2Caddressline%2Cbuildingname%2Cpostal_code%2Ccity%2Cstate%2Cstore_owner%2Ccountry%2Cstoretype%2Clongitude_google%2Clatitude_google%2Cstore_owner%2Cstate%2Cperformance%2Cbrand_store%2Cfactory_outlet%2Coriginals%2Cneo_label%2Cy3%2Cslvr%2Cchildren%2Cwoman%2Cfootwear%2Cfootball%2Cbasketball%2Coutdoor%2Cporsche_design%2Cmiadidas%2Cmiteam%2Cstella_mccartney%2Ceyewear%2Cmicoach%2Copening_ceremony%2Coperational_status%2Cfrom_date%2Cto_date%2Cdont_show_country&format=json&storetype="

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  # Parse JSON response

    if "wsResponse" in data and "result" in data["wsResponse"]:
        stores = data["wsResponse"]["result"]
        extracted_data = []

        for store in stores:
            if "city" in store and "İSTANBUL" in store["city"].upper():
                name = store.get("name", "")
                street1 = store.get("street1", "")
                addressline = store.get("addressline", "")
                longitude_google = store.get("longitude_google", "")
                latitude_google = store.get("latitude_google", "")

                extracted_data.append({
                    "Name": name,
                    "Street1": street1,
                    "Addressline": addressline,
                    "Longitude (Google)": longitude_google,
                    "Latitude (Google)": latitude_google
                })

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(extracted_data)

        # Export the DataFrame to an Excel file
        excel_filename = "istanbul_adidas_store_data4.xlsx"
        df.to_excel(excel_filename, index=False)
        print(f"Data exported to {excel_filename} successfully.")
    else:
        print("No store data found in the response.")
else:
    print("Failed to retrieve data from the URL.")

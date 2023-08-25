from bs4 import BeautifulSoup
import pandas as pd

html = """
html response was taken due to clarity and was removed, fill it. 
"""

soup = BeautifulSoup(html, 'html.parser')

data = []
items = soup.find_all('div', class_='item')

for item in items:
    title = item.find('div', class_='title').text
    address = item.find('div', class_='text2').text
    data.append({'Name': title, 'Address': address})

df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
excel_filename = 'ozsut.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data has been exported to {excel_filename}")

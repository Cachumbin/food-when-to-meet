import requests
from bs4 import BeautifulSoup
import json

url = "https://somosthegula.com/bogotaeats-a-cielo-abierto/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

menu_data = []
menu_container = soup.find('div', class_='dce-menu-list-items')

if menu_container:
    current_category = "Uncategorized"
    for child in menu_container.find_all(recursive=False):
        if 'dce-menu-list-category' in child.get('class', []):
            category_title = child.find('h3', class_='dce-menu-list-category-title')
            if category_title:
                current_category = category_title.get_text(strip=True)
        
        elif 'dce-menu-list-item' in child.get('class', []):
            title = child.find('div', class_='dce-menu-list-item-title').get_text(strip=True)
            price = child.find('div', class_='dce-menu-list-item-price').get_text(strip=True)
            description_tag = child.find('div', class_='dce-menu-list-item-description')
            description = description_tag.get_text(strip=True) if description_tag else ""

            menu_data.append({
                'category': current_category,
                'name': title,
                'price': price,
                'description': description
            })

print(json.dumps(menu_data, indent=2, ensure_ascii=False))
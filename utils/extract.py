import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def extract_data(url="https://fashion-studio.dicoding.dev/", total_pages=50):
    """
    Melakukan ekstraksi data dari website.
    """
    all_products = []
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    try:
        for page in range(1, total_pages + 1):
            target_url = f"{url}?page={page}"
            response = session.get(target_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('div', class_='collection-card')
            
            for card in cards:
                details = card.find('div', class_='product-details')
                if not details: 
                    continue
                
                title_elem = details.find('h3', class_='product-title')
                price_elem = details.find(class_='price')
                
                if not title_elem or not price_elem:
                    continue

                data = {
                    "Title": title_elem.get_text(strip=True),
                    "Price": price_elem.get_text(strip=True),
                    "Rating": "Rating: 0 / 5",
                    "Colors": "0 Colors",
                    "Size": "Size: -",
                    "Gender": "Gender: -",
                    "Timestamp": datetime.now().isoformat(), 
                }
        
                for p in details.find_all('p'):
                    txt = p.get_text(strip=True)
                    if "Rating:" in txt: data["Rating"] = txt
                    elif "Colors" in txt: data["Colors"] = txt
                    elif "Size:" in txt: data["Size"] = txt
                    elif "Gender:" in txt: data["Gender"] = txt
                
                all_products.append(data)
            
            if len(all_products) >= 1000: 
                break
            time.sleep(0.1)
            
        return all_products
    except Exception as e:
        print(f"Error pada tahap Extract: {e}")
        return None
# https://realpython.com/introduction-to-mongodb-and-python/
# https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/

import requests
from bs4 import BeautifulSoup
import json

## Ove dve funkcije bi mogle da idu u poseban py fajl i da se importuju
## Deo nakon funkcija bi ostao u ovom glavnom fajlu, koji ih koristi i ima logiku
def obradi_laptop(url):
    # .product-declaration table tbody tr > td:first-child   naziv
    # .product-declaration table tbody tr > td:last-child    vrednost
    # .product-specification ...isto
    
    specifikacija = {}
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    redovi = soup.select('.product-declaration table tbody tr')
    for red in redovi:
        naziv    = red.select('td:first-child')[0].text.strip()
        vrednost = red.select('td:last-child')[0].text.strip()
        specifikacija[naziv] = vrednost
        
    redovi = soup.select('.product-specification table tbody tr')
    for red in redovi:
        naziv    = red.select('td:first-child')[0].text.strip()
        vrednost = red.select('td:last-child')[0].text.strip()
        specifikacija[naziv] = vrednost

    # full-product-price  old-price   price
    specifikacija['stara cena'] = soup.select('.full-product-price .old-price')[0].text.strip()
    specifikacija['cena'] = soup.select('.full-product-price .price')[0].text.strip()

    laptop_data = {
        'url': url,
        'spec': specifikacija
    }
    
    return laptop_data

def smesti_u_bazu(laptop_data):
    #na kolekciju
    #laptopovi = db.laptopovi
    #unesi
    #result = laptopovi.insert_one(laptop_data)
    #vrati id
    #return result.inserted_id
    
    db = open('data.txt', 'a')
    json.dump(laptop_data, db)
    db.write("\n")
    db.close()

    return laptop_data

############# odavde pocinjem glavnu obradu
start_url = 'https://www.tehnomanija.rs/it-shop/laptop-racunari?filter_submited=1&show_filters=1&sort=default&filters%5Bprice_max%5D%5B%5D=140.138&filters%5BRezolucija%5D%5B%5D=1440x900&filters%5BRezolucija%5D%5B%5D=1920x1080&filters%5BRezolucija%5D%5B%5D=2560x1600&filters%5BMemorija%5D%5B%5D=8+GB&filters%5BMemorija%5D%5B%5D=12+GB&filters%5BMemorija%5D%5B%5D=16+GB&filters%5BHDMI%5D%5B%5D=da&filters%5Bstock%5D%5B%5D=dostupno&items_per_page=60'

page = requests.get(start_url)
soup = BeautifulSoup(page.content, 'html.parser')

# izdvajam sve linkove ka laptopovima
product_items = []
products = soup.select('.products-wrap a.product-link')
for link in products:
    link = link.get('href')
    product_items.append(link)

#print(product_items)

# sad pristupam svakom laptopu i izdvajam njegovu specifikaciju (tabela)
for url in product_items:
    print(url)
    l = obradi_laptop(url)
    smesti_u_bazu(l)

print("Kraj")

import requests
import pandas as pd
from datetime import datetime

date = datetime.now().strftime("%d_%m_%Y")
url = "https://product-cache.flip.ro/"

querystring = {"limit": "1135", "offset": "0", "sortBy": "suggestions", "sortDirection": "asc", "lang": "RO",
               "minPrice": "200", "maxPrice": "9149"}

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "/",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "AUTH_CODE": "Ortj05Xt9TwQ5xNasQ7u",
    "Origin": "https://flip.ro",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data = response.json()['data']['marketplace']
data_list = []
for i in data:
    prod_id = i['model_id']
    cond = i['shape']
    price = i['buy_price']
    retail_price = i['retail_price']
    brand = i['device']['brand']
    model = i['device']['model']
    storage = i['device']['storage']
    color = i['device']['color']
    processor = i['device']['processor']
    system = i['device']['system']
    sim = i['device']['sim']
    scraped_date = datetime.now().strftime("%d/%m/%y")

    data_list.append([
        prod_id,
        brand,
        model,
        cond,
        price,
        retail_price,
        storage,
        color,
        processor,
        system,
        sim,
        scraped_date
    ])

columns = ['ProdId', 'Brand', 'Model', "Conditie", "Pret", "Pret retail", "Spatiu stocare", 'Culoare', "Procesor", "System",
           "Sim"]
df = pd.DataFrame(data_list, columns=columns)
df.to_csv(f"D:/P/Webscrapers/BD/Flip_{date}.csv", index=False)

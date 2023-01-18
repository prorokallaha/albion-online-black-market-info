import time
import json
import requests

with open("items_db/items.json") as items:
    data = json.load(items)


def prices_json():
    arr_profit = []

    while True:
        for i in data:
            response_bm = requests.get(f"https://www.albion-online-data.com/api/v2/stats/Prices/{i}.json?locations=Black%20Market")
            response_lym = requests.get(f"https://www.albion-online-data.com/api/v2/stats/Prices/{i}.json?locations=Lymhurst")
            if response_bm.status_code or response_lym.status_code != 200: 
                jsondata_bm = json.loads(response_bm.text)
                jsondata_lym = json.loads(response_lym.text)
                name = i
                sell_price_bm = int(jsondata_bm[0]['sell_price_min'])
                sell_price_lym = int(jsondata_lym[0]['sell_price_min'])
                if sell_price_bm == 0 and sell_price_lym == 0:
                    continue
                elif sell_price_lym * 1.3 >= sell_price_bm and sell_price_bm != 0:
                    print(f"{name} - {sell_price_lym}(Lym) - {sell_price_bm}(BM)")
                else:
                    continue
            else:
                continue
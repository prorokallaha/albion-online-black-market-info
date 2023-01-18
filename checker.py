import time
import requests
import json
import os


def checker_items():
    while True:
        response = requests.get(url="https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/formatted/items.json")
        jsondata = json.loads(response.text)
        with open('items.json', 'w') as file:
            arr = []
            for i in jsondata:
                i = i['LocalizationNameVariable'].strip('@ITEMS')
                i = i.strip('_')
                arr.append(i)
            json.dump(arr, file, indent=4, ensure_ascii=False)
        with open('items_copy.json', 'w') as copy_file:
            arr = []
            for i in jsondata:
                i = i['LocalizationNameVariable'].strip('@ITEMS')
                i = i.strip('_')
                arr.append(i)
            json.dump(arr, copy_file, indent=4, ensure_ascii=False)
        if open('./items.json') == open('./items_copy.json'):
            os.remove('./items_copy.json')
            continue
        else:
            os.remove('./items.json')
            with open('items.json', 'w') as file:
                arr = []
                for i in jsondata:
                    i = i['LocalizationNameVariable'].strip('@ITEMS')
                    i = i.strip('_')
                    arr.append(i)
                json.dump(arr, file, indent=4, ensure_ascii=False)

            os.remove('./items_copy.json')
        time.sleep(86400)

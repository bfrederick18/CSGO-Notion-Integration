import json
import requests

headers = {'Content-Type': 'application/json'}


def get_item_list():
    # url = 'http://csgobackpack.net/api/GetItemsList/v2/?no_prices=yes&no_details=yes&details=no&prettyprint=yes'
    url = 'http://csgobackpack.net/api/GetItemsList/v2/?no_details=yes&details=no&prettyprint=yes'
    response = requests.get(url)
    response_json = response.json()

    with open('csgobackpack.json', 'w') as file:
        json.dump(response_json, file, indent=4, sort_keys=True)
        

def get_item_price_json(id):
    url = f'http://csgobackpack.net/api/GetItemPrice/?id={id}'
    response = requests.get(url)
    response_json = response.json()

    # print(response_json)
    return response_json
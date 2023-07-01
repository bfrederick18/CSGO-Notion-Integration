import json
import requests
from trm import trm_print

headers = {'Content-Type': 'application/json'}


def get_item_list():
    trm_print('Getting item list...')
    # url = 'http://csgobackpack.net/api/GetItemsList/v2/?no_prices=yes&no_details=yes&details=no&prettyprint=yes'
    url = 'http://csgobackpack.net/api/GetItemsList/v2/?no_details=yes&details=no&prettyprint=yes'
    response = requests.get(url)
    response_json = response.json()

    with open('csgobackpack.json', 'w') as file:
        json.dump(response_json, file, indent=4, sort_keys=True)

    trm_print('Done.')


def get_item_price_json(id):
    trm_print('Getting item price json...')
    url = f'http://csgobackpack.net/api/GetItemPrice/?id={id}'
    response = requests.get(url)
    response_json = response.json()

    # print(response_json)
    trm_print('Done.')
    return response_json

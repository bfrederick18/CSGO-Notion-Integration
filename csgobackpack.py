import json
import requests
from pin import new_pin, pin_print

headers = {'Content-Type': 'application/json'}


def get_item_list():
    pin = new_pin()
    url = 'http://csgobackpack.net/api/GetItemsList/v2/'
    payload = {
        'no_prices': 'yes',
        'no_details': 'yes',
        'details': 'no',
        'prettyprint': 'yes'
    }
    pin_print('Getting data...', pin)
    response = requests.get(url, json=payload)
    response_json = response.json()

    with open('csgobackpack.json', 'w') as file:
        json.dump(response_json, file, indent=4, sort_keys=True)

    # print(response_json)


def get_item_price(id):
    pin = new_pin()
    url = f'http://csgobackpack.net/api/GetItemPrice/?id={id}'

    pin_print('Getting data...', pin)
    response = requests.get(url)
    response_json = response.json()

    print(response_json)

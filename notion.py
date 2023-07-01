import os
import json
import requests
from pin import new_pin, pin_print

TOKEN = os.environ['TOKEN']

headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


def get_pages(db_id):
    pin = new_pin()
    url = f'https://api.notion.com/v1/databases/{db_id}/query'
    payload = {'page_size': 100}

    pin_print('Posting payload...', pin)
    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    data = {db_id: response_json}

    with open('dbs.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

    pin_print('Done.', pin)


def read_dbs(db_id):
    pin = new_pin()
    pin_print('Reading db...', pin)

    pages = {}
    with open('dbs.json', 'r') as file:
        data = json.load(file)
        pages = data[db_id]['results']

    pin_print('Done.', pin)
    return pages


def print_pages(db_id):
    pin = new_pin()
    pin_print('Printing pages...', pin)

    pages = read_dbs(db_id)
    for page in pages:
        props = page['properties']
        item_title = props['Item Name']['title']

        item_name = ''
        if len(item_title) > 0:
            item_name = item_title[0]['plain_text']

        id_name = props['ID Name']['formula']['string']
        print(id_name)

    pin_print('Done.', pin)
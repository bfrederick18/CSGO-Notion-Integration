import os
import json
import requests

TOKEN = os.environ['TOKEN']
ID_CURRENT_INV = os.environ['ID_CURRENT_INV']
ID_WISHLIST = os.environ['ID_WISHLIST']

headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


def get_pages(DB_ID):
    url = f'https://api.notion.com/v1/databases/{DB_ID}/query'
    payload = {'page_size': 100}

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    data = {DB_ID: response_json}

    print(json.dumps(response_json, indent=4))
    with open('dbs.json', 'w') as file:
        json.dump(data, file, indent=4, sort_keys=True)

    response_results = response_json['results']
    # print(len(response_results), response_results)

    # for result in response_results:
    #     print(json.dumps(result, indent=4, sort_keys=True), end='\n\n')

    return response_results


def print_pages(pages):
    for page in pages:
        props = page['properties']
        item_title = props['Item Name']['title']

        item_name = ''
        if len(item_title) > 0:
            item_name = item_title[0]['plain_text']

        id_name = props['ID Name']['formula']['string']

        print(id_name)


# print_pages(get_pages(ID_CURRENT_INV))
print_pages(get_pages(ID_WISHLIST))
from notion import add_page, get_pages, read_dbs, update_page
from csgobackpack import get_item_price_json


def item_price_json_to_add_data(response_json, id_name):
    data = {
        'ID Name': {
            'title': [{
                'text': {
                    'content': id_name
                }
            }]
        },
        'Average Price': {
            'number': float(response_json['average_price']),
            'type': 'number'
        },
        'Median Price': {
            'number': float(response_json['median_price']),
            'type': 'number'
        }
    }
    print(data)
    return data


def item_price_json_to_update_data(response_json):
    data = {
        'Average Price': {
            'number': float(response_json['average_price']),
            'type': 'number'
        },
        'Median Price': {
            'number': float(response_json['median_price']),
            'type': 'number'
        }
    }
    print(data)
    return data


def add_item(db_id, id_name):
    item_price_json = get_item_price_json(id_name)
    data = item_price_json_to_add_data(item_price_json, id_name)
    add_page(db_id, data)


def id_name_to_page_id(db_id, id_name):
    get_pages(db_id)
    pages = read_dbs(db_id)
    for page in pages:
        props = page['properties']
        plain_text = props['ID Name']['title'][0]['plain_text']
        if id_name == plain_text:
            return page['id']
    return ''

def update_item(db_id, id_name):
    item_price_json = get_item_price_json(id_name)
    print(item_price_json)
    data = item_price_json_to_update_data(item_price_json)
    page_id = id_name_to_page_id(db_id, id_name)
    update_page(page_id, data)
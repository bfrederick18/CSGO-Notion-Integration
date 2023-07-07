from notion import add_page, get_pages, read_dbs, update_page
from csgobackpack import get_item_price_json


def item_price_json_to_data(response_json, id_name=''):
    data = {
        'Average Price': {
            'number': float(response_json['average_price']),
            'type': 'number'
        },
        'Median Price': {
            'number': float(response_json['median_price']),
            'type': 'number'
        },
        'Amount Sold': {
            'number': float(response_json['amount_sold']),
            'type': 'number'
        }
    }

    if id_name != '':
        data['ID Name'] = {'title': [{'text': {'content': id_name}}]}

    print(data)
    return data


def add_item(db_id, id_name):
    item_price_json = get_item_price_json(id_name)
    data = item_price_json_to_data(item_price_json, id_name)
    add_page(db_id, data)


def update_item(db_id, id_name, page_id):
    item_price_json = get_item_price_json(id_name)
    data = item_price_json_to_data(item_price_json)
    update_page(page_id, data)


def refresh_item(db_id, id_name):
    get_pages(db_id)
    pages = read_dbs(db_id)
    for page in pages:
        props = page['properties']
        plain_text = props['ID Name']['title'][0]['plain_text']
        if id_name == plain_text:
            update_item(db_id, id_name, page['id'])
            return
    add_item(db_id, id_name)
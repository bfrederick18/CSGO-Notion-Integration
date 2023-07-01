from notion import add_page
from csgobackpack import get_item_price_json


def item_price_json_to_data(response_json, id_name):
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


def add_item(db_id, id_name):
    item_price_json = get_item_price_json(id_name)
    data = item_price_json_to_data(item_price_json, id_name)
    add_page(db_id, data)
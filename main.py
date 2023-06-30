import os
import json
import requests

TOKEN = os.environ['TOKEN']
DB_ID = os.environ['DB_ID']

headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


def get_pages():
    url = f'https://api.notion.com/v1/databases/{DB_ID}/query'
    payload = {'page_size': 100}

    response = requests.post(url, json=payload, headers=headers)
    response_json = response.json()
    # print(json.dumps(response_json, indent=4))

    response_results = response_json['results']
    # print(len(response_results), response_results)

    for result in response_results:
        print(json.dumps(result, indent=4, sort_keys=True), end='\n\n')

    return response_results


get_pages()
import os
from notion import get_pages, print_pages
from csgobackpack import get_item_list, get_item_price_json
from helper import add_item

ID_CURRENT_INV = os.environ['ID_CURRENT_INV']
ID_WISHLIST = os.environ['ID_WISHLIST']
ID_ITEM_PRICES = os.environ['ID_ITEM_PRICES']

# get_pages(ID_WISHLIST)
# print_pages(ID_WISHLIST)
get_pages(ID_ITEM_PRICES)

# print(get_item_price_json('XM1014 | Watchdog (Factory New)'))
# get_item_list()

add_item(ID_ITEM_PRICES, 'XM1014 | Watchdog (Factory New)')
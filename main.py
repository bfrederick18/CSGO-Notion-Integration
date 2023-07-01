import os
from notion import get_pages, print_pages
from csgobackpack import get_item_list, get_item_price_json

ID_CURRENT_INV = os.environ['ID_CURRENT_INV']
ID_WISHLIST = os.environ['ID_WISHLIST']

# print_pages(get_pages(ID_CURRENT_INV))
get_pages(ID_WISHLIST)
print_pages(ID_WISHLIST)

get_item_price_json('XM1014 | Watchdog (Factory New)')
get_item_list()
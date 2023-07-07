import os
from helper import refresh_item

ID_CURRENT_INV = os.environ['ID_CURRENT_INV']
ID_WISHLIST = os.environ['ID_WISHLIST']
ID_ITEM_PRICES = os.environ['ID_ITEM_PRICES']

refresh_item(ID_ITEM_PRICES, 'XM1014 | Watchdog (Factory New)')
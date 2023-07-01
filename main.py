import os
from notion import get_pages, print_pages

ID_CURRENT_INV = os.environ['ID_CURRENT_INV']
ID_WISHLIST = os.environ['ID_WISHLIST']

# print_pages(get_pages(ID_CURRENT_INV))
# get_pages(ID_WISHLIST)
print_pages(ID_WISHLIST)
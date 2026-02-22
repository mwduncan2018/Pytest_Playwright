from pages.navbar_page import NavbarPage
from pages.product_page import ProductPage
from pages.product_add_page import ProductAddPage
from pages.watch_list_page import WatchListPage
from pages.watch_list_add_page import WatchListAddPage
from pages.contact_page import ContactPage

class Pages:
    def __init__(self, page):
        self.navbar = NavbarPage(page)
        self.products = ProductPage(page)
        self.product_add = ProductAddPage(page)
        self.watchlist = WatchListPage(page)
        self.watchlist_add = WatchListAddPage(page)
        self.contact = ContactPage(page)
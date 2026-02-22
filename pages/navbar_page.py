from .base_page import BasePage

class NavbarPage(BasePage):
    _PRODUCT_LIST_LINK = "[data-cy='ProductListNav']"
    _WATCH_LIST_LINK = "[data-cy='WatchListNav']"
    _CONTACT_LINK = "[data-cy='ContactNav']"

    def go_to_home(self):
        self.page.goto("/")

    def go_to_product_list(self):
        self.page.click(self._PRODUCT_LIST_LINK)

    def go_to_watch_list(self):
        self.page.click(self._WATCH_LIST_LINK)

    def go_to_contact(self):
        self.page.click(self._CONTACT_LINK)
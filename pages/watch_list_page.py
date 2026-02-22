from .base_page import BasePage

class WatchListPage(BasePage):
    _BTN_ADD_NEW_ENTRY = "text=Add To Watch List"

    def add_new_entry(self):
        self.page.click(self._BTN_ADD_NEW_ENTRY)
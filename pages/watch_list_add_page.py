from .base_page import BasePage
from models.models import EntryModel

class WatchListAddPage(BasePage):
    _INPUT_MANUFACTURER = "[data-cy='manufacturerInput']"
    _INPUT_MODEL = "[data-cy='modelInput']"
    _BTN_ADD = "[data-cy='submitButton']"

    def add_entry(self, entry: EntryModel):
        self.page.fill(self._INPUT_MANUFACTURER, entry.manufacturer)
        self.page.fill(self._INPUT_MODEL, entry.model)
        self.page.click(self._BTN_ADD)
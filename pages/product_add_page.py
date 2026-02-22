from .base_page import BasePage
from models.models import ProductModel

class ProductAddPage(BasePage):
    _INPUT_MANUFACTURER = "[data-cy='manufacturerInput']"
    _INPUT_MODEL = "[data-cy='modelInput']"
    _INPUT_PRICE = "[data-cy='priceInput']"
    _INPUT_STOCK = "[data-cy='numberInStockInput']"
    _BTN_ADD = "[data-cy='submitButton']"

    def add_product(self, product: ProductModel):
        self.page.fill(self._INPUT_MANUFACTURER, product.manufacturer)
        self.page.fill(self._INPUT_MODEL, product.model)
        self.page.fill(self._INPUT_PRICE, str(product.price))
        self.page.fill(self._INPUT_STOCK, str(product.numberInStock))
        self.page.click(self._BTN_ADD)
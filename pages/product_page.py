from .base_page import BasePage
from models.models import ProductModel

class ProductPage(BasePage):
    _BTN_ADD_NEW_PRODUCT = "text=Add New Product"
    _BTN_FUZZY_MATCHING = "#fuzzFuzz"
    _CHK_MATCH = "td:nth-child(1)"
    _CHK_FUZZY_MATCH = "td:nth-child(7)"

    def add_new_product(self):
        self.page.click(self._BTN_ADD_NEW_PRODUCT)

    def is_fuzzy_matching_enabled(self):
        return self.page.inner_text(self._BTN_FUZZY_MATCHING) == "Disable Fuzzy Matching!"

    def enable_fuzzy_matching(self):
        if not self.is_fuzzy_matching_enabled():
            self.page.click(self._BTN_FUZZY_MATCHING)

    def get_product_row(self, product: ProductModel):
        m_name = product.manufacturer
        model = product.model
        return (f"tbody tr:has(td:nth-child(2):has-text(\"{m_name}\"))"
                f":has(td:nth-child(3):has-text(\"{model}\"))")

    def is_product_a_match(self, product):
        row = self.get_product_row(product)
        status = self.page.inner_text(f"{row} >> {self._CHK_MATCH}")
        return status.strip().lower() == "true"

    def is_product_a_fuzzy_match(self, product):
        row = self.get_product_row(product)
        fuzzy_cell = f"{row} >> {self._CHK_FUZZY_MATCH}"
        # Check if the cell exists before grabbing text
        if self.page.locator(fuzzy_cell).count() > 0:
            status = self.page.inner_text(fuzzy_cell)
            return status.strip().lower() == "true"
        return False
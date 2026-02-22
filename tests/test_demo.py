import allure
import pytest
from playwright.sync_api import Page, expect, Locator
from models.models import ProductModel
from typing import Any
step: Any = allure.step

pytestmark = [pytest.mark.duncansafeproduct, pytest.mark.contact]

@allure.epic("Duncan Safe App")
@allure.feature("Demo")
class TestDemo:
    
    @allure.story("Add New Product")
    def test_add_new_product(self, page: Page):

        # Test Data
        product: ProductModel = ProductModel(manufacturer="Ibanez", model="RG", price=1800, numberInStock=2)

        # Test Steps
        with step("Open the app"):
            page.goto("/")

        with step("Navigate to the Add New Product form"):
            page.locator("[data-cy='addNewProductButton']").click()

        with step("Fill out the form"):
            page.locator("[data-cy='manufacturerInput']").fill(product.manufacturer)
            page.locator("[data-cy='modelInput']").fill(product.model)
            page.locator("[data-cy='priceInput']").fill(str(product.price))
            page.locator("[data-cy='numberInStockInput']").fill(str(product.numberInStock))

        with step("Submit the form"):
            page.locator("[data-cy='submitButton']").click()

        with step("Verify the product appears in the products table"):
            rows: Locator = page.locator("table tr")
            target_row: Locator = rows.filter(has_text=product.manufacturer).filter(has_text=product.model)
            expect(target_row).to_be_visible()
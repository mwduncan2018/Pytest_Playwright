import allure
import pytest
from pages.pages import Pages
from models.models import ProductModel, EntryModel
from typing import Any
step: Any = allure.step

pytestmark = [pytest.mark.duncansafeproduct, pytest.mark.standardMatching]

@allure.epic("Duncan Safe App")
@allure.feature("Standard Matching")
class TestStandardMatching:

    @allure.story("Manufacturer match, model match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Porsche", "Cayenne", "Porsche", "Cayenne"),
        ("Porsche", "Boxster", "Porsche", "Boxster"),
    ])
    def test_manufacturer_match_model_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=50000, numberInStock=1)
        entry: EntryModel = EntryModel(manufacturer=entry_manufacturer, model=entry_model)

        with step(f"A product is added: {product_manufacturer} {product_model}"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_product_list()
            pages.products.add_new_product()
            pages.product_add.add_product(product)

        with step(f"An entry is added to watch list: {entry_manufacturer} {entry_model}"):
            pages.navbar.go_to_watch_list()
            pages.watchlist.add_new_entry()
            pages.watchlist_add.add_entry(entry)

        with step("Standard matching is confirmed"):
            pages.navbar.go_to_product_list()
            assert pages.products.is_product_a_match(product) is True

    @allure.story("Manufacturer no match, model no match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Porsche", "911", "Toyota", "Corolla"),
        ("Porsche", "Cayman", "Toyota", "Camry"),
    ])
    def test_manufacturer_no_match_model_no_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=40000, numberInStock=2)
        entry: EntryModel = EntryModel(manufacturer=entry_manufacturer, model=entry_model)

        with step(f"A product is added: {product_manufacturer} {product_model}"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_product_list()
            pages.products.add_new_product()
            pages.product_add.add_product(product)

        with step(f"An entry is added to watch list: {entry_manufacturer} {entry_model}"):
            pages.navbar.go_to_watch_list()
            pages.watchlist.add_new_entry()
            pages.watchlist_add.add_entry(entry)

        with step("Verify the product is NOT a match"):
            pages.navbar.go_to_product_list()
            assert pages.products.is_product_a_match(product) is False

    @allure.story("Manufacturer match, model no match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Porsche", "Taycan", "Porsche", "Panamera"),
        ("Toyota", "Land Cruiser", "Toyota", "Supra"),
    ])
    def test_manufacturer_match_model_no_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=40000, numberInStock=2)
        entry: EntryModel = EntryModel(manufacturer=entry_manufacturer, model=entry_model)

        with step(f"A product is added: {product_manufacturer} {product_model}"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_product_list()
            pages.products.add_new_product()
            pages.product_add.add_product(product)

        with step(f"An entry is added to watch list: {entry_manufacturer} {entry_model}"):
            pages.navbar.go_to_watch_list()
            pages.watchlist.add_new_entry()
            pages.watchlist_add.add_entry(entry)

        with step("Verify the product is NOT a match"):
            pages.navbar.go_to_product_list()
            assert pages.products.is_product_a_match(product) is False

    @allure.story("Manufacturer no match, model match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("BMW", "Sports Car", "Tesla", "Sports Car"),
        ("Honda", "SUV", "General Motors", "SUV"),
    ])
    def test_manufacturer_no_match_model_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=40000, numberInStock=2)
        entry: EntryModel = EntryModel(manufacturer=entry_manufacturer, model=entry_model)

        with step(f"A product is added: {product_manufacturer} {product_model}"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_product_list()
            pages.products.add_new_product()
            pages.product_add.add_product(product)

        with step(f"An entry is added to watch list: {entry_manufacturer} {entry_model}"):
            pages.navbar.go_to_watch_list()
            pages.watchlist.add_new_entry()
            pages.watchlist_add.add_entry(entry)

        with step("Verify the product is not a match"):
            pages.navbar.go_to_product_list()
            assert pages.products.is_product_a_match(product) is False
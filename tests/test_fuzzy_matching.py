import allure
import pytest
from playwright.sync_api import Page
from pages.pages import Pages
from models.models import ProductModel, EntryModel
from typing import Any, ContextManager
step: Any = allure.step

pytestmark = [pytest.mark.duncansafeproduct, pytest.mark.fuzzyMatching]

@allure.epic("Duncan Safe App")
@allure.feature("Fuzzy Matching")
class TestFuzzyMatching:

    @allure.story("Manufacturer match, model match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Wendys", "Taco Salad", "Wendys", "Taco Salad"),
        ("Wendys", "Apple Pecan Salad", "Wendys", "Apple Pecan Salad"),
        ("Wendys", "Jalapeno Popper Salad", "Wendys", "Jalapeno Popper Salad"),
        ("Wendys", "Bourbon Bacon Cheeseburger", "Wendys", "Bourbon Bacon Cheeseburger"),
    ])
    def test_manufacturer_match_model_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        # Test Title
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        # Test Data
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=10, numberInStock=5)
        entry: EntryModel = EntryModel(manufacturer=entry_manufacturer, model=entry_model)

        # Test Steps
        with step(f"A product is added: {product_manufacturer} {product_model}"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_product_list()
            pages.products.add_new_product()
            pages.product_add.add_product(product)

        with step(f"An entry is added to watch list: {entry_manufacturer} {entry_model}"):
            pages.navbar.go_to_watch_list()
            pages.watchlist.add_new_entry()
            pages.watchlist_add.add_entry(entry)

        with step("Fuzzy matching is enabled"):
            pages.navbar.go_to_product_list()
            pages.products.enable_fuzzy_matching()

        with step(f"The product should be a standard match"):
            assert pages.products.is_product_a_match(product) is True


    @allure.story("Manufacturer no match, model no match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Taco Bell", "Grilled Cheese Burrito", "Burger King", "Impossible Whopper"),
        ("Taco Bell", "Veggie Burrito Supreme", "Burger King", "Texas Double Whopper"),
    ])
    def test_manufacturer_no_match_model_no_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=10, numberInStock=5)
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

        with step("Fuzzy matching is enabled"):
            pages.navbar.go_to_product_list()
            pages.products.enable_fuzzy_matching()

        with step(f"The product should not be a match"):
            assert pages.products.is_product_a_match(product) is False
            assert pages.products.is_product_a_fuzzy_match(product) is False


    @allure.story("Manufacturer match, model no match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Burger King", "Italian Original Chicken", "Burger King", "Four nuggets"),
        ("Burger King", "Spicy Chicken Sandwich", "Burger King", "Chicken Deluxe Sandwich"),
    ])
    def test_manufacturer_match_model_no_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=10, numberInStock=5)
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

        with step("Fuzzy matching is enabled"):
            pages.navbar.go_to_product_list()
            pages.products.enable_fuzzy_matching()

        with step(f"The product should be a fuzzy match"):
            assert pages.products.is_product_a_fuzzy_match(product) is True


    @allure.story("Manufacturer no match, model match")
    @pytest.mark.parametrize("product_manufacturer, product_model, entry_manufacturer, entry_model", [
        ("Popeyes", "Chicken Sandwich", "Burger King", "Chicken Sandwich"),
        ("McDonalds", "Hamburger", "Sonic", "Hamburger"),
    ])
    def test_manufacturer_no_match_model_match(self, pages: Pages, product_manufacturer: str, product_model: str, entry_manufacturer: str, entry_model: str):
        allure.dynamic.title(f"Product: {product_manufacturer} {product_model}, Model: {entry_manufacturer} {entry_model}")
        
        product: ProductModel = ProductModel(manufacturer=product_manufacturer, model=product_model, price=10, numberInStock=5)
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

        with step("Fuzzy matching is enabled"):
            pages.navbar.go_to_product_list()
            pages.products.enable_fuzzy_matching()

        with step(f"The product should be a fuzzy match"):
            assert pages.products.is_product_a_fuzzy_match(product) is True
import allure
import pytest
from pages.pages import Pages
from playwright.sync_api import expect
from typing import Any
step: Any = allure.step

pytestmark = [pytest.mark.duncansafeproduct, pytest.mark.contact]

@allure.epic("Duncan Safe App")
@allure.feature("Contact")
class TestContact:

    @allure.story("Duncan safe product")
    def test_duncan_safe_product_footer(self, pages: Pages):
        allure.dynamic.title("Verify Footer Text: (Duncan Safe Product!)")

        expected_footer_text: str = "Duncan Safe Product"
        
        with step("The Contact page is viewed"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_contact()

        with step("The expected text should display in the footer"):
            assert expected_footer_text in pages.contact.get_footer_text()

    @allure.story("GitHub link")
    def test_github_link_provided(self, pages: Pages):
        allure.dynamic.title("Verify GitHub Link")
        
        expected_url: str = "https://github.com/mwduncan2018"

        with step("The Contact page is viewed"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_contact()

        with step(f"A GitHub link should be provided"):
            assert expected_url in pages.contact.get_github_href()

    @allure.story("Technical skills are displayed")
    @pytest.mark.parametrize("skill", [
        "SpecFlow", "Cucumber", "Selenium", "Appium", "Docker", "Eggplant", "Python",
        "C#", "pytest-bdd", "Java", "Appium", "Cypress", "Playwright", "TypeScript"
    ])
    def test_technical_skills_display(self, pages: Pages, skill: str):
        allure.dynamic.title(f"Verify Skill Listed: {skill}")
        
        with step("The Contact page is viewed"):
            pages.navbar.go_to_home()
            pages.navbar.go_to_contact()

        with step(f"The skill '{skill}' should be listed"):
            assert skill in pages.contact.get_all_skills()

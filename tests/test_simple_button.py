import allure
from playwright.sync_api import Page
from pages.simple_button_page import SimpleButtonPage


@allure.feature("Buttons")
@allure.story("Simple Button")
@allure.title("Check that simple button exists")
def test_simple_button_exists(page: Page):
    simple_button_page = SimpleButtonPage(page)
    simple_button_page.open()
    simple_button_page.check_button_exists()


@allure.feature("Buttons")
@allure.story("Simple Button")
@allure.title("Click simple button and check result")
def test_simple_button_click(page: Page):
    simple_button_page = SimpleButtonPage(page)
    simple_button_page.open()
    simple_button_page.click_button()
    simple_button_page.check_result_text_is_("Submitted")

import allure
from playwright.sync_api import Page
from pages.iframe_page import IFramePage


@allure.feature("IFrame")
@allure.story("Check iframe contains Album example")
def test_iframe_contains_album_example(page: Page):
    iframe_page = IFramePage(page)
    iframe_page.open()
    iframe_page.check_iframe_exists()
    iframe_page.check_iframe_contains_title()

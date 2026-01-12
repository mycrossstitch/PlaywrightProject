import allure
from playwright.sync_api import Page
from pages.like_a_button_page import LikeAButtonPage


@allure.feature("Buttons")
@allure.story("Like a Button")
@allure.title("Check that 'Like a Button' exists")
def test_like_a_button_exists(page: Page):
    like_a_button_page = LikeAButtonPage(page)
    like_a_button_page.open()
    like_a_button_page.check_button_exists()


@allure.feature("Buttons")
@allure.story("Like a Button")
@allure.title("Click 'Like a Button' and check result")
def test_like_a_button_click(page: Page):
    like_a_button_page = LikeAButtonPage(page)
    like_a_button_page.open()
    like_a_button_page.click_button()
    like_a_button_page.check_result_text_is_("Submitted")

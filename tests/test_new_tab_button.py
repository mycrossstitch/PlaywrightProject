import allure
from playwright.sync_api import Page
from pages.new_tab_button_page import NewTabButtonPage


@allure.feature("New Tab")
@allure.story("Button")
@allure.title("The button should open the correct URL in a new tab")
def test_buton_open_url(page: Page):
    new_tab_button_page = NewTabButtonPage(page)
    new_tab_button_page.open()
    new_tab_button_page.click_and_wait_new_tab()
    new_tab_button_page.check_new_tab_url()


@allure.feature("New Tab")
@allure.story("Button")
@allure.title("Clicking the button opens a new tab")
def test_button_opens_new_tab(page: Page):
    new_tab_button_page = NewTabButtonPage(page)
    new_tab_button_page.open()
    new_tab_button_page.click_and_wait_new_tab()
    new_tab_button_page.check_new_tab_opened()


@allure.feature("New Tab")
@allure.story("Button")
@allure.title("New tab shows correct result text after button click")
def test_check_new_tab_result(page: Page):
    new_tab_button_page = NewTabButtonPage(page)
    new_tab_button_page.open()
    new_tab_button_page.click_and_wait_new_tab()
    new_tab_button_page.check_new_tab_result_text_is_("I am a new page in a new tab")

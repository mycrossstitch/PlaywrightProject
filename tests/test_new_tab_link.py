import allure
from playwright.sync_api import Page
from pages.new_tab_link_page import NewTabLinkPage


@allure.feature("New Tab")
@allure.story("Link")
@allure.title("The link should open the correct URL in a new tab")
def test_link_open_url(page: Page):
    new_tab_link_page = NewTabLinkPage(page)
    new_tab_link_page.open()
    new_tab_link_page.click_and_wait_new_tab()
    new_tab_link_page.check_new_tab_url()


@allure.feature("New Tab")
@allure.story("Link")
@allure.title("Clicking the link opens a new tab")
def test_link_opens_new_tab(page: Page):
    new_tab_link_page = NewTabLinkPage(page)
    new_tab_link_page.open()
    new_tab_link_page.click_and_wait_new_tab()
    new_tab_link_page.check_new_tab_opened()


@allure.feature("New Tab")
@allure.story("Link")
@allure.title("New tab shows correct result text after link click")
def test_check_new_tab_result(page: Page):
    new_tab_link_page = NewTabLinkPage(page)
    new_tab_link_page.open()
    new_tab_link_page.click_and_wait_new_tab()
    new_tab_link_page.check_new_tab_result_text_is_("I am a new page in a new tab")

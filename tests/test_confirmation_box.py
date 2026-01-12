import allure
from playwright.sync_api import Page
from pages.confirmation_box_page import ConfirmationBoxPage


@allure.feature("Alerts")
@allure.story("Confirmation Box")
@allure.title("Check button exists")
def test_check_button_exists(page: Page):
    confirm_page = ConfirmationBoxPage(page)
    confirm_page.open()
    confirm_page.check_button_exists()

@allure.feature("Alerts")
@allure.story("Confirmation Box")
@allure.title("Clicking confirmation button shows alert with correct text")
def test_confirmation_box_text(page: Page):
    confirm_page = ConfirmationBoxPage(page)
    confirm_page.open()
    confirm_page.check_alert_text("Select Ok or Cancel")
    confirm_page.click_button()


@allure.feature("Alerts")
@allure.story("Confirmation Box")
@allure.title("Click OK on confirmation shows correct result")
def test_confirmation_box_ok(page: Page):
    confirm_page = ConfirmationBoxPage(page)
    confirm_page.open()
    confirm_page.accept_alert()
    confirm_page.click_button()
    confirm_page.check_result_text("Ok")

@allure.feature("Alerts")
@allure.story("Confirmation Box")
@allure.title("Click Cancel on confirmation shows correct result")
def test_confirmation_box_cancel(page: Page):
    confirm_page = ConfirmationBoxPage(page)
    confirm_page.open()
    confirm_page.dismiss_alert()
    confirm_page.click_button()
    confirm_page.check_result_text("Cancel")

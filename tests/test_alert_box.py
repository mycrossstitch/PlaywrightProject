import allure
from playwright.sync_api import Page
from pages.alert_box_page import AlertBoxPage


@allure.feature("Alerts")
@allure.story("Alert Box")
@allure.title("Check button exists")
def test_check_button_exists(page: Page):
    alert_box_page = AlertBoxPage(page)
    alert_box_page.open()
    alert_box_page.check_button_exists()


@allure.feature("Alerts")
@allure.story("Alert Box")
@allure.title("Clicking alert button shows alert with correct text")
def test_alert_box_text(page: Page):
    alert_box_page = AlertBoxPage(page)
    alert_box_page.open()
    alert_box_page.check_alert_text("I am an alert!")
    alert_box_page.click_button()


@allure.feature("Alerts")
@allure.story("Alert Box")
@allure.title("Alert Box closes after clicking OK")
def test_alert_box_accept(page: Page):
    alert_box_page = AlertBoxPage(page)
    alert_box_page.open()
    alert_box_page.accept_alert()
    alert_box_page.click_button()
    alert_box_page.check_button_exists()

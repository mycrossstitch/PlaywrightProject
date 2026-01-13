import allure
from playwright.sync_api import Page, expect, Dialog
from base.base_page import BasePage


class BaseAlertPage(BasePage):
    BUTTON = ".a-button"

    # ---------------- Actions ----------------
    @allure.step("Click on the alert button")
    def click_button(self):
        button = self.page.locator(self.BUTTON)
        button.click()

    @allure.step("Accept the alert")
    def accept_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    @allure.step("Dismiss the alert")
    def dismiss_alert(self):
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    @allure.step("Send text '{text}' to the alert and accept")
    def send_text_to_alert(self, text: str):
        self.page.once("dialog", lambda dialog: dialog.accept(prompt_text=text))

    # ---------------- Assertions ----------------

    @allure.step("Check that the submit button exists")
    def check_button_exists(self):
        button = self.page.locator(self.BUTTON)
        expect(button).to_be_visible()

    @allure.step("Check that the alert displays text '{expected_text}'")
    def check_alert_text(self, expected_text: str):
        def accept_alert(alert: Dialog):
            assert (
                alert.message == expected_text
            ), f"Expected alert text '{expected_text}', got '{alert.message}'"
            alert.accept()

        self.page.on("dialog", accept_alert)
